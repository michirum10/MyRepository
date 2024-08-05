# main.py
# indexページ
# Shopの商品一覧画面へ遷移のみ

# インポート
from flask import Blueprint, flash, redirect, render_template, request, url_for  # 必要なFlaskモジュールをインポート
from app import app  # アプリケーション、データベース、およびモデルをインポート
from flask.views import MethodView  # Flaskのクラスベースのビューを使用するためにインポート

# ルーティング
@app.route("/")  # ルート
def index():
    return render_template("pages/index.html")