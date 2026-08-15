import os

def create_svg(w, h, content):
    return f'''<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">
<rect width="100%" height="100%" fill="#ffffff" />
<style>
  .title {{ font-family: sans-serif; font-size: 16px; font-weight: bold; fill: #343a40; }}
  .text {{ font-family: sans-serif; font-size: 14px; fill: #212529; }}
  .mono {{ font-family: monospace; font-size: 14px; fill: #e63946; font-weight: bold; }}
  .addr {{ font-family: monospace; font-size: 12px; fill: #6c757d; }}
  .node {{ fill: #e1f5fe; stroke: #0288d1; stroke-width: 2; }}
  .node-memo {{ fill: #ffe0b2; stroke: #f57c00; stroke-width: 2; }}
  .node-base {{ fill: #e8f5e9; stroke: #388e3c; stroke-width: 2; }}
  .box {{ fill: #f8f9fa; stroke: #adb5bd; stroke-width: 2; }}
  .box-pivot {{ fill: #ffcdd2; stroke: #d32f2f; stroke-width: 2; }}
  .box-sorted {{ fill: #c8e6c9; stroke: #388e3c; stroke-width: 2; }}
</style>
{content}
</svg>'''

def draw_tree(nodes, edges, w, h, title):
    content = f'<text class="title" x="50" y="40">{title}</text>\n'
    for src, dst in edges:
        x1, y1 = nodes[src]['x'], nodes[src]['y'] + 15
        x2, y2 = nodes[dst]['x'], nodes[dst]['y'] - 15
        content += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#adb5bd" stroke-width="2"/>\n'
    for n, data in nodes.items():
        x, y = data['x'], data['y']
        cls = data.get('class', 'node')
        content += f'<rect x="{x-35}" y="{y-15}" width="70" height="30" rx="15" class="{cls}"/>\n'
        content += f'<text x="{x}" y="{y+5}" class="text" text-anchor="middle">{data["label"]}</text>\n'
    return create_svg(w, h, content)

def generate_fib():
    # fib(4) tree
    nodes = {
        'F4': {'label': 'fib(4)', 'x': 300, 'y': 80},
        'F3': {'label': 'fib(3)', 'x': 150, 'y': 150},
        'F2_A': {'label': 'fib(2)', 'x': 450, 'y': 150},
        'F2_B': {'label': 'fib(2)', 'x': 75, 'y': 220},
        'F1_A': {'label': 'fib(1)', 'x': 225, 'y': 220, 'class': 'node-base'},
        'F1_B': {'label': 'fib(1)', 'x': 375, 'y': 220, 'class': 'node-base'},
        'F0_A': {'label': 'fib(0)', 'x': 525, 'y': 220, 'class': 'node-base'},
        'F1_C': {'label': 'fib(1)', 'x': 35, 'y': 290, 'class': 'node-base'},
        'F0_B': {'label': 'fib(0)', 'x': 115, 'y': 290, 'class': 'node-base'}
    }
    edges = [
        ('F4', 'F3'), ('F4', 'F2_A'),
        ('F3', 'F2_B'), ('F3', 'F1_A'),
        ('F2_A', 'F1_B'), ('F2_A', 'F0_A'),
        ('F2_B', 'F1_C'), ('F2_B', 'F0_B')
    ]
    with open('05_RecursionAlgorithms/theory/assets/fib_tree.svg', 'w') as f:
        f.write(draw_tree(nodes, edges, 600, 350, "Fibonacci Recursion Tree: O(2^N) Exponential Growth"))
        
    # Memoized version
    nodes['F2_A']['class'] = 'node-memo'
    nodes['F1_B']['class'] = 'node-memo'
    nodes['F0_A']['class'] = 'node-memo'
    with open('05_RecursionAlgorithms/theory/assets/fib_memo_tree.svg', 'w') as f:
        f.write(draw_tree(nodes, edges, 600, 350, "Memoized Fibonacci Tree: Overlapping Subproblems Pruned (O(N))"))

def generate_binary_search():
    arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    boxes = ""
    for i, v in enumerate(arr):
        x = 50 + i * 50
        bg = "#e3f2fd" if i == 4 else "#f8f9fa" # highlight 16
        stroke = "#1976d2" if i == 4 else "#adb5bd"
        boxes += f'<rect x="{x}" y="80" width="40" height="40" rx="4" fill="{bg}" stroke="{stroke}" stroke-width="2"/>\n'
        boxes += f'<text x="{x+20}" y="105" class="text" text-anchor="middle" font-weight="bold">{v}</text>\n'
        boxes += f'<text x="{x+20}" y="140" class="addr" text-anchor="middle">{i}</text>\n'
        
        if i == 0:
            boxes += f'<text x="{x+20}" y="60" class="mono" text-anchor="middle" fill="#d32f2f">low</text>\n'
            boxes += f'<line x1="{x+20}" y1="65" x2="{x+20}" y2="75" stroke="#d32f2f" stroke-width="2"/>\n'
        elif i == 4:
            boxes += f'<text x="{x+20}" y="60" class="mono" text-anchor="middle" fill="#388e3c">mid</text>\n'
            boxes += f'<line x1="{x+20}" y1="65" x2="{x+20}" y2="75" stroke="#388e3c" stroke-width="2"/>\n'
        elif i == 9:
            boxes += f'<text x="{x+20}" y="60" class="mono" text-anchor="middle" fill="#1976d2">high</text>\n'
            boxes += f'<line x1="{x+20}" y1="65" x2="{x+20}" y2="75" stroke="#1976d2" stroke-width="2"/>\n'

    content = f'''
    <text class="title" x="50" y="30">Binary Search Execution: target = 16</text>
    {boxes}
    <text class="text" x="50" y="180">Formula: mid = low + (high - low) / 2</text>
    '''
    with open('05_RecursionAlgorithms/theory/assets/binary_search.svg', 'w') as f: f.write(create_svg(600, 220, content))

