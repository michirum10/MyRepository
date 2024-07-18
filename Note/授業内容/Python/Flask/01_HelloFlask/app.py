from flask import Flask

# インスタンス生成
app = Flask(__name__)

# ルーティング「/」にアクセスされたときの処理
@app.route("/")
# ルーティングの条件で実行される関数
def hello_world():
    return "<h1>HELLO</h1> Flask！"

# 毎回ターミナルで実行する場合
# ターミナルで: flask --app app runで実行
# ポートエラー出たら: flask --app app run -p 5001 でポート番号を変える
# 外部公開する場合：flask --app app run -h 0.0.0.0 -p 5001

# http://127.0.0.1:5001(localhost:5001) をクリックでページに飛ぶ「HELLO Flask！！」
# ipconfigで 自分のIPv4アドレスだす

# ゴミ箱はターミナルを終了させるときに使う
# ✕ボタンで閉じる
# ctrl + @でターミナル開く
# エラーが出たときは落ちるので実行しない
# 変更を保存してページを更新すると反映される
# 自動保存だとエラーが反映されたまま実行されるので注意

# 上のやつ毎回書かなくても▷の実行ボタンで動かせるように
if __name__ == "__main__":
    # Pythonで実行した時に動作
    # デバッグモード
    app.debug = True
    # ホストとポートの指定
    # WEBサーバー実行
    app.run(host="0.0.0.0",port=5001)
    # コマンドで実行の場合はターミナルで
    # flask --app app run -h 0.0.0.0 -p 5001 --debugger --reload 

# 一行にまとめる
# if __name__ == "__main__":
#     app.run(host="0.0.0.0",port=5001,debug=True)