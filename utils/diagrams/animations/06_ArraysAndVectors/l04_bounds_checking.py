from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene, export_manim_scenes

class L04BoundsChecking(BaseLearningScene):
    def construct(self):
        # 1. Encabezado estándar
        header = self.create_header("Acceso Seguro a Vectores", "operator[] Ciego vs Bounds Checking con .at()")
        self.add(header)
        self.wait(0.6)

        Y_MAIN = 0.2

        # PANEL IZQUIERDO: Ventana de Código IDE (Aprovechando el ancho)
        win_group, code_bg = self.create_code_window(width=5.8, height=3.3, title="main.cpp")
        win_group.move_to(LEFT * 3.4 + UP * Y_MAIN)

        code_lines = VGroup(
            Text("std::vector<int> v{10, 20, 30}; // size = 3", font="Consolas", font_size=12, color=self.COLOR_CYAN),
            Text("\n// 1. operator[] (Ciego / Sin Bounds Checking)", font="Consolas", font_size=11, color=self.COLOR_MUTED),
            Text("int x = v[5]; // Acceso Ciego a Memoria!", font="Consolas", font_size=12, color=self.COLOR_RED, weight=BOLD),
            Text("\n// 2. Metodo .at() (Protegido con Excepcion)", font="Consolas", font_size=11, color=self.COLOR_MUTED),
            Text("int y = v.at(5); // Lanza std::out_of_range", font="Consolas", font_size=12, color=self.COLOR_GREEN_LIGHT, weight=BOLD)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.10).move_to(code_bg.get_center() + DOWN * 0.05)

        # PANEL DERECHO: Tarjeta de Memoria RAM
        ram_group, ram_bg = self.create_card_panel(width=5.8, height=3.3, title="Validacion de Limites", subtitle="size = 3 (indices validos: 0, 1, 2)")
        ram_group.move_to(RIGHT * 3.4 + UP * Y_MAIN)

        self.play(FadeIn(win_group), FadeIn(ram_group), run_time=0.6)
        self.wait(0.5)

        # ACTO 1: Renderizar celdas válidas en memoria
        self.play(Write(code_lines[0]), run_time=0.6)

        c0 = self.create_cell("[0]\n10", width=1.1, height=0.7, color=self.COLOR_CYAN, font_size=11)
        c1 = self.create_cell("[1]\n20", width=1.1, height=0.7, color=self.COLOR_CYAN, font_size=11)
        c2 = self.create_cell("[2]\n30", width=1.1, height=0.7, color=self.COLOR_CYAN, font_size=11)
        vec_cells = VGroup(c0, c1, c2).arrange(RIGHT, buff=0.08).move_to(ram_bg.get_center() + UP * 0.45 + LEFT * 0.6)

        self.play(FadeIn(vec_cells), run_time=0.6)
        self.wait(0.8)

        # ACTO 2: Error ciego con [] - Flecha roja gruesa y clara
        self.play(Write(code_lines[1]), Write(code_lines[2]), run_time=0.7)

        blind_arrow = Arrow(
            start=c2.get_right() + RIGHT * 0.08,
            end=c2.get_right() + RIGHT * 1.8,
            buff=0,
            color=self.COLOR_RED,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.3
        )
        blind_badge = self.create_badge("UB: Fuera de Limites", fill_color="#3b1115", stroke_color=self.COLOR_RED, text_color=self.COLOR_RED_LIGHT, width=2.4, height=0.4).next_to(blind_arrow, UP, buff=0.1)

        self.play(
            GrowArrow(blind_arrow),
            FadeIn(blind_badge, shift=UP * 0.1),
            Flash(blind_arrow.get_end(), color=self.COLOR_RED, flash_radius=1.2),
            run_time=0.9
        )
        self.wait(1.8)

        # ACTO 3: Protección con .at()
        self.play(
            FadeOut(blind_arrow), FadeOut(blind_badge),
            Write(code_lines[3]), Write(code_lines[4]),
            run_time=0.8
        )

        shield_barrier = RoundedRectangle(
            width=0.25, height=1.1, corner_radius=0.05,
            fill_color=self.COLOR_GREEN, fill_opacity=0.8,
            stroke_color=self.COLOR_GREEN_LIGHT, stroke_width=2.5
        ).next_to(c2, RIGHT, buff=0.15)

        shield_badge = self.create_badge("Barrera .at() -> Lanza std::out_of_range", fill_color="#064e3b", stroke_color=self.COLOR_GREEN, text_color=self.COLOR_GREEN_LIGHT, width=4.8, height=0.45).move_to(ram_bg.get_center() + DOWN * 0.65)

        self.play(
            FadeIn(shield_barrier, scale=1.2),
            FadeIn(shield_badge, shift=UP * 0.15),
            Flash(shield_barrier.get_center(), color=self.COLOR_GREEN, flash_radius=1.3),
            run_time=0.9
        )
        self.wait(2.0)

        # ACTO 4: HUD Footer con tiempo generoso de lectura
        hud_group = self.create_hud_footer("ACCESO SEGURO", ".at() valida los limites en cada lectura, previniendo lecturas y corrupciones silenciosas.", color=self.COLOR_GREEN)
        self.play(FadeIn(hud_group, shift=UP * 0.2), run_time=0.7)
        self.wait(6.0)

if __name__ == "__main__":
    export_manim_scenes(__file__, "06_ArraysAndVectors", {"L04BoundsChecking": "l04_bounds_checking.gif"})
