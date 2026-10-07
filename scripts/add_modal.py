import re

with open('scripts/build_prototype.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace the button text and function name in Cereal tab
old_button_html = '<button onclick="addImpromptuOrder()" class="text-xs bg-green-600 hover:bg-green-700 text-white px-3 py-1.5 rounded-lg font-bold transition flex items-center gap-1 shadow-sm">➕ Orden Imprevista</button>'
new_button_html = '<button onclick="openNewOrderModal()" class="text-xs bg-green-600 hover:bg-green-700 text-white px-3 py-1.5 rounded-lg font-bold transition flex items-center gap-1 shadow-sm">➕ Ingresar Orden</button>'
content = content.replace(old_button_html, new_button_html)

# 2. Also add this button to Leche tab just in case, or leave it. Actually the modal can handle both.
# But let's check if the old_button_html was found.
if old_button_html not in content:
    print("WARNING: Old button HTML not found!")

# 3. Add the HTML for the Modal
new_modal_html = """
<!-- ══════════════════════════════════════════════════════════
     MODAL: NUEVA ORDEN DE COMPRA
══════════════════════════════════════════════════════════ -->
<div id="modalNewOrder" class="fixed inset-0 bg-gray-900 bg-opacity-50 hidden items-center justify-center z-50 p-4 transition-opacity">
  <div class="bg-white rounded-2xl shadow-2xl max-w-lg w-full overflow-hidden transform scale-95 transition-transform" id="modalNewOrderPanel">
    <div class="bg-green-600 px-6 py-4 flex items-center justify-between">
      <h3 class="font-black text-white text-lg flex items-center gap-2">🛒 Registrar Orden de Compra</h3>
      <button onclick="closeNewOrderModal()" class="text-green-200 hover:text-white transition">✕</button>
    </div>
    
    <div class="p-6 space-y-4">
      <div class="grid grid-cols-2 gap-4">
        <div>
          <label class="block text-xs font-bold text-gray-700 mb-1">Municipalidad / Cliente</label>
          <input type="text" id="no-mun" placeholder="Ej: San Miguel" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:border-green-500 focus:outline-none">
        </div>
        <div>
          <label class="block text-xs font-bold text-gray-700 mb-1">Mes correspondiente</label>
          <select id="no-mes" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:border-green-500 focus:outline-none bg-white">
            <option>Enero</option><option>Febrero</option><option>Marzo</option><option>Abril</option>
            <option>Mayo</option><option>Junio</option><option>Julio</option><option>Agosto</option>
            <option>Setiembre</option><option>Octubre</option><option>Noviembre</option><option>Diciembre</option>
          </select>
        </div>
      </div>
      
      <div class="grid grid-cols-2 gap-4">
        <div>
          <label class="block text-xs font-bold text-gray-700 mb-1">Producto</label>
          <select id="no-tipo" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:border-green-500 focus:outline-none bg-white">
            <option value="cereal">Cereal (Bolsas)</option>
            <option value="leche">Leche (Latas)</option>
          </select>
        </div>
        <div>
          <label class="block text-xs font-bold text-gray-700 mb-1">Fecha Plazo de Entrega</label>
          <input type="date" id="no-fecha" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:border-green-500 focus:outline-none">
        </div>
      </div>
      
      <div class="grid grid-cols-2 gap-4 border-t border-gray-100 pt-4">
        <div>
          <label class="block text-xs font-bold text-gray-700 mb-1" id="lbl-cant">Cantidad (Bolsas)</label>
          <input type="number" id="no-cant" placeholder="0" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm font-mono focus:border-green-500 focus:outline-none">
        </div>
        <div>
          <label class="block text-xs font-bold text-gray-700 mb-1" id="lbl-peso">Kg por Bolsa</label>
          <input type="number" id="no-peso" value="1" step="0.01" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm font-mono focus:border-green-500 focus:outline-none">
        </div>
      </div>
      
      <div class="bg-gray-50 p-3 rounded-lg border border-gray-200 mt-2">
        <div class="flex justify-between items-center">
          <span class="text-xs text-gray-500 font-bold">TOTAL ESTIMADO:</span>
          <span class="font-black text-lg text-green-700" id="no-total">0.00 kg</span>
        </div>
      </div>
    </div>
    
    <div class="px-6 py-4 bg-gray-50 border-t border-gray-200 flex justify-end gap-3">
      <button onclick="closeNewOrderModal()" class="px-4 py-2 text-sm font-bold text-gray-600 hover:text-gray-800 transition">Cancelar</button>
      <button onclick="submitNewOrder()" class="px-6 py-2 bg-green-600 hover:bg-green-700 text-white rounded-lg text-sm font-bold transition shadow-sm flex items-center gap-2">
        Guardar Orden
      </button>
    </div>
  </div>
</div>
"""
# Insert modal before </main>
content = content.replace("</main>", new_modal_html + "\n</main>")


# 4. Replace the old JS function with the new ones
old_js_func_regex = r'function addImpromptuOrder\(\) \{\{[\s\S]*?\}\}'
new_js_funcs = """
function openNewOrderModal() {{
  const m = document.getElementById('modalNewOrder');
  const p = document.getElementById('modalNewOrderPanel');
  m.classList.remove('hidden');
  m.classList.add('flex');
  setTimeout(() => p.classList.remove('scale-95'), 10);
  
  // Reset fields
  document.getElementById('no-mun').value = '';
  document.getElementById('no-cant').value = '';
  document.getElementById('no-total').textContent = '0.00 kg';
  
  // Set default month to current actual month
  const mesIdx = new Date().getMonth();
  const meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Setiembre','Octubre','Noviembre','Diciembre'];
  document.getElementById('no-mes').value = meses[mesIdx];
}}

function closeNewOrderModal() {{
  const m = document.getElementById('modalNewOrder');
  const p = document.getElementById('modalNewOrderPanel');
  p.classList.add('scale-95');
  setTimeout(() => {{
    m.classList.add('hidden');
    m.classList.remove('flex');
  }}, 150);
}}

// Listeners for dynamic updates in modal
document.addEventListener('DOMContentLoaded', () => {{
  const tipo = document.getElementById('no-tipo');
  const cant = document.getElementById('no-cant');
  const peso = document.getElementById('no-peso');
  
  if(tipo && cant && peso) {{
    const updateTotal = () => {{
      const c = parseFloat(cant.value) || 0;
      if(tipo.value === 'cereal') {{
        const p = parseFloat(peso.value) || 0;
        document.getElementById('no-total').textContent = (c * p).toLocaleString('es-PE', {{minimumFractionDigits:2}}) + ' kg';
      }} else {{
        document.getElementById('no-total').textContent = (c / 48).toFixed(1) + ' cajas';
      }}
    }};
    
    tipo.addEventListener('change', () => {{
      const isLeche = tipo.value === 'leche';
      document.getElementById('lbl-cant').textContent = isLeche ? 'Cantidad (Latas)' : 'Cantidad (Bolsas)';
      document.getElementById('no-peso').parentElement.style.display = isLeche ? 'none' : 'block';
      updateTotal();
    }});
    
    cant.addEventListener('input', updateTotal);
    peso.addEventListener('input', updateTotal);
  }}
}});

function submitNewOrder() {{
  const mun = document.getElementById('no-mun').value.trim();
  if (!mun) return alert('Debes ingresar la municipalidad');
  
  const mes = document.getElementById('no-mes').value;
  const fecha = document.getElementById('no-fecha').value || 'Por definir';
  const tipo = document.getElementById('no-tipo').value;
  const cant = parseFloat(document.getElementById('no-cant').value) || 0;
  const peso = parseFloat(document.getElementById('no-peso').value) || 1;
  
  if (tipo === 'cereal') {{
    const tbody = document.getElementById('tbody-cereal');
    const tbodyPend = document.getElementById('tbody-pend-cereal');
    const totalKg = cant * peso;
    
    // Create new row for main cereal tab
    const rowHtml = `
      <tr class="trow hover:bg-green-50 transition bg-green-50" data-mes="${{mes}}" data-mun="${{mun.toLowerCase()}}">
        <td class="px-3 py-2 font-semibold text-green-800 text-xs">${{mun}} <span class="text-[9px] bg-green-200 text-green-800 px-1 rounded uppercase ml-1">Nuevo</span></td>
        <td class="px-3 py-2 text-xs text-gray-600">${{mes}}</td>
        <td class="px-3 py-2 text-xs font-mono text-gray-700">${{fecha}}</td>
        <td class="px-2 py-1"><input type="date" onchange="markDateSaved(this)" class="text-[10px] border border-gray-300 rounded p-1 w-24 bg-white focus:border-red-500 text-blue-700 font-mono"></td>
        <td class="px-2 py-1"><input type="date" onchange="markDateSaved(this)" class="text-[10px] border border-gray-300 rounded p-1 w-24 bg-white focus:border-red-500 text-amber-700 font-mono"></td>
        <td class="px-2 py-1"><input type="date" onchange="markDateSaved(this)" class="text-[10px] border border-gray-300 rounded p-1 w-24 bg-white focus:border-red-500 text-purple-700 font-mono"></td>
        <td class="px-3 py-2 text-xs font-mono text-right">${{cant}}</td>
        <td class="px-3 py-2 text-xs font-mono text-right">${{peso}}</td>
        <td class="px-3 py-2 text-xs font-mono text-right font-bold text-red-700">${{totalKg.toFixed(2)}}</td>
        <td class="px-3 py-2 text-xs font-mono text-right">-</td>
        <td class="px-3 py-2 text-xs font-mono text-right">-</td>
      </tr>`;
      
    // Create new row for pendientes tab
    const rowPendHtml = `
      <tr class="trow hover:bg-orange-50 transition bg-orange-50" data-mes="${{mes}}">
        <td class="px-2 py-1 font-semibold text-gray-800 text-[11px] truncate max-w-[120px]">${{mun}} <span class="text-[9px] bg-orange-200 text-orange-800 px-1 rounded uppercase ml-1">Nuevo</span></td>
        <td class="px-2 py-1 text-[11px] text-gray-600 truncate max-w-[70px]">${{mes}}</td>
        <td class="px-2 py-1 text-[11px] font-mono text-gray-700">${{fecha}}</td>
        <td class="px-2 py-1 text-[11px] font-mono text-right">${{cant}}</td>
        <td class="px-2 py-1 text-[11px] font-mono text-right">${{peso}}</td>
        <td class="px-2 py-1 text-[11px] font-mono text-right font-bold text-orange-700">${{totalKg.toFixed(2)}}</td>
        <td class="px-2 py-1 text-[11px] font-mono text-right">-</td>
        <td class="px-2 py-1 text-[11px] font-mono text-right">-</td>
        <td class="px-2 py-1 text-[11px] font-mono text-right">-</td>
      </tr>`;
      
    if(tbody) tbody.insertAdjacentHTML('afterbegin', rowHtml);
    if(tbodyPend) tbodyPend.insertAdjacentHTML('afterbegin', rowPendHtml);
    applyTableFilters('cereal');
    
  }} else {{
    // Leche
    const tbody = document.getElementById('tbody-leche');
    const tbodyPend = document.getElementById('tbody-pend-leche');
    const cajas = (cant / 48).toFixed(1);
    
    const rowHtml = `
      <tr class="trow hover:bg-green-50 transition bg-green-50" data-mes="${{mes}}">
        <td class="px-3 py-2 font-semibold text-green-800 text-xs">${{mun}} <span class="text-[9px] bg-green-200 text-green-800 px-1 rounded uppercase ml-1">Nuevo</span></td>
        <td class="px-3 py-2 text-xs text-gray-600">${{mes}}</td>
        <td class="px-3 py-2 text-xs font-mono text-gray-700">${{fecha}}</td>
        <td class="px-3 py-2 text-xs font-mono text-right font-bold text-blue-700">${{cant}}</td>
        <td class="px-3 py-2 text-xs font-mono text-right">${{cajas}}</td>
        <td class="px-3 py-2 text-xs font-mono text-right">-</td>
        <td class="px-3 py-2 text-xs text-center">🟡</td>
        <td class="px-2 py-1"><input type="date" class="text-[10px] border border-gray-300 rounded p-1 w-24 bg-white focus:border-blue-500 font-mono"></td>
      </tr>`;
      
    const rowPendHtml = `
      <tr class="trow hover:bg-orange-50 transition bg-orange-50" data-mes="${{mes}}">
        <td class="px-2 py-1 font-semibold text-gray-800 text-[11px] truncate max-w-[120px]">${{mun}} <span class="text-[9px] bg-orange-200 text-orange-800 px-1 rounded uppercase ml-1">Nuevo</span></td>
        <td class="px-2 py-1 text-[11px] text-gray-600 truncate max-w-[70px]">${{mes}}</td>
        <td class="px-2 py-1 text-[11px] font-mono text-gray-700">${{fecha}}</td>
        <td class="px-2 py-1 text-[11px] font-mono text-right font-bold text-blue-700">${{cant}}</td>
        <td class="px-2 py-1 text-[11px] font-mono text-right">${{cajas}}</td>
        <td class="px-2 py-1 text-[11px] font-mono text-right">-</td>
      </tr>`;
      
    if(tbody) tbody.insertAdjacentHTML('afterbegin', rowHtml);
    if(tbodyPend) tbodyPend.insertAdjacentHTML('afterbegin', rowPendHtml);
    applyTableFilters('leche');
  }}
  
  closeNewOrderModal();
  // Optional visually show toast
}}
"""

content = re.sub(old_js_func_regex, new_js_funcs, content)

with open('scripts/build_prototype.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Modal added and old impromptu order function replaced.")
