import os

def render_fib_tree(path):
    width = 700
    height = 350
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
    coord_map = {n[0]: (n[2], n[3]) for n in nodes}
    
    num_steps = len(nodes) + 2 # Add 2 steps of pause at the end
    step_dur = 0.8
    total_time = num_steps * step_dur
    
    svg = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
    svg += f'<rect width="{width}" height="{height}" fill="#ffffff" rx="10"/>\n'
    svg += '''<style>
    text { font-family: 'Segoe UI', Roboto, Helvetica, sans-serif; font-size: 14px; font-weight: bold; }
    .node-box { fill: #e1f5fe; stroke: #0288d1; stroke-width: 2; rx: 6; }
    .node-leaf { fill: #e8f5e9; stroke: #388e3c; stroke-width: 2; rx: 6; }
    .edge { stroke: #adb5bd; stroke-width: 2; }
'''
    # Generate exact keyframes for looping
    for i in range(len(nodes)):
        appear_pct = (i / num_steps) * 100
        svg += f'''
    @keyframes show-node-{i} {{
        0%, {max(0, appear_pct - 0.1):.1f}% {{ opacity: 0; }}
        {appear_pct:.1f}%, 100% {{ opacity: 1; }}
    }}
    .node-{i} {{ animation: show-node-{i} {total_time}s infinite; opacity: 0; }}
'''
    svg += '</style>\n'
    svg += f'<text x="{width/2}" y="30" font-size="20" font-weight="bold" text-anchor="middle" fill="#212529">Árbol de Recursión Animado: fib(4)</text>\n'

    for n_id, text, x, y, p_id, is_leaf in nodes:
        box_class = "node-leaf" if is_leaf else "node-box"
        svg += f'<g class="node-{n_id}">\n'
        if p_id != -1:
            px, py = coord_map[p_id]
            svg += f'  <line x1="{px}" y1="{py+15}" x2="{x}" y2="{y-15}" class="edge"/>\n'
        svg += f'  <rect x="{x-40}" y="{y-15}" width="80" height="30" class="{box_class}"/>\n'
        svg += f'  <text x="{x}" y="{y+5}" text-anchor="middle" fill="#212529">{text}</text>\n'
        svg += '</g>\n'
        
    svg += '</svg>'
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)

def render_hanoi_tree(path):
    width = 850 # Increased width
    height = 300
    
    # Hanoi nodes with wider spacing
    nodes = [
        (0, "Hanoi(3, A→C)", 425, 50, -1, False),
        
        (1, "Hanoi(2, A→B)", 200, 130, 0, False),
        (2, "Hanoi(1, A→C)", 70, 210, 1, True),
        (3, "Mover 2 (A→B)", 200, 210, 1, True),
        (4, "Hanoi(1, C→B)", 330, 210, 1, True),
        
        (5, "Mover 3 (A→C)", 425, 130, 0, True),
        
        (6, "Hanoi(2, B→C)", 650, 130, 0, False),
        (7, "Hanoi(1, B→A)", 520, 210, 6, True),
        (8, "Mover 2 (B→C)", 650, 210, 6, True),
        (9, "Hanoi(1, A→C)", 780, 210, 6, True)
    ]
    coord_map = {n[0]: (n[2], n[3]) for n in nodes}
    
    num_steps = len(nodes) + 2
    step_dur = 0.8
    total_time = num_steps * step_dur
    
    svg = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
    svg += f'<rect width="{width}" height="{height}" fill="#ffffff" rx="10"/>\n'
    svg += '''<style>
    text { font-family: 'Segoe UI', Roboto, Helvetica, sans-serif; font-size: 13px; font-weight: bold; }
    .node-box { fill: #f3e5f5; stroke: #8e24aa; stroke-width: 2; rx: 6; }
    .node-move { fill: #fff3e0; stroke: #f57c00; stroke-width: 2; rx: 6; }
    .edge { stroke: #adb5bd; stroke-width: 2; }
'''
    for i in range(len(nodes)):
        appear_pct = (i / num_steps) * 100
        svg += f'''
    @keyframes show-node-{i} {{
        0%, {max(0, appear_pct - 0.1):.1f}% {{ opacity: 0; }}
        {appear_pct:.1f}%, 100% {{ opacity: 1; }}
    }}
    .node-{i} {{ animation: show-node-{i} {total_time}s infinite; opacity: 0; }}
'''
    svg += '</style>\n'
    svg += f'<text x="{width/2}" y="30" font-size="20" font-weight="bold" text-anchor="middle" fill="#212529">Árbol de Recursión Animado: Torres de Hanói (N=3)</text>\n'

    for n_id, text, x, y, p_id, is_move in nodes:
        box_class = "node-move" if is_move else "node-box"
        bw = 120 # Fixed width for all
        svg += f'<g class="node-{n_id}">\n'
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
