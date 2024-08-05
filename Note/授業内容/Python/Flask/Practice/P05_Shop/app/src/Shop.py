# Shop.py
# 商品一覧
# カートへの商品追加

from flask import Blueprint, flash, redirect, render_template, request, url_for  # 必要なFlaskモジュールをインポート
from app import app, db  # アプリケーション、データベース、およびモデルをインポート
from flask.views import MethodView  # Flaskのクラスベースのビューを使用するためにインポート
from app.src.model import *

# Blueprint
shop = Blueprint('shop', __name__)

# 商品情報を表示
@shop.route("/")
def index():
    # 全件取得処理
    products = Product.query.all()
    return render_template("pages/shop.html", products=products)

@shop.route("/cart")
def cart():
    return render_template("pages/cart.html")

# detailのルーティング
@shop.route("/detail")
def detail():
    return render_template("pages/detail.html")

# completeのルーティング
@shop.route("/complete")
def complete():
    return render_template("pages/complete.html")