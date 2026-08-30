from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene

class L02ElseIf(BaseLearningScene):
    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "Cascadas de Condiciones (else if)", 
            "Evaluación secuencial de arriba a abajo y salto en cortocircuito"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.5)

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (6.0 x 3.6)
        code_win, code_bg = self.create_code_window(width=6.0, height=3.6, title="calificaciones.cpp")
        code_win.shift(LEFT * 3.3 + DOWN * 0.15)
        
        line1 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> nota{<span foreground="#fbbf24">85</span>};',
            font="Consolas", font_size=16, color="#f0f6fc"
        )
        line2 = MarkupText(
            '<span foreground="#c084fc"><b>if</b></span> (nota &gt;= <span foreground="#fbbf24">90</span>) <span foreground="#c084fc">{</span>',
            font="Consolas", font_size=16
        )
        line3 = MarkupText(
            '<span foreground="#c084fc"><b>return</b></span> <span foreground="#f59e0b">\'A\'</span>;',
            font="Consolas", font_size=16, color="#64748b"
        )
        line4 = MarkupText(
            '<span foreground="#c084fc">} <b>else if</b></span> (nota &gt;= <span foreground="#fbbf24">80</span>) <span foreground="#c084fc">{</span>',
            font="Consolas", font_size=16
        )
        line5 = MarkupText(
            '<span foreground="#c084fc"><b>return</b></span> <span foreground="#10b981">\'B\'</span>; <span foreground="#10b981">// Se ejecuta</span>',
            font="Consolas", font_size=16, color="#f0f6fc"
        )
        line6 = MarkupText(
            '<span foreground="#c084fc">} <b>else</b> {</span> <span foreground="#c084fc"><b>return</b></span> <span foreground="#64748b">\'F\'</span>; <span foreground="#c084fc">}</span>',
            font="Consolas", font_size=15, color="#64748b"
        )
        
        INDENT = 0.45
        line1.move_to(ORIGIN)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.16)
        line3.next_to(line2, DOWN, aligned_edge=LEFT, buff=0.16).shift(RIGHT * INDENT)
        line4.next_to(line3, DOWN, aligned_edge=LEFT, buff=0.16).shift(LEFT * INDENT)
        line5.next_to(line4, DOWN, aligned_edge=LEFT, buff=0.16).shift(RIGHT * INDENT)
        line6.next_to(line5, DOWN, aligned_edge=LEFT, buff=0.16).shift(LEFT * INDENT)

        code_lines = VGroup(line1, line2, line3, line4, line5, line6)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: CASCADA DE EVALUACIÓN
        panel_win, panel_bg = self.create_card_panel(
            width=5.8, height=3.6, 
            title="Cascada de Evaluación", 
            subtitle="Filtro Secuencial de Condiciones"
        )
        panel_win.shift(RIGHT * 3.3 + DOWN * 0.15)
        
        # Filtro 1 (Falla)
        cond1 = RoundedRectangle(
            width=5.2, height=0.60, corner_radius=0.08, 
            fill_color="#0f172a", fill_opacity=0.95, 
            stroke_color="#ef4444", stroke_width=1.5
        )
        t_c1 = Text("1. (85 >= 90) -> false (Fallo, continua)", font="Consolas", font_size=11, color="#fca5a5", weight=BOLD).move_to(cond1.get_center())
        card1 = VGroup(cond1, t_c1)

        # Filtro 2 (Match)
        cond2 = RoundedRectangle(
            width=5.2, height=0.60, corner_radius=0.08, 
            fill_color="#0f172a", fill_opacity=0.95, 
            stroke_color="#10b981", stroke_width=2.0
        )
        t_c2 = Text("2. (85 >= 80) -> true (MATCH -> 'B')", font="Consolas", font_size=11, color="#6ee7b7", weight=BOLD).move_to(cond2.get_center())
        card2 = VGroup(cond2, t_c2)

        # Filtro 3 (Skip)
        cond3 = RoundedRectangle(
            width=5.2, height=0.60, corner_radius=0.08, 
            fill_color="#0f172a", fill_opacity=0.5, 
            stroke_color="#475569", stroke_width=1.2
        )
        t_c3 = Text("3. else -> OMITIDO (Cortocircuito)", font="Consolas", font_size=11, color="#94a3b8").move_to(cond3.get_center())
        card3 = VGroup(cond3, t_c3)

        cards = VGroup(card1, card2, card3).arrange(DOWN, buff=0.22)
        cards.move_to(panel_bg.get_center() + DOWN * 0.15)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "SISTEMA", 
            "Iniciando evaluación en cascada para la variable 'nota{85}'.", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(code_win, shift=RIGHT * 0.2),
            FadeIn(code_lines, shift=RIGHT * 0.2),
            FadeIn(panel_win, shift=LEFT * 0.2),
            FadeIn(card1, shift=LEFT * 0.2),
            FadeIn(hud, shift=UP * 0.2),
            rate_func=smooth
        )
        self.wait(1.5)

        # FASE 1: PRIMER FILTRO (FALLA)
        hud_step1 = self.create_hud_footer(
            "FILTRO 1", 
            "if (nota >= 90): (85 >= 90) evalúa a 'false'. La CPU pasa al siguiente 'else if'.", 
            color=self.COLOR_RED
        )
        pointer1 = self.create_code_pointer(line2, color=self.COLOR_RED)

        self.play(
            FadeIn(pointer1, shift=RIGHT * 0.1),
            cond1.animate.set_stroke(color="#ef4444", width=2.2),
            ReplacementTransform(hud, hud_step1),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 2: SEGUNDO FILTRO (MATCH)
        hud_step2 = self.create_hud_footer(
            "FILTRO 2 (MATCH)", 
            "else if (nota >= 80): (85 >= 80) evalúa a 'true'. Se ejecuta el retorno de 'B'.", 
            color=self.COLOR_GREEN
        )
        pointer2 = self.create_code_pointer(line4, color=self.COLOR_GREEN)
        pointer_ret = self.create_code_pointer(line5, color=self.COLOR_GREEN)

        self.play(
            ReplacementTransform(pointer1, pointer2),
            FadeIn(card2, shift=DOWN * 0.1),
            ReplacementTransform(hud_step1, hud_step2),
            rate_func=smooth
        )
        self.wait(1.0)
        self.play(
            ReplacementTransform(pointer2, pointer_ret),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 3: CORTOCIRCUITO (OMISIÓN DEL RESTO)
        hud_step3 = self.create_hud_footer(
            "CORTOCIRCUITO", 
            "Al encontrar un match verdadero, se omite todo el resto de la cadena condicional.", 
            color=self.COLOR_CYAN
        )
        self.play(
            FadeIn(card3, shift=DOWN * 0.1),
            ReplacementTransform(hud_step2, hud_step3),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 4: SÍNTESIS FINAL
        hud_final = self.create_hud_footer(
            "ELSE-IF CASCADA", 
            "Evaluación de arriba a abajo: La primera condición verdadera detiene el escaneo.", 
            color=self.COLOR_GREEN
        )
        self.play(
            FadeOut(pointer_ret),
            ReplacementTransform(hud_step3, hud_final),
            rate_func=smooth
        )
        
        # Pausa final extendida de 5.0s para asimilación completa antes de loop
        self.wait(5.0)

if __name__ == "__main__":
    import shutil
    import subprocess
    import glob
    GIF_WIDTH = 720
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    MODULE_NAME = os.path.basename(SCRIPT_DIR)
    REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR))))
    out_dir = os.path.join(REPO_ROOT, MODULE_NAME, "theory", "assets")
    os.makedirs(out_dir, exist_ok=True)
    script_path = os.path.abspath(__file__)

    scenes = {
        "L02ElseIf": "l02_else_if_cascade.gif",
    }

    for scene_name, final_gif_name in scenes.items():
        command = f'python -m manim -qm --disable_caching --media_dir "{out_dir}" "{script_path}" {scene_name}'
        print(f"Executing: {command}")
        result = subprocess.run(command, shell=True)
        if result.returncode != 0:
            print(f"ERROR: Manim falló para '{scene_name}'.")
            continue

        matches = glob.glob(os.path.join(out_dir, "videos", "**", f"{scene_name}*.mp4"), recursive=True)
        if matches:
            mp4_path = matches[0]
            final_gif_path = os.path.join(out_dir, final_gif_name)
            ffmpeg_cmd = [
                "ffmpeg", "-y", "-i", mp4_path,
                "-vf", f"fps=15,scale={GIF_WIDTH}:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse",
                final_gif_path,
            ]
            print(f"Generating optimized GIF: {final_gif_path}")
            subprocess.run(ffmpeg_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"GIF generated successfully: {final_gif_path}")

    for folder in ["videos", "images", "texts", "Tex"]:
        cache_dir = os.path.join(out_dir, folder)
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir, ignore_errors=True)
