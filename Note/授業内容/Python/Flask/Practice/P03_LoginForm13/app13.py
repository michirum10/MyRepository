from flask import Flask, render_template
# blueprintをimport
from LoginSystem13 import login_bp

# インスタンス生成(appを初期化)
app = Flask(__name__, template_folder='templates')

# 各Blueprintをインポート
from app207 import app207
# Blueprintの登録
app.register_blueprint(app207)
from login_system import login_system_blueprint
# Blueprintの登録（URLプレフィックスを指定）
app.register_blueprint(login_system_blueprint, url_prefix='/LoginSystem')

# セッションを使うための鍵
app.secret_key = b"hit"

# Blueprintの登録
app.register_blueprint(login_bp, url_prefix='/LoginSystem13')
# indexの表示
@app.route("/") 
def index():
    return render_template("13/pages/index.html", msg="WELCOME！")



if __name__ == "__main__":
    # デバッグモード
    app.debug = True
    # ホストとポートの指定
    # WEBサーバー実行
    app.run(host="0.0.0.0", port=8080)
    
# myproject/
# ├── 07nakamura
# │   └── app207.py
# ├── 12mita
# │   └── login_system.py
# ├── app.py
# ├── LoginSystem.py
# ├── forms.py
# ├── config.py
# └── templates/
#     └── 13/
#         └── pages/
#             ├── login.html
#             └── success.html
