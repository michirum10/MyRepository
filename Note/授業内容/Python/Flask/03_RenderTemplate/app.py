from flask import Flask, render_template, request

# インスタンス生成
app = Flask(__name__)

# ルーティング『/』にアクセスされたときの処理
@app.route("/")
# ルーティングの条件で実行される関数
# TOPページを表示
def hello_world():
    return render_template("index.html")  # 第一引数にHTMLファイル名
# ルーティング『/page』にアクセスされたときの処理

@app.route("/page")
def page():
    return render_template("page.html",id="abc")

# ルーティング『/pages』にアクセスされたときの処理
# http://localhost:5000/pages/100
# <id>はダイナミックルーティング
# Pythonの関数の引数と連動する。
# あたかもいくつものページが存在するように見える。
# ダイナミックルーティング<id>
@app.route("/pages/<id>")
def pages(id):  # 引数揃える
    return render_template("page.html",id=id)
# 右が引数と同じid


# GETパラメータ(おまけ)
# http://localhost:5000/get?id=100
@app.route("/get")
def get():
    id = request.args.get("id")
    return render_template("page.html",id=id)


if __name__ == "__main__":
    # デバッグモード
    app.debug = True
    # ホストとポートの指定
    # WEBサーバー実行
    app.run(host="0.0.0.0",port=5000)
    
    
# ルーティングは自由に変更できる
#  メソッドは絶対変えない