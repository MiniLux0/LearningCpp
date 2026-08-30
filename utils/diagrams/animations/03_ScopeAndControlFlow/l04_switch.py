from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene

class L04SwitchFallthrough(BaseLearningScene):
    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "Sentencia switch y Fallthrough", 
            "Tabla de saltos de la CPU y la importancia crítica de 'break'"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.5)

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (6.0 x 3.6)
        code_win, code_bg = self.create_code_window(width=6.0, height=3.6, title="menu.cpp")
        code_win.shift(LEFT * 3.3 + DOWN * 0.15)
        
        line1 = MarkupText(
            '<span foreground="#c084fc"><b>switch</b></span> (opcion) <span foreground="#c084fc">{</span>',
            font="Consolas", font_size=16
        )
        line2 = MarkupText(
            '<span foreground="#c084fc"><b>case</b></span> <span foreground="#fbbf24">1</span>: <span foreground="#38bdf8">play</span>(); <span foreground="#c084fc"><b>break</b></span>;',
            font="Consolas", font_size=15, color="#64748b"
        )
        line3 = MarkupText(
            '<span foreground="#c084fc"><b>case</b></span> <span foreground="#fbbf24">2</span>: <span foreground="#38bdf8">pause</span>(); <span foreground="#ef4444">// Sin break!</span>',
            font="Consolas", font_size=15, color="#f0f6fc"
        )
        line4 = MarkupText(
            '<span foreground="#c084fc"><b>case</b></span> <span foreground="#fbbf24">3</span>: <span foreground="#38bdf8">stop</span>(); <span foreground="#ef4444">// Ejecutado!</span>',
            font="Consolas", font_size=15, color="#f87171"
        )
        line5 = MarkupText(
            '<span foreground="#c084fc"><b>default</b>: <b>break</b></span>;',
            font="Consolas", font_size=15, color="#64748b"
        )
        line6 = MarkupText(
            '<span foreground="#c084fc">}</span>',
            font="Consolas", font_size=16
        )
        
        INDENT = 0.45
        line1.move_to(ORIGIN)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.16).shift(RIGHT * INDENT)
        line3.next_to(line2, DOWN, aligned_edge=LEFT, buff=0.16)
        line4.next_to(line3, DOWN, aligned_edge=LEFT, buff=0.16)
        line5.next_to(line4, DOWN, aligned_edge=LEFT, buff=0.16)
        line6.next_to(line5, DOWN, aligned_edge=LEFT, buff=0.16).shift(LEFT * INDENT)

        code_lines = VGroup(line1, line2, line3, line4, line5, line6)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: TABLA DE SALTOS (JUMP TABLE)
        panel_win, panel_bg = self.create_card_panel(
            width=5.8, height=3.6, 
            title="Tabla de Saltos (CPU)", 
            subtitle="Desborde Secuencial por Falta de break"
        )
        panel_win.shift(RIGHT * 3.3 + DOWN * 0.15)
        
        # Case 2 Match
        c2_box = RoundedRectangle(
            width=5.2, height=0.65, corner_radius=0.08, 
            fill_color="#0f172a", fill_opacity=0.95, 
            stroke_color="#38bdf8", stroke_width=1.8
        )
        t_c2 = Text("Salto Directo -> case 2: pause()", font="Consolas", font_size=12, color="#7dd3fc", weight=BOLD).move_to(c2_box.get_center())
        card2 = VGroup(c2_box, t_c2)

        # Case 3 Fallthrough
        c3_box = RoundedRectangle(
            width=5.2, height=0.65, corner_radius=0.08, 
            fill_color="#180a0a", fill_opacity=0.95, 
            stroke_color="#ef4444", stroke_width=1.8
        )
        t_c3 = Text("FALLTHROUGH -> case 3: stop() (Error)", font="Consolas", font_size=11, color="#fca5a5", weight=BOLD).move_to(c3_box.get_center())
        card3 = VGroup(c3_box, t_c3)

        cards = VGroup(card2, card3).arrange(DOWN, buff=0.45)
        cards.move_to(panel_bg.get_center() + DOWN * 0.15)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "SISTEMA", 
            "Evaluando switch(opcion) con valor opcion = 2.", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(code_win, shift=RIGHT * 0.2),
            FadeIn(code_lines, shift=RIGHT * 0.2),
            FadeIn(panel_win, shift=LEFT * 0.2),
            FadeIn(card2, shift=LEFT * 0.2),
            FadeIn(hud, shift=UP * 0.2),
            rate_func=smooth
        )
        self.wait(1.5)

        # FASE 1: SALTO DIRECTO A CASE 2
        hud_jump = self.create_hud_footer(
            "JUMP TABLE", 
            "La CPU salta instantáneamente a la etiqueta 'case 2' y ejecuta 'pause()'.", 
            color=self.COLOR_CYAN
        )
        pointer2 = self.create_code_pointer(line3, color=self.COLOR_CYAN)

        self.play(
            FadeIn(pointer2, shift=RIGHT * 0.1),
            c2_box.animate.set_stroke(color="#38bdf8", width=2.2),
            ReplacementTransform(hud, hud_jump),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 2: CAÍDA EN CASCADA (FALLTHROUGH)
        hud_fall = self.create_hud_footer(
            "FALLTHROUGH", 
            "¡Al omitir 'break', la CPU no se detiene y cae directamente a ejecutar 'case 3'!", 
            color=self.COLOR_RED
        )
        pointer3 = self.create_code_pointer(line4, color=self.COLOR_RED)
        fall_arrow = Arrow(start=c2_box.get_bottom(), end=c3_box.get_top(), buff=0.08, color="#ef4444", stroke_width=2.5)

        self.play(
            ReplacementTransform(pointer2, pointer3),
            GrowArrow(fall_arrow),
            FadeIn(card3, shift=DOWN * 0.1),
            ReplacementTransform(hud_jump, hud_fall),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 3: SÍNTESIS FINAL
        hud_final = self.create_hud_footer(
            "REGLA DE ORO", 
            "Siempre finaliza cada case con 'break' para evitar ejecuciones accidentales.", 
            color=self.COLOR_GREEN
        )
        self.play(
            FadeOut(pointer3),
            ReplacementTransform(hud_fall, hud_final),
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
        "L04SwitchFallthrough": "l04_switch_fallthrough.gif",
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
