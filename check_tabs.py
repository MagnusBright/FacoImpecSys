import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/build_prototype.py', 'r', encoding='utf-8') as f:
    content = f.read()

tabs = re.findall(r'id="pane-([\w-]+)"', content)
print('Tabs:', tabs)

# Check what action buttons already exist per tab
open_fns = re.findall(r'onclick="(open\w+|addNote|openNueva\w*)\(\)"', content)
print('Open funcs:', list(set(open_fns)))

# Check what tab headers look like (for finding where to add buttons)
sections = re.findall(r'<!-- ══.*?──', content)
print('Sections:', sections[:20])
