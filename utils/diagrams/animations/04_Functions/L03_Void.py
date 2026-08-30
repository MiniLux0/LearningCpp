from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene

class VoidActionScene(BaseLearningScene):
    def construct(self):
        # 1. ENCABEZADO SUPERIOR
        header = self.create_header(
            "Funciones Void (Acción Pura)", 
            "Efectos Secundarios (I/O) sin transferencia de valor a memoria"
        )
        self.play(FadeIn(header, shift=DOWN * 0.2), rate_func=smooth)
        self.wait(0.5)

        # 2. PANEL IZQUIERDO: VENTANA DE CÓDIGO IDE (Editor Realista 6.0 x 3.6)
        code_win, code_bg = self.create_code_window(width=6.0, height=3.6, title="alerta.cpp")
        code_win.shift(LEFT * 3.3 + DOWN * 0.15)
        
        # Líneas con sintaxis hiper-realista tipo VS Code
        line1 = MarkupText(
            '<span foreground="#c084fc"><b>void</b></span> '
            '<span foreground="#38bdf8"><b>imprimirAlerta</b></span>() '
            '<span foreground="#c084fc">{</span>',
            font="Consolas", font_size=17
        )
        line2 = MarkupText(
            'std::cout &lt;&lt; <span foreground="#f59e0b">"Peligro!\\n"</span>;',
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
            '<span foreground="#38bdf8">imprimirAlerta</span>();',
            font="Consolas", font_size=17, color="#f0f6fc"
        )
        line6 = MarkupText(
            '<span foreground="#64748b">// int x{imprimirAlerta()};</span>',
            font="Consolas", font_size=15, color="#64748b"
        )
        line7 = MarkupText(
            '<span foreground="#c084fc">}</span>',
            font="Consolas", font_size=17
        )
        
        # Sangría de 4 espacios (tab)
        INDENT = 0.45
        line1.move_to(ORIGIN)
        line2.next_to(line1, DOWN, aligned_edge=LEFT, buff=0.18).shift(RIGHT * INDENT)
        line3.next_to(line2, DOWN, aligned_edge=LEFT, buff=0.18).shift(LEFT * INDENT)
        line4.next_to(line3, DOWN, aligned_edge=LEFT, buff=0.20)
        line5.next_to(line4, DOWN, aligned_edge=LEFT, buff=0.18).shift(RIGHT * INDENT)
        line6.next_to(line5, DOWN, aligned_edge=LEFT, buff=0.18)
        line7.next_to(line6, DOWN, aligned_edge=LEFT, buff=0.18).shift(LEFT * INDENT)

        code_lines = VGroup(line1, line2, line3, line4, line5, line6, line7)
        code_lines.move_to(code_bg.get_center() + DOWN * 0.08)

        # 3. PANEL DERECHO: CONSOLA DE ALTA FIDELIDAD Y TARJETA DE ESTADO
        panel_win, panel_bg = self.create_card_panel(
            width=5.8, height=3.6, 
            title="Consola de Salida & Estado", 
            subtitle="Efecto Secundario en Hardware"
        )
        panel_win.shift(RIGHT * 3.3 + DOWN * 0.15)
        
        # Terminal de Consola Realista de Alto Impacto
        term_box = RoundedRectangle(
            width=5.3, height=1.45, corner_radius=0.1,
            fill_color="#030712", fill_opacity=0.98,
            stroke_color="#38bdf8", stroke_width=1.5
        )
        term_header_bg = RoundedRectangle(
            width=5.3, height=0.32, corner_radius=0.1,
            fill_color="#0f172a", fill_opacity=1.0,
            stroke_color="#38bdf8", stroke_width=1.2
        ).next_to(term_box.get_top(), DOWN, buff=0)
        
        dot_r = Dot(radius=0.04, color="#ef4444")
        dot_y = Dot(radius=0.04, color="#f59e0b")
        dot_g = Dot(radius=0.04, color="#10b981")
        dots = VGroup(dot_r, dot_y, dot_g).arrange(RIGHT, buff=0.08).next_to(term_header_bg.get_left(), RIGHT, buff=0.15)
        term_title = Text("bash - stdout (pantalla)", font="Consolas", font_size=10, color="#94a3b8").next_to(dots, RIGHT, buff=0.15)
        
        prompt = Text("$ ./alerta", font="Consolas", font_size=13, color="#38bdf8").next_to(term_header_bg, DOWN, buff=0.16).align_to(term_box, LEFT).shift(RIGHT * 0.25)
        stdout_msg = Text("Peligro!", font="Consolas", font_size=16, color="#f87171", weight=BOLD).next_to(prompt, DOWN, buff=0.12).align_to(term_box, LEFT).shift(RIGHT * 0.25)
        
        terminal_group = VGroup(term_box, term_header_bg, dots, term_title, prompt)
        
        # Badge de Retorno Void (Fondo oscuro, texto blanco de alto contraste, sin destellos)
        badge_void = self.create_badge(
            "Retorno: void -> 0 Bytes inyectados a RAM", 
            fill_color="#0f172a", stroke_color="#a855f7", text_color="#f1f5f9", 
            width=5.3, height=0.48
        )
        
        right_group = VGroup(terminal_group, badge_void).arrange(DOWN, buff=0.25)
        right_group.move_to(panel_bg.get_center() + DOWN * 0.15)

        # 4. HUD INFERIOR INICIAL
        hud = self.create_hud_footer(
            "SISTEMA", 
            "Iniciando flujo en main(): Evaluando invocación de rutina void.", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(code_win, shift=RIGHT * 0.2),
            FadeIn(code_lines, shift=RIGHT * 0.2),
            FadeIn(panel_win, shift=LEFT * 0.2),
            FadeIn(right_group, shift=LEFT * 0.2),
            FadeIn(hud, shift=UP * 0.2),
            rate_func=smooth
        )
        self.wait(1.5)

        # FASE 1: TRANSFERENCIA DE CONTROL A LA RUTINA
        hud_call = self.create_hud_footer(
            "INVOCACIÓN", 
            "imprimirAlerta(): El flujo salta al cuerpo de la rutina void para ejecutarla.", 
            color=self.COLOR_CYAN
        )
        pointer = self.create_code_pointer(line5, color=self.COLOR_CYAN)
        pointer_func = self.create_code_pointer(line2, color=self.COLOR_PURPLE)

        self.play(
            FadeIn(pointer, shift=RIGHT * 0.1),
            ReplacementTransform(hud, hud_call),
            rate_func=smooth
        )
        self.wait(0.6)
        self.play(
            ReplacementTransform(pointer, pointer_func),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 2: EFECTO SECUNDARIO (SIDE EFFECT EN CONSOLA - SIN ESCALAR CAJAS)
        hud_side = self.create_hud_footer(
            "SIDE EFFECT", 
            "std::cout: Se emite texto a la terminal sin escribir datos en la memoria RAM.", 
            color=self.COLOR_GOLD
        )
        self.play(
            ReplacementTransform(hud_call, hud_side),
            FadeIn(stdout_msg, shift=RIGHT * 0.15),
            term_box.animate.set_stroke(color="#f87171", width=2.2),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 3: RETORNO DE CONTROL SIN PAQUETE DE DATOS (ILUMINACIÓN LIMPIA SIN ESCALADO)
        hud_ret = self.create_hud_footer(
            "CIERRE DE SCOPE", 
            "Al alcanzar '}', el flujo regresa a main() transportando CERO datos de retorno.", 
            color=self.COLOR_PURPLE
        )
        pointer_ret = self.create_code_pointer(line5, color=self.COLOR_GREEN)

        self.play(
            ReplacementTransform(hud_side, hud_ret),
            ReplacementTransform(pointer_func, pointer_ret),
            badge_void.animate.set_stroke(color="#c084fc", width=2.2),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 4: TRAMPA DE ASIGNACIÓN ILEGAL & DIAGNÓSTICO ESTRUCTURADO DE ALTO CONTRASTE
        hud_err = self.create_hud_footer(
            "ERROR FATAL", 
            "int x{imprimirAlerta()}: Error del compilador. Es ilegal atrapar un flujo void.", 
            color=self.COLOR_RED
        )
        pointer_err = self.create_code_pointer(line6, color=self.COLOR_RED)
        
        # Tarjeta de Diagnóstico Limpia, Elegante y de Máximo Contraste (Cero Cajas Rosas o Deformadas)
        diag_box = RoundedRectangle(
            width=5.3, height=1.4, corner_radius=0.1, 
            fill_color="#0b0f19", fill_opacity=0.98, 
            stroke_color="#ef4444", stroke_width=1.5
        )
        diag_title = Text("ERROR DE COMPILACION:", font="Consolas", font_size=12, color="#ef4444", weight=BOLD)
        diag_code = Text("int x{imprimirAlerta()};", font="Consolas", font_size=13, color="#f8fafc", weight=BOLD)
        diag_caret = Text("     ^^^^^^^^^^^^^^^^", font="Consolas", font_size=12, color="#f87171", weight=BOLD)
        diag_reason = Text("void = 0 Bytes (Ilegal asignar a variable)", font="Consolas", font_size=11, color="#fbbf24", weight=BOLD)

        diag_content = VGroup(diag_title, diag_code, diag_caret, diag_reason).arrange(DOWN, aligned_edge=LEFT, buff=0.09)
        diag_content.move_to(diag_box.get_center())
        diag_card = VGroup(diag_box, diag_content).move_to(badge_void.get_center())

        self.play(
            ReplacementTransform(hud_ret, hud_err),
            ReplacementTransform(pointer_ret, pointer_err),
            FadeOut(badge_void),
            FadeIn(diag_card, shift=UP * 0.1),
            rate_func=smooth
        )
        self.wait(3.0)

        # FASE 5: SÍNTESIS FINAL
        hud_final = self.create_hud_footer(
            "VOID EN C++", 
            "Acción Pura: Invoca funciones void como instrucciones independientes.", 
            color=self.COLOR_GREEN
        )
        self.play(
            FadeOut(pointer_err),
            ReplacementTransform(hud_err, hud_final),
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
        "VoidActionScene": "l03_void_action.gif",
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
