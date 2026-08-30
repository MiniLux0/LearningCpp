from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene

class NarrowingConversion(BaseLearningScene):
    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "Inicialización Uniforme {}", 
            "Prevención de Narrowing Conversion (Pérdida Silenciosa de Precisión)"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.5)

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (6.0 x 3.6)
        code_win, code_bg = self.create_code_window(width=6.0, height=3.6, title="narrowing.cpp")
        code_win.shift(LEFT * 3.3 + DOWN * 0.15)
        
        line1 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> a = <span foreground="#ef4444">3.99</span>; <span foreground="#64748b">// Trunca a 3 (C-style)</span>',
            font="Consolas", font_size=15, color="#f0f6fc"
        )
        line2 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> b{<span foreground="#f59e0b">3.99</span>};  <span foreground="#ef4444">// ERROR g++ (Moderno)</span>',
            font="Consolas", font_size=15, color="#f0f6fc"
        )

        code_lines = VGroup(line1, line2).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: INTERCEPCIÓN DEL COMPILADOR
        panel_win, panel_bg = self.create_card_panel(
            width=5.8, height=3.6, 
            title="Compilador g++ vs Stack RAM", 
            subtitle="Validación de Tipos en Compile-Time"
        )
        panel_win.shift(RIGHT * 3.3 + DOWN * 0.15)
        
        # Celda RAM objetivo
        cell_int = RoundedRectangle(
            width=5.2, height=1.0, corner_radius=0.1,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color="#38bdf8", stroke_width=1.5
        ).move_to(panel_bg.get_center() + UP * 0.55)
        
        int_title = Text("Variable 'b': int (Solo Enteros de 4 Bytes)", font="Consolas", font_size=11, color="#7dd3fc", weight=BOLD)
        int_title.next_to(cell_int.get_top(), DOWN, buff=0.12)
        int_val = Text("[ ? ] Esperando dato entero...", font="Consolas", font_size=12, color="#64748b")
        int_val.next_to(int_title, DOWN, buff=0.10)
        ram_target = VGroup(cell_int, int_title, int_val)

        # Tarjeta de Diagnóstico Estructurada de Alto Contraste
        diag_box = RoundedRectangle(
            width=5.2, height=1.35, corner_radius=0.1, 
            fill_color="#180a0a", fill_opacity=0.98, 
            stroke_color="#ef4444", stroke_width=1.5
        ).move_to(panel_bg.get_center() + DOWN * 0.70)
        
        diag_title = Text("ERROR: Narrowing Conversion", font="Consolas", font_size=12, color="#ef4444", weight=BOLD)
        diag_code = Text("int b{3.99};", font="Consolas", font_size=13, color="#f8fafc", weight=BOLD)
        diag_caret = Text("     ^^^^", font="Consolas", font_size=12, color="#f87171", weight=BOLD)
        diag_reason = Text("g++ bloquea la pérdida del decimal (.99)", font="Consolas", font_size=11, color="#fbbf24", weight=BOLD)

        diag_content = VGroup(diag_title, diag_code, diag_caret, diag_reason).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        diag_content.move_to(diag_box.get_center())
        diag_card = VGroup(diag_box, diag_content)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "SISTEMA", 
            "Evaluando asignación con '=' clásica vs Inicialización Uniforme con '{}'.", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(code_win, shift=RIGHT * 0.2),
            FadeIn(code_lines, shift=RIGHT * 0.2),
            FadeIn(panel_win, shift=LEFT * 0.2),
            FadeIn(ram_target, shift=LEFT * 0.2),
            FadeIn(hud, shift=UP * 0.2),
            rate_func=smooth
        )
        self.wait(1.5)

        # FASE 1: PELIGRO DEL C-STYLE CAST '='
        hud_cstyle = self.create_hud_footer(
            "C-STYLE TRUNCATE", 
            "int a = 3.99: El compilador trunca silenciosamente a 3, perdiendo .99 sin avisar.", 
            color=self.COLOR_RED
        )
        pointer1 = self.create_code_pointer(line1, color=self.COLOR_RED)

        self.play(
            FadeIn(pointer1, shift=RIGHT * 0.1),
            ReplacementTransform(hud, hud_cstyle),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 2: BLOQUEO MODERNO CON BRACES {}
        hud_braces = self.create_hud_footer(
            "PROTECCIÓN {}", 
            "int b{3.99}: Las llaves activan Narrowing Check y detienen la compilación con error.", 
            color=self.COLOR_GOLD
        )
        pointer2 = self.create_code_pointer(line2, color=self.COLOR_GOLD)

        # Proyectil decimal intentando penetrar
        proj_double = VGroup(
            RoundedRectangle(width=1.8, height=0.45, corner_radius=0.08, fill_color="#3d2c00", fill_opacity=0.95, stroke_color="#f59e0b", stroke_width=1.8),
            Text("3.99 (double)", font="Consolas", font_size=11, color="#fbbf24", weight=BOLD)
        ).move_to(LEFT * 0.5 + UP * 0.4)

        self.play(
            ReplacementTransform(pointer1, pointer2),
            ReplacementTransform(hud_cstyle, hud_braces),
            FadeIn(proj_double),
            rate_func=smooth
        )
        self.play(
            proj_double.animate.move_to(cell_int.get_left() + LEFT * 0.3),
            rate_func=rush_into,
            run_time=0.6
        )
        # Rebote en espacio neutral central
        self.play(
            proj_double.animate.move_to(LEFT * 0.5 + DOWN * 0.5).set_opacity(0),
            cell_int.animate.set_stroke(color="#ef4444", width=2.5),
            FadeIn(diag_card, shift=UP * 0.1),
            rate_func=smooth,
            run_time=0.8
        )
        self.wait(3.0)

        # FASE 3: SÍNTESIS FINAL
        hud_final = self.create_hud_footer(
            "REGLA DE ORO", 
            "Usa siempre llaves {} para inicializar: Protege tu software contra pérdida de datos.", 
            color=self.COLOR_GREEN
        )
        self.play(
            FadeOut(pointer2),
            ReplacementTransform(hud_braces, hud_final),
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
        "NarrowingConversion": "l02_narrowing_conversion.gif",
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
