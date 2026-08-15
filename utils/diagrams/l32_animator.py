import os

class HanoiAnimator:
    def __init__(self, num_disks=3):
        self.num_disks = num_disks
        self.pegs = [[i for i in range(num_disks, 0, -1)], [], []] 
        self.states = [] 
        
        self._record_state("Estado Inicial")
        self.solve(num_disks, 0, 2, 1)
        self.states[-1]["msg"] = "¡Completado!"
        
    def _record_state(self, msg):
        import copy
        self.states.append({
            "pegs": copy.deepcopy(self.pegs),
            "msg": msg
        })
                
    def solve(self, n, source, target, aux):
        if n > 0:
            self.solve(n - 1, source, aux, target)
            disk = self.pegs[source].pop()
            self.pegs[target].append(disk)
            self._record_state(f"Movimiento: Disco {disk} de {chr(65+source)} a {chr(65+target)}")
            self.solve(n - 1, aux, target, source)
            
    def render(self, path):
        width = 600
        height = 350
        peg_x = [150, 300, 450]
        base_y = 280
        slot_h = 24
        
        num_steps = len(self.states)
        step_dur = 1.0 # faster
        total_time = num_steps * step_dur
        
        svg = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
        svg += f'<rect width="{width}" height="{height}" fill="#ffffff" rx="10"/>\n'
        
        svg += '''<style>
    text { font-family: 'Segoe UI', Roboto, Helvetica, sans-serif; }
    .peg { fill: #dee2e6; rx: 4; }
    .base { fill: #ced4da; rx: 6; }
    .disk { stroke: #fff; stroke-width: 2; rx: 10; }
'''
        # Generate layer keyframes
        for i in range(num_steps):
            start_pct = (i / num_steps) * 100
            end_pct = ((i + 1) / num_steps) * 100
            svg += f'''
    @keyframes show-step-{i} {{
        0%, {max(0, start_pct - 0.1):.1f}% {{ opacity: 0; }}
        {start_pct:.1f}%, {end_pct - 0.1:.1f}% {{ opacity: 1; }}
        {end_pct:.1f}%, 100% {{ opacity: 0; }}
    }}
    .step-{i} {{ animation: show-step-{i} {total_time}s infinite; opacity: 0; }}
'''
        svg += '</style>\n'
        svg += f'<text x="{width/2}" y="40" font-size="22" font-weight="bold" text-anchor="middle" fill="#212529">Torres de Hanói (N=3) Animado</text>\n'

        colors = {1: "#ef5350", 2: "#ff9800", 3: "#42a5f5"}
        widths = {1: 60, 2: 100, 3: 140}
        
        for i, state in enumerate(self.states):
            svg += f'<g class="step-{i}">\n'
            
            # Draw Msg Box
            svg += f'''
    <rect x="{width/2 - 200}" y="295" width="400" height="40" rx="8" fill="#f8f9fa" stroke="#dee2e6" stroke-width="2"/>
    <text x="{width/2}" y="320" font-size="16" font-weight="bold" text-anchor="middle" fill="#0288d1">Paso {i}: {state["msg"]}</text>
'''
            # Draw Base and Pegs
            svg += '    <rect x="50" y="280" width="500" height="10" class="base"/>\n'
            for px in peg_x:
                svg += f'    <rect x="{px - 6}" y="120" width="12" height="160" class="peg"/>\n'
            
            svg += '    <text x="150" y="110" font-size="16" font-weight="bold" text-anchor="middle" fill="#6c757d">A</text>\n'
            svg += '    <text x="300" y="110" font-size="16" font-weight="bold" text-anchor="middle" fill="#6c757d">B</text>\n'
            svg += '    <text x="450" y="110" font-size="16" font-weight="bold" text-anchor="middle" fill="#6c757d">C</text>\n'

            # Draw Disks
            for peg_idx, peg_disks in enumerate(state["pegs"]):
                for slot_idx, disk in enumerate(peg_disks):
                    w = widths[disk]
                    c = colors[disk]
                    px = peg_x[peg_idx] - w/2
                    py = base_y - (slot_idx + 1) * slot_h
                    svg += f'    <rect x="{px}" y="{py}" width="{w}" height="{slot_h}" fill="{c}" class="disk"/>\n'
            
            svg += '</g>\n'

        svg += '</svg>'
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)

if __name__ == "__main__":
    out_dir = "05_RecursionAlgorithms/theory/assets"
    os.makedirs(out_dir, exist_ok=True)
    anim = HanoiAnimator(3)
    anim.render(os.path.join(out_dir, "hanoi_animated.svg"))
    print("Hanoi Layer-Based Animated SVG generated successfully!")
