import os

def hanoi_steps(n, source, target, auxiliary, state, steps):
    if n == 1:
        # Move disk from source to target
        disk = state[source].pop()
        state[target].append(disk)
        # Deep copy state
        steps.append({k: list(v) for k, v in state.items()})
        return
    hanoi_steps(n-1, source, auxiliary, target, state, steps)
    disk = state[source].pop()
    state[target].append(disk)
    steps.append({k: list(v) for k, v in state.items()})
    hanoi_steps(n-1, auxiliary, target, source, state, steps)

def generate_filmstrip(out_path):
    # Simulate
    state = {'A': [3, 2, 1], 'B': [], 'C': []}
    steps = [{k: list(v) for k, v in state.items()}] # Initial state
    hanoi_steps(3, 'A', 'C', 'B', state, steps)
    
    # Drawing parameters
    W_frame = 300
    H_frame = 200
    cols = 4
    rows = 2
    
    W_total = cols * W_frame
    H_total = rows * H_frame
    
    svg = [f'<svg width="{W_total}" height="{H_total}" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<rect width="{W_total}" height="{H_total}" fill="#ffffff"/>')
    svg.append('<style>.text { font-family: sans-serif; }</style>')
    
    for i, step in enumerate(steps):
        r = i // cols
        c = i % cols
        
        ox = c * W_frame
        oy = r * H_frame
        
        # Border
        svg.append(f'<rect x="{ox+10}" y="{oy+10}" width="{W_frame-20}" height="{H_frame-20}" rx="10" fill="#f8f9fa" stroke="#dee2e6" stroke-width="2"/>')
        
        title = "Estado Inicial" if i == 0 else f"Paso {i}/7"
        svg.append(f'<text x="{ox+W_frame/2}" y="{oy+35}" class="text" font-size="16" font-weight="bold" text-anchor="middle" fill="#343a40">{title}</text>')
        
        # Pegs
        peg_y = oy + H_frame - 30
        for p, peg in enumerate(['A', 'B', 'C']):
            px = ox + (p+1) * (W_frame / 4)
            svg.append(f'<rect x="{px-3}" y="{oy+70}" width="6" height="{H_frame-100}" fill="#adb5bd" rx="3"/>')
            svg.append(f'<text x="{px}" y="{peg_y+20}" class="text" font-size="14" text-anchor="middle" fill="#6c757d">Torre {peg}</text>')
            
            # Disks
            disks = step[peg]
            for d_idx, d_size in enumerate(disks):
                dw = d_size * 20 + 20
                dh = 12
                dx = px - dw/2
                dy = peg_y - (d_idx+1)*dh - d_idx*2
                
                colors = {1: '#fca311', 2: '#14213d', 3: '#e63946'}
                svg.append(f'<rect x="{dx}" y="{dy}" width="{dw}" height="{dh}" fill="{colors[d_size]}" rx="4"/>')
                
    svg.append('</svg>')
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))


def generate_tree(out_path):
    # Tree data manually defined for Hanoi(3)
    nodes = {
        'H3': {'label': 'Hanoi(3, A→C, B)', 'type': 'call', 'x': 500, 'y': 50},
        
        'H2a': {'label': 'Hanoi(2, A→B, C)', 'type': 'call', 'x': 250, 'y': 150},
        'M3': {'label': 'Mover D3: A → C', 'type': 'move', 'x': 500, 'y': 150},
        'H2b': {'label': 'Hanoi(2, B→C, A)', 'type': 'call', 'x': 750, 'y': 150},
        
        'H1a': {'label': 'Hanoi(1, A→C, B)', 'type': 'call', 'x': 100, 'y': 250},
        'M2a': {'label': 'Mover D2: A → B', 'type': 'move', 'x': 250, 'y': 250},
        'H1b': {'label': 'Hanoi(1, C→B, A)', 'type': 'call', 'x': 400, 'y': 250},
        
        'H1c': {'label': 'Hanoi(1, B→A, C)', 'type': 'call', 'x': 600, 'y': 250},
        'M2b': {'label': 'Mover D2: B → C', 'type': 'move', 'x': 750, 'y': 250},
        'H1d': {'label': 'Hanoi(1, A→C, B)', 'type': 'call', 'x': 900, 'y': 250},
        
        'M1a': {'label': 'Mover D1: A → C', 'type': 'move', 'x': 100, 'y': 350},
        'M1b': {'label': 'Mover D1: C → B', 'type': 'move', 'x': 400, 'y': 350},
        'M1c': {'label': 'Mover D1: B → A', 'type': 'move', 'x': 600, 'y': 350},
        'M1d': {'label': 'Mover D1: A → C', 'type': 'move', 'x': 900, 'y': 350},
    }
    
    edges = [
        ('H3', 'H2a'), ('H3', 'M3'), ('H3', 'H2b'),
        ('H2a', 'H1a'), ('H2a', 'M2a'), ('H2a', 'H1b'),
        ('H2b', 'H1c'), ('H2b', 'M2b'), ('H2b', 'H1d'),
        ('H1a', 'M1a'), ('H1b', 'M1b'), ('H1c', 'M1c'), ('H1d', 'M1d')
    ]
    
    W = 1000
    H = 450
    
    svg = [f'<svg width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg">']
    svg.append(f'<rect width="{W}" height="{H}" fill="#ffffff"/>')
    svg.append('<style>.text { font-family: sans-serif; font-size: 14px; }</style>')
    
    # Edges
    for src, dst in edges:
        x1, y1 = nodes[src]['x'], nodes[src]['y'] + 20
        x2, y2 = nodes[dst]['x'], nodes[dst]['y'] - 20
        svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#adb5bd" stroke-width="2"/>')
        
    # Nodes
    for n, data in nodes.items():
        x, y = data['x'], data['y']
        
        if data['type'] == 'call':
            fill = '#e1f5fe'
            stroke = '#0288d1'
            if 'Hanoi(2' in data['label']:
                fill = '#fff3e0'
                stroke = '#f57c00'
            elif 'Hanoi(1' in data['label']:
                fill = '#f3e5f5'
                stroke = '#7b1fa2'
        else:
            fill = '#e8f5e9'
            stroke = '#388e3c'
            
        width = 140
        height = 40
        rx = 8
        svg.append(f'<rect x="{x-width/2}" y="{y-height/2}" width="{width}" height="{height}" fill="{fill}" stroke="{stroke}" stroke-width="2" rx="{rx}"/>')
        svg.append(f'<text x="{x}" y="{y+5}" class="text" text-anchor="middle" fill="#212529">{data["label"]}</text>')

    svg.append('</svg>')
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))

if __name__ == '__main__':
    generate_filmstrip('05_RecursionAlgorithms/theory/assets/hanoi_steps.svg')
    generate_tree('05_RecursionAlgorithms/theory/assets/hanoi_tree.svg')
    print("Visuals generated successfully in assets/ directory.")
