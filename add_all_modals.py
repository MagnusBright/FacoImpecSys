"""
Adds/upgrades all modals in build_prototype.py:
1. Upgrade O.C. modal → multi-month support
2. Upgrade Entradas modal → replace prompt() with proper modal
3. Add Almacén → modal to update stock
4. Add Salida/Despacho → modal to register dispatches
"""

with open('scripts/build_prototype.py', 'r', encoding='utf-8') as f:
    content = f.read()

# ──────────────────────────────────────────────────────────────
# 1. UPGRADE O.C. MODAL: add multi-month checkboxes
# ──────────────────────────────────────────────────────────────
old_mes_field = """      <div>
          <label class="block text-xs font-bold text-gray-700 mb-1">Mes correspondiente</label>
          <select id="no-mes" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:border-green-500 focus:outline-none bg-white">
            <option>Enero</option><option>Febrero</option><option>Marzo</option><option>Abril</option>
            <option>Mayo</option><option>Junio</option><option>Julio</option><option>Agosto</option>
            <option>Setiembre</option><option>Octubre</option><option>Noviembre</option><option>Diciembre</option>
          </select>
        </div>"""

new_mes_field = """      <div>
          <label class="block text-xs font-bold text-gray-700 mb-1">Mes(es) correspondientes</label>
          <div class="grid grid-cols-3 gap-1 mt-1" id="no-meses-grid">
            <label class="flex items-center gap-1 text-[11px] cursor-pointer"><input type="checkbox" value="Enero" class="no-mes-cb"> Enero</label>
            <label class="flex items-center gap-1 text-[11px] cursor-pointer"><input type="checkbox" value="Febrero" class="no-mes-cb"> Febrero</label>
            <label class="flex items-center gap-1 text-[11px] cursor-pointer"><input type="checkbox" value="Marzo" class="no-mes-cb"> Marzo</label>
            <label class="flex items-center gap-1 text-[11px] cursor-pointer"><input type="checkbox" value="Abril" class="no-mes-cb"> Abril</label>
            <label class="flex items-center gap-1 text-[11px] cursor-pointer"><input type="checkbox" value="Mayo" class="no-mes-cb"> Mayo</label>
            <label class="flex items-center gap-1 text-[11px] cursor-pointer"><input type="checkbox" value="Junio" class="no-mes-cb"> Junio</label>
            <label class="flex items-center gap-1 text-[11px] cursor-pointer"><input type="checkbox" value="Julio" class="no-mes-cb"> Julio</label>
            <label class="flex items-center gap-1 text-[11px] cursor-pointer"><input type="checkbox" value="Agosto" class="no-mes-cb"> Agosto</label>
            <label class="flex items-center gap-1 text-[11px] cursor-pointer"><input type="checkbox" value="Setiembre" class="no-mes-cb"> Setiembre</label>
            <label class="flex items-center gap-1 text-[11px] cursor-pointer"><input type="checkbox" value="Octubre" class="no-mes-cb"> Octubre</label>
            <label class="flex items-center gap-1 text-[11px] cursor-pointer"><input type="checkbox" value="Noviembre" class="no-mes-cb"> Noviembre</label>
            <label class="flex items-center gap-1 text-[11px] cursor-pointer"><input type="checkbox" value="Diciembre" class="no-mes-cb"> Diciembre</label>
          </div>
        </div>"""

content = content.replace(old_mes_field, new_mes_field)

# Fix the openNewOrderModal JS to pre-check current month
old_open_modal_end = """  document.getElementById('no-mes').value = meses[mesIdx];
}}"""
new_open_modal_end = """  document.querySelectorAll('.no-mes-cb').forEach(cb => cb.checked = false);
  document.querySelectorAll('.no-mes-cb')[mesIdx].checked = true;
}}"""
content = content.replace(old_open_modal_end, new_open_modal_end)

# Fix submitNewOrder to read multiple months
old_mes_read = "  const mes = document.getElementById('no-mes').value;"
new_mes_read = """  const checkedMeses = [...document.querySelectorAll('.no-mes-cb:checked')].map(cb => cb.value);
  if (checkedMeses.length === 0) { alert('Selecciona al menos un mes'); return; }
  const mes = checkedMeses.join(' / ');"""
