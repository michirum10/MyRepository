// 配列　array
// マンションの部屋、電車の車両のイメージ
// keyは""で囲む

// 出力準備
let output = document.getElementById('output')

// 配列の生成方法
// []で囲って宣言。今から配列を入れます。中は空
let arr01 = []
// 配列の初期化0番目に木内
// 複数入力はカンマで区切る
// 中身を配列要素という
let arr02 = ["木内", "浦", "傘木"]

// 配列の取得方法
// 左から0,1,2,3...
arr02[0]

// 配列の取得方法
output.innerHTML += arr02[0] + "<br>"
output.innerHTML += arr02[1] + "<br>"
output.innerHTML += arr02[2] + "<br>"

// 配列の上書き
arr02[0] = "木内和也"
output.innerHTML += arr02[0] + "<br>"

// 配列への要素の追加
arr02[3] = '金'
output.innerHTML += arr02[3] + "<br>"

// arr02.lengthで数字を呼び出す
output.innerHTML += arr02.length + '<br>'

// 何番目までデータがあるか分からない時length
// 新しい番号を取得
// []なしだとJS限定で配列を自動で展開
arr02[arr02.length] = '木村'
output.innerHTML += arr02[4] + '<br>'
output.innerHTML += arr02.length + '<br>'


// 配列の最後に追加する。push
// 入門p.156応用p.100
arr02.push('豊岡')
output.innerHTML += arr02 + '<br>'

arr02.unshift('中島')
output.innerHTML += arr02 + '<br>'


// 末尾の要素を取り出す。arr02.pop()
// 途中に入れる
// 末尾の要素を削除(取り出す)
output.innerHTML += arr02.pop() + '<br>'
output.innerHTML += arr02 + '<br>'

// 先頭の要素を取り出して返す。arr02.shift()
output.innerHTML += arr02.shift() + '<br>'
output.innerHTML += arr02 + '<br>'

// 連想配列(Dictionary)　map,hash-map
// 正確にはjsには存在しない。オブジェクト(参照型)という仕組みを連想配列とする。
// keyの名前があっていれば良いので、配列要素が何番目に入ってるかを気にしなくても良い
// 鍵の名前からデータの中身を連想できることから


// 連想配列(オブジェクト)の生成方法
let map01 = {}
let map02 = {
    // key 講師,value 木内
    '講師': '木内',
    '生徒1': '中村',
    // 続ける時　,　を忘れないように。
    '生徒2': '西'
}

// 連想配列の取得方法
// []は文字が使える
output.innerHTML += map02['講師'] + '<br>'
output.innerHTML += map02['生徒1'] + '<br>'
output.innerHTML += map02['生徒2'] + '<br>'
// JSでは存在しないキーを入れた場合undefinedと表示
output.innerHTML += map02[''] + '<br>'

// 連想配列の上書き
map02['講師'] = '木内和也'
output.innerHTML += arr02[0] + '<br>'

// 連想配列への要素の追加
map02['生徒3'] = '羽者家'
// 作った順番と違うこともあるので注意
// Object.valuesはオブジェクトのすべての列挙可能なプロパティの値を取得し、それらを配列として返す
output.innerHTML += Object.keys(map02) + '<br>'
output.innerHTML += Object.values(map02) + '<br>'

// 連想配列(オブジェクト)の生成方法
let map03 = {
    '講師':'木内',
    '生徒1':'中村',
    '生徒2':'西'
}

// 連想配列(オブジェクト)の取得方法
// keyは変数の値なので.変数で取得できる
// 変数として扱うのでkeyの命名には本当は日本語は使わない。
output.innerHTML += map03.講師 + '<br>'
output.innerHTML += map03.生徒1 + '<br>'
output.innerHTML += map03.生徒2 + '<br>'

// 連想配列(オブジェクト)の上書き
map03.講師 = '木内和也'
output.innerHTML += map03.講師 + '<br>'

// 連想配列(オブジェクト)への要素の追加
map03.生徒3 = '羽者家'
output.innerHTML += Object.keys(map03) + '<br>'
output.innerHTML += Object.values(map03) + '<br>'