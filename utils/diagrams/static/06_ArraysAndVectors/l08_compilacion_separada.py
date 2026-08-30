from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'core')))
from manim_base import BaseLearningScene, export_manim_image

class L08CompilacionSeparada(BaseLearningScene):
    def construct(self):
        # 1. Encabezado
        header = self.create_header("Arquitectura Multi-Archivo", "Pipeline de Compilacion Separada y Enlazado (Linker)")
        self.add(header)

        # ETAPA 1: Código Fuente (.h y .cpp)
        box_src, bg_src = self.create_card_panel(width=3.6, height=4.2, title="1. Fuentes", subtitle="Codigo C++ (.h / .cpp)")
        box_src.move_to(LEFT * 4.6 + DOWN * 0.2)

        f_h = self.create_cell("Modulo.h\n(Contrato / Prototipos)", width=2.9, height=0.9, color=self.COLOR_CYAN, font_size=11).move_to(bg_src.get_center() + UP * 0.7)
        f_cpp1 = self.create_cell("Modulo.cpp\n(Implementacion)", width=2.9, height=0.75, color=self.COLOR_CYAN, font_size=10).move_to(bg_src.get_center() + DOWN * 0.2)
        f_main = self.create_cell("main.cpp\n(Punto de Entrada)", width=2.9, height=0.75, color=self.COLOR_CYAN, font_size=10).move_to(bg_src.get_center() + DOWN * 1.1)

        # ETAPA 2: Compilación a Objetos (.o)
        box_obj, bg_obj = self.create_card_panel(width=3.6, height=4.2, title="2. Compilador", subtitle="g++ -c (Traduccion a Binario)")
        box_obj.move_to(DOWN * 0.2)

        o_mod = self.create_cell("Modulo.o\n(Codigo Objeto)", width=2.9, height=0.85, color=self.COLOR_GOLD, font_size=11).move_to(bg_obj.get_center() + UP * 0.4)
        o_main = self.create_cell("main.o\n(Codigo Objeto)", width=2.9, height=0.85, color=self.COLOR_GOLD, font_size=11).move_to(bg_obj.get_center() + DOWN * 0.8)

        # ETAPA 3: Enlazador (Linker) a Ejecutable Final
        box_bin, bg_bin = self.create_card_panel(width=3.6, height=4.2, title="3. Enlazado (Linker)", subtitle="Resolucion de Direcciones")
        box_bin.move_to(RIGHT * 4.6 + DOWN * 0.2)

        f_exe = self.create_cell("app.exe / bin\n(Ejecutable Final)", width=2.9, height=1.1, color=self.COLOR_GREEN, font_size=12).move_to(bg_bin.get_center() + DOWN * 0.1)
        exe_badge = self.create_badge("LISTO PARA CPU", fill_color="#064e3b", stroke_color=self.COLOR_GREEN, text_color=self.COLOR_GREEN_LIGHT, width=2.8, height=0.4).next_to(f_exe, DOWN, buff=0.25)

        # Flechas de conexión
        arr1 = Arrow(start=box_src.get_right() + UP * 0.2, end=box_obj.get_left() + UP * 0.2, buff=0.1, color=self.COLOR_GOLD, stroke_width=3)
        arr2 = Arrow(start=box_src.get_right() + DOWN * 0.8, end=box_obj.get_left() + DOWN * 0.8, buff=0.1, color=self.COLOR_GOLD, stroke_width=3)
        arr3 = Arrow(start=box_obj.get_right(), end=box_bin.get_left(), buff=0.1, color=self.COLOR_GREEN, stroke_width=4)

        self.add(box_src, f_h, f_cpp1, f_main)
        self.add(box_obj, o_mod, o_main)
        self.add(box_bin, f_exe, exe_badge)
        self.add(arr1, arr2, arr3)

if __name__ == "__main__":
    export_manim_image(__file__, "06_ArraysAndVectors", {"L08CompilacionSeparada": "l08_compilacion_separada.png"})
