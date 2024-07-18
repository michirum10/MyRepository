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

# 全部表示するやつ
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

# 性別選択の整数入力関数の定義
def numberInput(msg):
    while True:
        cmd = input(msg + "\n>")
        try:
            return int(cmd)
        except:
            print("ERROR:整数を入力してください。")

# 年齢の範囲指定、数値入力チェック関数の定義
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

# 更新機能
def update(scoped_ses: scoped_session):
    # 現在の全レコードを表示
    session = scoped_ses()
    res = session.query(Person).all()
    for record in res:
        print("----------------")
        dispRecord(record)
    print("----------------")
    session.close()
    
    # IDを入力(整数のみ受付)
    id = numberInput("更新するレコードのIDを入力してください")
    session = scoped_ses()
    record = session.get(Person, id)

    if record:
        new_name = input("新しい名前を入力してください（変更しない場合は空白のままにしてください）:\n>")
        if new_name:
            record.name = new_name
        if confirm("性別を変更しますか？"):
            new_gender = numberRangeInput("新しい性別を入力してください（1:男、2:女、3:その他）:", 1, 3)  # (msg, min, max)
            new_gender_str = transGenderNumToStr(new_gender)
            record.gender = new_gender
        if confirm("年齢を変更しますか？"):
            new_age = numberRangeInput("新しい年齢を入力してください:", 0, 150) # (msg, min, max)
            record.age = new_age
        
        session.commit()
        print("データが更新されました。")
        dispRecord(record)
    else:
        print(f"ID {id} のレコードが見つかりません。")

    session.close()

# 削除機能(物理削除)
def delete(scoped_ses: scoped_session):
    
    # レコードの一覧を表示
    session = scoped_ses()
    res = session.query(Person).all()
    for record in res:
        print("----------------")
        dispRecord(record)
    print("----------------")
    # 表示したら一旦閉じる
    session.close()
    
    id = numberInput("削除するレコードのIDを入力してください")
    session = scoped_ses()
    record = session.get(Person, id)
    
    if record:
        if confirm(f"本当にID {id} のレコードを削除してもよろしいですか？:\n>"):
            session.delete(record)
            session.commit()
            print(f"ID {id} のレコードが削除されました。")
        else:
            print("削除がキャンセルされました。")
    else:
        print(f"ID {id} のレコードが見つかりません。")
    # 閉じる
    session.close()