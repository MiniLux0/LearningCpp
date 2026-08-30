from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene, export_manim_scenes

class IoPipeline(BaseLearningScene):
    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "Ciclo Interactivo de Entrada/Salida (I/O)", 
            "Coordinación bidireccional entre la consola del SO y el programa C++"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.3)

        Y_MAIN = 0.2

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (5.4 x 3.0)
        win_group, code_bg = self.create_code_window(width=5.4, height=3.0, title="main.cpp")
        win_group.move_to(LEFT * 3.4 + UP * Y_MAIN)

        line1 = MarkupText(
            '<span foreground="#38bdf8">std::cout</span> &lt;&lt; '
            '<span foreground="#6ee7b7">"Nombre: "</span>;',
            font="Consolas", font_size=13
        )
        line2 = MarkupText(
            '<span foreground="#38bdf8">std::cin</span> &gt;&gt; '
            '<span foreground="#fbbf24">nombre</span>;',
            font="Consolas", font_size=13
        )
        line3 = MarkupText(
            '<span foreground="#38bdf8">std::cout</span> &lt;&lt; '
            '<span foreground="#6ee7b7">"Hola "</span> &lt;&lt; '
            '<span foreground="#fbbf24">nombre</span> &lt;&lt; '
            '<span foreground="#6ee7b7">\'\\n\'</span>;',
            font="Consolas", font_size=12
        )

        line1.move_to(ORIGIN)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.25)
        line3.next_to(line2, DOWN, aligned_edge=LEFT, buff=0.25)

        code_lines = VGroup(line1, line2, line3)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: TERMINAL INTERACTIVO (5.4 x 3.0)
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

        term_title = Text("Terminal Interactivo OS", font="Consolas", font_size=13, color="#8b949e").move_to(term_bar.get_center())

        t_line1 = Text("Nombre: ", font="Consolas", font_size=14, color="#f0f6fc").move_to(term_bg.get_center() + UP * 0.50 + LEFT * 1.3)
        t_input = Text("Link", font="Consolas", font_size=14, color=self.COLOR_GOLD_LIGHT, weight=BOLD).next_to(t_line1, RIGHT, buff=0.1)
        t_line2 = Text("Hola Link", font="Consolas", font_size=16, color=self.COLOR_GREEN_LIGHT, weight=BOLD).move_to(term_bg.get_center() + DOWN * 0.25 + LEFT * 1.2)

        term_group = VGroup(term_bg, term_bar, term_title)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "PIPELINE I/O", 
            "El ciclo interactivo alterna flujos de salida con esperas de entrada por teclado.", 
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

        # FASE 1: Emisión del Prompt
        hud_fase1 = self.create_hud_footer(
            "PROMPT DE SALIDA", 
            "std::cout imprime 'Nombre: ' sin salto de linea para mantener el cursor en la misma posicion.", 
            color=self.COLOR_CYAN
        )
        pointer1 = self.create_code_pointer(line1, color=self.COLOR_CYAN)

        self.play(
            FadeIn(pointer1, shift=RIGHT * 0.1),
            FadeIn(t_line1, shift=RIGHT * 0.2),
            ReplacementTransform(hud, hud_fase1),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 2: Captura del Input
        hud_fase2 = self.create_hud_footer(
            "CAPTURA DE ENTRADA", 
            "std::cin pausa la ejecucion hasta que el usuario teclea 'Link' y presiona Enter.", 
            color=self.COLOR_GOLD
        )
        pointer2 = self.create_code_pointer(line2, color=self.COLOR_GOLD)

        self.play(
            FadeOut(pointer1),
            FadeIn(pointer2, shift=RIGHT * 0.1),
            FadeIn(t_input, shift=DOWN * 0.1),
            Flash(t_input.get_center(), color=self.COLOR_GOLD, flash_radius=0.9, num_lines=10),
            ReplacementTransform(hud_fase1, hud_fase2),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 3: Emisión de Respuesta Formateada
        hud_fase3 = self.create_hud_footer(
            "RESPUESTA FORMATEADA", 
            "std::cout concatena el saludo con la variable y emite el resultado final con '\\n'.", 
            color=self.COLOR_GREEN
        )
        pointer3 = self.create_code_pointer(line3, color=self.COLOR_GREEN)

        self.play(
            FadeOut(pointer2),
            FadeIn(pointer3, shift=RIGHT * 0.1),
            FadeIn(t_line2, shift=UP * 0.1),
            Flash(t_line2.get_center(), color=self.COLOR_GREEN, flash_radius=1.2, num_lines=12),
            ReplacementTransform(hud_fase2, hud_fase3),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 4: Insignia y Síntesis Final
        insight_badge = self.create_badge("Ciclo de Entrada y Salida Sincronizado", width=5.8).move_to(UP * 2.2 + RIGHT * 3.4)
        hud_final = self.create_hud_footer(
            "FLUJO COMPLETO", 
            "La coordinacion de flujos I/O es la base de las aplicaciones de consola interactivas.", 
            color=self.COLOR_GREEN
        )

        self.play(
            FadeOut(pointer3),
            FadeIn(insight_badge, shift=DOWN * 0.15),
            ReplacementTransform(hud_fase3, hud_final),
            rate_func=smooth
        )
        # Pausa final obligatoria de 5.0s
        self.wait(5.0)

if __name__ == "__main__":
    export_manim_scenes(
        script_file=__file__,
        module_name="01_GettingStarted",
        scenes_dict={
            "IoPipeline": "l06_io_pipeline.gif",
        },
        gif_width=960,
        fps=18
    )
