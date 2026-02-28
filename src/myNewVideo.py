import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from manim import *
from common.base_scene import BaseScene
from common.config import *

class MyNewVideo(BaseScene):
    def construct(self):
        # BaseSceneにより背景色は自動設定済み
        
        # 共通設定の色やフォントを使用
        text = Text("Hello Manim", font=DEFAULT_FONT, color=TEXT_COLOR)
        self.play(Write(text))