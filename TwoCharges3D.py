from manim import *

class TwoChargeElectricField3D(ThreeDScene):
    def construct(self):
        # Set up 3D camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Create two point charges
        charge1 = Sphere(radius=0.2, color=RED).shift(LEFT * 2)
        charge2 = Sphere(radius=0.2, color=BLUE).shift(RIGHT * 2)
        charge1_label = Text("Q1").next_to(charge1, UP)
        charge2_label = Text("Q2").next_to(charge2, UP)

        # Create electric field lines for both charges
        field_lines = VGroup()
        for angle in np.linspace(0, 2 * PI, 8, endpoint=False):
            for z in np.linspace(-1, 1, 5):
                start1 = charge1.get_center()
                end1 = start1 + np.array([3 * np.cos(angle), 3 * np.sin(angle), z])
                line1 = Arrow3D(start1, end1, color=RED_C)
                field_lines.add(line1)
                
                start2 = charge2.get_center()
                end2 = start2 + np.array([3 * np.cos(angle), 3 * np.sin(angle), z])
                line2 = Arrow3D(start2, end2, color=BLUE_C)
                field_lines.add(line2)
        
        # Add the point charges and field lines to the scene
        self.add(charge1, charge2, charge1_label, charge2_label)
        self.play(Create(field_lines))
        
        # Rotate the scene for a better view
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)
        self.stop_ambient_camera_rotation()

        # Hold the final scene
        self.wait(2)

