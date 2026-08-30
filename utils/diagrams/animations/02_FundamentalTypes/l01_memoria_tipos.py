from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene

class MemoriaTipos(BaseLearningScene):
    def create_ram_slot(self, address: str, var_type: str, var_name: str, val_str: str, val_color: str = "#38bdf8", width: float = 5.2):
        bg = RoundedRectangle(
            width=width, height=0.48, corner_radius=0.08, 
            fill_color="#0f172a", fill_opacity=0.9, 
            stroke_color="#334155", stroke_width=1.2
        )
        addr_lbl = Text(address, font="Consolas", font_size=10, color="#64748b")
        type_lbl = Text(var_type, font="Consolas", font_size=11, color=val_color, weight=BOLD)
        name_lbl = Text(var_name, font="Consolas", font_size=13, color="#f1f5f9", weight=BOLD)
        
        left_group = VGroup(addr_lbl, type_lbl, name_lbl).arrange(RIGHT, buff=0.14)
        left_group.next_to(bg.get_left(), RIGHT, buff=0.15)
        
        val_box = RoundedRectangle(
            width=1.2, height=0.36, corner_radius=0.06, 
            fill_color="#1e293b", fill_opacity=0.95, 
            stroke_color=val_color, stroke_width=1.5
        )
        val_box.next_to(bg.get_right(), LEFT, buff=0.12)
        val_lbl = Text(val_str, font="Consolas", font_size=12, color=val_color, weight=BOLD).move_to(val_box.get_center())
        val_group = VGroup(val_box, val_lbl)
        
        return VGroup(bg, left_group, val_group)

    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "Tipos Fundamentales en Memoria", 
            "Tamaño en Bytes y estructura física en el Stack RAM"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.5)

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (6.0 x 3.6)
        code_win, code_bg = self.create_code_window(width=6.0, height=3.6, title="tipos.cpp")
        code_win.shift(LEFT * 3.3 + DOWN * 0.15)
        
        line1 = MarkupText(
            '<span foreground="#10b981"><b>bool</b></span> activo{<span foreground="#38bdf8">true</span>};    <span foreground="#64748b">// 1 Byte</span>',
            font="Consolas", font_size=15, color="#f0f6fc"
        )
        line2 = MarkupText(
            '<span foreground="#10b981"><b>char</b></span> letra{<span foreground="#fbbf24">\'Z\'</span>};      <span foreground="#64748b">// 1 Byte</span>',
            font="Consolas", font_size=15, color="#f0f6fc"
        )
        line3 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> vidas{<span foreground="#fbbf24">100</span>};       <span foreground="#64748b">// 4 Bytes</span>',
            font="Consolas", font_size=15, color="#f0f6fc"
        )
        line4 = MarkupText(
            '<span foreground="#10b981"><b>double</b></span> pi{<span foreground="#fbbf24">3.14159</span>};   <span foreground="#64748b">// 8 Bytes</span>',
            font="Consolas", font_size=15, color="#f0f6fc"
        )

        code_lines = VGroup(line1, line2, line3, line4).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.10)

        # 3. PANEL DERECHO: STACK RAM CON CELDAS FÍSICAS
        panel_win, panel_bg = self.create_card_panel(
            width=5.8, height=3.6, 
            title="Memoria RAM (Stack)", 
            subtitle="Asignación Física de Bytes"
        )
        panel_win.shift(RIGHT * 3.3 + DOWN * 0.15)
        
        slot_bool = self.create_ram_slot("0x7FFE00", "bool(1B)", "activo", "true", val_color="#10b981", width=5.2)
        slot_char = self.create_ram_slot("0x7FFE01", "char(1B)", "letra", "'Z'", val_color="#fbbf24", width=5.2)
        slot_int  = self.create_ram_slot("0x7FFE04", "int(4B)", "vidas", "100", val_color="#38bdf8", width=5.2)
        slot_dbl  = self.create_ram_slot("0x7FFE08", "double(8B)", "pi", "3.14159", val_color="#c084fc", width=5.2)

        stack_slots = VGroup(slot_bool, slot_char, slot_int, slot_dbl).arrange(DOWN, buff=0.14)
        stack_slots.move_to(panel_bg.get_center() + DOWN * 0.15)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "SISTEMA", 
            "Asignando variables primitivas en el Stack RAM con Inicialización Uniforme {}.", 
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

        # FASE 1: BOOL & CHAR (1 BYTE C/U)
        hud_1b = self.create_hud_footer(
            "1 BYTE", 
            "bool y char ocupan exactamente 1 Byte (8 bits) cada uno en direcciones consecutivas.", 
            color=self.COLOR_GREEN
        )
        pointer1 = self.create_code_pointer(line1, color=self.COLOR_GREEN)

        self.play(
            FadeIn(pointer1, shift=RIGHT * 0.1),
            FadeIn(slot_bool, shift=LEFT * 0.15),
            ReplacementTransform(hud, hud_1b),
            rate_func=smooth
        )
        self.wait(0.8)

        pointer2 = self.create_code_pointer(line2, color=self.COLOR_GOLD)
        self.play(
            ReplacementTransform(pointer1, pointer2),
            FadeIn(slot_char, shift=LEFT * 0.15),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 2: INT (4 BYTES)
        hud_int = self.create_hud_footer(
            "4 BYTES (INT)", 
            "int ocupa 4 Bytes (32 bits), alineándose en memoria de 4 en 4 (0x7FFE04).", 
            color=self.COLOR_CYAN
        )
        pointer3 = self.create_code_pointer(line3, color=self.COLOR_CYAN)

        self.play(
            ReplacementTransform(pointer2, pointer3),
            FadeIn(slot_int, shift=LEFT * 0.15),
            ReplacementTransform(hud_1b, hud_int),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 3: DOUBLE (8 BYTES)
        hud_dbl = self.create_hud_footer(
            "8 BYTES (DOUBLE)", 
            "double ocupa 8 Bytes (64 bits) en formato IEEE 754 de alta precisión decimal.", 
            color=self.COLOR_PURPLE
        )
        pointer4 = self.create_code_pointer(line4, color=self.COLOR_PURPLE)

        self.play(
            ReplacementTransform(pointer3, pointer4),
            FadeIn(slot_dbl, shift=LEFT * 0.15),
            ReplacementTransform(hud_int, hud_dbl),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 4: SÍNTESIS FINAL
        hud_final = self.create_hud_footer(
            "TIPADO ESTÁTICO", 
            "Cada tipo define de forma inmutable el espacio de memoria y la interpretación binaria.", 
            color=self.COLOR_GREEN
        )
        self.play(
            FadeOut(pointer4),
            ReplacementTransform(hud_dbl, hud_final),
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
        "MemoriaTipos": "l01_memoria_tipos.gif",
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
