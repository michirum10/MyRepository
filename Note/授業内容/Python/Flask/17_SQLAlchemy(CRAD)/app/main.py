from flask import flash, redirect, render_template, request, url_for
from app import app,db,ToDo

# データ一覧の表示ページ
@app.route("/")
def index():
    dbses = db.session
    # 全件取得処理
    res = dbses.query(ToDo).all()
    dbses.close()
    return render_template("index.html",datas = res)

# データの挿入処理
@app.route("/create", methods=["POST"])
def create():
    # 入力されたテキストを取得
    text = request.form.get("text")
    # modelにデータを挿入
    data = ToDo(text=text)
    dbses = db.session
    # 追加
    dbses.add(data)
    # コミット
    dbses.commit()
    flash("データの作成に成功しました")  # flashはsessionのシークレットキーが必要
    # 全件表示のページへリダイレクト
    return redirect(url_for("index"))

# データの更新
@app.route("/update", methods=["POST"])
def update():
    # textとidを取得
    text = request.form.get("text")
    id = request.form.get("id")
    # セッション開始
    dbses = db.session
    # 1件取得
    res = dbses.query(ToDo).get(id)
    # textが何型か確認
    print("ここ")
    print(res)
    if res == None:
        # idが存在しない時
        flash("指定されたデータが存在しません")
        return redirect(url_for("index"))
    else:
        # 
        res.text = text  # データ書き換え(代入)
        # コミット
        dbses.commit()
        flash("データの更新に成功しました")
        # 全件表示のページへリダイレクト
        return redirect(url_for("index"))
    
    # POSTはアンカータグに対応できない
    # GETはアンカータグに対応できる
    # ボタンにするとPOST使えるが、フォームを書かないといけない
    
    # データの削除処理
@app.route("/delete")
def delete():
    id = request.args.get("id")
    # session開始
    dbses = db.session
    # １件検索
    res = dbses.query(ToDo).get(id)
    if res == None:
        # idが存在しない時
        flash("指定されたIDが存在しないので失敗しました。")
        return redirect(url_for('index'))
    else:
        dbses.delete(res)
        dbses.commit()
        flash("データの削除に成功しました")
        return redirect(url_for("index"))