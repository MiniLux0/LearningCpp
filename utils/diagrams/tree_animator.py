import os

def render_fib_tree(path):
    width = 700
    height = 350
    
    # DFS Node order for fib(4)
    # (id, text, x, y, parent_id, is_leaf)
    nodes = [
        (0, "fib(4)", 350, 50, -1, False),
        (1, "fib(3)", 200, 130, 0, False),
        (2, "fib(2)", 100, 210, 1, False),
        (3, "fib(1)=1", 50, 290, 2, True),
        (4, "fib(0)=0", 150, 290, 2, True),
        (5, "fib(1)=1", 300, 210, 1, True),
        (6, "fib(2)", 500, 130, 0, False),
        (7, "fib(1)=1", 420, 210, 6, True),
        (8, "fib(0)=0", 580, 210, 6, True)
    ]
    
    # Find coordinates for edges
    coord_map = {n[0]: (n[2], n[3]) for n in nodes}
    
    svg = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
    svg += f'<rect width="{width}" height="{height}" fill="#ffffff" rx="10"/>\n'
    svg += '''<style>
    text { font-family: 'Segoe UI', Roboto, Helvetica, sans-serif; font-size: 14px; font-weight: bold; }
    .node-box { fill: #e1f5fe; stroke: #0288d1; stroke-width: 2; rx: 6; }
    .node-leaf { fill: #e8f5e9; stroke: #388e3c; stroke-width: 2; rx: 6; }
    .edge { stroke: #adb5bd; stroke-width: 2; }
    
    @keyframes fadeIn {
        0% { opacity: 0; transform: scale(0.8); transform-origin: center; }
        100% { opacity: 1; transform: scale(1); transform-origin: center; }
    }
    .anim-item { opacity: 0; animation: fadeIn 0.5s forwards; }
</style>
'''
    svg += f'<text x="{width/2}" y="30" font-size="20" font-weight="bold" text-anchor="middle" fill="#212529">Árbol de Recursión Animado: fib(4)</text>\n'

    # Generate SVGs
    step_dur = 0.8
    for n_id, text, x, y, p_id, is_leaf in nodes:
        delay = n_id * step_dur
        
        box_class = "node-leaf" if is_leaf else "node-box"
        
        svg += f'<g class="anim-item" style="animation-delay: {delay}s; transform-origin: {x}px {y}px;">\n'
        
        # Draw edge from parent (if any)
        if p_id != -1:
            px, py = coord_map[p_id]
            svg += f'  <line x1="{px}" y1="{py+15}" x2="{x}" y2="{y-15}" class="edge"/>\n'
            
        # Draw node
        svg += f'  <rect x="{x-40}" y="{y-15}" width="80" height="30" class="{box_class}"/>\n'
        svg += f'  <text x="{x}" y="{y+5}" text-anchor="middle" fill="#212529">{text}</text>\n'
        svg += '</g>\n'
        
    svg += '</svg>'
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)

def render_hanoi_tree(path):
    width = 750
    height = 300
    
    # Hanoi(3, A, C, B)
    # DFS order:
    # 0: H(3, A->C)
    # 1: H(2, A->B)
    # 2: H(1, A->C) -> Move 1 A->C
    # 3: Move 2 A->B
    # 4: H(1, C->B) -> Move 1 C->B
    # 5: Move 3 A->C
    # 6: H(2, B->C)
    # 7: H(1, B->A) -> Move 1 B->A
    # 8: Move 2 B->C
    # 9: H(1, A->C) -> Move 1 A->C
    
    nodes = [
        (0, "Hanoi(3, A→C)", 375, 50, -1, False),
        
        (1, "Hanoi(2, A→B)", 180, 130, 0, False),
        (2, "Hanoi(1, A→C)", 80, 210, 1, True),
        (3, "Mover Disco 2 (A→B)", 180, 210, 1, True),
        (4, "Hanoi(1, C→B)", 280, 210, 1, True),
        
        (5, "Mover Disco 3 (A→C)", 375, 130, 0, True),
        
        (6, "Hanoi(2, B→C)", 570, 130, 0, False),
        (7, "Hanoi(1, B→A)", 470, 210, 6, True),
        (8, "Mover Disco 2 (B→C)", 570, 210, 6, True),
        (9, "Hanoi(1, A→C)", 670, 210, 6, True)
    ]
    
    coord_map = {n[0]: (n[2], n[3]) for n in nodes}
    
    svg = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
    svg += f'<rect width="{width}" height="{height}" fill="#ffffff" rx="10"/>\n'
    svg += '''<style>
    text { font-family: 'Segoe UI', Roboto, Helvetica, sans-serif; font-size: 13px; font-weight: bold; }
    .node-box { fill: #f3e5f5; stroke: #8e24aa; stroke-width: 2; rx: 6; }
    .node-move { fill: #fff3e0; stroke: #f57c00; stroke-width: 2; rx: 6; }
    .edge { stroke: #adb5bd; stroke-width: 2; }
    
    @keyframes fadeInScale {
        0% { opacity: 0; transform: scale(0.7); }
        100% { opacity: 1; transform: scale(1); }
    }
    .anim-item { opacity: 0; animation: fadeInScale 0.6s forwards; }
</style>
'''
    svg += f'<text x="{width/2}" y="30" font-size="20" font-weight="bold" text-anchor="middle" fill="#212529">Árbol de Recursión Animado: Torres de Hanói (N=3)</text>\n'

    step_dur = 0.8
    for n_id, text, x, y, p_id, is_move in nodes:
        delay = n_id * step_dur
        
        box_class = "node-move" if is_move else "node-box"
        bw = 140 if is_move else 110
        
        svg += f'<g class="anim-item" style="animation-delay: {delay}s; transform-origin: {x}px {y}px;">\n'
        
        if p_id != -1:
            px, py = coord_map[p_id]
            svg += f'  <line x1="{px}" y1="{py+15}" x2="{x}" y2="{y-15}" class="edge"/>\n'
            
        svg += f'  <rect x="{x-bw/2}" y="{y-15}" width="{bw}" height="30" class="{box_class}"/>\n'
        svg += f'  <text x="{x}" y="{y+5}" text-anchor="middle" fill="#212529">{text}</text>\n'
        svg += '</g>\n'
        
    svg += '</svg>'
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    out_dir = "05_RecursionAlgorithms/theory/assets"
    os.makedirs(out_dir, exist_ok=True)
    render_fib_tree(os.path.join(out_dir, "fib_tree.svg"))
    render_hanoi_tree(os.path.join(out_dir, "hanoi_tree_3.svg"))
    print("Tree Animations SVGs generated successfully!")
