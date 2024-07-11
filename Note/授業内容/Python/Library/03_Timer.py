# =============
# タイマー
# =============
from datetime import datetime
from threading import Timer
import time

# 現在時刻を取得
date01 = datetime.now()
# そのまま表示
print(date01)
# フォーマット設定して表示
# %Y年%m月%d日 %H時%M分%S秒
timeStr01 = date01.strftime("%Y/%m/%d %H:%M:%S")
print(timeStr01)

#======
# 遅延実行
#======

# 遅延実行(コールバック関数)
def dutation():
    print("遅延実行されました。")
    # 現在時刻を取得
    date02 = datetime.now()
    # ５秒後に実行されたか確認するためにタイマーを起動
    timeStr02 = date02.strftime("%Y/%m/%d %H:%M:%S")
    print(timeStr02)

# 遅延実行
# 第一引数に何秒後
# 第２引数にコールバック関数
thread01 = Timer(5, dutation)

# 開始
thread01.start()

#======
# 定期実行
#======

# フラグ立て無いとずっとループしてしまう
# 定期実行終了フラグ
stopFlag = False

# 定期実行(コールバック関数)
def tick():
    print("遅延実行されました。")
    # 現在時刻を取得
    date03 = datetime.now()
    # ５秒後に実行されたか確認するためにタイマーを起動
    timeStr03 = date03.strftime("%Y/%m/%d %H:%M:%S")
    print(timeStr03)
    
    # Trueになるまで実行
    if not stopFlag:
        # 定期実行関数の再帰登録(自分の関数tickの中で自分tickを呼び出す)
        thread03 = Timer(1,tick)
        # 開始
        thread03.start()

# 定期実行
# 設定
thread02 = Timer(1,dutation)
# 開始
thread02.start()

# 10秒間強制的にプログラムを一時停止
time.sleep(10)

# 定期実行終了フラグ
stopFlag = True