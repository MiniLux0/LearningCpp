from manim import *
import os
import glob
import shutil
import subprocess
from typing import List, Tuple, Optional, Union, Dict, Any

class BaseLearningScene(Scene):
    """
    Base class for all LearningCpp Manim animations.
    Provides standard colors, fonts, background, and visual UI primitives
    to ensure scalable, accessible, and ultra-high-fidelity aesthetics across all visuals.
    """
    
    # -------------------------------------------------------------------------
    # Cyber-Academic Dark Palette
    # -------------------------------------------------------------------------
    BG_COLOR = "#0d1117"
    TEXT_COLOR = "#f0f6fc"
    SUBTEXT_COLOR = "#8b949e"
    HIGHLIGHT_COLOR = "#fbbf24"
    
    # Semantic Cyber-Academic colors
    COLOR_GOLD = "#f59e0b"
    COLOR_GOLD_LIGHT = "#fbbf24"
    COLOR_CYAN = "#38bdf8"
    COLOR_CYAN_LIGHT = "#7dd3fc"
    COLOR_GREEN = "#10b981"
    COLOR_GREEN_LIGHT = "#6ee7b7"
    COLOR_RED = "#ef4444"
    COLOR_RED_LIGHT = "#fca5a5"
    COLOR_RED_ACCENT = "#ef4444"
    COLOR_PURPLE = "#c084fc"
    COLOR_PURPLE_LIGHT = "#e9d5ff"
    COLOR_PANEL = "#161b22"
    COLOR_BORDER = "#30363d"
    COLOR_MUTED = "#8b949e"
    
    # Pastel node colors for collections
    PALETTE = ["#ef4444", "#fbbf24", "#38bdf8", "#10b981", "#c084fc"]
    PEG_COLOR = "#30363d"
    
    # Semantic type/status colors
    COLOR_INT = "#10b981"       # Green
    COLOR_DOUBLE = "#c084fc"    # Purple
    COLOR_CHAR = "#fbbf24"      # Gold / Amber
    COLOR_ERROR = "#ef4444"     # Red
    COLOR_SUCCESS = "#10b981"   # Green

    def setup(self):
        """Initializes the scene background and default configurations."""
        super().setup()
        self.camera.background_color = self.BG_COLOR

    # -------------------------------------------------------------------------
    # UI Component Builders (Standardized & Anti-Overlap)
    # -------------------------------------------------------------------------

    def create_header(self, title_str: str, subtitle_str: str = "") -> VGroup:
        """
        Creates a standardized top header for the animation.
        Anchored cleanly at UP with buff=0.25.
        """
        title = Text(title_str, font="Consolas", weight=BOLD, color=self.TEXT_COLOR).scale(0.85)
        if title.width > 12.8:
            title.scale_to_fit_width(12.8)
        
        if subtitle_str:
            subtitle = Text(subtitle_str, font="Consolas", color=self.SUBTEXT_COLOR).scale(0.52)
            if subtitle.width > 11.5:
                subtitle.scale_to_fit_width(11.5)
            header = VGroup(title, subtitle).arrange(DOWN, buff=0.08)
        else:
            header = title
            
        header.to_edge(UP, buff=0.25)
        return header

    def create_code_window(self, width: float = 5.4, height: float = 3.0, title: str = "main.cpp") -> Tuple[VGroup, RoundedRectangle]:
        """
        Creates a standardized IDE code window with OS window controls and editor card.
        Returns: (full_window_group, background_card)
        """
        bg = RoundedRectangle(
            width=width, height=height, corner_radius=0.18,
            fill_color=self.COLOR_PANEL, fill_opacity=0.95,
            stroke_color=self.COLOR_BORDER, stroke_width=1.8
        )
        bar = RoundedRectangle(
            width=width, height=0.45, corner_radius=0.12,
            fill_color="#21262d", fill_opacity=1.0,
            stroke_color=self.COLOR_BORDER, stroke_width=1
        ).next_to(bg.get_top(), DOWN, buff=0).shift(UP * 0.225)
        
        dot_r = Dot(radius=0.06, color="#ff5f56").move_to(bar.get_left() + RIGHT * 0.25)
        dot_y = Dot(radius=0.06, color="#ffbd2e").next_to(dot_r, RIGHT, buff=0.12)
        dot_g = Dot(radius=0.06, color="#27c93f").next_to(dot_y, RIGHT, buff=0.12)
        tab_txt = Text(title, font="Consolas", font_size=14, color=self.SUBTEXT_COLOR).next_to(dot_g, RIGHT, buff=0.3)
        
        window = VGroup(bg, bar, dot_r, dot_y, dot_g, tab_txt)
        return window, bg

    def create_code_pointer(self, target_line: Mobject, color: str = None) -> Triangle:
        """
        Creates a non-intrusive execution pointer pointing at a target code line from the left.
        Avoids the deformation artifacts of SurroundingRectangle.
        """
        if color is None:
            color = self.COLOR_GOLD_LIGHT
            
        pointer = Triangle(
            fill_color=color, fill_opacity=1.0,
            stroke_color="#ffffff", stroke_width=1.0
        ).scale(0.14).rotate(-PI / 2).next_to(target_line, LEFT, buff=0.18)
        return pointer

    def create_card_panel(self, width: float = 5.4, height: float = 3.0, title: str = "Memoria RAM", subtitle: str = "") -> Tuple[VGroup, RoundedRectangle]:
        """
        Creates a standardized hardware, RAM, or inspection card panel.
        Returns: (card_group, background_rect)
        """
        bg = RoundedRectangle(
            width=width, height=height, corner_radius=0.18,
            fill_color="#13141f", fill_opacity=0.95,
            stroke_color="#2e344d", stroke_width=1.8
        )
        title_txt = Text(title, font="Consolas", font_size=16, color=self.COLOR_CYAN, weight=BOLD).next_to(bg.get_top(), DOWN, buff=0.18)
        
        if subtitle:
            sub_txt = Text(subtitle, font="Consolas", font_size=13, color="#8b949e").next_to(title_txt, DOWN, buff=0.06)
            card = VGroup(bg, title_txt, sub_txt)
        else:
            card = VGroup(bg, title_txt)
            
        return card, bg

    def create_badge(self, text: str, fill_color: str = "#064e3b", stroke_color: str = "#10b981", text_color: str = "#6ee7b7", width: float = 5.8, height: float = 0.45) -> VGroup:
        """
        Creates a standardized pill badge with no-overlap safe dimensions.
        """
        box = RoundedRectangle(
            width=width, height=height, corner_radius=0.1,
            fill_color=fill_color, fill_opacity=0.9,
            stroke_color=stroke_color, stroke_width=1.5
        )
        lbl = Text(text, font="Consolas", font_size=13, color=text_color, weight=BOLD).move_to(box.get_center())
        return VGroup(box, lbl)

    def create_cell(self, text: str, width: float = 1.2, height: float = 0.6, color: str = None, font_size: int = 12) -> VGroup:
        """
        Creates a standardized memory cell (for Arrays, Vectors, Stack/Heap cells).
        """
        if color is None:
            color = self.COLOR_CYAN
        rect = RoundedRectangle(
            width=width, height=height, corner_radius=0.08,
            fill_color="#1e293b", fill_opacity=0.9,
            stroke_color=color, stroke_width=1.8
        )
        txt = Text(text, font="Consolas", font_size=font_size, color=self.TEXT_COLOR).move_to(rect.get_center())
        return VGroup(rect, txt)

    def create_hud_footer(self, tag: str, message: str, color: str = None, width: float = 12.2, height: float = 0.85) -> VGroup:
        """
        Creates an anti-overlap bottom status HUD anchored strictly to DOWN with buff=0.35.
        Guarantees zero collision with workspace cards above.
        """
        if color is None:
            color = self.COLOR_CYAN
            
        bg_fill = "#1a0a0d" if color == self.COLOR_RED else "#0a192f"
        box = RoundedRectangle(
            width=width, height=height, corner_radius=0.12,
            fill_color=bg_fill, fill_opacity=0.98,
            stroke_color=color, stroke_width=1.8
        ).to_edge(DOWN, buff=0.35)

        tag_txt = Text(f"[{tag}]", font="Consolas", font_size=14, color=color, weight=BOLD).move_to(box.get_left() + RIGHT * 1.3)
        msg_txt = Text(message, font="Consolas", font_size=15, color="#ffffff").next_to(tag_txt, RIGHT, buff=0.25)
        
        # Prevent text overflow
        if msg_txt.get_right()[0] > box.get_right()[0] - 0.2:
            msg_txt.scale_to_fit_width(box.width - tag_txt.width - 1.8)
            msg_txt.next_to(tag_txt, RIGHT, buff=0.25)
            
        return VGroup(box, tag_txt, msg_txt)

    def create_pointer_arrow(self, start_mobj: Mobject, end_mobj: Mobject, label: str = "", color: str = None) -> VGroup:
        """
        Creates an animated pointer/reference arrow between two memory objects.
        """
        if color is None:
            color = self.COLOR_GOLD
            
        arrow = Arrow(
            start=start_mobj.get_top(),
            end=end_mobj.get_bottom(),
            buff=0.1,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.25,
            color=color
        )
        group = VGroup(arrow)
        if label:
            lbl = Text(label, font="Consolas", font_size=12, color=color, weight=BOLD).next_to(arrow, RIGHT, buff=0.08)
            group.add(lbl)
        return group

    def create_byte_grid(self, elements: List[Union[str, int]], base_color: str = "#38bdf8", show_indices: bool = True, show_addresses: bool = False, base_addr: int = 0x7FFEE0) -> VGroup:
        """
        Creates a contiguous memory grid (Array / Vector / Buffer representation) with index and address markers.
        """
        grid = VGroup()
        for idx, val in enumerate(elements):
            box = RoundedRectangle(
                width=0.85, height=0.85, corner_radius=0.08,
                fill_color="#1e1e2e", fill_opacity=0.95,
                stroke_color=base_color, stroke_width=1.5
            )
            txt = Text(str(val), font="Consolas", font_size=18, color="#ffffff", weight=BOLD).move_to(box.get_center())
            cell = VGroup(box, txt)
            
            cell_full = VGroup(cell)
            if show_indices:
                idx_txt = Text(f"[{idx}]", font="Consolas", font_size=13, color=self.SUBTEXT_COLOR).next_to(box, UP, buff=0.08)
                cell_full.add(idx_txt)
            if show_addresses:
                addr_hex = hex(base_addr + (idx * 4))
                addr_txt = Text(addr_hex, font="Consolas", font_size=10, color="#6e7681").next_to(box, DOWN, buff=0.08)
                cell_full.add(addr_txt)
                
            grid.add(cell_full)
            
        grid.arrange(RIGHT, buff=0.15)
        return grid

    def create_rounded_node(self, width: float, height: float, color: str, label_str: str = "") -> RoundedRectangle:
        """Creates a scalable rounded rectangle (pill shape) with an optional label."""
        radius = min(width, height) / 2
        node = RoundedRectangle(
            width=width, 
            height=height, 
            corner_radius=radius,
            fill_color=color, 
            fill_opacity=0.9,
            stroke_color=WHITE,
            stroke_width=1.5
        )
        
        if label_str:
            label = Text(str(label_str), font="Consolas", color=BLACK, weight=BOLD)
            if label.width > width * 0.9:
                label.scale_to_fit_width(width * 0.9)
            if label.height > height * 0.7:
                label.scale_to_fit_height(height * 0.7)
                
            label.move_to(node.get_center())
            node.add(label)
            
        return node
        
    def create_counter(self, label: str, initial_value: int) -> VGroup:
        """Creates a standardized UI counter."""
        counter_text = Text(f"{label}: {initial_value}", font="Consolas", color=self.HIGHLIGHT_COLOR).scale(0.5)
        counter_text.to_corner(UR)
        return counter_text

    def get_jump_arc(self, source_idx: int, target_idx: int, intensity: float = 0.5) -> float:
        """
        Returns the correct path_arc angle for a jump animation.
        Ensures the arc always curves UPWARDS regardless of direction.
        """
        dist = abs(target_idx - source_idx)
        base_angle = PI/2 if target_idx > source_idx else -PI/2
        if dist > 1:
            base_angle = (PI * intensity) if target_idx > source_idx else -(PI * intensity)
        return base_angle


