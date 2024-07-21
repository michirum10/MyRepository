# 簡易電卓

# 1. 値は２入力して加算処理を行ってください。
# 2. ポート番号8080
# 3. ルートで値２つを入力し
# 4. /resultで答えを出力してください。


from flask import Flask, render_template, request

# インスタンス生成
app = Flask(__name__)

@app.route("/" ,methods=["GET", "POST"])
# methods=["GET", "POST"]書いておくと良いらしい
# GET : データの取得やページの表示
# POST: データの送信や処理
def index():
    # レンダーテンプレート
    return render_template("/index.html",title="簡易電卓", e1='', e2='')
# e1='', e2=''の初期値指定しておくと良いらしい


# 計算する関数
def calc(e1, e2, op):
    try:
    # 初期化
        num1 = int(e1)  
        num2 = int(e2)  
        # 計算分岐
        if op == 'add':
            return num1 + num2
        elif op == 'sub':
            return num1 - num2
        elif op == 'mul':
            return num1 * num2
        elif op == 'div':
            if num2 == 0:
                return "ゼロでは割れません！"
            return num1 / num2
        else:
            return "無効な操作です"
    except (TypeError, ValueError):
        return "無効な入力です"


# 結果を表示する関数
@app.route("/result", methods=["GET"])
# methods=["GET"]は省略できるが書いた方が良い
def result():
    e1 = request.args.get("e1")
    e2 = request.args.get("e2")
    op = request.args.get("op")
    # 計算結果
    result = calc(e1, e2, op)
    return render_template("result.html", title="計算結果", e1=e1, e2=e2, result=result, op=op)
# 引数の順番注意

if __name__ == "__main__":
    # デバッグモード
    app.debug = True
    # ホストとポートの指定
    # WEBサーバー実行
    app.run(host="0.0.0.0",port=8080)

#     # GETパラメータ(おまけ)
# # http://localhost:5000/get?id=100
# @app.route("/get")
# def get():
#     id = request.args.get("id")
#     return f'ページ{id}<a href="/">ホームへ戻る</a>'

