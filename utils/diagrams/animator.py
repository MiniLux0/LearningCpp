import os

class ArrayAnimator:
    def __init__(self, title, arr_len, box_w=60, box_h=60, spacing=20):
        self.title = title
        self.arr_len = arr_len
        self.box_w = box_w
        self.box_h = box_h
        self.spacing = spacing
        self.step_dur = 2.0 # seconds per step
        self.steps = []
        
    def add_step(self, arr, pointers=None, highlights=None, message=""):
        if pointers is None: pointers = {}
        if highlights is None: highlights = []
        self.steps.append({
            "arr": list(arr),
            "pointers": dict(pointers),
            "highlights": list(highlights),
            "message": message
        })
        
    def render(self, path):
        num_steps = len(self.steps)
        total_time = num_steps * self.step_dur
        
        width = max(800, self.arr_len * (self.box_w + self.spacing) + 100)
        height = 350
        
        svg = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
        svg += f'<rect width="{width}" height="{height}" fill="#ffffff"/>\n'
        svg += '''<style>
    text { font-family: 'Segoe UI', Roboto, Helvetica, sans-serif; }
    .box { fill: #f8f9fa; stroke: #dee2e6; stroke-width: 2; transition: all 0.3s; }
    .box-hl { fill: #fff3cd; stroke: #ffc107; stroke-width: 3; }
    .box-found { fill: #d4edda; stroke: #28a745; stroke-width: 3; }
    .box-text { font-size: 18px; font-weight: bold; fill: #343a40; }
    .ptr-text { font-size: 14px; font-weight: bold; }
    .ptr-line { stroke-width: 2; stroke-dasharray: 4; }
    .msg-text { font-size: 16px; fill: #495057; font-weight: bold; opacity: 0; }
'''
        
        # We need to generate keyframes for each element that changes.
        # Elements: 
        # 1. Pointers (x positions)
        # 2. Box values (text changes? For sorting yes)
        # 3. Messages (opacity toggles)
        # 4. Box highlights (color changes, we can do this via CSS animation on fill/stroke)
        
        # It's actually easier to use <g> layers for each STEP and just animate their opacity!
        # Since it's SVG, hiding/showing a whole step layer is trivial.
        # Keyframe: step-N
        # 0% - 10%: opacity 0
        # 10% - 30%: opacity 1 ... etc.
        # Let's compute exact percentages.
        
        for i in range(num_steps):
            start_pct = (i / num_steps) * 100
            end_pct = ((i + 1) / num_steps) * 100
            
            # To avoid flickering, make it visible precisely from start to end
            svg += f'''
    @keyframes show-step-{i} {{
        0%, {max(0, start_pct - 0.1):.1f}% {{ opacity: 0; }}
        {start_pct:.1f}%, {end_pct - 0.1:.1f}% {{ opacity: 1; }}
        {end_pct:.1f}%, 100% {{ opacity: 0; }}
    }}
    .step-{i} {{ animation: show-step-{i} {total_time}s infinite; opacity: 0; }}
'''
        svg += '</style>\n'
        
        svg += f'<text x="{width/2}" y="30" font-size="22" font-weight="bold" text-anchor="middle" fill="#212529">{self.title}</text>\n'
        
        x_offset = (width - (self.arr_len * (self.box_w + self.spacing) - self.spacing)) / 2
        y_offset = 120
        
        for i, step in enumerate(self.steps):
            svg += f'<g class="step-{i}">\n'
            
            # Render Info Box
            svg += f'''
    <rect x="{width/2 - 200}" y="240" width="400" height="80" rx="8" fill="#f8f9fa" stroke="#dee2e6" stroke-width="2"/>
    <text x="{width/2}" y="265" font-size="14" font-weight="bold" text-anchor="middle" fill="#0288d1">Step {i+1} / {num_steps}</text>
    <text x="{width/2}" y="295" font-size="16" text-anchor="middle" fill="#343a40">{step['message']}</text>
'''
            
            # Render Array
            for j in range(self.arr_len):
                bx = x_offset + j * (self.box_w + self.spacing)
                by = y_offset
                
                # Highlight logic
                hl_class = "box"
                if "found" in step.get("state", "") and j in step["highlights"]:
                    hl_class = "box-found"
                elif j in step["highlights"]:
                    hl_class = "box-hl"
                    
                val = step["arr"][j]
                
                svg += f'    <rect x="{bx}" y="{by}" width="{self.box_w}" height="{self.box_h}" rx="6" class="{hl_class}"/>\n'
                svg += f'    <text x="{bx + self.box_w/2}" y="{by + 36}" class="box-text" text-anchor="middle">{val}</text>\n'
                svg += f'    <text x="{bx + self.box_w/2}" y="{by + 80}" font-size="12" fill="#adb5bd" text-anchor="middle">[{j}]</text>\n'
                
            # Render Pointers
            colors = ["#d32f2f", "#0288d1", "#f57c00", "#388e3c", "#8e24aa"]
            p_idx = 0
            for ptr_name, ptr_pos in step["pointers"].items():
                if ptr_pos < 0 or ptr_pos >= self.arr_len: continue
                c = colors[p_idx % len(colors)]
                px = x_offset + ptr_pos * (self.box_w + self.spacing) + self.box_w/2
                
                # Draw pointer above or below
                if p_idx % 2 == 0: # Above
                    svg += f'    <line x1="{px}" y1="{y_offset - 40}" x2="{px}" y2="{y_offset - 10}" class="ptr-line" stroke="{c}"/>\n'
                    svg += f'    <text x="{px}" y="{y_offset - 45}" class="ptr-text" fill="{c}" text-anchor="middle">{ptr_name}</text>\n'
                else: # Below (further down)
                    svg += f'    <line x1="{px}" y1="{y_offset + 95}" x2="{px}" y2="{y_offset + 125}" class="ptr-line" stroke="{c}"/>\n'
                    svg += f'    <text x="{px}" y="{y_offset + 140}" class="ptr-text" fill="{c}" text-anchor="middle">{ptr_name}</text>\n'
                p_idx += 1
                
            svg += '</g>\n'
            
        svg += '</svg>'
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)

