# =============
# 反復構文
# =============

# for文：指定された回数繰り返すと終了する
# while文：条件を満たさなくなったら終了する

print("--- for文 ---")
# 配列の要素を一つずつ取り出し繰り返し処理を行う。
print("0 - 9")
# rengeが配列を作ってiに入れる
for i in range(10): #配列10個目まで
    # 一文字づつの終わりに「,」を付ける
    print(i,end=",")
print()

print("1 - 9")
# 何から始まって何で終わるのかを引数で指定(配列1個目から,配列10個目で終了)
# range(start, end)
for i in range(1,10):
    print(i,end=",")  # 出力
print()

print("文字を一文字ずつ取り出す")
str01 = "abcdefg"
# 文字はキャラクターなので「c」
for c in str01:
    print(c,end=",")
print()

print("--- while文 ---")
print("0 - 9")
int01 = 0
# 条件は10未満
while int01 < 10:
    print(int01,end=",")
    # インクリメント(++)がないので加算代入する
    int01 += 1
# -------------------------------
# JSのwhile文
# while (index < 10) {
#     output.innerHTML += index
#     index++
# }
# -------------------------------

print("-- continue,break --")
# 乱数を発生させて
# 3の倍数のときは何も表示しない (continue)
# 3の倍数では無い時はメッセージ
# 4の時は終了 (break)

# 乱数ライブラリのインポート
import random
count = 0

while True:
    # カウント1ずつ増える
    count += 1
    # 乱数を発生
    # ランダムライブラリにrandintがある(1から9)
    rnd = random.randint(1,9)
    # 値の表示(float)
    print(f"{count} : {rnd}")
    # 4の倍数のとき
    if rnd == 4:
        # 終了
        break
    # 3の倍数のときは何も表示しない
    elif rnd % 3 == 0:
         continue
    print("3の倍数じゃないよ！")
print(f"{count}回繰り返しました。")


print("-- elseについて --")
# forとwhileに対するelseについて
# forが終わったらelseを実行「出力完了」と表示
# 配列
arr01 = ["A","B","C","D"]
# element:要素
for element in arr01:
    print(element,end=",")
else:
    print("出力完了")

print("-- elseとbreakについて --")
# breakと組み合わせる
# エラーで終了したのか、正常終了したのかを判別できる
for element in arr01:
    print(element,end=",")
    if element == "C":
        # breakで終了した場合はelseが実行されない
        break
# 条件として終了したときはelseを実行
else:
    print("出力完了")
print()  # 改行

# おまけ
# 配列の要素と添字を扱いたい時にenumerate関数を利用する(分割代入)。
# 番号と中身の名前を紐づけたい時
arr02 = ["りんご","みかん","もも","ぶどう","メロン"]
# forの後に2つ書く
# index何番目
# element要素(果物)の名前
# enumerate列挙型
for index,element in enumerate(arr02,1):  # (arr02,1)番号つける1から。数字変えたらその数から始まる
    print(index,element)

