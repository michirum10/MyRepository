from flask import Flask,render_template,Blueprint

# Blueprintの名称：APP2
# モジュール名：app2
# URL：/APP2
app2 = Blueprint("APP2",__name__,url_prefix="/APP2")

@app2.route("/")
def index():
    return render_template("index.html",msg="APP2のホーム。")

@app2.route("/next")
def next():
    return render_template("index.html",msg="APP2のネクスト。")