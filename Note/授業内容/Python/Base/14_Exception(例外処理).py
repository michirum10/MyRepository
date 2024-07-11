# =============
# 例外処理
# =============

# 入力受付
inputStr = input("整数を入力してください。\n>")

# 例外処理
try:
    # 例外が発生する可能性のある処理
    inputInt = int(inputStr)
    print(inputInt + 100)
except:
    # 例外が発生した時の処理
    print("エラー発生")

# 例外処理(エラー指定)
try:
    # 例外が発生する可能性のある処理
    inputInt = int(inputStr)
    print(100 / inputInt)
    # エラー名を指定
except ValueError as ex:  # asで別名を付ける
    # 例外が発生した時(整数変換失敗)の処理
    print("整数を入力してください。")
    print(ex.args)
    # エラー名を指定
except ZeroDivisionError:
    # 例外が発生した時(0割エラー)の処理
    print("0で割らないでください。")
except:
    # その他の例外が発生した時の処理
    print("想定外のエラーが発生しました。")

# Finallyについて
try:
    # 例外が発生する可能性のある処理
    inputInt = int(inputStr)
    print(inputInt + 100)
except:
    # 例外が発生した時の処理
    print("エラー発生")
finally:
    print("エラーが発生してもしなくても実行します。")
print("プログラムが終了しました。")

# elseについて
try:
    # 例外が発生する可能性のある処理
    inputInt = int(inputStr)
    ans = 100 / inputInt
except:
    # 例外が発生した時の処理
    print("エラー発生")
else:
    # 例外が発生する可能性がある処理を成功した時
    print(ans)
finally:
    print("エラーが発生してもしなくても実行します。")

print("プログラムが終了しました。")