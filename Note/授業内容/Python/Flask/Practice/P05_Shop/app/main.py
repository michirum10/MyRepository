# main.py
# 確認のためのルーティング
# Shopの商品一覧画面へ遷移

# インポート
from flask import flash, redirect, render_template, request, url_for  # 必要なFlaskモジュールをインポート
from app import app  # アプリケーション、データベース、およびモデルをインポート
from flask.views import MethodView  # Flaskのクラスベースのビューを使用するためにインポート

# Blueprintの登録
# from app.CartManager import dept_list  # カート管理のBlueprintをインポート
# app.register_blueprint(dept_list)  # Blueprintをアプリケーションに登録

# ルーティング
@app.route("/")  # ルート
def index():
    return render_template("pages/index.html")

# cartのルーティング
@app.route("/cart")
def cart():
    return render_template("pages/cart.html")

# detailのルーティング
@app.route("/detail")
def detail():
    return render_template("pages/detail.html")

# completeのルーティング
@app.route("/complete")
def complete():
    return render_template("pages/complete.html")


