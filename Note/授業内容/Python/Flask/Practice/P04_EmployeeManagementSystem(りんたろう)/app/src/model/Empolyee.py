from app import db

class Employee(db.Model):
    __tableName__ = "employee"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    gender = db.Column(db.Integer)
    del_flag = db.Column(db.Integer)
    # ForeignKeyは外部キー
    # 引数はテーブル名+カラム名
    dept_id = db.Column(db.Integer,db.ForeignKey('department.id'))


    # 辞書型で取得
    def getData(self):
        return{
            "id":int(self.id),
            "name":str(self.name),
            "age":int(self.age),
            "gender":int(self.gender),
            "dept_name":int(self.dept.name)
        }
