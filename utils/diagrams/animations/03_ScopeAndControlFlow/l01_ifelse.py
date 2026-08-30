from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene

class L01IfElse(BaseLearningScene):
    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "Bifurcación Condicional (if - else)", 
            "Evaluación booleana y rutas de ejecución excluyentes en CPU"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.5)

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (6.0 x 3.6)
        code_win, code_bg = self.create_code_window(width=6.0, height=3.6, title="decision.cpp")
        code_win.shift(LEFT * 3.3 + DOWN * 0.15)
        
        line1 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> edad{<span foreground="#fbbf24">20</span>};',
            font="Consolas", font_size=17, color="#f0f6fc"
        )
        line2 = MarkupText(
            '<span foreground="#c084fc"><b>if</b></span> (edad &gt;= <span foreground="#fbbf24">18</span>) <span foreground="#c084fc">{</span>',
            font="Consolas", font_size=17
        )
        line3 = MarkupText(
            'std::cout &lt;&lt; <span foreground="#10b981">"Acceso VIP\\n"</span>;',
            font="Consolas", font_size=17, color="#f0f6fc"
        )
        line4 = MarkupText(
            '<span foreground="#c084fc">} <b>else</b> {</span>',
            font="Consolas", font_size=17
        )
        line5 = MarkupText(
            'std::cout &lt;&lt; <span foreground="#ef4444">"Acceso Denegado\\n"</span>;',
            font="Consolas", font_size=17, color="#64748b"
        )
        line6 = MarkupText(
            '<span foreground="#c084fc">}</span>',
            font="Consolas", font_size=17
        )
        
        INDENT = 0.45
        line1.move_to(ORIGIN)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.18)
        line3.next_to(line2, DOWN, aligned_edge=LEFT, buff=0.18).shift(RIGHT * INDENT)
        line4.next_to(line3, DOWN, aligned_edge=LEFT, buff=0.18).shift(LEFT * INDENT)
        line5.next_to(line4, DOWN, aligned_edge=LEFT, buff=0.18).shift(RIGHT * INDENT)
        line6.next_to(line5, DOWN, aligned_edge=LEFT, buff=0.18).shift(LEFT * INDENT)

        code_lines = VGroup(line1, line2, line3, line4, line5, line6)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: EVALUACIÓN Y SALTO EN CPU
        panel_win, panel_bg = self.create_card_panel(
            width=5.8, height=3.6, 
            title="Pipeline de la CPU", 
            subtitle="Evaluación Booleana y Salto"
        )
        panel_win.shift(RIGHT * 3.3 + DOWN * 0.15)
        
        # Tarjeta de Condición
        cond_box = RoundedRectangle(
            width=5.2, height=0.65, corner_radius=0.08,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color="#fbbf24", stroke_width=1.5
        )
        cond_txt = Text("Condicion: edad >= 18 -> true", font="Consolas", font_size=12, color="#fde047", weight=BOLD).move_to(cond_box.get_center())
        cond_card = VGroup(cond_box, cond_txt)

        # Rama True (Acceso VIP)
        branch_true = RoundedRectangle(
            width=5.2, height=0.65, corner_radius=0.08,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color="#10b981", stroke_width=1.8
        )
        true_txt = Text("RAMA IF -> Ejecuta: [ Acceso VIP ]", font="Consolas", font_size=12, color="#6ee7b7", weight=BOLD).move_to(branch_true.get_center())
        branch_true_card = VGroup(branch_true, true_txt)

        # Rama False (Denegado / Omitida)
        branch_false = RoundedRectangle(
            width=5.2, height=0.65, corner_radius=0.08,
            fill_color="#0f172a", fill_opacity=0.5,
            stroke_color="#475569", stroke_width=1.2
        )
        false_txt = Text("RAMA ELSE -> OMITIDA (Branch Skip)", font="Consolas", font_size=12, color="#94a3b8").move_to(branch_false.get_center())
        branch_false_card = VGroup(branch_false, false_txt)

        cards = VGroup(cond_card, branch_true_card, branch_false_card).arrange(DOWN, buff=0.22)
        cards.move_to(panel_bg.get_center() + DOWN * 0.15)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "SISTEMA", 
            "Iniciando evaluación condicional: 'edad' inicializada con valor 20.", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(code_win, shift=RIGHT * 0.2),
            FadeIn(code_lines, shift=RIGHT * 0.2),
            FadeIn(panel_win, shift=LEFT * 0.2),
            FadeIn(cond_card, shift=LEFT * 0.2),
            FadeIn(hud, shift=UP * 0.2),
            rate_func=smooth
        )
        self.wait(1.5)

        # FASE 1: EVALUACIÓN DE LA CONDICIÓN
        hud_eval = self.create_hud_footer(
            "EVALUACIÓN", 
            "if (edad >= 18): (20 >= 18) evalúa a 'true'. Se habilita la rama principal.", 
            color=self.COLOR_GOLD
        )
        pointer_if = self.create_code_pointer(line2, color=self.COLOR_GOLD)

        self.play(
            FadeIn(pointer_if, shift=RIGHT * 0.1),
            cond_box.animate.set_stroke(color="#fbbf24", width=2.2),
            ReplacementTransform(hud, hud_eval),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 2: SALTO Y EJECUCIÓN DE LA RAMA VERDADERA
        hud_exec = self.create_hud_footer(
            "EJECUCIÓN", 
            "El flujo ingresa al cuerpo del 'if' e imprime 'Acceso VIP'.", 
            color=self.COLOR_GREEN
        )
        pointer_body = self.create_code_pointer(line3, color=self.COLOR_GREEN)

        self.play(
            ReplacementTransform(pointer_if, pointer_body),
            FadeIn(branch_true_card, shift=DOWN * 0.1),
            ReplacementTransform(hud_eval, hud_exec),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 3: SALTO SOBRE LA RAMA ELSE (BRANCH SKIP)
        hud_skip = self.create_hud_footer(
            "EXCLUSIÓN MUTUA", 
            "La rama 'else' es ignorada por completo por la CPU y se salta fuera del bloque.", 
            color=self.COLOR_CYAN
        )
        pointer_end = self.create_code_pointer(line6, color=self.COLOR_CYAN)

        self.play(
            ReplacementTransform(pointer_body, pointer_end),
            FadeIn(branch_false_card, shift=DOWN * 0.1),
            ReplacementTransform(hud_exec, hud_skip),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 4: SÍNTESIS FINAL
        hud_final = self.create_hud_footer(
            "IF - ELSE C++", 
            "Bifurcación estricta: Una sola ruta de ejecución se activa por evaluación booleana.", 
            color=self.COLOR_GREEN
        )
        self.play(
            FadeOut(pointer_end),
            ReplacementTransform(hud_skip, hud_final),
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
        "L01IfElse": "l01_if_else_flow.gif",
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
