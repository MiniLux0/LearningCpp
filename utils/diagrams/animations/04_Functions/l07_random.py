from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene

class L07RandomMachine(BaseLearningScene):
    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "Arquitectura de un PRNG Moderno", 
            "Entropía, Motor Mersenne Twister y Distribución Uniforme (<random>)"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.5)

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (6.0 x 3.6)
        code_win, code_bg = self.create_code_window(width=6.0, height=3.6, title="azar.cpp")
        code_win.shift(LEFT * 3.3 + DOWN * 0.15)
        
        line1 = MarkupText(
            '<span foreground="#c084fc">#include</span> <span foreground="#f59e0b">&lt;random&gt;</span>',
            font="Consolas", font_size=15
        )
        line2 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> '
            '<span foreground="#38bdf8"><b>lanzarDado</b></span>() '
            '<span foreground="#c084fc">{</span>',
            font="Consolas", font_size=16
        )
        line3 = MarkupText(
            '<span foreground="#c084fc">static</span> std::mt19937 motor{',
            font="Consolas", font_size=14, color="#7dd3fc"
        )
        line4 = MarkupText(
            'std::random_device{}()};',
            font="Consolas", font_size=14, color="#f87171"
        )
        line5 = MarkupText(
            'std::uniform_int_distribution dist{<span foreground="#fbbf24">1</span>, <span foreground="#fbbf24">6</span>};',
            font="Consolas", font_size=13, color="#fde047"
        )
        line6 = MarkupText(
            '<span foreground="#c084fc"><b>return</b></span> dist(motor);',
            font="Consolas", font_size=15, color="#6ee7b7"
        )
        line7 = MarkupText(
            '<span foreground="#c084fc">}</span>',
            font="Consolas", font_size=16
        )

        INDENT = 0.40
        INDENT2 = 0.70
        line1.move_to(ORIGIN)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.18)
        line3.next_to(line2, DOWN, aligned_edge=LEFT, buff=0.14).shift(RIGHT * INDENT)
        line4.next_to(line3, DOWN, aligned_edge=LEFT, buff=0.12).shift(RIGHT * (INDENT2 - INDENT))
        line5.next_to(line4, DOWN, aligned_edge=LEFT, buff=0.14).shift(LEFT * (INDENT2 - INDENT))
        line6.next_to(line5, DOWN, aligned_edge=LEFT, buff=0.14)
        line7.next_to(line6, DOWN, aligned_edge=LEFT, buff=0.14).shift(LEFT * INDENT)

        code_lines = VGroup(line1, line2, line3, line4, line5, line6, line7)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: PIPELINE DE 3 CAPAS EN HARDWARE
        panel_win, panel_bg = self.create_card_panel(
            width=5.8, height=3.6, 
            title="Pipeline C++ <random>", 
            subtitle="Las 3 Capas de Generación de Azar"
        )
        panel_win.shift(RIGHT * 3.3 + DOWN * 0.15)
        
        # 3 Badges de Alto Contraste con Flechas ASCII
        badge_entropy = self.create_badge(
            "1. std::random_device -> Entropia Hardware", 
            fill_color="#0f172a", stroke_color="#ef4444", text_color="#fca5a5", 
            width=5.3, height=0.48
        )
        badge_engine = self.create_badge(
            "2. static std::mt19937 -> Motor Mersenne", 
            fill_color="#0f172a", stroke_color="#38bdf8", text_color="#7dd3fc", 
            width=5.3, height=0.48
        )
        badge_dist = self.create_badge(
            "3. std::uniform_int_distribution -> [1, 6]", 
            fill_color="#0f172a", stroke_color="#f59e0b", text_color="#fde047", 
            width=5.3, height=0.48
        )

        badges = VGroup(badge_entropy, badge_engine, badge_dist).arrange(DOWN, buff=0.22)
        badges.move_to(panel_bg.get_center() + DOWN * 0.15)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "SISTEMA", 
            "Iniciando arquitectura de azar en C++ Moderno (<random>).", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(code_win, shift=RIGHT * 0.2),
            FadeIn(code_lines, shift=RIGHT * 0.2),
            FadeIn(panel_win, shift=LEFT * 0.2),
            FadeIn(badges, shift=LEFT * 0.2),
            FadeIn(hud, shift=UP * 0.2),
            rate_func=smooth
        )
        self.wait(1.5)

        # FASE 1: ENTROPÍA
        hud_ent = self.create_hud_footer(
            "ENTROPÍA", 
            "random_device: Captura ruido físico del hardware como semilla inicial.", 
            color=self.COLOR_RED
        )
        self.play(
            badge_entropy.animate.set_stroke(color="#ef4444", width=2.5),
            ReplacementTransform(hud, hud_ent),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 2: MOTOR MERSENNE TWISTER CON STATIC
        hud_eng = self.create_hud_footer(
            "MOTOR STATIC", 
            "mt19937: El modificador 'static' ancla el motor en RAM evitando secuencias clonadas.", 
            color=self.COLOR_CYAN
        )
        self.play(
            badge_engine.animate.set_stroke(color="#38bdf8", width=2.5),
            ReplacementTransform(hud_ent, hud_eng),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 3: DISTRIBUCIÓN ESTADÍSTICA UNIFORME
        hud_dist = self.create_hud_footer(
            "DISTRIBUCIÓN", 
            "uniform_int_distribution: Normaliza el output masivo en un entero uniforme (1 a 6).", 
            color=self.COLOR_GOLD
        )
        
        dice_result = self.create_badge(
            "VALOR GENERADO: [ 4 ] -> Rango [1, 6]", 
            fill_color="#0f172a", stroke_color="#10b981", text_color="#6ee7b7", 
            width=5.3, height=0.48
        ).move_to(badge_dist.get_center())

        self.play(
            ReplacementTransform(hud_eng, hud_dist),
            FadeOut(badge_dist),
            FadeIn(dice_result, shift=UP * 0.1),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 4: SÍNTESIS FINAL
        hud_final = self.create_hud_footer(
            "PRNG C++", 
            "Arquitectura robusta: Cero sesgo modular y alta calidad estadística.", 
            color=self.COLOR_GREEN
        )
        self.play(
            ReplacementTransform(hud_dist, hud_final),
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
        "L07RandomMachine": "l07_rng_machine.gif",
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
