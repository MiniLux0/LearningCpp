from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene, export_manim_scenes

class L01MemoriaContigua(BaseLearningScene):
    def construct(self):
        # 1. Encabezado estándar
        header = self.create_header("Colecciones en Memoria", "Variables Dispersas vs Secuencia Contigua")
        self.add(header)
        self.wait(0.6)

        Y_MAIN = 0.25

        # PANEL IZQUIERDO: Ventana de Código IDE con MarkupText Hiper-Realista
        win_group, code_bg = self.create_code_window(width=5.8, height=3.4, title="main.cpp")
        win_group.move_to(LEFT * 3.4 + UP * Y_MAIN)

        l1 = MarkupText('<span foreground="#8b949e">// 1. Variables Sueltas (Dispersas)</span>', font="Consolas", font_size=12)
        l2 = MarkupText('<span foreground="#10b981"><b>int</b></span> <span foreground="#fca5a5">nota1</span>{<span foreground="#fbbf24">18</span>};', font="Consolas", font_size=13)
        l3 = MarkupText('<span foreground="#10b981"><b>int</b></span> <span foreground="#fca5a5">nota2</span>{<span foreground="#fbbf24">15</span>};', font="Consolas", font_size=13)
        l4 = MarkupText('<span foreground="#10b981"><b>int</b></span> <span foreground="#fca5a5">nota3</span>{<span foreground="#fbbf24">20</span>};', font="Consolas", font_size=13)
        l5 = MarkupText('<span foreground="#8b949e">// 2. Arreglo Contiguo (Indexable)</span>', font="Consolas", font_size=12)
        l6 = MarkupText('<span foreground="#10b981"><b>int</b></span> <span foreground="#6ee7b7"><b>notas</b></span>[<span foreground="#fbbf24">3</span>]{<span foreground="#fbbf24">18</span>, <span foreground="#fbbf24">15</span>, <span foreground="#fbbf24">20</span>};', font="Consolas", font_size=13)

        code_group = VGroup(l1, l2, l3, l4, l5, l6).arrange(DOWN, aligned_edge=LEFT, buff=0.14).move_to(code_bg.get_center() + DOWN * 0.05)

        # PANEL DERECHO: Tarjeta de Memoria RAM
        ram_group, ram_bg = self.create_card_panel(width=5.8, height=3.4, title="Mapa de Memoria RAM", subtitle="Direcciones Fisicas en Stack")
        ram_group.move_to(RIGHT * 3.4 + UP * Y_MAIN)

        self.play(FadeIn(win_group), FadeIn(ram_group), run_time=0.6)
        self.wait(0.5)

        # ACTO 1: Variables Dispersas
        self.play(Write(l1), Write(l2), Write(l3), Write(l4), run_time=0.9)

        var_a = self.create_cell("nota1: 18", width=2.0, height=0.55, color=self.COLOR_RED, font_size=11).move_to(ram_bg.get_center() + UP * 0.8 + LEFT * 0.9)
        var_b = self.create_cell("nota2: 15", width=2.0, height=0.55, color=self.COLOR_RED, font_size=11).move_to(ram_bg.get_center() + DOWN * 0.4 + RIGHT * 0.9)
        gap_txt = Text("(Memoria fragmentada no indexable)", font="Consolas", font_size=10, color=self.COLOR_MUTED).move_to(ram_bg.get_center() + UP * 0.2)

        self.play(
            FadeIn(var_a, shift=RIGHT * 0.2),
            FadeIn(var_b, shift=LEFT * 0.2),
            FadeIn(gap_txt),
            run_time=0.7
        )
        self.wait(2.8)

        # ACTO 2: Transformación a Secuencia Contigua
        self.play(
            FadeOut(var_a), FadeOut(var_b), FadeOut(gap_txt),
            Write(l5), Write(l6),
            run_time=0.8
        )

        c0 = self.create_cell("notas[0]\n18", width=1.5, height=0.7, color=self.COLOR_GREEN, font_size=11)
        c1 = self.create_cell("notas[1]\n15", width=1.5, height=0.7, color=self.COLOR_GREEN, font_size=11)
        c2 = self.create_cell("notas[2]\n20", width=1.5, height=0.7, color=self.COLOR_GREEN, font_size=11)
        
        arr_contiguous = VGroup(c0, c1, c2).arrange(RIGHT, buff=0.1).move_to(ram_bg.get_center() + UP * 0.1)
        addr_tag = Text("0x1000          0x1004          0x1008", font="Consolas", font_size=10, color=self.COLOR_CYAN).next_to(arr_contiguous, DOWN, buff=0.2)

        self.play(
            FadeIn(arr_contiguous, shift=UP * 0.2),
            FadeIn(addr_tag),
            Flash(arr_contiguous.get_center(), color=self.COLOR_GREEN, flash_radius=1.3),
            run_time=0.9
        )
        self.wait(2.8)

        # ACTO 3: HUD Footer con pausa generosa de lectura
        hud_group = self.create_hud_footer("MEMORIA CONTIGUA", "Elementos adyacentes en RAM: indexacion matematica O(1) y maximo rendimiento en cache.", color=self.COLOR_GREEN)
        self.play(FadeIn(hud_group, shift=UP * 0.2), run_time=0.7)
        self.wait(5.0)

if __name__ == "__main__":
    export_manim_scenes(__file__, "06_ArraysAndVectors", {"L01MemoriaContigua": "l01_memoria_contigua.gif"})
