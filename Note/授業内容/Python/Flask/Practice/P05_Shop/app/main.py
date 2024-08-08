# main.py
# indexページ
# Shopの商品一覧画面へ遷移のみ

# インポート
from flask import Blueprint, flash, redirect, render_template, request, url_for
from app import app
from flask.views import MethodView

# ルーティング
@app.route("/")  # ルート
def index():
    return render_template("pages/index.html")