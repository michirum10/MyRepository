# config.py
# SECRET_KEYの設定
# データベースURIを取得


import os  # OSモジュールをインポートして環境変数を読み込むために使用
from dotenv import load_dotenv  # dotenvモジュールをインポートして.envファイルから環境変数を読み込むために使用

# .envファイルから環境変数を読み込む
load_dotenv()

# Configクラスを定義してアプリケーションの設定を管理
class Config:
    # 環境変数からシークレットキーを取得し、存在しない場合はデフォルト値を設定
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # 環境変数からデータベースURIを取得し、存在しない場合はデフォルト値を設定
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///DB.db'
    # SQLAlchemyのトラック変更機能を無効にする
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 環境変数からデバッグモードを取得し、存在しない場合はデフォルト値を設定
    DEBUG = os.environ.get('DEBUG') or True
