from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene, export_manim_scenes

class L02ConstexprCompiletime(BaseLearningScene):
    def construct(self):
        # 1. Encabezado estándar
        header = self.create_header("Evaluacion en Tiempo de Compilacion", "Calculos instantaneos con constexpr")
        self.add(header)
        self.wait(0.4)

        Y_MAIN = 0.2

        # PANEL IZQUIERDO: Ventana de Código IDE
        win_group, code_bg = self.create_code_window(width=5.4, height=3.0, title="main.cpp")
        win_group.move_to(LEFT * 3.4 + UP * Y_MAIN)

        code_lines = VGroup(
            Text("constexpr int dias{7};", font="Consolas", font_size=15, color=self.COLOR_GOLD_LIGHT),
            Text("constexpr int horas{dias * 24};", font="Consolas", font_size=14, color=self.COLOR_PURPLE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).move_to(code_bg.get_center() + DOWN * 0.1)

        # PANEL DERECHO: Tarjeta de Compilación vs Binario
        stage_group, stage_bg = self.create_card_panel(width=5.4, height=3.0, title="Fase 1: Compilador g++", subtitle="Evaluacion Aritmetica en RAM")
        stage_group.move_to(RIGHT * 3.4 + UP * Y_MAIN)

        stage_title = stage_group[1]
        stage_sub = stage_group[2]

        calc_box = RoundedRectangle(
            width=4.4, height=1.1, corner_radius=0.12,
            fill_color="#1e1e2e", fill_opacity=0.9,
            stroke_color=self.COLOR_PURPLE, stroke_width=1.5
        ).move_to(stage_bg.get_center() + DOWN * 0.45)

        calc_expr = Text("7 * 24 = ?", font="Consolas", font_size=20, color=self.COLOR_PURPLE).move_to(calc_box.get_center())

        stage_full = VGroup(stage_group, calc_box, calc_expr)
        self.play(FadeIn(win_group), FadeIn(stage_full), run_time=0.5)
        self.wait(0.2)

        # ACTO 1: constexpr resuelto por g++
        self.play(Write(code_lines[0]), Write(code_lines[1]), run_time=0.8)
        self.wait(0.3)

        calc_resolved = Text("7 * 24 = 168", font="Consolas", font_size=20, color=self.COLOR_GOLD_LIGHT, weight=BOLD).move_to(calc_box.get_center())
        
        self.play(
            ReplacementTransform(calc_expr, calc_resolved),
            calc_box.animate.set_stroke(color=self.COLOR_GOLD, width=2.5),
            Flash(calc_box.get_center(), color=self.COLOR_GOLD, flash_radius=1.2, num_lines=12),
            run_time=0.7
        )
        self.wait(0.4)

        # ACTO 2: Transición a Binario Final
        runtime_title = Text("Fase 2: Ejecutable Binario", font="Consolas", font_size=15, color=self.COLOR_GREEN, weight=BOLD).move_to(stage_title.get_center())
        runtime_sub = Text("Valor inyectado directamente", font="Consolas", font_size=12, color="#6e7681").move_to(stage_sub.get_center())

        binary_val_box = RoundedRectangle(
            width=4.0, height=1.1, corner_radius=0.12,
            fill_color="#064e3b", fill_opacity=0.35,
            stroke_color=self.COLOR_GREEN, stroke_width=2
        ).move_to(calc_box.get_center())

        binary_val_text = Text("horas = 168", font="Consolas", font_size=22, color="#6ee7b7", weight=BOLD).move_to(binary_val_box.get_center())

        self.play(
            ReplacementTransform(stage_title, runtime_title),
            ReplacementTransform(stage_sub, runtime_sub),
            ReplacementTransform(calc_box, binary_val_box),
            ReplacementTransform(calc_resolved, binary_val_text),
            run_time=0.8
        )
        self.wait(0.4)

        # ACTO 3: Insignia de Eficiencia y HUD Inferior
        insight_badge = self.create_badge("0 Ciclos de CPU en Runtime", width=5.8).move_to(UP * 2.2 + RIGHT * 3.4)
        hud_group = self.create_hud_footer("OPTIMIZACION", "El compilador calculo '168' por adelantado. Cero costo en vivo.", color=self.COLOR_CYAN)

        self.play(
            FadeIn(insight_badge, shift=DOWN * 0.15),
            FadeIn(hud_group, shift=UP * 0.25),
            run_time=0.7
        )
        self.wait(3.8)

if __name__ == "__main__":
    export_manim_scenes(__file__, "05_ConstantsAndStrings", {"L02ConstexprCompiletime": "l02_constexpr_compiletime.gif"})
