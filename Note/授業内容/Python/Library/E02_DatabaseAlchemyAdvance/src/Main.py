# =============
# 自作ライブラリの利用とCUIアプリケーション
# =============
import Logic
from DatabaseManager import db,ses

print("DBシステムを開始しました。")

# 無限ループ
while True:
    cmd = input("[1]追加[2]確認[q]終了\n>")
    if cmd == "1":# データの追加
        print("データを追加します。")
        Logic.add(ses)
    elif cmd == "2":# データの確認
        print("データを確認します。")
        Logic.getAll(ses)
    elif cmd == "q" or cmd == "Q":# システムの終了
        break

# DBの終了処理
db.dispose()
print("システムが終了しました。")
