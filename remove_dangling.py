with open('scripts/build_prototype.py', 'r', encoding='utf-8') as f:
    content = f.read()

# The dangling remnant from the old addImpromptuOrder function starts with
# a template literal continuation and ends with the closing alert+brace.
# Find the exact start marker and end marker.
start_marker = '\" data-mun=\"${{mun.toLowerCase()}}\">\n'
end_marker = '  alert(`\u2705 Orden imprevista para ${{mun}} agregada a la vista local.`);\n}}\n'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    # Remove the dangling block including the end marker
    content = content[:start_idx] + content[end_idx + len(end_marker):]
    print(f"Removed dangling block ({end_idx - start_idx} chars)")
else:
    print(f"start_idx={start_idx}, end_idx={end_idx}")
    # Try alternate approach - find by lines
    lines = content.split('\n')
    new_lines = []
    skip = False
    for i, line in enumerate(lines):
        if 'data-mun="${{mun.toLowerCase()}}">' in line and not skip:
            skip = True
        if skip:
            if 'Orden imprevista para' in line:
                # also skip the closing }}
                skip = False
                continue
            continue
        new_lines.append(line)
    content = '\n'.join(new_lines)
    print("Used line-by-line removal fallback")

with open('scripts/build_prototype.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done. Rebuilding...")
