# config.py

# SECRET_KEY
class Config:
    SECRET_KEY = b'secret_key'  # bはバイト列
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# SQLデータベース
class DevelopmentConfig(Config):
    DEBUG = True
    # データベース作成
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'

# 本番用と分けると良い
# class ProductionConfig(Config):
#     DEBUG = False
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///production.db'