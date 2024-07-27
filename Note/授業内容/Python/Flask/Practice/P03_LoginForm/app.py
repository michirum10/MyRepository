from flask import Flask,render_template, request
from flask.views import MethodView
# flask-loginからLoginManagerをimport
from flask_login import LoginManager

# インスタンス生成(appを初期化)
app = Flask(__name__)
# LoginManagerの起動
login = LoginManager(app) #extensionを起動させる際の標準的な記述
class LoginSystem(MethodView):
    # getでのアクセス時
    def get(self):
        return render_template("index.html")
    
    # postでのアクセス時
    def post(self):
        id = request.form.get("id")
        pw = request.form.get("pw")
        return render_template("success.html",id=id,pw=pw)

app.add_url_rule("/",view_func=LoginSystem.as_view("login"))

if __name__ == "__main__":
    # デバッグモード
    app.debug = True
    # ホストとポートの指定
    # WEBサーバー実行
    app.run(host="0.0.0.0",port=5002)