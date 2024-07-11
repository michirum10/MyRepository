# =============
# モジュール
# =============

# 勝手に__pycache__キャッシュファイルできる
# Githubにプッシュする必要ないのでignoreしておく

# 動かないときはターミナルのファイルパスを確認
# c:/Users/hit0037/Documents/MyRepository/Note/授業内容/Python/Base/12_Module/Main.py
# ターミナルを一度閉じると治るかも

# クラスを取り込み、利用する
# ファイル名のみでいい
# MemberクラスのMemberモジュールを呼び出す
from Member import Member

# Memberを継承
class ClassMember(Member):
    def __init__(self, name, age, classNumber):
        super().__init__(name, age)
        # 初期化して、引数に入れる
        self.classNumber = classNumber
# 挨拶メソッド
    def greeting(self):
        print(f"私の名前は{self.name}です。")
        print(f"私の年齢は{self.age}です。")
        print(f"{self.classNumber}クラスの皆さんよろしくお願いたします。")

# 呼び出す
member01 = ClassMember("木内",36,"0037")
member01.greeting()

