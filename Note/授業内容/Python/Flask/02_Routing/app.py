from flask import Flask, request

# インスタンス生成
app = Flask(__name__)

# ルーティング『/』にアクセスされたときの処理
@app.route("/")
# ルーティングの条件で実行される関数
def hello_world():
    return '<h1>Hello2</h1>Flask!!!!!!<a href="/page">ページへ進む</a>'

# ルーティング『/page』にアクセスされたときの処理

@app.route("/page")
def page():
    return 'ページ<a href="/">ホームへ戻る</a>'

# ルーティング『/pages』にアクセスされたときの処理
# http://localhost:5000/pages/100
# <id>はダイナミックルーティング
# Pythonの関数の引数と連動する。
# あたかもいくつものページが存在するように見える。
@app.route("/pages/<id>")
def pages(id):  # 引数揃える
    return f'ページ{id}<a href="/">ホームへ戻る</a>'

# GETパラメータ(おまけ)
# http://localhost:5000/get?id=100
@app.route("/get")
def get():
    id = request.args.get("id")
    return f'ページ{id}<a href="/">ホームへ戻る</a>'


if __name__ == "__main__":
    # デバッグモード
    app.debug = True
    # ホストとポートの指定
    # WEBサーバー実行
    app.run(host="0.0.0.0",port=5000)