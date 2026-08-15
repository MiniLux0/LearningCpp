import os
import graphviz

# Force add Graphviz default install paths to PATH
for g_path in [r"C:\Program Files\Graphviz\bin", r"C:\Program Files (x86)\Graphviz\bin"]:
    if os.path.exists(g_path) and g_path not in os.environ["PATH"]:
        os.environ["PATH"] += os.pathsep + g_path

def get_base(name, title=""):
    dot = graphviz.Digraph(name, format='svg')
    dot.attr(bgcolor='white', rankdir='TB', fontname='sans-serif', label=f'\\n{title}' if title else '', labelloc='t', fontsize='14', fontcolor='#343a40')
    dot.attr('node', shape='box', style='rounded,filled', fillcolor='#e1f5fe', color='#0288d1', fontname='sans-serif', fontcolor='#212529', penwidth='2')
    dot.attr('edge', fontname='sans-serif', color='#0288d1', penwidth='2', fontcolor='#495057', fontsize='11')
    return dot

def mem_node(dot, name, html):
    dot.node(name, html, shape='none', style='', fillcolor='transparent', color='transparent')

# --- DATA / MEMORY DIAGRAMS ---

def gen_l06(out_dir):
    dot = get_base("L06", "Variables in Memory: int age = 25;")
    dot.attr(rankdir='LR')
    html = '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10" BGCOLOR="#e8f5e9">
      <TR><TD>25</TD></TR>
      <TR><TD BORDER="0"><FONT COLOR="#6c757d">age</FONT></TD></TR>
      <TR><TD BORDER="0"><FONT POINT-SIZE="10" COLOR="#6c757d">0x1F4A</FONT></TD></TR>
    </TABLE>>'''
    mem_node(dot, "var", html)
    dot.render(os.path.join(out_dir, "L06_Variables"), cleanup=True)

def gen_l07(out_dir):
    dot = get_base("L07", 'C-Style String Memory Layout: "Hi"')
    html = '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10" BGCOLOR="#e1f5fe">
      <TR><TD>H</TD><TD>i</TD><TD BGCOLOR="#ffcdd2">\\0</TD></TR>
      <TR><TD BORDER="0"><FONT COLOR="#6c757d">0</FONT></TD><TD BORDER="0"><FONT COLOR="#6c757d">1</FONT></TD><TD BORDER="0"><FONT COLOR="#6c757d">2</FONT></TD></TR>
    </TABLE>>'''
    mem_node(dot, "str", html)
    dot.render(os.path.join(out_dir, "L07_Strings"), cleanup=True)

def gen_l08(out_dir):
    dot = get_base("L08", "Input Buffer (std::cin)")
    dot.attr(rankdir='LR')
    dot.node("kb", "Keyboard", shape="ellipse", fillcolor="#f3e5f5", color="#8e24aa")
    html = '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="8" BGCOLOR="#f8f9fa">
      <TR><TD>4</TD><TD>2</TD><TD BGCOLOR="#ffcdd2">\\n</TD></TR>
    </TABLE>>'''
    mem_node(dot, "buf", html)
    dot.node("var", "int var;", fillcolor="#e8f5e9", color="#388e3c")
    dot.edge("kb", "buf", " Type '42\\n'")
    dot.edge("buf", "var", " cin >> var\\n(Extracts 42,\\nleaves \\n)")
    dot.render(os.path.join(out_dir, "L08_UserInput"), cleanup=True)

def gen_l09(out_dir):
    dot = get_base("L09", "Binary Representation (1 Byte = 8 Bits)")
    html = '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10" BGCOLOR="#fff3e0">
      <TR><TD>0</TD><TD>1</TD><TD>1</TD><TD>0</TD><TD>0</TD><TD>0</TD><TD>0</TD><TD>1</TD></TR>
      <TR>
        <TD BORDER="0"><FONT POINT-SIZE="10">128</FONT></TD>
        <TD BORDER="0"><FONT POINT-SIZE="10">64</FONT></TD>
        <TD BORDER="0"><FONT POINT-SIZE="10">32</FONT></TD>
        <TD BORDER="0"><FONT POINT-SIZE="10">16</FONT></TD>
        <TD BORDER="0"><FONT POINT-SIZE="10">8</FONT></TD>
        <TD BORDER="0"><FONT POINT-SIZE="10">4</FONT></TD>
        <TD BORDER="0"><FONT POINT-SIZE="10">2</FONT></TD>
        <TD BORDER="0"><FONT POINT-SIZE="10">1</FONT></TD>
      </TR>
    </TABLE>>'''
    mem_node(dot, "bin", html)
    dot.node("val", "Value: 64 + 32 + 1 = 97 ('a')", shape="none")
    dot.edge("bin", "val", style="invis")
    dot.render(os.path.join(out_dir, "L09_BinaryNumbers"), cleanup=True)

