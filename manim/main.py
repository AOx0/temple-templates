from manim import *


class {{ project }}(Scene):
    def construct(self):
        self: Scene

        text = Text("Welcome to {{ project }}")

        self.play(Write(text))
        self.wait(0.2)
        self.play(FadeOut(text))