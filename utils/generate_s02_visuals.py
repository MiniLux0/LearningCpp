import os

def create_svg(w, h, content):
    return f'''<svg width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">
<rect width="100%" height="100%" fill="#ffffff" />
<style>
  .title {{ font-family: sans-serif; font-size: 16px; font-weight: bold; fill: #343a40; }}
  .text {{ font-family: sans-serif; font-size: 13px; fill: #212529; }}
  .mono {{ font-family: monospace; font-size: 12px; fill: #e63946; font-weight: bold; }}
  .box {{ fill: #f8f9fa; stroke: #adb5bd; stroke-width: 2; }}
  .box-blue {{ fill: #e1f5fe; stroke: #0288d1; stroke-width: 2; }}
  .box-green {{ fill: #e8f5e9; stroke: #388e3c; stroke-width: 2; }}
  .box-orange {{ fill: #fff3e0; stroke: #f57c00; stroke-width: 2; }}
  .box-red {{ fill: #ffebee; stroke: #d32f2f; stroke-width: 2; }}
  .diamond {{ fill: #fff8e1; stroke: #ffb300; stroke-width: 2; }}
</style>
<defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 z" fill="#adb5bd"/>
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 z" fill="#388e3c"/>
    </marker>
    <marker id="arrow-red" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 z" fill="#d32f2f"/>
    </marker>
</defs>
{content}
</svg>'''

def draw_rect(x, y, w, h, t, s="", cls="box", rx=8):
    c = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cls}"/>\n'
    if s:
        c += f'<text x="{x+w/2}" y="{y+h/2-6}" class="text" font-weight="bold" text-anchor="middle">{t}</text>\n'
        c += f'<text x="{x+w/2}" y="{y+h/2+14}" class="mono" text-anchor="middle">{s}</text>\n'
    else:
        c += f'<text x="{x+w/2}" y="{y+h/2+4}" class="text" font-weight="bold" text-anchor="middle">{t}</text>\n'
    return c

def draw_diamond(x, y, w, h, t):
    pts = f"{x+w/2},{y} {x+w},{y+h/2} {x+w/2},{y+h} {x},{y+h/2}"
    c = f'<polygon points="{pts}" class="diamond"/>\n'
    c += f'<text x="{x+w/2}" y="{y+h/2+4}" class="text" font-weight="bold" text-anchor="middle">{t}</text>\n'
    return c

