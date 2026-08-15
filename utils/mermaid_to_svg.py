import os
import re
import subprocess
import time

directories = ['01_GettingStarted', '02_BasicSyntax', '03_Subroutines', '04_ArraysStrings', '05_RecursionAlgorithms']

for d in directories:
    for root, _, files in os.walk(d):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if '```mermaid' not in content:
                    continue
                
                print(f"Processing {path}...")
                
                # Make sure assets dir exists
                assets_dir = os.path.join(root, 'assets')
                if not os.path.exists(assets_dir):
                    os.makedirs(assets_dir)
                
                # Split content to replace safely
                # Regex to match ```mermaid\n...\n```
                blocks = re.split(r'(```mermaid\s*\n.*?```)', content, flags=re.DOTALL)
                
                new_content = ""
                block_counter = 1
                base_name = os.path.splitext(file)[0]
                
                for part in blocks:
                    if part.startswith('```mermaid'):
                        # Extract the mermaid code
                        mmd_code = part[10:-3].strip()
                        
                        # Save to temp
                        with open("temp.mmd", "w", encoding="utf-8") as tmp:
                            tmp.write(mmd_code)
                            
                        # Generate SVG path
                        svg_name = f"flow_{base_name}_{block_counter}.svg"
                        svg_path = os.path.join(assets_dir, svg_name)
                        
                        print(f"  -> Generating {svg_path}...")
                        # Run mmdc
                        # use shell=True on windows for mmdc command resolving
                        cmd = f"mmdc -i temp.mmd -o {svg_path} -b transparent"
                        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        
                        # Replace in markdown
                        rel_path = f"assets/{svg_name}"
                        new_content += f"![Logic Flow Diagram]({rel_path})"
                        block_counter += 1
                    else:
                        new_content += part
                
                with open(path, 'w', encoding='utf-8', newline='\n') as f:
                    f.write(new_content)

if os.path.exists("temp.mmd"):
    os.remove("temp.mmd")
print("All Mermaid blocks successfully eradicated and converted to SVG!")
