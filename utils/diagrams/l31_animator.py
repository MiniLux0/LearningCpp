import os

class CallStackAnimator:
    def __init__(self, n=3):
        self.n = n
        self.box_h = 65
        self.spacing = 15
        self.width = 600
        self.height = (n + 2) * (self.box_h + self.spacing) + 80
        
    def render(self, path):
        # States: 
        # 1. n calls down to 0 (n+1 steps)
        # 2. 0 returns up to n (n+1 steps)
        # Total steps = 2n + 2
        
        total_steps = 2 * self.n + 2
        step_dur = 2.0 # seconds per step
        total_time = total_steps * step_dur
        
        svg = f'<svg width="{self.width}" height="{self.height}" xmlns="http://www.w3.org/2000/svg">\n'
        svg += f'<rect width="{self.width}" height="{self.height}" fill="#ffffff" rx="10"/>\n'
        svg += '''<style>
    text { font-family: 'Segoe UI', Roboto, Helvetica, sans-serif; }
    .frame { stroke-width: 2; rx: 8; }
    .call-text { font-size: 16px; font-weight: bold; fill: #343a40; }
    .sub-text { font-size: 14px; fill: #495057; }
    .ret-text { font-size: 16px; fill: #d32f2f; font-weight: bold; }
'''

        # Generate CSS Keyframes dynamically
        # Box 'i' appears at step (self.n - i). Disappears at step (self.n + i + 1).
        # Colors: normal until it returns. Returns at step (self.n + i + 1).
        
        for i in range(self.n, -1, -1):
            idx = self.n - i # 0-indexed from top of stack sequence
            appear_step = idx
            return_step = total_steps - 1 - idx
            
            # Opacity Keyframe
            appear_pct = (appear_step / total_steps) * 100
            disappear_pct = ((return_step + 1) / total_steps) * 100
            
            svg += f'''
    @keyframes appear-{i} {{
        0%, {max(0, appear_pct - 1):.1f}% {{ opacity: 0; }}
        {appear_pct:.1f}%, {disappear_pct - 1:.1f}% {{ opacity: 1; }}
        {disappear_pct:.1f}%, 100% {{ opacity: 0; }}
    }}
    .g-{i} {{ animation: appear-{i} {total_time}s infinite; opacity: 0; }}
'''
            # Color Keyframe
            # Normal fill #f8f9fa, stroke #dee2e6. 
            # When returning (return_step), turns green #d4edda, stroke #28a745
            ret_pct = (return_step / total_steps) * 100
            svg += f'''
    @keyframes color-{i} {{
        0%, {max(0, ret_pct - 1):.1f}% {{ fill: #f8f9fa; stroke: #dee2e6; }}
        {ret_pct:.1f}%, 100% {{ fill: #d4edda; stroke: #28a745; }}
    }}
    .rect-{i} {{ animation: color-{i} {total_time}s infinite; fill: #f8f9fa; stroke: #dee2e6; }}
'''
            # Math Text vs Return Text opacity
            # Math text shows until return_step.
            # Return text shows AT return_step.
            svg += f'''
    @keyframes text-math-{i} {{
        0%, {max(0, ret_pct - 1):.1f}% {{ opacity: 1; }}
        {ret_pct:.1f}%, 100% {{ opacity: 0; }}
    }}
    .math-{i} {{ animation: text-math-{i} {total_time}s infinite; opacity: 1; }}

    @keyframes text-ret-{i} {{
        0%, {max(0, ret_pct - 1):.1f}% {{ opacity: 0; }}
        {ret_pct:.1f}%, 100% {{ opacity: 1; }}
    }}
    .ret-{i} {{ animation: text-ret-{i} {total_time}s infinite; opacity: 0; }}
'''
        svg += '</style>\n'
        svg += f'<text x="{self.width/2}" y="40" font-size="22" font-weight="bold" text-anchor="middle" fill="#212529">Call Stack Animado: factorial({self.n})</text>\n'
        
        # Calculate factorials for exact return values
        import math
        
        base_y = self.height - 80
        
        for i in range(self.n, -1, -1):
            y = base_y - (self.n - i) * (self.box_h + self.spacing)
            
            call_str = f"factorial({i})"
            if i == 0:
                math_str = "BASE CASE"
                ret_str = "return 1"
            else:
                math_str = f"{i} × factorial({i-1})"
                ret_str = f"return {i} × {math.factorial(i-1)} = {math.factorial(i)}"
                
            svg += f'''
<g class="g-{i}">
    <rect x="{self.width/2 - 150}" y="{y}" width="300" height="{self.box_h}" class="frame rect-{i}" />
    <text x="{self.width/2}" y="{y + 25}" class="call-text" text-anchor="middle">{call_str}</text>
    <text x="{self.width/2}" y="{y + 45}" class="sub-text math-{i}" text-anchor="middle">{math_str}</text>
    <text x="{self.width/2}" y="{y + 45}" class="ret-text ret-{i}" text-anchor="middle">{ret_str}</text>
</g>
'''
        
        svg += '</svg>'
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)

