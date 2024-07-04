# =============
# 演算子
# =============

print("--- 演算子 ---")
print("--- 四則演算子 ---")

# 標準入力input(引数)
# \n:改行,>:入力欄それっぽく見せる
str01 = input("値１を入力してください。\n>")
# 型変換(文字列型→整数型)
# Cast
int01 = int(str01)

int02 = int(input("値２を入力してください。\n>"))

# 加算
print(int01 + int02)
# 減算
print(int01 - int02)
# 乗算
print(int01 * int02)
# 除算
print(int01 / int02)
print(type(int01 / int02))
# 商
print(int01 // int02)
print(type(int01 // int02))
# 剰余算
print(int01 % int02)
print(type(int01 % int02))
# 冪乗(べき乗)
print(int01 ** int02)

print("--- 代入演算子 ---")
# 代入
int03 = 10
print(int03)
# 加算代入等
int03 += 3
print(int03)
int03 **= 4
print(int03)

# インクリメント、デクリメントは存在しない
# i = 10
# i++

print("--- 比較演算子 ---")
bool01 = 10 != 1
print(bool01)

print(10 == 1)
print(10 != 1)
print(10 >= 1)
print(10 >  1)
print(10 <= 1)
print(10 < 1)

print("--- 論理演算子 ---")
# かつ
print(True and True)
# または
print(True or True)
# 否定
print(not True)
# 等価
print(1 is 1)
# 不等価
print(1 is not 1)

# 配列の中に存在するか確認する演算子
print(3 in [1,2,3,4,5,6,7,8,9])
print(3 not in [1,2,3,4,5,6,7,8,9])

