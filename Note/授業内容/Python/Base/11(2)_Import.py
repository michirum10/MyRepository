# =============
# インポート
# =============

# モジュールをインポート
# モジュールのインポート時に別名を付けられる(短くして読み書きしやすく)
import tkinter as tk

# モジュール名.クラス名
rt = tk.Tk()
rt.title("インポートサンプル01")
rt.geometry("210x100")

lb = tk.Label(text="インポートサンプル01")
lb.pack()

rt.mainloop()