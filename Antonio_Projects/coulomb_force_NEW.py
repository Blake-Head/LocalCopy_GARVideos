from manim import *
import numpy as np


# Coulomb Force Animation
class CoulombForce(Scene):
    def construct(self):
        # Constants
        k = 8.99e9  # Coulomb's constant in N·m²/C²
        q1 = 1e-6   # Charge of the first particle in Coulombs
        q2 = 1e-6   # Charge of the second particle in Coulombs
        
        # Define two points with initial positions
        dot1 = Dot(np.array([-3, 0, 0]), color=RED)
        dot2 = Dot(np.array([3, 0, 0]), color=BLUE)
        
        # Add dots to the scene
        self.add(dot1, dot2)
        
        # Create lines to show force direction (for visual effect)
        line = Line(dot1.get_center(), dot2.get_center(), color=WHITE)
        self.add(line)
        
        # Function to update the Coulomb force text
        def update_force_text(text):
            r = np.linalg.norm(dot1.get_center() - dot2.get_center())
            force = k * q1 * q2 / r**2
            text.become(Text(f"Force: {force:.2e} N").to_edge(UP))
        
        # Create the force text and add it to the scene
        force_text = Text("Force: Calculating...").to_edge(UP)
        self.add(force_text)
        
        # Update function for the animation
        def update_dots(mob, dt):
            # Move dots in opposite directions for the animation
            dot1.shift(0.1 * dt * RIGHT)
            dot2.shift(0.1 * dt * LEFT)
            
            # Update the line position
            line.put_start_and_end_on(dot1.get_center(), dot2.get_center())
            
            # Update the force text
            update_force_text(force_text)
        
        # Add updater to the dots
        dot1.add_updater(update_dots)
        dot2.add_updater(update_dots)
        
        # Run the animation for 5 seconds
        self.wait(5)
        
        # Remove updaters to stop the animation
        dot1.remove_updater(update_dots)
        dot2.remove_updater(update_dots)