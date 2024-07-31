from flask import Blueprint, request, render_template, redirect, url_for

# Blueprintのインスタンスを作成
login_system_blueprint = Blueprint('login_system', __name__)

class LoginSystem:
    # ユーザーIDとパスワードのハードコードされた辞書
    users = {
        "admin": "password",
        "user": "1234"
    }
    
    @staticmethod
    def login():
        if request.method == 'POST':
            # フォームからユーザーIDとパスワードを取得
            user_id = request.form.get('id')
            user_pw = request.form.get('pw')
            
            # ユーザーIDとパスワードのチェック
            if user_id in LoginSystem.users:
                # 既存ユーザーIDのパスワードチェック
                if LoginSystem.users[user_id] == user_pw:
                    return redirect(url_for('login_system.success'))
                else:
                    return render_template("12/login.html", error="パスワードが間違っています")
            else:
                # 新規ユーザーの場合、IDとパスワードを追加
                LoginSystem.users[user_id] = user_pw
                return redirect(url_for('login_system.success'))
        
        # GETリクエスト時には通常のログインページを表示
        return render_template("12/login.html", error=False)
    
    @staticmethod
    def success():
        # ログイン成功時に表示するページ
        return render_template("12/success.html")

# ルートURLと対応するビュー関数を登録
login_system_blueprint.add_url_rule('/login', view_func=LoginSystem.login, methods=['GET', 'POST'])
login_system_blueprint.add_url_rule('/success', view_func=LoginSystem.success)
