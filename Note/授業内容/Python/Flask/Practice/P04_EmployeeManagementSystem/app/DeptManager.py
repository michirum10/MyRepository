# Department.py

from flask import flash, redirect, render_template, request, url_for,Blueprint
from app import app,db,Department as Dept
from flask.views import MethodView

dept_list = Blueprint('dept_list',__name__,url_prefix='/dept_list')

# 部署データ一覧の表示ページ
@dept_list.route("/")
def index():
    # セッション開始
    dbses = db.session
    # 全件取得処理
    depts = dbses.query(Dept).filter(Dept.del_flag == 0).all()
    # dbses.close()があるとhtmlでエラーになるので書かない
    return render_template("dept_index.html",depts = depts)


class DeptCreate(MethodView):
    def get(self):
        # 新規登録モードでDeptDetail.htmlを呼び出す
        return render_template("DeptDetail.html",mode=1)
    
    # 登録
    def post(self):
        name = request.form.get("name")
        # 論理削除フラグは0
        del_flag = 0
        dept = Dept(name=name,del_flag=del_flag)
        # セッション開始
        dbses = db.session
        # 追加
        dbses.add(dept)
        # コミット
        dbses.commit()
        flash("部署の作成に成功しました。")
        # 全件表示のページへリダイレクト
        return redirect(url_for('dept_list.index'))
# 関連づけ
app.add_url_rule("/Create",view_func=DeptCreate.as_view("Create"))

@dept_list.route("/detail/<id>")
def dept_detail(id):
    # セッション開始
    dbses = db.session
    # １件取得
    dept = dbses.query(Dept).get(id)
    # 詳細モードでDeptDetail.htmlを呼び出す
    return render_template("DeptDetail.html",dept=dept,mode=2)

class DeptUpdate(MethodView):
    def get(self,id):
        dbses = db.session
        # 一覧を取得
        dept = dbses.query(Dept).get(id)
        
        # 更新モードでDeptDetail.htmlを呼び出す
        return render_template("DeptDetail.html",dept=dept,mode=3)

    def post(self,id):
        name = request.form.get("name")
        # セッション開始
        dbses = db.session
        # １件取得
        dept = dbses.query(Dept).get(id)
        if dept == None:
            # idが存在しない時
            flash("指定されたIDが存在しないので失敗しました。")
            return redirect(url_for('dept_list.index'))
        else:
            # データを更新する処理
            dept.name = name
            dbses.commit()
            flash("データの更新に成功しました。")
            # 全件表示のページへリダイレクト
            return redirect(url_for('dept_list.index'))
    
app.add_url_rule("/update/<id>",view_func=DeptUpdate.as_view("dUpdate"))


@dept_list.route("/delete/<id>")
def dept_delete(id):
    dbses = db.session
    dept = dbses.query(Dept).get(id)
    if dept == None:
        # idが存在しない時
        flash("指定されたIDが存在しないので失敗しました。")
        return redirect(url_for('dept_list.index'))
    else:
        # データを削除する処理
        dept.del_flag = 1
        dbses.commit()
        flash("データの削除に成功しました。")
        # 全件表示のページへリダイレクト
        return redirect(url_for('dept_list.index')) 

# エンドポイントの登録
app.add_url_rule("/delete/<id>", view_func=dept_delete, endpoint="dept_delete")