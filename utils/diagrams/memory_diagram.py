"""
Memory Diagram Generator
Uses Matplotlib to precisely draw Box-and-Arrow diagrams (Memory, Pointers, Arrays, UML)
that Graphviz struggles to lay out strictly.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from utils.diagrams.style import PALETTE, FONTS

def get_color(name, default):
    return PALETTE.get(name, default)

class MemoryDiagramBuilder:
    def __init__(self, title="", width=8, height=4):
        self.fig, self.ax = plt.subplots(figsize=(width, height))
        self.ax.set_xlim(0, width * 100)
        self.ax.set_ylim(0, height * 100)
        self.ax.axis('off')
        
        if title:
            self.ax.text(width * 50, height * 100 - 20, title, 
                         ha='center', va='top', 
                         fontsize=FONTS["title_size"], 
                         fontweight='bold', 
                         color=PALETTE["title"], 
                         family=FONTS["primary"])
            
    def draw_box(self, x, y, w, h, title="", subtitle="", style="default"):
        """Draws a styled memory block or array cell."""
        fill = get_color(f"node_{style}_fill", PALETTE["node_default_fill"])
        stroke = get_color(f"node_{style}_stroke", PALETTE["node_default_stroke"])
        
        rect = patches.FancyBboxPatch((x, y), w, h, 
                                      boxstyle=patches.BoxStyle("Round", pad=0.0, rounding_size=4),
                                      linewidth=2, edgecolor=stroke, facecolor=fill)
        self.ax.add_patch(rect)
        
        if title and subtitle:
            self.ax.text(x + w/2, y + h/2 + 5, title, ha='center', va='center',
                         fontsize=FONTS["text_size"], fontweight='bold', color=PALETTE["text_primary"], family=FONTS["primary"])
            self.ax.text(x + w/2, y + h/2 - 15, subtitle, ha='center', va='center',
                         fontsize=FONTS["mono_size"], color=PALETTE["text_secondary"], family=FONTS["monospace"])
        elif title:
            self.ax.text(x + w/2, y + h/2, title, ha='center', va='center',
                         fontsize=FONTS["text_size"], fontweight='bold', color=PALETTE["text_primary"], family=FONTS["primary"])
            
    def draw_pointer(self, x1, y1, x2, y2, label="", style="default"):
        """Draws an arrow representing a pointer or reference."""
        color = get_color(f"edge_{style}", PALETTE["edge_default"])
        
        self.ax.annotate(label,
                         xy=(x2, y2), xycoords='data',
                         xytext=(x1, y1), textcoords='data',
                         arrowprops=dict(arrowstyle="->", color=color, lw=2),
                         ha='center', va='bottom', color=PALETTE["text_secondary"], family=FONTS["primary"], fontsize=11)

    def render(self, output_path):
        """Exports the diagram to SVG."""
        plt.tight_layout()
        plt.savefig(output_path, format='svg', bbox_inches='tight', transparent=True)
        plt.close(self.fig)
        print(f"Successfully generated: {output_path}")

def generate_hanoi_filmstrip(n_disks, output_path):
    """
    Pilot example: Generates the static filmstrip for Hanoi using matplotlib boxes.
    """
    # Quick simulation
    state = {'A': list(range(n_disks, 0, -1)), 'B': [], 'C': []}
    steps = [{k: list(v) for k, v in state.items()}]
    
    def sim(n, s, t, a):
        if n == 1:
            state[t].append(state[s].pop())
            steps.append({k: list(v) for k, v in state.items()})
            return
        sim(n-1, s, a, t)
        state[t].append(state[s].pop())
        steps.append({k: list(v) for k, v in state.items()})
        sim(n-1, a, t, s)
        
    sim(n_disks, 'A', 'C', 'B')
    
    total = len(steps)
    cols = 4 if total <= 8 else 5
    rows = (total + cols - 1) // cols
    
    # Each frame is roughly 250x180 scaled to matplotlib coordinates
    builder = MemoryDiagramBuilder(f"Towers of Hanoi - State Filmstrip (N={n_disks})", cols * 3, rows * 2)
    
    disk_colors = ['#fca311', '#14213d', '#e63946', '#2a9d8f', '#9c27b0']
    
    for i, step in enumerate(steps):
        r = rows - 1 - (i // cols) # invert Y for matplotlib
        c = i % cols
        ox, oy = c * 300, r * 200
        
        # Frame
        builder.draw_box(ox+10, oy+10, 280, 180, "", "", "default")
        title = "Initial" if i == 0 else f"Step {i}/{total-1}"
        builder.ax.text(ox + 150, oy + 175, title, ha='center', va='top', fontweight='bold')
        
        for p, peg in enumerate(['A', 'B', 'C']):
            px = ox + (p+1) * 75
            # Draw peg
            rect = patches.Rectangle((px-2, oy+20), 4, 120, color=PALETTE["node_default_stroke"])
            builder.ax.add_patch(rect)
            builder.ax.text(px, oy+10, f"Peg {peg}", ha='center', fontsize=10, color=PALETTE["text_secondary"])
            
            for d_idx, d_size in enumerate(step[peg]):
                dw = d_size * 20 + 20
                dh = 15
                dy = oy + 20 + d_idx * 17
                color = disk_colors[(d_size-1) % len(disk_colors)]
                disk = patches.FancyBboxPatch((px - dw/2, dy), dw, dh, 
                                              boxstyle=patches.BoxStyle("Round", pad=0.0, rounding_size=2),
                                              facecolor=color, edgecolor="none")
                builder.ax.add_patch(disk)
                
    builder.render(output_path)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--test-filmstrip", type=int, help="Test Hanoi filmstrip with N disks")
    args = parser.parse_args()
    
    if args.test_filmstrip:
        generate_hanoi_filmstrip(args.test_filmstrip, "test_hanoi_filmstrip.svg")
