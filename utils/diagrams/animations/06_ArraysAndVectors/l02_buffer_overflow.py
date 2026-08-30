from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene, export_manim_scenes

class L02BufferOverflow(BaseLearningScene):
    def construct(self):
        # 1. Encabezado estándar
        header = self.create_header("Buffer Overflow en C-Arrays", "Corrupcion de Variables Vecinas en Stack")
        self.add(header)
        self.wait(0.6)

        Y_MAIN = 0.25

        # PANEL IZQUIERDO: Ventana de Código IDE con MarkupText
        win_group, code_bg = self.create_code_window(width=5.8, height=3.4, title="main.cpp")
        win_group.move_to(LEFT * 3.4 + UP * Y_MAIN)

        l1 = MarkupText('<span foreground="#10b981"><b>int</b></span> <span foreground="#fbbf24">secreta</span>{<span foreground="#fbbf24">100</span>};', font="Consolas", font_size=13)
        l2 = MarkupText('<span foreground="#10b981"><b>int</b></span> <span foreground="#38bdf8">arr</span>[<span foreground="#fbbf24">3</span>]{<span foreground="#fbbf24">10</span>, <span foreground="#fbbf24">20</span>, <span foreground="#fbbf24">30</span>};', font="Consolas", font_size=13)
        l3 = MarkupText('<span foreground="#8b949e">// Indices validos: 0, 1, 2</span>', font="Consolas", font_size=11)
        l4 = MarkupText('<span foreground="#8b949e">// Acceso ilegal fuera de rango:</span>', font="Consolas", font_size=11)
        l5 = MarkupText('<span foreground="#ef4444"><b>arr[3] = 999;</b></span> <span foreground="#8b949e">// Corrupcion!</span>', font="Consolas", font_size=13)

        code_group = VGroup(l1, l2, l3, l4, l5).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(code_bg.get_center() + DOWN * 0.05)

        # PANEL DERECHO: Tarjeta de Memoria Stack
        ram_group, ram_bg = self.create_card_panel(width=5.8, height=3.4, title="Stack Frame (Memoria)", subtitle="Variables en Direcciones Consecutivas")
        ram_group.move_to(RIGHT * 3.4 + UP * Y_MAIN)

        self.play(FadeIn(win_group), FadeIn(ram_group), run_time=0.6)
        self.wait(0.5)

        # ACTO 1: Declarar variables contiguas
        self.play(Write(l1), Write(l2), Write(l3), run_time=0.9)

        c0 = self.create_cell("arr[0]\n10", width=1.1, height=0.7, color=self.COLOR_CYAN, font_size=10)
        c1 = self.create_cell("arr[1]\n20", width=1.1, height=0.7, color=self.COLOR_CYAN, font_size=10)
        c2 = self.create_cell("arr[2]\n30", width=1.1, height=0.7, color=self.COLOR_CYAN, font_size=10)
        c_sec = self.create_cell("secreta\n100", width=1.3, height=0.7, color=self.COLOR_GOLD, font_size=10)

        stack_row = VGroup(c0, c1, c2, c_sec).arrange(RIGHT, buff=0.08).move_to(ram_bg.get_center() + DOWN * 0.1)

        self.play(FadeIn(stack_row, shift=UP * 0.2), run_time=0.7)
        self.wait(2.8)

        # ACTO 2: Escritura fuera de límites (arr[3])
        self.play(Write(l4), Write(l5), run_time=0.8)

        red_laser = Arrow(start=UP * 1.5 + RIGHT * 4.9, end=c_sec.get_top(), buff=0.08, color=self.COLOR_RED, stroke_width=4.5)
        c_corrupt = self.create_cell("secreta\n999", width=1.3, height=0.7, color=self.COLOR_RED, font_size=10).move_to(c_sec.get_center())

        self.play(
            GrowArrow(red_laser),
            Transform(c_sec, c_corrupt),
            Flash(c_sec.get_center(), color=self.COLOR_RED, flash_radius=1.3),
            run_time=0.9
        )
        self.wait(2.8)

        # ACTO 3: HUD Footer de advertencia con tiempo para leer
        hud_group = self.create_hud_footer("UNDEFINED BEHAVIOR", "Los C-Arrays no validan limites: escribir en arr[3] sobreescribe variables contiguas.", color=self.COLOR_RED)
        self.play(FadeIn(hud_group, shift=UP * 0.2), run_time=0.7)
        self.wait(5.0)

if __name__ == "__main__":
    export_manim_scenes(__file__, "06_ArraysAndVectors", {"L02BufferOverflow": "l02_buffer_overflow.gif"})