def generate_merge_sort():
    content = '''
    <text class="title" x="50" y="40">Merge Sort: Divide & Conquer (O(N log N))</text>
    
    <!-- Level 0: [38, 27, 43, 3] -->
    <rect class="box" x="250" y="70" width="160" height="30" rx="4"/>
    <text class="mono" x="330" y="90" text-anchor="middle" fill="#212529">[ 38, 27, 43, 3 ]</text>
    
    <!-- Level 1: [38, 27] | [43, 3] -->
    <line x1="330" y1="100" x2="200" y2="130" stroke="#adb5bd" stroke-width="2"/>
    <line x1="330" y1="100" x2="460" y2="130" stroke="#adb5bd" stroke-width="2"/>
    
    <rect class="box" x="160" y="130" width="80" height="30" rx="4"/>
    <text class="mono" x="200" y="150" text-anchor="middle" fill="#212529">[ 38, 27 ]</text>
    <rect class="box" x="420" y="130" width="80" height="30" rx="4"/>
    <text class="mono" x="460" y="150" text-anchor="middle" fill="#212529">[ 43, 3 ]</text>
    
    <!-- Level 2: [38] [27] | [43] [3] -->
    <line x1="200" y1="160" x2="160" y2="190" stroke="#adb5bd" stroke-width="2"/>
    <line x1="200" y1="160" x2="240" y2="190" stroke="#adb5bd" stroke-width="2"/>
    <line x1="460" y1="160" x2="420" y2="190" stroke="#adb5bd" stroke-width="2"/>
    <line x1="460" y1="160" x2="500" y2="190" stroke="#adb5bd" stroke-width="2"/>
    
    <rect class="box" x="140" y="190" width="40" height="30" rx="4" fill="#e8f5e9" stroke="#388e3c"/>
    <text class="mono" x="160" y="210" text-anchor="middle" fill="#388e3c">[ 38 ]</text>
    <rect class="box" x="220" y="190" width="40" height="30" rx="4" fill="#e8f5e9" stroke="#388e3c"/>
    <text class="mono" x="240" y="210" text-anchor="middle" fill="#388e3c">[ 27 ]</text>
    
    <rect class="box" x="400" y="190" width="40" height="30" rx="4" fill="#e8f5e9" stroke="#388e3c"/>
    <text class="mono" x="420" y="210" text-anchor="middle" fill="#388e3c">[ 43 ]</text>
    <rect class="box" x="480" y="190" width="40" height="30" rx="4" fill="#e8f5e9" stroke="#388e3c"/>
    <text class="mono" x="500" y="210" text-anchor="middle" fill="#388e3c">[ 3 ]</text>
    
    <text class="text" x="550" y="210" fill="#6c757d">&lt;-- Base Cases (Size 1)</text>
    
    <!-- Level 3 (Merge): [27, 38] | [3, 43] -->
    <line x1="160" y1="220" x2="200" y2="250" stroke="#adb5bd" stroke-width="2" stroke-dasharray="4"/>
    <line x1="240" y1="220" x2="200" y2="250" stroke="#adb5bd" stroke-width="2" stroke-dasharray="4"/>
    <line x1="420" y1="220" x2="460" y2="250" stroke="#adb5bd" stroke-width="2" stroke-dasharray="4"/>
    <line x1="500" y1="220" x2="460" y2="250" stroke="#adb5bd" stroke-width="2" stroke-dasharray="4"/>
    
    <rect class="box" x="160" y="250" width="80" height="30" rx="4" fill="#e3f2fd" stroke="#1976d2"/>
    <text class="mono" x="200" y="270" text-anchor="middle" fill="#1976d2">[ 27, 38 ]</text>
    <rect class="box" x="420" y="250" width="80" height="30" rx="4" fill="#e3f2fd" stroke="#1976d2"/>
    <text class="mono" x="460" y="270" text-anchor="middle" fill="#1976d2">[ 3, 43 ]</text>
    
    <!-- Level 4 (Merge): [3, 27, 38, 43] -->
    <line x1="200" y1="280" x2="330" y2="310" stroke="#adb5bd" stroke-width="2" stroke-dasharray="4"/>
    <line x1="460" y1="280" x2="330" y2="310" stroke="#adb5bd" stroke-width="2" stroke-dasharray="4"/>
    
    <rect class="box" x="250" y="310" width="160" height="30" rx="4" fill="#c8e6c9" stroke="#388e3c"/>
    <text class="mono" x="330" y="330" text-anchor="middle" fill="#388e3c">[ 3, 27, 38, 43 ]</text>
    '''
    with open('05_RecursionAlgorithms/theory/assets/merge_sort.svg', 'w') as f: f.write(create_svg(700, 380, content))

if __name__ == '__main__':
    if not os.path.exists('05_RecursionAlgorithms/theory/assets'):
        os.makedirs('05_RecursionAlgorithms/theory/assets')
    generate_fib()
    generate_binary_search()
    generate_merge_sort()
    print("Algorithm visuals generated successfully.")