def draw_arrow(x1, y1, x2, y2, label="", color="#adb5bd", marker="arrow"):
    c = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2" marker-end="url(#{marker})"/>\n'
    if label:
        mx, my = (x1+x2)/2, (y1+y2)/2 - 8
        c += f'<text x="{mx}" y="{my}" class="text" font-size="11" text-anchor="middle" fill="{color}">{label}</text>\n'
    return c

def draw_path(d, label="", color="#adb5bd", marker="arrow", lx=0, ly=0):
    c = f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2" marker-end="url(#{marker})"/>\n'
    if label:
        c += f'<text x="{lx}" y="{ly}" class="text" font-size="11" text-anchor="middle" fill="{color}">{label}</text>\n'
    return c

def gen_l13():
    c = '<text class="title" x="50" y="30">If Statement Control Flow</text>\n'
    c += draw_rect(150, 50, 100, 40, "Program Flow", "", "box")
    c += draw_arrow(200, 90, 200, 120)
    c += draw_diamond(120, 120, 160, 60, "Condition == true?")
    
    # True path
    c += draw_arrow(200, 180, 200, 220, "Yes (true)", "#388e3c", "arrow-green")
    c += draw_rect(130, 220, 140, 40, "Execute Block { }", "", "box-green")
    c += draw_arrow(200, 260, 200, 300)
    
    # False path
    c += draw_path("M 120 150 L 50 150 L 50 280 L 180 280", "No (false)", "#d32f2f", "arrow-red", 85, 140)
    
    c += draw_rect(130, 300, 140, 40, "Continue Execution", "", "box")
    with open("02_BasicSyntax/theory/assets/L13_If.svg", "w") as f: f.write(create_svg(350, 380, c))

def gen_l14():
    c = '<text class="title" x="80" y="30">If-Else Statement Flow</text>\n'
    c += draw_diamond(120, 60, 160, 60, "Condition == true?")
    
    # True
    c += draw_path("M 120 90 L 80 90 L 80 140", "True", "#388e3c", "arrow-green", 100, 80)
    c += draw_rect(30, 140, 100, 40, "'if' Block", "", "box-green")
    c += draw_path("M 80 180 L 80 230 L 180 230", "", "#adb5bd", "arrow", 0, 0)
    
    # False
    c += draw_path("M 280 90 L 320 90 L 320 140", "False", "#d32f2f", "arrow-red", 300, 80)
    c += draw_rect(270, 140, 100, 40, "'else' Block", "", "box-red")
    c += draw_path("M 320 180 L 320 230 L 220 230", "", "#adb5bd", "arrow", 0, 0)
    
    c += draw_rect(130, 250, 140, 40, "Resume Flow", "", "box")
    with open("02_BasicSyntax/theory/assets/L14_IfElse.svg", "w") as f: f.write(create_svg(400, 320, c))

def gen_l18():
    c = '<text class="title" x="50" y="30">While Loop Execution</text>\n'
    c += draw_diamond(120, 60, 160, 60, "Condition == true?")
    
    # True loop
    c += draw_arrow(200, 120, 200, 160, "True", "#388e3c", "arrow-green")
    c += draw_rect(120, 160, 160, 40, "Execute Body { }", "", "box-green")
    c += draw_path("M 120 180 L 50 180 L 50 90 L 110 90", "Loop Back", "#0288d1", "arrow", 85, 170)
    
    # False exit
    c += draw_path("M 280 90 L 350 90 L 350 250 L 220 250", "False", "#d32f2f", "arrow-red", 315, 80)
    c += draw_rect(130, 270, 140, 40, "Exit Loop", "", "box")
    
    with open("02_BasicSyntax/theory/assets/L18_WhileLoops.svg", "w") as f: f.write(create_svg(400, 350, c))

def gen_l20():
    c = '<text class="title" x="30" y="30">For Loop Pipeline</text>\n'
    c += draw_rect(30, 60, 120, 50, "1. Init", "int i = 0", "box-blue")
    c += draw_arrow(150, 85, 200, 85)
    
    c += draw_diamond(200, 55, 140, 60, "2. Cond: i < 5")
    
    c += draw_arrow(270, 115, 270, 160, "True", "#388e3c", "arrow-green")
    c += draw_rect(200, 160, 140, 40, "3. Execute Body", "", "box-green")
    
    c += draw_arrow(200, 180, 130, 180)
    c += draw_rect(30, 160, 100, 40, "4. Step", "i++", "box-orange")
    
    c += draw_path("M 80 160 L 80 130 L 220 130 L 220 105", "", "#adb5bd", "arrow")
    
    c += draw_arrow(340, 85, 410, 85, "False", "#d32f2f", "arrow-red")
    c += draw_rect(410, 65, 100, 40, "Exit Loop", "", "box")
    
    with open("02_BasicSyntax/theory/assets/L20_ForLoops.svg", "w") as f: f.write(create_svg(550, 230, c))

def gen_l06():
    c = '<text class="title" x="30" y="30">Variable Memory Allocation</text>\n'
    c += draw_rect(30, 50, 160, 40, "int age = 25;", "", "box-blue")
    c += draw_arrow(190, 70, 260, 70, "Allocates")
    c += draw_rect(260, 50, 140, 60, "RAM: 0x7FFA", "Value: 25", "box-green")
    with open("02_BasicSyntax/theory/assets/L06_Variables.svg", "w") as f: f.write(create_svg(450, 150, c))

def gen_l09():
    c = '<text class="title" x="30" y="30">Bitwise Operations</text>\n'
    c += draw_rect(30, 50, 140, 40, "a = 12 (1100)", "", "box-blue")
    c += draw_rect(200, 50, 140, 40, "b = 5 (0101)", "", "box-blue")
    
    c += draw_arrow(100, 90, 100, 130)
    c += draw_arrow(270, 90, 100, 130)
    c += draw_rect(30, 130, 160, 40, "a & b = 4 (0100)", "", "box-green")
    
    c += draw_arrow(120, 90, 280, 130)
    c += draw_arrow(270, 90, 280, 130)
    c += draw_rect(210, 130, 160, 40, "a | b = 13 (1101)", "", "box-orange")
    with open("02_BasicSyntax/theory/assets/L09_BinaryNumbers.svg", "w") as f: f.write(create_svg(420, 200, c))

def gen_l15():
    c = '<text class="title" x="50" y="30">If-ElseIf-Else Ladder</text>\n'
    c += draw_diamond(120, 50, 160, 60, "score >= 90?")
    c += draw_arrow(280, 80, 320, 80, "Yes", "#388e3c", "arrow-green")
    c += draw_rect(320, 60, 100, 40, "Grade = A", "", "box-green")
    
    c += draw_arrow(200, 110, 200, 140, "No", "#d32f2f", "arrow-red")
    c += draw_diamond(120, 140, 160, 60, "score >= 80?")
    c += draw_arrow(280, 170, 320, 170, "Yes", "#388e3c", "arrow-green")
    c += draw_rect(320, 150, 100, 40, "Grade = B", "", "box-green")
    
    c += draw_arrow(200, 200, 200, 230, "No", "#d32f2f", "arrow-red")
    c += draw_rect(150, 230, 100, 40, "Grade = C", "", "box-orange")
    with open("02_BasicSyntax/theory/assets/L15_IfElseIfElse.svg", "w") as f: f.write(create_svg(500, 300, c))

def gen_l22():
    c = '<text class="title" x="50" y="30">Switch Statement (Jump Table)</text>\n'
    c += draw_rect(150, 50, 100, 40, "switch (val)", "", "box-blue")
    c += draw_arrow(200, 90, 200, 120)
    c += draw_diamond(120, 120, 160, 60, "Jump Table Index")
    
    c += draw_arrow(120, 150, 50, 200, "case 1")
    c += draw_rect(10, 200, 100, 40, "Block 1", "", "box")
    
    c += draw_arrow(200, 180, 200, 200, "case 2")
    c += draw_rect(150, 200, 100, 40, "Block 2", "", "box")
    
    c += draw_arrow(280, 150, 350, 200, "default")
    c += draw_rect(290, 200, 100, 40, "Default Block", "", "box-orange")
    with open("02_BasicSyntax/theory/assets/L22_Switch.svg", "w") as f: f.write(create_svg(420, 270, c))

if __name__ == '__main__':
    os.makedirs("02_BasicSyntax/theory/assets", exist_ok=True)
    gen_l06()
    gen_l09()
    gen_l13()
    gen_l14()
    gen_l15()
    gen_l18()
    gen_l20()
    gen_l22()
    print("Section 02 critical flowcharts generated!")
