from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene, export_manim_scenes

class L04StringViewRef(BaseLearningScene):
    def construct(self):
        # 1. Encabezado estándar
        header = self.create_header("Vistas Ligeras (std::string_view)", "Zero-Copy vs Clonacion Pesada de Texto")
        self.add(header)
        self.wait(0.4)

        Y_MAIN = 0.2

        # PANEL IZQUIERDO: Ventana de Código IDE
        win_group, code_bg = self.create_code_window(width=5.4, height=3.0, title="main.cpp")
        win_group.move_to(LEFT * 3.4 + UP * Y_MAIN)

        code_lines = VGroup(
            Text("std::string libro{\"C++...\";}", font="Consolas", font_size=14, color=self.COLOR_CYAN),
            Text("void leer(std::string_view v);", font="Consolas", font_size=13, color=self.COLOR_GOLD_LIGHT),
            Text("leer(libro); // Zero-Copy", font="Consolas", font_size=13, color=self.COLOR_GREEN)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(code_bg.get_center() + DOWN * 0.1)

        # PANEL DERECHO: Tarjeta de Memoria RAM
        ram_group, ram_bg = self.create_card_panel(width=5.4, height=3.0, title="Memoria RAM Original", subtitle="Direccion: 0x7FFEE0 (500 KB)")
        ram_group.move_to(RIGHT * 3.4 + UP * Y_MAIN)

        orig_buf = RoundedRectangle(
            width=4.4, height=0.75, corner_radius=0.1,
            fill_color="#1e1e2e", fill_opacity=0.9,
            stroke_color=self.COLOR_CYAN, stroke_width=1.8
        ).move_to(ram_bg.get_center() + UP * 0.15)
        orig_txt = Text("\"C++ Moderno para Sistemas\"", font="Consolas", font_size=13, color="#ffffff", weight=BOLD).move_to(orig_buf.get_center())

        ram_full = VGroup(ram_group, orig_buf, orig_txt)
        self.play(FadeIn(win_group), FadeIn(ram_full), run_time=0.5)
        self.wait(0.2)

        # ACTO 1: Invocación de Función con string_view
        self.play(Write(code_lines[0]), Write(code_lines[1]), run_time=0.7)
        self.wait(0.3)
        self.play(Write(code_lines[2]), run_time=0.5)

        # ACTO 2: Creación del Observador Ligero [ptr | len]
        view_box = RoundedRectangle(
            width=4.4, height=0.6, corner_radius=0.08,
            fill_color=self.COLOR_GOLD, fill_opacity=0.2,
            stroke_color=self.COLOR_GOLD, stroke_width=2
        ).move_to(ram_bg.get_center() + DOWN * 0.75)
        view_txt = Text("string_view [ptr: 0x7FFEE0 | len: 26]", font="Consolas", font_size=11, color=self.COLOR_GOLD_LIGHT, weight=BOLD).move_to(view_box.get_center())

        view_arrow = Arrow(
            start=view_box.get_top(),
            end=orig_buf.get_bottom(),
            buff=0.08,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.25,
            color=self.COLOR_GOLD
        )

        self.play(
            FadeIn(view_box, shift=UP * 0.2),
            FadeIn(view_txt, shift=UP * 0.2),
            GrowArrow(view_arrow),
            Flash(orig_buf.get_center(), color=self.COLOR_GOLD, flash_radius=1.2, num_lines=12),
            run_time=0.8
        )
        self.wait(0.4)

        # ACTO 3: Insignia de Rendimiento y HUD Inferior
        insight_badge = self.create_badge("Zero-Copy: Solo 16 bytes en Stack", width=5.8).move_to(UP * 2.2 + RIGHT * 3.4)
        hud_group = self.create_hud_footer("ZERO-COPY", "std::string_view observa el texto existente sin clonar memoria.", color=self.COLOR_CYAN)

        self.play(
            FadeIn(insight_badge, shift=DOWN * 0.15),
            FadeIn(hud_group, shift=UP * 0.25),
            run_time=0.7
        )
        self.wait(3.8)

if __name__ == "__main__":
    export_manim_scenes(__file__, "05_ConstantsAndStrings", {"L04StringViewRef": "l04_string_view_ref.gif"})
