import re

with open('PROTOTIPO_FACOIMPEC.html', 'r', encoding='utf-8') as f:
    content = f.read()

scripts = re.findall(r'<script.*?>([\s\S]*?)</script>', content)
js = scripts[-1]

count = 0
for c in js:
    if c == '{': count += 1
    elif c == '}': count -= 1

print(f"Brace balance: {count} (should be 0)")
