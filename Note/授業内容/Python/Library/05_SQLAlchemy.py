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
    p1 = Person(name="田中",gender=1,age=32)
    ses.add(p1)
    ses.commit()
    
    # 出力メソッドの定義
    def dispRecord(record:Person):
        dicRecord = record.getData()
        print(f"id:{dicRecord["id"]}")
        print(f"name:{dicRecord["name"]}")
        print(f"gender:{dicRecord["gender"]}")
        print(f"age:{dicRecord["age"]}")

    # 全データ取得
    print("全データ取得")
    res1 =  ses.query(Person).all()
    for record in res1:
        dispRecord(record)  # 表示

# 1件だけ取得
    print("１件データ取得(id=2)")
    # １件データ取得
    # ID(プライマリキー)が2番のレコードを取得
    p2 = ses.get(Person,2)
    # 表示
    dispRecord(p2)

# 1件データ取得(検索)
    # 1件データ取得(検索)
    print("１件データ取得(id=3)")
    # 複数ヒットしたデータのはじめの1件だけ取得
    p3 = ses.query(Person).filter(Person.id==3).first()  # first()無いと配列になってしまう
    # 表示
    dispRecord(p3)
    
    # データ検索
    print("データ取得(age=37)")
    p4 = ses.query(Person).filter(Person.age == 37)  # 全部のデータ見たいので、「.first()」いらない
    for record in p4:
        dispRecord(record)

# データ検索(あいまい検索)
    print("データ検索(name=「田」が付くもの)")
    p5 = ses.query(Person).filter(Person.name.like("%田%"))
    for record in p5:
        dispRecord(record)

# データの更新
# 取得したデータをそのまま書き換えてコミットする
    print("データの更新")
    print("idを指定して内容を書き換える")
    inputNo = input("IDを指定してください>")  # ターミナルに入力
    # １件データ取得
    p6 = ses.get(Person,inputNo)  # ターミナルに入力したIDを取得。(第１引数はテーブル、第２引数はどこを取得するか)
    print("データの更新前")
    dispRecord(p6)  # 一旦表示(勉強用。書かなくて良い)
    # データを書き換える
    p6.name = "木之内"
    # コミット(更新)
    ses.commit()
    print("データの更新後")
    dispRecord(p6)
    
    # データの削除
    print("データの削除")
    ses.query(Person).filter(Person.name == "木之内").delete()
    ses.commit()
    
    # １件取得して書き換える
    # p6 = ses.get(Person,inputNo)  # ターミナルに入力したIDを取得。(第１引数はテーブル、第２引数はどこを取得するか)
    # p6.name = "木之内"
    # コミット(更新)
    # ses.commit()