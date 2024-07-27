from flask import Flask, render_template,request,session

# インスタンス生成
app = Flask(__name__)
# セッションを使うための鍵
app.secret_key = b"hit"

@app.route("/",methods=["GET","POST"])
def index():
    msg = request.args.get("msg")
    print(msg)
    if msg:
        session["msg"] = msg
    else:
        msg = session.get(msg)
    return render_template("index.html",msg = msg)

if __name__ == "__main__":
    # デバッグモード
    app.debug = True
    # ホストとポートの指定
    # WEBサーバー実行
    app.run(host="0.0.0.0",port=5002)