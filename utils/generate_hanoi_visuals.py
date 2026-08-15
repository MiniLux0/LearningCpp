"""
Hanoi Visuals Generator
-----------------------
This script generates two types of high-quality SVG visuals for the Towers of Hanoi problem:
1. 'hanoi_steps.svg': A static "filmstrip" grid showing the exact state of the pegs at each step.
   This replaces animated GIFs to ensure 100% compatibility with static PDF exports.
2. 'hanoi_tree.svg': A recursion tree showing the Divide & Conquer call stack.

Usage:
    python generate_hanoi_visuals.py --disks <N>
    
Example:
    python generate_hanoi_visuals.py --disks 3

The script uses pure Python string formatting to generate SVGs, eliminating the need for external
system binaries like Graphviz ('dot') which often fail on Windows environments.
"""

import os
import argparse

def simulate_hanoi(n, source, target, auxiliary, state, steps):
    if n == 1:
        state[target].append(state[source].pop())
        steps.append({k: list(v) for k, v in state.items()})
        return
    simulate_hanoi(n-1, source, auxiliary, target, state, steps)
    state[target].append(state[source].pop())
    steps.append({k: list(v) for k, v in state.items()})
    simulate_hanoi(n-1, auxiliary, target, source, state, steps)

def generate_filmstrip(out_path, n_disks=3):
    """
    Generates a static SVG filmstrip (grid) of all moves in the Towers of Hanoi.
    """
    state = {'A': list(range(n_disks, 0, -1)), 'B': [], 'C': []}
    steps = [{k: list(v) for k, v in state.items()}]
    simulate_hanoi(n_disks, 'A', 'C', 'B', state, steps)
    
    total_steps = len(steps)
    cols = 4 if total_steps <= 8 else 5
    rows = (total_steps + cols - 1) // cols
    
    W_frame, H_frame = 250, 180
    W_total, H_total = cols * W_frame, rows * H_frame
    
    svg = [f'<svg width="{W_total}" height="{H_total}" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<rect width="{W_total}" height="{H_total}" fill="#ffffff"/>')
    svg.append('<style>.text { font-family: sans-serif; }</style>')
    
    # Disk Colors (up to 6 disks)
    colors = ['#fca311', '#14213d', '#e63946', '#2a9d8f', '#9c27b0', '#e91e63']
    
    for i, step in enumerate(steps):
        r, c = i // cols, i % cols
        ox, oy = c * W_frame, r * H_frame
        
        # Frame Border
        svg.append(f'<rect x="{ox+10}" y="{oy+10}" width="{W_frame-20}" height="{H_frame-20}" rx="10" fill="#f8f9fa" stroke="#dee2e6" stroke-width="2"/>')
        
        title = "Estado Inicial" if i == 0 else f"Paso {i}/{total_steps-1}"
        svg.append(f'<text x="{ox+W_frame/2}" y="{oy+35}" class="text" font-size="14" font-weight="bold" text-anchor="middle" fill="#343a40">{title}</text>')
        
        peg_y = oy + H_frame - 30
        for p, peg in enumerate(['A', 'B', 'C']):
            px = ox + (p+1) * (W_frame / 4)
            svg.append(f'<rect x="{px-2}" y="{oy+60}" width="4" height="{H_frame-90}" fill="#adb5bd" rx="2"/>')
            svg.append(f'<text x="{px}" y="{peg_y+20}" class="text" font-size="12" text-anchor="middle" fill="#6c757d">Torre {peg}</text>')
            
            for d_idx, d_size in enumerate(step[peg]):
                dw = d_size * 15 + 15
                dh = 10
                dx = px - dw/2
                dy = peg_y - (d_idx+1)*dh - d_idx*2
                color = colors[(d_size-1) % len(colors)]
                svg.append(f'<rect x="{dx}" y="{dy}" width="{dw}" height="{dh}" fill="{color}" rx="3"/>')
                
    svg.append('</svg>')
    with open(out_path, 'w', encoding='utf-8') as f: f.write('\n'.join(svg))

class Node:
    def __init__(self, label, node_type, level):
        self.label = label
        self.node_type = node_type
        self.level = level
        self.x = 0
        self.y = 0

