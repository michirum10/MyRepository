# StudentPickerのロジックモジュール
import json
from random import randint

# 保存
# 引数のデータの形式
# [{"name":"氏名","count":0}]
def save(studentArray):
    data = {}
    data["student"] = studentArray
    with open('student.json', 'w',encoding="utf-8") as file:
        json.dump(data, file,ensure_ascii=False)

# 読み込み
# 戻り値のデータの形式
# [{"name":"氏名","count":0}]
def load():
    try:
        with open('student.json', 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data["student"]
    except FileNotFoundError:
        return []

def randomPick(studentArray):
    try:
        min = studentArray[0]["count"]
        for student in studentArray:
            if student["count"] < min:
                min = student["count"]
        while True:
            # 乱数発生
            rnd = randint(0,len(studentArray)-1)
            if studentArray[rnd]["count"] == min:
                # カウントアップ
                studentArray[rnd]["count"] += 1
                save(studentArray)
                return studentArray[rnd]
    except IndexError:
        return None


# テストコード
if __name__ == "__main__":
    print("プログラムを開始します")
    endFlag = False
    studentData = load()
    print(studentData)
    while not endFlag:
        cmd = input("[1]登録[2]ランダムで一人[0]終了\n>")
        if cmd == "1":
            name = input("氏名を入力してください。\n>")
            studentData.append({"name":name,"count":0})
            save(studentData)
        elif cmd == "2":
            student = randomPick(studentData)
            if student is not None:
                print(f'{student["name"]}:{student["count"]}')
            else:
                print("データがありません。")
        elif cmd == "0":
            print("終了が選択されました。")
            endFlag = True
        else:
            print("正しいコマンドを入力してください。")
    print("プログラムを終了します。")
