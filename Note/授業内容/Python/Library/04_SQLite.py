# =============
# データベース
# =============
import sqlite3

# 接続処理
# InputOutputフォルダにPerson.dbができる
con = sqlite3.connect("InputOutput/Person.db")

# 一度のみなので、コメントアウトしておく
# テーブル生成
# SQLをテキストで準備
# 頑張って手打ちする
# sql = "CREATE TABLE person(id,name,gender,age)"
# SQL実行
# con.execute(sql)

# レコード挿入
# ()の中は変数の方が良い(formatかリテラル使う)
sql = "INSERT INTO person VALUES(1,'木内和也',1,35)"
# 実行execute
con.execute(sql)

# 全件取得
sql = "SELECT * FROM person"
res = con.execute(sql)

# カーソル型(Cursor object)なので表示できない
# print(res)
# for文で一つづつ取り出す
for record in res:
    print(record)  #()はタプル？？？

# 更新
# {}で囲う
# 更新の内容は変数にしたほうが良い(formatかリテラル使う)
name = "木内和也1"
sql = "UPDATE person SET name='{}' WHERE id={}".format(name,1)
con.execute(sql)

# オートコミットされないので、まだ反映されない
# コミット
con.commit()
# 接続解除
con.close()