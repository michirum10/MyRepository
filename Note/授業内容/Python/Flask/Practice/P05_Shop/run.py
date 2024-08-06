# run.pyを実行

# パッケージ化したappを読み込むだけで実行できる
from app import app


if __name__ == "__main__":
    # WEBサーバー実行
    app.run(host="0.0.0.0",port=5002,debug=True)


# ctrl+shift+Bで実行

# ターミナル＞タスクの構成＞tasks.json＞other
# run.butファイルを実行したいファイル（run.py）と同じ場所に作る
# run.butにフルパスと実行したいコマンドを書く（/の向き注意）
# 日本語フォルダが文字化けしたら、shift JISに変換
# tasks.jsonの"command"にフルパス（/の向き注意）