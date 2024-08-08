# __init__.py
# パッケージ化(appとして扱う)
# 複数のファイルをひと固まりにしたもの

# パッケージ全体で使用されるグローバル変数を定義したり、
# 初期設定を読み込んだりすることができる

print("initファイルの実行")  # 初期化ファイルが実行されたことを示すメッセージを表示

# インポート
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
# migrateをインポートしてDB操作できるように
from flask_migrate import Migrate
# Configクラス（設定）をインポート
from config import Config 

# Flaskアプリケーションのインスタンスを生成
app = Flask(__name__)
# Configクラスから設定を読み込む
app.config.from_object(Config)

# Flaskアプリケーションと連動するSQLAlchemyインスタンスを作成
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Flask-Migrateのインスタンスを作成

# Flask-Loginの設定
login_manager = LoginManager()
login_manager.init_app(app)  # Flaskアプリケーションにログインマネージャを設定
login_manager.login_view = 'auth.login'  # ログインページの設定
login_manager.login_message = "ログインが必要です。"  # フラッシュメッセージをカスタマイズ
login_manager.login_message_category = "warning"  # フラッシュメッセージのカテゴリを設定

# モデルクラスをインポート（*で省略可能）
# from app.src.model import User, PersonalInfo, Product, Cart, TransactionStatus
from app.src.model import *

# ユーザーローダー関数を定義（何？）
# Flask-Loginがユーザーをロードするために使用する
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# # # データベースの初期化
# with app.app_context():
#     db.create_all()  # データベーステーブルを作成

# Blueprintの登録
from app.src import Login,Account,Shop,CartManager
app.register_blueprint(Login.auth_bp, url_prefix='/auth')  # auth(認証)
app.register_blueprint(Account.account_bp, url_prefix='/account')
app.register_blueprint(Shop.shop_bp, url_prefix='/shop')
app.register_blueprint(CartManager.cart_bp, url_prefix='/cart')

# メインモジュールをインポート
from app import main

# コンテキストプロセッサを追加して、current_userを全テンプレートで利用可能にする（ha？）
@app.context_processor
def inject_user():
    return dict(current_user=current_user)

# sql3はDb.dbの統合ターミナル開いて実行
# sqlite3 DB.db
