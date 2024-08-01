# 実行アプリ
# rom app import create_app を使って、Flask アプリケーションのインスタンスを作成
# app.run() でサーバーを起動

from app import create_app

# インスタンス作成
app = create_app()

if __name__ == "__main__":
    # WEBサーバー実行
    app.run(host="0.0.0.0",port=5001,debug=True)
