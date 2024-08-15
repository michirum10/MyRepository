# Shop.py
# 商品一覧
# カートへの商品追加

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required  # 必要なFlaskモジュールをインポート
from app import app, db  # アプリケーション、データベース、およびモデルをインポート
from flask.views import MethodView  # Flaskのクラスベースのビューを使用するためにインポート
from app.src.model import *

# Blueprint
shop_bp = Blueprint('shop', __name__)

# 商品情報を表示
@shop_bp.route("/shop")
def shop():
    # 全件取得処理
    products = Product.query.all()
    return render_template("pages/shop.html", products=products)

# 詳細を表示
@shop_bp.route("/detail/<id>")  # ダイレクトルーティング
def detail(id):
    # 商品の詳細を取得(1件取得)
    product = Product.query.get(id)
    return render_template("pages/detail.html",product=product)

# # カートの中身を表示
# @shop_bp.route("/cart")
# def cart():
#     # 全件取得処理(フィルタリング：追加されたもののみ)
#     cart_items = Cart.query.filter(Product.del_flag == 0).all()
#     return render_template("pages/cart.html",cart_items=cart_items)

# カートに追加する処理
@shop_bp.route("/add_to_cart/<int:product_id>", methods=["POST"])
@login_required  # このルートはログインが必要
def add_to_cart(product_id):
    # userがログアウト状態の場合、ログイン画面にリダイレクト
    if not current_user.is_authenticated:
        flash('ログインして下さい')
        return redirect(url_for('auth.login'))
    # userがログイン状態の場合、カートに商品を追加できる
    else:
        # 商品idを1件取得
        product = Product.query.get(product_id)
        if product:
            # カートIDと商品IDの組み合わせが重複しないようにチェック
            existing_item = Cart.query.filter_by(user_id=current_user.id, product_id=product_id).first()
            if existing_item:
                existing_item.quantity += 1
                flash("カート内の商品の数量を更新しました。", "success")
            else:
                cart_item = Cart(user_id=current_user.id, product_id=product.id, quantity=1)
                db.session.add(cart_item)
                flash("商品をカートに追加しました。", "success")
            db.session.commit()
        else:
            flash('商品が見つかりませんでした。')
        return redirect(url_for('shop.shop'))