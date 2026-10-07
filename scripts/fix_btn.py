import re

with open('scripts/build_prototype.py', 'r', encoding='utf-8') as f:
    content = f.read()

btn = re.search(r'<button onclick="addImpromptuOrder\(\)".*?</button>', content)
if btn:
    print('Found:', btn.group(0))
    content = content.replace(btn.group(0), '<button onclick="openNewOrderModal()" class="text-xs bg-green-600 hover:bg-green-700 text-white px-3 py-1.5 rounded-lg font-bold transition flex items-center gap-1 shadow-sm">➕ Agregar O.C.</button>')
    with open('scripts/build_prototype.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Replaced!")
else:
    print("Not found")
