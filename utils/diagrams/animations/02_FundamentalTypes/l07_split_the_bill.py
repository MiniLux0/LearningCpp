from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene

class SplitTheBillScene(BaseLearningScene):
    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "MiniProyecto: Split the Bill", 
            "Integración de tipos mixtos (double/int), casting y precisión decimal en terminal"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.5)

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (6.0 x 3.6)
        code_win, code_bg = self.create_code_window(width=6.0, height=3.6, title="split_the_bill.cpp")
        code_win.shift(LEFT * 3.3 + DOWN * 0.15)
        
        line1 = MarkupText(
            '<span foreground="#10b981"><b>double</b></span> total{<span foreground="#fbbf24">125.50</span>};',
            font="Consolas", font_size=15, color="#f0f6fc"
        )
        line2 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> personas{<span foreground="#fbbf24">4</span>};',
            font="Consolas", font_size=15, color="#f0f6fc"
        )
        line3 = MarkupText(
            '<span foreground="#10b981"><b>double</b></span> pago{total / personas};',
            font="Consolas", font_size=15, color="#f0f6fc"
        )
        line4 = MarkupText(
            'std::cout &lt;&lt; pago &lt;&lt; <span foreground="#10b981">\'\\n\'</span>;',
            font="Consolas", font_size=15, color="#f0f6fc"
        )

        code_lines = VGroup(line1, line2, line3, line4).arrange(DOWN, aligned_edge=LEFT, buff=0.20)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: TERMINAL DE CONSOLA DE ALTA FIDELIDAD
        panel_win, panel_bg = self.create_card_panel(
            width=5.8, height=3.6, 
            title="Terminal de Salida (I/O)", 
            subtitle="Facturación en Consola"
        )
        panel_win.shift(RIGHT * 3.3 + DOWN * 0.15)
        
        term_box = RoundedRectangle(
            width=5.2, height=1.6, corner_radius=0.1,
            fill_color="#030712", fill_opacity=0.98,
            stroke_color="#38bdf8", stroke_width=1.5
        ).move_to(panel_bg.get_center() + DOWN * 0.15)
        
        term_header = RoundedRectangle(
            width=5.2, height=0.32, corner_radius=0.1,
            fill_color="#0f172a", fill_opacity=1.0,
            stroke_color="#38bdf8", stroke_width=1.2
        ).next_to(term_box.get_top(), DOWN, buff=0)
        
        dot_r = Dot(radius=0.04, color="#ef4444")
        dot_y = Dot(radius=0.04, color="#f59e0b")
        dot_g = Dot(radius=0.04, color="#10b981")
        dots = VGroup(dot_r, dot_y, dot_g).arrange(RIGHT, buff=0.08).next_to(term_header.get_left(), RIGHT, buff=0.15)
        term_title = Text("bash - factura", font="Consolas", font_size=10, color="#94a3b8").next_to(dots, RIGHT, buff=0.15)
        
        t_line1 = Text("Cuenta Total: $125.50", font="Consolas", font_size=11, color="#e2e8f0").next_to(term_header, DOWN, buff=0.12).align_to(term_box, LEFT).shift(RIGHT * 0.2)
        t_line2 = Text("Personas:     4", font="Consolas", font_size=11, color="#38bdf8").next_to(t_line1, DOWN, buff=0.08).align_to(term_box, LEFT).shift(RIGHT * 0.2)
        t_line3 = Text("Total c/u:    $31.38", font="Consolas", font_size=14, color="#10b981", weight=BOLD).next_to(t_line2, DOWN, buff=0.08).align_to(term_box, LEFT).shift(RIGHT * 0.2)

        term_group = VGroup(term_box, term_header, dots, term_title)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "SISTEMA", 
            "Iniciando cálculo: double (125.50) / int (4) genera un resultado exacto en double.", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(code_win, shift=RIGHT * 0.2),
            FadeIn(code_lines, shift=RIGHT * 0.2),
            FadeIn(panel_win, shift=LEFT * 0.2),
            FadeIn(term_group, shift=LEFT * 0.2),
            FadeIn(hud, shift=UP * 0.2),
            rate_func=smooth
        )
        self.wait(1.5)

        # FASE 1: IMPRESIÓN DE TOTAL
        hud_f1 = self.create_hud_footer(
            "CUENTA TOTAL", 
            "total{125.50}: Monto global ingresado con precisión de punto flotante.", 
            color=self.COLOR_GOLD
        )
        pointer1 = self.create_code_pointer(line1, color=self.COLOR_GOLD)

        self.play(
            FadeIn(pointer1, shift=RIGHT * 0.1),
            FadeIn(t_line1, shift=RIGHT * 0.1),
            ReplacementTransform(hud, hud_f1),
            rate_func=smooth
        )
        self.wait(2.5)

        # FASE 2: COMENSALES
        hud_f2 = self.create_hud_footer(
            "COMENSALES", 
            "personas{4}: Cantidad entera de personas para dividir la cuenta.", 
            color=self.COLOR_CYAN
        )
        pointer2 = self.create_code_pointer(line2, color=self.COLOR_CYAN)

        self.play(
            ReplacementTransform(pointer1, pointer2),
            FadeIn(t_line2, shift=RIGHT * 0.1),
            ReplacementTransform(hud_f1, hud_f2),
            rate_func=smooth
        )
        self.wait(2.5)

        # FASE 3: RESULTADO POR PERSONA
        hud_f3 = self.create_hud_footer(
            "CÁLCULO EXACTO", 
            "pago = 125.50 / 4 = 31.375 -> Emite $31.38 en terminal sin truncamiento.", 
            color=self.COLOR_GREEN
        )
        pointer3 = self.create_code_pointer(line3, color=self.COLOR_GREEN)

        self.play(
            ReplacementTransform(pointer2, pointer3),
            FadeIn(t_line3, shift=RIGHT * 0.1),
            term_box.animate.set_stroke(color="#10b981", width=2.2),
            ReplacementTransform(hud_f2, hud_f3),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 4: SÍNTESIS FINAL
        hud_final = self.create_hud_footer(
            "CAPSTONE M02", 
            "Tipado seguro, inicialización uniforme y aritmética exacta dominadas con éxito.", 
            color=self.COLOR_GREEN
        )
        self.play(
            FadeOut(pointer3),
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
        "SplitTheBillScene": "l07_split_the_bill.gif",
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
