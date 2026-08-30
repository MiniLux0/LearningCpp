from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene, export_manim_scenes

class L03StringConcat(BaseLearningScene):
    def construct(self):
        # 1. Encabezado estándar
        header = self.create_header("Cadenas Dinamicas (std::string)", "Concatenacion y Expansion de Memoria")
        self.add(header)
        self.wait(0.4)

        Y_MAIN = 0.2

        # PANEL IZQUIERDO: Ventana de Código IDE
        win_group, code_bg = self.create_code_window(width=5.4, height=3.0, title="main.cpp")
        win_group.move_to(LEFT * 3.4 + UP * Y_MAIN)

        code_lines = VGroup(
            Text("std::string texto{\"Hola\"};", font="Consolas", font_size=14, color=self.COLOR_CYAN),
            Text("texto = texto + \" Mundo\";", font="Consolas", font_size=13, color=self.COLOR_GREEN),
            Text("// \"A\" + \"B\" -> Error (C-strings)", font="Consolas", font_size=12, color=self.COLOR_RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(code_bg.get_center() + DOWN * 0.1)

        # PANEL DERECHO: Tarjeta de Buffer Dinámico en RAM
        ram_group, ram_bg = self.create_card_panel(width=5.4, height=3.0, title="Buffer Dinamico en RAM", subtitle="Capacidad auto-escalable")
        ram_group.move_to(RIGHT * 3.4 + UP * Y_MAIN)

        def make_cells(letters, base_color):
            group = VGroup()
            for ch in letters:
                box = RoundedRectangle(width=0.40, height=0.55, corner_radius=0.06, fill_color="#1e1e2e", fill_opacity=0.9, stroke_color=base_color, stroke_width=1.5)
                txt = Text(ch, font="Consolas", font_size=15, color="#ffffff", weight=BOLD).move_to(box.get_center())
                group.add(VGroup(box, txt))
            group.arrange(RIGHT, buff=0.05)
            return group

        cells_init = make_cells(["H", "o", "l", "a"], self.COLOR_CYAN).move_to(ram_bg.get_center() + DOWN * 0.45 + LEFT * 1.0)
        size_lbl = Text("Size: 4 bytes", font="Consolas", font_size=13, color=self.COLOR_CYAN, weight=BOLD).next_to(cells_init, UP, buff=0.15)

        self.play(FadeIn(win_group), FadeIn(ram_group), run_time=0.5)
        self.wait(0.2)

        # ACTO 1: Creación del Objeto Dinámico Inicial
        self.play(Write(code_lines[0]), run_time=0.6)
        self.play(FadeIn(cells_init, shift=DOWN * 0.2), Write(size_lbl), run_time=0.6)
        self.wait(0.4)

        # ACTO 2: Concatenación con + y Expansión Elástica
        self.play(Write(code_lines[1]), run_time=0.6)

        cells_all = make_cells(["H", "o", "l", "a", " ", "M", "u", "n", "d", "o"], self.COLOR_GREEN).move_to(ram_bg.get_center() + DOWN * 0.45)
        size_lbl_expanded = Text("Size: 10 bytes (Auto-expand)", font="Consolas", font_size=13, color=self.COLOR_GREEN, weight=BOLD).next_to(cells_all, UP, buff=0.15)

        self.play(
            ReplacementTransform(cells_init, cells_all),
            ReplacementTransform(size_lbl, size_lbl_expanded),
            Flash(cells_all.get_center(), color=self.COLOR_GREEN, flash_radius=1.3, num_lines=14),
            run_time=0.8
        )
        self.wait(0.4)

        # ACTO 3: Advertencia de Literales Estáticos ("A" + "B")
        self.play(Write(code_lines[2]), run_time=0.5)

        insight_badge = self.create_badge("Buffer Dinamico Auto-Administrado", width=5.8).move_to(UP * 2.2 + RIGHT * 3.4)
        hud_group = self.create_hud_footer("BUFFER STL", "std::string reserva RAM contigua automaticamente al concatenar.", color=self.COLOR_CYAN)

        self.play(
            FadeIn(insight_badge, shift=DOWN * 0.15),
            FadeIn(hud_group, shift=UP * 0.25),
            run_time=0.7
        )
        self.wait(3.8)

if __name__ == "__main__":
    export_manim_scenes(__file__, "05_ConstantsAndStrings", {"L03StringConcat": "l03_string_concat.gif"})
