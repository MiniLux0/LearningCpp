from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene

class FunctionAnatomyScene(BaseLearningScene):
    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "Anatomía de una Función", 
            "Componentes de la firma y arquitectura modular en C++"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.3)

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (Editor Realista con Indentación)
        code_win, code_bg = self.create_code_window(width=6.0, height=3.6, title="matematica.cpp")
        code_win.shift(LEFT * 3.3 + DOWN * 0.15)
        
        # Líneas de código con sintaxis hiper-realista tipo VS Code con proporción dorada (20pt)
        line1 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> '
            '<span foreground="#38bdf8"><b>sumar</b></span>'
            '(<span foreground="#10b981">int</span> <span foreground="#fbbf24">a</span>, '
            '<span foreground="#10b981">int</span> <span foreground="#fbbf24">b</span>) '
            '<span foreground="#c084fc">{</span>',
            font="Consolas", font_size=20
        )
        line2 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> resultado{<span foreground="#fbbf24">a</span> + <span foreground="#fbbf24">b</span>};',
            font="Consolas", font_size=20, color="#f0f6fc"
        )
        line3 = MarkupText(
            '<span foreground="#c084fc"><b>return</b></span> resultado;',
            font="Consolas", font_size=20, color="#f0f6fc"
        )
        line4 = MarkupText(
            '<span foreground="#c084fc">}</span>',
            font="Consolas", font_size=20
        )
        
        # Posicionamiento con indentación real de 4 espacios (tab) y espaciado armónico
        INDENT = 0.52
        line1.move_to(ORIGIN)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.30).shift(RIGHT * INDENT)
        line3.next_to(line2, DOWN, aligned_edge=LEFT, buff=0.30)
        line4.next_to(line3, DOWN, aligned_edge=LEFT, buff=0.30).shift(LEFT * INDENT)

        code_lines = VGroup(line1, line2, line3, line4)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.12)

        # 3. PANEL DERECHO: DESGLOSE ESTRUCTURAL
        panel_win, panel_bg = self.create_card_panel(
            width=5.8, height=3.6, 
            title="Desglose de la Firma", 
            subtitle="Auditoría de Componentes"
        )
        panel_win.shift(RIGHT * 3.3 + DOWN * 0.15)
        
        badge_ret = self.create_badge(
            "1. Retorno [int] -> Output de datos", 
            fill_color="#064e3b", stroke_color="#10b981", text_color="#6ee7b7", 
            width=5.2, height=0.46
        )
        badge_name = self.create_badge(
            "2. Nombre [sumar] -> Identificador unico", 
            fill_color="#0c2d48", stroke_color="#38bdf8", text_color="#7dd3fc", 
            width=5.2, height=0.46
        )
        badge_params = self.create_badge(
            "3. Parametros [(a, b)] -> Canales de entrada", 
            fill_color="#3d2c00", stroke_color="#f59e0b", text_color="#fbbf24", 
            width=5.2, height=0.46
        )
        badge_scope = self.create_badge(
            "4. Cuerpo [{ ... }] -> Scope y aislamiento RAM", 
            fill_color="#2e1065", stroke_color="#c084fc", text_color="#e9d5ff", 
            width=5.2, height=0.46
        )
        
        badges = VGroup(badge_ret, badge_name, badge_params, badge_scope).arrange(DOWN, buff=0.14)
        badges.move_to(panel_bg.get_center() + DOWN * 0.22)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "SISTEMA", 
            "Analizando la firma contractual y componentes de la función.", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(code_win, shift=RIGHT * 0.2),
            FadeIn(code_lines, shift=RIGHT * 0.2),
            FadeIn(panel_win, shift=LEFT * 0.2),
            FadeIn(hud, shift=UP * 0.2),
            rate_func=smooth
        )
        self.wait(1.5)

        # FASE 1: TIPO DE RETORNO (int)
        hud_ret = self.create_hud_footer(
            "TIPO DE RETORNO", 
            "Garantiza el tipo estricto del valor inyectado hacia el llamador.", 
            color=self.COLOR_GREEN
        )
        box_ret = SurroundingRectangle(
            line1[0:3], color=self.COLOR_GREEN, 
            fill_color=self.COLOR_GREEN, fill_opacity=0.22, 
            corner_radius=0.06, stroke_width=2.0, buff=0.06
        )

        self.play(
            FadeIn(box_ret),
            FadeIn(badge_ret, shift=RIGHT * 0.2),
            ReplacementTransform(hud, hud_ret),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 2: IDENTIFICADOR (sumar)
        hud_name = self.create_hud_footer(
            "IDENTIFICADOR", 
            "Nombre único para invocar y transferir el flujo a la rutina.", 
            color=self.COLOR_CYAN
        )
        box_name = SurroundingRectangle(
            line1[3:8], color=self.COLOR_CYAN, 
            fill_color=self.COLOR_CYAN, fill_opacity=0.22, 
            corner_radius=0.06, stroke_width=2.0, buff=0.06
        )

        self.play(
            FadeOut(box_ret),
            FadeIn(box_name),
            FadeIn(badge_name, shift=RIGHT * 0.2),
            ReplacementTransform(hud_ret, hud_name),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 3: PARÁMETROS ((int a, int b))
        hud_params = self.create_hud_footer(
            "PARÁMETROS", 
            "Variables locales que reciben los inputs clonados por Pass-by-value.", 
            color=self.COLOR_GOLD
        )
        box_params = SurroundingRectangle(
            line1[8:19], color=self.COLOR_GOLD, 
            fill_color=self.COLOR_GOLD, fill_opacity=0.22, 
            corner_radius=0.06, stroke_width=2.0, buff=0.06
        )

        self.play(
            FadeOut(box_name),
            FadeIn(box_params),
            FadeIn(badge_params, shift=RIGHT * 0.2),
            ReplacementTransform(hud_name, hud_params),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 4: SCOPE LOCAL Y CUERPO ({ ... })
        hud_scope = self.create_hud_footer(
            "SCOPE LOCAL", 
            "Delimita el ciclo de vida en RAM; las variables se destruyen al salir de '}'.", 
            color=self.COLOR_PURPLE
        )
        box_scope = SurroundingRectangle(
            code_lines, color=self.COLOR_PURPLE, 
            fill_color=self.COLOR_PURPLE, fill_opacity=0.14, 
            corner_radius=0.12, stroke_width=2.0, buff=0.15
        )

        self.play(
            FadeOut(box_params),
            FadeIn(box_scope),
            FadeIn(badge_scope, shift=RIGHT * 0.2),
            ReplacementTransform(hud_params, hud_scope),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 5: SÍNTESIS FINAL Y RETENCIÓN
        hud_final = self.create_hud_footer(
            "CONTRATO C++", 
            "Firma validada: Los 4 pilares operan en perfecta modularidad y aislamiento.", 
            color=self.COLOR_GREEN
        )
        self.play(
            FadeOut(box_scope),
            ReplacementTransform(hud_scope, hud_final),
            rate_func=smooth
        )
        
        # Pausa final extendida de 5.0s para lectura cómoda
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
        "FunctionAnatomyScene": "l01_anatomy_of_a_function.gif",
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
