# LoginSystem.py

from flask import Blueprint, redirect, render_template, request, session, url_for
from flask.views import MethodView
# SQLAlchemyデータベース
from flask_sqlalchemy import SQLAlchemy
# ハッシュ化のためのモジュール
import bcrypt
# インプットフォーム
from forms import InputForm

# Blueprintの名称：LoginSystem
# モジュール名：LoginSystem
# URL：/LoginSystem
login_bp = Blueprint("LoginSystem", __name__, url_prefix="/LoginSystem")

# データベースの設定(インスタンス作成)
db = SQLAlchemy()

# データベース(SQL)初期化関数
def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

# ユーザーのIDとパスワードを管理(ハッシュ化)
class User(db.Model):
    
    # SQLテーブル
    # ユーザーのID。最大80文字の文字列型。主キー
    id = db.Column(db.String(80), primary_key=True)
    # ユーザーのパスワード。最大120文字の文字列型。NULL値を許可しない
    password = db.Column(db.String(120), nullable=False)

    # パスワードをハッシュ化して文字列として保存
    def set_password(self, password):
        # パスワードをUTF-8でエンコード、ハッシュ化し、再度デコードして保存
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # 入力されたパスワードが正しいかチェックするメソッド
    def check_password(self, password):
        # 入力パスワードをハッシュ化し、保存されているハッシュと比較
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

# loginのルート
class LoginSystem(MethodView):
    def get(self):
        form = InputForm()  # インスタンス化
        if 'id' in session:  # セッションに'id'が存在するか確認
            form.id.data = session['id']  # セッションから'id'を取得してフォームに設定
        return render_template("pages/login.html", form=form)  # ログインページへ

    def post(self):
        form = InputForm()  # インスタンス化
        msg = None  # エラーメッセージ用の変数を初期化
        
        if form.validate_on_submit():  # バリデーションが成功したか確認
            id = form.id.data  # フォームからIDを取得
            pw = form.pw.data  # フォームからパスワードを取得
            session['id'] = id  # セッションにIDを保存

            user = User.query.get(id)  # データベースからユーザーを検索
            
            if user:  # ユーザーが存在する場合
                if user.check_password(pw):  # 入力されたパスワードが正しいかチェック
                    session['flag'] = True  # ログイン成功、セッションにフラグを設定
                    return render_template('pages/success.html', id=id, pw=pw)  # 成功ページに
                else:  # パスワードが間違っている場合
                    session['flag'] = False
                    msg = 'エラー：idまたはパスワードが間違っています！'
                    
            else:  # 新規登録
                new_user = User(id=id)  # 新しいユーザーをインスタンス化
                new_user.set_password(pw)  # パスワードをハッシュ化
                db.session.add(new_user)  # 新しいユーザーを追加
                db.session.commit()  # 変更をコミット
                session['flag'] = True  # ログイン成功フラグ
                return redirect(url_for('LoginSystem.success'))  # 成功ページにリダイレクト
            
        return render_template('pages/login.html', form=form)  # ログインページを再表示

# successのルート(分ける)
class Success(MethodView):
    def get(self):
        if 'flag' in session and session['flag']:
            id = session.get('id')
            if id is None:
                # IDが取得できない場合はログインページにリダイレクト
                return redirect(url_for('LoginSystem.login'))
            
            msg = 'ログインに成功しました！'
            title = 'ログイン成功'
            return render_template("pages/success.html", id=id, pw="••••••••", msg=msg, title=title)
        else:
            return redirect(url_for('LoginSystem.login'))

# /loginをブループリントに登録
login_bp.add_url_rule("/login", view_func=LoginSystem.as_view("login"))

# /successをブループリントに登録
login_bp.add_url_rule("/success", view_func=Success.as_view("success"))