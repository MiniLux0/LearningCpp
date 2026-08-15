"""
Graphviz Diagram Generator
Provides wrappers around the `graphviz` python package to generate parameterized 
recursion trees and linear flowcharts.

This script explicitly checks for the system `dot` binary to prevent silent failures.
"""

import os
import sys
import shutil

# Force add Graphviz default install paths to PATH (for unrefreshed terminal sessions)
for g_path in [r"C:\Program Files\Graphviz\bin", r"C:\Program Files (x86)\Graphviz\bin"]:
    if os.path.exists(g_path) and g_path not in os.environ["PATH"]:
        os.environ["PATH"] += os.pathsep + g_path

# Ensure Graphviz binary is installed
if not shutil.which("dot"):
    print("CRITICAL ERROR: 'dot' binary not found in system PATH.", file=sys.stderr)
    print("Please install Graphviz system package (e.g. `choco install graphviz` on Windows).", file=sys.stderr)
    sys.exit(1)

try:
    import graphviz
except ImportError:
    print("CRITICAL ERROR: 'graphviz' Python package not installed.", file=sys.stderr)
    print("Run `pip install graphviz`.", file=sys.stderr)
    sys.exit(1)

from utils.diagrams.style import get_graphviz_theme, get_graphviz_node_style, get_graphviz_edge_style

class GraphvizBuilder:
    def __init__(self, name, title=""):
        self.dot = graphviz.Digraph(name, format='svg')
        self.dot.attr(label=title, labelloc='t', **get_graphviz_theme())
        
    def add_node(self, node_id, label, node_type="default"):
        """Adds a styled node to the graph."""
        attrs = get_graphviz_node_style(node_type)
        self.dot.node(node_id, label, **attrs)
        
    def add_edge(self, source, target, label="", edge_type="default"):
        """Adds a styled edge between nodes."""
        attrs = get_graphviz_edge_style(edge_type)
        if label:
            attrs['label'] = f" {label} "
        self.dot.edge(source, target, **attrs)
        
    def render(self, output_path):
        """Renders the diagram to an SVG file."""
        # Graphviz automatically adds the .svg extension based on format
        base_path = os.path.splitext(output_path)[0]
        out_file = self.dot.render(base_path, cleanup=True)
        print(f"Successfully generated: {out_file}")
        return out_file

def generate_recursion_tree(n_disks, output_path):
    """
    Pilot example: Generates the Hanoi recursion tree using Graphviz.
    """
    builder = GraphvizBuilder("HanoiTree", f"Towers of Hanoi Recursion Tree (N={n_disks})")
    
    def build_tree(n, src, tgt, aux, parent_id=None, child_dir=""):
        node_id = f"N_{n}_{src}_{tgt}_{id(src)}_{parent_id}_{child_dir}"
        
        if n == 1:
            builder.add_node(node_id, f"Move D1:\\n{src} → {tgt}", "base")
            if parent_id:
                builder.add_edge(parent_id, node_id)
            return node_id
            
        builder.add_node(node_id, f"Hanoi({n}, {src}→{tgt})", "call")
        if parent_id:
            builder.add_edge(parent_id, node_id)
            
        build_tree(n-1, src, aux, tgt, node_id, "L")
        
        mid_id = f"M_{n}_{src}_{tgt}_{id(src)}_{parent_id}"
        builder.add_node(mid_id, f"Move D{n}:\\n{src} → {tgt}", "default")
        builder.add_edge(node_id, mid_id)
        
        build_tree(n-1, aux, tgt, src, node_id, "R")
        
        return node_id

    build_tree(n_disks, 'A', 'C', 'B')
    builder.render(output_path)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--test-hanoi", type=int, help="Test Hanoi tree with N disks")
    args = parser.parse_args()
    
    if args.test_hanoi:
        generate_recursion_tree(args.test_hanoi, "test_hanoi_tree.svg")
