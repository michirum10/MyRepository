// エントリーポイント
// Vue インスタンスを作成
// App.vue コンポーネントをマウント
// Vue アプリケーションの初期設定
// グローバルなプラグインの設定

import Vue from 'vue'
import App from './components/views/App.vue'
import store from '../../store'

Vue.config.productionTip = false

// Vue インスタンスの作成とルートコンポーネントのマウント（？）
new Vue({
  store,  // ストアを Vue インスタンスに渡す
  render: h => h(App),
}).$mount('#app')