# -------------------------------------------------------------------------
# Automated Rendering & GIF Export Engine
# -------------------------------------------------------------------------

def export_manim_scenes(script_file: str, module_name: str, scenes_dict: Dict[str, str], gif_width: int = 960, fps: int = 18):
    """
    Reusable automated export function for rendering Manim scenes to optimized GIFs.
    Applies FFmpeg palettegen/paletteuse lanczos filters and purges intermediate caches.
    """
    script_dir = os.path.dirname(os.path.abspath(script_file))
    repo_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(script_dir))))
    out_dir = os.path.join(repo_root, module_name, "theory", "assets")
    os.makedirs(out_dir, exist_ok=True)
    script_path = os.path.abspath(script_file)

    for scene_name, final_gif_name in scenes_dict.items():
        print(f"--> [MANIM ENGINE] Rendering scene '{scene_name}' from {os.path.basename(script_file)}...")
        command = f'python -m manim -qm --disable_caching --media_dir "{out_dir}" "{script_path}" {scene_name}'
        subprocess.run(command, shell=True)

        matches = glob.glob(os.path.join(out_dir, "videos", "**", f"{scene_name}*.mp4"), recursive=True)
        if matches:
            mp4_path = matches[0]
            final_gif_path = os.path.join(out_dir, final_gif_name)
            print(f"--> [FFMPEG] Optimizing palette and encoding to '{final_gif_name}' (960px Lanczos)...")
            ffmpeg_cmd = [
                "ffmpeg", "-y", "-i", mp4_path,
                "-vf", f"fps={fps},scale={gif_width}:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse",
                final_gif_path,
            ]
            subprocess.run(ffmpeg_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"--> [SUCCESS] Created: {final_gif_path}")

    # Limpieza de caché temporal de Manim
    for folder in ["videos", "images", "texts", "Tex"]:
        cache_dir = os.path.join(out_dir, folder)
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir, ignore_errors=True)
