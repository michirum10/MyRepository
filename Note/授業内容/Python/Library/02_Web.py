# =============
# Web
# =============

# https://pypi.org/
# で調べてインストールできる(偽物に注意)
# pip install requests
# コンソールに貼り付けしてインストール

import requests
import json

# DogAPI
URL = "https://dog.ceo/api/breeds/image/random"
# リクエストを送信し、レスポンスを取得(HTTP通信を開始)
res = requests.get(URL)   #getとpostのget
# レスポンスのテキストデータを取得
dat = res.text
# テキストをjson解析(dict型(ディクショナリー)に変換)
dic = json.loads(dat)
# 表示(URLのみを取得)
print(dic["message"])

# 犬の画像の取得
res2 = requests.get(dic["message"])
# テキストデータをバイナリデータとして取得
dat2 = res2.content
# ファイルを(バイナリデータの)画像データとして書き込み
file = open("InputOutput/dog.jpg","wb")  # write binary
# 書き込み
file.write(dat2)
# 書き込み終了
file.close()