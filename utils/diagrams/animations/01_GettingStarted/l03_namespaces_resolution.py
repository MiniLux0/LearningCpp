from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene, export_manim_scenes

class NamespacesResolution(BaseLearningScene):
    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "Espacios de Nombres (Namespaces)", 
            "Resolución de ámbito y prevención de colisión de símbolos con el operador ::"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.3)

        Y_MAIN = 0.2

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (5.4 x 3.0)
        win_group, code_bg = self.create_code_window(width=5.4, height=3.0, title="main.cpp")
        win_group.move_to(LEFT * 3.4 + UP * Y_MAIN)

        line1 = MarkupText(
            '<span foreground="#38bdf8"><b>Graficos</b></span><span foreground="#f59e0b">::</span><span foreground="#6ee7b7">dibujar</span>();',
            font="Consolas", font_size=15
        )
        line2 = MarkupText(
            '<span foreground="#fbbf24"><b>Audio</b></span><span foreground="#f59e0b">::</span><span foreground="#6ee7b7">dibujar</span>();',
            font="Consolas", font_size=15
        )

        line1.move_to(ORIGIN)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.35)

        code_lines = VGroup(line1, line2)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: DOS ÁMBITOS AISLADOS (5.4 x 3.0)
        box_graf = RoundedRectangle(
            width=5.0, height=1.1, corner_radius=0.12,
            fill_color="#0b1320", fill_opacity=0.98,
            stroke_color=self.COLOR_CYAN, stroke_width=1.8
        ).move_to(RIGHT * 3.4 + UP * (Y_MAIN + 0.65))
        lbl_graf = Text("namespace Graficos { void dibujar(); }", font="Consolas", font_size=12, color=self.COLOR_CYAN_LIGHT, weight=BOLD).move_to(box_graf.get_center())

        box_audio = RoundedRectangle(
            width=5.0, height=1.1, corner_radius=0.12,
            fill_color="#1f1807", fill_opacity=0.98,
            stroke_color=self.COLOR_GOLD, stroke_width=1.8
        ).move_to(RIGHT * 3.4 + UP * (Y_MAIN - 0.65))
        lbl_audio = Text("namespace Audio    { void dibujar(); }", font="Consolas", font_size=12, color=self.COLOR_GOLD_LIGHT, weight=BOLD).move_to(box_audio.get_center())

        ns_group = VGroup(box_graf, lbl_graf, box_audio, lbl_audio)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "NAMESPACES", 
            "Los espacios de nombres agrupan funciones y clases bajo un prefijo identificador unico.", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(win_group, shift=RIGHT * 0.2),
            FadeIn(code_lines, shift=RIGHT * 0.2),
            FadeIn(ns_group, shift=LEFT * 0.2),
            FadeIn(hud, shift=UP * 0.2),
            rate_func=smooth, run_time=0.6
        )
        self.wait(1.5)

        # FASE 1: Resolución a Graficos::dibujar()
        hud_fase1 = self.create_hud_footer(
            "RESOLUCION 1", 
            "Graficos:: le indica al compilador que ejecute 'dibujar()' en el modulo de renderizado.", 
            color=self.COLOR_CYAN
        )
        pointer1 = self.create_code_pointer(line1, color=self.COLOR_CYAN)
        arrow1 = Arrow(start=line1.get_right(), end=box_graf.get_left(), buff=0.15, color=self.COLOR_CYAN, stroke_width=3)

        self.play(
            FadeIn(pointer1, shift=RIGHT * 0.1),
            GrowArrow(arrow1),
            box_graf.animate.set_stroke(color="#ffffff", width=2.5),
            Flash(box_graf.get_center(), color=self.COLOR_CYAN, flash_radius=1.2, num_lines=12),
            ReplacementTransform(hud, hud_fase1),
            rate_func=smooth
        )
        self.play(box_graf.animate.set_stroke(color=self.COLOR_CYAN, width=1.8), run_time=0.2)
        self.wait(3.0)

        # FASE 2: Resolución a Audio::dibujar()
        hud_fase2 = self.create_hud_footer(
            "RESOLUCION 2", 
            "Audio:: redirige el flujo hacia la rutina de sintetizacion de sonido sin colisiones.", 
            color=self.COLOR_GOLD
        )
        pointer2 = self.create_code_pointer(line2, color=self.COLOR_GOLD)
        arrow2 = Arrow(start=line2.get_right(), end=box_audio.get_left(), buff=0.15, color=self.COLOR_GOLD, stroke_width=3)

        self.play(
            FadeOut(pointer1),
            FadeOut(arrow1),
            FadeIn(pointer2, shift=RIGHT * 0.1),
            GrowArrow(arrow2),
            box_audio.animate.set_stroke(color="#ffffff", width=2.5),
            Flash(box_audio.get_center(), color=self.COLOR_GOLD, flash_radius=1.2, num_lines=12),
            ReplacementTransform(hud_fase1, hud_fase2),
            rate_func=smooth
        )
        self.play(box_audio.animate.set_stroke(color=self.COLOR_GOLD, width=1.8), run_time=0.2)
        self.wait(3.0)

        # FASE 3: Insignia y Síntesis Final
        insight_badge = self.create_badge("Cero Colisiones de Nombres en Memoria", width=5.8).move_to(UP * 2.2 + RIGHT * 3.4)
        hud_final = self.create_hud_footer(
            "REGLA DE INGENIERIA", 
            "El prefijo explico 'std::' garantiza claridad y robustez en proyectos profesionales.", 
            color=self.COLOR_GREEN
        )

        self.play(
            FadeOut(pointer2),
            FadeOut(arrow2),
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
            "NamespacesResolution": "l03_namespaces_resolution.gif",
        },
        gif_width=960,
        fps=18
    )
