# __init__.py
# パッケージ化(appとして扱う)
# 複数のファイルをひと固まりにしたもの

# パッケージ全体で使用されるグローバル変数を定義したり、
# 初期設定を読み込んだりすることができる

print("initファイルの実行")  # 初期化ファイルが実行されたことを示すメッセージを表示

# Flaskモジュールをインポート
from flask import Flask, render_template
# SQLAlchemyモジュールをインポート
from flask_sqlalchemy import SQLAlchemy
# Flask-Loginモジュールをインポート
from flask_login import LoginManager, current_user
# Flask-Migrateをインポート
from flask_migrate import Migrate
# Configクラスをインポート
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

# モデルクラスをインポート
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
# authブループリントを登録
from app.src import Login
app.register_blueprint(Login.auth, url_prefix='/auth')  # authブループリントを登録

# shopBlueprintを登録
from app.src import Shop
app.register_blueprint(Shop.shop, url_prefix='/shop')


# メインモジュールをインポート
from app import main

# コンテキストプロセッサを追加して、current_userを全テンプレートで利用可能にする（？）
@app.context_processor
def inject_user():
    return dict(current_user=current_user)

# sql3はDb.dbの統合ターミナル開いて実行
# sqlite3 DB.db
