from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene

class L07BreakContinue(BaseLearningScene):
    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "Sentencias break y continue", 
            "Interrupción y salto de iteraciones en bucles"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.5)

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (6.0 x 3.6)
        code_win, code_bg = self.create_code_window(width=6.0, height=3.6, title="control.cpp")
        code_win.shift(LEFT * 3.3 + DOWN * 0.15)
        
        line1 = MarkupText(
            '<span foreground="#c084fc"><b>for</b></span> '
            '(<span foreground="#10b981">int</span> i{<span foreground="#fbbf24">0</span>}; '
            'i &lt; <span foreground="#fbbf24">5</span>; '
            '<span foreground="#10b981">++i</span>) <span foreground="#c084fc">{</span>',
            font="Consolas", font_size=15
        )
        line2 = MarkupText(
            '<span foreground="#c084fc"><b>if</b></span> (i == <span foreground="#fbbf24">2</span>) <span foreground="#fbbf24"><b>continue</b></span>; <span foreground="#64748b">// Salta a ++i</span>',
            font="Consolas", font_size=14, color="#f0f6fc"
        )
        line3 = MarkupText(
            '<span foreground="#c084fc"><b>if</b></span> (i == <span foreground="#fbbf24">4</span>) <span foreground="#ef4444"><b>break</b></span>;    <span foreground="#64748b">// Rompe bucle</span>',
            font="Consolas", font_size=14, color="#f0f6fc"
        )
        line4 = MarkupText(
            'std::cout &lt;&lt; i &lt;&lt; <span foreground="#10b981">\'\\n\'</span>;',
            font="Consolas", font_size=15, color="#f0f6fc"
        )
        line5 = MarkupText(
            '<span foreground="#c084fc">}</span>',
            font="Consolas", font_size=15
        )
        line6 = MarkupText(
            '<span foreground="#64748b">// Fuera del bucle</span>',
            font="Consolas", font_size=14, color="#64748b"
        )
        
        INDENT = 0.45
        line1.move_to(ORIGIN)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.16).shift(RIGHT * INDENT)
        line3.next_to(line2, DOWN, aligned_edge=LEFT, buff=0.16)
        line4.next_to(line3, DOWN, aligned_edge=LEFT, buff=0.16)
        line5.next_to(line4, DOWN, aligned_edge=LEFT, buff=0.16).shift(LEFT * INDENT)
        line6.next_to(line5, DOWN, aligned_edge=LEFT, buff=0.16)

        code_lines = VGroup(line1, line2, line3, line4, line5, line6)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: TARJETAS DE REDIRECCIÓN DE FLUJO
        panel_win, panel_bg = self.create_card_panel(
            width=5.8, height=3.6, 
            title="Redirección de Flujo", 
            subtitle="Comportamiento en Hardware CPU"
        )
        panel_win.shift(RIGHT * 3.3 + DOWN * 0.15)
        
        box_cont = RoundedRectangle(
            width=5.2, height=0.75, corner_radius=0.08, 
            fill_color="#0f172a", fill_opacity=0.95, 
            stroke_color="#fbbf24", stroke_width=1.5
        )
        t_cont_title = Text("SENTENCIA CONTINUE:", font="Consolas", font_size=11, color="#fbbf24", weight=BOLD)
        t_cont_desc = Text("Salta directo a ++i (Omite resto del cuerpo)", font="Consolas", font_size=11, color="#fde047")
        t_cont = VGroup(t_cont_title, t_cont_desc).arrange(DOWN, aligned_edge=LEFT, buff=0.08).move_to(box_cont.get_center())
        card_cont = VGroup(box_cont, t_cont)

        box_break = RoundedRectangle(
            width=5.2, height=0.75, corner_radius=0.08, 
            fill_color="#180a0a", fill_opacity=0.95, 
            stroke_color="#ef4444", stroke_width=1.5
        )
        t_break_title = Text("SENTENCIA BREAK:", font="Consolas", font_size=11, color="#ef4444", weight=BOLD)
        t_break_desc = Text("Salta fuera del bucle (Termina iteraciones)", font="Consolas", font_size=11, color="#fca5a5")
        t_break = VGroup(t_break_title, t_break_desc).arrange(DOWN, aligned_edge=LEFT, buff=0.08).move_to(box_break.get_center())
        card_break = VGroup(box_break, t_break)

        cards = VGroup(card_cont, card_break).arrange(DOWN, buff=0.35)
        cards.move_to(panel_bg.get_center() + DOWN * 0.15)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "SISTEMA", 
            "Analizando interrupción y saltos de flujo dentro del bucle for.", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(code_win, shift=RIGHT * 0.2),
            FadeIn(code_lines, shift=RIGHT * 0.2),
            FadeIn(panel_win, shift=LEFT * 0.2),
            FadeIn(card_cont, shift=LEFT * 0.2),
            FadeIn(hud, shift=UP * 0.2),
            rate_func=smooth
        )
        self.wait(1.5)

        # FASE 1: CONTINUE
        hud_cont = self.create_hud_footer(
            "CONTINUE", 
            "if (i == 2) continue: Cancela la iteración actual y salta al incremento ++i.", 
            color=self.COLOR_GOLD
        )
        pointer_cont = self.create_code_pointer(line2, color=self.COLOR_GOLD)

        self.play(
            FadeIn(pointer_cont, shift=RIGHT * 0.1),
            box_cont.animate.set_stroke(color="#fbbf24", width=2.2),
            ReplacementTransform(hud, hud_cont),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 2: BREAK
        hud_break = self.create_hud_footer(
            "BREAK", 
            "if (i == 4) break: Aborta el bucle inmediatamente y salta fuera de '}'.", 
            color=self.COLOR_RED
        )
        pointer_break = self.create_code_pointer(line3, color=self.COLOR_RED)

        self.play(
            ReplacementTransform(pointer_cont, pointer_break),
            FadeIn(card_break, shift=DOWN * 0.1),
            box_break.animate.set_stroke(color="#ef4444", width=2.2),
            ReplacementTransform(hud_cont, hud_break),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 3: SÍNTESIS FINAL
        hud_final = self.create_hud_footer(
            "BREAK & CONTINUE C++", 
            "'break' termina el ciclo; 'continue' solo avanza a la siguiente iteración.", 
            color=self.COLOR_GREEN
        )
        pointer_end = self.create_code_pointer(line6, color=self.COLOR_CYAN)

        self.play(
            ReplacementTransform(pointer_break, pointer_end),
            ReplacementTransform(hud_break, hud_final),
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
        "L07BreakContinue": "l07_break_continue.gif",
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
