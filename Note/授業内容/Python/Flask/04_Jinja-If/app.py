from flask import Flask, render_template, request

# インスタンス生成
app = Flask(__name__)

@app.route("/")
def index():
    # レンダーテンプレート
    return render_template("index.html",title="ホーム")

@app.route("/next/<var>")
def next(var):
    return render_template("index.html",title="next",msg=var)

if __name__ == "__main__":
    # デバッグモード
    app.debug = True
    # ホストとポートの指定
    # WEBサーバー実行
    app.run(host="0.0.0.0",port=5000)
    
    
# ルーティングは自由に変更できる
#  メソッドは絶対変えない