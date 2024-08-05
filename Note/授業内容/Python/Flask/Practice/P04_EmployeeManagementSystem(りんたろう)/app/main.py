from flask import flash, redirect, render_template, request, url_for
from flask.views import MethodView
from app import app,db,Employee,Department
from sqlalchemy import or_,and_

# データ一覧の表示ページ
@app.route("/")
def index():
    dbses = db.session
    # 全件取得処理
    res = dbses.query(Employee).filter(Employee.del_flag == 0).all()

    dept_data_list = {}
    dept_datas = dbses.query(Department).all()
    for dept_data in dept_datas:
            dept_data_list[dept_data.id] = {'name':dept_data.name,'del_flag':dept_data.del_flag}
    return render_template("index.html", datas = res , dept_datas = dept_data_list)

@app.route("/search")
def search():
    name = request.args.get("name")
    gender = request.args.get("gender")
    dept = request.args.get("dept")
    try:
        dept = int(dept)
    except ValueError:
        pass
    search_opt = request.args.get("search_opt")
    searchData = {'name':name,'gender':gender,'dept':dept}
    filters = []
    if name:
        filters.append(Employee.name.like(f'%{name}%'))
    if gender:
        filters.append(Employee.gender == gender)
    if dept:
        filters.append(Employee.dept_id == dept)
    filters.append(Employee.del_flag == 0)
    dbses = db.session
    Tfilters = tuple(filters)
    if search_opt == "and":
        res = dbses.query(Employee).filter(and_(*Tfilters)).all()
    else:
        res = dbses.query(Employee).filter(or_(*Tfilters)).all()

    dept_data_list = {}
    dept_datas = dbses.query(Department).all()
    for dept_data in dept_datas:
            dept_data_list[dept_data.id] = {'name':dept_data.name,'del_flag':dept_data.del_flag}

    if res == None:
        flash("検索項目を正しく入力してください。")
        return redirect(url_for(index))
    else:
        return render_template("index.html", datas = res , dept_datas = dept_data_list , searchData = searchData)

class EmployeeCreate(MethodView):
    def get(self):
        # 新規登録モードでEmployeeDetail.htmlを呼び出す
        # 部署IDのSelected処理
        dbses = db.session
        deptSelect = {}
        depts = dbses.query(Department).filter(Department.del_flag == 0).all()
        for dept in depts:
            deptSelect[dept.id] = {'name':dept.name,'selected':''}
        # 新規登録モードでEmployeeDetail.htmlを呼び出す
        return render_template("EmployeeDetail.html",mode=1,deptSelect=deptSelect)

    def post(self):
        name = request.form.get("name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        dept_id = request.form.get("dept")
        # 論理削除フラグは0
        del_flag = 0
        data = Employee(name=name,age=age,gender=gender,dept_id=dept_id,del_flag=del_flag)
        dbses = db.session
        dbses.add(data)
        dbses.commit()
        flash("データの作成に成功しました。")
        # 全件表示のページへリダイレクト
        return redirect(url_for('index'))
    
app.add_url_rule("/eCreate",view_func=EmployeeCreate.as_view("eCreate"))

@app.route("/detail/<id>")
def detail(id):
    dbses = db.session
    res = dbses.query(Employee).get(id)

    # 性別のSelected処理
    res.genderSelect = ['','','']
    try:
        res.genderSelect[res.gender] = 'selected'
    except TypeError:
        pass

    # 部署IDのSelect処理
    res.deptSelect = {}
    depts = dbses.query(Department).all()
    for dept in depts:
        res.deptSelect[dept.id] = {'name':dept.name,'del_flag':dept.del_flag,'selected':''}
    # 部署IDのSelected処理
    try:
        res.deptSelect[res.dept_id]['selected'] = 'selected'
    except KeyError:
        pass


    # 詳細モードでEmployeeDetail.htmlを呼び出す
    return render_template("EmployeeDetail.html",data=res,mode=2)

class EmployeeUpdate(MethodView):
    def get(self,id):
        dbses = db.session
        res = dbses.query(Employee).get(id)

        # 性別のSelected処理
        res.genderSelect = ['','','']
        try:
            res.genderSelect[res.gender] = 'selected'
        except TypeError:
            pass

        # 部署IDのSelect処理
        res.deptSelect = {}
        depts = dbses.query(Department).order_by(Department.del_flag).all()
        for dept in depts:
            res.deptSelect[dept.id] = {'name':dept.name,'del_flag':dept.del_flag,'selected':''}
        # 部署IDのSelected処理
        try:
            res.deptSelect[res.dept_id]['selected'] = 'selected'
        except KeyError:
            pass

        # 更新モードでEmployeeDetail.htmlを呼び出す
        return render_template("EmployeeDetail.html",data=res,mode=3)

    def post(self,id):
        name = request.form.get("name")
        age = request.form.get("age")
        gender = request.form.get("gender")
        dept_id = request.form.get("dept")
        data = Employee(name=name,age=age,gender=gender,dept_id=dept_id)
        dbses = db.session
        res = dbses.query(Employee).get(id)
        if res == None:
            # idが存在しない時
            flash("指定されたIDが存在しないので失敗しました。")
            return redirect(url_for('index'))
        else:
            # データを更新する処理
            res.name = name
            res.age = age
            res.gender = gender
            res.dept_id = dept_id
            dbses.commit()
            flash("データの更新に成功しました。")
            # 全件表示のページへリダイレクト
            return redirect(url_for('index')) 

app.add_url_rule("/update/<id>",view_func=EmployeeUpdate.as_view("eUpdate"))

@app.route("/delete/<id>")
def delete(id):
    dbses = db.session
    res = dbses.query(Employee).get(id)
    if res == None:
        # idが存在しない時
        flash("指定されたIDが存在しないので失敗しました。")
        return redirect(url_for('index'))
    else:
        # データを削除する処理
        res.del_flag = 1
        dbses.commit()
        flash("データの削除に成功しました。")
        # 全件表示のページへリダイレクト
        return redirect(url_for('index'))