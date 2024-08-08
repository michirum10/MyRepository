from datetime import datetime, timezone  # 日付と時間を操作するためのモジュールをインポート
from . import db

# 個人情報モデルクラス
class PersonalInfo(db.Model):
    __tablename__ = 'personal_info'  # テーブル名を指定
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主キーとしてのIDカラム
    
    # ユーザーIDカラム（外部キー）
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    
    last_name = db.Column(db.String(64), nullable=False)  # 名字カラム（必須）
    first_name = db.Column(db.String(64), nullable=False)  # 名前カラム（必須）
    address1 = db.Column(db.String(256), nullable=False)  # 住所1カラム（必須）
    address2 = db.Column(db.String(256), nullable=True)  # 住所2カラム（任意）
    address3 = db.Column(db.String(256), nullable=True)  # 住所3カラム（任意）
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))  # レコードの作成時間カラム（デフォルトは現在のUTC時間）
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))  # レコードの最終更新時間カラム（更新時に自動更新）
    del_flag = db.Column(db.Integer, default=0)  # 論理削除フラグを追加（デフォルトは0）
