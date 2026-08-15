import os
import graphviz

for g_path in [r"C:\Program Files\Graphviz\bin", r"C:\Program Files (x86)\Graphviz\bin"]:
    if os.path.exists(g_path) and g_path not in os.environ["PATH"]:
        os.environ["PATH"] += os.pathsep + g_path

def get_base(name, title="", rankdir='TB'):
    dot = graphviz.Digraph(name, format='svg')
    dot.attr(bgcolor='white', rankdir=rankdir, fontname='sans-serif', label=f'\\n{title}' if title else '', labelloc='t', fontsize='14', fontcolor='#343a40')
    dot.attr('node', shape='box', style='rounded,filled', fillcolor='#e1f5fe', color='#0288d1', fontname='sans-serif', fontcolor='#212529', penwidth='2')
    dot.attr('edge', fontname='sans-serif', color='#0288d1', penwidth='2', fontcolor='#495057', fontsize='11')
    return dot

def html_node(dot, name, html):
    dot.node(name, f"<{html}>", shape='none', style='', fillcolor='transparent', color='transparent')

def gen_l31(out_dir):
    # 1. Flowchart factorial(3)
    dot = get_base("L31_Flow", "Recursion Flow: factorial(3)")
    dot.node("c3", "factorial(3)\\nreturns 3 * 2 = 6", fillcolor="#e8f5e9")
    dot.node("c2", "factorial(2)\\nreturns 2 * 1 = 2", fillcolor="#fff3e0")
    dot.node("c1", "factorial(1)\\nreturns 1 * 1 = 1", fillcolor="#f3e5f5")
    dot.node("c0", "factorial(0)\\nBase Case: returns 1", fillcolor="#ffcdd2", color="#d32f2f")
    dot.edge("c3", "c2", " calls")
    dot.edge("c2", "c1", " calls")
    dot.edge("c1", "c0", " calls")
    dot.edge("c0", "c1", " returns 1", style="dashed")
    dot.edge("c1", "c2", " returns 1", style="dashed")
    dot.edge("c2", "c3", " returns 2", style="dashed")
    dot.render(os.path.join(out_dir, "L31_FactorialFlow"), cleanup=True)

    # 2. Base Case Flow
    dot2 = get_base("L31_BaseCase", "General Recursive Function")
    dot2.node("start", "Call Function", shape="ellipse")
    dot2.node("cond", "Is Base Case?", shape="diamond", fillcolor="#fff3e0", color="#f57c00")
    dot2.node("base", "Return Result\\n(Stop)", fillcolor="#e8f5e9", color="#388e3c")
    dot2.node("rec", "Recursive Step\\n(Call self with simpler input)", fillcolor="#fce4ec", color="#d81b60")
    dot2.edge("start", "cond")
    dot2.edge("cond", "base", " Yes")
    dot2.edge("cond", "rec", " No")
    dot2.edge("rec", "cond", " Loop implicitly")
    dot2.render(os.path.join(out_dir, "L31_BaseCaseFlow"), cleanup=True)

def gen_l33(out_dir):
    # 1. Simple DAG
    dot = get_base("L33_DAG", "Overlapping Subproblems")
    dot.node("a", "Problem A")
    dot.node("b1", "Subproblem B", fillcolor="#ffcdd2")
    dot.node("b2", "Subproblem B", fillcolor="#ffcdd2")
    dot.edge("a", "b1", " requires")
    dot.edge("a", "b2", " requires")
    dot.render(os.path.join(out_dir, "L33_Overlapping"), cleanup=True)

    # 2. Memoization Flow
    dot2 = get_base("L33_MemoFlow", "Memoization Pattern")
    dot2.node("start", "fib(n)")
    dot2.node("cond1", "Base Case?", shape="diamond")
    dot2.node("base", "Return n")
    dot2.node("cond2", "In Memo?", shape="diamond")
    dot2.node("memo", "Return memo[n]", fillcolor="#e8f5e9", color="#388e3c")
    dot2.node("calc", "res = fib(n-1) + fib(n-2)")
    dot2.node("save", "memo[n] = res")
    dot2.node("ret", "Return res")
    dot2.edge("start", "cond1")
    dot2.edge("cond1", "base", " Yes")
    dot2.edge("cond1", "cond2", " No")
    dot2.edge("cond2", "memo", " Yes")
    dot2.edge("cond2", "calc", " No")
    dot2.edge("calc", "save")
    dot2.edge("save", "ret")
    dot2.render(os.path.join(out_dir, "L33_MemoPattern"), cleanup=True)

