// 分岐構文

// 出力準備
// HTML内のid="output"を持つ<div>要素を取得し、変数outputに格納
let output = document.getElementById('output')

// 入力準備
// optはhtmlで指定したID
// HTMLドキュメント内のidがoptの要素を取得し、その要素を変数optに格納
let opt = document.getElementById('opt')
// variableは変数という意味
let variable = opt.value

function changeSelect() {
    variable = opt.value
    // 数字として扱うにはNumberで囲う(06_Cast参照)
    // コメントアウトでオンオフ
    // variable = Number(opt.value)
    output.innerHTML = ""

    // if文
    // ブロックで囲った処理を実行するかどうか？の分岐を行う構文
    // ()の中には条件式を入れる
    // 条件式の結果はtrueかfalseになる
    // 特殊パターンが存在する。
    // 文字列の場合は""(空白)がfalse
    // 数値の場合は0がfalse

    if (variable) {
        output.innerHTML += "変数：True"
    }
    output.innerHTML += "<br>"

    // if-else文
    // {}で囲まれてるところがブロック
    // ifブロックで囲った処理は実行するかどうか？
    // ifブロックを実行しない場合はelseブロックを実行する。
    if (variable) {
        output.innerHTML += "変数：True"
    } else {
        output.innerHTML += "変数：False"
    }
    output.innerHTML += "<br>"
    // // if-else if-else文
    // ifブロックで囲った処理は実行するかどうか？
    // ifブロックを実行しない場合はelse ifブロックを処理を実行するかどうか
    // else ifブロックを実行しない場合はelseブロックを実行する。
    // もし、１の場合は"変数：1"、１より大きいときは"変数：1より大きい"、そうじゃないときは、"変数：1より小さい"
    if (variable == 1) {
        output.innerHTML += "変数：1"
    } else if (variable > 1) {
        output.innerHTML += "変数：1より大きい"
    } else {
        output.innerHTML += "変数：1より小さい"
    }

    // 正しいif-else if-else文使い方。
    // variable >= 100とvariable3 > 10が別のブロックになる。
    if (variable >= 100) {
        output.innerHTML += "変数：100以上"
    } else if (variable >= 10) {
        output.innerHTML += "変数：10以上100未満"
    } else {
        output.innerHTML += "変数：10未満"
    }
    output.innerHTML += "<br>"

    // 誤ったif-else if-else文使い方。
    // 順番が大事
    // variable >= 10のブロックが実行されると
    // variable >= 100のブロックが実行されない。(なんの数字が来ても実行されない。)
    if (variable >= 10) {
            output.innerHTML += "変数：10以上100未満"
        } else if (variable >= 100) {
            output.innerHTML += "変数：100以上"
        } else {
            output.innerHTML += "変数：10未満"
        }
        output.innerHTML += "<br>"

        // Switch文
        // 文字打った時、キーワードの横側が四角いアイコンはテンプレートになってる
        // ()内には検索する対象の変数を入れる。(key)
        // ()の中に入れた変数とcaseで定義した値と等価の部分までジャンプする。
        // もしなかった場合はdefaultへジャンプする
        // breakでブロックを抜ける(switchブロックを抜ける)

        switch (variable) {
            // '0'の時
            case '0':
            case '1':
            case '2':
            case '15':
            case '100':
                output.innerHTML += '変数：数値'

                // ブロックを抜ける
                // 複数の条件を書ける
                // 大文字で打っても小文字で打っても'A'と表示される
                // 上が優先
                break;
            case 'A':
            case 'a':
                output.innerHTML += '変数：A'
                break;
            case 'B':
            case 'b':
                output.innerHTML += '変数：B'
                break;
            case 'C':
            case 'c':
                output.innerHTML += '変数：C'
                break;
            default:
                output.innerHTML += '変数：空白'
                break;
        }

    }

changeSelect()