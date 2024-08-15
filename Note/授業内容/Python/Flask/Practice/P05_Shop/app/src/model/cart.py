from datetime import datetime, timezone  # 日付と時間を操作するためのモジュールをインポート
from . import db

# カートモデルクラス
class Cart(db.Model):
    __tablename__ = 'carts'  # テーブル名を指定
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主キーとしてのIDカラムを定義
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # ユーザーIDカラムを定義（外部キー）
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)  # 商品IDカラムを定義（外部キー）
    quantity = db.Column(db.Integer, nullable=False, default=1)  # 商品の数量を定義
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))  # レコードの作成時間カラムを定義（デフォルトは現在のUTC時間）
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # レコードの最終更新時間カラムを定義（更新時に自動更新）
    del_flag = db.Column(db.Integer, default=0)  # 論理削除フラグを追加（デフォルトは0）

    __table_args__ = (db.UniqueConstraint('user_id', 'product_id', name='user_product_uc'),)  # ユーザーIDと商品IDの組み合わせをユニークにする

    # TransactionStatusモデルとの一対多のリレーションシップ
    transactions = db.relationship('TransactionStatus', backref='cart', lazy=True)