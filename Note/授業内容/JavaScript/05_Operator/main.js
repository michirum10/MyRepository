// 演算子

// 出力準備
// 変数outputを宣言して初期化
// getElementById HTMLタグで指定したID('output')を取得
let output = document.getElementById('output')

// 代入演算子『=』
// 右辺の値を左辺の変数に格納する。
let str1 = '森美智瑠'

// 算術演算子
// 変数resultを宣言して初期化
let result = ''

let num1 = 3
let num2 = 5


// 四則演算

// 加算 +
result = num1 + num2
output.innerHTML += result
output.innerHTML += '<br>'

// 減算 -
result = num1 - num2
output.innerHTML += result
output.innerHTML += '<br>'

// 乗算 *
result = num1 * num2
output.innerHTML += result
output.innerHTML += '<br>'

// 除算 /
result = num1 / num2
output.innerHTML += result
output.innerHTML += '<br>'

// 剰余算 %
// あまり算
result = num1 % num2
output.innerHTML += result
output.innerHTML += '<br>'

// ++インクリメント、--デクリメント
// Pythonにはない
// イコールいらない。代入もする
output.innerHTML += '- インクリメント、デクリメント -'
output.innerHTML += '<br>'

let num3 = 5
// インクリメント(増加、値を１足す) ++
num3++
output.innerHTML += num3
output.innerHTML += '<br>'

// デクリメント(減少、値を１引く) --
num3--
output.innerHTML += num3
output.innerHTML += '<br>'

// 前置加算 ++を先に
// 前置演算では先にインクリメント（またはデクリメント）を行ってから他の処理を行う
output.innerHTML += ++num3
output.innerHTML += num3
output.innerHTML += '<br>'
// 後置加算 後に++
// 後置演算では先に他の処理を行ってから最後にインクリメント（またはデクリメント）を行う
output.innerHTML += num3++
output.innerHTML += num3
output.innerHTML += '<br>'

// 前置減算 --を先に
output.innerHTML += --num3
output.innerHTML += num3
output.innerHTML += '<br>'
// 後置減算　後に--
output.innerHTML += num3--
output.innerHTML += num3
output.innerHTML += '<br>'

// 代入演算子
// 加算代入しか使わない
output.innerHTML += '- 代入演算子 -'
output.innerHTML += '<br>'

let num4 = 5

// 加算代入 +=
num4 += 2
output.innerHTML += num4
output.innerHTML += '<br>'

// 減算代入 -=
num4 -= 2
output.innerHTML += num4
output.innerHTML += '<br>'

// 乗算代入 *=
num4 *= 2
output.innerHTML += num4
output.innerHTML += '<br>'

// 除算代入 /=
num4 /= 2
output.innerHTML += num4
output.innerHTML += '<br>'

// 剰余算代入 %=
num4 %= 2
output.innerHTML += num4
output.innerHTML += '<br>'

// 比較演算子
// 結果がTrueかFalse
output.innerHTML += '- 比較演算子 -'
output.innerHTML += '<br>'

num5 = 5
num6 = 5
num7 = 6

// 等価 ==
result = num5 == num6
output.innerHTML += result
output.innerHTML += '<br>'
result = num5 == num7
output.innerHTML += result
output.innerHTML += '<br>'

// 否定 !=
result = num5 != num6
output.innerHTML += result
output.innerHTML += '<br>'
result = num5 == num7
output.innerHTML += result
output.innerHTML += '<br>'

// 3つパターン
// 厳密等価 ===
// 左側の値と右側の値が同じか「型まで含めて」比較するときに使う演算子
result = num5 === num6
output.innerHTML += result
output.innerHTML += '<br>'
result = num5 === num7
output.innerHTML += result
output.innerHTML += '<br>'

// 厳密否定 !==
result = num5 !== num6
output.innerHTML += result
output.innerHTML += '<br>'
result = num5 !== num7
output.innerHTML += result
output.innerHTML += '<br>'

// 小なり <
result = num5 < num6
output.innerHTML += result
output.innerHTML += '<br>'
result = num5 < num7
output.innerHTML += result
output.innerHTML += '<br>'

// 大なり >
result = num5 > num6
output.innerHTML += result
output.innerHTML += '<br>'
result = num5 > num7
output.innerHTML += result
output.innerHTML += '<br>'

// 以下 <=
result = num5 <= num6
output.innerHTML += result
output.innerHTML += '<br>'
result = num5 <= num7
output.innerHTML += result
output.innerHTML += '<br>'

// 以上 >=
result = num5 >= num6
output.innerHTML += result
output.innerHTML += '<br>'
result = num5 >= num7
output.innerHTML += result
output.innerHTML += '<br>'

// 論理演算子
output.innerHTML += '- 論理演算子 -'
output.innerHTML += '<br>'

// かつ &&
let bool1 = true
let bool2 = true
let bool3 = false
result = bool1 && bool2
output.innerHTML += result
output.innerHTML += '<br>'
result = bool1 && bool3
output.innerHTML += result
output.innerHTML += '<br>'

// または ||
result = bool1 || bool2
output.innerHTML += result
output.innerHTML += '<br>'
result = bool1 || bool3
output.innerHTML += result
output.innerHTML += '<br>'

// 否定 
result = !bool1
output.innerHTML += result
output.innerHTML += '<br>'
result = !bool3
output.innerHTML += result
output.innerHTML += '<br>'

// 文字列演算子
output.innerHTML += '- 文字列演算子 -'
output.innerHTML += '<br>'

let str4 = '森'
let str5 = '美智瑠'
result = str4 + str5
output.innerHTML += result
output.innerHTML += '<br>'
let str6 = '100'
let str7 = '200'
result = str6 + str7
output.innerHTML += result
output.innerHTML += '<br>'




// 使い方の具体例
output.innerHTML += '- 比較演算子＋論理演算子の使い方の具体例 -'
output.innerHTML += '<br>'
// 値6 ～ 12の時true
// 6以上　かつ　12以下　と言い換えられる
num7 = 8
num8 = 14

// ()で優先的に計算
result = (6 <= num7) && num7 <= 12
output.innerHTML += result
output.innerHTML += '<br>'
result = 6 <= num8 && num8 <= 12
output.innerHTML += result
output.innerHTML += '<br>'

// 論理演算子がややこしい時は変数に置き換える
r1 = p1()
r2 = p2()
r1 && r2

// p1が実行された後にp2が実行される
p1() && p2()

output.innerHTML += '- 厳密等価の使い方の具体例 -'
output.innerHTML += '<br>'
let str2 = 1
let str3 = '1'

// 等価 ==
// こっち覚えとく
result = str2 == str3
output.innerHTML += result
output.innerHTML += '<br>'

// 厳密等価 ===
// 右側の値と左側の値は、変数の型まで含めて同じか？
// 動きが怪しい時はこいつを疑う
// 言語によって意味が違う
result = str2 === str3
output.innerHTML += result
output.innerHTML += '<br>'
