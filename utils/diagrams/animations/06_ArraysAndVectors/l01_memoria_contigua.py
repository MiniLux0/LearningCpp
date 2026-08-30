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

        Y_MAIN = 0.2

        # PANEL IZQUIERDO: Ventana de Código IDE (Aprovechamiento completo del espacio)
        win_group, code_bg = self.create_code_window(width=5.8, height=3.3, title="main.cpp")
        win_group.move_to(LEFT * 3.4 + UP * Y_MAIN)

        code_lines = VGroup(
            Text("// 1. Variables Sueltas (Inconexas)", font="Consolas", font_size=12, color=self.COLOR_MUTED),
            Text("int nota1{18};", font="Consolas", font_size=13, color=self.COLOR_RED_LIGHT),
            Text("int nota2{15};", font="Consolas", font_size=13, color=self.COLOR_RED_LIGHT),
            Text("int nota3{20};", font="Consolas", font_size=13, color=self.COLOR_RED_LIGHT),
            Text("\n// 2. Coleccion Contigua (Indexable)", font="Consolas", font_size=12, color=self.COLOR_MUTED),
            Text("int notas[3]{18, 15, 20};", font="Consolas", font_size=14, color=self.COLOR_GREEN_LIGHT, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(code_bg.get_center() + DOWN * 0.05)

        # PANEL DERECHO: Tarjeta de Memoria RAM
        ram_group, ram_bg = self.create_card_panel(width=5.8, height=3.3, title="Mapa de Memoria RAM", subtitle="Direcciones Fisicas en Stack")
        ram_group.move_to(RIGHT * 3.4 + UP * Y_MAIN)

        self.play(FadeIn(win_group), FadeIn(ram_group), run_time=0.6)
        self.wait(0.5)

        # ACTO 1: Variables Dispersas en Stack
        self.play(
            Write(code_lines[0]),
            Write(code_lines[1]),
            Write(code_lines[2]),
            Write(code_lines[3]),
            run_time=0.9
        )

        var_a = self.create_cell("nota1: 18", width=2.2, height=0.55, color=self.COLOR_RED, font_size=11).move_to(ram_bg.get_center() + UP * 0.75 + LEFT * 0.8)
        var_b = self.create_cell("nota2: 15", width=2.2, height=0.55, color=self.COLOR_RED, font_size=11).move_to(ram_bg.get_center() + DOWN * 0.4 + RIGHT * 0.8)
        gap_txt = Text("(Memoria fragmentada sin orden)", font="Consolas", font_size=10, color=self.COLOR_MUTED).move_to(ram_bg.get_center() + UP * 0.15)

        self.play(
            FadeIn(var_a, shift=RIGHT * 0.2),
            FadeIn(var_b, shift=LEFT * 0.2),
            FadeIn(gap_txt),
            run_time=0.7
        )
        self.wait(1.2)

        # ACTO 2: Transformación a Secuencia Contigua
        self.play(
            FadeOut(var_a), FadeOut(var_b), FadeOut(gap_txt),
            Write(code_lines[4]), Write(code_lines[5]),
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
        self.wait(1.5)

        # ACTO 3: HUD Footer con pausa generosa de lectura
        hud_group = self.create_hud_footer("MEMORIA CONTIGUA", "Elementos adyacentes en RAM: acceso O(1) y maximo rendimiento en cache del CPU.", color=self.COLOR_GREEN)
        self.play(FadeIn(hud_group, shift=UP * 0.2), run_time=0.7)
        self.wait(5.5)

if __name__ == "__main__":
    export_manim_scenes(__file__, "06_ArraysAndVectors", {"L01MemoriaContigua": "l01_memoria_contigua.gif"})
