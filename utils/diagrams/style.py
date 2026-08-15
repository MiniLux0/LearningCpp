"""
Shared Styling and Palette Configuration for LearningCpp Diagrams
Ensures visual consistency across Graphviz, Matplotlib, and custom SVG diagrams.
"""

PALETTE = {
    "background": "#ffffff",
    "text_primary": "#212529",
    "text_secondary": "#6c757d",
    "title": "#343a40",
    
    "node_default_fill": "#f8f9fa",
    "node_default_stroke": "#adb5bd",
    
    "node_call_fill": "#e1f5fe",
    "node_call_stroke": "#0288d1",
    
    "node_base_fill": "#e8f5e9",
    "node_base_stroke": "#388e3c",
    
    "node_memo_fill": "#fff3e0",
    "node_memo_stroke": "#f57c00",
    
    "node_alert_fill": "#ffebee",
    "node_alert_stroke": "#d32f2f",
    
    "edge_default": "#adb5bd",
    "edge_highlight": "#1976d2",
    "edge_success": "#388e3c",
    "edge_error": "#d32f2f",
}

FONTS = {
    "primary": "sans-serif",
    "monospace": "monospace",
    "title_size": 16,
    "text_size": 13,
    "mono_size": 12,
}

def get_graphviz_theme():
    """Returns a Graphviz attributes dictionary for the overall graph."""
    return {
        "bgcolor": PALETTE["background"],
        "fontname": FONTS["primary"],
        "fontsize": str(FONTS["title_size"]),
        "fontcolor": PALETTE["title"],
        "pad": "0.5"
    }

def get_graphviz_node_style(node_type="default"):
    """Returns a Graphviz attributes dictionary for nodes based on semantic type."""
    fill = PALETTE.get(f"node_{node_type}_fill", PALETTE["node_default_fill"])
    stroke = PALETTE.get(f"node_{node_type}_stroke", PALETTE["node_default_stroke"])
    return {
        "shape": "box",
        "style": "filled,rounded",
        "fillcolor": fill,
        "color": stroke,
        "penwidth": "2",
        "fontname": FONTS["primary"],
        "fontsize": str(FONTS["text_size"]),
        "fontcolor": PALETTE["text_primary"],
        "margin": "0.2,0.1"
    }

def get_graphviz_edge_style(edge_type="default"):
    """Returns a Graphviz attributes dictionary for edges based on semantic type."""
    color = PALETTE.get(f"edge_{edge_type}", PALETTE["edge_default"])
    return {
        "color": color,
        "penwidth": "2",
        "fontname": FONTS["primary"],
        "fontsize": "11",
        "fontcolor": PALETTE["text_secondary"]
    }
