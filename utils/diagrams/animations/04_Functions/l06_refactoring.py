from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene

class L06Refactoring(BaseLearningScene):
    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "Modularidad y Refactoring", 
            "Separación de Responsabilidades y Extracción de Rutinas en C++"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.5)

        # 2. PANEL IZQUIERDO: CÓDIGO MONOLÍTICO (ANTES) - 5.8 x 3.6
        win_before, bg_before = self.create_code_window(width=5.8, height=3.6, title="monolito.cpp [Antes]")
        win_before.shift(LEFT * 3.3 + DOWN * 0.15)
        
        b_line1 = MarkupText(
            '<span foreground="#ef4444"><b>int</b></span> '
            '<span foreground="#ef4444"><b>main</b></span>() '
            '<span foreground="#ef4444">{</span>',
            font="Consolas", font_size=15
        )
        b_line2 = MarkupText(
            '<span foreground="#64748b">// 20 lineas: Dibujar UI</span>',
            font="Consolas", font_size=13, color="#64748b"
        )
        b_line3 = MarkupText(
            'std::cout &lt;&lt; <span foreground="#f59e0b">"=== MENU ===\\n"</span>;',
            font="Consolas", font_size=13, color="#f0f6fc"
        )
        b_line4 = MarkupText(
            '<span foreground="#64748b">// 15 lineas: Validar Input</span>',
            font="Consolas", font_size=13, color="#64748b"
        )
        b_line5 = MarkupText(
            'std::cin &gt;&gt; opt; <span foreground="#ef4444">if (opt &lt; 0)...</span>',
            font="Consolas", font_size=13, color="#f0f6fc"
        )
        b_line6 = MarkupText(
            '<span foreground="#64748b">// 30 lineas: Calculo</span>',
            font="Consolas", font_size=13, color="#64748b"
        )
        b_line7 = MarkupText(
            '<span foreground="#10b981">int</span> res{opt * <span foreground="#fbbf24">42</span>};',
            font="Consolas", font_size=13, color="#f0f6fc"
        )
        b_line8 = MarkupText(
            '<span foreground="#c084fc"><b>return</b></span> <span foreground="#fbbf24">0</span>;',
            font="Consolas", font_size=15, color="#f0f6fc"
        )
        b_line9 = MarkupText(
            '<span foreground="#ef4444">}</span>',
            font="Consolas", font_size=15
        )

        INDENT = 0.40
        b_line1.move_to(ORIGIN)
        b_line2.next_to(b_line1, DOWN, aligned_edge=LEFT, buff=0.12).shift(RIGHT * INDENT)
        b_line3.next_to(b_line2, DOWN, aligned_edge=LEFT, buff=0.12)
        b_line4.next_to(b_line3, DOWN, aligned_edge=LEFT, buff=0.12)
        b_line5.next_to(b_line4, DOWN, aligned_edge=LEFT, buff=0.12)
        b_line6.next_to(b_line5, DOWN, aligned_edge=LEFT, buff=0.12)
        b_line7.next_to(b_line6, DOWN, aligned_edge=LEFT, buff=0.12)
        b_line8.next_to(b_line7, DOWN, aligned_edge=LEFT, buff=0.12)
        b_line9.next_to(b_line8, DOWN, aligned_edge=LEFT, buff=0.12).shift(LEFT * INDENT)

        code_before = VGroup(b_line1, b_line2, b_line3, b_line4, b_line5, b_line6, b_line7, b_line8, b_line9)
        code_before.move_to(bg_before.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: CÓDIGO MODULAR (DESPUÉS) - 5.8 x 3.6
        win_after, bg_after = self.create_code_window(width=5.8, height=3.6, title="modular.cpp [Despues]")
        win_after.shift(RIGHT * 3.3 + DOWN * 0.15)

        a_line1 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> '
            '<span foreground="#38bdf8"><b>main</b></span>() '
            '<span foreground="#c084fc">{</span>',
            font="Consolas", font_size=16
        )
        a_line2 = MarkupText(
            '<span foreground="#38bdf8">dibujarMenu</span>(); <span foreground="#64748b">// Delegado</span>',
            font="Consolas", font_size=15, color="#f0f6fc"
        )
        a_line3 = MarkupText(
            '<span foreground="#10b981">int</span> opt{<span foreground="#38bdf8">pedirOpcion</span>()};',
            font="Consolas", font_size=15, color="#f0f6fc"
        )
        a_line4 = MarkupText(
            '<span foreground="#38bdf8">procesarCalculo</span>(opt);',
            font="Consolas", font_size=15, color="#f0f6fc"
        )
        a_line5 = MarkupText(
            '<span foreground="#c084fc"><b>return</b></span> <span foreground="#fbbf24">0</span>; <span foreground="#10b981">// Orquestador</span>',
            font="Consolas", font_size=15, color="#f0f6fc"
        )
        a_line6 = MarkupText(
            '<span foreground="#c084fc">}</span>',
            font="Consolas", font_size=16
        )

        a_line1.move_to(ORIGIN)
        a_line2.next_to(a_line1, DOWN, aligned_edge=LEFT, buff=0.18).shift(RIGHT * INDENT)
        a_line3.next_to(a_line2, DOWN, aligned_edge=LEFT, buff=0.18)
        a_line4.next_to(a_line3, DOWN, aligned_edge=LEFT, buff=0.18)
        a_line5.next_to(a_line4, DOWN, aligned_edge=LEFT, buff=0.18)
        a_line6.next_to(a_line5, DOWN, aligned_edge=LEFT, buff=0.18).shift(LEFT * INDENT)

        code_after = VGroup(a_line1, a_line2, a_line3, a_line4, a_line5, a_line6)
        code_after.move_to(bg_after.get_center() + DOWN * 0.08)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "MONOLITO", 
            "Código acoplado: Todas las responsabilidades comprimidas dentro de main().", 
            color=self.COLOR_RED
        )

        self.play(
            FadeIn(win_before, shift=RIGHT * 0.2),
            FadeIn(code_before, shift=RIGHT * 0.2),
            FadeIn(hud, shift=UP * 0.2),
            rate_func=smooth
        )
        self.wait(1.5)

        # FASE 1: ESCANEO Y EXTRACCIÓN DE RUTINAS
        hud_extract = self.create_hud_footer(
            "EXTRACCIÓN", 
            "Identificando bloques lógicos para modularizarlos en rutinas delegadas.", 
            color=self.COLOR_GOLD
        )
        scan_box = SurroundingRectangle(
            code_before[1:7], color=self.COLOR_GOLD, 
            fill_color=self.COLOR_GOLD, fill_opacity=0.15, 
            corner_radius=0.10, stroke_width=2.0, buff=0.08
        )

        self.play(
            FadeIn(scan_box),
            ReplacementTransform(hud, hud_extract),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 2: REFACTORIZACIÓN MODULAR
        hud_modular = self.create_hud_footer(
            "DELEGACIÓN", 
            "Separation of Concerns: El main() se convierte en un orquestador limpio y modular.", 
            color=self.COLOR_CYAN
        )
        self.play(
            FadeOut(scan_box),
            FadeIn(win_after, shift=LEFT * 0.2),
            FadeIn(code_after, shift=LEFT * 0.2),
            ReplacementTransform(hud_extract, hud_modular),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 3: SÍNTESIS FINAL
        hud_final = self.create_hud_footer(
            "PRINCIPIO DRY", 
            "Don't Repeat Yourself: Código legible, testeable y de fácil mantenimiento.", 
            color=self.COLOR_GREEN
        )
        self.play(
            win_after.animate.set_stroke(color="#10b981", width=2.5),
            ReplacementTransform(hud_modular, hud_final),
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
        "L06Refactoring": "l06_refactoring.gif",
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
