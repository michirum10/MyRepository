# main.py
# 社員管理システム

from flask import flash, redirect, render_template, request, url_for  # 必要なFlaskモジュールをインポート
from app import app, db, Employee, Department  # アプリケーション、データベース、およびモデルをインポート
from flask.views import MethodView  # Flaskのクラスベースのビューを使用するためにインポート

# Blueprintの登録
from app.DeptManager import dept_list  # 部署管理のBlueprintをインポート
app.register_blueprint(dept_list)  # Blueprintをアプリケーションに登録

# データ一覧の表示ページ
@app.route("/")  # ルートパスに対するルート定義
def index():
    # セッション開始
    dbses = db.session  # データベースセッションを開始
    # 社員情報を全件取得処理(削除されていないもののみ)
    emps = dbses.query(Employee).filter(Employee.del_flag == 0).all()  # del_flagが0のレコードをすべて取得
    
    # 各社員の部署情報を一つずつチェック
    for emp in emps:
        # 社員が所属する部署のID (dept_id) を使って部署情報を取得
        dept = dbses.query(Department).get(emp.dept_id)
        if dept:  # 部署が存在する場合
            if dept and dept.del_flag == 1:  # flagが1(論理削除)のときは削除済みと表示
                emp.dept_name = dept.name + "[削除済み]"
            else:
                emp.dept_name = dept.name  # 部署が存在する場合は名前を表示
        else:
            emp.dept_name = "部署なし"  # 部署が存在しない場合
    
    return render_template("index.html", datas=emps)  # 取得したデータをテンプレートに渡してレンダリング

class EmployeeCreate(MethodView):  # 社員新規作成用のクラスベースビュー
    def get(self):
        # 新規登録モードでEmployeeDetail.htmlを呼び出す
        # 部署IDのSelected処理
        # セッション開始
        dbses = db.session  # データベースセッションを開始
        # 部署の選択肢を格納する辞書を初期化
        deptSelect = {}  
        # 全件取得
        # filter(Department.del_flag == 0)で論理削除されたレコードを除外
        depts = dbses.query(Department).filter(Department.del_flag == 0).all()  # 有効な部署をすべて取得
        for dept in depts:  # 各部署についてループ
            deptSelect[dept.id] = {'name': dept.name, 'selected': ''}  # 辞書に部署情報を追加
            
        return render_template("EmployeeDetail.html", mode=1, deptSelect=deptSelect)  # 新規登録モードでテンプレートを表示
    
    # 登録
    def post(self):
        name = request.form.get("name")  # フォームから名前を取得
        age = request.form.get("age")  # フォームから年齢を取得
        gender = request.form.get("gender")  # フォームから性別を取得
        dept_id = request.form.get("dept_id")  # フォームから部署IDを取得
        # 論理削除フラグは0
        del_flag = 0  # 新規作成時はdel_flagを0に設定
        data = Employee(name=name, age=age, gender=gender, dept_id=dept_id, del_flag=del_flag)  # 新しいEmployeeオブジェクトを作成
        # セッション開始
        dbses = db.session  # データベースセッションを開始
        # 追加
        dbses.add(data)  # 新しいデータをセッションに追加
        # コミット
        dbses.commit()  # 変更をデータベースにコミット
        flash("データの作成に成功しました。")  # 成功メッセージを表示
        # 全件表示のページへリダイレクト
        return redirect(url_for('index'))  # インデックスページにリダイレクト

# 関連づけ
app.add_url_rule("/eCreate", view_func=EmployeeCreate.as_view("eCreate"))  # 新規作成のURLルールを追加

