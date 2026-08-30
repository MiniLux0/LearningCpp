from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene

class StaticCastScene(BaseLearningScene):
    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "Conversión Segura de Tipos (Casting)", 
            "Transformación explícita en tiempo de compilación con static_cast<T>()"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.5)

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (6.0 x 3.6)
        code_win, code_bg = self.create_code_window(width=6.0, height=3.6, title="casting.cpp")
        code_win.shift(LEFT * 3.3 + DOWN * 0.15)
        
        line1 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> suma{<span foreground="#fbbf24">15</span>};',
            font="Consolas", font_size=15, color="#f0f6fc"
        )
        line2 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> num{<span foreground="#fbbf24">2</span>};',
            font="Consolas", font_size=15, color="#f0f6fc"
        )
        line3 = MarkupText(
            '<span foreground="#10b981"><b>double</b></span> res{<span foreground="#c084fc"><b>static_cast</b></span>&lt;<span foreground="#10b981">double</span>&gt;(suma)',
            font="Consolas", font_size=14, color="#f0f6fc"
        )
        line4 = MarkupText(
            '             / num}; <span foreground="#10b981">// 7.5 (Exacto)</span>',
            font="Consolas", font_size=14, color="#f0f6fc"
        )

        code_lines = VGroup(line1, line2, line3, line4).arrange(DOWN, aligned_edge=LEFT, buff=0.20)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: TRANSFORMACIÓN DE TIPO EN MEMORIA
        panel_win, panel_bg = self.create_card_panel(
            width=5.8, height=3.6, 
            title="Transformación de Tipo", 
            subtitle="Reinterpretación Explícita de Bytes"
        )
        panel_win.shift(RIGHT * 3.3 + DOWN * 0.15)
        
        # Bloque original int (4 bytes)
        box_int = RoundedRectangle(
            width=5.2, height=0.65, corner_radius=0.08, 
            fill_color="#0f172a", fill_opacity=0.95, 
            stroke_color="#38bdf8", stroke_width=1.5
        )
        txt_int = Text("suma: [ 15 ] (int 4 Bytes)", font="Consolas", font_size=12, color="#7dd3fc", weight=BOLD).move_to(box_int.get_center())
        card_int = VGroup(box_int, txt_int).move_to(panel_bg.get_center() + UP * 0.55)

        # Bloque transformado double (8 bytes)
        box_dbl = RoundedRectangle(
            width=5.2, height=0.65, corner_radius=0.08, 
            fill_color="#0f172a", fill_opacity=0.98, 
            stroke_color="#10b981", stroke_width=2.0
        )
        txt_dbl = Text("static_cast: [ 15.0 ] (double 8 Bytes)", font="Consolas", font_size=11, color="#6ee7b7", weight=BOLD).move_to(box_dbl.get_center())
        card_dbl = VGroup(box_dbl, txt_dbl).move_to(panel_bg.get_center() + DOWN * 0.65)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "SISTEMA", 
            "Iniciando cálculo: Necesitamos calcular el promedio decimal (15 / 2 = 7.5).", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(code_win, shift=RIGHT * 0.2),
            FadeIn(code_lines, shift=RIGHT * 0.2),
            FadeIn(panel_win, shift=LEFT * 0.2),
            FadeIn(card_int, shift=LEFT * 0.2),
            FadeIn(hud, shift=UP * 0.2),
            rate_func=smooth
        )
        self.wait(1.5)

        # FASE 1: LECTURA DE VARIABLES ENTERAS
        hud_vars = self.create_hud_footer(
            "VARIABLES ENTERAS", 
            "suma{15} y num{2} son de tipo int. Una división directa truncaría a 7.", 
            color=self.COLOR_GOLD
        )
        pointer1 = self.create_code_pointer(line1, color=self.COLOR_CYAN)

        self.play(
            FadeIn(pointer1, shift=RIGHT * 0.1),
            ReplacementTransform(hud, hud_vars),
            rate_func=smooth
        )
        self.wait(2.5)

        # FASE 2: APLICACIÓN DE STATIC_CAST
        hud_cast = self.create_hud_footer(
            "STATIC_CAST", 
            "static_cast<double>(suma): Promueve explícitamente 15 a 15.0 para habilitar división decimal.", 
            color=self.COLOR_GREEN
        )
        pointer2 = self.create_code_pointer(line3, color=self.COLOR_GREEN)
        cast_arrow = Arrow(start=box_int.get_bottom(), end=box_dbl.get_top(), buff=0.10, color="#fbbf24", stroke_width=2.5)

        self.play(
            ReplacementTransform(pointer1, pointer2),
            GrowArrow(cast_arrow),
            FadeIn(card_dbl, shift=UP * 0.1),
            box_dbl.animate.set_stroke(color="#10b981", width=2.5),
            ReplacementTransform(hud_vars, hud_cast),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 3: SÍNTESIS FINAL
        hud_final = self.create_hud_footer(
            "CASTING MODERNO", 
            "Prohibido el casting clásico '(double)x'. Usa siempre static_cast<T>() en C++ Moderno.", 
            color=self.COLOR_GREEN
        )
        self.play(
            FadeOut(pointer2),
            ReplacementTransform(hud_cast, hud_final),
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
        "StaticCastScene": "l05_static_cast.gif",
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
