from flask import Flask, render_template,request

# インスタンス生成
app = Flask(__name__)

# methods=["GET"]は書かなくても動作する。
@app.route("/",methods=["GET"])
def get():
    # getの値を取得できる。
    msg = request.args.get("msg")
    return render_template("index.html",msg = msg)

@app.route("/",methods=["POST"])
def post():
    msg = request.form.get("msg")
    return render_template("index.html",msg = msg)

if __name__ == "__main__":
    # デバッグモード
    app.debug = True
    # ホストとポートの指定
    # WEBサーバー実行
    app.run(host="0.0.0.0",port=5001)