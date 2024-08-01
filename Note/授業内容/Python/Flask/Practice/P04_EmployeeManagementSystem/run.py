# run.pyを実行

# 読み込むだけで実行できる
from app import app

# # インスタンス生成
# app = app

if __name__ == "__main__":
    # WEBサーバー実行
    app.run(host="0.0.0.0",port=5003,debug=True)