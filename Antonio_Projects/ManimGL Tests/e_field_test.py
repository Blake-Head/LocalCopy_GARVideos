from manim import *
from manim_physics import *
import numpy as np

# Making a charged particle influence an electric field
class PointChargeInElectricField(Scene):
    def construct(self):
        # Create the electric field
        field = ElectricField()
        
        # Create the point charge
        pointCharge = Charge(magnitude=1, position=np.array([-3, 0, 0]))

        # Add the electric field and the point charge to the scene
        self.add(field, pointCharge)

        # Add a set path for the point charge to move along
        path = Line(start=pointCharge.get_center(), end=RIGHT * 3)

        # Animation time!
        self.play(MoveAlongPath(pointCharge, path, rate_func=linear, run_time=5))

        self.wait(1)

class PointChargeInVectorField(Scene):
    def construct(self):
        # Create electric field
        vector_field = ArrowVectorField(
            lambda pos: np.array([pos[0], pos[1], 0]),  # simple linear field for visualization
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1]
        )
        
        # Create a point charge
        point_charge = Dot(color=RED).move_to(np.array([-3, 0, 0]))
        charge_label = Tex("+Q").next_to(point_charge, UP, buff=0.1)

        # Add the vector field and point charge to the scene
        self.add(vector_field, point_charge, charge_label)
        
        # Define the movement path for the point charge
        path = ParametricFunction(
            lambda t: np.array([-3 + 2*t, np.sin(t*PI), 0]),  # Path from left to right with a sine wave motion
            t_range=np.array([0, 3, 0.01]),
            color=RED
        )

        # Create the animation of the point charge moving along the path
        self.play(MoveAlongPath(point_charge, path), run_time=5, rate_func=linear)

        self.wait(2)
