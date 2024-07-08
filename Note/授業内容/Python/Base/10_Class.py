# =============
# クラス
# =============

# 第一引数はself
# 呼び出すときは自動でselfを渡す

# アトリビュート=JSのプロパティ
class Car:
    # クラス変数の宣言(なくても良い)
    # クラス変数の中のspeed,number
    # アクセスは.でつなぐ
    # あまり使わない。大規模なシステムを扱う際に使われるイメージ
    speed = 0
    number = 0
    
    # イニシャライザ(初期化メソッド)
    # speed=0,number=0：デフォルト引数
    def __init__(self,speed=0,number=0):  # 引数はself=this
        # クラスの中に書くときはメソッドになる
        # 初期化(引数の値をプロパティに代入する)
        self.speed = speed
        self.number = number

    # メソッド
    # 情報表示メソッド
    # 引数でselfを宣言する
    def disp(self):
        print("--------")
        print(f"番号：{self.number}")
        print(f"速度：{self.speed}")

# クラス変数へのアクセス
# 同じ変数名のアトリビュートとは違う
Car.number = 100
Car.speed = -100

# Newしなくて良い
# Car()クラスを呼び出してcar01インスタンスを作る(実体化)
car01 = Car()
# 関数実行
car01.disp()

# アトリビュートへのアクセス
# 書き換えられる
car01.number =  10
car01.speed = 5
car01.disp()

# 引数を渡す
car02 = Car(5,2)
car02.disp()

# 引数名を指定して値を代入できる
car03 = Car(number=100)
car03.disp()

# クラス変数へのアクセス
# アトリビュートとは違う
print(Car.number)
print(Car.speed)

print("------ 継承 ------")

class CarEx(Car):
    # 加速メソッド
    def accel(self,speed=1):
        self.speed += speed

# オーバーライド(親のメソッドと同じ名のメソッド)
# __class__動作させるシステムの値を取得
    def disp(self):
        print("--------")
        print(f"車種：{self.__class__.__name__}")
        # 親のメソッドsuper()の呼び出し
        super().disp()
        
carEx01 = CarEx()
carEx01.disp()
carEx01.accel(5)
carEx01.disp()

# CarEx.disp(carEx01)はcarEx01.disp()と一緒

# 多重継承

# 人を乗せる機能を持った物
class Mobile:
    def __init__(self,driver="名無しさん"):
        self.driver = driver

    def disp(self):
        print(f"運転：{self.driver}")

# CarExに人を乗せる機能を追加
# ()で囲むと継承
class Vehicle(CarEx,Mobile):
    def __init__(self, speed=0, number=0,driver="名無しさん"):
        # 親が２ついる場合はsuper()は使えない
        # selfを忘れないように
        CarEx.__init__(self,speed, number)
        Mobile.__init__(self,driver)

    def disp(self):
        # selfを忘れないように
        CarEx.disp(self)
        Mobile.disp(self)

# 呼び出すときはselfはいらない(クラスから呼び出すときはself必要)
# インスタンス化
vehicle01 = Vehicle()
# 実行
vehicle01.disp()

# 運転手を変える
vehicle02 = Vehicle(driver="木内")
vehicle02.disp()
vehicle02.accel(15)
vehicle02.disp()

# プロトタイプベース
class Robot:
    pass

robot01 = Robot()
robot01.name = "一号機"
robot01.disp = lambda self: print(self.name)
robot01.disp()
