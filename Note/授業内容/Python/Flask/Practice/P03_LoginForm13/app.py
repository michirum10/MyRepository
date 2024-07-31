from flask import Flask, render_template
from login_system import login_system_blueprint  # 同じディレクトリにある場合

# Flaskアプリケーションの作成
app = Flask(__name__)

# Blueprintの登録（URLプレフィックスを指定）
app.register_blueprint(login_system_blueprint, url_prefix='/LoginSystem')

# ルートURLにアクセスしたときの処理
@app.route("/")
def index():
    return render_template("12/index.html")

# アプリケーションのエントリーポイント
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
