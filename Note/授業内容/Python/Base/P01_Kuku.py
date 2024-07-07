# 九九
print()  # 改行 

# 1の段から9の段までの答えを出力してください。
print("--- 九九の答えのみ ---")
for i in range(1,10):  # 1から10番目まで
    for j in range(1,10):
        print(i * j,end=",")
print()  # 改行    
print()  # 改行    

# 1の段から9の段までの式と答えをセットで出力してください。
print("--- 九九の式と答え ---")
for i in range(1,10):  # 1から10番目まで
    for j in range(1,10):
        print(f"{i} x {j} = {i*j:2}",end="  ")  # セットで出力(==i * j)
    print()  # 改行
print()  # 改行

# フォーマット済み文字列リテラル(JSでいうテンプレートリテラル)
# print("--- なんとかリテラル ---")
# str01 = f"数値{int01}"
# print(str01)

# 1の段から9の段までの九九表を出力してください。
print("--- 九九表 ---")
for i in range(1,10):  # 1から10番目まで
    for j in range(1,10):
        print(i * j,end=" ")
    print()  # 段で改行
print()  # 改行

# フォーマット式文字リテラル
# f'{i * j:2}'で2桁の幅に書式設定できる
print("--- 九九表ｆリテラル ---")
for i in range(1,10):  # 1から10番目まで
    for j in range(1,10):
        # ：（コロン）を付けることで書式設定できる
        # {i * j}を「フィールド幅：2」に設定
        print(f'{i * j:2}',end=" ")
    print()  # 段で改行
print()  # 改行