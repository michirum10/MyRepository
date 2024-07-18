# ランダムで当てるアプリ
# 任意の人を登録できるようにしてください。
# 登録した人からランダムに1人を出力してください。
# 偏らない様に、全員が平等に出力されるようにしてください。
# アプリケーションを終了しても、データを維持できるようにしてください。（データの読み込みと保存）
import tkinter
import Logic as Logic

# ウィンドウの準備
root = tkinter.Tk()
root.title("StudentPicker")
root.geometry("200x120")

registrationLabel = tkinter.Label(text="登録:")
registrationEntry = tkinter.Entry()

# データ配列
studentArray = Logic.load()

# 登録ボタン押下時の処理
def push_registrationButton():
    # 値(氏名)の取得
    name = registrationEntry.get()
    registrationEntry.delete(0,tkinter.END)
    # データの登録
    studentArray.append({"name":name,"count":0})
    # データの保存
    Logic.save(studentArray)

registrationButton = tkinter.Button(text="登録",command=push_registrationButton)

# ランダムボタン押下時の処理
def push_randomPickButton():
    student = Logic.randomPick(studentArray)
    if student is not None:
        name = student["name"]
        randomPickLabel.configure(text=name)
    else:
        randomPickLabel.configure(text="データがありません")

randomPickButton= tkinter.Button(text="ランダムで一人",command=push_randomPickButton)

randomPickLabel = tkinter.Label()

# デザイン
registrationLabel.pack()
registrationEntry.pack()
registrationButton.pack()

randomPickButton.pack()
randomPickLabel.pack()

# 表示開始
root.mainloop()