// 例外処理について

// 出力先の要素を習得
let output = document.getElementById('output')
let output2 = document.getElementById('output2')


// 実行するとエラーが発生する
// output.innerHTML = "存在する"
// output2.innerHTML = "存在しない"
// output.innerHTML = "存在する"

// 例外処理の基本
try {
    // 例外が発生しうる処理
    output.innerHTML = "存在する"
    // 実行するとエラーが発生する可能性のある部分
    output2.innerHTML = "存在しない"
    output.innerHTML = "存在する"
} catch (error) {
    // 例外が発生した時
    output.innerHTML = "エラー対応済み"
} finally {
    // 何があっても実行される
    output.innerHTML += '<br>ファイナリー<br>'
}
// エラーが発生することを投げるという
// try-catch文は、例外が発生した場合はcatch文が実行され、例外が発生しなかった場合はfinally文が実行される

function div(num1, num2) {
    if (num2 == 0) {
        throw new Error("0では割れません。")
    }
    return num1 / num2
}
// 実行するとエラーが発生する
// output.innerHTML += div(3,0)

try {
    output.innerHTML += div(3, 0)
} catch (error) {
    // errorにはエラーの情報が入っている。(本来コンソールに出る予定だったもの)
    output.innerHTML += error.message
} finally {
    output.innerHTML += '<br>ファイナリー<br>'
}

