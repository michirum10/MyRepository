# __init__.py

print("initファイルの実行")
# 順番が大事
# パッケージ化する

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# インスタンス生成
app = Flask(__name__)
# Sessionのシークレットキー
app.secret_key = b"hit"

# SQLAlchemyの接続先サーバーの設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///EmployeeManagementSystem.db'
# Flaskインスタンスと連動ｓ
db = SQLAlchemy(app)

# DBへmodelの設定
from app.src.model.Employee import Employee
from app.src.model.Department import Department

# DBの初期化
with app.app_context():
    db.create_all()

# Flaskの設定
from app import main

# EmployeeManagementSystem.dbの統合ターミナル開いて
# フルパスで実行
# C:\Users\hit0037\DownloaC:\Users\hit0037C:\Users\hit0037\Downloads\sqlite-tools-win-x64-3460000\sqlite3.exe EmployeeManagementSystem.db