import os
import sys

from utils.diagrams.memory_diagram import generate_hanoi_filmstrip
from utils.diagrams.graphviz_diagram import generate_recursion_tree

def build_pilot():
    out_dir = "05_RecursionAlgorithms/theory/assets"
    os.makedirs(out_dir, exist_ok=True)
    
    # 1. Filmstrip (Matplotlib)
    filmstrip_path = os.path.join(out_dir, "hanoi_steps_3.svg")
    print(f"Generating filmstrip to {filmstrip_path}...")
    generate_hanoi_filmstrip(3, filmstrip_path)
    
    # 2. Recursion Tree (Graphviz)
    tree_path = os.path.join(out_dir, "hanoi_tree_3.svg")
    print(f"Generating recursion tree to {tree_path}...")
    try:
        generate_recursion_tree(3, tree_path)
    except Exception as e:
        print(f"Failed to generate recursion tree: {e}")
        sys.exit(1)

if __name__ == "__main__":
    build_pilot()
