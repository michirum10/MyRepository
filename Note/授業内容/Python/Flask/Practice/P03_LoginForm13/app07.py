from flask import Flask, Blueprint, request, render_template, redirect, url_for

# インスタンス作成
app = Flask(__name__)

# Blueprintの登録
from app207 import app207
app.register_blueprint(app207)


@app.route('/')
def index():
    return render_template('07index.html')



if __name__ == "__main__":
    # デバッグモード
    app.debug = True
    # ホストとポートの指定
    # WEBサーバー実行
    app.run(host="0.0.0.0",port=8080)
