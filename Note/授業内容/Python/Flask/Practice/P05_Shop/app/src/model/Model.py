# Model.py
# User,PersonalInfo,Product,Cart,TransactionStatusのモデルクラス

from datetime import datetime, timezone  # 日付と時間を操作するためのモジュールをインポート
from flask_sqlalchemy import SQLAlchemy  # SQLAlchemyを使用してデータベース操作を行うためのモジュールをインポート
from werkzeug.security import generate_password_hash, check_password_hash  # パスワードのハッシュ化と検証を行うためのモジュールをインポート

db = SQLAlchemy()  # SQLAlchemyのインスタンスを作成

# ユーザーモデルクラス
class User(db.Model):
    __tablename__ = 'users'  # テーブル名を指定
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主キーとしてのIDカラムを定義
    username = db.Column(db.String(64), unique=True, nullable=False)  # ユーザー名カラムを定義（ユニークかつ必須）
    password_hash = db.Column(db.String(128), nullable=False)  # パスワードハッシュカラムを定義（必須）
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))  # レコードの作成時間カラムを定義（デフォルトは現在のUTC時間）
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # レコードの最終更新時間カラムを定義（更新時に自動更新）
    del_flag = db.Column(db.Integer, default=0)  # 論理削除フラグを追加（デフォルトは0）
    
    personal_info = db.relationship('PersonalInfo', backref='user', uselist=False)  # PersonalInfoモデルとの一対一のリレーションシップを定義

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)  # パスワードをハッシュ化して保存

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)  # パスワードを検証

# 個人情報モデルクラス
class PersonalInfo(db.Model):
    __tablename__ = 'personal_info'  # テーブル名を指定
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主キーとしてのIDカラムを定義
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)  # ユーザーIDカラムを定義（外部キー）
    last_name = db.Column(db.String(64), nullable=False)  # 名字カラムを定義（必須）
    first_name = db.Column(db.String(64), nullable=False)  # 名前カラムを定義（必須）
    address = db.Column(db.String(256), nullable=False)  # 住所カラムを定義（必須）
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))  # レコードの作成時間カラムを定義（デフォルトは現在のUTC時間）
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # レコードの最終更新時間カラムを定義（更新時に自動更新）
    del_flag = db.Column(db.Integer, default=0)  # 論理削除フラグを追加（デフォルトは0）

# 商品モデルクラス
class Product(db.Model):
    __tablename__ = 'products'  # テーブル名を指定
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主キーとしてのIDカラムを定義
    name = db.Column(db.String(128), nullable=False)  # 商品名カラムを定義（必須）
    image_url = db.Column(db.String(256))  # 商品画像URLカラムを定義
    price = db.Column(db.Integer, nullable=False)  # 値段カラムを定義（必須）
    del_flag = db.Column(db.Integer, default=0)  # 論理削除フラグを追加（デフォルトは0）

# カートモデルクラス
class Cart(db.Model):
    __tablename__ = 'carts'  # テーブル名を指定
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主キーとしてのIDカラムを定義
    cart_id = db.Column(db.String(64), unique=True, nullable=False)  # カートIDカラムを定義（ユニークかつ必須）
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)  # 商品IDカラムを定義（外部キー）
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))  # レコードの作成時間カラムを定義（デフォルトは現在のUTC時間）
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # レコードの最終更新時間カラムを定義（更新時に自動更新）
    del_flag = db.Column(db.Integer, default=0)  # 論理削除フラグを追加（デフォルトは0）

    product = db.relationship('Product', backref='cart_items')  # Productモデルとのリレーションシップを定義

# 取引状況モデルクラス
class TransactionStatus(db.Model):
    __tablename__ = 'transaction_status'  # テーブル名を指定
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主キーとしてのIDカラムを定義
    cart_id = db.Column(db.String(64), db.ForeignKey('carts.cart_id'), nullable=False)  # カートIDカラムを定義（外部キー）
    delivery_address = db.Column(db.String(256), nullable=False)  # 届け先カラムを定義（必須）
    status = db.Column(db.Enum('保留', '購入', 'キャンセル'), nullable=False)  # 状況カラムを定義（必須）
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))  # レコードの作成時間カラムを定義（デフォルトは現在のUTC時間）
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # レコードの最終更新時間カラムを定義（更新時に自動更新）
    del_flag = db.Column(db.Integer, default=0)  # 論理削除フラグを追加（デフォルトは0）

    cart = db.relationship('Cart', backref='transaction_status')  # Cartモデルとのリレーションシップを定義
