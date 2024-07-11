# =============
# モジュール
# =============

# 勝手に__pycache__キャッシュファイルできる
# Githubにプッシュする必要ないのでignoreしておく

# クラスの作成
# メンバークラス
class Member:
    def __init__(self, name, age):
        # アトリビュート
        self.name = name
        self.age = age

# 読み込むときにも実行される
print(f"{__name__}を読み込みました。")
# Memberで読み込まれたとき：__main__を読み込みました。
# Mainで読み込まれたとき：Memberを読み込みました。

# テストコードを書くことができる
# 実行したときと読み込まれたときで違う
if __name__ == "__main__":
    print("---- テストコード ----")
    member01 = Member("木内",36)
    print(f"名前は{member01.name}です。")
    print(f"年齢は{member01.age}です。")