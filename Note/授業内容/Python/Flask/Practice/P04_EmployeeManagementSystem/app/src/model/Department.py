# Department.py(model)
from app import db

# 部署クラスを別で作る
class Department(db.Model):
    # テーブルの名前をつける
    __tablename__ = "department"
    
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(20))
    
    del_flag = db.Column(db.Integer, default=0)  # 論理削除フラグを追加
    
    # relationshipの第一引数はクラス名(モデル)を指定
    # relationshipのbackref引数は関連先のモデルのプロパティに追加するプロパティ名
    employees = db.relationship("Employee", backref="dept")  # 第一引数("Employee")はクラス名

    # 辞書型で取得
    def getData(self):
        return{
            "id":int(self.id),
            "name":str(self.name)
        }