def build_tree(n, source, target, auxiliary, level=0):
    """
    Recursively builds the tree structure returning nodes and edges.
    """
    node_id = f"N_{n}_{source}_{target}_{level}_{id(source)}"
    nodes = {node_id: Node(f"Hanoi({n}, {source}→{target}, {auxiliary})", 'call', level)}
    edges = []
    
    if n > 1:
        # Left child
        left_nodes, left_edges, left_root = build_tree(n-1, source, auxiliary, target, level+1)
        nodes.update(left_nodes)
        edges.extend(left_edges)
        edges.append((node_id, left_root))
        
        # Middle (Move)
        mid_id = f"M_{n}_{source}_{target}_{level}_{id(source)}"
        nodes[mid_id] = Node(f"Mover D{n}: {source}→{target}", 'move', level+1)
        edges.append((node_id, mid_id))
        
        # Right child
        right_nodes, right_edges, right_root = build_tree(n-1, auxiliary, target, source, level+1)
        nodes.update(right_nodes)
        edges.extend(right_edges)
        edges.append((node_id, right_root))
    else:
        # For N=1, just the move
        mid_id = f"M_{n}_{source}_{target}_{level}_{id(source)}"
        nodes[mid_id] = Node(f"Mover D1: {source}→{target}", 'move', level+1)
        edges.append((node_id, mid_id))
        
    return nodes, edges, node_id

def assign_coordinates(nodes, root_id, x_min, x_max, y_start, y_step):
    def layout(node_id, x_l, x_r, current_y):
        nodes[node_id].x = (x_l + x_r) / 2
        nodes[node_id].y = current_y
        
        children = [dst for src, dst in edges if src == node_id]
        if not children: return
        
        w = (x_r - x_l) / len(children)
        for i, child_id in enumerate(children):
            layout(child_id, x_l + i*w, x_l + (i+1)*w, current_y + y_step)

    # We need access to edges here
    layout(root_id, x_min, x_max, y_start)

def generate_tree(out_path, n_disks=3):
    """
    Generates a hierarchical recursion tree SVG programmatically (No Graphviz needed).
    """
    global edges
    nodes, edges, root_id = build_tree(n_disks, 'A', 'C', 'B')
    
    # Calculate SVG dimensions dynamically based on N
    depth = n_disks + 1
    width_per_leaf = 100
    leaves_count = 3**(n_disks-1) # rough estimate of max width
    
    W = max(1000, leaves_count * width_per_leaf)
    H = depth * 100 + 100
    
    assign_coordinates(nodes, root_id, 0, W, 80, 100)
    
    svg = [f'<svg width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
    svg.append('<style>.text { font-family: sans-serif; font-size: 13px; }</style>')
    svg.append(f'<text x="50" y="40" font-family="sans-serif" font-size="20" font-weight="bold" fill="#343a40">Árbol de Recursión de las Torres de Hanói para N={n_disks}</text>')
    
    # Draw edges
    for src, dst in edges:
        x1, y1 = nodes[src].x, nodes[src].y + 20
        x2, y2 = nodes[dst].x, nodes[dst].y - 20
        svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#adb5bd" stroke-width="2"/>')
        
    # Draw nodes
    for node_id, data in nodes.items():
        x, y = data.x, data.y
        if data.node_type == 'call':
            fill, stroke = '#e1f5fe', '#0288d1'
        else:
            fill, stroke = '#e8f5e9', '#388e3c'
            
        box_w, box_h = 130, 40
        svg.append(f'<rect x="{x-box_w/2}" y="{y-box_h/2}" width="{box_w}" height="{box_h}" fill="{fill}" stroke="{stroke}" stroke-width="2" rx="8"/>')
        svg.append(f'<text x="{x}" y="{y+5}" class="text" text-anchor="middle" fill="#212529">{data.label}</text>')
        
    svg.append('</svg>')
    with open(out_path, 'w', encoding='utf-8') as f: f.write('\n'.join(svg))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate Towers of Hanoi SVGs")
    parser.add_argument('--disks', type=int, default=3, help="Number of disks")
    args = parser.parse_args()
    
    out_dir = '05_RecursionAlgorithms/theory/assets'
    os.makedirs(out_dir, exist_ok=True)
    
    filmstrip_path = os.path.join(out_dir, f'hanoi_steps_{args.disks}.svg')
    tree_path = os.path.join(out_dir, f'hanoi_tree_{args.disks}.svg')
    
    generate_filmstrip(filmstrip_path, args.disks)
    generate_tree(tree_path, args.disks)
    
    print(f"Hanoi visuals for {args.disks} disks generated successfully in {out_dir}.")
