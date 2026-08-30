from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene, export_manim_scenes

class L07VectorGrowth(BaseLearningScene):
    def construct(self):
        # 1. Encabezado estándar
        header = self.create_header("Crecimiento Dinamico (push_back)", "Realocacion en Heap y Duplicacion de Capacidad")
        self.add(header)
        self.wait(0.6)

        Y_MAIN = 0.2

        # PANEL IZQUIERDO: Ventana de Código IDE (Aprovechamiento completo del ancho)
        win_group, code_bg = self.create_code_window(width=5.8, height=3.3, title="main.cpp")
        win_group.move_to(LEFT * 3.4 + UP * Y_MAIN)

        code_lines = VGroup(
            Text("std::vector<int> v{10, 20};", font="Consolas", font_size=12, color=self.COLOR_CYAN),
            Text("// size: 2, capacity: 2 (Bloque Lleno)", font="Consolas", font_size=11, color=self.COLOR_MUTED),
            Text("\nv.push_back(30); // Requiere Espacio!", font="Consolas", font_size=12, color=self.COLOR_GOLD_LIGHT, weight=BOLD),
            Text("// 1. Reserva nuevo bloque (cap: 4)", font="Consolas", font_size=11, color=self.COLOR_GREEN_LIGHT),
            Text("// 2. Mueve datos existentes", font="Consolas", font_size=11, color=self.COLOR_CYAN),
            Text("// 3. Inserta 30 y libera bloque viejo", font="Consolas", font_size=11, color=self.COLOR_PURPLE_LIGHT)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.09).move_to(code_bg.get_center() + DOWN * 0.05)

        # PANEL DERECHO: Tarjeta de Memoria Heap (Amplio y sin desbordamientos)
        ram_group, ram_bg = self.create_card_panel(width=5.8, height=3.3, title="Memoria Dinámica (Heap)", subtitle="Estrategia de Capacidad Duplicada")
        ram_group.move_to(RIGHT * 3.4 + UP * Y_MAIN)

        self.play(FadeIn(win_group), FadeIn(ram_group), run_time=0.6)
        self.wait(0.5)

        # ACTO 1: Bloque Antiguo Lleno (Capacidad 2)
        self.play(Write(code_lines[0]), Write(code_lines[1]), run_time=0.7)

        old_tag = Text("Bloque Heap A (cap: 2)", font="Consolas", font_size=11, color=self.COLOR_MUTED).move_to(ram_bg.get_center() + UP * 0.95)
        old_0 = self.create_cell("10", width=1.2, height=0.55, color=self.COLOR_CYAN, font_size=11)
        old_1 = self.create_cell("20", width=1.2, height=0.55, color=self.COLOR_CYAN, font_size=11)
        old_block = VGroup(old_0, old_1).arrange(RIGHT, buff=0.08).next_to(old_tag, DOWN, buff=0.1)

        self.play(FadeIn(old_tag), FadeIn(old_block), run_time=0.6)
        self.wait(1.0)

        # ACTO 2: push_back y Realocación a Bloque B (Capacidad 4)
        self.play(
            Write(code_lines[2]), Write(code_lines[3]), Write(code_lines[4]), Write(code_lines[5]),
            run_time=0.9
        )

        new_tag = Text("Bloque Heap B (cap: 4 - Duplicada)", font="Consolas", font_size=11, color=self.COLOR_GREEN_LIGHT, weight=BOLD).move_to(ram_bg.get_center() + DOWN * 0.25)
        new_0 = self.create_cell("10", width=1.0, height=0.55, color=self.COLOR_GREEN, font_size=10)
        new_1 = self.create_cell("20", width=1.0, height=0.55, color=self.COLOR_GREEN, font_size=10)
        new_2 = self.create_cell("30", width=1.0, height=0.55, color=self.COLOR_GOLD, font_size=10)
        new_3 = self.create_cell("Libre", width=1.0, height=0.55, color=self.COLOR_MUTED, font_size=10)
        new_block = VGroup(new_0, new_1, new_2, new_3).arrange(RIGHT, buff=0.06).next_to(new_tag, DOWN, buff=0.1)

        self.play(
            FadeIn(new_tag, shift=UP * 0.15),
            FadeIn(new_block, shift=UP * 0.15),
            Flash(new_2.get_center(), color=self.COLOR_GOLD, flash_radius=1.1),
            run_time=0.9
        )
        self.wait(1.2)

        # ACTO 3: Liberación del bloque antiguo
        old_x = Text("[LIBERADO: delete[]]", font="Consolas", font_size=11, color=self.COLOR_RED, weight=BOLD).move_to(old_block.get_center())
        self.play(
            old_block.animate.set_opacity(0.2),
            FadeIn(old_x),
            run_time=0.7
        )
        self.wait(1.5)

        # ACTO 4: HUD Footer
        hud_group = self.create_hud_footer("CRECIMIENTO AMORTIZADO", "std::vector duplica su capacidad (2 -> 4 -> 8) para garantizar un costo amortizado O(1).", color=self.COLOR_CYAN)
        self.play(FadeIn(hud_group, shift=UP * 0.2), run_time=0.7)
        self.wait(5.5)

if __name__ == "__main__":
    export_manim_scenes(__file__, "06_ArraysAndVectors", {"L07VectorGrowth": "l07_vector_growth.gif"})
