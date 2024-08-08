# cart.py
from datetime import datetime, timezone  # 日付と時間を操作するためのモジュールをインポート
from . import db

# カートモデルクラス
class Cart(db.Model):
    __tablename__ = 'carts'  # テーブル名を指定
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主キーとしてのIDカラム
    cart_id = db.Column(db.String(64), unique=True, nullable=False)  # カートIDカラム（ユニークかつ必須）
    # 商品IDカラム（外部キー）
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False) 
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))  # レコードの作成時間カラム（デフォルトは現在のUTC時間）
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # レコードの最終更新時間カラム（更新時に自動更新）
    del_flag = db.Column(db.Integer, default=0)  # 論理削除フラグを追加（デフォルトは0）
    # TransactionStatusモデルとの一対多のリレーションシップ
    transactions = db.relationship('TransactionStatus', backref='cart', lazy=True)