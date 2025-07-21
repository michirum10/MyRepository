import os
import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import datetime
import time
from keep_alive import keep_alive

PRIVATE_TOKEN = os.environ['PRIVATE_TOKEN']
SENDER_EMAIL = os.environ['SENDER_EMAIL']
SENDER_PASSWORD = os.environ['SENDER_PASSWORD']
RECEIVER_EMAIL = os.environ['RECEIVER_EMAIL']
SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']

headers = {"Authorization": f"Bearer {PRIVATE_TOKEN}"}
ORGANIZER_ID = "107252340551"

# --- 最新の10件イベントID取得 ---
def get_latest_10_event_ids(organizer_id):
    url = f"https://www.eventbriteapi.com/v3/organizers/{organizer_id}/events/"
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            events = data.get('events', [])
            # 開催日時順で新しい順にソート（なければcreated順）
            events_sorted = sorted(
                events,
                key=lambda x: x.get('start', {}).get('local', x.get('created', '')),
                reverse=True
            )
            event_ids = [
                str(int(float(event['id'])))
                for event in events_sorted[:10]
            ]
            return event_ids
        else:
            print(f"イベント一覧取得エラー: {response.status_code}")
            return []
    except Exception as e:
        print(f"イベント一覧取得中にエラー: {e}")
        return []

# 以下、既存の空席チェック、通知関数は変更不要

if __name__ == "__main__":
    print("イタリア館監視システム開始")
    keep_alive()
    last_availability_status = {}
    try:
        while True:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\n[{timestamp}] 監視サイクル開始")

            # 最新の10イベントIDのみ取得
            current_event_ids = get_latest_10_event_ids(ORGANIZER_ID)
            print(f"監視対象イベント数: {len(current_event_ids)}件")
            print(f"イベントID一覧: {current_event_ids}")

            for event_id in current_event_ids:
                event_info = check_event_availability(event_id)
                if event_info:
                    print(
                        f"イベント: {event_info['event_name']} - 空席数: {event_info['available_count']}"
                    )
                    last_count = last_availability_status.get(event_id, 0)
                    if event_info['available_count'] > 0 and last_count == 0:
                        print(
                            f"空席発生通知: {event_info['event_name']} - {event_info['available_count']}件"
                        )
                        send_notification(event_info)
                    last_availability_status[event_id] = event_info['available_count']
                else:
                    print(f"イベント{event_id}の情報取得失敗")
            print("監視完了")
            time.sleep(10)
    except KeyboardInterrupt:
        print("手動で監視を停止しました。")
    except Exception as e:
        print(f"致命的なエラーによりプログラムが停止します: {e}")
        print("コンテナを再起動します。")
        os.system("kill 1")
