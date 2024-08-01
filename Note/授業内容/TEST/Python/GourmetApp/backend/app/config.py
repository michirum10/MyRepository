class Config:
    # Flask アプリケーションの設定クラス

    SECRET_KEY = 'your_secret_key'  # セキュリティキー
    SQLALCHEMY_DATABASE_URI = 'sqlite:///your_database.db'  # データベース URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # データベースの変更追跡を無効化
