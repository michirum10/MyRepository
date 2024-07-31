print("initファイルの実行")
# 順番が大事
# パッケージ化する

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# インスタンス生成
app = Flask(__name__)
# SQLAlchemyの接続先サーバーの設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ToDo.db'
# Flaskインスタンスと連動ｓ
db = SQLAlchemy(app)

# DBへmodelの設定
from app.src.model.Todo import ToDo
# DBの初期化
with app.app_context():
    db.create_all()

# Flaskの設定
from app import main
