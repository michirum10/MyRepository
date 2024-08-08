from datetime import datetime, timezone  # 日付と時間を操作するためのモジュールをインポート
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash  # パスワードのハッシュ化と検証を行うためのモジュールをインポート
from . import db

# ユーザーモデルクラス
class User(UserMixin, db.Model):
    __tablename__ = 'users'  # テーブル名を指定
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主キー
    username = db.Column(db.String(64), unique=True, nullable=False)  # ユーザー名カラム（ユニークかつ必須）
    password_hash = db.Column(db.String(128), nullable=False)  # パスワードハッシュカラム（必須）
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))  # レコードの作成時間カラムを定義（デフォルトは現在のUTC時間）
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # レコードの最終更新時間カラムを定義（更新時に自動更新）
    del_flag = db.Column(db.Integer, default=0)  # 論理削除フラグを追加（デフォルトは0）
    
    # PersonalInfoモデルとの一対一のリレーションシップ
    personal_info = db.relationship('PersonalInfo', backref='user', uselist=False)
    # TransactionStatusと一対多のリレーションシップ
    transactions = db.relationship('TransactionStatus', backref='user', lazy=True)
    
    # パスワードをハッシュ化して保存
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # パスワードを検証
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
