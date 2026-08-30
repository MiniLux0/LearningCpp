from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene, export_manim_scenes

class L01ConstMemory(BaseLearningScene):
    def construct(self):
        # 1. Encabezado estándar
        header = self.create_header("Inmutabilidad en Memoria", "Proteccion contra Reasignacion con const")
        self.add(header)
        self.wait(0.4)

        Y_MAIN = 0.2

        # PANEL IZQUIERDO: Ventana de Código IDE
        win_group, code_bg = self.create_code_window(width=5.4, height=3.0, title="main.cpp")
        win_group.move_to(LEFT * 3.4 + UP * Y_MAIN)

        code_lines = VGroup(
            Text("const int vidas{3};", font="Consolas", font_size=15, color=self.COLOR_GOLD_LIGHT),
            Text("vidas = 0;  // Bug", font="Consolas", font_size=15, color="#6e7681")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(code_bg.get_center() + DOWN * 0.1)

        # PANEL DERECHO: Tarjeta de Memoria RAM
        ram_group, ram_bg = self.create_card_panel(width=5.4, height=3.0, title="Memoria RAM (Stack)", subtitle="Direccion: 0x7FFEE4")
        ram_group.move_to(RIGHT * 3.4 + UP * Y_MAIN)

        cell_inner = RoundedRectangle(
            width=3.8, height=1.1, corner_radius=0.12,
            fill_color="#1e1e2e", fill_opacity=0.9,
            stroke_color=self.COLOR_CYAN, stroke_width=1.5
        ).move_to(ram_bg.get_center() + DOWN * 0.45)

        var_tag = Text("vidas (int)", font="Consolas", font_size=13, color=self.COLOR_CYAN).next_to(cell_inner.get_top(), UP, buff=0.08)
        val_text = Text("3", font="Consolas", font_size=32, color="#ffffff", weight=BOLD).move_to(cell_inner.get_center())

        ram_full = VGroup(ram_group, cell_inner, var_tag)
        self.play(FadeIn(win_group), FadeIn(ram_full), run_time=0.5)
        self.wait(0.2)

        # ACTO 1: Inyección e Inmutabilidad Dorada
        self.play(Write(code_lines[0]), run_time=0.6)
        self.play(FadeIn(val_text, shift=DOWN * 0.3), run_time=0.5)

        shield_frame = RoundedRectangle(
            width=4.0, height=1.3, corner_radius=0.16,
            fill_color=self.COLOR_GOLD, fill_opacity=0.15,
            stroke_color=self.COLOR_GOLD, stroke_width=3.5
        ).move_to(cell_inner.get_center())

        lock_badge = VGroup(
            RoundedRectangle(width=2.0, height=0.38, corner_radius=0.08, fill_color="#0d1117", fill_opacity=0.95, stroke_color=self.COLOR_GOLD, stroke_width=1.2),
            Text("READ-ONLY", font="Consolas", font_size=11, color=self.COLOR_GOLD_LIGHT, weight=BOLD)
        ).next_to(shield_frame.get_top(), UP, buff=0.02)

        self.play(
            Create(shield_frame),
            FadeIn(lock_badge, shift=DOWN * 0.1),
            Flash(shield_frame.get_center(), color=self.COLOR_GOLD, flash_radius=1.2, num_lines=12),
            run_time=0.8
        )
        self.wait(0.4)

        # ACTO 2: Mutación y Rebote Neutral
        self.play(Write(code_lines[1]), code_lines[1].animate.set_color(self.COLOR_RED), run_time=0.6)

        bad_proj = VGroup(
            RoundedRectangle(width=1.2, height=0.65, corner_radius=0.1, fill_color=self.COLOR_RED, fill_opacity=0.9, stroke_color="#ffffff", stroke_width=1.5),
            Text("= 0", font="Consolas", font_size=18, color="#ffffff", weight=BOLD)
        ).move_to(LEFT * 0.8 + UP * (Y_MAIN - 0.45))

        self.play(FadeIn(bad_proj, scale=0.8), run_time=0.3)

        impact_target = shield_frame.get_left() + LEFT * 0.1
        self.play(bad_proj.animate.move_to(impact_target), rate_func=rush_into, run_time=0.45)

        shockwave = Circle(radius=0.2, color=self.COLOR_GOLD_LIGHT, stroke_width=5).move_to(impact_target)
        bounce_point = LEFT * 0.2 + DOWN * 0.8

        self.play(
            shockwave.animate.scale(3.5).set_opacity(0),
            bad_proj.animate.move_to(bounce_point).rotate(PI / 4).set_opacity(0.1),
            shield_frame.animate.set_stroke(color="#ffffff", width=5),
            run_time=0.45
        )
        self.remove(shockwave, bad_proj)
        self.play(shield_frame.animate.set_stroke(color=self.COLOR_GOLD, width=3.5), run_time=0.2)

        # ACTO 3: HUD y Badge de Aprendizaje
        err_hud = self.create_hud_footer("ERROR DE COMPILADOR", "assignment of read-only variable 'vidas'", color=self.COLOR_RED)
        insight_badge = self.create_badge("Proteccion en Tiempo de Compilacion", width=5.8).move_to(UP * 2.2 + RIGHT * 3.4)

        self.play(
            FadeIn(err_hud, shift=UP * 0.25),
            FadeIn(insight_badge, shift=DOWN * 0.15),
            run_time=0.7
        )
        self.wait(3.8)

if __name__ == "__main__":
    export_manim_scenes(__file__, "05_ConstantsAndStrings", {"L01ConstMemory": "l01_const_memory.gif"})
