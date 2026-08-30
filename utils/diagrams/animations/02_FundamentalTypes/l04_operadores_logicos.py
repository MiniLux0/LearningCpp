from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene

class OperadoresLogicos(BaseLearningScene):
    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "Operadores Relacionales y Lógicos", 
            "Evaluación Booleana (&&, ||) y Comparación Estricta (==)"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.5)

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (6.0 x 3.6)
        code_win, code_bg = self.create_code_window(width=6.0, height=3.6, title="logica.cpp")
        code_win.shift(LEFT * 3.3 + DOWN * 0.15)
        
        line1 = MarkupText(
            '<span foreground="#10b981"><b>bool</b></span> esMayor{edad &gt;= <span foreground="#fbbf24">18</span>}; <span foreground="#10b981">// true</span>',
            font="Consolas", font_size=15, color="#f0f6fc"
        )
        line2 = MarkupText(
            '<span foreground="#10b981"><b>bool</b></span> paseVIP{<span foreground="#38bdf8">true</span>};        <span foreground="#10b981">// true</span>',
            font="Consolas", font_size=15, color="#f0f6fc"
        )
        line3 = MarkupText(
            '<span foreground="#10b981"><b>bool</b></span> entrar{esMayor <span foreground="#c084fc"><b>&amp;&amp;</b></span> paseVIP};',
            font="Consolas", font_size=15, color="#f0f6fc"
        )

        code_lines = VGroup(line1, line2, line3).arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: COMPUERTA LÓGICA AND (&&)
        panel_win, panel_bg = self.create_card_panel(
            width=5.8, height=3.6, 
            title="Compuerta Lógica AND (&&)", 
            subtitle="Evaluación Booleana Rigurosa"
        )
        panel_win.shift(RIGHT * 3.3 + DOWN * 0.15)
        
        # Entradas
        in1_box = RoundedRectangle(width=2.2, height=0.55, corner_radius=0.08, fill_color="#0f172a", fill_opacity=0.95, stroke_color="#10b981", stroke_width=1.5).move_to(panel_bg.get_center() + UP * 0.55 + LEFT * 1.2)
        t_in1 = Text("esMayor: true", font="Consolas", font_size=11, color="#6ee7b7", weight=BOLD).move_to(in1_box.get_center())
        card_in1 = VGroup(in1_box, t_in1)

        in2_box = RoundedRectangle(width=2.2, height=0.55, corner_radius=0.08, fill_color="#0f172a", fill_opacity=0.95, stroke_color="#10b981", stroke_width=1.5).move_to(panel_bg.get_center() + DOWN * 0.15 + LEFT * 1.2)
        t_in2 = Text("paseVIP: true", font="Consolas", font_size=11, color="#6ee7b7", weight=BOLD).move_to(in2_box.get_center())
        card_in2 = VGroup(in2_box, t_in2)

        # Salida
        out_box = RoundedRectangle(width=5.2, height=0.65, corner_radius=0.08, fill_color="#0f172a", fill_opacity=0.98, stroke_color="#10b981", stroke_width=2.0).move_to(panel_bg.get_center() + DOWN * 0.85)
        t_out = Text("RESULTADO (&&): [ true ] (Ambas cumplen)", font="Consolas", font_size=11, color="#6ee7b7", weight=BOLD).move_to(out_box.get_center())
        card_out = VGroup(out_box, t_out)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "SISTEMA", 
            "Evaluando compuertas lógicas: '&&' (AND) exige que ambos operandos sean verdaderos.", 
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

        # FASE 1: PRIMER OPERANDO
        hud_op1 = self.create_hud_footer(
            "OPERANDO 1", 
            "esMayor: (edad >= 18) evalúa a 'true' en el Stack.", 
            color=self.COLOR_GREEN
        )
        pointer1 = self.create_code_pointer(line1, color=self.COLOR_GREEN)

        self.play(
            FadeIn(pointer1, shift=RIGHT * 0.1),
            FadeIn(card_in1, shift=LEFT * 0.15),
            ReplacementTransform(hud, hud_op1),
            rate_func=smooth
        )
        self.wait(2.5)

        # FASE 2: SEGUNDO OPERANDO
        hud_op2 = self.create_hud_footer(
            "OPERANDO 2", 
            "paseVIP: Variable booleana evaluada en 'true'.", 
            color=self.COLOR_CYAN
        )
        pointer2 = self.create_code_pointer(line2, color=self.COLOR_CYAN)

        self.play(
            ReplacementTransform(pointer1, pointer2),
            FadeIn(card_in2, shift=LEFT * 0.15),
            ReplacementTransform(hud_op1, hud_op2),
            rate_func=smooth
        )
        self.wait(2.5)

        # FASE 3: EVALUACIÓN AND (&&)
        hud_and = self.create_hud_footer(
            "EVALUACIÓN &&", 
            "true && true -> La compuerta AND produce 'true' inyectando el valor a 'entrar'.", 
            color=self.COLOR_GOLD
        )
        pointer3 = self.create_code_pointer(line3, color=self.COLOR_GOLD)

        self.play(
            ReplacementTransform(pointer2, pointer3),
            FadeIn(card_out, shift=UP * 0.1),
            out_box.animate.set_stroke(color="#10b981", width=2.5),
            ReplacementTransform(hud_op2, hud_and),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 4: SÍNTESIS FINAL
        hud_final = self.create_hud_footer(
            "LÓGICA BOOLEANA", 
            "Usa '&&' para conjunciones, '||' para disyunciones y '==' para comparar igualdad.", 
            color=self.COLOR_GREEN
        )
        self.play(
            FadeOut(pointer3),
            ReplacementTransform(hud_and, hud_final),
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
        "OperadoresLogicos": "l04_operadores_logicos.gif",
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
