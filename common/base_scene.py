from manim import *
from common.config import *

class BaseScene(Scene):
    """
    プロジェクト共通の基底シーンクラス。
    全ての動画スクリプトはこのクラスを継承してください。
    
    機能:
    - 共通の背景色を適用
    - 共通の設定ファイルを読み込み済み
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def setup(self):
        """
        各シーンの生成前に実行される初期化処理
        """
        # 1. 背景色の適用
        self.camera.background_color = BACKGROUND_COLOR
        
        # 2. テキストのデフォルトスタイルの適用（概念的実装）
        # ManimのTextクラスはインスタンス生成時に引数を取るため、
        # ここでグローバルに強制するのは難しいですが、
        # configの値を利用するように設計しています。
        
        # 親クラスのsetupを呼び出す
        super().setup()

    def construct(self):
        """
        メインの描画ロジック。
        サブクラスでオーバーライドして記述します。
        """
        pass
