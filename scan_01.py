import os, re
d = '01_GettingStarted'
for root, _, files in os.walk(d):
    for file in files:
        if file.endswith('.md'):
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                content = f.read()
            blocks = re.findall(r'```mermaid(.*?)```', content, re.DOTALL)
            for b in blocks:
                print(f"--- {file} ---")
                print(b.strip())
