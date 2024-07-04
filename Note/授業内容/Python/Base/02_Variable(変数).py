
# Pythonは計算が得意
# 確認するときは右上の三角の実行ボタンを押す

# -------------
# 変数とデータ型
# -------------

# 変数の宣言は不必要
# 初期化は必要
print("--- 整数型 ---")
int01 = 123
print(int01)

# データ型の表示
print(type(int01))
print(type(10))

print("10進数")
print(10)
print("2進数")
print(0b10)
print("8進数")
print(0o10)
print("16進数")
print(0x1c)

print("--- 浮動小数点型 ---")
float01 = 1.23
print(float01)
print(type(float01))

# 指数指定
# eは桁数
print(1.2e-5)
print(type(1.2e-5))

print("--- 文字列型 ---")
# 「' '」と「" "」の違い
str01 = "abc"
str02 = 'abc'

# 「,」で区切る
# 半角スペースが入って表示される
print(str01,str02)
print(type(str01),type(str02))

print("--- 論理型 ---")
# 一文字目大文字
# 小文字で書くとエラーになる
bool01 = True
bool02 = False

print(bool01,bool02)
print(type(bool01),type(bool02))

# 型が指定できる「var:int」varは整数型
# プログラマにとってわかりやすい
# 書かなくても良い
var:int
var = 100
print(var)



