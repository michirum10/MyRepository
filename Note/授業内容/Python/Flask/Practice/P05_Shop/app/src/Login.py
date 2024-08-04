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
# モデルクラスをインポート
from app.src.model.Model import User, PersonalInfo, Product, Cart, TransactionStatus

bp = Blueprint('auth', __name__)  # 'auth'(認証)という名前のBlueprintを作成

# ログイン用入力クラス
class LoginForm(FlaskForm):
    username = StringField('ユーザー名：', validators=[DataRequired('ユーザー名は必須入力です')])  # ユーザー名入力フィールドと必須バリデータ
    password = PasswordField('パスワード：', validators=[Length(4, 10, 'パスワードの長さは4文字以上10文字以内です')])  # パスワード入力フィールドと長さバリデータ
    submit = SubmitField('ログイン')  # ログインボタン

    # カスタムバリデータ
    def validate_password(self, password):
        if not (any(c.isalpha() for c in password.data) and  # 英字が含まれているかチェック
                any(c.isdigit() for c in password.data)):  # 数字が含まれているかチェック
            raise ValidationError('パスワードには【英数字を含める必要があります')  # バリデーションエラーメッセージ

# サインアップ用入力クラス
class SignUpForm(LoginForm):  # LoginFormを継承してSignUpFormを作成
    submit = SubmitField('サインアップ')  # サインアップボタン

    # カスタムバリデータ
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()  # ユーザー名が既に存在するかチェック
        if user:
            raise ValidationError('そのユーザー名は既に使用されています')  # バリデーションエラーメッセージ

@bp.route('/login', methods=['GET', 'POST'])  # /loginルートを定義
def login():
    form = LoginForm()  # LoginFormのインスタンスを作成
    if form.validate_on_submit():  # フォームが送信され、バリデーションが成功した場合
        user = User.query.filter_by(username=form.username.data).first()  # 入力されたユーザー名でユーザーを検索
        if user and user.check_password(form.password.data):  # ユーザーが存在し、パスワードが一致する場合
            login_user(user)  # ユーザーをログイン
            flash('ログインに成功しました。', 'success')  # 成功メッセージを表示
            return redirect(url_for('main.index'))  # メインページにリダイレクト
        else:
            flash('ユーザー名またはパスワードが間違っています。', 'danger')  # エラーメッセージを表示
    return render_template('pages/login.html', form=form)  # ログインページをレンダリング

@bp.route('/signup', methods=['GET', 'POST'])  # /signupルートを定義
def signup():
    form = SignUpForm()  # SignUpFormのインスタンスを作成
    if form.validate_on_submit():  # フォームが送信され、バリデーションが成功した場合
        user = User(username=form.username.data)  # 新しいユーザーを作成
        user.set_password(form.password.data)  # パスワードを設定
        db.session.add(user)  # ユーザーをデータベースに追加
        db.session.commit()  # 変更をコミット
        flash('アカウントが作成されました。', 'success')  # 成功メッセージを表示
        return redirect(url_for('auth.login'))  # ログインページにリダイレクト
    return render_template('pages/sign_up.html', form=form)  # サインアップページをレンダリング

@bp.route('/logout')  # /logoutルートを定義
@login_required  # このルートはログインが必要
def logout():
    logout_user()  # ユーザーをログアウト
    flash('ログアウトしました。', 'success')  # 成功メッセージを表示
    return redirect(url_for('main.index'))  # メインページにリダイレクト

@bp.route('/')  # ルートページを定義
def index():
    return render_template('pages/index.html')  # インデックスページをレンダリング
