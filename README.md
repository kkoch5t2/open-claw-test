# OpenClaw エージェント分業テストプロジェクト

このプロジェクトは、AIエージェントフレームワーク「OpenClaw」を用いて、**「企画から記事化までを完全自動化するエージェント分業パイプライン」**を構築したテスト環境です。

## 📂 プロジェクト構成

- **`SOUL.md`**: 全体を統括する「編集長エージェント」の振る舞いを定義するメイン設定ファイルです。
- **`skills/researcher/`**: トレンド情報を収集し、記事ネタを決定するリサーチャー用スキル。
- **`skills/writer/`**: トピックをもとに記事を執筆し、HTMLを生成するライター用スキル。
- **`skills/publisher/`**: 生成された記事をWordPressへ投稿（モック）し、SNS告知を行うパブリッシャー用スキル。
- **`*.py` スクリプト**: 今回はテスト用として、実際の外部API（Twitter, WordPressなど）は叩かず、結果をファイル（`draft_result.txt` 等）に出力するダミー処理（モック）で実装しています。

---

## 🚀 環境構築と起動方法

### 前提条件
- **Node.js**: v22.19 以上が必須です。バージョンが古い場合は公式サイトから最新版をインストールしてください。
- **仮想環境について**: OpenClawはNode.jsベースのため、Pythonのような `venv` 等の仮想環境を明示的に作る必要はありません（`node_modules`がその役割を果たします）。また、Pythonスクリプトも標準ライブラリのみで書かれているため `pip` 用の仮想環境も現在は不要です。

### 起動と初回設定（ウィザード）
1. ターミナルでこのディレクトリ（`open-claw-test`）を開きます。
2. 以下のコマンドを実行してOpenClawを起動します。
   ```bash
   npx openclaw
   ```
3. 初回起動時は設定ウィザードが開きます。以下の設定を推奨します。
   - **Setup mode**: `Manual setup`
   - **Gateway**: `Local gateway (this machine)`
   - **Workspace**: デフォルトのパスを消し、現在のディレクトリ（`C:\Users\chiba\site\open-claw-test`）を指定
   - **Provider / Method**: `Google` / `Google Gemini API key` 等を利用（または後述の代替API）
   - **Bind address**: `Loopback (127.0.0.1)`
   - **Protection**: `Token (recommended)`
   - **Hooks / Extra Skills / Search**: 全て `Skip for now`（SpaceキーでチェックしてEnter）
   - **Hatch**: `Hatch in Terminal (recommended)`

---

## ⚙️ モデルの変更・追加方法

OpenClawで動作するAIモデルを変更するには、以下の2つの方法があります。

### 方法1: チャット画面（TUI）から変更する（推奨）
OpenClawのターミナルチャット画面の入力欄で、直接以下のコマンドを打ち込みます。
```text
/model google/gemini-1.5-flash
/model ollama/llama3.2
```

### 方法2: コンフィグ画面から変更する
一度 `Ctrl + C` を2回押してOpenClawを終了させ、設定コマンドを起動します。
```bash
npx openclaw configure
```
メニューから「Model」を選び、`Default model` を `Enter model manually` から任意のモデル名に書き換えて「Done」で保存します。

---

## ⚠️ 今後の運用・設計見直しに向けた重要事項

エージェント運用を行う上で、**API利用枠（Rate Limits）と代替手段**の設計見直しは最も重要な課題となります。

### 1. なぜAPIの利用制限（429エラー）にすぐ引っかかるのか？
エージェントは「1回指示を出したら1回APIを使う」わけではありません。
「どう行動するか考える」→「ツールを実行する」→「ツールの結果を見て次を考える」…と、**1つのタスクを完了するまでに自律的に何度もAPIと通信を行います**。
そのため、API側の無料枠（特に1日あたりの上限が厳しい最新モデルや未課金アカウント）を使っていると、処理速度を遅く設定してもすぐに制限に到達し、エラーで止まってしまいます。

### 2. 今後の運用に向けた解決策（代替手段）
無料で快適なエージェント運用を目指す場合、以下のいずれかのアプローチに設計を見直すことを強く推奨します。

- **ローカルLLMの導入（Ollama） ★おすすめ**
  [Ollama](https://ollama.com/) をインストールし、ご自身のパソコン内でAIを処理させます。クラウドAPIを使わないため**完全に無料・無制限**です。
  設定例: `/model ollama/gemma2` など
- **制限のゆるい別APIの利用（Groq）**
  Googleの代わりに、処理が高速で無料枠の大きい [Groq](https://console.groq.com/) などのAPIを利用します。`.env` に `GROQ_API_KEY` を設定してモデルを切り替えます。
- **有料プラン（課金設定）の有効化**
  Google Cloud等でクレジットカードを登録し、本来の制限を解除して利用します（従量課金）。

### 3. モックから本番環境への移行
テストが正常に動作することを確認できたら、各スキルの `.py` スクリプトを本番用に書き換えます。
- **`fetch_trends.py`**: 実際の X API や Google Trends API を組み込む。
- **`scrape_info.py`**: `BeautifulSoup` や `Selenium` 等を使って実際のサイトからスクレイピングを行う。
- **`post_to_wordpress.py`**: 実際の WordPress REST API（ユーザー名とアプリパスワード等）を利用した通信処理を実装する。
※これら外部パッケージをインストールする段階になった場合は、Pythonの仮想環境（`venv`）を構築してください。
