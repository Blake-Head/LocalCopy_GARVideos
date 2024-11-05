from manim import *
import manim_physics as mp
import numpy as np

# Making a charged particle influence an electric field
class PointChargeInElectricField(Scene):
    def construct(self):
        # Create the electric field
        #field = mp.ElectricField()
        
        # Create the point charge
        pointCharge = mp.Charge(magnitude=3, point=np.array([-3, 0, 0]))
        field = mp.ElectricField(pointCharge)

        # Add the electric field and the point charge to the scene
        self.add(field, pointCharge)

        # Add a set path for the point charge to move along
        path = Line(start=pointCharge.get_center(), end=RIGHT * 3)

        # Animation time!
        self.play(MoveAlongPath(pointCharge, path, rate_func=linear, run_time=5))

        self.wait(1)
