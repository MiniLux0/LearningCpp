from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene, export_manim_image

class L01StackVsContiguo(BaseLearningScene):
    def construct(self):
        # 1. Encabezado
        header = self.create_header("Modelo Físico de Memoria RAM", "Variables Sueltas en Stack vs Colección Contigua")
        self.add(header)

        # PANEL SUPERIOR: Variables Sueltas
        panel_top, bg_top = self.create_card_panel(width=12.2, height=2.4, title="1. Variables Sueltas Desconectadas (Stack)", subtitle="Identificadores independientes en memoria no contigua")
        panel_top.move_to(UP * 1.5)

        va = self.create_cell("nota1 (0x1000)\nValor: 18", width=2.4, height=0.9, color=self.COLOR_RED, font_size=11).move_to(bg_top.get_center() + LEFT * 3.6 + DOWN * 0.15)
        vb = self.create_cell("nota2 (0x1084)\nValor: 15", width=2.4, height=0.9, color=self.COLOR_RED, font_size=11).move_to(bg_top.get_center() + DOWN * 0.15)
        vc = self.create_cell("nota3 (0x1120)\nValor: 20", width=2.4, height=0.9, color=self.COLOR_RED, font_size=11).move_to(bg_top.get_center() + RIGHT * 3.6 + DOWN * 0.15)
        
        warn_badge = self.create_badge("INCOMPATIBLE CON BUCLES (Sin patron de direccion)", fill_color="#3b1115", stroke_color=self.COLOR_RED, text_color=self.COLOR_RED_LIGHT, width=5.5, height=0.38).move_to(bg_top.get_center() + UP * 0.55 + RIGHT * 2.8)

        # PANEL INFERIOR: Colección Contigua
        panel_bot, bg_bot = self.create_card_panel(width=12.2, height=2.6, title="2. Colección Contigua Indexable (Array / Vector)", subtitle="Elementos adyacentes calculables por formula matematica: Base + (Indice * Size)")
        panel_bot.move_to(DOWN * 1.6)

        c0 = self.create_cell("[0] 0x1000\n18", width=2.2, height=0.9, color=self.COLOR_GREEN, font_size=11)
        c1 = self.create_cell("[1] 0x1004\n15", width=2.2, height=0.9, color=self.COLOR_GREEN, font_size=11)
        c2 = self.create_cell("[2] 0x1008\n20", width=2.2, height=0.9, color=self.COLOR_GREEN, font_size=11)
        arr_row = VGroup(c0, c1, c2).arrange(RIGHT, buff=0.15).move_to(bg_bot.get_center() + LEFT * 2.2 + DOWN * 0.15)

        success_badge = self.create_badge("ACCESO O(1) + CPU CACHE L1/L2", fill_color="#064e3b", stroke_color=self.COLOR_GREEN, text_color=self.COLOR_GREEN_LIGHT, width=4.2, height=0.45).move_to(bg_bot.get_center() + RIGHT * 3.4 + DOWN * 0.15)

        self.add(panel_top, va, vb, vc, warn_badge)
        self.add(panel_bot, arr_row, success_badge)

if __name__ == "__main__":
    export_manim_image(__file__, "06_ArraysAndVectors", {"L01StackVsContiguo": "l01_stack_vs_contiguo.png"})
