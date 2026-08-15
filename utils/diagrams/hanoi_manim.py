from manim import *

class HanoiScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        # Title
        title = Text("Torres de Hanói (N=3)", color=BLACK, font_size=36).to_edge(UP)
        self.add(title)
        
        # Pegs
        peg_xs = [-4, 0, 4]
        pegs = [
            Rectangle(width=0.2, height=3, color=GRAY, fill_opacity=1).move_to([x, -1.5, 0])
            for x in peg_xs
        ]
        base = Rectangle(width=10, height=0.2, color=GRAY, fill_opacity=1).move_to([0, -3, 0])
        self.add(*pegs, base)
        
        # Labels
        labels = [
            Text(label, color=DARK_GRAY, font_size=24).move_to([x, -3.5, 0])
            for x, label in zip(peg_xs, ["A (Origen)", "B (Auxiliar)", "C (Destino)"])
        ]
        self.add(*labels)
        
        # Disks
        disk_colors = [BLUE, ORANGE, RED] # 1 (smallest), 2, 3 (largest)
        disk_widths = [1.5, 2.5, 3.5]
        disk_height = 0.4
        
        disks = []
        for i in range(3):
            d = Rectangle(width=disk_widths[i], height=disk_height, stroke_color=WHITE, fill_color=disk_colors[i], fill_opacity=1)
            disks.append(d)
            
        # Initial positions on Peg 0 (3, 2, 1 from bottom to top)
        # index 2 is the largest (RED), index 0 is smallest (BLUE)
        self.pegs_state = [[2, 1, 0], [], []]
        for slot_idx, disk_idx in enumerate(self.pegs_state[0]):
            disks[disk_idx].move_to([peg_xs[0], -2.9 + slot_idx * disk_height, 0])
            self.add(disks[disk_idx])
            
        self.wait(1)
        self.solve(3, 0, 2, 1, disks, peg_xs, disk_height)
        self.wait(2)
        
    def solve(self, n, source, target, aux, disks, peg_xs, dh):
        if n > 0:
            self.solve(n-1, source, aux, target, disks, peg_xs, dh)
            
            # Move disk
            disk_idx = self.pegs_state[source].pop()
            disk = disks[disk_idx]
            slot_idx = len(self.pegs_state[target])
            
            # Animate in a smooth arc! Manim allows this easily
            target_pos = [peg_xs[target], -2.9 + slot_idx * dh, 0]
            
            # Arc movement is much more elegant
            self.play(
                disk.animate.move_to(target_pos),
                path_arc= -PI/2 if target > source else PI/2,
                run_time=0.6,
                rate_func=smooth
            )
            
            self.pegs_state[target].append(disk_idx)
            
            self.solve(n-1, aux, target, source, disks, peg_xs, dh)

if __name__ == "__main__":
    import os
    os.system("manim -qm --format=gif utils/diagrams/hanoi_manim.py HanoiScene")
