#This code shows an example Electric Field of a Point Charge
from manim import *

class ElectricField3D(ThreeDScene):
    def construct(self):
        # Set up 3D camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Create a point charge
        charge = Sphere(radius=0.2, color=RED).shift(LEFT * 2)
        charge_label = Text("Q").next_to(charge, RIGHT)

        # Create electric field lines
        field_lines = VGroup()
        for angle in np.linspace(0, 2 * PI, 8, endpoint=False):
            for z in np.linspace(-1, 1, 5):
                start = charge.get_center()
                end = start + np.array([3 * np.cos(angle), 3 * np.sin(angle), z])
                line = Arrow3D(start, end, color=YELLOW)
                field_lines.add(line)
        
        # Add the point charge and field lines to the scene
        self.add(charge, charge_label)
        self.play(Create(field_lines))
        
        # Rotate the scene for a better view
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)
        self.stop_ambient_camera_rotation()

        # Hold the final scene
        self.wait(2)

#Post notes about the 1st Run:
    #Move the animation slightly to the left to center it?
        #Add text to the left instead?
    #Remove the cached files to run faster:
        #Current runtime as of 10/15/2024: ~1 hour (Initial code running)

