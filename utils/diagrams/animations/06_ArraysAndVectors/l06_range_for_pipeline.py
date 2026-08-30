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

        Y_MAIN = 0.25

        # PANEL IZQUIERDO: Ventana de Código IDE con MarkupText Hiper-Realista
        win_group, code_bg = self.create_code_window(width=5.8, height=3.4, title="main.cpp")
        win_group.move_to(LEFT * 3.4 + UP * Y_MAIN)

        l1 = MarkupText('<span foreground="#38bdf8">std::vector</span>&lt;<span foreground="#10b981"><b>int</b></span>&gt; <span foreground="#fbbf24">datos</span>{<span foreground="#fbbf24">10</span>, <span foreground="#fbbf24">20</span>};', font="Consolas", font_size=12)
        l2 = MarkupText('<span foreground="#8b949e">// Bucle Seguro C++17 (Sin Indices Manuales)</span>', font="Consolas", font_size=11)
        l3 = MarkupText('<span foreground="#c084fc"><b>for</b></span> (<span foreground="#10b981"><b>int</b></span> <span foreground="#fbbf24">n</span> : <span foreground="#fbbf24">datos</span>) {', font="Consolas", font_size=13)
        l4 = MarkupText('    <span foreground="#38bdf8">std::cout</span> &lt;&lt; <span foreground="#fbbf24">n</span> &lt;&lt; <span foreground="#fca5a5">\'\\n\'</span>;', font="Consolas", font_size=13)
        l5 = MarkupText('}', font="Consolas", font_size=13, color="#f0f6fc")

        code_group = VGroup(l1, l2, l3, l4, l5).arrange(DOWN, aligned_edge=LEFT, buff=0.14).move_to(code_bg.get_center() + DOWN * 0.05)

        # PANEL DERECHO: Tarjeta de Memoria RAM
        ram_group, ram_bg = self.create_card_panel(width=5.8, height=3.4, title="Procesamiento en Heap", subtitle="Paso Secuencial Automático")
        ram_group.move_to(RIGHT * 3.4 + UP * Y_MAIN)

        self.play(FadeIn(win_group), FadeIn(ram_group), run_time=0.6)
        self.wait(0.5)

        # ACTO 1: Dibujar Vector (2 elementos exactos para máx 2 ciclos)
        self.play(Write(l1), run_time=0.6)

        c0 = self.create_cell("[0]\n10", width=1.5, height=0.75, color=self.COLOR_CYAN, font_size=12)
        c1 = self.create_cell("[1]\n20", width=1.5, height=0.75, color=self.COLOR_CYAN, font_size=12)
        vec_row = VGroup(c0, c1).arrange(RIGHT, buff=0.15).move_to(ram_bg.get_center() + DOWN * 0.25)

        self.play(FadeIn(vec_row), run_time=0.6)
        self.wait(0.6)

        # ACTO 2: Bucle for con 2 iteraciones
        self.play(Write(l2), Write(l3), Write(l4), Write(l5), run_time=0.8)

        # Iteración 1
        cursor = Arrow(start=UP * 0.8, end=UP * 0.15, buff=0.05, color=self.COLOR_GOLD, stroke_width=4.5).next_to(c0, UP, buff=0.15)
        val_badge = self.create_badge("Ciclo 1: n = 10", fill_color="#3b2d11", stroke_color=self.COLOR_GOLD, text_color=self.COLOR_GOLD_LIGHT, width=2.8, height=0.42).next_to(cursor, UP, buff=0.1)

        self.play(GrowArrow(cursor), FadeIn(val_badge), run_time=0.6)
        self.wait(2.5)

        # Iteración 2 (Máximo 2 ciclos)
        val_badge2 = self.create_badge("Ciclo 2: n = 20", fill_color="#3b2d11", stroke_color=self.COLOR_GOLD, text_color=self.COLOR_GOLD_LIGHT, width=2.8, height=0.42).next_to(c1, UP, buff=0.75)
        self.play(
            cursor.animate.next_to(c1, UP, buff=0.15),
            Transform(val_badge, val_badge2),
            run_time=0.8
        )
        self.wait(2.8)

        # ACTO 3: HUD Footer
        hud_group = self.create_hud_footer("CERO OFF-BY-ONE", "Range-based for recorre la coleccion de inicio a fin sin manipular indices manuales.", color=self.COLOR_CYAN)
        self.play(FadeIn(hud_group, shift=UP * 0.2), run_time=0.7)
        self.wait(5.0)

if __name__ == "__main__":
    export_manim_scenes(__file__, "06_ArraysAndVectors", {"L06RangeForPipeline": "l06_range_for_pipeline.gif"})
