from manim import *
import sys
import os

sys.path.append(os.path.abspath("utils/diagrams/core"))
from manim_base import BaseLearningScene

class HeroReadmeShowcase(BaseLearningScene):
    def construct(self):
        # =====================================================================
        # ESCENA 1: BIENVENIDA OFICIAL & PRESENTACIÓN DEL AUTOR
        # =====================================================================
        logo_box = RoundedRectangle(
            width=2.4, height=2.4, corner_radius=0.45,
            fill_color="#0b1120", fill_opacity=0.98,
            stroke_color="#38bdf8", stroke_width=2.8
        ).move_to(UP * 1.35)

        logo_glow = RoundedRectangle(
            width=2.55, height=2.55, corner_radius=0.50,
            fill_opacity=0, stroke_color="#10b981", stroke_width=1.2, stroke_opacity=0.6
        ).move_to(logo_box.get_center())

        logo_txt = MarkupText(
            '<span foreground="#38bdf8"><b>C</b></span><span foreground="#10b981"><b>++</b></span>',
            font="Consolas", font_size=58
        ).move_to(logo_box.get_center())
        logo_grp = VGroup(logo_glow, logo_box, logo_txt)

        title_main = MarkupText(
            '<b>Learning</b><span foreground="#38bdf8"><b>Cpp</b></span>',
            font="Consolas", font_size=46, color="#f8fafc"
        ).move_to(DOWN * 0.25)

        tagline = Text(
            "El Curso Interactivo y Visual de C++ Moderno",
            font="Consolas", font_size=18, color="#cbd5e1", weight=BOLD
        ).move_to(DOWN * 0.90)

        badge_std = RoundedRectangle(
            width=7.8, height=0.42, corner_radius=0.21,
            fill_color="#0f172a", fill_opacity=0.95,
            stroke_color="#334155", stroke_width=1.2
        ).move_to(DOWN * 1.45)
        badge_txt = Text(
            "ESTANDAR C++17 BASE · EVOLUCION C++20 · METODOLOGIA BREAK-FIRST",
            font="Consolas", font_size=10, color="#38bdf8", weight=BOLD
        ).move_to(badge_std.get_center())
        std_grp = VGroup(badge_std, badge_txt)

        author_box = RoundedRectangle(
            width=6.4, height=0.54, corner_radius=0.27,
            fill_color="#062e24", fill_opacity=0.95,
            stroke_color="#10b981", stroke_width=1.6
        ).move_to(DOWN * 2.05)

        author_txt = MarkupText(
            'Creado y Mantenido por <span foreground="#34d399"><b>Jesus Vera V. (MiniLux0)</b></span>',
            font="Consolas", font_size=13.5, color="#f8fafc"
        ).move_to(author_box.get_center())
        author_grp = VGroup(author_box, author_txt)

        scene1_group = VGroup(logo_grp, title_main, tagline, std_grp, author_grp)

        self.play(
            FadeIn(logo_grp, scale=0.8),
            FadeIn(title_main, shift=UP * 0.2),
            FadeIn(tagline, shift=UP * 0.15),
            FadeIn(std_grp, shift=UP * 0.1),
            FadeIn(author_grp, shift=UP * 0.1),
            rate_func=smooth,
            run_time=1.3
        )
        self.wait(2.5)

        self.play(
            FadeOut(scene1_group, shift=UP * 0.4),
            rate_func=smooth,
            run_time=0.7
        )
        self.wait(0.2)

        # =====================================================================
        # ESCENA 2: VISTAZO AL CURSO (MAPA DE 6 FASES Y 15 MÓDULOS)
        # =====================================================================
        header2 = self.create_header(
            "PLAN DE ESTUDIOS OFICIAL — 6 FASES & 15 MÓDULOS", 
            "De Cero Absoluto a Grado Profesional · C++17 Base (Evolución C++20)"
        )

        # 6 Tarjetas de Fases en Cuadrícula 3x2
        def create_phase_card(phase_num: str, title_str: str, modules_str: str, col_hex: str, x_pos: float, y_pos: float) -> VGroup:
            card_bg = RoundedRectangle(
                width=3.7, height=1.52, corner_radius=0.14,
                fill_color="#0b1120", fill_opacity=0.96,
                stroke_color=col_hex, stroke_width=1.8
            ).move_to([x_pos, y_pos, 0])
            
            p_badge = RoundedRectangle(
                width=1.35, height=0.32, corner_radius=0.08,
                fill_color=col_hex, fill_opacity=0.25,
                stroke_color=col_hex, stroke_width=1.0
            ).move_to(card_bg.get_top() + DOWN * 0.26)
            p_badge_txt = Text(f"FASE {phase_num}", font="Consolas", font_size=10, color=col_hex, weight=BOLD).move_to(p_badge.get_center())
            
            t_txt = Text(title_str, font="Consolas", font_size=11, color="#f8fafc", weight=BOLD).next_to(p_badge, DOWN, buff=0.10)
            m_txt = Text(modules_str, font="Consolas", font_size=9.8, color="#94a3b8").next_to(t_txt, DOWN, buff=0.08)
            
            return VGroup(card_bg, p_badge, p_badge_txt, t_txt, m_txt)

        f1 = create_phase_card("1", "Fundamentos", "M01 · M02 · M03", "#38bdf8", -3.9, 1.0)
        f2 = create_phase_card("2", "Funciones & Texto", "M04 · M05 (string_view)", "#10b981", 0.0, 1.0)
        f3 = create_phase_card("3", "Colecciones", "M06 · M07 (std::vector)", "#f59e0b", 3.9, 1.0)
        f4 = create_phase_card("4", "Memoria Real", "M08 · M09 (RAII & Heap)", "#c084fc", -3.9, -0.85)
        f5 = create_phase_card("5", "POO Moderna", "M10 · M11 · M12 (VTable)", "#f43f5e", 0.0, -0.85)
        f6 = create_phase_card("6", "Resiliencia & STL", "M13 · M14 · M15 (Capstone)", "#60a5fa", 3.9, -0.85)

        phases_group = VGroup(f1, f2, f3, f4, f5, f6)

        hud2 = self.create_hud_footer(
            "PLAN DE ESTUDIOS", 
            "Progresion estrictamente incremental paso a paso. Cero cajas negras.", 
            color=self.COLOR_CYAN
        )

        self.play(
            FadeIn(header2, shift=DOWN * 0.2),
            FadeIn(f1, shift=RIGHT * 0.15),
            FadeIn(f2, shift=DOWN * 0.15),
            FadeIn(f3, shift=LEFT * 0.15),
            FadeIn(f4, shift=RIGHT * 0.15),
            FadeIn(f5, shift=UP * 0.15),
            FadeIn(f6, shift=LEFT * 0.15),
            FadeIn(hud2, shift=UP * 0.2),
            rate_func=smooth,
            run_time=1.3
        )
        self.wait(3.2)

        scene2_group = VGroup(header2, phases_group, hud2)
        self.play(
            FadeOut(scene2_group, shift=UP * 0.3),
            rate_func=smooth,
            run_time=0.7
        )
        self.wait(0.2)

        # =====================================================================
        # ESCENA 3: CIRCUITO DE APRENDIZAJE & BIENVENIDA FINAL
        # =====================================================================
        header3 = self.create_header(
            "EL CIRCUITO DE APRENDIZAJE — 5 PASOS POR LECCIÓN", 
            "Metodología Break-First, Fix-Later & Modelos Visuales de Memoria RAM"
        )

        # 5 Nodos Conectados del Circuito
        def create_step_node(num: str, label: str, col_hex: str, x_pos: float) -> VGroup:
            box = RoundedRectangle(
                width=2.1, height=0.92, corner_radius=0.12,
                fill_color="#0b1120", fill_opacity=0.96,
                stroke_color=col_hex, stroke_width=1.6
            ).move_to([x_pos, 1.15, 0])
            
            n_txt = Text(f"PASO {num}", font="Consolas", font_size=9.5, color=col_hex, weight=BOLD).move_to(box.get_top() + DOWN * 0.22)
            l_txt = Text(label, font="Consolas", font_size=10.5, color="#f8fafc", weight=BOLD).next_to(n_txt, DOWN, buff=0.08)
            return VGroup(box, n_txt, l_txt)

        s1 = create_step_node("1", "Teoria & RAM", "#38bdf8", -4.8)
        s2 = create_step_node("2", "Laboratorio", "#10b981", -2.4)
        s3 = create_step_node("3", "Bug Demo", "#f43f5e", 0.0)
        s4 = create_step_node("4", "Reto Practico", "#f59e0b", 2.4)
        s5 = create_step_node("5", "Cheatsheet", "#c084fc", 4.8)

        # Flechas de conexión entre pasos
        arr1 = Arrow(start=[-3.65, 1.15, 0], end=[-3.5, 1.15, 0], buff=0, stroke_width=2.0, color="#64748b", max_tip_length_to_length_ratio=0.5)
        arr2 = Arrow(start=[-1.25, 1.15, 0], end=[-1.1, 1.15, 0], buff=0, stroke_width=2.0, color="#64748b", max_tip_length_to_length_ratio=0.5)
        arr3 = Arrow(start=[1.15, 1.15, 0], end=[1.3, 1.15, 0], buff=0, stroke_width=2.0, color="#64748b", max_tip_length_to_length_ratio=0.5)
        arr4 = Arrow(start=[3.55, 1.15, 0], end=[3.7, 1.15, 0], buff=0, stroke_width=2.0, color="#64748b", max_tip_length_to_length_ratio=0.5)

        circuit_group = VGroup(s1, arr1, s2, arr2, s3, arr3, s4, arr4, s5)

        # Tarjeta Gigante de Bienvenida
        welcome_hero_box = RoundedRectangle(
            width=11.6, height=1.75, corner_radius=0.16,
            fill_color="#062e24", fill_opacity=0.98,
            stroke_color="#10b981", stroke_width=2.2
        ).move_to(DOWN * 0.70)

        w_title = Text(
            ">> ¡BIENVENIDO A LEARNINGCPP! <<",
            font="Consolas", font_size=18, color="#6ee7b7", weight=BOLD
        ).move_to(welcome_hero_box.get_top() + DOWN * 0.38)

        w_sub = Text(
            "15 Modulos · 117 Lecciones · Animaciones Manim · 100% Gratuito y Open Source",
            font="Consolas", font_size=13, color="#f8fafc"
        ).next_to(w_title, DOWN, buff=0.14)

        w_author = MarkupText(
            'Creado y Mantenido con dedicacion por <span foreground="#38bdf8"><b>Jesus Vera V. (MiniLux0)</b></span> · 2026',
            font="Consolas", font_size=11.5, color="#cbd5e1"
        ).next_to(w_sub, DOWN, buff=0.12)

        welcome_hero_card = VGroup(welcome_hero_box, w_title, w_sub, w_author)

        hud3 = self.create_hud_footer(
            "COMIENZA TU VIAJE", 
            "Explora 01_GettingStarted/ o consulta el temario detallado en SYLLABUS.md.", 
            color=self.COLOR_GREEN
        )

        self.play(
            FadeIn(header3, shift=DOWN * 0.2),
            FadeIn(circuit_group, shift=UP * 0.15),
            FadeIn(welcome_hero_card, shift=UP * 0.2),
            FadeIn(hud3, shift=UP * 0.2),
            rate_func=smooth,
            run_time=1.3
        )

        # Destello final en la tarjeta de bienvenida
        self.play(
            welcome_hero_box.animate.set_stroke(color="#38bdf8", width=3.0),
            rate_func=there_and_back,
            run_time=1.4
        )

        # Pausa final extendida de 5.0 segundos antes de reiniciar el loop
        self.wait(5.0)

if __name__ == "__main__":
    import shutil
    import subprocess
    import glob
    GIF_WIDTH = 720
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR)))
    out_dir = os.path.join(REPO_ROOT, "assets")
    os.makedirs(out_dir, exist_ok=True)
    script_path = os.path.abspath(__file__)

    scenes = {
        "HeroReadmeShowcase": "hero_learningcpp.gif",
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
