# model
# DatabaseManager.py

# FlaskアプリケーションにSQLAlchemyを設定するためのファイル
# データベースの接続や管理を行うために必要な設定が含まれる
# appオブジェクトはFlaskアプリケーションのインスタンス
# SQLAlchemyを使用してデータベースとの連携を行う

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import app
