# __init__.py
# パッケージ化(appとして扱う)
# 複数のファイルをひと固まりにしたもの

# パッケージ全体で使用されるグローバル変数を定義したり、
# 初期設定を読み込んだりすることができる


print("initファイルの実行")
# 順番が大事

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# インスタンス生成
app = Flask(__name__)
# Sessionのシークレットキー
app.secret_key = b"hit"

# SQLAlchemyデータベースを作る
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///EmployeeManagementSystem.db'
# Flaskインスタンスと連動
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