from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene, export_manim_scenes

class CoutStream(BaseLearningScene):
    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "Flujos de Salida Estándar (std::cout)", 
            "Inserción ordenada de bytes en el flujo de salida con el operador <<"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.3)

        Y_MAIN = 0.2

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (5.4 x 3.0)
        win_group, code_bg = self.create_code_window(width=5.4, height=3.0, title="main.cpp")
        win_group.move_to(LEFT * 3.4 + UP * Y_MAIN)

        line1 = MarkupText(
            '<span foreground="#c084fc">#include</span> '
            '<span foreground="#f59e0b">&lt;iostream&gt;</span>',
            font="Consolas", font_size=13
        )
        line2 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> '
            '<span foreground="#38bdf8"><b>main</b></span>() {',
            font="Consolas", font_size=13
        )
        line3 = MarkupText(
            '    <span foreground="#38bdf8">std::cout</span> &lt;&lt; '
            '<span foreground="#6ee7b7">"Hola Mundo\\n"</span>;',
            font="Consolas", font_size=13
        )
        line4 = MarkupText(
            '    <span foreground="#c084fc"><b>return</b></span> '
            '<span foreground="#38bdf8">0</span>;',
            font="Consolas", font_size=13
        )
        line5 = MarkupText(
            '}',
            font="Consolas", font_size=13
        )

        code_lines = VGroup(line1, line2, line3, line4, line5).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: TERMINAL DEL SISTEMA OPERATIVO (5.4 x 3.0)
        term_bg = RoundedRectangle(
            width=5.4, height=3.0, corner_radius=0.18,
            fill_color="#090d13", fill_opacity=0.98,
            stroke_color="#30363d", stroke_width=1.8
        ).move_to(RIGHT * 3.4 + UP * Y_MAIN)

        term_bar = RoundedRectangle(
            width=5.4, height=0.45, corner_radius=0.12,
            fill_color="#161b22", fill_opacity=1.0,
            stroke_color="#30363d", stroke_width=1
        ).next_to(term_bg.get_top(), DOWN, buff=0).shift(UP * 0.225)

        term_title = Text("Terminal / Consola OS", font="Consolas", font_size=13, color="#8b949e").move_to(term_bar.get_center())
        prompt_txt = Text("$ ./app", font="Consolas", font_size=13, color="#6e7681").move_to(term_bg.get_center() + UP * 0.55 + LEFT * 1.6)

        term_group = VGroup(term_bg, term_bar, term_title, prompt_txt)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "STREAM I/O", 
            "std::cout representa el canal de comunicacion entre el programa y la consola del sistema.", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(win_group, shift=RIGHT * 0.2),
            FadeIn(code_lines, shift=RIGHT * 0.2),
            FadeIn(term_group, shift=LEFT * 0.2),
            FadeIn(hud, shift=UP * 0.2),
            rate_func=smooth, run_time=0.6
        )
        self.wait(1.5)

        # FASE 1: Inyección en el flujo con <<
        hud_fase1 = self.create_hud_footer(
            "OPERADOR DE INSERCION (<<)", 
            "El operador '<<' empuja la secuencia de caracteres hacia el buffer de salida estándar.", 
            color=self.COLOR_GREEN
        )
        pointer = self.create_code_pointer(line3, color=self.COLOR_GREEN)

        msg_packet = VGroup(
            RoundedRectangle(width=2.8, height=0.60, corner_radius=0.08, fill_color="#064e3b", fill_opacity=0.98, stroke_color=self.COLOR_GREEN, stroke_width=1.8),
            Text('"Hola Mundo\\n"', font="Consolas", font_size=13, color="#6ee7b7", weight=BOLD)
        ).move_to(line3.get_center())

        arrow_stream = Arrow(start=code_bg.get_right(), end=term_bg.get_left(), buff=0.15, color=self.COLOR_GREEN, stroke_width=3.5)

        self.play(
            FadeIn(pointer, shift=RIGHT * 0.1),
            FadeIn(msg_packet),
            GrowArrow(arrow_stream),
            ReplacementTransform(hud, hud_fase1),
            rate_func=smooth
        )
        self.play(
            msg_packet.animate.move_to(term_bg.get_center() + DOWN * 0.10),
            rate_func=smooth, run_time=0.7
        )
        self.wait(3.0)

        # FASE 2: Despliegue en la Terminal
        hud_fase2 = self.create_hud_footer(
            "DESPLIEGUE EN PANTALLA", 
            "El buffer se vacia en la consola y el caracter '\\n' posiciona el cursor en la siguiente linea.", 
            color=self.COLOR_CYAN
        )
        term_out = Text("Hola Mundo", font="Consolas", font_size=18, color=self.COLOR_GREEN_LIGHT, weight=BOLD).move_to(term_bg.get_center() + DOWN * 0.05 + LEFT * 1.0)
        cursor_block = Rectangle(width=0.18, height=0.35, fill_color="#58a6ff", fill_opacity=0.8, stroke_width=0).next_to(term_bg.get_center() + DOWN * 0.55 + LEFT * 2.1, RIGHT, buff=0.05)

        self.play(
            ReplacementTransform(msg_packet, term_out),
            FadeIn(cursor_block),
            FadeOut(arrow_stream),
            Flash(term_out.get_center(), color=self.COLOR_GREEN, flash_radius=1.2, num_lines=12),
            ReplacementTransform(hud_fase1, hud_fase2),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 3: Insignia y Síntesis Final
        insight_badge = self.create_badge("Flujo de Salida Tipado y Seguro", width=5.8).move_to(UP * 2.2 + RIGHT * 3.4)
        hud_final = self.create_hud_footer(
            "SISTEMA C++", 
            "La cabecera <iostream> gestiona buffers y codificaciones de forma transparente y eficiente.", 
            color=self.COLOR_GREEN
        )

        self.play(
            FadeOut(pointer),
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
            "CoutStream": "l02_cout_stream.gif",
        },
        gif_width=960,
        fps=18
    )
