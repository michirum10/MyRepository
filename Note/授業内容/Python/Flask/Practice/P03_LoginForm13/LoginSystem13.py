from flask import Blueprint, render_template, request, session, redirect, url_for
from flask.views import MethodView

login_bp = Blueprint("LoginSystem13", __name__, url_prefix="/LoginSystem13")

# loginのルート
class LoginSystem(MethodView):
    def get(self):
        return render_template("13/pages/login.html")
    
    def post(self):
        id = request.form.get("id")
        pw = request.form.get("pw")
        # idとpwが一致するかどうかの確認
        if id == "id" and pw == "pass":
            session['flag'] = True
            session['id'] = id
            return redirect(url_for('LoginSystem13.success'))
        else:
            msg = 'エラー：IDまたはパスワードが間違っています。'
            return render_template('13/pages/login.html', msg=msg)

# successのルート
class Success(MethodView):
    def get(self):
        # ユーザーがログインしているかどうかを確認
        if 'flag' in session and session['flag']:
            id = session.get('id')
            # 'id' がセッションに存在しない場合は Noneを返す
            if id is None:
                return redirect(url_for('LoginSystem13.login'))
            
            msg = 'ログインに成功しました！'
            title = 'ログイン成功'
            return render_template("13/pages/success.html", id=id, pw="••••••••", msg=msg, title=title)
        else:
            return redirect(url_for('LoginSystem13.login'))

# /loginをブループリントに登録
login_bp.add_url_rule("/login", view_func=LoginSystem.as_view("login"))

# /successをブループリントに登録
login_bp.add_url_rule("/success", view_func=Success.as_view("success"))
