# パックは一箇所にまとめると良い

# Pythonの標準ライブラリ
import tkinter

# インスタンス化
# tkinter:モジュール
# Tk:クラス
root = tkinter.Tk()
# ウィンドウの背景色
root.configure(bg="#00FFFF")
# ウィンドウのタイトル
root.title("自己紹介")
# ウィンドウのサイズ
root.geometry("400x500+1000+200")

# ラベルを作る
lb = tkinter.Label(text="自己紹介をします。")
# どこに表示するか指定
# なぜか方角で示す
# tkinter.N:北
# tkinter.S:南
# tkinter.E:東
# tkinter.W:西
lb.pack(anchor=tkinter.NW)

# 入力フォームのインスタンス化
e = tkinter.Entry(bg="#FF0000")
# 入力フォームの設置
e.pack(anchor=tkinter.NW)

# ボタンのクリックイベント時の処理
def push_button():
    # 変えたい時はconfigure
    # e(入力フォーム)の中身を取得
    lb.configure(text=f"私の名前は{e.get()}です。")

# ボタンのインスタンス化と同時にコールバック関数の設定
# bt = tkinter.Button(text="紹介",command=コールバック関数)
# コールバックは()で実行されるので、後で書くのが良い
bt = tkinter.Button(text="紹介",command=push_button)
# ボタンの設置
bt.pack(anchor=tkinter.NW)

# キャンパスのインスタンス化
c = tkinter.Canvas(bg="#FFFFFF",height=100,width=100)
# キャンバスの設置
c.pack(anchor=tkinter.NW)
# 線を引く
c.create_line(0,0,60,100,fill="#000000")

# 表示開始
root.mainloop()
# イベントドリブンの仕様
# mainloop:無限に監視する