def gen_basecase_flow(path):
    # Using animateMotion for the dot
    svg = '''<svg width="600" height="400" xmlns="http://www.w3.org/2000/svg">
<rect width="600" height="400" fill="#ffffff" rx="10"/>
<style>
    text { font-family: 'Segoe UI', Roboto, Helvetica, sans-serif; }
    .box { fill: #f8f9fa; stroke: #dee2e6; stroke-width: 2; rx: 8; }
    .diamond { fill: #fff3e0; stroke: #f57c00; stroke-width: 2; }
    .base { fill: #e8f5e9; stroke: #388e3c; stroke-width: 2; rx: 8; }
    .rec { fill: #fce4ec; stroke: #d81b60; stroke-width: 2; rx: 8; }
    
    .label { font-size: 14px; font-weight: bold; fill: #343a40; }
    .arrow { stroke: #adb5bd; stroke-width: 2; fill: none; }
</style>

<text x="300" y="30" font-size="20" font-weight="bold" text-anchor="middle" fill="#212529">Flujo de Ejecución de Función Recursiva</text>

<!-- Flowchart -->
<!-- Call Function -->
<rect x="220" y="60" width="160" height="50" class="box"/>
<text x="300" y="90" class="label" text-anchor="middle">Llamada a Función</text>

<path d="M300,110 L300,140" class="arrow" marker-end="url(#arrowhead)"/>

<!-- Diamond Condition -->
<polygon points="300,140 380,180 300,220 220,180" class="diamond"/>
<text x="300" y="185" class="label" text-anchor="middle">¿Es Caso Base?</text>

<path d="M300,220 L300,260" class="arrow" marker-end="url(#arrowhead)"/>
<text x="310" y="245" font-size="12" fill="#d81b60" font-weight="bold">No</text>

<path d="M220,180 L180,180" class="arrow" marker-end="url(#arrowhead)"/>
<text x="200" y="175" font-size="12" fill="#388e3c" font-weight="bold">Sí</text>

<!-- Recursive Step -->
<rect x="220" y="260" width="160" height="50" class="rec"/>
<text x="300" y="285" class="label" fill="#d81b60" text-anchor="middle">Paso Recursivo</text>
<!-- Loop back -->
<path d="M380,285 L440,285 L440,180 L380,180" class="arrow" stroke-dasharray="5"/>

<!-- Base Case -->
<rect x="20" y="155" width="160" height="50" class="base"/>
<text x="100" y="185" class="label" fill="#388e3c" text-anchor="middle">Retornar y Detener</text>

<!-- The animated dot tracing the path exactly! -->
<!-- Continuous Path: Call -> Cond -> Rec -> Loop -> Cond -> Base -->
<circle r="6" fill="#0288d1">
    <animateMotion 
        dur="6s" 
        repeatCount="indefinite"
        path="M 300,110 L 300,140 L 300,220 L 300,260 L 380,285 L 440,285 L 440,180 L 380,180 L 300,180 L 220,180 L 180,180"
        calcMode="linear"
    />
</circle>

<defs>
  <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
    <polygon points="0 0, 10 3.5, 0 7" fill="#adb5bd" />
  </marker>
</defs>

</svg>'''
    with open(path, "w", encoding="utf-8") as f: f.write(svg)

if __name__ == "__main__":
    out_dir = "05_RecursionAlgorithms/theory/assets"
    os.makedirs(out_dir, exist_ok=True)
    
    CallStackAnimator(n=3).render(os.path.join(out_dir, "L31_FactorialFlow.svg"))
    gen_basecase_flow(os.path.join(out_dir, "L31_BaseCaseFlow.svg"))
    
    print("L31 Updated Animated SVGs generated successfully!")
