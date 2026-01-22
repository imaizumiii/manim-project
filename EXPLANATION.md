# Manim YouTube動画制作プロジェクト

数学解説動画をYouTubeに投稿するためのManimプロジェクトです。

## 概要

このプロジェクトは、Manimを使用して数学解説動画を効率的に制作するためのテンプレートとライブラリを提供します。再利用可能なコンポーネント（ロゴ、BGM、スタイル設定、カスタムオブジェクト）を活用し、一貫性のある動画制作を支援します。

## 主な特徴

- 🎨 **統一されたスタイル**: テーマカラーとスタイル設定を一元管理
- 🎵 **BGM管理**: 全編でフェードイン/アウトするBGMを自動適用
- 🖼️ **ロゴ表示**: 全シーンの右下にロゴを常時表示
- 📦 **再利用可能なコンポーネント**: シーン構成、カスタムオブジェクトをライブラリ化
- 🎬 **効率的なワークフロー**: 低品質プレビューから高品質レンダリングまで

## プロジェクト構造

```
manim-lib/
├── videos/                    # 各動画のスクリプト
├── lib/                       # 再利用可能なコード
│   ├── config.py             # テーマカラー、解像度などの設定
│   ├── styles.py             # スタイル設定
│   ├── scenes/               # シーン構成のテンプレート
│   ├── objects/              # カスタムオブジェクト
│   └── utils/                # ユーティリティ関数
├── assets/                    # 静的ファイル（ロゴ、BGMなど）
├── output/                    # レンダリング出力
└── docs/                      # ドキュメント
```

詳細は [ARCHITECTURE.md](./ARCHITECTURE.md) を参照してください。

## セットアップ

### 必要な環境

- Python 3.8以上
- Manim Community Edition（最新版推奨）

### インストール手順

1. リポジトリをクローンまたはダウンロード

2. 依存関係をインストール：
```bash
pip install -r requirements.txt
```

3. Manimをインストール（まだの場合）：
```bash
pip install manim
```

4. 必要なアセットを配置：
   - `assets/logo/logo.png` - ロゴ画像
   - `assets/music/bgm.mp3` - BGMファイル

## 使い方

### 新しい動画を作成する

1. `videos/` ディレクトリに新しいPythonファイルを作成：
```python
from manim import *
from lib.scenes.base_scene import BaseScene

class MyVideo(BaseScene):
    def construct(self):
        # 動画の内容を記述
        pass
```

2. 低品質でプレビュー：
```bash
manim -ql videos/my_video.py MyVideo
```

3. 高品質でレンダリング：
```bash
manim -qh videos/my_video.py MyVideo
```

### レンダリング品質オプション

- `-ql` (low quality): 低品質、高速プレビュー用
- `-qm` (medium quality): 中品質、中間確認用
- `-qh` (high quality): 高品質、最終レンダリング用

## 開発ワークフロー

1. **スクリプト作成**: `videos/` 内に新しい動画スクリプトを作成
2. **低品質プレビュー**: `-ql` オプションで高速に確認
3. **調整・修正**: 必要に応じてスクリプトを修正
4. **最終レンダリング**: `-qh` オプションで高品質動画を生成

## カスタマイズ

### テーマカラーの変更

`lib/config.py` の `THEME_COLORS` を編集してください。

### ロゴの変更

`assets/logo/logo.png` を置き換えてください。

### BGMの変更

`assets/music/bgm.mp3` を置き換えてください。

## ドキュメント

- [ARCHITECTURE.md](./ARCHITECTURE.md) - プロジェクト構造と設計思想
- [PROJECT.md](./PROJECT.md) - 要件定義と仕様

## ライセンス

このプロジェクトは個人利用を想定しています。必要に応じてライセンスを追加してください。

## 貢献

このプロジェクトは個人プロジェクトですが、改善提案やバグ報告は歓迎します。
