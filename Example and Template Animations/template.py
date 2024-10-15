from manim import *   # This line imports the entire manim library, allows manim functions to be called.

class SCENE_NAME(Scene): # Each chunk of code will begin with these two lines. The first line defines a 'class' called SCENE_NAME, which has the type "scene"
    def construct(self): # The second line defines the "self" construct.  I'm not entirely sure what this does, but you need it for things to work. 
            
            circ = Circle() # Make a Circle called "circ"
            sqr = Square() # Make a Square called "sqr"

            self.play(Create(circ)) # Use the animation "Create" to put circ on the screen
            self.play(FadeIn(sqr)) # Use the animation "FadeIn" to put sqr on the screen

            self.wait(3) # Make the animation wait 3 secons before ending