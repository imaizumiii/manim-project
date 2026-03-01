# Manim 数学教材アニメーション

高校数学の概念を視覚的にわかりやすく伝えるアニメーション動画を、Manimで制作するプロジェクトです。

## フォルダ構成

```
common/          共通モジュール（config、BaseScene、再利用コンポーネント）
src/             動画スクリプト（分野別: analysis, algebra, geometry, probability）
docs/            動画ごとの企画書（マークダウン）
manim.cfg        Manim設定（本番用: 1080p/60fps）
```

## 環境構築

### 必須ツール
- Python 3.x
- [Manim Community Edition](https://docs.manim.community/en/stable/installation.html)
- LaTeX（MathTexで数式を使用するため）

### インストール手順

1. Python環境を用意する
2. Manimをインストールする
   ```bash
   pip install manim
   ```
3. LaTeXをインストールする
   - Windows: [MiKTeX](https://miktex.org/) または [TeX Live](https://tug.org/texlive/)
   - macOS: `brew install --cask mactex`

## 実行方法

```bash
# テスト実行（低画質・高速）
manim -ql src/analysis/why_sin_is_wave.py WhySinIsWave

# 本番レンダリング（manim.cfgの設定が適用される）
manim src/analysis/why_sin_is_wave.py WhySinIsWave
```