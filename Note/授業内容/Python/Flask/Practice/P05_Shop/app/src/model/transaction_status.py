from datetime import datetime, timezone  # 日付と時間を操作するためのモジュールをインポート
from . import db  # SQLAlchemyインスタンスをインポート

# 取引状況モデルクラス
class TransactionStatus(db.Model):
    __tablename__ = 'transaction_status'  # テーブル名を指定
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主キーとしてのIDカラム
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)  # カートIDカラム（外部キー）
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # ユーザーIDカラム（外部キー）
    delivery_address = db.Column(db.String(256), nullable=False)  # 届け先カラム（必須）
    status = db.Column(db.Enum('保留', '購入', 'キャンセル'), nullable=False)  # 状況カラム（必須）
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))  # レコードの作成時間カラム（デフォルトは現在のUTC時間）
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # レコードの最終更新時間カラム（更新時に自動更新）
    del_flag = db.Column(db.Integer, default=0)  # 論理削除フラグを追加（デフォルトは0）
