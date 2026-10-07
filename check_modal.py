import re

with open('PROTOTIPO_FACOIMPEC.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("BTN:", bool(re.search(r"openNewOrderModal", content)))
print("MODAL HTML:", bool(re.search(r"id=\"modalNewOrder\"", content)))
print("JS:", bool(re.search(r"function openNewOrderModal", content)))
