# =============
# print関数の使い方
# =============

# 反映されると色が変わる

# 一緒に使うことができる
# 覚えてると便利
# sep(区切り文字)とend(語尾文字)
# フォーマット済み文字列リテラル

# 仮引数を指定できる
int01 = int(input("値１を入力してください。\n>"))
int02 = int(input("値２を入力してください。\n>"))

# 複数のデータ出力
print(int01,int02,"abc")
# 区切り文字の変更(defaultは" "(半角スペース))
# sepはセパレーターの略
print(int01,int02,"abc",sep="/")
# 語尾文字の変更(defaultは"\n"(改行コード))
print(int01,int02,"abc",end="です。")
print(int01,int02,"abc",end="です。")
print(int01,int02,"abc",end="です。\n")
print(int01,int02,"abc",end="です。\n")
# 組み合わせることもできる。
# 順番逆でも良い(仮引数を指定できるから)
print(int01,int02,"abc",sep="/",end="です。\n")
print(int01,int02,"abc",end="です。\n",sep="/")

print("--- 文字列内変数の展開 ---")
# ,で区切る
print(int01,int02,"abc",end="です。\n")
# formatメソッド(printではなくstrの機能)
str01 = "数値{}です。".format(int01)
print(str01)
str01 = "数値{}と{}です。".format(int01,int02)
print(str01)
# 配列番号として扱える(1=int02,0=int01)
str01 = "数値{1}と{0}です。".format(int01,int02)
print(str01)
# 連想配列みたいに使える
# プレイスフォルダー
# 先に、仮に入れる予定の変数を置く事ができる
str01 = "数値{A}と{B}です。".format(A=int01,B=int02)
print(str01)

# 文字連結
# str01 = "abc" + int01 これはエラー
# 文字は「""」で囲む必要がある
str01 = "abc" + "def"
print(str01)
# 3回繰り返す
str01 = "abc" * 3
print(str01)

# 書式化演算子
# dは数字
str01 = "数値%d" % int01
print(str01)
# float(小数点以下)
str01 = "数値%f" % int01
print(str01)
# string(文字列)
str01 = "数値%s" % int01
print(str01)

# なんとかリテラル
# フォーマット済み文字列リテラル(JSでいうテンプレートリテラル)
print("--- なんとかリテラル ---")
str01 = f"数値{int01}"
print(str01)

# 生リテラル(raw)
# 書いたものがそのまま表示される
str01 = r"abc/def/ghi\n\n\n"
print(str01)
str01 = "abc/def/ghi\n\n\n"
print(str01)

# バイト列リテラル(bytes)
str01 = b"abc/def/ghi\n\n\n"
print(str01)
# 型を見る
print(type(str01))

# Unicodeに変換する
str01 = u"abc/def/ghi\n\n\n"
print(str01)
print(type(str01))
# .encodeでも変換できる
# ()の中に文字コードを指定
str01 = "abc/def/ghi\n\n\n".encode('utf-8')
print(str01)
print(type(str01))
