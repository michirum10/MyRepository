# GourmetApp

GourmetApp は、飲食店の情報を管理・表示するためのアプリケーションです。ユーザーは飲食店を検索し、レビューやお気に入りリストを作成できます。

## 特徴

- **ユーザーアカウント**: アカウント作成とログイン機能
- **お気に入りリスト**: お気に入りの飲食店を保存
- **フィルタリングとソート**: 料理の種類や価格帯で検索
- **レビューとコメント**: 飲食店にレビューを投稿し、コメントを追加
- **地図のカスタマイズ**: マーカーのクラスタリングやカスタムマーカー

## 技術スタック

- **バックエンド**: Flask (Python)
- **フロントエンド**: Vue.js
- **データベース**: SQLite
- **デプロイ**: Heroku

## セットアップ方法

### バックエンドのセットアップ

1. **仮想環境の作成**（Python）:
    python -m venv venv
    source venv/bin/activate  # Windows の場合は venv\Scripts\activate

2. **依存関係のインストール**:
    pip install -r backend/requirements.txt

3. **データベースの初期化**:
    flask db init
    flask db migrate
    flask db upgrade

4. **バックエンドの起動**:
    python backend/run.py

### フロントエンドのセットアップ

1. **依存関係のインストール**（Node.js）:
    cd frontend
    npm install

2. **フロントエンドの起動**:
    npm run serve

## デプロイ

1. **Heroku へのデプロイ**:
    - Heroku CLI をインストールし、ログイン:
      heroku login

    - Heroku アプリを作成:

      heroku create

    - デプロイ:
      git push heroku main

    - データベースの設定（必要に応じて）:
      heroku run flask db upgrade

## 使用方法

1. **アカウント作成**: アプリケーションにアクセスし、アカウントを作成します。
2. **ログイン**: 作成したアカウントでログインします。
3. **飲食店の検索**: 検索機能を使用して飲食店を探します。
4. **お気に入りの管理**: お気に入りの飲食店をリストに追加します。
5. **レビューの投稿**: 飲食店にレビューを投稿し、コメントを追加します。

## コントリビューション

1. **フォーク**: このリポジトリをフォークして、自分の変更を加えます。
2. **プルリクエスト**: 変更が完了したら、プルリクエストを作成して変更を提案します。

## ライセンス

このプロジェクトは [MIT ライセンス](LICENSE) の下でライセンスされています。

<!-- Procfile
web: gunicorn app:app
web: Heroku のためのプロセスタイプです。gunicorn は WSGI サーバーで、app:app は app モジュール内の app インスタンスを指します。 -->
