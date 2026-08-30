from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene

class L05WhileLoop(BaseLearningScene):
    def create_ram_slot(self, address: str, var_type: str, var_name: str, val_str: str, val_color: str = "#38bdf8", width: float = 4.9):
        bg = RoundedRectangle(
            width=width, height=0.48, corner_radius=0.08, 
            fill_color="#0f172a", fill_opacity=0.9, 
            stroke_color="#334155", stroke_width=1.2
        )
        addr_lbl = Text(address, font="Consolas", font_size=10, color="#64748b")
        type_lbl = Text(var_type, font="Consolas", font_size=11, color="#10b981", weight=BOLD)
        name_lbl = Text(var_name, font="Consolas", font_size=13, color="#f1f5f9", weight=BOLD)
        
        left_group = VGroup(addr_lbl, type_lbl, name_lbl).arrange(RIGHT, buff=0.15)
        left_group.next_to(bg.get_left(), RIGHT, buff=0.15)
        
        val_box = RoundedRectangle(
            width=1.1, height=0.36, corner_radius=0.06, 
            fill_color="#1e293b", fill_opacity=0.95, 
            stroke_color=val_color, stroke_width=1.5
        )
        val_box.next_to(bg.get_right(), LEFT, buff=0.12)
        val_lbl = Text(val_str, font="Consolas", font_size=13, color=val_color, weight=BOLD).move_to(val_box.get_center())
        val_group = VGroup(val_box, val_lbl)
        
        return VGroup(bg, left_group, val_group)

    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "Bucle While (while)", 
            "Ciclo repetitivo basado en condición booleana y mutación en Stack RAM"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.5)

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (6.0 x 3.6)
        code_win, code_bg = self.create_code_window(width=6.0, height=3.6, title="contador.cpp")
        code_win.shift(LEFT * 3.3 + DOWN * 0.15)
        
        line1 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> i{<span foreground="#fbbf24">0</span>};',
            font="Consolas", font_size=17, color="#f0f6fc"
        )
        line2 = MarkupText(
            '<span foreground="#c084fc"><b>while</b></span> (i &lt; <span foreground="#fbbf24">3</span>) <span foreground="#c084fc">{</span>',
            font="Consolas", font_size=17
        )
        line3 = MarkupText(
            'std::cout &lt;&lt; i &lt;&lt; <span foreground="#10b981">\'\\n\'</span>;',
            font="Consolas", font_size=17, color="#f0f6fc"
        )
        line4 = MarkupText(
            '<span foreground="#38bdf8">++i</span>; <span foreground="#64748b">// Incremento</span>',
            font="Consolas", font_size=17, color="#f0f6fc"
        )
        line5 = MarkupText(
            '<span foreground="#c084fc">}</span>',
            font="Consolas", font_size=17
        )
        line6 = MarkupText(
            '<span foreground="#64748b">// Fin del ciclo</span>',
            font="Consolas", font_size=15, color="#64748b"
        )
        
        INDENT = 0.45
        line1.move_to(ORIGIN)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.18)
        line3.next_to(line2, DOWN, aligned_edge=LEFT, buff=0.18).shift(RIGHT * INDENT)
        line4.next_to(line3, DOWN, aligned_edge=LEFT, buff=0.18)
        line5.next_to(line4, DOWN, aligned_edge=LEFT, buff=0.18).shift(LEFT * INDENT)
        line6.next_to(line5, DOWN, aligned_edge=LEFT, buff=0.18)

        code_lines = VGroup(line1, line2, line3, line4, line5, line6)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: ESTADO EN STACK RAM Y EVALUACIÓN
        panel_win, panel_bg = self.create_card_panel(
            width=5.8, height=3.6, 
            title="Estado de Memoria & Bucle", 
            subtitle="Mutación en RAM por Iteración"
        )
        panel_win.shift(RIGHT * 3.3 + DOWN * 0.15)
        
        # Celda RAM de 'i'
        slot_i = self.create_ram_slot("0x7FFEE0", "int", "i", "0", val_color="#38bdf8", width=5.2)
        slot_i.move_to(panel_bg.get_center() + UP * 0.7)

        # Tarjeta de Condición
        eval_box = RoundedRectangle(
            width=5.2, height=1.3, corner_radius=0.1,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color="#fbbf24", stroke_width=1.5
        ).move_to(panel_bg.get_center() + DOWN * 0.45)
        
        eval_title = Text("EVALUACIÓN DE CONDICIÓN:", font="Consolas", font_size=11, color="#fbbf24", weight=BOLD)
        eval_step = Text("Paso 0: (0 < 3) -> true  [Itera]", font="Consolas", font_size=12, color="#6ee7b7", weight=BOLD)
        eval_content = VGroup(eval_title, eval_step).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(eval_box.get_center())
        eval_card = VGroup(eval_box, eval_content)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "SISTEMA", 
            "Iniciando bucle: 'int i{0}' asignado en 0x7FFEE0.", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(code_win, shift=RIGHT * 0.2),
            FadeIn(code_lines, shift=RIGHT * 0.2),
            FadeIn(panel_win, shift=LEFT * 0.2),
            FadeIn(slot_i, shift=LEFT * 0.2),
            FadeIn(eval_card, shift=LEFT * 0.2),
            FadeIn(hud, shift=UP * 0.2),
            rate_func=smooth
        )
        self.wait(1.5)

        # ITERACIÓN 1: i = 0 -> ++i -> 1
        hud_it1 = self.create_hud_footer(
            "ITERACIÓN 1", 
            "Condición (0 < 3) es true: Imprime 0 y ejecuta ++i mutando 'i' a 1.", 
            color=self.COLOR_GREEN
        )
        pointer_w = self.create_code_pointer(line2, color=self.COLOR_GOLD)
        pointer_inc = self.create_code_pointer(line4, color=self.COLOR_CYAN)

        self.play(
            FadeIn(pointer_w, shift=RIGHT * 0.1),
            ReplacementTransform(hud, hud_it1),
            rate_func=smooth
        )
        self.wait(0.6)
        
        slot_i1 = self.create_ram_slot("0x7FFEE0", "int", "i", "1", val_color="#10b981", width=5.2).move_to(slot_i.get_center())
        eval_step1 = Text("Paso 1: (1 < 3) -> true  [Itera]", font="Consolas", font_size=12, color="#6ee7b7", weight=BOLD).move_to(eval_step.get_center())
        
        self.play(
            ReplacementTransform(pointer_w, pointer_inc),
            ReplacementTransform(slot_i, slot_i1),
            ReplacementTransform(eval_step, eval_step1),
            rate_func=smooth
        )
        self.wait(2.5)

        # ITERACIÓN 2: i = 1 -> ++i -> 2
        hud_it2 = self.create_hud_footer(
            "ITERACIÓN 2", 
            "Condición (1 < 3) es true: Imprime 1 y ejecuta ++i mutando 'i' a 2.", 
            color=self.COLOR_GREEN
        )
        slot_i2 = self.create_ram_slot("0x7FFEE0", "int", "i", "2", val_color="#10b981", width=5.2).move_to(slot_i.get_center())
        eval_step2 = Text("Paso 2: (2 < 3) -> true  [Itera]", font="Consolas", font_size=12, color="#6ee7b7", weight=BOLD).move_to(eval_step.get_center())

        self.play(
            ReplacementTransform(hud_it1, hud_it2),
            ReplacementTransform(slot_i1, slot_i2),
            ReplacementTransform(eval_step1, eval_step2),
            rate_func=smooth
        )
        self.wait(2.5)

        # ITERACIÓN 3: i = 2 -> ++i -> 3 (FIN DE BUCLE)
        hud_it3 = self.create_hud_footer(
            "FIN DE BUCLE", 
            "Condición (3 < 3) es FALSE: Se rompe el bucle y el flujo salta fuera de '}'.", 
            color=self.COLOR_RED
        )
        pointer_end = self.create_code_pointer(line6, color=self.COLOR_CYAN)
        slot_i3 = self.create_ram_slot("0x7FFEE0", "int", "i", "3", val_color="#ef4444", width=5.2).move_to(slot_i.get_center())
        eval_step3 = Text("Paso 3: (3 < 3) -> FALSE [Fin]", font="Consolas", font_size=12, color="#fca5a5", weight=BOLD).move_to(eval_step.get_center())

        self.play(
            ReplacementTransform(pointer_inc, pointer_end),
            ReplacementTransform(hud_it2, hud_it3),
            ReplacementTransform(slot_i2, slot_i3),
            ReplacementTransform(eval_step2, eval_step3),
            eval_box.animate.set_stroke(color="#ef4444", width=2.2),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 4: SÍNTESIS FINAL
        hud_final = self.create_hud_footer(
            "WHILE LOOP C++", 
            "El ciclo avanza mientras la condición sea true y finaliza apenas evalúe a false.", 
            color=self.COLOR_GREEN
        )
        self.play(
            FadeOut(pointer_end),
            ReplacementTransform(hud_it3, hud_final),
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
        "L05WhileLoop": "l05_while_loop.gif",
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