def gen_l10(out_dir):
    dot = get_base("L10", "Integer Types Memory Sizes")
    html = '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="2" CELLPADDING="8">
      <TR><TD BGCOLOR="#e1f5fe">short (2 Bytes)</TD><TD BORDER="0"></TD><TD BORDER="0"></TD><TD BORDER="0"></TD></TR>
      <TR><TD BGCOLOR="#c8e6c9" COLSPAN="2">int (4 Bytes)</TD><TD BORDER="0"></TD><TD BORDER="0"></TD></TR>
      <TR><TD BGCOLOR="#ffcdd2" COLSPAN="4">long long (8 Bytes)</TD></TR>
    </TABLE>>'''
    mem_node(dot, "sizes", html)
    dot.render(os.path.join(out_dir, "L10_IntegerTypes"), cleanup=True)

def gen_l12(out_dir):
    dot = get_base("L12", "Char & Bool Memory")
    dot.attr(rankdir='LR')
    h1 = '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10" BGCOLOR="#e8f5e9">
      <TR><TD>65</TD></TR><TR><TD BORDER="0">char c = 'A'</TD></TR></TABLE>>'''
    h2 = '''<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10" BGCOLOR="#e8f5e9">
      <TR><TD>1</TD></TR><TR><TD BORDER="0">bool b = true</TD></TR></TABLE>>'''
    mem_node(dot, "c", h1)
    mem_node(dot, "b", h2)
    dot.render(os.path.join(out_dir, "L12_CharAndBool"), cleanup=True)

# --- FLOWCHARTS ---

def condition(dot, name, label):
    dot.node(name, label, shape='diamond', fillcolor='#fff3e0', color='#f57c00')

def gen_l13(out_dir):
    dot = get_base("L13", "If Statement Flow")
    condition(dot, "cond", "Condition")
    dot.node("body", "Execute Block", fillcolor="#e8f5e9", color="#388e3c")
    dot.node("end", "Next Statement", shape="ellipse")
    
    dot.edge("cond", "body", " True", fontcolor="#388e3c")
    dot.edge("cond", "end", " False", fontcolor="#d32f2f")
    dot.edge("body", "end")
    dot.render(os.path.join(out_dir, "L13_If"), cleanup=True)

def gen_l14(out_dir):
    dot = get_base("L14", "If-Else Statement Flow")
    condition(dot, "cond", "Condition")
    dot.node("t", "if Block", fillcolor="#e8f5e9", color="#388e3c")
    dot.node("f", "else Block", fillcolor="#ffcdd2", color="#d32f2f")
    dot.node("end", "Next Statement", shape="ellipse")
    
    dot.edge("cond", "t", " True", fontcolor="#388e3c")
    dot.edge("cond", "f", " False", fontcolor="#d32f2f")
    dot.edge("t", "end")
    dot.edge("f", "end")
    dot.render(os.path.join(out_dir, "L14_IfElse"), cleanup=True)

def gen_l15(out_dir):
    dot = get_base("L15", "If - Else If - Else Flow")
    condition(dot, "c1", "Condition 1")
    condition(dot, "c2", "Condition 2")
    dot.node("b1", "Block 1", fillcolor="#e8f5e9", color="#388e3c")
    dot.node("b2", "Block 2", fillcolor="#e8f5e9", color="#388e3c")
    dot.node("b3", "Else Block", fillcolor="#ffcdd2", color="#d32f2f")
    dot.node("end", "Next Statement", shape="ellipse")
    
    dot.edge("c1", "b1", " True", fontcolor="#388e3c")
    dot.edge("c1", "c2", " False", fontcolor="#d32f2f")
    dot.edge("c2", "b2", " True", fontcolor="#388e3c")
    dot.edge("c2", "b3", " False", fontcolor="#d32f2f")
    dot.edge("b1", "end")
    dot.edge("b2", "end")
    dot.edge("b3", "end")
    dot.render(os.path.join(out_dir, "L15_IfElseIfElse"), cleanup=True)

def gen_l17(out_dir):
    dot = get_base("L17", "Short-Circuit Logic (A && B)")
    condition(dot, "a", "A is True?")
    condition(dot, "b", "B is True?")
    dot.node("t", "Result: TRUE", fillcolor="#e8f5e9", color="#388e3c")
    dot.node("f", "Result: FALSE\\n(B is skipped)", fillcolor="#ffcdd2", color="#d32f2f")
    
    dot.edge("a", "b", " True")
    dot.edge("a", "f", " False")
    dot.edge("b", "t", " True")
    dot.edge("b", "f", " False")
    dot.render(os.path.join(out_dir, "L17_Conditions"), cleanup=True)

