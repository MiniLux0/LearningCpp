from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene, export_manim_scenes

class L03VectorArchitecture(BaseLearningScene):
    def construct(self):
        # 1. Encabezado estándar
        header = self.create_header("Arquitectura de std::vector", "Controlador en Stack y Memoria en Heap")
        self.add(header)
        self.wait(0.6)

        Y_MAIN = 0.2

        # PANEL IZQUIERDO: Ventana de Código IDE
        win_group, code_bg = self.create_code_window(width=5.8, height=3.3, title="main.cpp")
        win_group.move_to(LEFT * 3.4 + UP * Y_MAIN)

        code_lines = VGroup(
            Text("#include <vector>", font="Consolas", font_size=12, color=self.COLOR_MUTED),
            Text("std::vector<int> v{10, 20, 30};", font="Consolas", font_size=13, color=self.COLOR_CYAN, weight=BOLD),
            Text("\n// Stack (Objeto Liviano):", font="Consolas", font_size=11, color=self.COLOR_MUTED),
            Text("// - Puntero a Heap (data*)", font="Consolas", font_size=11, color=self.COLOR_GOLD),
            Text("// - Tamano actual (size: 3)", font="Consolas", font_size=11, color=self.COLOR_GREEN_LIGHT),
            Text("// - Capacidad total (capacity: 3)", font="Consolas", font_size=11, color=self.COLOR_PURPLE_LIGHT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.10).move_to(code_bg.get_center() + DOWN * 0.05)

        # PANEL DERECHO: Tarjeta de Memoria RAM
        ram_group, ram_bg = self.create_card_panel(width=5.8, height=3.3, title="Modelo de Memoria", subtitle="Stack Frame vs Heap Allocation")
        ram_group.move_to(RIGHT * 3.4 + UP * Y_MAIN)

        self.play(FadeIn(win_group), FadeIn(ram_group), run_time=0.6)
        self.wait(0.5)

        # ACTO 1: Código escrito
        self.play(Write(code_lines[0]), Write(code_lines[1]), run_time=0.8)

        # ACTO 2: Stack Controller
        stack_box = RoundedRectangle(
            width=5.0, height=0.65, corner_radius=0.08,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=self.COLOR_CYAN, stroke_width=1.8
        ).move_to(ram_bg.get_center() + UP * 0.7)

        stack_txt = Text("STACK: [ ptr: 0x5000 | size: 3 | cap: 3 ]", font="Consolas", font_size=11, color=self.COLOR_CYAN, weight=BOLD).move_to(stack_box.get_center())

        self.play(
            FadeIn(stack_box), FadeIn(stack_txt),
            Write(code_lines[2]), Write(code_lines[3]), Write(code_lines[4]), Write(code_lines[5]),
            run_time=0.9
        )
        self.wait(0.8)

        # ACTO 3: Heap Buffer
        h0 = self.create_cell("10", width=1.2, height=0.65, color=self.COLOR_GREEN, font_size=12)
        h1 = self.create_cell("20", width=1.2, height=0.65, color=self.COLOR_GREEN, font_size=12)
        h2 = self.create_cell("30", width=1.2, height=0.65, color=self.COLOR_GREEN, font_size=12)
        heap_row = VGroup(h0, h1, h2).arrange(RIGHT, buff=0.08).move_to(ram_bg.get_center() + DOWN * 0.65)
        heap_tag = Text("HEAP (0x5000 - Memoria Contigua)", font="Consolas", font_size=10, color=self.COLOR_MUTED).next_to(heap_row, DOWN, buff=0.12)

        ptr_arrow = Arrow(start=stack_box.get_bottom(), end=heap_row.get_top(), buff=0.1, color=self.COLOR_GOLD, stroke_width=3.5)

        self.play(
            GrowArrow(ptr_arrow),
            FadeIn(heap_row),
            FadeIn(heap_tag),
            Flash(heap_row.get_center(), color=self.COLOR_GREEN, flash_radius=1.3),
            run_time=0.9
        )
        self.wait(1.5)

        # ACTO 4: HUD Footer
        hud_group = self.create_hud_footer("RAII AUTOMÁTICO", "Al terminar el ambito, el Stack destruye el vector y libera la memoria en el Heap.", color=self.COLOR_CYAN)
        self.play(FadeIn(hud_group, shift=UP * 0.2), run_time=0.7)
        self.wait(5.5)

if __name__ == "__main__":
    export_manim_scenes(__file__, "06_ArraysAndVectors", {"L03VectorArchitecture": "l03_vector_architecture.gif"})
