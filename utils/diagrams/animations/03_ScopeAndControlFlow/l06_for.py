from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene

class L06ForLoop(BaseLearningScene):
    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "Bucle For (for)", 
            "Anatomía en 3 fases: Inicialización, Condición e Incremento"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.5)

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (6.0 x 3.6)
        code_win, code_bg = self.create_code_window(width=6.0, height=3.6, title="bucle_for.cpp")
        code_win.shift(LEFT * 3.3 + DOWN * 0.15)
        
        line1 = MarkupText(
            '<span foreground="#c084fc"><b>for</b></span> '
            '(<span foreground="#10b981">int</span> <span foreground="#38bdf8">i{0}</span>; '
            '<span foreground="#fbbf24">i &lt; 3</span>; '
            '<span foreground="#10b981">++i</span>) <span foreground="#c084fc">{</span>',
            font="Consolas", font_size=15
        )
        line2 = MarkupText(
            'std::cout &lt;&lt; i &lt;&lt; <span foreground="#10b981">\'\\n\'</span>;',
            font="Consolas", font_size=16, color="#f0f6fc"
        )
        line3 = MarkupText(
            '<span foreground="#c084fc">}</span>',
            font="Consolas", font_size=16
        )
        line4 = MarkupText(
            '<span foreground="#64748b">// Variable \'i\' se destruye al salir</span>',
            font="Consolas", font_size=14, color="#64748b"
        )
        
        INDENT = 0.45
        line1.move_to(ORIGIN)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.20).shift(RIGHT * INDENT)
        line3.next_to(line2, DOWN, aligned_edge=LEFT, buff=0.20).shift(LEFT * INDENT)
        line4.next_to(line3, DOWN, aligned_edge=LEFT, buff=0.20)

        code_lines = VGroup(line1, line2, line3, line4)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: LAS 3 FASES DEL BUCLE
        panel_win, panel_bg = self.create_card_panel(
            width=5.8, height=3.6, 
            title="Las 3 Fases del Bucle For", 
            subtitle="Pipeline de Ejecución Cíclica"
        )
        panel_win.shift(RIGHT * 3.3 + DOWN * 0.15)
        
        f1 = RoundedRectangle(
            width=5.2, height=0.60, corner_radius=0.08, 
            fill_color="#0f172a", fill_opacity=0.95, 
            stroke_color="#38bdf8", stroke_width=1.5
        )
        t_f1 = Text("1. Inicializacion -> int i{0} (1 sola vez)", font="Consolas", font_size=11, color="#7dd3fc", weight=BOLD).move_to(f1.get_center())
        card1 = VGroup(f1, t_f1)

        f2 = RoundedRectangle(
            width=5.2, height=0.60, corner_radius=0.08, 
            fill_color="#0f172a", fill_opacity=0.95, 
            stroke_color="#fbbf24", stroke_width=1.5
        )
        t_f2 = Text("2. Condicion      -> i < 3 (Antes de iterar)", font="Consolas", font_size=11, color="#fde047", weight=BOLD).move_to(f2.get_center())
        card2 = VGroup(f2, t_f2)

        f3 = RoundedRectangle(
            width=5.2, height=0.60, corner_radius=0.08, 
            fill_color="#0f172a", fill_opacity=0.95, 
            stroke_color="#10b981", stroke_width=1.5
        )
        t_f3 = Text("3. Incremento     -> ++i (Al final del paso)", font="Consolas", font_size=11, color="#6ee7b7", weight=BOLD).move_to(f3.get_center())
        card3 = VGroup(f3, t_f3)

        cards = VGroup(card1, card2, card3).arrange(DOWN, buff=0.22)
        cards.move_to(panel_bg.get_center() + DOWN * 0.15)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "SISTEMA", 
            "Iniciando desglose anatómico del bucle 'for' en C++.", 
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

        # FASE 1: INICIALIZACIÓN
        hud_f1 = self.create_hud_footer(
            "1. INICIALIZACIÓN", 
            "int i{0}: Se crea la variable contadora una única vez en el Stack local.", 
            color=self.COLOR_CYAN
        )
        pointer_init = self.create_code_pointer(line1, color=self.COLOR_CYAN)

        self.play(
            FadeIn(pointer_init, shift=RIGHT * 0.1),
            f1.animate.set_stroke(color="#38bdf8", width=2.2),
            ReplacementTransform(hud, hud_f1),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 2: CONDICIÓN
        hud_f2 = self.create_hud_footer(
            "2. CONDICIÓN", 
            "i < 3: Se evalúa antes de cada iteración. Si es true, ejecuta el cuerpo.", 
            color=self.COLOR_GOLD
        )
        self.play(
            FadeIn(card2, shift=DOWN * 0.1),
            f2.animate.set_stroke(color="#fbbf24", width=2.2),
            ReplacementTransform(hud_f1, hud_f2),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 3: INCREMENTO
        hud_f3 = self.create_hud_footer(
            "3. INCREMENTO", 
            "++i: Se ejecuta automáticamente al final de cada iteración para avanzar.", 
            color=self.COLOR_GREEN
        )
        pointer_body = self.create_code_pointer(line2, color=self.COLOR_GREEN)

        self.play(
            ReplacementTransform(pointer_init, pointer_body),
            FadeIn(card3, shift=DOWN * 0.1),
            f3.animate.set_stroke(color="#10b981", width=2.2),
            ReplacementTransform(hud_f2, hud_f3),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 4: SÍNTESIS FINAL
        hud_final = self.create_hud_footer(
            "FOR LOOP C++", 
            "Estructura compacta: Encapsula inicio, comprobación y paso en una sola cabecera.", 
            color=self.COLOR_GREEN
        )
        self.play(
            FadeOut(pointer_body),
            ReplacementTransform(hud_f3, hud_final),
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
        "L06ForLoop": "l06_for_loop.gif",
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