def gen_l18(out_dir):
    dot = get_base("L18", "While Loop Flow")
    condition(dot, "cond", "Condition")
    dot.node("body", "Loop Body", fillcolor="#e8f5e9", color="#388e3c")
    dot.node("end", "Next Statement", shape="ellipse")
    
    dot.edge("cond", "body", " True", fontcolor="#388e3c")
    dot.edge("body", "cond", " Loop back")
    dot.edge("cond", "end", " False", fontcolor="#d32f2f")
    dot.render(os.path.join(out_dir, "L18_WhileLoops"), cleanup=True)

def gen_l19(out_dir):
    dot = get_base("L19", "Do-While Loop Flow")
    dot.node("body", "Loop Body\\n(Executes at least once)", fillcolor="#e8f5e9", color="#388e3c")
    condition(dot, "cond", "Condition")
    dot.node("end", "Next Statement", shape="ellipse")
    
    dot.edge("body", "cond")
    dot.edge("cond", "body", " True", fontcolor="#388e3c")
    dot.edge("cond", "end", " False", fontcolor="#d32f2f")
    dot.render(os.path.join(out_dir, "L19_DoWhileLoops"), cleanup=True)

def gen_l20(out_dir):
    dot = get_base("L20", "For Loop Flow")
    dot.node("init", "Initialization\\n(int i = 0)", fillcolor="#e1f5fe")
    condition(dot, "cond", "Condition\\n(i < N)")
    dot.node("body", "Loop Body", fillcolor="#e8f5e9", color="#388e3c")
    dot.node("upd", "Update\\n(i++)", fillcolor="#fff3e0", color="#f57c00")
    dot.node("end", "Next Statement", shape="ellipse")
    
    dot.edge("init", "cond")
    dot.edge("cond", "body", " True", fontcolor="#388e3c")
    dot.edge("body", "upd")
    dot.edge("upd", "cond")
    dot.edge("cond", "end", " False", fontcolor="#d32f2f")
    dot.render(os.path.join(out_dir, "L20_ForLoops"), cleanup=True)

def gen_l21(out_dir):
    dot = get_base("L21", "Break vs Continue")
    condition(dot, "cond", "Loop Condition")
    dot.node("body1", "Body Part 1")
    condition(dot, "check", "Special Case?")
    dot.node("brk", "break", shape="ellipse", fillcolor="#ffcdd2", color="#d32f2f")
    dot.node("cnt", "continue", shape="ellipse", fillcolor="#fff3e0", color="#f57c00")
    dot.node("body2", "Body Part 2")
    dot.node("end", "Next Statement", shape="ellipse")
    
    dot.edge("cond", "body1", " True")
    dot.edge("body1", "check")
    dot.edge("check", "body2", " False")
    dot.edge("check", "brk", " If Break")
    dot.edge("check", "cnt", " If Continue")
    dot.edge("brk", "end")
    dot.edge("cnt", "cond")
    dot.edge("body2", "cond")
    dot.edge("cond", "end", " False")
    dot.render(os.path.join(out_dir, "L21_BreakAndContinue"), cleanup=True)

def gen_l22(out_dir):
    dot = get_base("L22", "Switch Case Flow")
    dot.node("eval", "Evaluate Expression")
    condition(dot, "c1", "== Case 1?")
    condition(dot, "c2", "== Case 2?")
    dot.node("b1", "Block 1", fillcolor="#e8f5e9", color="#388e3c")
    dot.node("b2", "Block 2", fillcolor="#e8f5e9", color="#388e3c")
    dot.node("def", "Default Block", fillcolor="#ffcdd2", color="#d32f2f")
    dot.node("end", "Next Statement", shape="ellipse")
    
    dot.edge("eval", "c1")
    dot.edge("c1", "b1", " Match")
    dot.edge("c1", "c2", " No Match")
    dot.edge("c2", "b2", " Match")
    dot.edge("c2", "def", " No Match")
    
    dot.edge("b1", "end", " break")
    dot.edge("b2", "end", " break")
    dot.edge("def", "end")
    dot.render(os.path.join(out_dir, "L22_Switch"), cleanup=True)


if __name__ == "__main__":
    out_dir = "02_BasicSyntax/theory/assets"
    os.makedirs(out_dir, exist_ok=True)
    
    # Generate all 15 diagrams
    gen_l06(out_dir)
    gen_l07(out_dir)
    gen_l08(out_dir)
    gen_l09(out_dir)
    gen_l10(out_dir)
    gen_l12(out_dir)
    gen_l13(out_dir)
    gen_l14(out_dir)
    gen_l15(out_dir)
    gen_l17(out_dir)
    gen_l18(out_dir)
    gen_l19(out_dir)
    gen_l20(out_dir)
    gen_l21(out_dir)
    gen_l22(out_dir)
    
    print("All 15 Section 02 visuals generated successfully!")
