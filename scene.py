from manim import *

class Intro(Scene):
    def animate_pitch_sequence(
            self,
            pitches,
            p_sequence,
            start_point,
            plate_center,
            end_loc=None,
            scale=0.45,
    ):
        objects= VGroup()
        strike_zone=Rectangle(width=2, height=2.586, color=RED).shift(DOWN*.5)
        self.play(Create(strike_zone))
        objects.add(strike_zone)
        sequence = Text(p_sequence, font_size=20)
        objects.add(sequence)


        for pitch in pitches:
            ball = Dot(
                point=start_point,
                radius=.5,
                color=WHITE)
            label=Text(pitch['label'], font_size=20)
            label.add_updater(lambda m, b=ball: m.next_to(b, RIGHT))

            objects.add(ball, label)

            self.play(
                ball.animate
                .move_to(pitch["end"])
                .scale(0.2),
                run_time=1.2,
                rate_func=rate_functions.ease_in_back
            )
            if pitch['label'] == "Strike":
                self.play(
                    ball.animate.set_color(GREEN),
                    Write(label.next_to(ball, UP, buff=0.2))
                    )
            else:
                self.play(
                    ball.animate.set_color(RED),
                    Write(label.next_to(ball, UP, buff=0.2))
                )
        self.play(
            Write(sequence.next_to(strike_zone, UP, buff=0.2))
        )
        self.wait()
        if end_loc is not None:
            self.play(
                objects.animate
                    .scale(scale)
                    .move_to(end_loc),
                run_time=1,
                rate_func=rate_functions.linear
            )

        return objects
            

    def construct(self):
        title = Text("Pitch Sequencing Above Baseline").to_edge(UP)
        subtitle = Text("Project Overview", font_size=25).next_to(title, DOWN, buff=.2)
        strike1 = Text("Strike", font_size=20)
        strike2 = Text("Strike", font_size=20)
  
        ball = Text("Ball", font_size=20)

        strike_zone = Rectangle(width=2, height=2.586, color=RED).shift(DOWN*.5)

        release_point = UP 
        plate_center = strike_zone.get_center()

        pitch1 = Dot(
            point = release_point,
            radius=.5,
            color=WHITE
        )
        pitch2 = Dot(
            point=release_point + RIGHT * 0.6,
            radius=0.5,
            color=WHITE
        )
        pitch3 = Dot(
            point=release_point + RIGHT * 0.6,
            radius=0.5,
            color=WHITE
        )
        sequence2 = [
            {'label': "Strike", 'end':plate_center+DOWN*0.9 +RIGHT*0.1},
            {'label': "Strike", 'end':plate_center + UP *0.9 + LEFT*0.8},
            {'label': "Ball", 'end':plate_center + RIGHT*1.2},
        ]
        sequence3 = [
            {'label': "Strike", 'end':plate_center+UP*1.2 +RIGHT*0.1},
            {'label': "Strike", 'end':plate_center + UP *0.9 + LEFT*0.8},
            {'label': "Ball", 'end':plate_center + RIGHT*1.2},
        ]

        sequence4 = [
            {'label': "Strike", 'end':plate_center+UP*0.7 +RIGHT*0.4},
            {'label': "Strike", 'end':plate_center + UP *0.9 + RIGHT*0.8},
            {'label': "Ball", 'end':plate_center + DOWN*2},
        ]

        self.play(Write(title))
        self.play(Write(subtitle))
        # self.play(Create(strike_zone))
        # self.play(FadeIn(pitch1))
        # self.play(
        #     pitch1.animate
        #     .move_to(plate_center-0.9)
        #     .scale(0.2),
        #     run_time=1.2,
        #     rate_func=rate_functions.ease_in_back
        # )
        # self.play(
        #     pitch1.animate.set_color(GREEN),
        #     Write(strike1.next_to(pitch1, RIGHT, buff=0.2))
        #     )
        # self.play(FadeIn(pitch2))
        # self.play(
        #     pitch2.animate
        #     .move_to(plate_center + UP*0.8+LEFT*0.8)
        #     .scale(0.2),
        #     run_time=1.2,
        #     rate_func=rate_functions.ease_in_back
        # )
        # self.play(
        #     pitch2.animate.set_color(GREEN),
        #     Write(strike2.next_to(pitch2, RIGHT, buff=0.2))
        #     )
        # self.play(FadeIn(pitch3))
        # self.play(
        #     pitch3.animate
        #     .move_to(strike_zone.get_edge_center(RIGHT)+RIGHT*.2)
        #     .scale(0.2),
        #     run_time=1.2,
        #     rate_func=rate_functions.ease_in_back
        # )
        # self.play(
        #     pitch3.animate.set_color(RED),
        #     Write(ball.next_to(pitch3, RIGHT, buff=0.2))
        #     )
        # sequence=Text("SL, FF, CH", font_size=20)
        # self.play(
        #     Write(sequence.next_to(strike_zone, UP, buff=0.2))
        # )
        # self.wait()

        # sequence1 = VGroup(
        #     pitch1, pitch2, pitch3,
        #     strike1, strike2, ball, strike_zone,
        #     sequence
        # )
        # self.play(
        #     sequence1.animate
        #     .scale(.45)
        #     .to_corner(UL),
        #     run_time=2,
        #     rate_func=rate_functions.exponential_decay
        #     )

        seq2 = self.animate_pitch_sequence(
            sequence2,
            start_point=release_point,
            plate_center=strike_zone.get_center(),
            end_loc=(UL),
            p_sequence="FF, FF, FF"
        )

        seq3 = self.animate_pitch_sequence(
            sequence3,
            start_point=release_point,
            plate_center=strike_zone.get_center(),
            end_loc=(UL+DOWN*1),
            p_sequence="SL, CH, FS"
        )

        seq4 = self.animate_pitch_sequence(
            sequence4,
            start_point=release_point,
            plate_center=strike_zone.get_center(),
            end_loc=(UL+DOWN*1.5),
            p_sequence="SL, SL, FS"
        )
