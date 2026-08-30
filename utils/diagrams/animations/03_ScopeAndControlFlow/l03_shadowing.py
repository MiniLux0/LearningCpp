from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene

class L03VariableShadowing(BaseLearningScene):
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
            "Sombreado de Variables (Variable Shadowing)", 
            "Prioridad de ámbitos locales y ocultación en Stack RAM"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.5)

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (6.0 x 3.6)
        code_win, code_bg = self.create_code_window(width=6.0, height=3.6, title="sombras.cpp")
        code_win.shift(LEFT * 3.3 + DOWN * 0.15)
        
        line1 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> oro{<span foreground="#38bdf8">100</span>}; <span foreground="#64748b">// Externo</span>',
            font="Consolas", font_size=16, color="#f0f6fc"
        )
        line2 = MarkupText(
            '<span foreground="#c084fc">{</span>',
            font="Consolas", font_size=16
        )
        line3 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> oro{<span foreground="#fbbf24">50</span>}; <span foreground="#fbbf24">// Sombra</span>',
            font="Consolas", font_size=16, color="#f0f6fc"
        )
        line4 = MarkupText(
            'std::cout &lt;&lt; oro; <span foreground="#fbbf24">// 50</span>',
            font="Consolas", font_size=16, color="#f0f6fc"
        )
        line5 = MarkupText(
            '<span foreground="#c084fc">}</span>',
            font="Consolas", font_size=16
        )
        line6 = MarkupText(
            'std::cout &lt;&lt; oro; <span foreground="#38bdf8">// 100</span>',
            font="Consolas", font_size=16, color="#f0f6fc"
        )
        
        INDENT = 0.45
        line1.move_to(ORIGIN)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.16)
        line3.next_to(line2, DOWN, aligned_edge=LEFT, buff=0.16).shift(RIGHT * INDENT)
        line4.next_to(line3, DOWN, aligned_edge=LEFT, buff=0.16)
        line5.next_to(line4, DOWN, aligned_edge=LEFT, buff=0.16).shift(LEFT * INDENT)
        line6.next_to(line5, DOWN, aligned_edge=LEFT, buff=0.16)

        code_lines = VGroup(line1, line2, line3, line4, line5, line6)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: STACK RAM CON TARJETAS DE ÁMBITO
        panel_win, panel_bg = self.create_card_panel(
            width=5.8, height=3.6, 
            title="Memoria RAM (Stack)", 
            subtitle="Resolución de Variables por Ámbito"
        )
        panel_win.shift(RIGHT * 3.3 + DOWN * 0.15)
        
        # Scope Externo
        f_ext_box = RoundedRectangle(
            width=5.3, height=1.1, corner_radius=0.1,
            fill_color="#0b192c", fill_opacity=0.85,
            stroke_color="#38bdf8", stroke_width=1.5
        )
        f_ext_title = Text("Ámbito Externo", font="Consolas", font_size=11, color="#7dd3fc", weight=BOLD)
        f_ext_title.next_to(f_ext_box.get_top(), DOWN, buff=0.10)
        slot_ext = self.create_ram_slot("0x7FFE00", "int", "oro", "100", val_color="#38bdf8", width=4.9)
        slot_ext.next_to(f_ext_title, DOWN, buff=0.10)
        card_ext = VGroup(f_ext_box, f_ext_title, slot_ext)

        # Scope Interno (Sombra)
        f_inn_box = RoundedRectangle(
            width=5.3, height=1.1, corner_radius=0.1,
            fill_color="#18122B", fill_opacity=0.85,
            stroke_color="#fbbf24", stroke_width=1.5
        )
        f_inn_title = Text("Ámbito Interno (Sombra)", font="Consolas", font_size=11, color="#fde047", weight=BOLD)
        f_inn_title.next_to(f_inn_box.get_top(), DOWN, buff=0.10)
        slot_inn = self.create_ram_slot("0x7FFE04", "int", "oro", "50", val_color="#fbbf24", width=4.9)
        slot_inn.next_to(f_inn_title, DOWN, buff=0.10)
        card_inn = VGroup(f_inn_box, f_inn_title, slot_inn)

        cards = VGroup(card_inn, card_ext).arrange(DOWN, buff=0.25)
        cards.move_to(panel_bg.get_center() + DOWN * 0.15)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "SISTEMA", 
            "Declarando variable 'oro{100}' en el ámbito externo (0x7FFE00).", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(code_win, shift=RIGHT * 0.2),
            FadeIn(code_lines, shift=RIGHT * 0.2),
            FadeIn(panel_win, shift=LEFT * 0.2),
            FadeIn(card_ext, shift=LEFT * 0.2),
            FadeIn(hud, shift=UP * 0.2),
            rate_func=smooth
        )
        self.wait(1.5)

        # FASE 1: ENTRADA AL BLOQUE Y SHADOWING
        hud_shadow = self.create_hud_footer(
            "SHADOWING", 
            "Dentro de '{}', se declara 'oro{50}'. Oculta temporalmente a la externa.", 
            color=self.COLOR_GOLD
        )
        pointer_shadow = self.create_code_pointer(line3, color=self.COLOR_GOLD)

        self.play(
            FadeIn(pointer_shadow, shift=RIGHT * 0.1),
            FadeIn(card_inn, shift=DOWN * 0.15),
            card_ext.animate.set_opacity(0.35),
            ReplacementTransform(hud, hud_shadow),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 2: USO DE LA VARIABLE SOMBRA
        pointer_print_inn = self.create_code_pointer(line4, color=self.COLOR_GOLD)
        self.play(
            ReplacementTransform(pointer_shadow, pointer_print_inn),
            rate_func=smooth
        )
        self.wait(2.0)

        # FASE 3: SALIDA DEL BLOQUE (STACK POP Y DES-SOMBREADO)
        hud_pop = self.create_hud_footer(
            "FIN DE BLOQUE", 
            "Al alcanzar '}', la variable sombra se destruye y la externa recupera visibilidad.", 
            color=self.COLOR_CYAN
        )
        pointer_print_ext = self.create_code_pointer(line6, color=self.COLOR_CYAN)
        badge_pop = self.create_badge(
            "SOMBRA DESTRUIDA (STACK POP) -> Scope liberado", 
            fill_color="#180a0a", stroke_color="#ef4444", text_color="#fca5a5", 
            width=5.1, height=0.45
        ).move_to(card_inn.get_center())

        self.play(
            ReplacementTransform(pointer_print_inn, pointer_print_ext),
            ReplacementTransform(hud_shadow, hud_pop),
            FadeOut(card_inn),
            FadeIn(badge_pop, shift=UP * 0.1),
            card_ext.animate.set_opacity(1.0),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 4: SÍNTESIS FINAL
        hud_final = self.create_hud_footer(
            "SHADOWING C++", 
            "El compilador siempre resuelve hacia el ámbito más interno y cercano.", 
            color=self.COLOR_GREEN
        )
        self.play(
            FadeOut(pointer_print_ext),
            ReplacementTransform(hud_pop, hud_final),
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
        "L03VariableShadowing": "l03_variable_shadowing.gif",
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
