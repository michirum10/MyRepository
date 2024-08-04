from app import db

class Department(db.Model):
    __tablename__ = "department"

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(20))
    del_flag = db.Column(db.Integer)

    # relationshipの第一引数はクラス名(モデル)を指定
    # relationshipのbackref引数は関連先のモデルのプロパティに追加するプロパティ名
    employees = db.relationship("Employee", backref="dept")

    # 辞書型で取得
    def getData(self):
        return{
            "id":int(self.id),
            "name":str(self.name)
        }