@app.route("/detail/<id>")  # 詳細表示用のルート定義
def detail(id):
    # セッション開始
    dbses = db.session  # データベースセッションを開始
    # １件取得
    res = dbses.query(Employee).get(id)  # 指定されたIDのデータを取得
    
    # 性別のSelected処理
    res.genderSelect = ['', '', '']  # 性別の選択肢を初期化
    try:
        res.genderSelect[res.gender] = 'selected'  # 性別に応じて選択状態を設定
    except TypeError:
        pass  # 型エラーが発生した場合は何もしない
    
    # 部署IDのSelected処理
    res.deptSelect = {}  # 部署選択肢を初期化
    depts = dbses.query(Department).all()  # 全ての部署を取得
    for dept in depts:  # 各部署についてループ
        if dept.del_flag == 1:  # 部署の論理削除フラグが1の場合
            # 表示
            res.deptSelect[dept.id] = {'name': dept.name + "[削除済み]", 'selected': ''}  # 名前に削除済みと付け加える
        else:
            res.deptSelect[dept.id] = {'name': dept.name, 'selected': ''}  # 辞書に部署情報を追加
    try:
        res.deptSelect[res.dept_id]['selected'] = 'selected'  # 部署IDに応じて選択状態を設定
    except KeyError:
        pass  # キーエラーが発生した場合は何もしない

    # 詳細モードでEmployeeDetail.htmlを呼び出す
    return render_template("EmployeeDetail.html", data=res, mode=2)  # 詳細表示モードでテンプレートを表示

class EmployeeUpdate(MethodView):  # 社員情報更新用のクラスベースビュー
    def get(self, id):
        dbses = db.session  # データベースセッションを開始
        # 一覧を取得
        res = dbses.query(Employee).get(id)  # 指定されたIDのデータを取得
        
        # 性別のSelected処理
        res.genderSelect = ['', '', '']  # 性別の選択肢を初期化
        try:
            res.genderSelect[res.gender] = 'selected'  # 性別に応じて選択状態を設定
        except TypeError:
            pass  # 型エラーが発生した場合は何もしない
        
        # 部署IDのSelected処理
        res.deptSelect = {}  # 部署選択肢を初期化
        depts = dbses.query(Department).filter(Department.del_flag == 0).all()  # 有効な部署をすべて取得
        for dept in depts:  # 各部署についてループ
            res.deptSelect[dept.id] = {'name': dept.name, 'selected': ''}  # 辞書に部署情報を追加
        try:
            res.deptSelect[res.dept_id]['selected'] = 'selected'  # 部署IDに応じて選択状態を設定
        except KeyError:
            pass  # キーエラーが発生した場合は何もしない
        
        # 更新モードでEmployeeDetail.htmlを呼び出す
        return render_template("EmployeeDetail.html", data=res, mode=3)  # 更新モードでテンプレートを表示

    def post(self, id):
        name = request.form.get("name")  # フォームから名前を取得
        age = request.form.get("age")  # フォームから年齢を取得
        gender = request.form.get("gender")  # フォームから性別を取得
        dept_id = request.form.get("dept_id")  # フォームから部署IDを取得
        # セッション開始
        dbses = db.session  # データベースセッションを開始
        # １件取得
        res = dbses.query(Employee).get(id)  # 指定されたIDのデータを取得
        if res is None:
            # idが存在しない時
            flash("指定されたIDが存在しないので失敗しました。")  # エラーメッセージを表示
            return redirect(url_for('index'))  # インデックスページにリダイレクト
        else:
            # データを更新する処理
            res.name = name  # 名前を更新
            res.age = age  # 年齢を更新
            res.gender = gender  # 性別を更新
            res.dept_id = dept_id  # 部署IDを更新
            dbses.commit()  # 変更をデータベースにコミット
            flash("データの更新に成功しました。")  # 成功メッセージを表示
            # 全件表示のページへリダイレクト
            return redirect(url_for('index'))  # インデックスページにリダイレクト

# 関連づけ
app.add_url_rule("/eupdate/<id>", view_func=EmployeeUpdate.as_view("eUpdate"))  # 更新用のURLルールを追加

# 社員削除のルート
@app.route("/delete/<id>")
def delete(id):
    # セッション開始
    dbses = db.session
    # １件取得
    res = dbses.query(Employee).get(id)
    if res is None:
        # idが存在しない時
        flash("指定されたIDが存在しないので失敗しました。")  # 失敗メッセージを表示
        return redirect(url_for('index'))
    else:
        # データを削除する処理
        res.del_flag = 1
        dbses.commit()
        flash("データの削除に成功しました。")  # 成功メッセージを表示
        # 全件表示のページへリダイレクト
        return redirect(url_for('index'))