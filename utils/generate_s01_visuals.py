import os

def create_svg(w, h, content):
    return f'''<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">
<rect width="100%" height="100%" fill="#ffffff" />
<style>
  .title {{ font-family: sans-serif; font-size: 16px; font-weight: bold; fill: #343a40; }}
  .text {{ font-family: sans-serif; font-size: 13px; fill: #212529; }}
  .mono {{ font-family: monospace; font-size: 12px; fill: #e63946; font-weight: bold; }}
  .box {{ fill: #f8f9fa; stroke: #adb5bd; stroke-width: 2; }}
  .box-blue {{ fill: #e3f2fd; stroke: #1976d2; stroke-width: 2; }}
  .box-green {{ fill: #e8f5e9; stroke: #388e3c; stroke-width: 2; }}
</style>
<defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 z" fill="#adb5bd"/>
    </marker>
    <marker id="arrow-red" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 z" fill="#e63946"/>
    </marker>
</defs>
{content}
</svg>'''

def draw_box(x, y, w, h, title, sub, cls="box"):
    return f'''
    <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" class="{cls}"/>
    <text x="{x+w/2}" y="{y+25}" class="text" font-weight="bold" text-anchor="middle">{title}</text>
    <text x="{x+w/2}" y="{y+45}" class="mono" text-anchor="middle">{sub}</text>
    '''

def draw_arrow(x1, y1, x2, y2, label="", color="#adb5bd", marker="arrow"):
    res = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2" marker-end="url(#{marker})"/>'
    if label:
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2 - 10
        res += f'<text x="{mx}" y="{my}" class="text" font-size="11" text-anchor="middle" fill="#6c757d">{label}</text>'
    return res

def gen_l01():
    w, h = 900, 160
    c = f'<text class="title" x="30" y="30">C++ Compilation Pipeline</text>'
    boxes = [
        ("Source Code", "HelloWorld.cpp", "box"),
        ("Expanded Source", "#include expanded", "box-blue"),
        ("Assembly Code", "L01.s", "box-blue"),
        ("Object File", "L01.o / .obj", "box-blue"),
        ("Executable Binary", "L01.exe", "box-green")
    ]
    for i, (t, s, cls) in enumerate(boxes):
        x = 30 + i*170
        c += draw_box(x, 60, 140, 60, t, s, cls)
        if i > 0:
            labels = ["", "1. Preprocessor", "2. Compiler", "3. Assembler", "4. Linker"]
            c += draw_arrow(x-30, 90, x, 90, labels[i])
    with open("01_GettingStarted/theory/assets/L01_pipeline.svg", "w", encoding="utf-8") as f: f.write(create_svg(w, h, c))

def gen_l02():
    w, h = 600, 250
    c = f'<text class="title" x="30" y="30">Namespaces & Scope Hierarchy</text>'
    c += draw_box(230, 50, 140, 40, "Global Scope", "::", "box-blue")
    
    c += draw_box(50, 150, 140, 40, "namespace Graphics", "Graphics::", "box")
    c += draw_box(230, 150, 140, 40, "namespace Printer", "Printer::", "box")
    c += draw_box(410, 150, 140, 40, "namespace std", "std::", "box-green")
    
    c += draw_arrow(300, 90, 120, 150)
    c += draw_arrow(300, 90, 300, 150)
    c += draw_arrow(300, 90, 480, 150)
    
    c += f'<text class="mono" x="120" y="215" text-anchor="middle">print()</text>'
    c += f'<text class="mono" x="300" y="215" text-anchor="middle">print()</text>'
    c += f'<text class="mono" x="480" y="215" text-anchor="middle">cout, cin, string</text>'
    
    with open("01_GettingStarted/theory/assets/L02_namespaces.svg", "w", encoding="utf-8") as f: f.write(create_svg(w, h, c))

def gen_l03():
    w, h = 750, 200
    c = f'<text class="title" x="30" y="30">I/O Buffer Flushing: \\n vs std::endl</text>'
    
    c += draw_box(30, 60, 200, 40, "std::cout << 'Text\\n'", "", "box")
    c += draw_box(30, 130, 200, 40, "std::cout << std::endl", "", "box")
    
    c += draw_box(350, 95, 140, 40, "RAM I/O Buffer", "Pending Output", "box-blue")
    c += draw_box(580, 95, 140, 40, "OS Console", "Screen", "box-green")
    
    c += draw_arrow(230, 80, 350, 110, "Fast (Write to RAM)")
    c += draw_arrow(230, 150, 350, 120, "Slower (Write to RAM)")
    c += draw_arrow(490, 115, 580, 115, "Forced Flush", "#e63946", "arrow-red")
    
    with open("01_GettingStarted/theory/assets/L03_flush.svg", "w", encoding="utf-8") as f: f.write(create_svg(w, h, c))

def gen_l04():
    w, h = 800, 160
    c = f'<text class="title" x="30" y="30">C++ Stream I/O Architecture</text>'
    
    c += draw_box(30, 60, 120, 60, "[User Keyboard]", "Input", "box")
    c += draw_box(220, 60, 140, 60, "std::cin", "Stream Buffer", "box-blue")
    c += draw_box(430, 60, 140, 60, "Variable in RAM", "int, string", "box-green")
    c += draw_box(640, 60, 120, 60, "std::cout", "Console Screen", "box-blue")
    
    c += draw_arrow(150, 90, 220, 90, "Keystrokes")
    c += draw_arrow(360, 90, 430, 90, ">> (Extract)")
    c += draw_arrow(570, 90, 640, 90, "<< (Insert)")
    
    with open("01_GettingStarted/theory/assets/L04_io.svg", "w", encoding="utf-8") as f: f.write(create_svg(w, h, c))

def gen_l05():
    w, h = 400, 450
    c = f'<text class="title" x="200" y="30" text-anchor="middle">Interactive Profile App Flow</text>'
    
    y = 60
    steps = [
        ("Program Launch", ""),
        ("Print ASCII Banner Header", "std::cout"),
        ("Prompt & Extract Name", "std::string"),
        ("Prompt & Extract Subject", "std::string"),
        ("Prompt & Extract Lucky Number", "int"),
        ("Format & Render Profile Card", ""),
        ("Return 0 (Success)", "")
    ]
    
    for i, (t, s) in enumerate(steps):
        cls = "box-green" if i in [0, 6] else ("box-blue" if "Extract" in t else "box")
        c += draw_box(100, y, 200, 40, t, s, cls)
        if i < len(steps)-1:
            c += draw_arrow(200, y+40, 200, y+60)
        y += 60
        
    with open("01_GettingStarted/theory/assets/L05_profile.svg", "w", encoding="utf-8") as f: f.write(create_svg(w, h, c))

if __name__ == '__main__':
    os.makedirs("01_GettingStarted/theory/assets", exist_ok=True)
    gen_l01()
    gen_l02()
    gen_l03()
    gen_l04()
    gen_l05()
    print("Section 01 SVGs successfully generated!")
