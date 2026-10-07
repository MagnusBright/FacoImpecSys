import re

with open('scripts/build_prototype.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace ANY button that calls addImpromptuOrder with openNewOrderModal
content = re.sub(r'<button[^>]*onclick="addImpromptuOrder\(\)"[^>]*>.*?</button>',
                 '<button onclick="openNewOrderModal()" class="text-xs bg-green-600 hover:bg-green-700 text-white px-3 py-1.5 rounded-lg font-bold transition flex items-center gap-1 shadow-sm">➕ Registrar O.C.</button>',
                 content)

with open('scripts/build_prototype.py', 'w', encoding='utf-8') as f:
    f.write(content)
