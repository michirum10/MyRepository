# Pythonの標準ライブラリ
# tkinterモジュール
import tkinter

# ウィンドウのインスタンス化
root = tkinter.Tk()
# ウィンドウのタイトル
root.title("簡易電卓")
# ウィンドウのサイズ
root.geometry("400x500")

# ウィジェットのインスタンス化

# フレーム宣言(配置のため)
# デザインを整えるため、ウィジェットをまとめるウィジェット
# ラベルと入力フォームをまとめるフレーム
lb1_frame = tkinter.Frame()
lb2_frame = tkinter.Frame()
# 結果欄のフレーム
result_frame = tkinter.Frame()
# ボタンをフレームに
button_frame = tkinter.Frame()

# ラベルを作る
# root,(親)は省略できる
# 入力フォームのラベル
lb1 = tkinter.Label(lb1_frame, text="値１:")
lb2 = tkinter.Label(lb2_frame, text="値２:")
# 結果を表示するラベル
result_label = tkinter.Label(result_frame, text="結果:")

# 入力フォーム1
e1 = tkinter.Entry(lb1_frame)
# 入力フォーム2
e2 = tkinter.Entry(lb2_frame)

# 定数(計算と表示用に使う)
ADD = '+'
SUB = '-'
MUL = '*'
DIV = '/'
MOD = '%'

# ボタンのクリックイベント時の処理(閉鎖関数)
# swichの代わりにif-elif
def calc(op):  # opは変化しない変数？
    def calcProc():
        # 初期化
        # get(入力フォーム)の中身を取得
        num1 = int(e1.get())  # floatで小数点も扱えるように
        num2 = int(e2.get())  # intにすると整数
        result = None
        # 計算分岐
        if op == ADD:
            result = num1 + num2
        elif op == SUB:
            result = num1 - num2
        elif op == MUL:
            result = num1 * num2
        elif op == DIV:
            result = num1 / num2
        elif op == MOD:
            result = num1 % num2
        # 結果の表示
        result_label.configure(text=f"{num1} {op} {num2} = {result}")
    return calcProc

# ボタンを作る
# command=関数名
bt1 = tkinter.Button(button_frame, text="加算", command=calc(ADD))  # bt1のCommandのopが確定する
bt2 = tkinter.Button(button_frame, text="減算", command=calc(SUB))
bt3 = tkinter.Button(button_frame, text="乗算", command=calc(MUL))
bt4 = tkinter.Button(button_frame, text="除算", command=calc(DIV))
bt5 = tkinter.Button(button_frame, text="剰余", command=calc(MOD))

## デザインの設定

# パック(表示)はまとめる
# 書いた順に表示される

# ラベルフレームを表示
lb1_frame.pack()
lb2_frame.pack()
# ボタンをグループ化して入力フォームの下に配置
button_frame.pack()
# 結果ラベルフレームを表示
result_frame.pack()

# 入力フォーム1の設置
lb1.pack(side=tkinter.LEFT)
e1.pack(side=tkinter.LEFT)
# 入力フォーム2の設置
lb2.pack(side=tkinter.LEFT)
e2.pack(side=tkinter.LEFT)

# 四則演算ボタン設置
# 横並びに
bt1.pack(side=tkinter.LEFT)
bt2.pack(side=tkinter.LEFT)
bt3.pack(side=tkinter.LEFT)
bt4.pack(side=tkinter.LEFT)
bt5.pack(side=tkinter.LEFT)

# 結果ラベルを設置
result_label.pack()

# 表示開始
root.mainloop()
