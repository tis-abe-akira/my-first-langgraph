# LangGraph Examples

このプロジェクトは[LangGraph](https://github.com/langchain-ai/langgraph)を使用した様々なグラフ処理パターンの実装例を提供します。

## 機能概要

このリポジトリには以下の実装例が含まれています：

### 1. 基本的なグラフ処理 (basic_graph.py)
- シンプルなグラフ構造の実装
- ノード間の基本的な接続
- Mermaidを使用したグラフの可視化

### 2. メッセージグラフ (message_graph.py)
- メッセージベースのグラフ処理
- メッセージの連鎖的な処理フロー

### 3. 状態グラフ (state_graph.py)
- 状態を保持するグラフ処理
- ChatGPT (GPT-4) との連携
- API呼び出し回数の追跡

### 4. 条件付きエッジ (conditional_edge.py)
- 条件に基づくグラフの分岐処理
- LangChainツールとの統合
- カスタムデータベースAPIの模擬実装

## 技術スタック

- Python
- LangGraph
- LangChain
- OpenAI API (ChatGPT)
- Poetry (依存関係管理)

## プロジェクト構造

```
my-first-langgraph/
├── src/
│   ├── basic_graph.py      # 基本的なグラフ処理
│   ├── message_graph.py    # メッセージベースのグラフ
│   ├── state_graph.py      # 状態を持つグラフ
│   ├── conditional_edge.py # 条件付きエッジの実装
│   └── utils.py           # ユーティリティ関数
├── poetry.lock
└── pyproject.toml
```

## セットアップ

1. Poetryのインストール
2. 依存関係のインストール:
```bash
poetry install
```

3. 環境変数の設定:
```bash
export OPENAI_API_KEY=your_api_key
```

## 使用例

各実装例は個別のPythonファイルとして提供されており、それぞれ実行可能です。

例えば基本的なグラフ処理を実行する場合：

```bash
poetry run python src/basic_graph.py
```

実行後、`out/basic_graph.html`にグラフの可視化結果が生成されます。
