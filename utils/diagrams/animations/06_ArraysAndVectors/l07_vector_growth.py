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

        Y_MAIN = 0.25

        # PANEL IZQUIERDO: Ventana de Código IDE con MarkupText Hiper-Realista
        win_group, code_bg = self.create_code_window(width=5.8, height=3.4, title="main.cpp")
        win_group.move_to(LEFT * 3.4 + UP * Y_MAIN)

        l1 = MarkupText('<span foreground="#38bdf8">std::vector</span>&lt;<span foreground="#10b981"><b>int</b></span>&gt; <span foreground="#fbbf24">v</span>{<span foreground="#fbbf24">10</span>, <span foreground="#fbbf24">20</span>};', font="Consolas", font_size=12)
        l2 = MarkupText('<span foreground="#8b949e">// size: 2, capacity: 2 (Lleno)</span>', font="Consolas", font_size=11)
        l3 = MarkupText('<span foreground="#fbbf24">v</span>.<span foreground="#38bdf8"><b>push_back</b></span>(<span foreground="#fbbf24">30</span>); <span foreground="#8b949e">// Realocacion</span>', font="Consolas", font_size=12)
        l4 = MarkupText('<span foreground="#8b949e">// 1. Reserva bloque doble (cap: 4)</span>', font="Consolas", font_size=11)
        l5 = MarkupText('<span foreground="#8b949e">// 2. Mueve datos existentes</span>', font="Consolas", font_size=11)
        l6 = MarkupText('<span foreground="#8b949e">// 3. Inserta 30 y libera bloque A</span>', font="Consolas", font_size=11)

        code_group = VGroup(l1, l2, l3, l4, l5, l6).arrange(DOWN, aligned_edge=LEFT, buff=0.10).move_to(code_bg.get_center() + DOWN * 0.05)

        # PANEL DERECHO: Tarjeta de Memoria Heap (Amplio y sin desbordamientos)
        ram_group, ram_bg = self.create_card_panel(width=5.8, height=3.4, title="Memoria Dinámica (Heap)", subtitle="Estrategia de Capacidad Duplicada")
        ram_group.move_to(RIGHT * 3.4 + UP * Y_MAIN)

        self.play(FadeIn(win_group), FadeIn(ram_group), run_time=0.6)
        self.wait(0.5)

        # ACTO 1: Bloque Antiguo Lleno (Capacidad 2)
        self.play(Write(l1), Write(l2), run_time=0.7)

        old_tag = Text("Bloque Heap A (cap: 2)", font="Consolas", font_size=11, color=self.COLOR_MUTED).move_to(ram_bg.get_center() + UP * 0.95)
        old_0 = self.create_cell("10", width=1.2, height=0.55, color=self.COLOR_CYAN, font_size=11)
        old_1 = self.create_cell("20", width=1.2, height=0.55, color=self.COLOR_CYAN, font_size=11)
        old_block = VGroup(old_0, old_1).arrange(RIGHT, buff=0.08).next_to(old_tag, DOWN, buff=0.1)

        self.play(FadeIn(old_tag), FadeIn(old_block), run_time=0.6)
        self.wait(2.5)

        # ACTO 2: push_back y Realocación a Bloque B (Capacidad 4)
        self.play(
            Write(l3), Write(l4), Write(l5), Write(l6),
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
        self.wait(2.8)

        # ACTO 3: Liberación del bloque antiguo
        old_x = Text("[LIBERADO: delete[]]", font="Consolas", font_size=11, color=self.COLOR_RED, weight=BOLD).move_to(old_block.get_center())
        self.play(
            old_block.animate.set_opacity(0.2),
            FadeIn(old_x),
            run_time=0.7
        )
        self.wait(2.8)

        # ACTO 4: HUD Footer
        hud_group = self.create_hud_footer("CRECIMIENTO AMORTIZADO", "std::vector duplica su capacidad (2 -> 4 -> 8) para garantizar un costo amortizado O(1).", color=self.COLOR_CYAN)
        self.play(FadeIn(hud_group, shift=UP * 0.2), run_time=0.7)
        self.wait(5.0)

if __name__ == "__main__":
    export_manim_scenes(__file__, "06_ArraysAndVectors", {"L07VectorGrowth": "l07_vector_growth.gif"})
