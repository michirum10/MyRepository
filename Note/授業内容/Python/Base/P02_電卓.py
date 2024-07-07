# tkと省略
import tkinter as tk

class Calculator:
    def __init__(self, master):  # コンストラクタを定義？
        self.master = master  # 親ウィンドウの参照を保存？
        master.title("シンプル電卓")

        # ディスプレイ（入力と結果表示用）
        self.display = tk.Entry(master, width=30, justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # ボタンのテキストを定義
        # 配列
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+'
        ]

        # ボタンの配置
        row = 1
        col = 0
        for button in buttons:
            # 各ボタンにクリック時の動作を設定
            cmd = lambda x=button: self.click(x)
            tk.Button(master, text=button, command=cmd, width=10).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:  # 4列まで配置したら次の行へ
                col = 0
                row += 1

        # イコールボタン（幅を2倍に）
        tk.Button(master, text='=', command=self.calculate, width=22).grid(row=row, column=0, columnspan=4, padx=2, pady=2)

    def click(self, key):  #クリックされたボタンの値をself.display
        # ボタンがクリックされたときの処理
        if key == 'C':
            # Cがクリックされたら表示をクリア
            self.display.delete(0, tk.END)
        else:
            # その他のボタンの場合、表示に追加
            self.display.insert(tk.END, key)

    def calculate(self):
        # 計算を実行する
        try:  # 例外が発生する可能性のあるコード
            # Entryウィジェットに表示されている文字列を取得
            # evalは第1引数を式として評価
            result = eval(self.display.get())
            # 現在の表示をクリアし、結果を表示
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except:  # 例外処理
            # エラーが発生した場合（例：無効な式）
            self.display.delete(0, tk.END)
            self.display.insert(0, "エラー")

# メインウィンドウの作成
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()