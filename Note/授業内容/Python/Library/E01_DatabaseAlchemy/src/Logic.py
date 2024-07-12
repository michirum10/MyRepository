# =============
# ロジック
# =============

from sqlalchemy.orm  import scoped_session, Session
from DatabaseManager import Person

def add(scoped_ses:scoped_session):
    name = input("名前を入力してください。\n>")
    gender = input("性別を入力してください。\n[1]男[2]女[3]その他\n>")
    age = input("年齢を入力してください。\n>")
    p = Person(name=name,gender=gender,age=age)

    # セッション開始
    session = scoped_ses()
    # DB操作[データの挿入]
    session.add(p)
    # DB操作[コミット]
    session.commit()
    # DB操作セッションの終了
    session.close()
    
    print("登録が実行されました。")

def getAll(scoped_ses:scoped_session):
    # セッション開始
    session = scoped_ses()
    # DB操作[全件取得処理]
    res = session.query(Person).all()
    for record in res:
        dispRecord(record)
    # DB操作セッションの終了
    session.close()

# 出力メソッドの定義
def dispRecord(record:Person):
    dicRecord = record.getData()
    print(f"id:{dicRecord["id"]}")
    print(f"name:{dicRecord["name"]}")
    print(f"gender:{dicRecord["gender"]}")
    print(f"age:{dicRecord["age"]}")