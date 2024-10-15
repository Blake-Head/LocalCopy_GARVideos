from manim import *   # This line imports the entire manim library, allows manim functions to be called.

class SCENE_NAME(Scene): # Each chunk of code will begin with these two lines. The first line defines a 'class' called SCENE_NAME, which has the type "scene"
    def construct(self): # The second line defines the "self" construct.  I'm not entirely sure what this does, but you need it for things to work. 

        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
        # Test comment