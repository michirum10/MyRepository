# 簡易電卓
# パックは一箇所にまとめると良い

# JSの簡易電卓を参考に

# Pythonの標準ライブラリ
import tkinter

# ウィンドウのインスタンス化
root = tkinter.Tk()
# ウィンドウのタイトル
root.title("簡易電卓")
# ウィンドウのサイズ
root.geometry("400x500")

# ラベルを作る
lb = tkinter.Label(text="簡易電卓")
# 入力フォーム1のインスタンス化
e1 = tkinter.Entry()
# 入力フォーム2のインスタンス化
e2 = tkinter.Entry()
# 結果を表示するラベル
result_label = tkinter.Label(text="結果:")
# ボタンをフレームにしてまとめる準備
button_frame = tkinter.Frame()

# 定数
PLUS = '+'
MINUS = '-'
MULTIPLY = '*'
DIVIDE = '/'
MODULO = '%'

# ボタンのクリックイベント時の処理
# swichの代わりにif-elif
def calculate(op):
    # get(入力フォーム)の中身を取得
    # floatで小数点も扱えるように
    num1 = float(e1.get())
    num2 = float(e2.get())
    
    if op == PLUS:
        result = num1 + num2
    elif op == MINUS:
        result = num1 - num2
    elif op == MULTIPLY:
            result = num1 * num2
    elif op == DIVIDE:
        result = num1 / num2
    elif op == MODULO:
        result = num1 % num2
    # 結果の表示
    result_label.config(text=f"{num1} {op} {num2} = {result}")

# 四則演算関数
# calculate関数もここで使う
def add():
    calculate(PLUS)
def subtract():
    calculate(MINUS)
def multiply():
    calculate(MULTIPLY)
def divide():
    calculate(DIVIDE)
def modulo():
    calculate(MODULO)

# ボタンを作る
# command=関数名
bt1 = tkinter.Button(button_frame,text="加算", command=add)
bt2 = tkinter.Button(button_frame,text="減算", command=subtract)
bt3 = tkinter.Button(button_frame,text="乗算", command=multiply)
bt4 = tkinter.Button(button_frame,text="除算", command=divide)
bt5 = tkinter.Button(button_frame,text="剰余", command=modulo)

# 簡易電卓ラベルを表示
lb.pack()
# 入力フォーム1の設置
e1.pack()
# 入力フォーム2の設置
e2.pack()

# ボタンをグループ化して入力フォームの下に配置
button_frame.pack()

# 四則演算ボタン設置
# 横並びに
bt1.pack(side=tkinter.LEFT)
bt2.pack(side=tkinter.LEFT)
bt3.pack(side=tkinter.LEFT)
bt4.pack(side=tkinter.LEFT)
bt5.pack(side=tkinter.LEFT)

# 結果を表示
result_label.pack()

# 表示開始
root.mainloop()
