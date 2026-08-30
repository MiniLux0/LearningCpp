from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene

class PassByValueScene(BaseLearningScene):
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
            "El Modelo Pass-by-value", 
            "Clonación estricta de memoria y aislamiento físico en Stack RAM"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.5)

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (6.0 x 3.6)
        code_win, code_bg = self.create_code_window(width=6.0, height=3.6, title="copia.cpp")
        code_win.shift(LEFT * 3.3 + DOWN * 0.15)
        
        # Líneas con sintaxis hiper-realista tipo VS Code
        line1 = MarkupText(
            '<span foreground="#c084fc"><b>void</b></span> '
            '<span foreground="#38bdf8"><b>procesar</b></span>'
            '(<span foreground="#10b981">int</span> <span foreground="#fbbf24">copia</span>) '
            '<span foreground="#c084fc">{</span>',
            font="Consolas", font_size=17
        )
        line2 = MarkupText(
            '<span foreground="#fbbf24">copia</span> = <span foreground="#f59e0b">999</span>;',
            font="Consolas", font_size=17, color="#f0f6fc"
        )
        line3 = MarkupText(
            '<span foreground="#c084fc">}</span>',
            font="Consolas", font_size=17
        )
        line4 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> '
            '<span foreground="#38bdf8"><b>main</b></span>() '
            '<span foreground="#c084fc">{</span>',
            font="Consolas", font_size=17
        )
        line5 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> orig{<span foreground="#fbbf24">5</span>};',
            font="Consolas", font_size=17, color="#f0f6fc"
        )
        line6 = MarkupText(
            '<span foreground="#38bdf8">procesar</span>(orig);',
            font="Consolas", font_size=17, color="#f0f6fc"
        )
        line7 = MarkupText(
            'std::cout &lt;&lt; orig; <span foreground="#10b981">// Sigue siendo 5!</span>',
            font="Consolas", font_size=16, color="#f0f6fc"
        )
        line8 = MarkupText(
            '<span foreground="#c084fc">}</span>',
            font="Consolas", font_size=17
        )
        
        INDENT = 0.45
        line1.move_to(ORIGIN)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.16).shift(RIGHT * INDENT)
        line3.next_to(line2, DOWN, aligned_edge=LEFT, buff=0.16).shift(LEFT * INDENT)
        line4.next_to(line3, DOWN, aligned_edge=LEFT, buff=0.18)
        line5.next_to(line4, DOWN, aligned_edge=LEFT, buff=0.16).shift(RIGHT * INDENT)
        line6.next_to(line5, DOWN, aligned_edge=LEFT, buff=0.16)
        line7.next_to(line6, DOWN, aligned_edge=LEFT, buff=0.16)
        line8.next_to(line7, DOWN, aligned_edge=LEFT, buff=0.16).shift(LEFT * INDENT)

        code_lines = VGroup(line1, line2, line3, line4, line5, line6, line7, line8)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: STACK RAM CON TARJETAS DE FRAMES
        panel_win, panel_bg = self.create_card_panel(
            width=5.8, height=3.6, 
            title="Memoria RAM Stack", 
            subtitle="Direcciones Físicas Hexadecimales"
        )
        panel_win.shift(RIGHT * 3.3 + DOWN * 0.15)
        
        # Frame de main() - Bottom
        f_main_box = RoundedRectangle(
            width=5.3, height=1.1, corner_radius=0.1,
            fill_color="#0b192c", fill_opacity=0.85,
            stroke_color="#38bdf8", stroke_width=1.5
        )
        f_main_title = Text("Frame: main()", font="Consolas", font_size=11, color="#7dd3fc", weight=BOLD)
        f_main_title.next_to(f_main_box.get_top(), DOWN, buff=0.10)
        slot_orig = self.create_ram_slot("0x7FFEE0", "int", "orig", "5", val_color="#38bdf8", width=4.9)
        slot_orig.next_to(f_main_title, DOWN, buff=0.10)
        cell_orig = VGroup(f_main_box, f_main_title, slot_orig)

        # Frame de procesar() - Top
        f_clone_box = RoundedRectangle(
            width=5.3, height=1.1, corner_radius=0.1,
            fill_color="#18122B", fill_opacity=0.85,
            stroke_color="#a855f7", stroke_width=1.5
        )
        f_clone_title = Text("Frame: procesar()", font="Consolas", font_size=11, color="#c084fc", weight=BOLD)
        f_clone_title.next_to(f_clone_box.get_top(), DOWN, buff=0.10)
        slot_clone = self.create_ram_slot("0x7FFEE8", "int", "copia", "5", val_color="#fbbf24", width=4.9)
        slot_clone.next_to(f_clone_title, DOWN, buff=0.10)
        cell_clone = VGroup(f_clone_box, f_clone_title, slot_clone)

        mem_group = VGroup(cell_clone, cell_orig).arrange(DOWN, buff=0.25)
        mem_group.move_to(panel_bg.get_center() + DOWN * 0.15)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "SISTEMA", 
            "Declarando 'orig{5}' en el Scope principal (main) en 0x7FFEE0.", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(code_win, shift=RIGHT * 0.2),
            FadeIn(code_lines, shift=RIGHT * 0.2),
            FadeIn(panel_win, shift=LEFT * 0.2),
            FadeIn(cell_orig, shift=LEFT * 0.2),
            FadeIn(hud, shift=UP * 0.2),
            rate_func=smooth
        )
        self.wait(1.5)

        # FASE 1: INVOCACIÓN Y CLONACIÓN EN NUEVA DIRECCIÓN (PASS-BY-VALUE)
        hud_clone = self.create_hud_footer(
            "CLONACIÓN", 
            "procesar(orig): C++ clona el valor '5' en una nueva dirección (0x7FFEE8).", 
            color=self.COLOR_GOLD
        )
        pointer_call = self.create_code_pointer(line6, color=self.COLOR_CYAN)
        
        # Paquete de clonación viajando
        clone_packet = RoundedRectangle(
            width=1.1, height=0.36, corner_radius=0.06, 
            fill_color="#3d2c00", fill_opacity=0.95, 
            stroke_color="#f59e0b", stroke_width=2.0
        ).move_to(slot_orig[2].get_center())
        clone_packet_lbl = Text("5", font="Consolas", font_size=13, color="#fbbf24", weight=BOLD).move_to(clone_packet.get_center())
        clone_group = VGroup(clone_packet, clone_packet_lbl)

        self.play(
            FadeIn(pointer_call, shift=RIGHT * 0.1),
            ReplacementTransform(hud, hud_clone),
            FadeIn(f_clone_box),
            FadeIn(f_clone_title),
            FadeIn(clone_group),
            rate_func=smooth
        )
        self.play(
            clone_group.animate.move_to(slot_clone[2].get_center()),
            path_arc=-0.3,
            rate_func=smooth,
            run_time=1.3
        )
        self.play(
            FadeOut(clone_group),
            FadeIn(slot_clone),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 2: MUTACIÓN DEL CLON LOCAL
        hud_mutate = self.create_hud_footer(
            "MUTACIÓN LOCAL", 
            "copia = 999: Modifica exclusivamente la memoria temporal clonada en 0x7FFEE8.", 
            color=self.COLOR_PURPLE
        )
        pointer_mutate = self.create_code_pointer(line2, color=self.COLOR_PURPLE)
        slot_clone_mutated = self.create_ram_slot("0x7FFEE8", "int", "copia", "999", val_color="#f59e0b", width=4.9).move_to(slot_clone.get_center())

        self.play(
            ReplacementTransform(pointer_call, pointer_mutate),
            ReplacementTransform(hud_clone, hud_mutate),
            ReplacementTransform(slot_clone, slot_clone_mutated),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 3: DESTRUCCIÓN DEL CLON AL SALIR DE '}'
        hud_pop = self.create_hud_footer(
            "STACK POP", 
            "Al salir de '}', la variable 'copia' (0x7FFEE8) se destruye de la RAM.", 
            color=self.COLOR_RED
        )
        badge_pop = self.create_badge(
            "SCOPE DESTRUIDO (STACK POP) -> Clon liberado", 
            fill_color="#180a0a", stroke_color="#ef4444", text_color="#fca5a5", 
            width=5.1, height=0.45
        ).move_to(cell_clone.get_center())

        self.play(
            ReplacementTransform(hud_mutate, hud_pop),
            FadeOut(slot_clone_mutated),
            FadeOut(f_clone_title),
            FadeOut(f_clone_box),
            FadeIn(badge_pop, shift=UP * 0.1),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 4: DEMOSTRACIÓN DE INMUTABILIDAD EN MAIN
        hud_verify = self.create_hud_footer(
            "INMUTABILIDAD", 
            "std::cout << orig: La variable original en 0x7FFEE0 conserva intacto su valor 5.", 
            color=self.COLOR_GREEN
        )
        pointer_verify = self.create_code_pointer(line7, color=self.COLOR_GREEN)

        self.play(
            ReplacementTransform(hud_pop, hud_verify),
            ReplacementTransform(pointer_mutate, pointer_verify),
            slot_orig.animate.set_stroke(color="#10b981", width=2.0),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 5: SÍNTESIS FINAL
        hud_final = self.create_hud_footer(
            "PASS-BY-VALUE C++", 
            "Los parámetros primitivos son copias aisladas: Modificar el clon jamás afecta al original.", 
            color=self.COLOR_CYAN
        )
        self.play(
            FadeOut(pointer_verify),
            ReplacementTransform(hud_verify, hud_final),
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
        "PassByValueScene": "l04_pass_by_value.gif",
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
