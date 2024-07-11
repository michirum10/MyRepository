# 教科書p167
# =============
# SQLAlchemy(ORMの利用)
# =============

from sqlalchemy import Column, Integer, String, create_engine
# 標準モジュールじゃないのでインストール必要(pip install SQLAlchemy)
from sqlalchemy.orm import declarative_base, sessionmaker


# モデルを作成
# プログラムでいうとClassの事
# DBでいうとテーブルの事

# モデルのベースクラスを取得
Base = declarative_base()

# モデルの定義
class Person(Base):
    
    # テーブル名
    __tablename__ = "person"
    
    # カラムの定義
    # クイックフィックスでインポート追加
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    gender = Column(Integer)
    age = Column(Integer)
# データを辞書型で取得する
    def getData(self):
            return {
                "id":int(self.id),
                "name":str(self.name),
                "gender":int(self.gender),
                "age":int(self.age),
            } 

# テストコード
if __name__ == "__main__":
    # ORMエンジンの使用準備と接続
    db = create_engine("sqlite:///InputOutput/PersonAlchemy.db")

    # テーブルを自動生成する準備
    Base.metadata.create_all(bind=db,checkfirst=True)

    # セッション
    Session = sessionmaker(bind=db)
    ses = Session()

    # データベース操作
    # データの挿入
    p1 = Person(name="木内",gender=1,age=36)
    ses.add(p1)
    ses.commit()
    
    # 全データ取得
    print("全データ取得")
    # query()の中には、どの情報がほしいのかを書く
    res1 =  ses.query(Person).all()
    
    for record in res1:
        dicRecord = record.getData()
        print(f"id:{dicRecord["id"]}")
        print(f"name:{dicRecord["name"]}")
        print(f"gender:{dicRecord["gender"]}")
        print(f"age:{dicRecord["age"]}")
