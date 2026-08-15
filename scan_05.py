import os
import re

d = '05_RecursionAlgorithms'
for root, _, files in os.walk(d):
    for file in files:
        if file.endswith('.md'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            if '```mermaid' in content:
                print(f"\n--- {path} ---")
                blocks = re.findall(r'```mermaid(.*?)```', content, re.DOTALL)
                for i, block in enumerate(blocks):
                    print(f"Block {i+1}:\n{block.strip()}\n")
