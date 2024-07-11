# ==========
# クロージャ
# ==========

# 閉鎖関数(関数を返す関数???)
def enclosure(x):    # xは変化しない変数(レキシカルスコープ)
    def closure(y):  # yは変化する変数(ダイナミックスコープ)
        return x + y
    return closure

# int10のxの値が10で確定する
int10 = enclosure(10)

# int33のxの値が33で確定する
int33 = enclosure(33)

print(int10(50))
print(int33(50))

# 定数として扱いたいときに使う
# コールバック関数を使うときに効果を発揮する
# 分岐するときに使うと便利