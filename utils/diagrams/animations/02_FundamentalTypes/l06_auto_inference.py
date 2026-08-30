from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene

class AutoInference(BaseLearningScene):
    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "Inferencia de Tipos (auto)", 
            "Deducción estática en tiempo de compilación según el literal inicializador"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.5)

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (6.0 x 3.6)
        code_win, code_bg = self.create_code_window(width=6.0, height=3.6, title="auto.cpp")
        code_win.shift(LEFT * 3.3 + DOWN * 0.15)
        
        line1 = MarkupText(
            '<span foreground="#c084fc"><b>auto</b></span> vidas{<span foreground="#fbbf24">3</span>};      <span foreground="#64748b">// Deduce int</span>',
            font="Consolas", font_size=15, color="#f0f6fc"
        )
        line2 = MarkupText(
            '<span foreground="#c084fc"><b>auto</b></span> precio{<span foreground="#fbbf24">19.99</span>}; <span foreground="#64748b">// Deduce double</span>',
            font="Consolas", font_size=15, color="#f0f6fc"
        )

        code_lines = VGroup(line1, line2).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: ANÁLISIS DEL COMPILADOR
        panel_win, panel_bg = self.create_card_panel(
            width=5.8, height=3.6, 
            title="Análisis del Compilador g++", 
            subtitle="Deducción Estática por Literal"
        )
        panel_win.shift(RIGHT * 3.3 + DOWN * 0.15)
        
        # Cajas deducidas
        box_int = RoundedRectangle(
            width=5.2, height=0.75, corner_radius=0.08, 
            fill_color="#0f172a", fill_opacity=0.95, 
            stroke_color="#38bdf8", stroke_width=1.8
        )
        txt_int = Text("vidas  -> tipo deducido: int (4 Bytes)", font="Consolas", font_size=11, color="#7dd3fc", weight=BOLD).move_to(box_int.get_center())
        card_int = VGroup(box_int, txt_int).move_to(panel_bg.get_center() + UP * 0.55)

        box_dbl = RoundedRectangle(
            width=5.2, height=0.75, corner_radius=0.08, 
            fill_color="#0f172a", fill_opacity=0.95, 
            stroke_color="#c084fc", stroke_width=1.8
        )
        txt_dbl = Text("precio -> tipo deducido: double (8 Bytes)", font="Consolas", font_size=11, color="#e9d5ff", weight=BOLD).move_to(box_dbl.get_center())
        card_dbl = VGroup(box_dbl, txt_dbl).move_to(panel_bg.get_center() + DOWN * 0.65)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "SISTEMA", 
            "Iniciando deducción de tipos con 'auto': Cero sobrecarga en tiempo de ejecución.", 
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

        # FASE 1: DEDUCCIÓN DE ENTERO
        hud_d1 = self.create_hud_footer(
            "DEDUCCIÓN INT", 
            "El literal '3' es un entero estándar: El compilador asigna tipo 'int' a vidas.", 
            color=self.COLOR_CYAN
        )
        pointer1 = self.create_code_pointer(line1, color=self.COLOR_CYAN)

        self.play(
            FadeIn(pointer1, shift=RIGHT * 0.1),
            FadeIn(card_int, shift=LEFT * 0.15),
            box_int.animate.set_stroke(color="#38bdf8", width=2.2),
            ReplacementTransform(hud, hud_d1),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 2: DEDUCCIÓN DE DOUBLE
        hud_d2 = self.create_hud_footer(
            "DEDUCCIÓN DOUBLE", 
            "El literal '19.99' contiene decimales: El compilador asigna tipo 'double' a precio.", 
            color=self.COLOR_PURPLE
        )
        pointer2 = self.create_code_pointer(line2, color=self.COLOR_PURPLE)

        self.play(
            ReplacementTransform(pointer1, pointer2),
            FadeIn(card_dbl, shift=LEFT * 0.15),
            box_dbl.animate.set_stroke(color="#c084fc", width=2.2),
            ReplacementTransform(hud_d1, hud_d2),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 3: SÍNTESIS FINAL
        hud_final = self.create_hud_footer(
            "AUTO EN C++", 
            "El tipado sigue siendo 100% estático y estricto. 'auto' solo ahorra escritura repetitiva.", 
            color=self.COLOR_GREEN
        )
        self.play(
            FadeOut(pointer2),
            ReplacementTransform(hud_d2, hud_final),
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
        "AutoInference": "l06_auto_inference.gif",
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
