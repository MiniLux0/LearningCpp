from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene

class ReturnValueScene(BaseLearningScene):
    def create_ram_slot(self, address: str, var_type: str, var_name: str, val_str: str, val_color: str = "#38bdf8", width: float = 4.8):
        """
        Crea una celda de memoria RAM estructurada de alta tecnología con Dirección, Tipo, Identificador y Valor.
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
            "La Mecánica de Return", 
            "Transferencia de output, destrucción de Scope y Dead Code"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.5)

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (Editor Realista 6.0 x 3.6)
        code_win, code_bg = self.create_code_window(width=6.0, height=3.6, title="doble.cpp")
        code_win.shift(LEFT * 3.3 + DOWN * 0.15)
        
        # Líneas con sintaxis hiper-realista tipo VS Code
        line1 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> '
            '<span foreground="#38bdf8"><b>calcularDoble</b></span>'
            '(<span foreground="#10b981">int</span> <span foreground="#fbbf24">n</span>) '
            '<span foreground="#c084fc">{</span>',
            font="Consolas", font_size=18
        )
        line2 = MarkupText(
            '<span foreground="#10b981"><b>int</b></span> res{<span foreground="#fbbf24">n</span> * 2};',
            font="Consolas", font_size=18, color="#f0f6fc"
        )
        line3 = MarkupText(
            '<span foreground="#c084fc"><b>return</b></span> res;',
            font="Consolas", font_size=18, color="#f0f6fc"
        )
        line4 = MarkupText(
            'std::cout &lt;&lt; "No corre";',
            font="Consolas", font_size=16, color="#64748b"
        )
        line5 = MarkupText(
            '<span foreground="#c084fc">}</span>',
            font="Consolas", font_size=18
        )
        
        # Sangría de 4 espacios (tab)
        INDENT = 0.50
        line1.move_to(ORIGIN)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.22).shift(RIGHT * INDENT)
        line3.next_to(line2, DOWN, aligned_edge=LEFT, buff=0.22)
        line4.next_to(line3, DOWN, aligned_edge=LEFT, buff=0.22)
        line5.next_to(line4, DOWN, aligned_edge=LEFT, buff=0.22).shift(LEFT * INDENT)

        code_lines = VGroup(line1, line2, line3, line4, line5)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.10)

        # 3. PANEL DERECHO: STACK RAM CON TARJETAS DE FRAME
        panel_win, panel_bg = self.create_card_panel(
            width=5.8, height=3.6, 
            title="Memoria RAM Stack", 
            subtitle="Frames de Ejecución y Scope"
        )
        panel_win.shift(RIGHT * 3.3 + DOWN * 0.15)
        
        # Frame calcularDoble(5) - Top (Scope secundario)
        f_top_box = RoundedRectangle(
            width=5.3, height=1.45, corner_radius=0.1,
            fill_color="#18122B", fill_opacity=0.85,
            stroke_color="#a855f7", stroke_width=1.5
        )
        f_top_title = Text("Frame: calcularDoble(5)", font="Consolas", font_size=11, color="#c084fc", weight=BOLD)
        f_top_title.next_to(f_top_box.get_top(), DOWN, buff=0.10)
        
        slot_n = self.create_ram_slot("0x7FFEE8", "int", "n", "5", val_color="#fbbf24", width=4.9)
        slot_res = self.create_ram_slot("0x7FFEE4", "int", "res", "10", val_color="#34d399", width=4.9)
        top_slots = VGroup(slot_n, slot_res).arrange(DOWN, buff=0.08).next_to(f_top_title, DOWN, buff=0.10)
        func_frame = VGroup(f_top_box, f_top_title, top_slots)
        
        # Frame main() - Bottom (Scope principal)
        f_main_box = RoundedRectangle(
            width=5.3, height=1.05, corner_radius=0.1,
            fill_color="#0b192c", fill_opacity=0.85,
            stroke_color="#38bdf8", stroke_width=1.5
        )
        f_main_title = Text("Frame: main()", font="Consolas", font_size=11, color="#7dd3fc", weight=BOLD)
        f_main_title.next_to(f_main_box.get_top(), DOWN, buff=0.10)
        
        slot_total = self.create_ram_slot("0x7FFEE0", "int", "total", "?", val_color="#94a3b8", width=4.9)
        slot_total.next_to(f_main_title, DOWN, buff=0.10)
        main_frame = VGroup(f_main_box, f_main_title, slot_total)
        
        stack_frames = VGroup(func_frame, main_frame).arrange(DOWN, buff=0.14)
        stack_frames.move_to(panel_bg.get_center() + DOWN * 0.15)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "SISTEMA", 
            "Invocando calcularDoble(5): Se crea el frame local en el Stack.", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(code_win, shift=RIGHT * 0.2),
            FadeIn(code_lines, shift=RIGHT * 0.2),
            FadeIn(panel_win, shift=LEFT * 0.2),
            FadeIn(stack_frames, shift=LEFT * 0.2),
            FadeIn(hud, shift=UP * 0.2),
            rate_func=smooth
        )
        self.wait(1.5)

        # FASE 1: CÁLCULO LOCAL (res = 10)
        hud_calc = self.create_hud_footer(
            "CÁLCULO", 
            "res{5 * 2}: El valor 10 se procesa y aloja temporalmente en 0x7FFEE4.", 
            color=self.COLOR_GOLD
        )
        pointer = self.create_code_pointer(line2, color=self.COLOR_GOLD)

        self.play(
            FadeIn(pointer, shift=RIGHT * 0.1),
            Indicate(slot_res[2], color="#34d399"),
            ReplacementTransform(hud, hud_calc),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 2: EJECUCIÓN DE RETURN & TRANSFERENCIA DE OUTPUT
        hud_ret = self.create_hud_footer(
            "RETURN", 
            "return res: Transfiere el valor 10 de vuelta al llamador (main) en 0x7FFEE0.", 
            color=self.COLOR_GREEN
        )
        pointer_ret = self.create_code_pointer(line3, color=self.COLOR_GREEN)
        
        # Paquete de datos luminoso viajero
        val_packet = RoundedRectangle(
            width=1.1, height=0.36, corner_radius=0.06, 
            fill_color="#064e3b", fill_opacity=0.95, 
            stroke_color="#10b981", stroke_width=2.0
        ).move_to(slot_res[2].get_center())
        val_packet_lbl = Text("10", font="Consolas", font_size=13, color="#6ee7b7", weight=BOLD).move_to(val_packet.get_center())
        packet_group = VGroup(val_packet, val_packet_lbl)
        
        # Celda actualizada de total en main()
        slot_total_filled = self.create_ram_slot("0x7FFEE0", "int", "total", "10", val_color="#10b981", width=4.9).move_to(slot_total.get_center())

        self.play(
            FadeOut(pointer),
            FadeIn(pointer_ret),
            ReplacementTransform(hud_calc, hud_ret),
            FadeIn(packet_group),
            rate_func=smooth
        )
        self.play(
            packet_group.animate.move_to(slot_total[2].get_center()),
            path_arc=-0.35,
            rate_func=smooth,
            run_time=1.3
        )
        self.play(
            FadeOut(packet_group),
            FadeOut(slot_total),
            FadeIn(slot_total_filled),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 3: DESTRUCCIÓN INMEDIATA DEL SCOPE (STACK POP)
        hud_pop = self.create_hud_footer(
            "STACK POP", 
            "Scope destruido: Las variables locales 'n' y 'res' son liberadas de la RAM.", 
            color=self.COLOR_PURPLE
        )
        badge_destroyed = self.create_badge(
            "FRAME DESTRUIDO (STACK POP) -> Scope liberado", 
            fill_color="#1a0a0d", stroke_color="#ef4444", text_color="#fca5a5", 
            width=5.1, height=0.45
        ).move_to(func_frame.get_center())

        self.play(
            ReplacementTransform(hud_ret, hud_pop),
            FadeOut(top_slots),
            FadeOut(f_top_title),
            FadeOut(f_top_box),
            FadeIn(badge_destroyed, shift=UP * 0.1),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 4: DEAD CODE / CÓDIGO INALCANZABLE
        hud_dead = self.create_hud_footer(
            "DEAD CODE", 
            "Código Inalcanzable: Cualquier instrucción bajo un return jamás se ejecutará.", 
            color=self.COLOR_RED
        )
        dead_line_cross = Line(
            start=line4.get_left() + LEFT * 0.05,
            end=line4.get_right() + RIGHT * 0.05,
            color="#ef4444",
            stroke_width=2.5
        )
        dead_badge = self.create_badge(
            "INALCANZABLE", 
            fill_color="#2b1704", stroke_color="#f59e0b", text_color="#fbbf24", 
            width=2.0, height=0.32
        ).next_to(line4, RIGHT, buff=0.15)

        self.play(
            ReplacementTransform(hud_pop, hud_dead),
            Create(dead_line_cross),
            FadeIn(dead_badge, shift=LEFT * 0.1),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 5: SÍNTESIS FINAL
        hud_final = self.create_hud_footer(
            "MECÁNICA C++", 
            "Return entrega el output al llamador y destruye inmediatamente el frame local.", 
            color=self.COLOR_GREEN
        )
        self.play(
            FadeOut(pointer_ret),
            ReplacementTransform(hud_dead, hud_final),
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
        "ReturnValueScene": "l02_return_value.gif",
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
