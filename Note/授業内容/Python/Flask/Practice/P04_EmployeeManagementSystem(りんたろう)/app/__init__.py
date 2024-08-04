from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# インスタンス生成
app = Flask(__name__)



# sessionのシークレットキー
app.secret_key = b"rin"
# SQLAlchemyの接続先サーバーの設定
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///EmployeeManagementSystem.db'
# Flaskインスタンスと連動設定
db = SQLAlchemy(app)

# DBへmodelの設定
from app.src.model.Empolyee import Employee
from app.src.model.Department import Department

# DBの初期化
with app.app_context():
    db.create_all()


# blueprintの準備
# blueprintの書く場所はmodelを設定した後
from app.dept_crud import dCrud
app.register_blueprint(dCrud)

from app import main
