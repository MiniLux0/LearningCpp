from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene, export_manim_scenes

class L05CinBuffer(BaseLearningScene):
    def construct(self):
        # 1. Encabezado estándar
        header = self.create_header("Sanitizacion de Entrada (std::cin)", "Protocolo fail() -> clear() -> ignore()")
        self.add(header)
        self.wait(0.4)

        Y_MAIN = 0.2

        # PANEL IZQUIERDO: Ventana de Código IDE
        win_group, code_bg = self.create_code_window(width=5.4, height=3.0, title="main.cpp")
        win_group.move_to(LEFT * 3.4 + UP * Y_MAIN)

        code_lines = VGroup(
            Text("std::cin >> edad; // 'abc'", font="Consolas", font_size=13, color=self.COLOR_RED),
            Text("if (std::cin.fail()) {", font="Consolas", font_size=13, color=self.COLOR_GOLD_LIGHT),
            Text("    std::cin.clear();", font="Consolas", font_size=13, color=self.COLOR_CYAN),
            Text("    std::cin.ignore(10000, '\\n');", font="Consolas", font_size=12, color=self.COLOR_GREEN),
            Text("}", font="Consolas", font_size=13, color=self.COLOR_GOLD_LIGHT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.10).move_to(code_bg.get_center() + DOWN * 0.1)

        # PANEL DERECHO: Tarjeta de Tubería del Buffer
        ram_group, ram_bg = self.create_card_panel(width=5.4, height=3.0, title="Buffer de Entrada (std::cin)", subtitle="Tuberia de Flujo con Estado")
        ram_group.move_to(RIGHT * 3.4 + UP * Y_MAIN)

        pipe_outer = RoundedRectangle(
            width=4.4, height=0.85, corner_radius=0.1,
            fill_color="#1e1e2e", fill_opacity=0.9,
            stroke_color="#45475a", stroke_width=1.8
        ).move_to(ram_bg.get_center() + UP * 0.15)

        def make_char_node(ch, color):
            box = RoundedRectangle(width=0.5, height=0.55, corner_radius=0.08, fill_color="#181825", fill_opacity=0.95, stroke_color=color, stroke_width=1.5)
            txt = Text(ch, font="Consolas", font_size=15, color=color, weight=BOLD).move_to(box.get_center())
            return VGroup(box, txt)

        c1 = make_char_node("a", self.COLOR_RED)
        c2 = make_char_node("b", self.COLOR_RED)
        c3 = make_char_node("c", self.COLOR_RED)
        c4 = make_char_node("\\n", "#8b949e")
        stuck_group = VGroup(c1, c2, c3, c4).arrange(RIGHT, buff=0.12).move_to(pipe_outer.get_center())

        alarm_badge = VGroup(
            RoundedRectangle(width=2.4, height=0.4, corner_radius=0.08, fill_color="#1a0a0d", fill_opacity=0.95, stroke_color=self.COLOR_RED, stroke_width=1.5),
            Text("ESTADO: fail()", font="Consolas", font_size=12, color=self.COLOR_RED, weight=BOLD)
        ).move_to(ram_bg.get_center() + DOWN * 0.75)

        ram_full = VGroup(ram_group, pipe_outer)
        self.play(FadeIn(win_group), FadeIn(ram_full), run_time=0.5)
        self.wait(0.2)

        # ACTO 1: Fallo de Extracción y Bloqueo
        self.play(Write(code_lines[0]), Write(code_lines[1]), run_time=0.7)
        self.play(
            FadeIn(stuck_group, shift=RIGHT * 0.3),
            FadeIn(alarm_badge, shift=UP * 0.2),
            Flash(alarm_badge.get_center(), color=self.COLOR_RED, flash_radius=1.2, num_lines=12),
            run_time=0.8
        )
        self.wait(0.4)

        # ACTO 2: Reactivación del Canal (clear)
        self.play(Write(code_lines[2]), run_time=0.5)

        ready_badge = VGroup(
            RoundedRectangle(width=2.4, height=0.4, corner_radius=0.08, fill_color="#064e3b", fill_opacity=0.95, stroke_color=self.COLOR_GREEN, stroke_width=1.5),
            Text("ESTADO: good()", font="Consolas", font_size=12, color=self.COLOR_GREEN, weight=BOLD)
        ).move_to(alarm_badge.get_center())

        self.play(ReplacementTransform(alarm_badge, ready_badge), run_time=0.6)
        self.wait(0.3)

        # ACTO 3: Purga del Buffer (ignore)
        self.play(Write(code_lines[3]), Write(code_lines[4]), run_time=0.5)

        clean_lbl = Text("[Buffer Limpio]", font="Consolas", font_size=14, color=self.COLOR_GREEN, weight=BOLD).move_to(pipe_outer.get_center())

        self.play(
            stuck_group.animate.shift(RIGHT * 3.5).set_opacity(0),
            FadeIn(clean_lbl),
            pipe_outer.animate.set_stroke(color=self.COLOR_GREEN, width=2),
            run_time=0.7
        )
        self.remove(stuck_group)
        self.wait(0.4)

        # ACTO 4: Insignia de Rendimiento y HUD Inferior
        insight_badge = self.create_badge("Protocolo Defensivo Anti-Bloqueo", width=5.8).move_to(UP * 2.2 + RIGHT * 3.4)
        hud_group = self.create_hud_footer("FLUJO DEFENSIVO", "clear() reactiva el canal e ignore() purga los caracteres atascados.", color=self.COLOR_CYAN)

        self.play(
            FadeIn(insight_badge, shift=DOWN * 0.15),
            FadeIn(hud_group, shift=UP * 0.25),
            run_time=0.7
        )
        self.wait(3.8)

if __name__ == "__main__":
    export_manim_scenes(__file__, "05_ConstantsAndStrings", {"L05CinBuffer": "l05_cin_buffer.gif"})
