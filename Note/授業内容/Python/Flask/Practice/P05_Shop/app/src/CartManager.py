# CartManager.py
# カート内参照
    # - 商品一覧
    # - 合計金額
# カートの商品削除
# 購入手続き

# インポート
from flask import Blueprint, flash, redirect, render_template, request, url_for  # 必要なFlaskモジュールをインポート
from app import app, db  # アプリケーション、データベース、およびモデルをインポート
from flask.views import MethodView  # Flaskのクラスベースのビューを使用するためにインポート
from app.src.model import *

# Blueprint
cart_bp = Blueprint('cart', __name__)

# カートの中身を取得して表示
@cart_bp.route("/cart")
def cart():
    # 全件取得処理(フィルタリング：追加されたもののみ)
    cart_items = Cart.query.filter(Product.del_flag == 0).all()
    return render_template("pages/cart.html",cart_items=cart_items)

# カート内参照
    # - 商品一覧
    # - 合計金額

# カートの商品削除

# 購入手続き

# 購入完了画面へ
# completeのルーティング
@cart_bp.route("/complete")
def complete():
    return render_template("pages/complete.html")