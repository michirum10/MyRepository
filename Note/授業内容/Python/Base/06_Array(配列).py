# =============
# 配列
# =============
print("-- 配列 --")

# 文字列の配列
# []で囲ったやつはリスト
arr01 = ["a","b","c","d"]
print(arr01)
print(type(arr01))

# 様々な型を混同させることができる。
arr01 = ["a",1,False]
print(arr01)
print(type(arr01))

# 要素の取得方法
print("-- 要素の取得 --")
print(arr01[0])
print(arr01[1])
print(arr01[2])
# 3番目にはなにもないのでエラーになる(IndexError: list index out of range)
# print(arr01[3])

# 配列操作
print("-- 要素の操作 --")
arr01 = [6,4,8,6,5,2]
print(arr01)  # 現在の値を確認

# 要素の追加
arr01.append(3)  # 最後に「3」を追加
print(arr01)

# 要素の挿入
arr01.insert(2,9)  # insert:2番目に「9」を挿入
print(arr01)

# 要素の削除
# その要素の値を削除(インデックスじゃないので気をつける！)
arr01.remove(6)  # remove:一番左の値「6」を削除
print(arr01)

# インデックスを指定して削除する場合は
del arr01[4]  # del:4番目の値を削除
print(arr01)

# 要素を取得してからその要素を削除する。
# pop:最後の値を取得して削除
print(arr01.pop())  # 消す値を表示
print(arr01)  # 消えたか確認

# 要素を取得してからその要素を削除する。(インデックス指定版)
print(arr01.pop(0))
print(arr01)

# 指定した要素の数
print(arr01.count(6))

# 配列の要素数の取得
print(len(arr01))  # length:配列の要素数

# ソート(昇順)
arr01.sort()
print(arr01)

# 全削除
arr01.clear()
print(arr01)


# for文と組み合わせ
arr01 = ["A","B","C","D","E"]

for element in arr01:
    print(element)
else:
    print("出力完了")

print("-- while文と組み合わせ --")
while True:
    if len(arr01) == 0:
        break
    elif len(arr01) == 1:
        print(arr01.pop(0))
    # else:
    #     # 最後の「,」を出さないようにする
    #     print(arr01.pop(0),end=",")

