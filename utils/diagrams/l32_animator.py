import os

class HanoiAnimator:
    def __init__(self, num_disks=3):
        self.num_disks = num_disks
        self.pegs = [[i for i in range(num_disks, 0, -1)], [], []] # e.g. [3, 2, 1] on peg 0
        self.disk_positions = {} # disk_id -> list of (peg, slot)
        
        # Initial state (Step 0)
        self._record_state()
        
        # Run Hanoi to collect states
        self.solve(num_disks, 0, 2, 1)
        
    def _record_state(self):
        for peg_idx, peg in enumerate(self.pegs):
            for slot_idx, disk in enumerate(peg):
                if disk not in self.disk_positions:
                    self.disk_positions[disk] = []
                self.disk_positions[disk].append((peg_idx, slot_idx))
                
    def solve(self, n, source, target, aux):
        if n > 0:
            self.solve(n - 1, source, aux, target)
            # Move disk n
            disk = self.pegs[source].pop()
            self.pegs[target].append(disk)
            self._record_state()
            self.solve(n - 1, aux, target, source)
            
    def render(self, path):
        width = 600
        height = 350
        
        # Peg X coordinates
        peg_x = [150, 300, 450]
        # Y coordinates for slots (bottom is 280)
        base_y = 280
        slot_h = 24
        
        num_steps = len(self.disk_positions[1]) # total states
        step_dur = 1.5 # seconds per step
        total_time = num_steps * step_dur
        
        svg = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
        svg += f'<rect width="{width}" height="{height}" fill="#ffffff" rx="10"/>\n'
        
        # Styles
        svg += '''<style>
    text { font-family: 'Segoe UI', Roboto, Helvetica, sans-serif; }
    .peg { fill: #dee2e6; rx: 4; }
    .base { fill: #ced4da; rx: 6; }
    .disk { stroke: #fff; stroke-width: 2; rx: 10; }
    .msg-text { font-size: 16px; font-weight: bold; fill: #343a40; opacity: 0; }
</style>
'''
        svg += f'<text x="{width/2}" y="40" font-size="22" font-weight="bold" text-anchor="middle" fill="#212529">Torres de Hanói (N=3) Animado</text>\n'

        # Draw Pegs
        svg += '<rect x="50" y="280" width="500" height="20" class="base"/>\n'
        for px in peg_x:
            svg += f'<rect x="{px - 6}" y="120" width="12" height="160" class="peg"/>\n'
            
        svg += '<text x="150" y="325" font-size="18" font-weight="bold" text-anchor="middle" fill="#6c757d">Origen (A)</text>\n'
        svg += '<text x="300" y="325" font-size="18" font-weight="bold" text-anchor="middle" fill="#6c757d">Auxiliar (B)</text>\n'
        svg += '<text x="450" y="325" font-size="18" font-weight="bold" text-anchor="middle" fill="#6c757d">Destino (C)</text>\n'
        
        # Disk properties
        colors = {1: "#ef5350", 2: "#ff9800", 3: "#42a5f5"} # 1 is smallest
        widths = {1: 60, 2: 100, 3: 140}
        
        key_times = ",".join([f"{i/(num_steps-1):.3f}" for i in range(num_steps)])
        
        # Message Animations
        # At each step, what is happening? We can add a changing text.
        for i in range(num_steps):
            pct_start = i / num_steps * 100
            pct_end = (i+1) / num_steps * 100
            svg += f'''
<style>
    @keyframes show-msg-{i} {{
        0%, {max(0, pct_start - 0.1):.1f}% {{ opacity: 0; }}
        {pct_start:.1f}%, {pct_end - 0.1:.1f}% {{ opacity: 1; }}
        {pct_end:.1f}%, 100% {{ opacity: 0; }}
    }}
    .msg-{i} {{ animation: show-msg-{i} {total_time}s infinite; opacity: 0; }}
</style>
'''
            if i == 0:
                msg = "Estado Inicial"
            elif i == num_steps - 1:
                msg = "¡Completado!"
            else:
                msg = f"Movimiento {i} de {num_steps-1}"
            svg += f'<text x="{width/2}" y="80" class="msg-text msg-{i}" text-anchor="middle" fill="#0288d1">{msg}</text>\n'

        # Draw Disks with animate tags
        for disk in range(1, self.num_disks + 1):
            w = widths[disk]
            c = colors[disk]
            
            x_vals = []
            y_vals = []
            
            # Use discrete jump interpolation (calcMode="discrete" or "linear")
            # We want them to jump/slide fast. Linear is okay, but we can pause by duplicating states.
            # To make it pause at each state, we use calcMode="discrete"
            
            for (peg_idx, slot_idx) in self.disk_positions[disk]:
                px = peg_x[peg_idx] - w/2
                py = base_y - (slot_idx + 1) * slot_h
                x_vals.append(str(px))
                y_vals.append(str(py))
                
            x_val_str = ";".join(x_vals)
            y_val_str = ";".join(y_vals)
            
            # To hold the position instead of sliding constantly:
            # We want it to stay for 80% of the step, slide for 20%.
            # Using calcMode="discrete" will make it jump instantly, which is perfectly readable for state machines!
            # Let's use calcMode="discrete" to avoid messy slide paths going through other disks.
            
            svg += f'''
<rect x="{x_vals[0]}" y="{y_vals[0]}" width="{w}" height="{slot_h}" fill="{c}" class="disk">
    <animate attributeName="x" values="{x_val_str}" keyTimes="{key_times}" dur="{total_time}s" repeatCount="indefinite" calcMode="discrete"/>
    <animate attributeName="y" values="{y_val_str}" keyTimes="{key_times}" dur="{total_time}s" repeatCount="indefinite" calcMode="discrete"/>
</rect>
'''
        svg += '</svg>'
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)

if __name__ == "__main__":
    out_dir = "05_RecursionAlgorithms/theory/assets"
    os.makedirs(out_dir, exist_ok=True)
    anim = HanoiAnimator(3)
    anim.render(os.path.join(out_dir, "hanoi_animated.svg"))
    print("Hanoi Animated SVG generated successfully!")
