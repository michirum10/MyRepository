from app import db

class Employee(db.Model):
    # テーブルの名前をつける
    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    gender = db.Column(db.Integer)
    gender = db.Column(db.Integer)
    # フラグ
    del_flag = db.Column(db.Integer)
    # ForeignKeyは外部キー
    # 引数はテーブル名+カラム名
    # departmentのidと関連づいている
    dept_id = db.Column(db.Integer,db.ForeignKey('department.id'))  # ('department.id')テーブルの名前を書く
    
    # 辞書型で登録(純粋なデータ型として登録するため)
    def getdata(self):
        return {
            "id":int(self.id),
            "name":str(self.name),
            "age":int(self.age),
            "gender":int(self.gender),
            "dept_name":str(self.dept.name)
        }
# getdata()メソッドを作るといい(gender,dept_id)

# オレンジ色の鍵が主キー
# 白の鍵外部キー
# プロパティができる

