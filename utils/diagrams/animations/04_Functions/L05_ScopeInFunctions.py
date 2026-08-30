from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene

class ScopeInFunctionsScene(BaseLearningScene):
    def create_ram_slot(self, address: str, var_type: str, var_name: str, val_str: str, val_color: str = "#38bdf8", width: float = 4.9):
        """
        Crea una ranura estructurada de memoria física RAM con Dirección, Tipo, Identificador y Valor.
        """
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
            "Aislamiento de Scope e Identificadores", 
            "Coexistencia de variables homónimas y límites de memoria"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.5)

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (6.0 x 3.6)
        code_win, code_bg = self.create_code_window(width=6.0, height=3.6, title="alcance.cpp")
        code_win.shift(LEFT * 3.3 + DOWN * 0.15)
        
        # Líneas con sintaxis hiper-realista tipo VS Code
        line1 = MarkupText(
            '<span foreground="#c084fc"><b>void</b></span> '
            '<span foreground="#38bdf8"><b>cargarP1</b></span>() '
            '<span foreground="#c084fc">{</span>',
            font="Consolas", font_size=16
        )
        line2 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> oro{<span foreground="#fbbf24">500</span>};',
            font="Consolas", font_size=16, color="#f0f6fc"
        )
        line3 = MarkupText(
            '<span foreground="#c084fc">}</span>',
            font="Consolas", font_size=16
        )
        line4 = MarkupText(
            '<span foreground="#c084fc"><b>void</b></span> '
            '<span foreground="#a855f7"><b>cargarP2</b></span>() '
            '<span foreground="#c084fc">{</span>',
            font="Consolas", font_size=16
        )
        line5 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> oro{<span foreground="#fbbf24">10</span>};',
            font="Consolas", font_size=16, color="#f0f6fc"
        )
        line6 = MarkupText(
            '<span foreground="#c084fc">}</span>',
            font="Consolas", font_size=16
        )
        line7 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> '
            '<span foreground="#38bdf8"><b>main</b></span>() '
            '<span foreground="#c084fc">{</span>',
            font="Consolas", font_size=16
        )
        line8 = MarkupText(
            '<span foreground="#64748b">// std::cout &lt;&lt; oro;</span>',
            font="Consolas", font_size=15, color="#64748b"
        )
        line9 = MarkupText(
            '<span foreground="#c084fc">}</span>',
            font="Consolas", font_size=16
        )
        
        INDENT = 0.45
        line1.move_to(ORIGIN)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.14).shift(RIGHT * INDENT)
        line3.next_to(line2, DOWN, aligned_edge=LEFT, buff=0.14).shift(LEFT * INDENT)
        line4.next_to(line3, DOWN, aligned_edge=LEFT, buff=0.16)
        line5.next_to(line4, DOWN, aligned_edge=LEFT, buff=0.14).shift(RIGHT * INDENT)
        line6.next_to(line5, DOWN, aligned_edge=LEFT, buff=0.14).shift(LEFT * INDENT)
        line7.next_to(line6, DOWN, aligned_edge=LEFT, buff=0.16)
        line8.next_to(line7, DOWN, aligned_edge=LEFT, buff=0.14).shift(RIGHT * INDENT)
        line9.next_to(line8, DOWN, aligned_edge=LEFT, buff=0.14).shift(LEFT * INDENT)

        code_lines = VGroup(line1, line2, line3, line4, line5, line6, line7, line8, line9)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: AISLAMIENTO EN STACK RAM CON TARJETAS DE SCOPE
        panel_win, panel_bg = self.create_card_panel(
            width=5.8, height=3.6, 
            title="Aislamiento en RAM", 
            subtitle="Direcciones de Memoria Independientes"
        )
        panel_win.shift(RIGHT * 3.3 + DOWN * 0.15)
        
        # Scope cargarP1() - Top
        f_p1_box = RoundedRectangle(
            width=5.3, height=1.1, corner_radius=0.1,
            fill_color="#0b192c", fill_opacity=0.85,
            stroke_color="#38bdf8", stroke_width=1.5
        )
        f_p1_title = Text("Scope: cargarP1()", font="Consolas", font_size=11, color="#7dd3fc", weight=BOLD)
        f_p1_title.next_to(f_p1_box.get_top(), DOWN, buff=0.10)
        slot_p1 = self.create_ram_slot("0x7FFEE0", "int", "oro", "500", val_color="#38bdf8", width=4.9)
        slot_p1.next_to(f_p1_title, DOWN, buff=0.10)
        card_p1 = VGroup(f_p1_box, f_p1_title, slot_p1)

        # Scope cargarP2() - Bottom
        f_p2_box = RoundedRectangle(
            width=5.3, height=1.1, corner_radius=0.1,
            fill_color="#18122B", fill_opacity=0.85,
            stroke_color="#a855f7", stroke_width=1.5
        )
        f_p2_title = Text("Scope: cargarP2()", font="Consolas", font_size=11, color="#c084fc", weight=BOLD)
        f_p2_title.next_to(f_p2_box.get_top(), DOWN, buff=0.10)
        slot_p2 = self.create_ram_slot("0x7FFEE8", "int", "oro", "10", val_color="#fbbf24", width=4.9)
        slot_p2.next_to(f_p2_title, DOWN, buff=0.10)
        card_p2 = VGroup(f_p2_box, f_p2_title, slot_p2)

        cards = VGroup(card_p1, card_p2).arrange(DOWN, buff=0.25)
        cards.move_to(panel_bg.get_center() + DOWN * 0.15)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "SISTEMA", 
            "Analizando dos funciones independientes con variables homónimas ('oro').", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(code_win, shift=RIGHT * 0.2),
            FadeIn(code_lines, shift=RIGHT * 0.2),
            FadeIn(panel_win, shift=LEFT * 0.2),
            FadeIn(cards, shift=LEFT * 0.2),
            FadeIn(hud, shift=UP * 0.2),
            rate_func=smooth
        )
        self.wait(1.5)

        # FASE 1: COEXISTENCIA EN RAM
        hud_coexist = self.create_hud_footer(
            "COEXISTENCIA", 
            "Ambas variables se llaman 'oro', pero residen en direcciones físicas distintas.", 
            color=self.COLOR_GOLD
        )
        pointer_p1 = self.create_code_pointer(line2, color=self.COLOR_CYAN)

        self.play(
            FadeIn(pointer_p1, shift=RIGHT * 0.1),
            f_p1_box.animate.set_stroke(color="#38bdf8", width=2.2),
            ReplacementTransform(hud, hud_coexist),
            rate_func=smooth
        )
        self.wait(3.0)

        pointer_p2 = self.create_code_pointer(line5, color=self.COLOR_PURPLE)
        self.play(
            ReplacementTransform(pointer_p1, pointer_p2),
            f_p2_box.animate.set_stroke(color="#c084fc", width=2.2),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 2: INTENTO DE FUGA DE SCOPE & DIAGNÓSTICO ESTRUCTURADO
        hud_leak = self.create_hud_footer(
            "FUGA ILEGAL", 
            "std::cout << oro en main(): Error. main() no tiene visibilidad sobre Scopes hijos.", 
            color=self.COLOR_RED
        )
        pointer_leak = self.create_code_pointer(line8, color=self.COLOR_RED)
        
        # Tarjeta de Diagnóstico Estructurada de Alto Contraste
        diag_box = RoundedRectangle(
            width=5.3, height=1.4, corner_radius=0.1, 
            fill_color="#0b0f19", fill_opacity=0.98, 
            stroke_color="#ef4444", stroke_width=1.5
        )
        diag_title = Text("ERROR DE COMPILACION:", font="Consolas", font_size=12, color="#ef4444", weight=BOLD)
        diag_code = Text("std::cout << oro;", font="Consolas", font_size=13, color="#f8fafc", weight=BOLD)
        diag_caret = Text("             ^^^", font="Consolas", font_size=12, color="#f87171", weight=BOLD)
        diag_reason = Text("'oro' no declarado en este scope (main)", font="Consolas", font_size=11, color="#fbbf24", weight=BOLD)

        diag_content = VGroup(diag_title, diag_code, diag_caret, diag_reason).arrange(DOWN, aligned_edge=LEFT, buff=0.09)
        diag_content.move_to(diag_box.get_center())
        diag_card = VGroup(diag_box, diag_content).move_to(cards.get_center())

        self.play(
            ReplacementTransform(pointer_p2, pointer_leak),
            ReplacementTransform(hud_coexist, hud_leak),
            FadeOut(cards),
            FadeIn(diag_card, shift=UP * 0.1),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 3: SÍNTESIS FINAL
        hud_final = self.create_hud_footer(
            "SCOPE LOCAL", 
            "Aislamiento blindado: Cada bloque '{}' delimita su propia memoria física.", 
            color=self.COLOR_GREEN
        )
        self.play(
            FadeOut(pointer_leak),
            ReplacementTransform(hud_leak, hud_final),
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
        "ScopeInFunctionsScene": "l05_function_scope.gif",
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
