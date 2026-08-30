from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene, export_manim_scenes

class CompilationPipeline(BaseLearningScene):
    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "El Pipeline del Compilador", 
            "De Código Fuente C++ a Binario Nativo de Máquina (x86_64)"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.3)

        Y_MAIN = 0.2

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO FUENTE (4.0 x 3.0)
        win_group, code_bg = self.create_code_window(width=4.0, height=3.0, title="main.cpp")
        win_group.move_to(LEFT * 4.4 + UP * Y_MAIN)

        line1 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> '
            '<span foreground="#38bdf8"><b>main</b></span>() {',
            font="Consolas", font_size=13
        )
        line2 = MarkupText(
            '    <span foreground="#c084fc"><b>return</b></span> '
            '<span foreground="#38bdf8">0</span>;',
            font="Consolas", font_size=13
        )
        line3 = MarkupText(
            '}',
            font="Consolas", font_size=13
        )

        line1.move_to(ORIGIN)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.20)
        line3.next_to(line2, DOWN, aligned_edge=LEFT, buff=0.20)

        code_lines = VGroup(line1, line2, line3)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL CENTRAL: MOTOR DE COMPILACIÓN g++ (3.8 x 3.0)
        comp_group, comp_bg = self.create_card_panel(
            width=3.8, height=3.0, 
            title="Compilador g++", 
            subtitle="Parser & Optimizador AST"
        )
        comp_group.move_to(UP * Y_MAIN)

        gear_box = RoundedRectangle(
            width=3.0, height=0.9, corner_radius=0.1,
            fill_color="#180f24", fill_opacity=0.98,
            stroke_color=self.COLOR_PURPLE, stroke_width=1.8
        ).move_to(comp_bg.get_center() + DOWN * 0.40)
        gear_txt = Text("AST -> Codegen", font="Consolas", font_size=13, color=self.COLOR_PURPLE_LIGHT, weight=BOLD).move_to(gear_box.get_center())

        comp_full = VGroup(comp_group, gear_box, gear_txt)

        # 4. PANEL DERECHO: BINARIO NATIVO (4.0 x 3.0)
        bin_group, bin_bg = self.create_card_panel(
            width=4.0, height=3.0, 
            title="app.exe (Binario)", 
            subtitle="Instrucciones CPU Nativas"
        )
        bin_group.move_to(RIGHT * 4.4 + UP * Y_MAIN)

        bin_box = RoundedRectangle(
            width=3.2, height=1.1, corner_radius=0.1,
            fill_color="#064e3b", fill_opacity=0.40,
            stroke_color=self.COLOR_GREEN, stroke_width=2.0
        ).move_to(bin_bg.get_center() + DOWN * 0.40)

        bits_txt = Text("01001000 10001001\n11000000 11000011", font="Consolas", font_size=11, color="#6ee7b7", weight=BOLD).move_to(bin_box.get_center())
        bin_full = VGroup(bin_group, bin_box, bits_txt)

        # Flechas de flujo
        arrow1 = Arrow(start=code_bg.get_right(), end=comp_bg.get_left(), buff=0.12, color=self.COLOR_PURPLE, stroke_width=3)
        arrow2 = Arrow(start=comp_bg.get_right(), end=bin_bg.get_left(), buff=0.12, color=self.COLOR_GREEN, stroke_width=3)

        # HUD INICIAL
        hud = self.create_hud_footer(
            "PIPELINE", 
            "El compilador transforma el texto plano en codigo binario ejecutable directamente por la CPU.", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(win_group, shift=RIGHT * 0.2),
            FadeIn(code_lines, shift=RIGHT * 0.2),
            FadeIn(comp_full, shift=UP * 0.2),
            FadeIn(bin_full, shift=LEFT * 0.2),
            FadeIn(hud, shift=UP * 0.2),
            rate_func=smooth, run_time=0.6
        )
        self.wait(1.5)

        # FASE 1: Análisis Sintáctico (Parsing a g++)
        hud_fase1 = self.create_hud_footer(
            "FASE 1: PARSING", 
            "g++ lee el codigo fuente, valida la gramatica y genera el arbol de sintaxis abstracta (AST).", 
            color=self.COLOR_PURPLE
        )
        signal1 = Dot(radius=0.14, color=self.COLOR_GOLD_LIGHT).move_to(code_bg.get_center())

        self.play(
            GrowArrow(arrow1),
            FadeIn(signal1),
            ReplacementTransform(hud, hud_fase1),
            rate_func=smooth
        )
        self.play(
            signal1.animate.move_to(comp_bg.get_center()),
            rate_func=rush_into, run_time=0.5
        )
        self.play(
            Flash(gear_box.get_center(), color=self.COLOR_PURPLE, flash_radius=1.2, num_lines=12),
            gear_box.animate.set_stroke(color=self.COLOR_GOLD, width=2.2),
            FadeOut(signal1),
            run_time=0.5
        )
        self.wait(3.0)

        # FASE 2: Generación de Código Máquina (Codegen)
        hud_fase2 = self.create_hud_footer(
            "FASE 2: CODEGEN", 
            "El optimizador traduce el AST a instrucciones binarias en lenguaje maquina (OpCodes x86_64).", 
            color=self.COLOR_GREEN
        )
        signal2 = Dot(radius=0.14, color=self.COLOR_GREEN_LIGHT).move_to(comp_bg.get_center())

        self.play(
            GrowArrow(arrow2),
            FadeIn(signal2),
            ReplacementTransform(hud_fase1, hud_fase2),
            rate_func=smooth
        )
        self.play(
            signal2.animate.move_to(bin_bg.get_center()),
            rate_func=rush_from, run_time=0.5
        )
        self.play(
            Flash(bin_box.get_center(), color=self.COLOR_GREEN, flash_radius=1.3, num_lines=14),
            bin_box.animate.set_stroke(color="#ffffff", width=2.5),
            FadeOut(signal2),
            run_time=0.5
        )
        self.play(bin_box.animate.set_stroke(color=self.COLOR_GREEN, width=2.0), run_time=0.2)
        self.wait(3.0)

        # FASE 3: Insignia y Síntesis Final
        insight_badge = self.create_badge("Ejecucion Nativa Directa a la CPU (Cero VM)", width=5.8).move_to(UP * 2.2 + RIGHT * 3.4)
        hud_final = self.create_hud_footer(
            "COMPUTACION REAL", 
            "C++ no requiere interpretes ni maquinas virtuales: se ejecuta al maximo rendimiento del procesador.", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(insight_badge, shift=DOWN * 0.15),
            ReplacementTransform(hud_fase2, hud_final),
            rate_func=smooth
        )
        # Pausa final obligatoria de 5.0s
        self.wait(5.0)

if __name__ == "__main__":
    export_manim_scenes(
        script_file=__file__,
        module_name="01_GettingStarted",
        scenes_dict={
            "CompilationPipeline": "l00_compilation.gif",
        },
        gif_width=960,
        fps=18
    )
