# 簡易電卓

# パック(表示)は一番下にまとめる
# JSの簡易電卓を参考に

# Pythonの標準ライブラリ
# tkinterモジュール
import tkinter

# ウィンドウのインスタンス化
root = tkinter.Tk()
# ウィンドウのタイトル
root.title("簡易電卓")
# ウィンドウのサイズ
root.geometry("400x500")
# サイズ宣言がない場合はオートレイアウト


# ウィジェットのインスタンス化

# フレーム
# デザインを整えるため、ウィジェットをまとめるウィジェット

# ラベルと入力フォームをまとめるフレーム
lb1_frame = tkinter.Frame()
lb2_frame = tkinter.Frame()
result_frame = tkinter.Frame()
# ボタンをフレームにしてまとめる(配置のため)
button_frame = tkinter.Frame()

# ラベルを作る
# root,(親)は省略できる
# 入力フォームのラベル
lb1 = tkinter.Label(lb1_frame,text="値１:")
lb2 = tkinter.Label(lb2_frame,text="値２:")
# 結果を表示するラベル
result = tkinter.Label(result_frame,text="結果:")

# 入力フォーム1
e1 = tkinter.Entry(lb1_frame)
# 入力フォーム2
e2 = tkinter.Entry(lb2_frame)


# それぞれ関数をつくる
# 変えたい時はconfigure
# get()で入力フォームの中身を取得

# とりあえずのときは中身にpassと書いておくとエラー出ない
# def add():
#     pass

def add():
    # e1とe2の値を取得してintで数値に変換
    # 結果をresultラベルに表示
    result.configure(text=f"結果: {int(e1.get()) + int(e2.get())}")

def subtract():
    result.configure(text=f"結果: {int(e1.get()) - int(e2.get())}")

def multiply():
    result.configure(text=f"結果: {int(e1.get()) * int(e2.get())}")

def divide():
    # ゼロ除算のエラー処理
    if int(e2.get()) != 0:  # 値2が0でない場合
        result.configure(text=f"結果: {int(e1.get()) / int(e2.get())}")
    else:  # エラーメッセージを表示
        result.configure(text="エラー: ゼロでは割れません！")

def modulo():
    # ゼロ除算のエラー処理
    if int(e2.get()) != 0:
        result.configure(text=f"結果: {int(e1.get()) % int(e2.get())}")
    else:  # エラーメッセージを表示
        result.configure(text="エラー: ゼロでは割れません！")

# ボタンを作る(先に作る)
# ボタンフレームに配置
# command=関数名
bt1 = tkinter.Button(button_frame, text="加算", command=add)
bt2 = tkinter.Button(button_frame, text="減算", command=subtract)
bt3 = tkinter.Button(button_frame, text="乗算", command=multiply)
bt4 = tkinter.Button(button_frame, text="除算", command=divide)
bt5 = tkinter.Button(button_frame, text="剰余", command=modulo)

# パック(表示)はまとめる
# 書いた順に表示される

# フレームの設置
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
result.pack()

# 表示開始
root.mainloop()
