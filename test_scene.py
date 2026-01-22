from manim import *

class FirstScene(Scene):
    def construct(self):
        # --- 1. 定義（const element = ... のようなもの） ---
        circle = Circle()  # 円を作る
        square = Square()  # 正方形を作る

        # --- 2. スタイル設定（CSSのようなもの） ---
        circle.set_fill(WHITE, opacity=0.5)  # ピンクで塗りつぶす
        square.set_fill(BLUE, opacity=0.5)  # 青で塗りつぶす

        # --- 3. アニメーション実行（ここがManimの本体） ---
        
        # 円を描画する（1秒かけて）
        self.play(Create(circle))
        
        # 円を正方形に変形させる（1秒かけて）
        self.play(Transform(circle, square))
        
        # 1秒待機
        self.wait(1)
        
        # フェードアウトして消す
        self.play(FadeOut(circle)) 
        # ※変形(Transform)したので、実体はsquareになっていますが、
        # 変数名はcircleのまま扱われるのがPythonのクセです
        
class LatexCheck(Scene):
    def construct(self):
        # MathTex は内部でLaTeXコンパイラを呼び出します
        # r"..." の r は、バックスラッシュをエスケープしないための記述です
        equation = MathTex(
            r"\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}"
        )
        
        # 見やすいように大きくする
        equation.scale(2)
        
        # アニメーションなしでパッと表示（確認用）
        self.add(equation)