content = content.replace(old_mes_read, new_mes_read)


# ──────────────────────────────────────────────────────────────
# 2. REPLACE openNuevaEntrada prompt() → modal call
# ──────────────────────────────────────────────────────────────
old_btn_entrada = """<button onclick="openNuevaEntrada()" class="bg-red-600 hover:bg-red-700 text-white text-xs font-bold px-3 py-2 rounded-lg transition">➕ Nueva Entrada</button>"""
new_btn_entrada = """<div class="flex gap-2">
      <button onclick="openModalEntrada()" class="bg-red-600 hover:bg-red-700 text-white text-xs font-bold px-3 py-2 rounded-lg transition">📥 Nueva Entrada</button>
      <button onclick="openModalSalida()" class="bg-orange-500 hover:bg-orange-600 text-white text-xs font-bold px-3 py-2 rounded-lg transition">📤 Registrar Salida</button>
      </div>"""
content = content.replace(old_btn_entrada, new_btn_entrada)


# ──────────────────────────────────────────────────────────────
# 3. ADD BUTTON to Almacén Stock table
# ──────────────────────────────────────────────────────────────
old_almacen_btn = """<button onclick="hitlApproveAll()" class="text-xs bg-amber-50 hover:bg-amber-100 text-amber-700 border border-amber-300 px-3 py-1.5 rounded-lg font-bold transition">🔐 Aprobar Compras HITL</button>"""
new_almacen_btn = """<div class="flex gap-2">
          <button onclick="openModalStock()" class="text-xs bg-blue-50 hover:bg-blue-100 text-blue-700 border border-blue-300 px-3 py-1.5 rounded-lg font-bold transition">📦 Actualizar Stock</button>
          <button onclick="hitlApproveAll()" class="text-xs bg-amber-50 hover:bg-amber-100 text-amber-700 border border-amber-300 px-3 py-1.5 rounded-lg font-bold transition">🔐 Aprobar HITL</button>
          </div>"""
content = content.replace(old_almacen_btn, new_almacen_btn)


