# 簡易電卓

# 1. 値は２入力して加算処理を行ってください。
# 2. ポート番号8080
# 3. ルートで値２つを入力し
# 4. /resultで答えを出力してください。


from flask import Flask, render_template, request

# インスタンス生成
app = Flask(__name__)

@app.route("/")
def index():
    # レンダーテンプレート
    return render_template("/index.html",title="ホーム")

# 足し算の結果を表示
@app.route("/result", methods=["GET"])
def result():
    try:
        e1 = int(request.args.get("e1"))
        e2 = int(request.args.get("e2"))
        result = e1 + e2
    except (TypeError, ValueError):
        result = "無効な入力です"
    return render_template("result.html", title="結果", result=result)

if __name__ == "__main__":
    # デバッグモード
    app.debug = True
    # ホストとポートの指定
    # WEBサーバー実行
    app.run(host="0.0.0.0",port=8080)
