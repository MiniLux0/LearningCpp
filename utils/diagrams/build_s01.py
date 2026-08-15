import os
import graphviz

# Force add Graphviz default install paths to PATH
for g_path in [r"C:\Program Files\Graphviz\bin", r"C:\Program Files (x86)\Graphviz\bin"]:
    if os.path.exists(g_path) and g_path not in os.environ["PATH"]:
        os.environ["PATH"] += os.pathsep + g_path

def get_base_dot(name, title=""):
    dot = graphviz.Digraph(name, format='svg')
    # White background as requested by user
    dot.attr(bgcolor='white', rankdir='LR', fontname='sans-serif', label=f'\\n{title}' if title else '', labelloc='t', fontsize='14', fontcolor='#343a40')
    dot.attr('node', shape='box', style='rounded,filled', fillcolor='#e1f5fe', color='#0288d1', fontname='sans-serif', fontcolor='#212529', penwidth='2', margin='0.2,0.1')
    dot.attr('edge', fontname='sans-serif', color='#0288d1', penwidth='2', fontcolor='#495057', fontsize='11')
    return dot

def gen_l01(out_dir):
    dot = get_base_dot("L01", "C++ Compilation Pipeline")
    
    dot.node("src", "Source Code\\n(.cpp)", fillcolor="#e8f5e9", color="#388e3c")
    dot.node("comp", "Compiler\\n(g++)", shape="oval", fillcolor="#fff3e0", color="#f57c00")
    dot.node("obj", "Object Code\\n(.o)", fillcolor="#e8f5e9", color="#388e3c")
    dot.node("link", "Linker\\n(ld)", shape="oval", fillcolor="#fff3e0", color="#f57c00")
    dot.node("exe", "Executable\\n(.exe)", fillcolor="#c8e6c9", color="#2e7d32", penwidth="3")
    
    dot.edge("src", "comp", " Compile")
    dot.edge("comp", "obj")
    dot.edge("obj", "link", " Link")
    dot.edge("link", "exe")
    
    dot.render(os.path.join(out_dir, "L01_pipeline"), cleanup=True)

def gen_l02(out_dir):
    dot = get_base_dot("L02", "Namespaces: Avoiding Collisions")
    dot.attr(rankdir='TB')
    
    with dot.subgraph(name='cluster_std') as c:
        c.attr(label='std namespace', style='rounded,dashed', color='#6c757d', bgcolor='#f8f9fa')
        c.node('std_cout', 'cout', fillcolor='#e1f5fe', color='#0288d1')
        c.node('std_cin', 'cin', fillcolor='#e1f5fe', color='#0288d1')
        
    with dot.subgraph(name='cluster_my') as c:
        c.attr(label='my_namespace', style='rounded,dashed', color='#6c757d', bgcolor='#f8f9fa')
        c.node('my_cout', 'cout', fillcolor='#fce4ec', color='#d81b60')
        
    dot.node("call1", "std::cout << ...")
    dot.node("call2", "my_namespace::cout << ...")
    
    dot.edge("call1", "std_cout", " Resolves to")
    dot.edge("call2", "my_cout", " Resolves to")
    
    dot.render(os.path.join(out_dir, "L02_namespaces"), cleanup=True)

def gen_l03(out_dir):
    dot = get_base_dot("L03", "Buffer Flushing: \\n vs std::endl")
    dot.attr(rankdir='TB')
    
    dot.node("p1", "cout << \"Hello\\n\";", fillcolor="#e1f5fe")
    dot.node("b1", "Output Buffer\\n[ H e l l o \\n ]", shape="cylinder", fillcolor="#f8f9fa", color="#adb5bd")
    dot.node("o1", "Screen\\n(Delayed)", fillcolor="#e8f5e9")
    
    dot.edge("p1", "b1", " Written to buffer")
    dot.edge("b1", "o1", " Waits for flush")
    
    dot.node("p2", "cout << \"Hello\" << endl;", fillcolor="#e1f5fe")
    dot.node("b2", "Output Buffer\\n[ H e l l o \\n ]", shape="cylinder", fillcolor="#f8f9fa", color="#adb5bd")
    dot.node("o2", "Screen\\n(Immediate)", fillcolor="#e8f5e9")
    
    dot.edge("p2", "b2", " Written to buffer")
    dot.edge("b2", "o2", " FORCED FLUSH", color="#d32f2f", fontcolor="#d32f2f")
    
    dot.render(os.path.join(out_dir, "L03_flush"), cleanup=True)

def gen_l04(out_dir):
    dot = get_base_dot("L04", "Standard I/O Streams")
    
    dot.node("kb", "Keyboard\\n(Standard Input)", shape="ellipse", fillcolor="#f3e5f5", color="#8e24aa")
    dot.node("cin", "std::cin\\n(Input Stream)", shape="rarrow", fillcolor="#e1f5fe", color="#0288d1")
    dot.node("var", "Variable in RAM\\n(e.g., int age)", fillcolor="#e8f5e9", color="#388e3c")
    dot.node("cout", "std::cout\\n(Output Stream)", shape="rarrow", fillcolor="#e1f5fe", color="#0288d1")
    dot.node("mon", "Monitor\\n(Standard Output)", shape="ellipse", fillcolor="#f3e5f5", color="#8e24aa")
    
    dot.edge("kb", "cin", " Typing")
    dot.edge("cin", "var", " Extraction (>>)")
    dot.edge("var", "cout", " Insertion (<<)")
    dot.edge("cout", "mon", " Rendering")
    
    dot.render(os.path.join(out_dir, "L04_io"), cleanup=True)

def gen_l05(out_dir):
    dot = get_base_dot("L05", "Interactive Profile App Flow")
    dot.attr(rankdir='TB')
    
    dot.node("q1", "1. Ask for Name\\n(cout)", fillcolor="#e1f5fe")
    dot.node("i1", "2. Read Name\\n(getline)", fillcolor="#fff3e0")
    dot.node("q2", "3. Ask for Age\\n(cout)", fillcolor="#e1f5fe")
    dot.node("i2", "4. Read Age\\n(cin >>)", fillcolor="#fff3e0")
    dot.node("out", "5. Print Profile Summary\\n(cout)", fillcolor="#e8f5e9", color="#388e3c")
    
    dot.edge("q1", "i1")
    dot.edge("i1", "q2")
    dot.edge("q2", "i2")
    dot.edge("i2", "out")
    
    dot.render(os.path.join(out_dir, "L05_profile"), cleanup=True)

if __name__ == "__main__":
    out_dir = "01_GettingStarted/theory/assets"
    os.makedirs(out_dir, exist_ok=True)
    gen_l01(out_dir)
    gen_l02(out_dir)
    gen_l03(out_dir)
    gen_l04(out_dir)
    gen_l05(out_dir)
    print("Section 01 visuals generated successfully!")
