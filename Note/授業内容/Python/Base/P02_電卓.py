import tkinter as tk

def Calculator(window):
    
    global display  # グローバル変数として宣言
    window.title("シンプル電卓")
    # ディスプレイ（入力と結果表示用）
    display = tk.Entry(window, width=30, justify='right')
    display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
    # ボタンのラベル（数字と記号）
    # 配列で用意
    button_labels = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', 'C', '+'
    ]
    # ボタンの配置
    row = 1
    col = 0
    # forループ:button_labelsから要素を取り出す
    for label in button_labels:
        # tk.Button:ボタンを作る
        # window:ボタンを配置する親
        
        # ラムダ関数を使うことで、各ボタンの値（label）をbutton_click関数に渡すことができる
        # ループ内でlabelの値が変わるたびに、新しいラムダ関数が作成され、その時点でのlabelの値がxのデフォルト値として固定される
        # x=label:ラムダ関数のデフォ値にlabelを設定
        # button_click(x): ラムダ関数が呼び出されたとき、button_click関数をxを引数として呼び出す
        button = tk.Button(window, text=label, width=10, command=lambda x=label: button_click(x))
        button.grid(row=row, column=col, padx=2, pady=2)
        col += 1
        if col > 3:  # 4列まで配置したら次の行へ
            col = 0
            row += 1
    # '='ボタンを作成（幅を2倍に）
    equal_button = tk.Button(window, text='=', width=22, command=calculate)
    equal_button.grid(row=row, column=0, columnspan=4, padx=2, pady=2)

def button_click(value):
    global display
    # ボタンがクリックされたときの処理
    if value == 'C':
        # Cがクリックされたら表示をクリア
        display.delete(0, tk.END)
    else:
        # その他のボタンの場合、表示に追加
        display.insert(tk.END, value)

def calculate():
    global display
    # 計算を実行する
    try:
        # 表示されている式を計算
        result = eval(display.get())
        # 現在の表示をクリアし、結果を表示
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:  # 例外処理
        # エラーが発生した場合（例：無効な式）
        display.delete(0, tk.END)
        display.insert(0, "エラー")

# メインウィンドウを作成
root = tk.Tk()
# 電卓オブジェクトを作成
Calculator(root)
# 実行
root.mainloop()
