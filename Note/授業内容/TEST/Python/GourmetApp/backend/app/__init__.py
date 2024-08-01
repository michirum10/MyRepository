from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from .LoginSystem import login_bp, init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # データベース初期化
    init_db(app)
    
    # ブループリントの登録
    app.register_blueprint(login_bp)
    
    return app
