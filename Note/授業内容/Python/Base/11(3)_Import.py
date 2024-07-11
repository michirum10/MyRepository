# =============
# インポート
# =============

# クラスの名前被らないよう注意
# 一つのライブラリのみ使う場合に有効

# 指定したクラスを取り込む
from tkinter import Tk,Label
# モジュールすべてのクラスを取り込む
# from tkinter import *

# クラス名のみ指定
rt = Tk()
rt.title("インポートサンプル01")
rt.geometry("210x100")

lb = Label(text="インポートサンプル01")
lb.pack()

rt.mainloop()