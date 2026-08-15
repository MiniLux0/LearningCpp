import os

def create_svg_wrapper(width, height, content):
    return f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
<rect width="100%" height="100%" fill="#ffffff" />
<style>
  .title {{ font-family: sans-serif; font-size: 16px; font-weight: bold; fill: #343a40; }}
  .text {{ font-family: sans-serif; font-size: 14px; fill: #212529; }}
  .mono {{ font-family: monospace; font-size: 13px; fill: #e63946; }}
  .addr {{ font-family: monospace; font-size: 12px; fill: #6c757d; }}
  .box {{ fill: #f8f9fa; stroke: #adb5bd; stroke-width: 2; }}
  .box-ref {{ fill: #e3f2fd; stroke: #1976d2; stroke-width: 2; }}
</style>
{content}
</svg>'''

def generate_array_1d(out_path):
    boxes = ""
    for i in range(4):
        x = 50 + i * 120
        boxes += f'''
        <rect class="box" x="{x}" y="80" width="100" height="60" rx="4"/>
        <text class="addr" x="{x+50}" y="70" text-anchor="middle">0x100{hex(i*4)[2:].upper()}</text>
        <text class="mono" x="{x+50}" y="105" text-anchor="middle">arr[{i}]</text>
        <text class="text" x="{x+50}" y="125" text-anchor="middle" font-weight="bold">{(i+1)*10}</text>
        '''
        if i < 3:
            boxes += f'<line x1="{x+100}" y1="110" x2="{x+120}" y2="110" stroke="#adb5bd" stroke-width="2"/>'

    content = f'''
    <text class="title" x="50" y="40">1D Array Contiguous Memory (int: 4 bytes)</text>
    {boxes}
    '''
    with open(out_path, 'w', encoding='utf-8') as f: f.write(create_svg_wrapper(600, 180, content))

def generate_array_2d(out_path):
    boxes = ""
    for i in range(6):
        x = 50 + i * 100
        row = i // 3
        col = i % 3
        bg = "#f1f8e9" if row == 0 else "#fff3e0"
        stroke = "#7cb342" if row == 0 else "#fb8c00"
        
        boxes += f'''
        <rect x="{x}" y="80" width="90" height="60" rx="4" fill="{bg}" stroke="{stroke}" stroke-width="2"/>
        <text class="mono" x="{x+45}" y="105" text-anchor="middle">mat[{row}][{col}]</text>
        <text class="addr" x="{x+45}" y="125" text-anchor="middle">Index: {i}</text>
        '''
        if i < 5:
            boxes += f'<line x1="{x+90}" y1="110" x2="{x+100}" y2="110" stroke="#adb5bd" stroke-width="2"/>'
            
    content = f'''
    <text class="title" x="50" y="40">2D Matrix Row-Major Order Flattening (2x3)</text>
    <rect x="50" y="50" width="290" height="20" fill="#7cb342" rx="4"/>
    <text class="text" x="195" y="65" text-anchor="middle" fill="white" font-weight="bold">Row 0</text>
    <rect x="350" y="50" width="290" height="20" fill="#fb8c00" rx="4"/>
    <text class="text" x="495" y="65" text-anchor="middle" fill="white" font-weight="bold">Row 1</text>
    {boxes}
    '''
    with open(out_path, 'w', encoding='utf-8') as f: f.write(create_svg_wrapper(700, 180, content))

def generate_cstring(out_path):
    chars = ['H', 'e', 'l', 'l', 'o', '!', '\\0']
    boxes = ""
    for i, c in enumerate(chars):
        x = 50 + i * 70
        is_null = (c == '\\0')
        bg = "#ffebee" if is_null else "#f8f9fa"
        stroke = "#e53935" if is_null else "#adb5bd"
        boxes += f'''
        <rect x="{x}" y="80" width="60" height="60" rx="4" fill="{bg}" stroke="{stroke}" stroke-width="2"/>
        <text class="addr" x="{x+30}" y="70" text-anchor="middle">idx {i}</text>
        <text class="text" x="{x+30}" y="110" text-anchor="middle" font-weight="bold" font-size="20">'{c}'</text>
        '''
    
    content = f'''
    <text class="title" x="50" y="40">C-String Memory Layout (char array)</text>
    {boxes}
    <path d="M 50 160 L 50 170 L 400 170 L 400 160" fill="none" stroke="#1976d2" stroke-width="2"/>
    <text class="text" x="225" y="190" text-anchor="middle" fill="#1976d2">Useful Length (strlen) = 6</text>
    
    <path d="M 50 200 L 50 210 L 470 210 L 470 200" fill="none" stroke="#e53935" stroke-width="2"/>
    <text class="text" x="260" y="230" text-anchor="middle" fill="#e53935">Physically Allocated Capacity = 7 bytes (Includes Null Terminator)</text>
    '''
    with open(out_path, 'w', encoding='utf-8') as f: f.write(create_svg_wrapper(600, 260, content))

def generate_reference(out_path):
    content = '''
    <text class="title" x="50" y="40">Pass by Reference vs Pass by Value in RAM</text>
    
    <!-- RAM Box -->
    <rect class="box" x="250" y="80" width="150" height="100" rx="8"/>
    <text class="addr" x="325" y="70" text-anchor="middle">RAM Address: 0x7ffd</text>
    <text class="text" x="325" y="115" text-anchor="middle">Data (int)</text>
    <text class="title" x="325" y="145" text-anchor="middle" font-size="24">10</text>
    
    <!-- main() var -->
    <rect class="box" x="50" y="100" width="120" height="40" rx="4" fill="#e8f5e9" stroke="#388e3c"/>
    <text class="text" x="110" y="125" text-anchor="middle">main() num</text>
    <line x1="170" y1="120" x2="240" y2="120" stroke="#388e3c" stroke-width="2" marker-end="url(#arrow-green)"/>
    
    <!-- Function param -->
    <rect class="box" x="480" y="100" width="160" height="40" rx="4" fill="#fff3e0" stroke="#f57c00"/>
    <text class="text" x="560" y="125" text-anchor="middle">Func() Alias: int& x</text>
    <line x1="480" y1="120" x2="410" y2="120" stroke="#f57c00" stroke-width="2" marker-end="url(#arrow-orange)"/>
    
    <defs>
        <marker id="arrow-green" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="#388e3c"/>
        </marker>
        <marker id="arrow-orange" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="#f57c00"/>
        </marker>
    </defs>
    
    <text class="text" x="325" y="210" text-anchor="middle" fill="#d32f2f">Both identifiers point to the EXACT same memory cell.</text>
    '''
    with open(out_path, 'w', encoding='utf-8') as f: f.write(create_svg_wrapper(700, 240, content))


if __name__ == '__main__':
    generate_array_1d('04_ArraysStrings/theory/assets/array_1d.svg')
    generate_array_2d('04_ArraysStrings/theory/assets/array_2d.svg')
    generate_cstring('04_ArraysStrings/theory/assets/cstring_null.svg')
    generate_reference('03_Subroutines/theory/assets/pass_by_ref.svg')
    print("Memory visuals generated successfully.")
