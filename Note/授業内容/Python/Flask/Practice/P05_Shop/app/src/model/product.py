# product.py
from datetime import datetime, timezone  # 日付と時間を操作するためのモジュールをインポート
from . import db

# 商品モデルクラス
class Product(db.Model):
    __tablename__ = 'products'  # テーブル名を指定
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主キーとしてのIDカラム
    name = db.Column(db.String(128), nullable=False)  # 商品名カラム（必須）
    image_url = db.Column(db.String(256))  # 商品画像URLカラム
    price = db.Column(db.Integer, nullable=False)  # 値段カラム（必須）
    del_flag = db.Column(db.Integer, default=0)  # 論理削除フラグを追加（デフォルトは0）
    # Cartモデルとの一対多のリレーションシップ
    cart_items = db.relationship('Cart', backref='product', lazy=True)