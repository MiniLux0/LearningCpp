import os

def gen_animated_binary_search(path):
    svg = '''<svg width="700" height="250" xmlns="http://www.w3.org/2000/svg">
<rect width="700" height="250" fill="#ffffff"/>
<style>
    text { font-family: 'Segoe UI', Roboto, Helvetica, sans-serif; }
    .box { fill: #f8f9fa; stroke: #dee2e6; stroke-width: 2; transition: all 0.5s; }
    .box-text { font-size: 18px; font-weight: bold; fill: #343a40; }
    
    /* Pointers */
    .ptr { font-size: 14px; font-weight: bold; }
    .ptr-line { stroke-width: 2; stroke-dasharray: 4; }
    
    /* Animations for Target = 25 */
    @keyframes low-move {
        0%, 30% { transform: translateX(0px); opacity: 1; }
        35%, 100% { transform: translateX(320px); opacity: 1; }
    }
    @keyframes high-move {
        0%, 60% { transform: translateX(0px); opacity: 1; }
        65%, 100% { transform: translateX(-160px); opacity: 1; }
    }
    @keyframes mid-move {
        0%, 30% { transform: translateX(0px); }     /* idx 3 */
        35%, 60% { transform: translateX(160px); }  /* idx 5 */
        65%, 100% { transform: translateX(80px); }  /* idx 4 */
    }
    
    /* Fading discarded halves */
    @keyframes fade-left {
        0%, 30% { fill: #f8f9fa; stroke: #dee2e6; }
        35%, 100% { fill: #f1f3f5; stroke: #e9ecef; opacity: 0.3; }
    }
    @keyframes fade-right {
        0%, 60% { fill: #f8f9fa; stroke: #dee2e6; }
        65%, 100% { fill: #f1f3f5; stroke: #e9ecef; opacity: 0.3; }
    }
    
    /* Highlight found */
    @keyframes pulse-found {
        0%, 70% { fill: #f8f9fa; stroke: #dee2e6; }
        75%, 100% { fill: #d4edda; stroke: #28a745; stroke-width: 4; }
    }

    #low-group { animation: low-move 10s infinite; }
    #high-group { animation: high-move 10s infinite; }
    #mid-group { animation: mid-move 10s infinite; }
    
    .fade-l { animation: fade-left 10s infinite; }
    .fade-r { animation: fade-right 10s infinite; }
    #box4 { animation: pulse-found 10s infinite; }
</style>

<text x="350" y="30" font-size="20" font-weight="bold" text-anchor="middle" fill="#212529">Binary Search Animado: Buscando el valor 25</text>

<g transform="translate(70, 100)">
'''
    arr = [2, 7, 12, 19, 25, 30, 42]
    # Draw boxes
    for i, val in enumerate(arr):
        cls = ""
        if i <= 3: cls = "fade-l box"
        elif i >= 5: cls = "fade-r box"
        else: cls = "box"
        
        svg += f'    <rect id="box{i}" class="{cls}" x="{i*80}" y="0" width="60" height="60" rx="8" />\n'
        svg += f'    <text x="{i*80 + 30}" y="36" class="box-text" text-anchor="middle">{val}</text>\n'
        svg += f'    <text x="{i*80 + 30}" y="75" font-size="12" fill="#adb5bd" text-anchor="middle">[{i}]</text>\n'

    # Draw pointers
    # Low starts at 0 (x=30)
    svg += '''
    <!-- LOW -->
    <g id="low-group">
        <line x1="30" y1="130" x2="30" y2="85" class="ptr-line" stroke="#0288d1"/>
        <text x="30" y="145" class="ptr" fill="#0288d1" text-anchor="middle">low</text>
    </g>
    
    <!-- HIGH starts at 6 (x=30 + 6*80 = 510) -->
    <g id="high-group">
        <line x1="510" y1="130" x2="510" y2="85" class="ptr-line" stroke="#d32f2f"/>
        <text x="510" y="145" class="ptr" fill="#d32f2f" text-anchor="middle">high</text>
    </g>
    
    <!-- MID starts at 3 (x=30 + 3*80 = 270) -->
    <g id="mid-group">
        <line x1="270" y1="-45" x2="270" y2="-10" class="ptr-line" stroke="#f57c00"/>
        <text x="270" y="-55" class="ptr" fill="#f57c00" text-anchor="middle">mid</text>
    </g>
</g>
</svg>'''
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    out_dir = "05_RecursionAlgorithms/theory/assets"
    os.makedirs(out_dir, exist_ok=True)
    gen_animated_binary_search(os.path.join(out_dir, "binary_search.svg"))
    print("Animated Binary Search SVG generated!")
