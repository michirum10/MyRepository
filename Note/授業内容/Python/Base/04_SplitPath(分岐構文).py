# =============
# 分岐構文
# =============

# Switch文はない
# 最新バージョンはmatch文がSwitchの代わりに使えるけど代わりにしないほうが良い？


int01 = int(input("値を入力してください。\n>"))

print("--- 分岐構文 ---")
print("--- if文 ---")

print("--| if文 |--")
# {}いらない。インデントが{}の代わり
#「 : 」書く

if int01 >= 60:
    print("60点以上です。")
    
    print("--| if-else文 |--")
if int01 >= 60:
    print("60点以上です。")
else:
    print("60点未満です。")

# swich的に使える
print("--| if-else if-else文 |--")
if int01 >= 80:
    print("80点以上です。")
    # else ifは「elif」
elif int01 >= 60:
    print("60点以上です。")
else:
    print("60点未満です。")

# 三項演算子
# 簡単なものを書くときに使う
str01 = input("はい[Y]いいえ[N]\n>")
# true,if,else
str02 = "[Y]と入力された。" if str01 == "Y" else "[Y]以外が入力された。"
print(str02)