# ──────────────────────────────────────────────────────────────
# 4. INJECT NEW MODALS HTML (before </main>)
# ──────────────────────────────────────────────────────────────
new_modals_html = """
<!-- ══ MODAL: NUEVA ENTRADA KARDEX ══════════════════════════ -->
<div id="modalEntrada" class="fixed inset-0 bg-gray-900 bg-opacity-50 hidden items-center justify-center z-50 p-4">
  <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full overflow-hidden">
    <div class="bg-red-600 px-6 py-4 flex items-center justify-between">
      <h3 class="font-black text-white text-lg">📥 Nueva Entrada de Material</h3>
      <button onclick="closeModal('modalEntrada')" class="text-red-200 hover:text-white text-xl">✕</button>
    </div>
    <div class="p-5 space-y-3">
      <div class="grid grid-cols-2 gap-3">
        <div>
          <label class="block text-xs font-bold text-gray-700 mb-1">Producto / Materia Prima</label>
          <input id="ent-producto" type="text" placeholder="Ej: Trigo en Grano" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:border-red-500 focus:outline-none">
        </div>
        <div>
          <label class="block text-xs font-bold text-gray-700 mb-1">Código</label>
          <input id="ent-codigo" type="text" placeholder="Ej: TG" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:border-red-500 focus:outline-none">
        </div>
      </div>
      <div class="grid grid-cols-2 gap-3">
        <div>
          <label class="block text-xs font-bold text-gray-700 mb-1">N° Lote</label>
          <input id="ent-lote" type="text" placeholder="Ej: LT-2026-09" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:border-red-500 focus:outline-none">
        </div>
        <div>
          <label class="block text-xs font-bold text-gray-700 mb-1">Fecha de Entrada</label>
          <input id="ent-fecha" type="date" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:border-red-500 focus:outline-none">
        </div>
      </div>
      <div class="grid grid-cols-3 gap-3">
        <div class="col-span-2">
          <label class="block text-xs font-bold text-gray-700 mb-1">Cantidad</label>
          <input id="ent-cantidad" type="number" placeholder="0" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm font-mono focus:border-red-500 focus:outline-none">
        </div>
        <div>
          <label class="block text-xs font-bold text-gray-700 mb-1">U/M</label>
          <select id="ent-um" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:border-red-500 focus:outline-none bg-white">
            <option>Kg</option><option>TN</option><option>Und</option><option>Saco</option><option>Caja</option>
          </select>
        </div>
      </div>
      <div>
        <label class="block text-xs font-bold text-gray-700 mb-1">Proveedor</label>
        <input id="ent-proveedor" type="text" placeholder="Nombre del proveedor" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:border-red-500 focus:outline-none">
      </div>
      <div>
        <label class="block text-xs font-bold text-gray-700 mb-1">Notas / Observaciones</label>
        <input id="ent-notas" type="text" placeholder="Ej: Lote con devolución parcial" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:border-red-500 focus:outline-none">
      </div>
    </div>
    <div class="px-5 py-4 bg-gray-50 border-t flex justify-end gap-3">
      <button onclick="closeModal('modalEntrada')" class="px-4 py-2 text-sm font-bold text-gray-600">Cancelar</button>
      <button onclick="submitEntrada()" class="px-6 py-2 bg-red-600 hover:bg-red-700 text-white rounded-lg text-sm font-bold transition">Guardar Entrada</button>
    </div>
  </div>
</div>

<!-- ══ MODAL: SALIDA / DESPACHO ══════════════════════════════ -->
<div id="modalSalida" class="fixed inset-0 bg-gray-900 bg-opacity-50 hidden items-center justify-center z-50 p-4">
  <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full overflow-hidden">
    <div class="bg-orange-500 px-6 py-4 flex items-center justify-between">
      <h3 class="font-black text-white text-lg">📤 Registrar Salida / Despacho</h3>
      <button onclick="closeModal('modalSalida')" class="text-orange-200 hover:text-white text-xl">✕</button>
    </div>
    <div class="p-5 space-y-3">
      <div class="grid grid-cols-2 gap-3">
        <div>
          <label class="block text-xs font-bold text-gray-700 mb-1">Municipalidad / Destino</label>
          <input id="sal-destino" type="text" placeholder="Ej: San Miguel" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:border-orange-500 focus:outline-none">
        </div>
        <div>
          <label class="block text-xs font-bold text-gray-700 mb-1">Fecha de Salida</label>
          <input id="sal-fecha" type="date" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:border-orange-500 focus:outline-none">
        </div>
      </div>
      <div class="grid grid-cols-2 gap-3">
        <div>
          <label class="block text-xs font-bold text-gray-700 mb-1">Tipo de Producto</label>
          <select id="sal-tipo" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:border-orange-500 focus:outline-none bg-white">
            <option>Cereal (bolsas)</option>
            <option>Leche (latas)</option>
          </select>
        </div>
        <div>
          <label class="block text-xs font-bold text-gray-700 mb-1">Cantidad</label>
          <input id="sal-cantidad" type="number" placeholder="0" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm font-mono focus:border-orange-500 focus:outline-none">
        </div>
      </div>
      <div>
        <label class="block text-xs font-bold text-gray-700 mb-1">N° Acta / Guía de Remisión</label>
        <input id="sal-acta" type="text" placeholder="Ej: Acta N° 081" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:border-orange-500 focus:outline-none">
      </div>
      <div>
        <label class="block text-xs font-bold text-gray-700 mb-1">Responsable de Recepción</label>
        <input id="sal-responsable" type="text" placeholder="Nombre del responsable" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:border-orange-500 focus:outline-none">
      </div>
    </div>
    <div class="px-5 py-4 bg-gray-50 border-t flex justify-end gap-3">
      <button onclick="closeModal('modalSalida')" class="px-4 py-2 text-sm font-bold text-gray-600">Cancelar</button>
      <button onclick="submitSalida()" class="px-6 py-2 bg-orange-500 hover:bg-orange-600 text-white rounded-lg text-sm font-bold transition">Registrar Salida</button>
    </div>
  </div>
</div>

<!-- ══ MODAL: ACTUALIZAR STOCK ALMACÉN ═══════════════════════ -->
<div id="modalStock" class="fixed inset-0 bg-gray-900 bg-opacity-50 hidden items-center justify-center z-50 p-4">
  <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full overflow-hidden">
    <div class="bg-blue-600 px-6 py-4 flex items-center justify-between">
      <h3 class="font-black text-white text-lg">📦 Actualizar Stock de Almacén</h3>
      <button onclick="closeModal('modalStock')" class="text-blue-200 hover:text-white text-xl">✕</button>
    </div>
    <div class="p-5 space-y-3">
      <div>
        <label class="block text-xs font-bold text-gray-700 mb-1">Material</label>
        <select id="stk-material" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:border-blue-500 focus:outline-none bg-white">
          <option>Trigo en Grano</option>
          <option>Avena Perlada</option>
          <option>Quinua Perlada</option>
          <option>Maca Gelatinizada</option>
          <option>Azúcar Rubia</option>
          <option>Soya Desgrasada</option>
          <option>Leche Evaporada (latas)</option>
          <option>Sacos Vacíos</option>
          <option>Bolsas Impresión</option>
          <option>Premix Vitamínico</option>
        </select>
      </div>
      <div class="grid grid-cols-2 gap-3">
        <div>
          <label class="block text-xs font-bold text-gray-700 mb-1">Tipo de Ajuste</label>
          <select id="stk-tipo" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:border-blue-500 focus:outline-none bg-white">
            <option value="ingreso">➕ Ingreso</option>
            <option value="egreso">➖ Egreso / Consumo</option>
            <option value="ajuste">🔄 Ajuste por Inventario</option>
          </select>
        </div>
        <div>
          <label class="block text-xs font-bold text-gray-700 mb-1">Cantidad (kg / unid.)</label>
          <input id="stk-cantidad" type="number" placeholder="0" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm font-mono focus:border-blue-500 focus:outline-none">
        </div>
      </div>
      <div>
        <label class="block text-xs font-bold text-gray-700 mb-1">Motivo / Referencia</label>
        <input id="stk-motivo" type="text" placeholder="Ej: Compra OC-045, Consumo Lote LOT-C26-095" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:border-blue-500 focus:outline-none">
      </div>
      <div class="bg-blue-50 rounded-lg p-3 text-xs text-blue-700 border border-blue-200">
        ⚠️ Este ajuste actualiza visualmente el stock en la tabla. Para permanencia, requiere sincronización con la base de datos.
      </div>
    </div>
    <div class="px-5 py-4 bg-gray-50 border-t flex justify-end gap-3">
      <button onclick="closeModal('modalStock')" class="px-4 py-2 text-sm font-bold text-gray-600">Cancelar</button>
      <button onclick="submitStock()" class="px-6 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-sm font-bold transition">Aplicar Ajuste</button>
    </div>
  </div>
</div>
"""

