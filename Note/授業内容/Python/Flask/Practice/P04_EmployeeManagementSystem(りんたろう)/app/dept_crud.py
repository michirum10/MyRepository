from flask import flash, redirect, render_template, request, url_for,Blueprint
from flask.views import MethodView
from app import app,db,Employee,Department


# Blueprintの名称：DEPT_CRUD
# モジュール名：dCrud
# URL：/department
dCrud = Blueprint("DEPT_CRUD",__name__,url_prefix="/department")

# データ一覧の表示ページ
@dCrud.route("/")
def index():
    dbses = db.session
    # 全件取得処理.del_flag == 0
    res = dbses.query(Department).filter(Department.del_flag == 0).all()
    return render_template("dept_index.html",datas = res)

class DeptCreate(MethodView):
    def get(self):
        return render_template("dept_detail.html",mode=1)

    def post(self):
        name = request.form.get("name")
        # 論理削除フラグは0
        del_flag = 0
        data = Department(name=name,del_flag=del_flag)
        dbses = db.session
        dbses.add(data)
        dbses.commit()
        flash("データの作成に成功しました。")
        # 全件表示のページへリダイレクト
        return redirect(url_for('DEPT_CRUD.index'))
    
dCrud.add_url_rule("/dCreate",view_func=DeptCreate.as_view("dCreate"))

class DeptUpdate(MethodView):
    def get(self,id):
        dbses = db.session
        res = dbses.query(Department).get(id)
        # 更新モードでdept_detail.htmlを呼び出す
        return render_template("dept_detail.html",data=res,mode=2)

    def post(self,id):
        name = request.form.get("name")
        del_flag = request.form.get("del_flag")
        data = Department(name=name,del_flag=del_flag)
        dbses = db.session
        res = dbses.query(Department).get(id)
        if res == None:
            # idが存在しない時
            flash("指定されたIDが存在しないので失敗しました。")
            return redirect(url_for('DEPT_CRUD.index'))
        else:
            # データを更新する処理
            res.name = name
            res.del_flag = del_flag
            dbses.commit()
            flash("データの更新に成功しました。")
            # 全件表示のページへリダイレクト
            return redirect(url_for('DEPT_CRUD.index'))
dCrud.add_url_rule("/update/<id>",view_func=DeptUpdate.as_view("dUpdate"))

# 削除処理
@dCrud.route("/delete/<id>")
def delete(id):
    dbses = db.session
    res = dbses.query(Department).get(id)
    if res == None:
        # idが存在しない時
        flash("指定されたIDが存在しないので失敗しました。")
        return redirect(url_for('DEPT_CRUD.index'))
    else:
        # データを削除する処理
        res.del_flag = 1
        dbses.commit()
        flash("データの削除に成功しました。")
        # 全件表示のページへリダイレクト
        return redirect(url_for('DEPT_CRUD.index'))

class DeptDelete(MethodView):
    def get(self):
        dbses = db.session
        # 全件取得処理
        res = dbses.query(Department).all()
        return render_template("dept_delete.html",datas = res)
    
    # post()の括弧の中に値を入れるのはダイナミックルーティングを使用するとき
    def post(self):
        id = request.form.get("id")
        print(id)
        dbses = db.session
        # 全件取得処理
        res = dbses.query(Department).get(id)
        if res == None:
            # idが存在しない時
            flash("指定されたIDが存在しないので失敗しました。")
            return redirect(url_for('DEPT_CRUD.dDelete'))
        else:
            if res.del_flag == 0:
                res.del_flag = 1
            else:
                res.del_flag = 0
            dbses.commit()
            return redirect(url_for('DEPT_CRUD.dDelete'))

dCrud.add_url_rule("/delete",view_func=DeptDelete.as_view("dDelete"))