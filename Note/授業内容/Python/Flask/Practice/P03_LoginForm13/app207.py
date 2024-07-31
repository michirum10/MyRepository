from flask import Flask,render_template,Blueprint,request,redirect,url_for

# Blueprintの名称：LOGIN
# モジュール名：app2
# URL：/LoginSystem
app207 = Blueprint("LOGIN",__name__,url_prefix="/LoginSystem07")

# ユーザー情報
user_id = 1234
user_pw = 1111

# MethodBase
from flask.views import MethodView
class Login(MethodView):
    def get(self):
        return render_template("7/07login.html")

    def post(self):
        id = request.form.get('id')
        pw = request.form.get('pw')
        if id == str(user_id) and pw == str(user_pw):
            return redirect(url_for('LOGIN.success'))
        else:
            return render_template("7/07login.html", msg="ログイン失敗")
        
app207.add_url_rule('/login', view_func=Login.as_view('login'))


# successページへ
@app207.route('/success')
def success():
    return render_template('7/07success.html')