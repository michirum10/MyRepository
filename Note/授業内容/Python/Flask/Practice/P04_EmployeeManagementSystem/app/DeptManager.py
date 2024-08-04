# Department.py

from flask import flash, redirect, render_template, request, url_for, Blueprint
from app import app, db, Department as Dept
from flask.views import MethodView

dept_list = Blueprint('dept_list', __name__, url_prefix='/dept_list')

# 部署データ一覧の表示ページ
@dept_list.route("/")
def index():
    # セッション開始
    dbses = db.session
    # 全件取得処理
    # filter(Dept.del_flag == 0)で論理削除されたレコードを除外
    depts = dbses.query(Dept).filter(Dept.del_flag == 0).all()
    return render_template("Dept_index.html", depts=depts)

class DeptCreate(MethodView):
    def get(self):
        # 新規登録モードでDeptDetail.htmlを呼び出す
        return render_template("DeptDetail.html", mode=1)
    
    def post(self):
        name = request.form.get("name")
        # 論理削除フラグは0
        del_flag = 0
        dept = Dept(name=name, del_flag=del_flag)
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
app.add_url_rule("/dcreate", view_func=DeptCreate.as_view("dCreate"))

@dept_list.route("/detail/<id>")
def dept_detail(id):
    # セッション開始
    dbses = db.session
    # １件取得
    dept = dbses.query(Dept).get(id)
    if dept is None:
        # 部署が存在しない場合の処理（例：エラーページにリダイレクトするなど）
        flash("指定された部署は存在しません。")
        return redirect(url_for('dept_list.index'))
    # 詳細モードでDeptDetail.htmlを呼び出す
    return render_template("DeptDetail.html", dept=dept, mode=2)

class DeptUpdate(MethodView):
    def get(self, id):
        dbses = db.session
        # 一覧を取得
        dept = dbses.query(Dept).get(id)
        # 更新モードでDeptDetail.htmlを呼び出す
        return render_template("DeptDetail.html", dept=dept, mode=3)

    def post(self, id):
        name = request.form.get("name")
        # セッション開始
        dbses = db.session
        # １件取得
        dept = dbses.query(Dept).get(id)
        if dept is None:
            # idが存在しない時
            flash("指定されたIDが存在しないので失敗しました。")
            return redirect(url_for('dept_list.index'))
        
        # 更新前の部署名を取得
        old_name = dept.name
        
        # フォームから新しい名前を取得
        name = request.form.get("name")
        
        # データを更新する処理
        dept.name = name
        dbses.commit()
        
        flash("データの更新に成功しました。")
        # 更新後の部署情報を渡してリダイレクト
        return redirect(url_for('dept_list.update_success', id=dept.id,old_name=old_name))

# 関連づけ
app.add_url_rule("/dupdate/<id>", view_func=DeptUpdate.as_view("dUpdate"))

# 削除のルート
@dept_list.route("/delete/<id>")
def dept_delete(id):
    dbses = db.session
    dept = dbses.query(Dept).get(id)
    if dept is None:
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
    
    
# 更新完了画面用のルート
@dept_list.route('/update_success/<id>')
def update_success(id):
    old_name = request.args.get('old_name')
    dbses = db.session
    dept = dbses.query(Dept).get(id)
    if dept is None:
        flash("指定された部署は存在しません。")
        return redirect(url_for('dept_list.index'))
    return render_template('update_success.html', dept=dept, old_name=old_name)