def gen_l34(out_dir):
    dot = get_base("L34_BigO", "Big O Complexity Classes", rankdir="LR")
    dot.node("o1", "O(1)\\nConstant", fillcolor="#e8f5e9", color="#388e3c")
    dot.node("olog", "O(log N)\\nLogarithmic", fillcolor="#e8f5e9", color="#388e3c")
    dot.node("on", "O(N)\\nLinear", fillcolor="#fff3e0", color="#f57c00")
    dot.node("onlog", "O(N log N)\\nLinearithmic", fillcolor="#fff3e0", color="#f57c00")
    dot.node("on2", "O(N²)\\nQuadratic", fillcolor="#ffcdd2", color="#d32f2f")
    dot.node("o2n", "O(2^N)\\nExponential", fillcolor="#ffcdd2", color="#d32f2f")
    dot.node("onf", "O(N!)\\nFactorial", fillcolor="#ffcdd2", color="#d32f2f")
    
    dot.edge("o1", "olog")
    dot.edge("olog", "on")
    dot.edge("on", "onlog")
    dot.edge("onlog", "on2")
    dot.edge("on2", "o2n")
    dot.edge("o2n", "onf")
    dot.render(os.path.join(out_dir, "L34_BigO_Classes"), cleanup=True)

def gen_l35(out_dir):
    # 1. Linear Search
    dot = get_base("L35_Linear", "Linear Search: Target=19", rankdir="LR")
    h = '''<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="8" BGCOLOR="#f8f9fa">
      <TR>
        <TD BGCOLOR="#ffcdd2">42<BR/>!=19</TD>
        <TD BGCOLOR="#ffcdd2">12<BR/>!=19</TD>
        <TD BGCOLOR="#ffcdd2">88<BR/>!=19</TD>
        <TD BGCOLOR="#ffcdd2">7<BR/>!=19</TD>
        <TD BGCOLOR="#c8e6c9">19<BR/>==19 ✅</TD>
      </TR>
    </TABLE>'''
    html_node(dot, "arr", h)
    dot.render(os.path.join(out_dir, "L35_LinearSeq"), cleanup=True)

    # 2. Binary Flow
    dot2 = get_base("L35_BinaryFlow", "Recursive Binary Search Flow")
    dot2.node("start", "binarySearch(arr, low, high, target)")
    dot2.node("c1", "low > high?", shape="diamond")
    dot2.node("base1", "Return -1 (Not Found)", fillcolor="#ffcdd2")
    dot2.node("mid", "mid = low + (high-low)/2")
    dot2.node("c2", "arr[mid] == target?", shape="diamond")
    dot2.node("base2", "Return mid (Found!)", fillcolor="#e8f5e9")
    dot2.node("cl", "Search Left: mid-1")
    dot2.node("cr", "Search Right: mid+1")
    
    dot2.edge("start", "c1")
    dot2.edge("c1", "base1", " Yes")
    dot2.edge("c1", "mid", " No")
    dot2.edge("mid", "c2")
    dot2.edge("c2", "base2", " Yes")
    dot2.edge("c2", "cl", " Target < mid")
    dot2.edge("c2", "cr", " Target > mid")
    dot2.render(os.path.join(out_dir, "L35_BinaryFlow"), cleanup=True)

    # 3. Growth rate
    dot3 = get_base("L35_Growth", "Growth Rate: Linear vs Binary", rankdir="LR")
    dot3.node("n1", "N=10\\nLin=10, Bin=4")
    dot3.node("n2", "N=100\\nLin=100, Bin=7")
    dot3.node("n3", "N=1000\\nLin=1000, Bin=10")
    dot3.node("n4", "N=1,000,000\\nLin=1M, Bin=20")
    dot3.edge("n1", "n2")
    dot3.edge("n2", "n3")
    dot3.edge("n3", "n4")
    dot3.render(os.path.join(out_dir, "L35_GrowthComp"), cleanup=True)

