from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene, export_manim_scenes

class L06RangeForPipeline(BaseLearningScene):
    def construct(self):
        # 1. Encabezado estándar
        header = self.create_header("Range-based for Loop", "Iteracion Idiomatica y Segura")
        self.add(header)
        self.wait(0.6)

        Y_MAIN = 0.2

        # PANEL IZQUIERDO: Ventana de Código IDE (Espacioso y estructurado)
        win_group, code_bg = self.create_code_window(width=5.8, height=3.3, title="main.cpp")
        win_group.move_to(LEFT * 3.4 + UP * Y_MAIN)

        code_lines = VGroup(
            Text("std::vector<int> datos{10, 20, 30};", font="Consolas", font_size=12, color=self.COLOR_CYAN),
            Text("\n// Bucle Seguro C++17 (Sin Indices Manuales)", font="Consolas", font_size=11, color=self.COLOR_MUTED),
            Text("for (int n : datos) {", font="Consolas", font_size=13, color=self.COLOR_GOLD_LIGHT, weight=BOLD),
            Text("    std::cout << n << '\\n';", font="Consolas", font_size=13, color=self.COLOR_GREEN_LIGHT),
            Text("}", font="Consolas", font_size=13, color=self.COLOR_GOLD_LIGHT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.10).move_to(code_bg.get_center() + DOWN * 0.05)

        # PANEL DERECHO: Tarjeta de Memoria RAM
        ram_group, ram_bg = self.create_card_panel(width=5.8, height=3.3, title="Procesamiento en Heap", subtitle="Paso Secuencial Automático")
        ram_group.move_to(RIGHT * 3.4 + UP * Y_MAIN)

        self.play(FadeIn(win_group), FadeIn(ram_group), run_time=0.6)
        self.wait(0.5)

        # ACTO 1: Dibujar Vector
        self.play(Write(code_lines[0]), run_time=0.6)

        c0 = self.create_cell("[0]\n10", width=1.2, height=0.7, color=self.COLOR_CYAN, font_size=11)
        c1 = self.create_cell("[1]\n20", width=1.2, height=0.7, color=self.COLOR_CYAN, font_size=11)
        c2 = self.create_cell("[2]\n30", width=1.2, height=0.7, color=self.COLOR_CYAN, font_size=11)
        vec_row = VGroup(c0, c1, c2).arrange(RIGHT, buff=0.1).move_to(ram_bg.get_center() + DOWN * 0.25)

        self.play(FadeIn(vec_row), run_time=0.6)
        self.wait(0.6)

        # ACTO 2: Bucle for y puntero móvil
        self.play(
            Write(code_lines[1]), Write(code_lines[2]), Write(code_lines[3]), Write(code_lines[4]),
            run_time=0.8
        )

        cursor = Arrow(start=UP * 0.8, end=UP * 0.15, buff=0.05, color=self.COLOR_GOLD, stroke_width=4.5).next_to(c0, UP, buff=0.15)
        val_badge = self.create_badge("Elemento n = 10", fill_color="#3b2d11", stroke_color=self.COLOR_GOLD, text_color=self.COLOR_GOLD_LIGHT, width=2.6, height=0.4).next_to(cursor, UP, buff=0.1)

        self.play(GrowArrow(cursor), FadeIn(val_badge), run_time=0.6)
        self.wait(1.0)

        # Mover a elemento 1
        val_badge2 = self.create_badge("Elemento n = 20", fill_color="#3b2d11", stroke_color=self.COLOR_GOLD, text_color=self.COLOR_GOLD_LIGHT, width=2.6, height=0.4).next_to(c1, UP, buff=0.75)
        self.play(
            cursor.animate.next_to(c1, UP, buff=0.15),
            Transform(val_badge, val_badge2),
            run_time=0.8
        )
        self.wait(1.0)

        # Mover a elemento 2
        val_badge3 = self.create_badge("Elemento n = 30", fill_color="#3b2d11", stroke_color=self.COLOR_GOLD, text_color=self.COLOR_GOLD_LIGHT, width=2.6, height=0.4).next_to(c2, UP, buff=0.75)
        self.play(
            cursor.animate.next_to(c2, UP, buff=0.15),
            Transform(val_badge, val_badge3),
            run_time=0.8
        )
        self.wait(1.2)

        # ACTO 3: HUD Footer
        hud_group = self.create_hud_footer("CERO OFF-BY-ONE", "Range-based for recorre la coleccion de inicio a fin sin manipular indices manuales.", color=self.COLOR_CYAN)
        self.play(FadeIn(hud_group, shift=UP * 0.2), run_time=0.7)
        self.wait(5.5)

if __name__ == "__main__":
    export_manim_scenes(__file__, "06_ArraysAndVectors", {"L06RangeForPipeline": "l06_range_for_pipeline.gif"})
