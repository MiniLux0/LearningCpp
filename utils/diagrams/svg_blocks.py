import os

def gen_hanoi(path):
    svg = '''<svg width="1000" height="360" xmlns="http://www.w3.org/2000/svg">
<rect width="1000" height="360" fill="#ffffff"/>
<style>text { font-family: sans-serif; }</style>'''
    
    # Hanoi has 7 steps for 3 disks. We'll draw 4 frames (Start, Step 1, Step 3, End)
    # Actually, let's draw 8 frames (2 rows of 4) to show all 7 steps.
    
    states = [
        ("Estado Inicial", [[3,2,1], [], []]),
        ("Paso 1 (1 a C)", [[3,2], [], [1]]),
        ("Paso 2 (2 a B)", [[3], [2], [1]]),
        ("Paso 3 (1 a B)", [[3], [2,1], []]),
        ("Paso 4 (3 a C)", [[], [2,1], [3]]),
        ("Paso 5 (1 a A)", [[1], [2], [3]]),
        ("Paso 6 (2 a C)", [[1], [], [3,2]]),
        ("Paso 7 (1 a C)", [[], [], [3,2,1]])
    ]
    
    colors = {3: "#e63946", 2: "#14213d", 1: "#fca311"}
    widths = {3: 60, 2: 45, 1: 30}
    
    for i, (title, pegs) in enumerate(states):
        row = i // 4
        col = i % 4
        x_base = 10 + col * 240
        y_base = 10 + row * 180
        
        svg += f'<rect x="{x_base}" y="{y_base}" width="230" height="160" rx="10" fill="#f8f9fa" stroke="#dee2e6" stroke-width="2"/>\n'
        svg += f'<text x="{x_base + 115}" y="{y_base + 25}" font-size="14" font-weight="bold" text-anchor="middle" fill="#343a40">{title}</text>\n'
        
        for p in range(3):
            px = x_base + 50 + p * 65
            # Peg
            svg += f'<rect x="{px - 2}" y="{y_base + 50}" width="4" height="90" fill="#adb5bd" rx="2"/>\n'
            svg += f'<text x="{px}" y="{y_base + 155}" font-size="12" text-anchor="middle" fill="#6c757d">Torre {chr(65+p)}</text>\n'
            
            # Disks
            for d_idx, disk in enumerate(pegs[p]):
                dw = widths[disk]
                dy = y_base + 130 - d_idx * 12
                svg += f'<rect x="{px - dw/2}" y="{dy}" width="{dw}" height="10" fill="{colors[disk]}" rx="3"/>\n'

    svg += '</svg>'
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)

def draw_array(x, y, arr, highlights=None, pointers=None, title="", w=40, h=40):
    svg = f'<text x="{x}" y="{y-10}" font-size="12" font-weight="bold" fill="#343a40">{title}</text>\n'
    if highlights is None: highlights = []
    if pointers is None: pointers = {}
    
    for i, val in enumerate(arr):
        bx = x + i * w
        bg = "#ffcdd2" if i in highlights else "#e1f5fe"
        svg += f'<rect x="{bx}" y="{y}" width="{w}" height="{h}" fill="{bg}" stroke="#0288d1" stroke-width="2"/>\n'
        svg += f'<text x="{bx + w/2}" y="{y + h/2 + 5}" font-size="14" text-anchor="middle" fill="#000000">{val}</text>\n'
        svg += f'<text x="{bx + w/2}" y="{y + h + 15}" font-size="10" text-anchor="middle" fill="#6c757d">[{i}]</text>\n'
        
        if i in pointers:
            svg += f'<text x="{bx + w/2}" y="{y + h + 30}" font-size="12" text-anchor="middle" fill="#d32f2f" font-weight="bold">{pointers[i]}</text>\n'
            
    return svg

def gen_bubble(path):
    svg = '''<svg width="600" height="300" xmlns="http://www.w3.org/2000/svg">
<rect width="600" height="300" fill="#ffffff"/>
<style>text { font-family: sans-serif; }</style>'''
    svg += draw_array(20, 40, [5,1,4,2,8], highlights=[0,1], title="Paso 1: Comparar 5 y 1 (Swap)")
    svg += draw_array(20, 140, [1,5,4,2,8], highlights=[1,2], title="Paso 2: Comparar 5 y 4 (Swap)")
    svg += draw_array(20, 240, [1,4,5,2,8], highlights=[2,3], title="Paso 3: Comparar 5 y 2 (Swap)")
    svg += '</svg>'
    with open(path, "w", encoding="utf-8") as f: f.write(svg)

def gen_selection(path):
    svg = '''<svg width="600" height="300" xmlns="http://www.w3.org/2000/svg">
<rect width="600" height="300" fill="#ffffff"/>
<style>text { font-family: sans-serif; }</style>'''
    svg += draw_array(20, 40, [64,25,12,22,11], highlights=[0,4], title="Paso 1: Mínimo es 11, Swap con pos 0")
    svg += draw_array(20, 140, [11,25,12,22,64], highlights=[1,2], title="Paso 2: Mínimo es 12, Swap con pos 1")
    svg += draw_array(20, 240, [11,12,25,22,64], highlights=[2,3], title="Paso 3: Mínimo es 22, Swap con pos 2")
    svg += '</svg>'
    with open(path, "w", encoding="utf-8") as f: f.write(svg)

def gen_insertion(path):
    svg = '''<svg width="600" height="300" xmlns="http://www.w3.org/2000/svg">
<rect width="600" height="300" fill="#ffffff"/>
<style>text { font-family: sans-serif; }</style>'''
    svg += draw_array(20, 40, [12,11,13,5,6], highlights=[1], title="Paso 1: Insertar 11 antes de 12")
    svg += draw_array(20, 140, [11,12,13,5,6], highlights=[2], title="Paso 2: 13 ya está en posición")
    svg += draw_array(20, 240, [11,12,13,5,6], highlights=[3], title="Paso 3: Insertar 5 al principio")
    svg += '</svg>'
    with open(path, "w", encoding="utf-8") as f: f.write(svg)

def gen_binary(path):
    svg = '''<svg width="600" height="200" xmlns="http://www.w3.org/2000/svg">
<rect width="600" height="200" fill="#ffffff"/>
<style>text { font-family: sans-serif; }</style>'''
    svg += draw_array(20, 60, [2,7,12,19,25,30,42], highlights=[3], pointers={1: "low", 3: "mid (Target!)", 5: "high"}, title="Binary Search: Target 19")
    svg += '</svg>'
    with open(path, "w", encoding="utf-8") as f: f.write(svg)

if __name__ == "__main__":
    base = "05_RecursionAlgorithms/theory/assets"
    gen_hanoi(os.path.join(base, "hanoi_steps_3.svg"))
    gen_bubble(os.path.join(base, "bubble_sort.svg"))
    gen_selection(os.path.join(base, "selection_sort.svg"))
    gen_insertion(os.path.join(base, "insertion_sort.svg"))
    gen_binary(os.path.join(base, "binary_search.svg"))
    print("Native graphical SVGs generated successfully!")
