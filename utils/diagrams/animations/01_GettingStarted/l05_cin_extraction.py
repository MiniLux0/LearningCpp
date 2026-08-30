from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene, export_manim_scenes

class CinExtraction(BaseLearningScene):
    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "Entrada de Datos (std::cin)", 
            "Extracción de valores tipados desde el flujo hacia la memoria RAM"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.3)

        Y_MAIN = 0.2

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (5.4 x 3.0)
        win_group, code_bg = self.create_code_window(width=5.4, height=3.0, title="main.cpp")
        win_group.move_to(LEFT * 3.4 + UP * Y_MAIN)

        line1 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> '
            '<span foreground="#fbbf24">edad</span>{<span foreground="#38bdf8">0</span>};',
            font="Consolas", font_size=15
        )
        line2 = MarkupText(
            '<span foreground="#38bdf8">std::cin</span> &gt;&gt; '
            '<span foreground="#fbbf24">edad</span>;',
            font="Consolas", font_size=15
        )

        line1.move_to(ORIGIN)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.35)

        code_lines = VGroup(line1, line2)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: MEMORIA RAM EN STACK (5.4 x 3.0)
        ram_card, ram_bg = self.create_card_panel(
            width=5.4, height=3.0, 
            title="Memoria RAM (Stack)", 
            subtitle="Dirección Física: 0x7FFEE8"
        )
        ram_card.move_to(RIGHT * 3.4 + UP * Y_MAIN)

        cell_inner = RoundedRectangle(
            width=4.2, height=1.1, corner_radius=0.12,
            fill_color="#0b0f19", fill_opacity=0.98,
            stroke_color=self.COLOR_CYAN, stroke_width=1.8
        ).move_to(ram_bg.get_center() + DOWN * 0.40)

        var_tag = Text("edad (int · 4 Bytes)", font="Consolas", font_size=13, color=self.COLOR_CYAN_LIGHT, weight=BOLD).next_to(cell_inner.get_top(), UP, buff=0.08)
        val_text = Text("0", font="Consolas", font_size=32, color="#8b949e", weight=BOLD).move_to(cell_inner.get_center())

        ram_full = VGroup(ram_card, cell_inner, var_tag, val_text)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "STACK RAM", 
            "La variable 'edad' reserva 4 bytes contiguos en la pila de memoria.", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(win_group, shift=RIGHT * 0.2),
            FadeIn(code_lines, shift=RIGHT * 0.2),
            FadeIn(ram_full, shift=LEFT * 0.2),
            FadeIn(hud, shift=UP * 0.2),
            rate_func=smooth, run_time=0.6
        )
        self.wait(1.5)

        # FASE 1: Declaración e Inicialización Uniforme
        hud_fase1 = self.create_hud_footer(
            "INICIALIZACION", 
            "int edad{0} inicializa la celda a 0, evitando lecturas de basura residual en RAM.", 
            color=self.COLOR_CYAN
        )
        pointer1 = self.create_code_pointer(line1, color=self.COLOR_CYAN)

        self.play(
            FadeIn(pointer1, shift=RIGHT * 0.1),
            Flash(cell_inner.get_center(), color=self.COLOR_CYAN, flash_radius=1.1, num_lines=10),
            ReplacementTransform(hud, hud_fase1),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 2: Extracción con std::cin >> edad
        hud_fase2 = self.create_hud_footer(
            "EXTRACCION (>>)", 
            "std::cin lee caracteres del buffer del teclado, los convierte a entero y los inyecta en RAM.", 
            color=self.COLOR_GREEN
        )
        pointer2 = self.create_code_pointer(line2, color=self.COLOR_GREEN)

        input_packet = VGroup(
            RoundedRectangle(width=2.4, height=0.65, corner_radius=0.08, fill_color="#064e3b", fill_opacity=0.98, stroke_color=self.COLOR_GREEN, stroke_width=1.8),
            Text(">> 25", font="Consolas", font_size=15, color="#6ee7b7", weight=BOLD)
        ).move_to(line2.get_center())

        arrow_flow = Arrow(start=code_bg.get_right(), end=cell_inner.get_left(), buff=0.15, color=self.COLOR_GREEN, stroke_width=3.5)

        self.play(
            FadeOut(pointer1),
            FadeIn(pointer2, shift=RIGHT * 0.1),
            FadeIn(input_packet),
            GrowArrow(arrow_flow),
            ReplacementTransform(hud_fase1, hud_fase2),
            rate_func=smooth
        )
        self.play(
            input_packet.animate.move_to(cell_inner.get_center()),
            rate_func=smooth, run_time=0.7
        )

        val_updated = Text("25", font="Consolas", font_size=34, color="#ffffff", weight=BOLD).move_to(cell_inner.get_center())

        self.play(
            ReplacementTransform(input_packet, val_updated),
            FadeOut(val_text),
            FadeOut(arrow_flow),
            cell_inner.animate.set_stroke(color=self.COLOR_GREEN, width=2.2),
            Flash(cell_inner.get_center(), color=self.COLOR_GREEN, flash_radius=1.2, num_lines=12),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 3: Insignia y Síntesis Final
        insight_badge = self.create_badge("Escritura Directa en Memoria Stack", width=5.8).move_to(UP * 2.2 + RIGHT * 3.4)
        hud_final = self.create_hud_footer(
            "ESTADO SINCRONIZADO", 
            "La celda de memoria 0x7FFEE8 ahora contiene el valor 25 validado por tipo.", 
            color=self.COLOR_GREEN
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
            "CinExtraction": "l05_cin_extraction.gif",
        },
        gif_width=960,
        fps=18
    )