def gen_l36(out_dir):
    # 1. Bubble Intro
    dot = get_base("L36_SortIntro", "Sorting Goal", rankdir="LR")
    dot.node("a", "Desordenado:\\n64 25 12 22 11", fillcolor="#ffcdd2")
    dot.node("b", "Algorithm", shape="ellipse")
    dot.node("c", "Ordenado:\\n11 12 22 25 64", fillcolor="#e8f5e9")
    dot.edge("a", "b")
    dot.edge("b", "c")
    dot.render(os.path.join(out_dir, "L36_SortIntro"), cleanup=True)
    
    # 2. Selection Sort
    dot2 = get_base("L36_Selection", "Selection Sort Steps")
    dot2.node("p0", "Inicial: 64 25 12 22 11")
    dot2.node("p1", "Paso 1: min=11 (pos 4) -> swap pos 0\\n11 25 12 22 64", fillcolor="#e8f5e9")
    dot2.node("p2", "Paso 2: min=12 (pos 2) -> swap pos 1\\n11 12 25 22 64", fillcolor="#e8f5e9")
    dot2.node("p3", "Paso 3: min=22 (pos 3) -> swap pos 2\\n11 12 22 25 64", fillcolor="#e8f5e9")
    dot2.edge("p0", "p1")
    dot2.edge("p1", "p2")
    dot2.edge("p2", "p3")
    dot2.render(os.path.join(out_dir, "L36_SelectionSteps"), cleanup=True)

    # 3. Insertion Sort
    dot3 = get_base("L36_Insertion", "Insertion Sort Steps")
    dot3.node("p0", "Inicial: 12 11 13 5 6")
    dot3.node("p1", "Insertar 11: 11 12 13 5 6")
    dot3.node("p2", "Insertar 13: 11 12 13 5 6 (sin mover)")
    dot3.node("p3", "Insertar 5: 5 11 12 13 6")
    dot3.node("p4", "Insertar 6: 5 6 11 12 13")
    dot3.edge("p0", "p1")
    dot3.edge("p1", "p2")
    dot3.edge("p2", "p3")
    dot3.edge("p3", "p4")
    dot3.render(os.path.join(out_dir, "L36_InsertionSteps"), cleanup=True)
    
    # 4. Best Case Comparison
    dot4 = get_base("L36_BestCase", "Mejor Caso (Casi ordenado)")
    dot4.node("b", "Arreglo casi ordenado")
    dot4.node("is", "Insertion Sort: O(N)", fillcolor="#e8f5e9")
    dot4.node("bs", "Bubble Sort (Opt): O(N)", fillcolor="#e8f5e9")
    dot4.node("ss", "Selection Sort: O(N²)", fillcolor="#ffcdd2")
    dot4.edge("b", "is")
    dot4.edge("b", "bs")
    dot4.edge("b", "ss")
    dot4.render(os.path.join(out_dir, "L36_BestCaseComp"), cleanup=True)

def gen_l37(out_dir):
    # 1. Merge Tree
    dot = get_base("L37_Tree", "Merge Sort Divide Tree")
    dot.node("n0", "56 25 37 58 19 30 40 70")
    dot.node("n1a", "56 25 37 58")
    dot.node("n1b", "19 30 40 70")
    dot.node("n2a", "56 25")
    dot.node("n2b", "37 58")
    dot.node("n2c", "19 30")
    dot.node("n2d", "40 70")
    dot.edge("n0", "n1a")
    dot.edge("n0", "n1b")
    dot.edge("n1a", "n2a")
    dot.edge("n1a", "n2b")
    dot.edge("n1b", "n2c")
    dot.edge("n1b", "n2d")
    dot.render(os.path.join(out_dir, "L37_MergeTree"), cleanup=True)

    # 2. Complexity
    dot2 = get_base("L37_Comp", "Complexity Curve", rankdir="LR")
    dot2.node("c1", "O(1)")
    dot2.node("clog", "O(log N)")
    dot2.node("cn", "O(N)")
    dot2.node("cnlog", "O(N log N)\\nMergeSort", fillcolor="#e8f5e9", color="#388e3c", penwidth="3")
    dot2.node("cn2", "O(N²)")
    dot2.edge("c1", "clog")
    dot2.edge("clog", "cn")
    dot2.edge("cn", "cnlog")
    dot2.edge("cnlog", "cn2")
    dot2.render(os.path.join(out_dir, "L37_Complexity"), cleanup=True)

