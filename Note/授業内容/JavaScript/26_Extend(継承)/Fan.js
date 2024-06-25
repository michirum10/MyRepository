// 扇風機クラス
export default class Fan {
    // プロパティ

    // クラスプロパティ
    // 台数
    static #number = 0

    // 全体の状態出力先
    static #output

    // 扇風機のコレクションオブジェクト
    static #fanList = {}

    // クラス定数
    // windPowerの日本語名称の統一用定数
    static #POWER_STATUS = { OFF: '切', P1: '弱', P2: '中', P3: '強' }

    // プライベートプロパティ
    // シリアルナンバー
    #serialNumber
    // 羽根の枚数
    #blades
    // 風力
    #windPower
    // 電源
    #power
    // 首振り
    #swing
    // 状態の出力先
    #deviceOutput
    // カードの要素
    #block

    // 全デバイスのオブジェクトリスト取得
    static get fanList() {
        return Fan.#fanList
    }

    // blockのゲッター
    get block() {
        return this.#block
    }

    // クラスメソッド
    // 扇風機の統計情報の表示
    static infoFans() {
        if (Fan.#output == undefined) {
            Fan.#output = document.getElementById('output')
        }
        Fan.#output.innerHTML += `扇風機の台数は全部で${Fan.#number}台です。`
    }

    // コンストラクタ(メソッド)の宣言
    constructor(blades = 5) {
        // 扇風機の台数に一台追加        
        Fan.#number++
        this.#serialNumber = Fan.#number
        // 各値を初期化
        this.#blades = blades
        this.#windPower = Fan.#POWER_STATUS.OFF
        this.#power = false
        this.#swing = false

        // #outputが設定されていない時、初期設定を行う処理
        if (Fan.#output === undefined) {
            Fan.#output = document.getElementById('output')
        }

        // ブロック生成(divタグの生成)
        let block = document.createElement('div')
        // 各扇風機ブロックにIDを付与(シリアルナンバー)
        block.id = this.#serialNumber

        // 各扇風機ブロックの出力部分のdivタグを生成
        this.#deviceOutput = document.createElement('div')

        // blockの子要素に各扇風機ブロックの出力部分を追加
        block.appendChild(this.#deviceOutput)

        // 全体の状態出力先の子要素に各扇風機ブロックを追加
        Fan.#output.appendChild(block)

        // 切ボタン生成
        createFanBtn(Fan.#POWER_STATUS.OFF, () => this.pressPowerButton(Fan.#POWER_STATUS.OFF), block)

        // 弱ボタン生成
        createFanBtn(Fan.#POWER_STATUS.P1, () => this.pressPowerButton(Fan.#POWER_STATUS.P1), block)

        // 中ボタン生成
        createFanBtn(Fan.#POWER_STATUS.P2, () => this.pressPowerButton(Fan.#POWER_STATUS.P2), block)

        // 強ボタン生成
        createFanBtn(Fan.#POWER_STATUS.P3, () => this.pressPowerButton(Fan.#POWER_STATUS.P3), block)

        // 首振りボタン生成
        createFanBtn('首振り', () => this.pressSwingButton(), block)

        // 情報表示
        this.infoView()

        // カード情報の保存
        this.#block = block

        // データの管理
        Fan.#fanList[this.#serialNumber] = this

    }

    // メソッド(関数)

    // パワーボタングループ押下
    pressPowerButton(btnName) {
        console.log(`パワーボタン『${btnName}』が押されました。`)
        switch (btnName) {
            case Fan.#POWER_STATUS.OFF:
                // 風力0
                this.#windPower = Fan.#POWER_STATUS.OFF
                // 電源OFF
                this.#power = false
                break;
            case Fan.#POWER_STATUS.P1:
                // 風力1
                this.#windPower = 1
                // 電源ON
                this.#power = true

                break;
            case Fan.#POWER_STATUS.P2:
                // 風力2
                this.#windPower = 2
                // 電源ON
                this.#power = true

                break;
            case Fan.#POWER_STATUS.P3:
                // 風力3
                this.#windPower = 3
                // 電源ON
                this.#power = true

                break;

            default:
                break;
        }
        this.infoView()
    }

    // 首振りボタン押下
    pressSwingButton() {
        console.log('首振りボタンが押されました。')
        // 現在の状態を反転させる処理
        this.#swing = !this.#swing
        this.infoView()
    }

    // 状態確認
    // ${addInfo}で表示する情報をカスタム
    infoView(addInfo = '') {
        this.#deviceOutput.innerHTML = `
        羽根の枚数：${this.#blades}<br>
        風力：${this.#windPower}<br>
        電源：${this.#power}<br>
        首振り：${this.#swing}<br>
        ${addInfo}
        TimeStamp：${new Date()}<br>        `
    }

}

// 扇風機のボタン生成関数
function createFanBtn(value, handler, parent) {
    // ボタン生成
    // inputタグを生成
    let btn = document.createElement('input')

    // ボタンの各設定
    // タイプの指定
    btn.type = 'button'
    // valueの指定
    btn.value = value
    // イベントの指定
    btn.addEventListener('click', handler)

    // ボタンをblockの子要素に追加
    parent.appendChild(btn)
}

// Fanをスーパークラスとして継承し、PortableFanを定義する。
export class PortableFan extends Fan {
    // サブクラスのプロパティ
    // バッテリー
    // #battery
    battery


    // サブクラスのコンストラクタ
    constructor(blades = 5) {
        // スーパークラスのコンストラクタを実行
        super(blades)

        // サブクラスのプロパティを初期化
        // this.#battery = 100
        this.battery = 100
        const br = document.createElement('br')
        this.block.appendChild(br)
        createFanBtn('充電', () => this.chargeBattery(10), this.block)

        this.infoView()
    }

    // サブクラスでスーパークラスのメソッドをオーバーライドすると、
    // サブクラスのプライベートプロパティが利用不可のエラーが発生するため、
    // batteryはパブリック(#付けない)に変更
    // get battery(){
    //     return this.#battery
    // }

    // サブクラス専用メソッド
    chargeBattery(num) {
        //     this.#battery += num
        this.battery += num
        this.infoView()
    }

    dischargeBattery(num) {
        // this.#battery -= num
        this.battery -= num
        this.infoView()
    }
    // 親のメソッドを上書き
    // エラー出るので#は外す
    // オーバーライド
    infoView() {
        super.infoView(`残電力：${this.battery}<br>`)
    }

}