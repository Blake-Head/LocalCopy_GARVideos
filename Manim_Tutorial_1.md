Here I am attempting to write a step-by-step basic tutorial for how manim animations are set up, manipulated, and called.  This is based on how I (Blake) understand the system as of late 2024.  More than likely, my process is not the most efficient, but should get us going.

I am writing this in a Jupyter notebook, which is just a file that can contain multiple blocks of different code and words (like here).  I think you should be able to open this and run chunks of code locally within the notebook.  This way, you don't need to set up extra bits of computer environment to test and learn the basics of Manim.

The first block just below this is a starter command that (I think) just checks your system to ensure you actually have manim installed.  If you don't have manim installed, this block will show an error below, saying something to the effect of "No moudle named `manim' ".  If you have manim, nothing notable should happen here.

This also shows you how we will always be loading in the manim library.  This is all done in Python, with manim just being a library of tools within python.  The * symbol means "Take every single tool from the manim box out".  Sometimes, it's more efficient to only import the tools you know you'll be using rather than the entire library, but manim is small enough that we don't care. 

```python
  from manim import *
   
  config.media_width = "75%"
  config.verbosity = "WARNING"
```

Now we begin building our scene.

In manim, all animations are generated in a class called "Scene".  Inside this scence, we will build all objects (colors, sizes, locations) and how they move (or don't move) on the screen via animations. 

All manim scripts will begin with the following:

```python
from manim import *

class SCENE_NAME(Scene):
    def construct(self):
```

Note the the top line in the block below (%%manim -qh SCENE_NAME) is only relevant here in the Jupyter notebook.  You won't be putting this line in your python script.

These first three lines set up our template, but of course, there's nothing there yet.

Let's add something.  Here, I've made a variable named "a_circle".  I can make that variable be equal to whatever I want, but here I've set it equal to a Manim object called "Circle", which is a function within manim that will create a circle of a default width, color, line stroke, and position. 

Let's run this and see what happens. 

```python
%%manim -qh SCENE_NAME1

from manim import *

class SCENE_NAME1(Scene):        # Each chunk of code will begin with these two lines. The first line defines a 'class' called SCENE_NAME, which has the type "scene"
    def construct(self):        # The second line defines the "self" construct.  I'm not entirely sure what this does, but you need it for things to work. 
        a_circle = Circle()     # Define a variable called "a_circle", which will be the MObject "Circle".  Currently, no paramenters are passed to the Circle function. 
```