def gen_l38(out_dir):
    # 1. Flow
    dot = get_base("L38_Flow", "QuickSort Flow")
    dot.node("start", "quickSort()")
    dot.node("cb", "Size <= 1?", shape="diamond")
    dot.node("piv", "Choose Pivot")
    dot.node("part", "Partition Array")
    dot.node("l", "quickSort(Left)")
    dot.node("r", "quickSort(Right)")
    dot.node("done", "Sorted!", fillcolor="#e8f5e9")
    
    dot.edge("start", "cb")
    dot.edge("cb", "done", " Yes")
    dot.edge("cb", "piv", " No")
    dot.edge("piv", "part")
    dot.edge("part", "l")
    dot.edge("part", "r")
    dot.edge("l", "done")
    dot.edge("r", "done")
    dot.render(os.path.join(out_dir, "L38_Flow"), cleanup=True)

    # 2. Partition
    dot2 = get_base("L38_Part", "Partitioning Step (Pivote=56)")
    dot2.node("i", "Inicial: 56 25 37 58 19 30 40 70")
    dot2.node("p", "Comparar y mover lh, rh")
    dot2.node("f", "Final: 30 25 37 40 19 |56| 58 70", fillcolor="#e8f5e9")
    dot2.edge("i", "p")
    dot2.edge("p", "f")
    dot2.render(os.path.join(out_dir, "L38_Partition"), cleanup=True)

    # 3. Trees
    dot3 = get_base("L38_Trees", "Best vs Worst Case Trees", rankdir="LR")
    with dot3.subgraph(name="cluster_b") as cb:
        cb.attr(label="Best Case O(N log N)", color="green")
        cb.node("b1", "1 2 3 4 5 6 7 8")
        cb.node("b2", "1 2 3 4")
        cb.node("b3", "5 6 7 8")
        cb.edge("b1", "b2")
        cb.edge("b1", "b3")
    with dot3.subgraph(name="cluster_w") as cw:
        cw.attr(label="Worst Case O(N²)", color="red")
        cw.node("w1", "1 2 3 4 5 6 7 8\\n(Pivot 1)")
        cw.node("w2", "2 3 4 5 6 7 8\\n(Pivot 2)")
        cw.node("w3", "3 4 5 6 7 8\\n(Pivot 3)")
        cw.edge("w1", "w2")
        cw.edge("w2", "w3")
    dot3.render(os.path.join(out_dir, "L38_Trees"), cleanup=True)

def gen_l39(out_dir):
    # 1. Subset Tree
    dot = get_base("L39_Subset", "Subset Backtracking Tree")
    dot.node("r", "{}")
    dot.node("a1", "{A}")
    dot.node("a0", "{} ")
    dot.node("b1", "{A, B}")
    dot.node("b0", "{A}")
    dot.edge("r", "a1", " +A")
    dot.edge("r", "a0", " -A")
    dot.edge("a1", "b1", " +B")
    dot.edge("a1", "b0", " -B")
    dot.render(os.path.join(out_dir, "L39_SubsetTree"), cleanup=True)

    # 2. Maze Flow
    dot2 = get_base("L39_Maze", "Maze Backtracking Flow")
    dot2.node("start", "solveMaze()")
    dot2.node("c1", "Is End?", shape="diamond")
    dot2.node("c2", "Is Wall/Visited?", shape="diamond")
    dot2.node("ch", "CHOOSE (Mark)")
    dot2.node("ex", "EXPLORE (Recursion)")
    dot2.node("un", "UNCHOOSE (Unmark)", fillcolor="#ffcdd2")
    dot2.node("rt", "Return True", fillcolor="#e8f5e9")
    dot2.node("rf", "Return False", fillcolor="#ffcdd2")
    
    dot2.edge("start", "c1")
    dot2.edge("c1", "rt", " Yes")
    dot2.edge("c1", "c2", " No")
    dot2.edge("c2", "rf", " Yes")
    dot2.edge("c2", "ch", " No")
    dot2.edge("ch", "ex")
    dot2.edge("ex", "rt", " Path Found")
    dot2.edge("ex", "un", " Dead End")
    dot2.edge("un", "rf")
    dot2.render(os.path.join(out_dir, "L39_MazeFlow"), cleanup=True)

    # 3. Nim Flow
    dot3 = get_base("L39_Nim", "Nim Game Logic")
    dot3.node("fgm", "findGoodMove(n)\\nCheck take=1,2,3")
    dot3.node("ibp", "isBadPosition(n - take)\\nCheck if next player loses")
    dot3.node("res", "Return winning take\\nor -1", fillcolor="#e8f5e9")
    dot3.edge("fgm", "ibp", " Calls")
    dot3.edge("ibp", "fgm", " Returns True")
    dot3.edge("fgm", "res")
    dot3.render(os.path.join(out_dir, "L39_NimFlow"), cleanup=True)

