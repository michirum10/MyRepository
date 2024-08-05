# personal_info.py
from datetime import datetime, timezone  # 日付と時間を操作するためのモジュールをインポート
from . import db

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

