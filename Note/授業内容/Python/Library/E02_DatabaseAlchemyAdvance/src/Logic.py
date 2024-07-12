# =============
# ロジック
# =============

from sqlalchemy.orm  import scoped_session, Session
from DatabaseManager import Person

def add(scoped_ses:scoped_session):
    name = input("名前を入力してください。\n>")
    gender = numberRangeInput("性別を入力してください。\n[1]男[2]女[3]その他",1,3)
    age = numberRangeInput("年齢を入力してください。",0,150)
    p = Person(name=name,gender=gender,age=age)
    # 挿入予定のデータを出力
    dispRecord(p)
    if confirm("上記のデータで登録します。\nよろしいでしょうか？"):
        # セッション開始
        session = scoped_ses()
        # DB操作[データの挿入]
        session.add(p)
        # DB操作[コミット]
        session.commit()
        # DB操作セッションの終了
        session.close()
        print("登録が実行されました。")
    else:
        print("登録がキャンセルされました。")

def getAll(scoped_ses:scoped_session):
    # セッション開始
    session = scoped_ses()
    # DB操作[全件取得処理]
    res = session.query(Person).all()
    for record in res:
        print("----------------")
        dispRecord(record)
    print("----------------")
    # DB操作セッションの終了
    session.close()

# 出力メソッドの定義
def dispRecord(record:Person):
    dicRecord = record.getData()
    print(f"id:{dicRecord["id"]}")
    print(f"name:{dicRecord["name"]}")
    print(f"gender:{transGenderNumToStr(dicRecord["gender"])}")
    print(f"age:{dicRecord["age"]}")

# 整数入力関数の定義
def numberInput(msg):
    while True:
        cmd = input(msg + "\n>")
        try:
            return int(cmd)
        except:
            print("ERROR:整数を入力してください。")

# 範囲指定、数値入力チェック関数の定義
def numberRangeInput(msg,min,max):
    while True:
        cmd = int(numberInput(msg))
        if min <= cmd <= max:
            return cmd
        else:
            print(f"ERROR:{min}~{max}の範囲の整数を入力してください。")
        

# 承認チェック関数
def confirm(msg):
    while True:
        cmd = input(f"{msg}\n [y]YES[n]NO\n>")
        if cmd == "y":
            return True
        elif cmd == "n":
            return False
        else:
            print("ERROR:正しく入力してください。")

# 性別を番号から文字列に変換する関数
genderNumToStr = {1:"男",2:"女",3:"その他"}
def transGenderNumToStr(genderNum):
    try:
        genderStr = genderNumToStr[genderNum]
    except:
        genderStr = "ERROR:データが不正です。"
    return genderStr
