// 出力準備
let output = document.getElementById('output')

// GETパラメータの取得する処理
// ()今開いてる場所のパス
let url = new URL(window.location.href)
// パラメーター。複数系。情報を受け取る
let params = url.searchParams
let msg = params.get('msg')

output.innerHTML = msg

