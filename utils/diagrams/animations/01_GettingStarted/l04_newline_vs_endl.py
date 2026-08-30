from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene, export_manim_scenes

class NewlineVsEndl(BaseLearningScene):
    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "Formato de Salida y Rendimiento", 
            "'\\n' (Instantáneo en RAM) vs std::endl (Forzado de Flush y Bloqueo I/O)"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.3)

        Y_MAIN = 0.2

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (5.4 x 3.0)
        win_group, code_bg = self.create_code_window(width=5.4, height=3.0, title="main.cpp")
        win_group.move_to(LEFT * 3.4 + UP * Y_MAIN)

        line1 = MarkupText(
            '<span foreground="#38bdf8">std::cout</span> &lt;&lt; '
            '<span foreground="#6ee7b7">\'\\n\'</span>;     <span foreground="#10b981">// Rapido (RAM)</span>',
            font="Consolas", font_size=13
        )
        line2 = MarkupText(
            '<span foreground="#38bdf8">std::cout</span> &lt;&lt; '
            '<span foreground="#fca5a5">std::endl</span>; <span foreground="#ef4444">// Lento (Flush)</span>',
            font="Consolas", font_size=13
        )

        line1.move_to(ORIGIN)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.35)

        code_lines = VGroup(line1, line2)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: BUFFER DE SALIDA EN RAM (5.4 x 3.0)
        buf_card, buf_bg = self.create_card_panel(
            width=5.4, height=3.0, 
            title="Buffer de Salida en RAM", 
            subtitle="Memoria Intermedia de E/S"
        )
        buf_card.move_to(RIGHT * 3.4 + UP * Y_MAIN)

        buf_pipe = RoundedRectangle(
            width=4.6, height=0.9, corner_radius=0.1,
            fill_color="#0b0f19", fill_opacity=0.98,
            stroke_color=self.COLOR_GREEN, stroke_width=1.8
        ).move_to(buf_bg.get_center() + UP * 0.20)

        char_nl = VGroup(
            RoundedRectangle(width=0.9, height=0.6, corner_radius=0.08, fill_color="#064e3b", fill_opacity=0.98, stroke_color=self.COLOR_GREEN, stroke_width=1.8),
            Text("\\n", font="Consolas", font_size=16, color="#6ee7b7", weight=BOLD)
        ).move_to(buf_pipe.get_center() + LEFT * 1.4)

        buf_full = VGroup(buf_card, buf_pipe)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "BUFFER I/O", 
            "La biblioteca estandar almacena caracteres en RAM antes de transferirlos a la pantalla.", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(win_group, shift=RIGHT * 0.2),
            FadeIn(code_lines, shift=RIGHT * 0.2),
            FadeIn(buf_full, shift=LEFT * 0.2),
            FadeIn(hud, shift=UP * 0.2),
            rate_func=smooth, run_time=0.6
        )
        self.wait(1.5)

        # FASE 1: Inserción de '\n' (Sin Flush)
        hud_fase1 = self.create_hud_footer(
            "SALTO DIRECTO ('\\n')", 
            "'\\n' solo agrega 1 byte al buffer en RAM a velocidad de nanosegundos (Cero I/O Blocking).", 
            color=self.COLOR_GREEN
        )
        pointer1 = self.create_code_pointer(line1, color=self.COLOR_GREEN)

        self.play(
            FadeIn(pointer1, shift=RIGHT * 0.1),
            FadeIn(char_nl, shift=RIGHT * 0.4),
            Flash(char_nl.get_center(), color=self.COLOR_GREEN, flash_radius=1.1, num_lines=10),
            ReplacementTransform(hud, hud_fase1),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 2: Inserción de std::endl (Forzado de Flush)
        hud_fase2 = self.create_hud_footer(
            "FORZADO DE FLUSH (std::endl)", 
            "std::endl introduce '\\n' y fuerza una llamada al sistema para vaciar el buffer, frenando la CPU.", 
            color=self.COLOR_RED
        )
        pointer2 = self.create_code_pointer(line2, color=self.COLOR_RED)

        flush_warning = VGroup(
            RoundedRectangle(width=4.6, height=0.55, corner_radius=0.08, fill_color="#180a0a", fill_opacity=0.98, stroke_color=self.COLOR_RED, stroke_width=1.8),
            Text("FORCING FLUSH -> Bloqueo de Hardware", font="Consolas", font_size=12, color=self.COLOR_RED_LIGHT, weight=BOLD)
        ).move_to(buf_bg.get_center() + DOWN * 0.65)

        self.play(
            FadeOut(pointer1),
            FadeIn(pointer2, shift=RIGHT * 0.1),
            FadeIn(flush_warning, shift=UP * 0.15),
            buf_pipe.animate.set_stroke(color=self.COLOR_RED, width=2.2),
            Flash(flush_warning.get_center(), color=self.COLOR_RED, flash_radius=1.2, num_lines=12),
            ReplacementTransform(hud_fase1, hud_fase2),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 3: Insignia y Síntesis Final
        insight_badge = self.create_badge("Regla Profesional: Usa Siempre '\\n'", width=5.8).move_to(UP * 2.2 + RIGHT * 3.4)
        hud_final = self.create_hud_footer(
            "MAXIMO RENDIMIENTO", 
            "Deja que el Sistema Operativo vacie el buffer automaticamente cuando sea eficiente.", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeOut(pointer2),
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
            "NewlineVsEndl": "l04_newline_vs_endl.gif",
        },
        gif_width=960,
        fps=18
    )
