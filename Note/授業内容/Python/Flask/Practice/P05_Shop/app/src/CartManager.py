# CartManager.py
# カート内参照
# - 商品一覧
# - 合計金額
# カートの商品削除
# 購入手続き

# 必要なFlaskモジュールをインポート
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask.views import MethodView  # クラスベースのビューを使用するためにインポート
from flask_login import login_required, current_user  # Flask-Loginの関数をインポート
from app import db  # アプリケーション、データベースをインポート
from app.src.model import Cart, Product, TransactionStatus  # モデルクラスをインポート

# Blueprintを作成
cart_bp = Blueprint('cart', __name__)

# カートの中身を取得して表示
@cart_bp.route("/cart")
@login_required  # ログインが必要
def view_cart():
    # 現在のユーザーのカートアイテムを取得
    cart_items = Cart.query.filter_by(cart_id=current_user.id).all()
    # 合計金額を計算
    total_amount = sum(item.product.price for item in cart_items)
    return render_template("pages/cart.html", cart_items=cart_items, total_amount=total_amount)

# カートの商品削除
@cart_bp.route("/cart/delete/<int:item_id>", methods=["POST"])
@login_required  # ログインが必要
def delete_item(item_id):
    # 指定されたカートアイテムを取得
    cart_item = Cart.query.get(item_id)
    if cart_item and cart_item.cart_id == current_user.id:
        db.session.delete(cart_item)  # カートアイテムを削除
        db.session.commit()  # 変更をコミット
        flash("商品をカートから削除しました。", "success")
    else:
        flash("商品が見つかりませんでした。", "danger")
    return redirect(url_for('cart.view_cart'))


# 購入手続き
@cart_bp.route("/cart/checkout", methods=["POST"])
@login_required  # ログインが必要
def checkout():
    # 現在のユーザーのカートアイテムを取得
    cart_items = Cart.query.filter_by(cart_id=current_user.id).all()
    if not cart_items:
        flash("カートが空です。", "warning")
        return redirect(url_for('cart.view_cart'))

    # 購入手続きを行う
    for item in cart_items:
        transaction = TransactionStatus(
            cart_id=item.cart_id,
            delivery_address=current_user.personal_info.address,  # 住所を設定
            status="購入"
        )
        db.session.add(transaction)
        db.session.delete(item)  # カートアイテムを削除
    db.session.commit()  # 変更をコミット
    flash("購入手続きが完了しました。", "success")
    return redirect(url_for('cart.complete'))

# 購入完了画面
@cart_bp.route("/complete")
@login_required  # ログインが必要
def complete():
    return render_template("pages/complete.html")
