# Account.py
# アカウントの新規作成
# アカウントの設定変更
# 購入履歴

# インポート
from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask.views import MethodView
from flask_login import login_user, logout_user, login_required, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from app import db, app
from app.src.model import *
from app.src.Login import LoginForm

# ブループリントを作成
account_bp = Blueprint('account', __name__)  # 'account'(認証)のBlueprintを作成

# サインアップ用入力クラス
class SignUpForm(FlaskForm):  # LoginFormを継承してSignUpFormを作成
    username = StringField('ユーザー名：', validators=[DataRequired('ユーザー名は必須入力です')])
    password = PasswordField('パスワード：', validators=[Length(4, 10, 'パスワードの長さは4文字以上10文字以内です')])
    last_name = StringField('名字：', validators=[DataRequired('名字は必須入力です')])
    first_name = StringField('名前：', validators=[DataRequired('名前は必須入力です')])
    address = StringField('住所：', validators=[DataRequired('住所は必須入力です')])
    submit = SubmitField('サインアップ')  # サインアップボタンを追加

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
        # formから取得
        username = form.username.data
        password = form.password.data
        last_name = form.last_name.data
        first_name = form.first_name.data得
        address = form.address.data
        
        user = User(username=username)  # 新しいユーザーを作成
        user.set_password(password)  # パスワードをハッシュ化して設定
        db.session.add(user)  # ユーザーをデータベースに追加
        db.session.commit()  # 変更をコミット
        
        personal_info = PersonalInfo(user_id=user.id, last_name=last_name, first_name=first_name, address1=address)  # 個人情報を作成
        db.session.add(personal_info)  # 個人情報をデータベースに追加
        db.session.commit()  # 変更をコミット
        
        login_user(user)  # ユーザーを自動的にログイン
        flash('新規登録に成功しました！', 'success')  # 成功メッセージを表示
        return redirect(url_for('shop.shop'))  # 商品一覧ページにリダイレクト
    return render_template('pages/sign_up.html', form=form)  # サインアップページをレンダリング

# アカウントの更新用フォームクラス
class AccountUpdateForm(FlaskForm):
    username = StringField('ユーザー名：', validators=[DataRequired('ユーザー名は必須入力です')])  # ユーザー名入力フィールドと必須バリデータ
    password = PasswordField('パスワード：', validators=[Length(4, 10, 'パスワードの長さは4文字以上10文字以内です')])  # パスワード入力フィールドと長さバリデータ
    submit = SubmitField('更新')  # 更新ボタン

# アカウントの更新（マイページ）
class AccountUpdate(MethodView):
    @login_required  # ログインが必要
    def get(self):
        form = AccountUpdateForm(obj=current_user)  # 現在のユーザー情報をフォームに設定
        return render_template("pages/account_update.html", form=form)  # アカウント更新ページをレンダリング

    @login_required  # ログインが必要
    def post(self):
        form = AccountUpdateForm()  # フォームインスタンスを作成
        if form.validate_on_submit():  # フォームが送信され、バリデーションが成功した場合
            current_user.username = form.username.data  # ユーザー名を更新
            if form.password.data:  # パスワードが入力されている場合
                current_user.set_password(form.password.data)  # パスワードをハッシュ化して設定
            db.session.commit()  # 変更をコミット
            flash("アカウント情報が更新されました。", 'success')  # 成功メッセージを表示
            return redirect(url_for('main.index'))  # メインページにリダイレクト
        return render_template("pages/account_update.html", form=form)  # アカウント更新ページをレンダリング

# アカウント更新のルートを追加
app.add_url_rule("/account/update", view_func=AccountUpdate.as_view("account_update"))

# 購入履歴（マイページ）
@account_bp.route('/history')
@login_required  # ログインが必要
def history():
    transactions = TransactionStatus.query.filter_by(user_id=current_user.id).all()  # 購入履歴を取得
    return render_template('pages/history.html', transactions=transactions)  # 購入履歴ページをレンダリング

# マイページを表示
@account_bp.route('/mypage', methods=['GET', 'POST'])
@login_required  # ログインが必要
def mypage():
    return render_template('pages/mypage.html')
