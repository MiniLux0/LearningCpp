import os
import sys

from utils.diagrams.memory_diagram import MemoryDiagramBuilder
from utils.diagrams.graphviz_diagram import GraphvizBuilder

import graphviz

def gen_l28(out_dir):
    path = os.path.join(out_dir, "L28_ArrayDecay")
    dot = graphviz.Digraph(format='svg')
    dot.attr(rankdir='LR', fontname='sans-serif', bgcolor='transparent')
    dot.attr('node', shape='none', fontname='sans-serif')
    dot.attr('edge', fontname='sans-serif', color='#0288d1', penwidth='2')
    
    # Array table
    arr_html = '''<
    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10" BGCOLOR="#e1f5fe">
      <TR><TD PORT="f0">10</TD><TD PORT="f1">20</TD><TD PORT="f2">30</TD></TR>
      <TR><TD BORDER="0"><FONT POINT-SIZE="10" COLOR="#6c757d">arr[0]</FONT></TD><TD BORDER="0"><FONT POINT-SIZE="10" COLOR="#6c757d">arr[1]</FONT></TD><TD BORDER="0"><FONT POINT-SIZE="10" COLOR="#6c757d">arr[2]</FONT></TD></TR>
      <TR><TD BORDER="0"><FONT POINT-SIZE="10" COLOR="#6c757d">0x1000</FONT></TD><TD BORDER="0"></TD><TD BORDER="0"></TD></TR>
    </TABLE>>'''
    dot.node('arr', arr_html)
    
    # Pointer node
    ptr_html = '''<
    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10" BGCOLOR="#e8f5e9">
      <TR><TD PORT="p">0x1000</TD></TR>
      <TR><TD BORDER="0"><FONT POINT-SIZE="10" COLOR="#6c757d">int* ptr</FONT></TD></TR>
    </TABLE>>'''
    dot.node('ptr', ptr_html)
    
    dot.edge('ptr:p', 'arr:f0', label=' Points to 1st element', fontcolor='#0288d1', fontsize='12')
    
    dot.render(path, cleanup=True)
    print(f"Generated {path}.svg")

def gen_l30b(out_dir):
    path = os.path.join(out_dir, "L30B_StdString.svg")
    g = GraphvizBuilder("StdStringUML", "std::string Core Methods")
    
    g.add_node("str", "std::string", "base")
    g.add_node("cap", "Capacity", "call")
    g.add_node("acc", "Element Access", "call")
    g.add_node("mod", "Modifiers", "call")
    g.add_node("ops", "Operations", "call")
    
    g.add_edge("str", "cap")
    g.add_edge("str", "acc")
    g.add_edge("str", "mod")
    g.add_edge("str", "ops")
    
    # Children
    g.add_node("c1", ".size(), .length()\\n.empty()", "default")
    g.add_edge("cap", "c1")
    
    g.add_node("a1", ".front(), .back()\\n.at(i)", "default")
    g.add_edge("acc", "a1")
    
    g.add_node("m1", ".append(), .push_back()\\n.insert(), .erase()", "default")
    g.add_edge("mod", "m1")
    
    g.add_node("o1", ".find(), .substr()\\n.compare()", "default")
    g.add_edge("ops", "o1")
    
    g.render(path)

def gen_l30c(out_dir):
    path = os.path.join(out_dir, "L30C_CCtype.svg")
    g = GraphvizBuilder("CCtype", "<cctype> Library Functions")
    
    g.add_node("root", "<cctype>", "base")
    g.add_node("chk", "Character Classification", "call")
    g.add_node("cnv", "Character Conversion", "call")
    
    g.add_edge("root", "chk")
    g.add_edge("root", "cnv")
    
    g.add_node("c1", "isalpha()\\nisdigit()\\nisalnum()", "default")
    g.add_node("c2", "islower()\\nisupper()\\nisspace()", "default")
    
    g.add_edge("chk", "c1")
    g.add_edge("chk", "c2")
    
    g.add_node("cv1", "tolower()\\ntoupper()", "memo")
    g.add_edge("cnv", "cv1")
    
    g.render(path)

def gen_l30d(out_dir):
    path = os.path.join(out_dir, "L30D_TwoPointers")
    dot = graphviz.Digraph(format='svg')
    dot.attr(rankdir='TB', fontname='sans-serif', bgcolor='transparent')
    dot.attr('node', shape='none', fontname='sans-serif')
    dot.attr('edge', fontname='sans-serif', penwidth='2')
    
    # Array table
    arr_html = '''<
    <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10" BGCOLOR="#f8f9fa">
      <TR><TD PORT="f0">R</TD><TD PORT="f1">A</TD><TD PORT="f2">D</TD><TD PORT="f3">A</TD><TD PORT="f4">R</TD></TR>
      <TR><TD BORDER="0"><FONT POINT-SIZE="10" COLOR="#6c757d">0</FONT></TD><TD BORDER="0"><FONT POINT-SIZE="10" COLOR="#6c757d">1</FONT></TD><TD BORDER="0"><FONT POINT-SIZE="10" COLOR="#6c757d">2</FONT></TD><TD BORDER="0"><FONT POINT-SIZE="10" COLOR="#6c757d">3</FONT></TD><TD BORDER="0"><FONT POINT-SIZE="10" COLOR="#6c757d">4</FONT></TD></TR>
    </TABLE>>'''
    dot.node('arr', arr_html)
    
    # Pointers
    dot.node('left', 'left', fontcolor='#1976d2', shape='plaintext')
    dot.node('right', 'right', fontcolor='#d32f2f', shape='plaintext')
    
    dot.edge('left', 'arr:f0', color='#1976d2')
    dot.edge('right', 'arr:f4', color='#d32f2f')
    
    dot.render(path, cleanup=True)
    print(f"Generated {path}.svg")

if __name__ == "__main__":
    out_dir = "04_ArraysStrings/theory/assets"
    os.makedirs(out_dir, exist_ok=True)
    gen_l28(out_dir)
    gen_l30b(out_dir)
    gen_l30c(out_dir)
    gen_l30d(out_dir)
    print("Section 04 visuals generated successfully!")
