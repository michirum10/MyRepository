# =============
# 関数
# =============

# 関数の定義
# 「def」を使う
def add(x,y):
    print(x+y)

# 関数の呼び出し
# 足し算
add(3,5)
# 文字連結
add("aaa","bbb")
# 数字と文字は型が違うのでエラー
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# add(3,"aaa")

# 型指定(プログラムを実行時にはエラーにならないが、
# プログラミング中のヒントになる。)
def add2(x:int,y:int):
    print(x+y)
# エラーにならない
add2("a","b")

# 文字と数字混ぜたい時

# キャストで対策
def add_ex(x,y):
    # キャスト
    num1 = int(x)
    num2 = int(y)
    print(num1+num2)

add_ex("1",3)

# 型確認で対策
def add_ex2(x,y):
    # isinstanceでx,yの型(int,float)を確認
    if isinstance(x,(int,float)) and isinstance(y,(int,float)):
        print(x+y)

add_ex2("3",3)  # 表示されない
add_ex2(5,3)
add_ex2(5.3,3.2)

# 戻り値

def add_re(x,y):
    return x + y

print(add_re(4,6))  # 4+6=10の結果を表示

# 仮引数の指定
def say(name,msg):
    print(f"{name}さんは「{msg}」と言っている。")

say("A","こんにちは")
# 変数の中身を変えられる
say(msg="こんばんは",name="B")

# デフォルト引数(指定できるのは後(右側)の引数のみ)
def say(msg,name="名無しの権兵衛"):
    print(f"{name}さんは「{msg}」と言っている。")

say(msg="こんばんは")



