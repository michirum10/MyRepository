// 多次元配列

// 出力準備
let output = document.getElementById('output')

// 2次元配列(多次元配列)
// 配列の中に配列が入ってる
let arr01 = [[]]
let arr02 = [['0-0', '0-1', '0-2'], ['1-0', '1-1', '1-2']]

// 内[]の中を取り出す
output.innerHTML += arr02[0] + '<br>'
output.innerHTML += arr02[1] + '<br>'
// 1-1だけ取り出す
output.innerHTML += arr02[1][1] + '<br>'
// 配列の数を取り出す時は.length
output.innerHTML += arr02[1][1].length + '<br>'


// オブジェクト
let classRoom = {
    // 201 ''で囲ってないので数字として扱う
    ClassNumber: 201,
    // 配列なのでkyeは複数形にする
    teachers: ['木内', '有田', '林'],
    students: ['藤井', '前村', '三田', '森', '森藤', '山崎']
}

output.innerHTML += classRoom.ClassNumber + '<br>'
output.innerHTML += classRoom.students[4]  + '<br>'
