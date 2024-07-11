# =========
# ファイルの読み書き
# =========

# ファイルの読み込み
inputFile = open("InputOutput/input.csv",encoding="utf-8")
# ファイルを一行ずつ読み込む処理
print("---ファイルを一行ずつ読み込む処理---")
# for in ループ
for line in inputFile:
    # 一行ずつ文字列データを表示
    # print(line,end="")  #,end=""を付けることで改行しない
    # 文字列データを配列に変換
    list = line.split(sep=",")  # ,で区切った配列が表示される
    print(list)

# 読込中の場所を最初に戻す
inputFile.seek(0)

# 画像のときによく使う
# テキストデータ、全て読み込む
print("--- 全て読み込む ---")
text = inputFile.read()
print(text)

# 改行コードが\rの時
lines = text.split("\r")
if len(lines) == 1:
    # 改行コードが\nの時
    lines = text.split("\n")
print(lines)

# 一つづつのデータを多次元配列に変換
memberList = []
for line in lines:
    memberList.append(line.split(","))
print(memberList)

# 読込中の場所を最初に戻す
inputFile.seek(0)

# 次の行を読み込む
# 1行ずつreadlineを読み込む
print(inputFile.readline(),end="")
print(inputFile.readline(),end="")
print(inputFile.readline(),end="")
print(inputFile.readline(),end="")
print(inputFile.readline(),end="")
print(inputFile.readline(),end="")
print(inputFile.readline(),end="")
print(inputFile.readline(),end="")
print(inputFile.readline(),end="")
print(inputFile.readline(),end="")

# 読込中の場所を最初に戻す
inputFile.seek(0)
# readlineを配列で取得(次の行を読み込むデータを配列で取得)
print(inputFile.readlines())

# ファイルのハンドリングを終了
# 使い終わったらファイルを閉じる
inputFile.close()

# ファイルをオープン（書き込み専用）
# アウトプットファイルを作って、書き込みを行う
outputFile = open("InputOutput/output.csv","wt",encoding="utf-8")  # "wt"は"write text"の略。書き込み
outputFile.write("No.,名前,年齢,性別\n")

# 入れるデータの内容
for data in memberList:
    outputFile.write(",".join(data)+"\n")  # ","で区切って要素を結合

# 使い終わったらファイルを閉じる
outputFile.close()

# withバージョン
# どっち使っても良い
# blockを抜けると自動的にクローズが実行される。
with open("InputOutput/input.csv",encoding="utf-8") as csv:
    print(csv.read())