content = content.replace('</main>', new_modals_html + '\n</main>')


# ──────────────────────────────────────────────────────────────
# 5. ADD JS FUNCTIONS for the new modals (before // ── INIT)
# ──────────────────────────────────────────────────────────────
new_js = """
function closeModal(id) {{
  document.getElementById(id).classList.add('hidden');
  document.getElementById(id).classList.remove('flex');
}}
function openModal(id) {{
  const el = document.getElementById(id);
  el.classList.remove('hidden');
  el.classList.add('flex');
}}

function openModalEntrada() {{
  const hoy = new Date().toISOString().split('T')[0];
  document.getElementById('ent-fecha').value = hoy;
  openModal('modalEntrada');
}}
function submitEntrada() {{
  const prod = document.getElementById('ent-producto').value.trim();
  if (!prod) {{ alert('Ingresa el nombre del producto'); return; }}
  const cod = document.getElementById('ent-codigo').value || '—';
  const lote = document.getElementById('ent-lote').value || '—';
  const fecha = document.getElementById('ent-fecha').value || new Date().toLocaleDateString('es-PE');
  const cant = parseFloat(document.getElementById('ent-cantidad').value) || 0;
  const um = document.getElementById('ent-um').value;
  const prov = document.getElementById('ent-proveedor').value || '—';
  const notas = document.getElementById('ent-notas').value || '';
  const fechaFmt = fecha ? new Date(fecha + 'T00:00:00').toLocaleDateString('es-PE') : '—';
  const entry = {{ fecha: fechaFmt, producto: prod, codigo: cod, lote, cantidad: cant * (um === 'TN' ? 1000 : 1), um: um === 'TN' ? 'Kg' : um, proveedor: prov, notas }};
  liveKardex.push(entry);
  renderKardex();
  closeModal('modalEntrada');
  alert('✅ Entrada registrada en el Kardex');
}}

function openModalSalida() {{
  const hoy = new Date().toISOString().split('T')[0];
  document.getElementById('sal-fecha').value = hoy;
  openModal('modalSalida');
}}
function submitSalida() {{
  const dest = document.getElementById('sal-destino').value.trim();
  if (!dest) {{ alert('Ingresa el destino'); return; }}
  const fecha = document.getElementById('sal-fecha').value;
  const tipo = document.getElementById('sal-tipo').value;
  const cant = document.getElementById('sal-cantidad').value || '0';
  const acta = document.getElementById('sal-acta').value || '—';
  const resp = document.getElementById('sal-responsable').value || '—';
  const fechaFmt = fecha ? new Date(fecha + 'T00:00:00').toLocaleDateString('es-PE') : '—';
  const entry = {{ fecha: fechaFmt, producto: 'SALIDA - ' + tipo, codigo: 'SAL', lote: acta, cantidad: parseFloat(cant), um: tipo.includes('Cereal') ? 'Bolsas' : 'Latas', proveedor: dest, notas: 'Resp: ' + resp }};
  liveKardex.push(entry);
  renderKardex();
  closeModal('modalSalida');
  alert('✅ Salida registrada en el Kardex\\nDestino: ' + dest);
}}

function openModalStock() {{
  openModal('modalStock');
}}
function submitStock() {{
  const mat = document.getElementById('stk-material').value;
  const tipo = document.getElementById('stk-tipo').value;
  const cant = parseFloat(document.getElementById('stk-cantidad').value) || 0;
  const motivo = document.getElementById('stk-motivo').value || 'Ajuste manual';
  
  // Find the row in the stock table and update it visually
  const rows = document.querySelectorAll('#pane-almacen tbody tr');
  for (const row of rows) {{
    const name = row.querySelector('td')?.textContent?.trim();
    if (name === mat) {{
      const stockCell = row.querySelectorAll('td')[1];
      if (stockCell) {{
        const currentRaw = stockCell.textContent.replace(/[^0-9.]/g, '');
        let current = parseFloat(currentRaw) || 0;
        if (tipo === 'ingreso') current += cant;
        else if (tipo === 'egreso') current -= cant;
        else current = cant; // ajuste directo
        stockCell.textContent = current.toLocaleString('es-PE') + (mat.includes('latas') ? '' : ' kg');
        stockCell.className = stockCell.className; // keep class
      }}
      break;
    }}
  }}
  closeModal('modalStock');
  alert('✅ Stock de ' + mat + ' actualizado\\nMotivo: ' + motivo);
}}

"""

content = content.replace('// ── INIT ────────────────────────────────────────────────────', new_js + '// ── INIT ────────────────────────────────────────────────────')

# ──────────────────────────────────────────────────────────────
# 6. Replace old openNuevaEntrada (uses prompts) with redirect
# ──────────────────────────────────────────────────────────────
import re
content = re.sub(r'function openNuevaEntrada\(\) \{\{[\s\S]*?\}\}\n', 'function openNuevaEntrada() {{ openModalEntrada(); }}\n', content)

with open('scripts/build_prototype.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("All modals injected successfully.")