# Algorithms Logic
def build_binary_search():
    arr = [2, 7, 12, 19, 25, 30, 42]
    target = 25
    anim = ArrayAnimator("Binary Search: Target = 25", len(arr))
    
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            anim.add_step(arr, {"low": low, "high": high, "mid": mid}, highlights=[mid], message=f"arr[mid] ({arr[mid]}) == {target}. Found!")
            anim.steps[-1]["state"] = "found"
            # Add an extra frame to hold the "found" state longer
            anim.add_step(arr, {"low": low, "high": high, "mid": mid}, highlights=[mid], message=f"Algorithm Complete.")
            anim.steps[-1]["state"] = "found"
            break
            
        elif arr[mid] < target:
            anim.add_step(arr, {"low": low, "high": high, "mid": mid}, highlights=[mid], message=f"arr[mid] ({arr[mid]}) < {target}. Discard left half.")
            low = mid + 1
        else:
            anim.add_step(arr, {"low": low, "high": high, "mid": mid}, highlights=[mid], message=f"arr[mid] ({arr[mid]}) > {target}. Discard right half.")
            high = mid - 1
            
    anim.render("05_RecursionAlgorithms/theory/assets/binary_search.svg")

def build_bubble_sort():
    arr = [5, 1, 4, 2, 8]
    anim = ArrayAnimator("Bubble Sort (First Pass)", len(arr))
    
    anim.add_step(arr, {}, [], "Initial Array")
    n = len(arr)
    # Just do 1 pass for the animation to not be too long
    for j in range(0, n-1):
        anim.add_step(arr, {"j": j, "j+1": j+1}, highlights=[j, j+1], message=f"Compare {arr[j]} and {arr[j+1]}")
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            anim.add_step(arr, {"j": j, "j+1": j+1}, highlights=[j, j+1], message=f"Swap! {arr[j+1]} > {arr[j]}")
        else:
            anim.add_step(arr, {"j": j, "j+1": j+1}, highlights=[j, j+1], message=f"No swap needed")
    
    anim.add_step(arr, {"sorted": n-1}, highlights=[n-1], message="Pass complete. 8 is bubbled up!")
    anim.steps[-1]["state"] = "found"
    anim.render("05_RecursionAlgorithms/theory/assets/bubble_sort.svg")

def build_selection_sort():
    arr = [64, 25, 12, 22, 11]
    anim = ArrayAnimator("Selection Sort (First Pass)", len(arr))
    anim.add_step(arr, {}, [], "Initial Array")
    
    # Just pass 1
    i = 0
    min_idx = i
    anim.add_step(arr, {"i": i, "min": min_idx}, highlights=[i], message="Assume first unsorted element is minimum")
    for j in range(i+1, len(arr)):
        anim.add_step(arr, {"i": i, "min": min_idx, "j": j}, highlights=[min_idx, j], message=f"Compare current min {arr[min_idx]} with {arr[j]}")
        if arr[j] < arr[min_idx]:
            min_idx = j
            anim.add_step(arr, {"i": i, "min": min_idx, "j": j}, highlights=[min_idx], message=f"New minimum found: {arr[min_idx]} at index {min_idx}")
            
    anim.add_step(arr, {"i": i, "min": min_idx}, highlights=[i, min_idx], message=f"Swap {arr[i]} with {arr[min_idx]}")
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
    anim.add_step(arr, {"i": i}, highlights=[i], message="First element is now sorted")
    anim.steps[-1]["state"] = "found"
    anim.render("05_RecursionAlgorithms/theory/assets/selection_sort.svg")

def build_insertion_sort():
    arr = [12, 11, 13, 5, 6]
    anim = ArrayAnimator("Insertion Sort (First 2 Elements)", len(arr))
    anim.add_step(arr, {}, highlights=[0], message="First element is trivially sorted")
    
    # Pass 1
    key = arr[1]
    j = 0
    anim.add_step(arr, {"key=11": 1, "j": j}, highlights=[0, 1], message="Select 11 as key. Compare with 12")
    arr[1] = arr[0]
    anim.add_step(arr, {"key=11": 1, "j": j}, highlights=[0, 1], message="12 > 11. Shift 12 to the right")
    arr[0] = key
    anim.add_step(arr, {}, highlights=[0, 1], message="Insert key 11 at index 0. [11, 12] sorted.")
    anim.steps[-1]["state"] = "found"
    anim.render("05_RecursionAlgorithms/theory/assets/insertion_sort.svg")

if __name__ == "__main__":
    os.makedirs("05_RecursionAlgorithms/theory/assets", exist_ok=True)
    build_binary_search()
    build_bubble_sort()
    build_selection_sort()
    build_insertion_sort()
    print("Architectural Algorithm SVGs generated!")