# MANUALLY RECREATING OLD SVGS
def gen_manuals(out_dir):
    # Call Stack
    dot1 = get_base("call_stack", "Call Stack")
    h = '''<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10" BGCOLOR="#e1f5fe">
      <TR><TD BGCOLOR="#ffcdd2">fact(1) [Top]</TD></TR>
      <TR><TD>fact(2)</TD></TR>
      <TR><TD>fact(3)</TD></TR>
      <TR><TD BGCOLOR="#e8f5e9">main() [Bottom]</TD></TR>
    </TABLE>'''
    html_node(dot1, "s", h)
    dot1.render(os.path.join(out_dir, "call_stack"), cleanup=True)

    # Fib Tree
    dot2 = get_base("fib_tree", "Fibonacci Tree (Exponential O(2^N))")
    dot2.node("f5", "fib(5)")
    dot2.node("f4", "fib(4)")
    dot2.node("f3", "fib(3)")
    dot2.node("f3_2", "fib(3)", fillcolor="#ffcdd2")
    dot2.node("f2", "fib(2)")
    dot2.edge("f5", "f4")
    dot2.edge("f5", "f3_2")
    dot2.edge("f4", "f3")
    dot2.edge("f4", "f2")
    dot2.render(os.path.join(out_dir, "fib_tree"), cleanup=True)

    # Fib Memo Tree
    dot3 = get_base("fib_memo_tree", "Fibonacci Memoized Tree O(N)")
    dot3.node("f5", "fib(5)")
    dot3.node("f4", "fib(4)")
    dot3.node("f3", "fib(3)")
    dot3.node("f3_2", "fib(3)\\n(Cached!)", fillcolor="#e8f5e9")
    dot3.edge("f5", "f4")
    dot3.edge("f5", "f3_2")
    dot3.edge("f4", "f3")
    dot3.render(os.path.join(out_dir, "fib_memo_tree"), cleanup=True)

    # Binary Search array
    dot4 = get_base("binary_search", "Binary Search Concept", rankdir="LR")
    h = '''<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10" BGCOLOR="#f8f9fa">
      <TR>
        <TD>2</TD>
        <TD BGCOLOR="#e1f5fe">7 (low)</TD>
        <TD BGCOLOR="#e1f5fe">12</TD>
        <TD BGCOLOR="#c8e6c9">19 (mid) ✅</TD>
        <TD BGCOLOR="#e1f5fe">25</TD>
        <TD BGCOLOR="#e1f5fe">30 (high)</TD>
        <TD>42</TD>
      </TR>
    </TABLE>'''
    html_node(dot4, "arr", h)
    dot4.render(os.path.join(out_dir, "binary_search"), cleanup=True)

    # Hanoi Steps 3
    dot5 = get_base("hanoi_steps_3", "Hanoi 3 Disks")
    h = '''<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="10" BGCOLOR="#f8f9fa">
      <TR><TD COLSPAN="3" BGCOLOR="#e1f5fe"><B>Target: Move Stack from A to B via C</B></TD></TR>
      <TR><TD>Peg A (Src)</TD><TD>Peg B (Dst)</TD><TD>Peg C (Aux)</TD></TR>
      <TR><TD>[3, 2, 1]</TD><TD>[]</TD><TD>[]</TD></TR>
      <TR><TD>[]</TD><TD>[3, 2, 1]</TD><TD>[]</TD></TR>
    </TABLE>'''
    html_node(dot5, "arr", h)
    dot5.render(os.path.join(out_dir, "hanoi_steps_3"), cleanup=True)

    # The other basic array sorts:
    dot6 = get_base("bubble_sort", "Bubble Sort")
    h = '''<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="8"><TR><TD>5</TD><TD>1</TD><TD>4</TD><TD>2</TD><TD>8</TD></TR></TABLE>'''
    html_node(dot6, "a", h)
    dot6.render(os.path.join(out_dir, "bubble_sort"), cleanup=True)
    dot7 = get_base("insertion_sort", "Insertion Sort")
    html_node(dot7, "a", h)
    dot7.render(os.path.join(out_dir, "insertion_sort"), cleanup=True)
    dot8 = get_base("selection_sort", "Selection Sort")
    html_node(dot8, "a", h)
    dot8.render(os.path.join(out_dir, "selection_sort"), cleanup=True)
    dot9 = get_base("backtracking_tree", "Backtracking Tree")
    dot9.node("R", "Root")
    dot9.node("D", "Dead End", fillcolor="#ffcdd2")
    dot9.node("S", "Solution", fillcolor="#e8f5e9")
    dot9.edge("R", "D", " Explore")
    dot9.edge("D", "R", " Backtrack", style="dashed")
    dot9.edge("R", "S", " Explore")
    dot9.render(os.path.join(out_dir, "backtracking_tree"), cleanup=True)


if __name__ == "__main__":
    out_dir = "05_RecursionAlgorithms/theory/assets"
    os.makedirs(out_dir, exist_ok=True)
    
    gen_l31(out_dir)
    gen_l33(out_dir)
    gen_l34(out_dir)
    gen_l35(out_dir)
    gen_l36(out_dir)
    gen_l37(out_dir)
    gen_l38(out_dir)
    gen_l39(out_dir)
    gen_manuals(out_dir)
    
    print("All 29 Section 05 visuals generated successfully!")
