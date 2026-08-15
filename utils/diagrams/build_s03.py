import os
import graphviz
from utils.diagrams.graphviz_diagram import GraphvizBuilder

def gen_l23(out_dir):
    path = os.path.join(out_dir, "L23_Functions.svg")
    g = GraphvizBuilder("L23", "Function Call Flow")
    
    g.add_node("main", "main() Call", "base")
    g.add_node("func", "Function Body:\\nshowWelcome()", "call")
    g.add_node("ops", "Console Output /\\nCalculations", "default")
    
    g.add_edge("main", "func", "Pass Arguments")
    g.add_edge("func", "ops", "Execute Instructions")
    g.add_edge("ops", "main", "Return Control")
    
    g.render(path)

def gen_l24(out_dir):
    path = os.path.join(out_dir, "L24_ReturnValues.svg")
    g = GraphvizBuilder("L24", "Return Value Flow")
    
    g.add_node("caller", "int res = alCuadrado(4);", "base")
    g.add_node("func", "square(int n)", "call")
    g.add_node("ret", "return 16;", "memo")
    
    g.add_edge("caller", "func", "Function Call")
    g.add_edge("func", "ret", "Calculates 4 * 4 = 16")
    g.add_edge("ret", "caller", "Returns 16")
    
    g.render(path)

def gen_pass_by_ref(out_dir):
    path = os.path.join(out_dir, "pass_by_ref")
    dot = graphviz.Digraph(format='svg')
    dot.attr(rankdir='TB', fontname='sans-serif', bgcolor='transparent')
    dot.attr('node', shape='none', fontname='sans-serif')
    dot.attr('edge', fontname='sans-serif', penwidth='2')
    
    # Memory Layout with HTML tables
    mem_html = '''<
    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="15" BGCOLOR="#e8f5e9">
      <TR><TD PORT="mem">10</TD></TR>
      <TR><TD BORDER="0"><FONT POINT-SIZE="12" COLOR="#6c757d">Memory Address 0x1A2B</FONT></TD></TR>
    </TABLE>>'''
    dot.node('memory', mem_html)
    
    # main scope
    dot.node('main', 'main()\\nint x', fontcolor='#1976d2', shape='plaintext')
    
    # function scope
    dot.node('func', 'function(int& ref)\\nint& ref', fontcolor='#d32f2f', shape='plaintext')
    
    dot.edge('main', 'memory:mem', color='#1976d2')
    dot.edge('func', 'memory:mem', color='#d32f2f', style='dashed')
    
    dot.render(path, cleanup=True)
    print(f"Generated {path}.svg")

if __name__ == "__main__":
    out_dir = "03_Subroutines/theory/assets"
    os.makedirs(out_dir, exist_ok=True)
    gen_l23(out_dir)
    gen_l24(out_dir)
    gen_pass_by_ref(out_dir)
    print("Section 03 visuals generated successfully!")
