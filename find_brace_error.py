import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('PROTOTIPO_FACOIMPEC.html', 'r', encoding='utf-8') as f:
    content = f.read()

scripts = re.findall(r'<script.*?>([\s\S]*?)</script>', content)
js = scripts[-1]

# Find all function declarations and track their brace balance
lines = js.split('\n')
count = 0
for i, line in enumerate(lines):
    for c in line:
        if c == '{': count += 1
        elif c == '}': count -= 1
    if i > len(lines) - 60:
        print(f"{i}: [{count}] {line[:80]}")
