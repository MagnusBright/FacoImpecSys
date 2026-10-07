import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('PROTOTIPO_FACOIMPEC.html', 'r', encoding='utf-8') as f:
    content = f.read()

scripts = re.findall(r'<script.*?>([\s\S]*?)</script>', content)
js = scripts[-1]

lines = js.split('\n')
count = 0
# print first 40 lines with running brace count to find where we go wrong
for i, line in enumerate(lines[:60]):
    for c in line:
        if c == '{': count += 1
        elif c == '}': count -= 1
    print(f"{i}: [{count}] {line[:100]}")
