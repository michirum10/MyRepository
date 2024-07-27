from flask import Flask, render_template,request,abort

# インスタンス生成
app = Flask(__name__)

# methods=["GET"]["POST"]は書かなくても動作する。
@app.route("/",methods=["GET","POST"])
def index():
    methodName = request.method
    if methodName == "GET":
        # getの値を取得できる。
        msg = request.args.get("msg")
    elif methodName == "POST":
        # postの値を取得できる。
        msg = request.form.get("msg")
    else:
        abort(404)  # わざとエラーに飛ばす
    return render_template("index.html",msg = msg)


if __name__ == "__main__":
    # デバッグモード
    app.debug = True
    # ホストとポートの指定
    # WEBサーバー実行
    app.run(host="0.0.0.0",port=5002)