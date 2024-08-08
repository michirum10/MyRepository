# Login.py
# ログイン
# ログアウト
# サインアップ

from flask import Blueprint, render_template, redirect, url_for, flash  # FlaskのBlueprint、テンプレートレンダリング、リダイレクト、URL生成、フラッシュメッセージをインポート
from flask_login import login_user, logout_user, login_required  # Flask-Loginの関数をインポート
from flask_wtf import FlaskForm  # Flask-WTFのフォームクラスをインポート
from wtforms import StringField, PasswordField, SubmitField  # WTFormsのフィールドクラスをインポート
from wtforms.validators import DataRequired, Length, ValidationError  # WTFormsのバリデータをインポート
from app import db  # データベースインスタンスをインポート

# モデルクラスをインポート(appから持ってくる)
from app import *

auth_bp = Blueprint('auth', __name__)  # 'auth'(認証)という名前のBlueprintを作成

# ログイン用入力クラス
class LoginForm(FlaskForm):
    username = StringField('ユーザー名：', validators=[DataRequired('ユーザー名は必須入力です')])  # ユーザー名入力フィールドと必須バリデータ
    password = PasswordField('パスワード：', validators=[Length(4, 10, 'パスワードの長さは4文字以上10文字以内です')])  # パスワード入力フィールドと長さバリデータ
    submit = SubmitField('ログイン')  # ログインボタン

    # カスタムバリデータ
    def validate_password(self, password):
        if not (any(c.isalpha() for c in password.data) and  # 英字が含まれているかチェック
                any(c.isdigit() for c in password.data)):  # 数字が含まれているかチェック
            raise ValidationError('パスワードには【英数字】を含める必要があります')  # バリデーションエラーメッセージ

# /loginルート
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # LoginFormのインスタンスを作成
    if form.validate_on_submit():  # フォームが送信され、バリデーションが成功した場合
        # データ入力取得
        username = form.username.data
        password = form.password.data
        # 入力されたユーザー名でユーザーを検索
        user = User.query.filter_by(username=username).first()
        # 認証判定
        if user is not None and user.check_password(password):  # ユーザーが存在し、パスワードが一致する場合
            # 成功
            login_user(user)  # 引数として渡されたuserオブジェクトを使用して、ユーザーをログイン状態にする
            # 画面遷移
            return redirect(url_for("shop.shop"))  # shopルートのshop関数？
        # 失敗
        flash("認証不備です")
    # GET時
    # 画面遷移
    return render_template('pages/login.html', form=form)  # ログインページをレンダリング


# /logoutルート
@auth_bp.route('/logout')
@login_required  # このルートはログインが必要
def logout():
    logout_user()  # ユーザーをログアウト
    flash('ログアウトしました。', 'success')  # 成功メッセージを表示
    return redirect(url_for('index'))  # メインページにリダイレクト
