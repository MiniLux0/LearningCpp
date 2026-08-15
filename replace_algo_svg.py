import re

def rep(path, pattern, replacement):
    with open(path, "r", encoding="utf-8") as f: content = f.read()
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    with open(path, "w", encoding="utf-8", newline="\n") as f: f.write(new_content)

# L32 (Fibonacci Tree)
rep("05_RecursionAlgorithms/theory/L32_RecursiveProblems.md", 
    r"```mermaid\s+graph TD\s+F4\[\"fib\(4\)\"\].*?style F2_B.*?```", 
    "![Fibonacci Recursion Tree: Exponential O(2^N) Growth](assets/fib_tree.svg)")

# L33 (Memoized Fibonacci Tree)
rep("05_RecursionAlgorithms/theory/L33_Memoization.md", 
    r"```mermaid\s+graph TD\s+F5\[\"fib\(5\)\"\].*?style F2_C.*?```", 
    "![Memoized Fibonacci Tree: Overlapping Subproblems Pruned](assets/fib_memo_tree.svg)")

print("Markdown files updated.")
