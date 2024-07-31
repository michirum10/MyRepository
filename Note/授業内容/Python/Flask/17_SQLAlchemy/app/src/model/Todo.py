from app import db

class ToDo(db.Model):
    # テーブルの名前をつける
    __tablename__ = "todo"
    
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000))

    # 辞書型で登録(純粋なデータ型として登録するため)
    def getdata(self):
        return {
            "id": self.id,
            "text": self.text
        }
