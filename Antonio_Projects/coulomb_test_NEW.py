from manim import *
import numpy as np

# Coulomb's Law Scene with R Updates
class CoulombNEW(Scene):
    def construct(self):
        # Define our initial variables
        q1 = 11
        q2 = 2
        k = 1

        # Placing the Charges on-screen (can be changed)
        dot1 = Dot(color=RED).shift(LEFT * 3 + UP * 1)
        dot2 = Dot(color=BLUE).shift(RIGHT * 2)
        
        # Function to calculate force and r
        def calculate_force(dot1, dot2, q1, q2, k):
            r = np.linalg.norm(dot1.get_center() - dot2.get_center())
                # This is the same function Blake uses but we can constantly update the function as the charges move
                    # Apply this to multiple charges since the function relies on the "dots" we provide?
            force = k * q1 * q2 / r**2
                # Force equation
            return force, r
                # Returns the new values calculated to be re-animated
        
        # Calculate the initial force with the starting r value
        force, r = calculate_force(dot1, dot2, q1, q2, k)
        force_text = MathTex(r"\vec{F}_{c} = k_{c} \frac{q_1 q_2}{r^2} \ \hat{\mathrm{r}} =", str(round(force, 2)), r"\ \mathrm{N} \ \hat{\mathrm{r}}").to_edge(UP)
        
        # Taken from Blake's initial code: Redraws all of the variables in the video as we move them around
        c1 = always_redraw(lambda: MathTex(r"q_1").next_to(dot1, UP, buff=0.2))
        c2 = always_redraw(lambda: MathTex(r"q_2").next_to(dot2, UP, buff=0.2))
        char1 = VGroup(dot1, c1)
        char2 = VGroup(dot2, c2)
        rline = always_redraw(lambda: Line(start=dot1.get_center(), end=dot2.get_center(), color=GREEN))
        r_text = always_redraw(lambda: Tex("r").move_to(rline.get_center() + UP * 0.2))
        
        # Function to update the on-screen Force equation with the new r values
        def update_force_text(force_text):
            force, r = calculate_force(dot1, dot2, q1, q2, k)
            force_text.become(MathTex(r"\vec{F}_{c} = k_{c} \frac{q_1 q_2}{r^2} \ \hat{\mathrm{r}} =", str(round(force, 2)), r"\ \mathrm{N} \ \hat{\mathrm{r}}").to_edge(UP))
        
        # Applies the above function to the on-screen text
        force_text.add_updater(update_force_text)
        
        # Parameters for the animation to play
        self.add(force_text, char1, char2, rline, r_text)
        self.play(char1.animate.shift(RIGHT * 1), char2.animate.shift(LEFT * 1), run_time=2)
        self.play(char1.animate.shift(LEFT * 1), char2.animate.shift(RIGHT * 1), run_time=2)
        self.play(char1.animate.shift(UP * 1), run_time=2)
        self.wait(1)