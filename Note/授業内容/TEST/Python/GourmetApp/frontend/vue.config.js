// Vue CLI の設定ファイル
// プロジェクトのビルドや開発サーバーの設定、プロキシ設定
// バックエンドのサーバーにリクエストをプロキシする設定

module.exports = {
    devServer: {
      // 開発サーバーのプロキシ設定
      proxy: 'http://localhost:5001'  // Flask の開発サーバーにプロキシを設定
    }
}
