# Account.py
# アカウントの新規作成
# アカウントの設定変更
# 購入履歴

from flask import Blueprint, render_template, redirect, url_for, flash  # FlaskのBlueprint、テンプレートレンダリング、リダイレクト、URL生成、フラッシュメッセージをインポート
from flask_login import login_user, logout_user, login_required  # Flask-Loginの関数をインポート
from flask_wtf import FlaskForm  # Flask-WTFのフォームクラスをインポート
from wtforms import StringField, PasswordField, SubmitField  # WTFormsのフィールドクラスをインポート
from wtforms.validators import DataRequired, Length, ValidationError  # WTFormsのバリデータをインポート
from app import * # データベースインスタンスをインポート
from app.src.Login import LoginForm
# ブループリント
account_bp = Blueprint('account', __name__)  # 'account'(認証)という名前のBlueprintを作成

# サインアップ（新規登録）
# サインアップ用入力クラス
class SignUpForm(LoginForm):  # LoginFormを継承してSignUpFormを作成
    submit = SubmitField('サインアップ')  # サインアップボタン

    # カスタムバリデータ
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()  # ユーザー名が既に存在するかチェック
        if user:
            raise ValidationError('そのユーザー名は既に使用されています')  # バリデーションエラーメッセージ
        
# /signupルート
@account_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()  # SignUpFormのインスタンスを作成
    if form.validate_on_submit():  # フォームが送信され、バリデーションが成功した場合
        # データ入力取得
        username = form.username.data
        password = form.password.data
        # モデルを生成
        user = User(username=username)  # 新しいユーザーを作成
        # パスワードハッシュ化
        user.set_password(password)  # パスワードを設定
        # 登録処理
        db.session.add(user)  # ユーザーをデータベースに追加
        db.session.commit()  # 変更をコミット
        login_user(user)  # ユーザーを自動的にログイン
        # フラッシュメッセージ
        flash('アカウントが作成されました。', 'success')  # 成功メッセージを表示
        return redirect(url_for('shop.shop'))  # ログインページにリダイレクト
    return render_template('pages/sign_up.html', form=form)  # サインアップページをレンダリング


# アカウントの更新（マイページ）

# 購入履歴（マイページ）