import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = r"c:\Users\FACOIMPEC\Documents\SISTEMA_Facoimpec\FACO"
artifact_dir  = r"C:\Users\FACOIMPEC\.gemini\antigravity\brain\2c5464e3-4bae-4ebf-97a3-c3ff6bd7d756"

with open(os.path.join(workspace_dir, "data/logo_b64.txt"), "r") as f:
    logo_b64 = f.read().strip()

with open(os.path.join(workspace_dir, "data/formulas_data.json"), "r", encoding="utf-8") as f:
    formulas_data = json.load(f)

with open(os.path.join(workspace_dir, "data/full_data.json"), "r", encoding="utf-8") as f:
    pendientes_data = json.load(f)

with open(os.path.join(workspace_dir, "data/entregado_data.json"), "r", encoding="utf-8") as f:
    entregado_data = json.load(f)

with open(os.path.join(workspace_dir, "data/resumen_cereal_data.json"), "r", encoding="utf-8") as f:
    resumen_cereal_data = json.load(f)

formulas_json     = json.dumps(formulas_data, ensure_ascii=False)
pendientes_json   = json.dumps(pendientes_data, ensure_ascii=False)
entregado_json    = json.dumps(entregado_data, ensure_ascii=False)
resumen_json      = json.dumps(resumen_cereal_data, ensure_ascii=False)

# ─── Requerimientos 000236 y 000237 ────────────────────────────────────────────
REQ_236 = {
    "numero": "000236", "tipo": "Proyección Septiembre", "fecha": "23/09/2026", "estado": "APROBADO",
    "items": [
        {"codigo": "TG26",  "descripcion": "Trigo en Grano",              "um": "TN", "cantidad": 30},
        {"codigo": "AV31",  "descripcion": "Avena Perlada Estabilizada",  "um": "TN", "cantidad": 44},
        {"codigo": "Q20",   "descripcion": "Quinua PVL",                  "um": "TN", "cantidad": 1.5},
        {"codigo": "MZC1B", "descripcion": "Maíz Chiclayano",             "um": "TN", "cantidad": 1.2},
        {"codigo": "LP13",  "descripcion": "Leche en Polvo",              "um": "Kg", "cantidad": 350},
        {"codigo": "AZ21",  "descripcion": "Azúcar",                      "um": "TN", "cantidad": 10},
        {"codigo": "KW13",  "descripcion": "Kiwicha",                     "um": "Kg", "cantidad": 850},
        {"codigo": "CC6",   "descripcion": "Cacao",                       "um": "Kg", "cantidad": 75},
    ]
}
REQ_237 = {
    "numero": "000237", "tipo": "Proyección Octubre", "fecha": "23/09/2026", "estado": "PENDIENTE_HITL",
    "items": [
        {"codigo": "TG27",  "descripcion": "Trigo en grano",              "um": "TN", "cantidad": 25},
        {"codigo": "AV32",  "descripcion": "Avena Perlada Estabilizada",  "um": "TN", "cantidad": 112},
        {"codigo": "AZ22",  "descripcion": "Azúcar",                      "um": "TN", "cantidad": 22},
        {"codigo": "Q21",   "descripcion": "Quinua",                      "um": "TN", "cantidad": 7.5},
        {"codigo": "MZC19", "descripcion": "Maíz Chiclayano",             "um": "TN", "cantidad": 1.5},
        {"codigo": "LP14",  "descripcion": "Leche en Polvo",              "um": "Kg", "cantidad": 900},
        {"codigo": "KW14",  "descripcion": "Kiwicha",                     "um": "Kg", "cantidad": 300},
    ]
}

# ─── Kardex histórico Jul / Ago / Sep 2026 (entradas) ──────────────────────────
KARDEX_HIST = [
    # JULIO 2026
    {"fecha":"01/07/2026","producto":"Sacos",             "codigo":"SACO",  "lote":"",   "cantidad":3000,  "um":"Und","proveedor":"","notas":""},
    {"fecha":"02/07/2026","producto":"Avena",             "codigo":"AV",    "lote":"24", "cantidad":15000, "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"03/07/2026","producto":"Azúcar",            "codigo":"AZ",    "lote":"16", "cantidad":32000, "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"04/07/2026","producto":"Maíz chufla",       "codigo":"MZC",   "lote":"11", "cantidad":1000,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"06/07/2026","producto":"S. Leche",          "codigo":"SL",    "lote":"6",  "cantidad":20,    "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"06/07/2026","producto":"S. Lucuma",         "codigo":"SLC",   "lote":"1",  "cantidad":20,    "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"06/07/2026","producto":"S. Plátano",        "codigo":"SP",    "lote":"5",  "cantidad":20,    "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"06/07/2026","producto":"S. Vainilla",       "codigo":"SV",    "lote":"2",  "cantidad":20,    "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"07/07/2026","producto":"Sacos",             "codigo":"SACO",  "lote":"",   "cantidad":2000,  "um":"Und","proveedor":"","notas":""},
    {"fecha":"07/07/2026","producto":"Maíz chufla",       "codigo":"MZC",   "lote":"12", "cantidad":1518,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"10/07/2026","producto":"Quinua",            "codigo":"Q",     "lote":"14", "cantidad":8000,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"10/07/2026","producto":"Maíz chufla",       "codigo":"MZC",   "lote":"14", "cantidad":1978,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"13/07/2026","producto":"Avena",             "codigo":"AV",    "lote":"25", "cantidad":42000, "um":"Kg", "proveedor":"Pacífico","notas":"Pacifico"},
    {"fecha":"15/07/2026","producto":"Kiwicha",           "codigo":"KW",    "lote":"11", "cantidad":750,   "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"15/07/2026","producto":"Maíz chufla",       "codigo":"MZC",   "lote":"15", "cantidad":500,   "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"16/07/2026","producto":"Maíz Pollo",        "codigo":"MZP",   "lote":"7",  "cantidad":900,   "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"18/07/2026","producto":"Sacos",             "codigo":"SACO",  "lote":"",   "cantidad":2000,  "um":"Und","proveedor":"","notas":""},
    {"fecha":"19/07/2026","producto":"Avena",             "codigo":"AV",    "lote":"26", "cantidad":280000,"um":"Kg", "proveedor":"","notas":""},
    {"fecha":"19/07/2026","producto":"Leche en Polvo",    "codigo":"LP",    "lote":"9",  "cantidad":1000,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"23/07/2026","producto":"Azúcar",            "codigo":"AZ",    "lote":"17", "cantidad":1500,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"24/07/2026","producto":"Trigo",             "codigo":"TG",    "lote":"18", "cantidad":10000, "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"24/07/2026","producto":"Quinua",            "codigo":"Q",     "lote":"15", "cantidad":3000,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"24/07/2026","producto":"Soya",              "codigo":"SY",    "lote":"4",  "cantidad":3000,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"24/07/2026","producto":"Sacos",             "codigo":"SACO",  "lote":"",   "cantidad":2000,  "um":"Und","proveedor":"","notas":""},
    {"fecha":"24/07/2026","producto":"Quinua Qaliwarma",  "codigo":"QQ",    "lote":"4",  "cantidad":200,   "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"25/07/2026","producto":"Azúcar",            "codigo":"AZ",    "lote":"18", "cantidad":34000, "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"30/07/2026","producto":"Trigo",             "codigo":"TG",    "lote":"19", "cantidad":6000,  "um":"Kg", "proveedor":"","notas":""},
    # AGOSTO 2026
    {"fecha":"01/08/2026","producto":"Quinua Qaliwarma",  "codigo":"QQ",    "lote":"5",  "cantidad":250,   "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"01/08/2026","producto":"Kiwicha",           "codigo":"KW",    "lote":"12", "cantidad":500,   "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"02/08/2026","producto":"Trigo",             "codigo":"TG",    "lote":"20", "cantidad":24000, "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"02/08/2026","producto":"Maca",              "codigo":"MC",    "lote":"11", "cantidad":6000,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"03/08/2026","producto":"Soya",              "codigo":"SY",    "lote":"5",  "cantidad":30000, "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"03/08/2026","producto":"Quinua",            "codigo":"Q",     "lote":"16", "cantidad":6000,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"03/08/2026","producto":"Maíz chufla",       "codigo":"MZC",   "lote":"16", "cantidad":1400,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"07/08/2026","producto":"Sacos",             "codigo":"SACO",  "lote":"",   "cantidad":3000,  "um":"Und","proveedor":"","notas":""},
    {"fecha":"14/08/2026","producto":"Maca",              "codigo":"MC",    "lote":"12", "cantidad":6000,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"14/08/2026","producto":"Trigo",             "codigo":"TG",    "lote":"21", "cantidad":30000, "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"14/08/2026","producto":"Leche en Polvo",    "codigo":"LP",    "lote":"10", "cantidad":1000,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"15/08/2026","producto":"Leche en Polvo",    "codigo":"LP",    "lote":"11", "cantidad":250,   "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"15/08/2026","producto":"S. Leche",          "codigo":"SL",    "lote":"7",  "cantidad":20,    "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"15/08/2026","producto":"S. Plátano",        "codigo":"SP",    "lote":"6",  "cantidad":20,    "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"15/08/2026","producto":"Maíz pollo",        "codigo":"MZP",   "lote":"8",  "cantidad":900,   "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"20/08/2026","producto":"Sacos",             "codigo":"SACO",  "lote":"",   "cantidad":2000,  "um":"Und","proveedor":"","notas":""},
    {"fecha":"22/08/2026","producto":"Azúcar",            "codigo":"AZ",    "lote":"19", "cantidad":3200,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"26/08/2026","producto":"Sacos",             "codigo":"SACO",  "lote":"",   "cantidad":2000,  "um":"Und","proveedor":"","notas":""},
    {"fecha":"27/08/2026","producto":"Quinua",            "codigo":"Q",     "lote":"17", "cantidad":6000,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"27/08/2026","producto":"Maca",              "codigo":"MC",    "lote":"13", "cantidad":7000,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"27/08/2026","producto":"Trigo",             "codigo":"TG",    "lote":"22", "cantidad":22000, "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"28/08/2026","producto":"Quinua",            "codigo":"Q",     "lote":"18", "cantidad":1000,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"28/08/2026","producto":"Trigo",             "codigo":"TG",    "lote":"23", "cantidad":6000,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"28/08/2026","producto":"Cocoa",             "codigo":"CC",    "lote":"4",  "cantidad":325,   "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"28/08/2026","producto":"Azúcar",            "codigo":"AZ",    "lote":"20", "cantidad":32000, "um":"Kg", "proveedor":"","notas":""},
    # SEPTIEMBRE 2026
    {"fecha":"03/09/2026","producto":"Trigo",             "codigo":"TG",    "lote":"24", "cantidad":36000, "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"05/09/2026","producto":"Quinua",            "codigo":"Q",     "lote":"19", "cantidad":7000,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"07/09/2026","producto":"Avena",             "codigo":"AV",    "lote":"27", "cantidad":30000, "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"07/09/2026","producto":"Maca",              "codigo":"MC",    "lote":"14", "cantidad":6000,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"07/09/2026","producto":"Cocoa",             "codigo":"CC",    "lote":"5",  "cantidad":125,   "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"07/09/2026","producto":"Maíz chufla",       "codigo":"MZC",   "lote":"17", "cantidad":1334,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"09/09/2026","producto":"Leche en Polvo",    "codigo":"LP",    "lote":"12", "cantidad":2000,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"11/09/2026","producto":"S. Leche",          "codigo":"SL",    "lote":"8",  "cantidad":40,    "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"11/09/2026","producto":"S. Plátano",        "codigo":"SP",    "lote":"7",  "cantidad":20,    "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"14/09/2026","producto":"Avena",             "codigo":"AV",    "lote":"28", "cantidad":15000, "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"17/09/2026","producto":"Trigo",             "codigo":"TG",    "lote":"25", "cantidad":7000,  "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"17/09/2026","producto":"Maíz Pollo",        "codigo":"MZP",   "lote":"9",  "cantidad":900,   "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"18/09/2026","producto":"Avena",             "codigo":"AV",    "lote":"29", "cantidad":21000, "um":"Kg", "proveedor":"","notas":"6 tn devolución - total 27"},
    {"fecha":"18/09/2026","producto":"Quinua Qaliwarma",  "codigo":"QQ",    "lote":"",   "cantidad":285,   "um":"Kg", "proveedor":"","notas":""},
    {"fecha":"23/09/2026","producto":"Avena",             "codigo":"AV",    "lote":"30", "cantidad":36000, "um":"Kg", "proveedor":"","notas":""},
]

KARDEX_JSON = json.dumps(KARDEX_HIST, ensure_ascii=False)
REQ_JSON    = json.dumps([REQ_236, REQ_237], ensure_ascii=False)

# ─── Generate Cereal rows from pendientes ────────────────────────────────────
def cereal_rows():
    rows = ""
    for item in pendientes_data.get("cereal", []):
        m  = item.get("mes","")
        fn = item.get("fecha","")
        bl = item.get("bolsas",0)
        kg = item.get("kg_bolsa",0)
        tk = item.get("total_kg",0)
        cs = item.get("cap_saco",0)
        ns = item.get("n_sacos",0)
        un = item.get("unidades",0)
        mu = item.get("mun","")
        
        f_prod = item.get("f_prod", "")
        f_env  = item.get("f_env", "")
        f_des  = item.get("f_des", "")
        
        # fallback dates if empty to avoid breaking layout
        if not f_prod: f_prod = ""
        if not f_env: f_env = ""
        if not f_des: f_des = ""

        rows += f"""
          <tr class="trow hover:bg-red-50 transition" data-mes="{m}" data-mun="{mu.lower()}">
            <td class="px-3 py-2 font-semibold text-gray-800 text-xs">{mu}</td>
            <td class="px-3 py-2 text-xs text-gray-600">{m}</td>
            <td class="px-3 py-2 text-xs font-mono text-gray-700">{fn}</td>
            <td class="px-2 py-1"><input type="date" value="{f_prod}" onchange="markDateSaved(this)" class="text-[10px] border border-gray-300 rounded p-1 w-24 bg-white focus:border-red-500 focus:ring-1 focus:ring-red-500 text-blue-700 font-mono"></td>
            <td class="px-2 py-1"><input type="date" value="{f_env}" onchange="markDateSaved(this)" class="text-[10px] border border-gray-300 rounded p-1 w-24 bg-white focus:border-red-500 focus:ring-1 focus:ring-red-500 text-amber-700 font-mono"></td>
            <td class="px-2 py-1"><input type="date" value="{f_des}" onchange="markDateSaved(this)" class="text-[10px] border border-gray-300 rounded p-1 w-24 bg-white focus:border-red-500 focus:ring-1 focus:ring-red-500 text-purple-700 font-mono"></td>
            <td class="px-3 py-2 text-xs font-mono text-right">{bl:,}</td>
            <td class="px-3 py-2 text-xs font-mono text-right">{kg}</td>
            <td class="px-3 py-2 text-xs font-mono text-right font-bold text-red-700">{tk:,.2f}</td>
            <td class="px-3 py-2 text-xs font-mono text-right">{cs}</td>
            <td class="px-3 py-2 text-xs font-mono text-right">{ns}</td>
          </tr>"""
    return rows

def pendientes_cereal_rows():
    rows = ""
    for item in pendientes_data.get("cereal", []):
        if item.get("empresa", "").upper() != "PENDIENTE": continue
        m  = item.get("mes","")
        fn = item.get("fecha","")
        bl = item.get("bolsas",0)
        kg = item.get("kg_bolsa",0)
        tk = item.get("total_kg",0)
        cs = item.get("cap_saco",0)
        ns = item.get("n_sacos",0)
        un = item.get("unidades",0)
        mu = item.get("mun","")
        
        rows += f"""
          <tr class="trow hover:bg-orange-50 transition" data-mes="{m}">
            <td class="px-2 py-1 font-semibold text-gray-800 text-[11px] truncate max-w-[120px]">{mu}</td>
            <td class="px-2 py-1 text-[11px] text-gray-600 truncate max-w-[70px]">{m}</td>
            <td class="px-2 py-1 text-[11px] font-mono text-gray-700">{fn}</td>
            <td class="px-2 py-1 text-[11px] font-mono text-right">{bl:,}</td>
            <td class="px-2 py-1 text-[11px] font-mono text-right">{kg}</td>
            <td class="px-2 py-1 text-[11px] font-mono text-right font-bold text-orange-700">{tk:,.2f}</td>
            <td class="px-2 py-1 text-[11px] font-mono text-right">{cs}</td>
            <td class="px-2 py-1 text-[11px] font-mono text-right">{ns}</td>
            <td class="px-2 py-1 text-[11px] font-mono text-right">{un}</td>
          </tr>"""
    return rows

def leche_rows():
    rows = ""
    for item in pendientes_data.get("leche", []):
        m  = item.get("mes","")
        fn = item.get("fecha","")
        la = item.get("latas",0)
        cj = item.get("cajas",0)
        un = item.get("unidades",0)
        mu = item.get("mun","")
        conf = item.get("confirmacion", "")
        f_ent = item.get("f_ent", "")
        
        status = "✅" if conf == "Confirmado" else "🟡"
        rows += f"""
          <tr class="trow hover:bg-blue-50 transition" data-mes="{m}">
            <td class="px-3 py-2 font-semibold text-gray-800 text-xs">{mu}</td>
            <td class="px-3 py-2 text-xs text-gray-600">{m}</td>
            <td class="px-3 py-2 text-xs font-mono text-gray-700">{fn}</td>
            <td class="px-3 py-2 text-xs font-mono text-right font-bold text-blue-700">{la:,.0f}</td>
            <td class="px-3 py-2 text-xs font-mono text-right">{cj:,.0f}</td>
            <td class="px-3 py-2 text-xs font-mono text-right">{un}</td>
            <td class="px-3 py-2 text-xs text-center">{status}</td>
            <td class="px-2 py-1"><input type="date" value="{f_ent}" onchange="markDateSaved(this)" class="text-[10px] border border-gray-300 rounded p-1 w-24 bg-white focus:border-blue-500 focus:ring-1 focus:ring-blue-500 font-mono"></td>
          </tr>"""
    return rows

def pendientes_leche_rows():
    rows = ""
    for item in pendientes_data.get("leche", []):
        if item.get("empresa", "").upper() != "PENDIENTE": continue
        m  = item.get("mes","")
        fn = item.get("fecha","")
        la = item.get("latas",0)
        cj = item.get("cajas",0)
        un = item.get("unidades",0)
        mu = item.get("mun","")
        
        rows += f"""
          <tr class="trow hover:bg-orange-50 transition" data-mes="{m}">
            <td class="px-2 py-1 font-semibold text-gray-800 text-[11px] truncate max-w-[120px]">{mu}</td>
            <td class="px-2 py-1 text-[11px] text-gray-600 truncate max-w-[70px]">{m}</td>
            <td class="px-2 py-1 text-[11px] font-mono text-gray-700">{fn}</td>
            <td class="px-2 py-1 text-[11px] font-mono text-right font-bold text-blue-700">{la:,.0f}</td>
            <td class="px-2 py-1 text-[11px] font-mono text-right">{cj:,.0f}</td>
            <td class="px-2 py-1 text-[11px] font-mono text-right">{un}</td>
          </tr>"""
    return rows

def entregado_cereal_rows():
    rows = ""
    for item in entregado_data.get("cereal", []):
        m  = item.get("mes","")
        fn = item.get("fecha","")
        bl = item.get("bolsas",0)
        kg = item.get("kg_bolsa",0)
        tk = item.get("total_kg",0)
        ns = item.get("n_sacos",0)
        mu = item.get("mun","")
        fe = item.get("f_entrega", fn)
        rows += f"""
          <tr class="trow hover:bg-green-50 transition" data-mes="{m}">
            <td class="px-3 py-2 font-semibold text-gray-800 text-xs">{mu}</td>
            <td class="px-3 py-2 text-xs text-gray-600">{m}</td>
            <td class="px-3 py-2 text-xs font-mono text-gray-700">{fn}</td>
            <td class="px-3 py-2 text-xs font-mono text-right">{bl:,}</td>
            <td class="px-3 py-2 text-xs font-mono text-right">{kg}</td>
            <td class="px-3 py-2 text-xs font-mono text-right font-bold text-green-700">{tk:,.2f}</td>
            <td class="px-3 py-2 text-xs font-mono text-right">{ns}</td>
            <td class="px-3 py-2 text-xs font-mono text-right text-green-600 font-bold">{fe}</td>
          </tr>"""
    return rows

def entregado_leche_rows():
    rows = ""
    for item in entregado_data.get("leche", []):
        m  = item.get("mes","")
        fn = item.get("fecha","")
        la = item.get("latas",0)
        ca = item.get("cajas",0)
        mu = item.get("mun","")
        fe = item.get("f_entrega", fn)
        rows += f"""
          <tr class="trow hover:bg-green-50 transition" data-mes="{m}">
            <td class="px-3 py-2 font-semibold text-gray-800 text-xs">{mu}</td>
            <td class="px-3 py-2 text-xs text-gray-600">{m}</td>
            <td class="px-3 py-2 text-xs font-mono text-gray-700">{fn}</td>
            <td class="px-3 py-2 text-xs font-mono text-right font-bold text-blue-700">{la:,}</td>
            <td class="px-3 py-2 text-xs font-mono text-right">{ca}</td>
            <td class="px-3 py-2 text-xs font-mono text-right text-green-600 font-bold">{fe}</td>
          </tr>"""
    return rows

def resumen_rows():
    rows = ""
    for item in resumen_cereal_data:
        m  = item.get("mes","")
        mu = item.get("mun","")
        fn = item.get("fecha","")
        tk = item.get("total_kg",0)
        tr = item.get("trigo",0)
        av = item.get("avena",0)
        qi = item.get("quinua",0)
        so = item.get("soya",0)
        ma = item.get("maca",0)
        az = item.get("azucar",0)
        rows += f"""
          <tr class="trow hover:bg-gray-50 transition" data-mes="{m}">
            <td class="px-3 py-2 font-semibold text-gray-800 text-xs">{mu}</td>
            <td class="px-3 py-2 text-xs text-gray-600">{m}</td>
            <td class="px-3 py-2 text-xs font-mono text-gray-700">{fn}</td>
            <td class="px-3 py-2 text-xs font-mono text-right font-bold text-red-700">{tk:,.2f}</td>
            <td class="px-3 py-2 text-xs font-mono text-right">{tr:,.2f}</td>
            <td class="px-3 py-2 text-xs font-mono text-right">{av:,.2f}</td>
            <td class="px-3 py-2 text-xs font-mono text-right">{qi:,.2f}</td>
            <td class="px-3 py-2 text-xs font-mono text-right">{so:,.2f}</td>
            <td class="px-3 py-2 text-xs font-mono text-right">{ma:,.2f}</td>
            <td class="px-3 py-2 text-xs font-mono text-right">{az:,.2f}</td>
          </tr>"""
    return rows

def formulas_options():
    opts = ""
    for dist in formulas_data.keys():
        opts += f'<option value="{dist}">{dist}</option>'
    return opts

# ─── Requerimientos HTML ────────────────────────────────────────────────────
def req_html(req):
    color = "green" if req["estado"] == "APROBADO" else "amber"
    label = "✅ Aprobado" if req["estado"] == "APROBADO" else "⏳ Pendiente Aprobación HITL"
    rows = ""
    for it in req["items"]:
        um_col = "text-blue-600" if it["um"] == "Kg" else "text-red-600"
        rows += f"""<tr class="hover:bg-gray-50">
          <td class="px-3 py-1.5 text-xs font-mono text-gray-500">{it['codigo']}</td>
          <td class="px-3 py-1.5 text-xs font-semibold text-gray-800">{it['descripcion']}</td>
          <td class="px-3 py-1.5 text-xs font-mono {um_col}">{it['um']}</td>
          <td class="px-3 py-1.5 text-xs font-bold font-mono text-right text-red-700">{it['cantidad']:g}</td>
        </tr>"""
    btn = "" if req["estado"] == "APROBADO" else f"""
      <button onclick="aprobarReq('{req['numero']}')"
        class="mt-3 w-full bg-red-600 hover:bg-red-700 text-white text-xs font-bold py-2 rounded-lg transition flex items-center justify-center gap-2">
        🔐 Aprobar Requerimiento (HITL)
      </button>"""
    return f"""
    <div class="bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden">
      <div class="bg-gray-50 border-b border-gray-200 px-4 py-3 flex items-center justify-between">
        <div>
          <span class="text-xs font-black text-gray-800">REQUERIMIENTO N° {req['numero']}</span>
          <span class="ml-2 text-xs text-gray-500">{req['tipo']} — {req['fecha']}</span>
        </div>
        <span class="text-xs font-bold px-2 py-0.5 rounded-full bg-{color}-100 text-{color}-700 border border-{color}-200">{label}</span>
      </div>
      <table class="w-full text-left">
        <thead class="bg-gray-50 text-[10px] uppercase text-gray-400">
          <tr>
            <th class="px-3 py-2">Código</th>
            <th class="px-3 py-2">Descripción</th>
            <th class="px-3 py-2">U/M</th>
            <th class="px-3 py-2 text-right">Cantidad</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-100">{rows}</tbody>
      </table>
      <div class="px-4 pb-4">{btn}</div>
    </div>"""

req_cards_html = req_html(REQ_236) + req_html(REQ_237)

# ─── Month Filter Component ─────────────────────────────────────────────────
MONTHS = ["Enero","Febrero","Marzo","Abril","Mayo","Junio",
          "Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre","Todos"]

def month_filter(filter_id):
    pills = ""
    for m in MONTHS:
        active = ' style="background:#DC1B24;color:#fff;border-color:#DC1B24;"' if m == "Todos" else ""
        pills += f'<button onclick="filterMonth(\'{filter_id}\',this,\'{m}\')" class="month-pill px-3 py-1 rounded-full text-xs font-semibold border border-gray-300 text-gray-600 hover:border-red-400 hover:text-red-600 transition"{active}>{m}</button>\n'
    return f"""
    <div class="flex flex-wrap gap-1.5 items-center py-2 px-1" id="mf-{filter_id}">
      <span class="text-[11px] font-bold text-gray-400 uppercase mr-1">Mes:</span>
      {pills}
    </div>"""

# ─── HTML ───────────────────────────────────────────────────────────────────
html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FACOIMPEC E.I.R.L. — Sistema de Gestión Operativa</title>
  <link rel="icon" type="image/png" href="data:image/png;base64,{logo_b64}">
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    :root {{ --faco: #DC1B24; --faco-dk: #B91820; --faco-lt: #FEF2F2; }}
    body {{ background: #F3F4F6; }}
    ::-webkit-scrollbar {{ width:6px; height:6px; }}
    ::-webkit-scrollbar-track {{ background:#f1f1f1; }}
    ::-webkit-scrollbar-thumb {{ background:#DC1B24; border-radius:4px; }}

    /* Tab system */
    .tab-pane {{ display:none; }}
    .tab-pane.active {{ display:block; }}

    /* Active tab */
    .tab-btn.active {{
      background: #DC1B24 !important;
      color: #fff !important;
      border-color: #DC1B24 !important;
      box-shadow: 0 2px 8px rgba(220,27,36,0.3);
    }}

    /* Sticky note */
    .sticky-note {{
      background: #fffde7;
      border: 1px solid #f9a825;
      border-radius: 8px;
      padding: 10px 12px;
      min-height: 60px;
      font-size: 12px;
      color: #5d4037;
      position: relative;
      cursor: pointer;
      transition: box-shadow .2s;
    }}
    .sticky-note:hover {{ box-shadow: 0 4px 12px rgba(249,168,37,.4); }}
    .sticky-note textarea {{
      width:100%; border:none; background:transparent; font-size:12px;
      color:#5d4037; resize:none; outline:none; min-height:50px;
    }}
    .sticky-note .note-label {{
      font-size:9px; font-weight:700; letter-spacing:.08em;
      text-transform:uppercase; color:#f57f17; margin-bottom:4px;
    }}

    /* WhatsApp theme */
    .wa-bg {{ background:#0b141a; }}
    .wa-bubble-user {{
      background:#005c4b; color:#e9edef; border-radius:12px 2px 12px 12px;
      padding:8px 12px; max-width:80%; font-size:13px; line-height:1.5;
      margin-left:auto; margin-bottom:6px;
    }}
    .wa-bubble-bot {{
      background:#202c33; color:#e9edef; border-radius:2px 12px 12px 12px;
      padding:8px 12px; max-width:85%; font-size:13px; line-height:1.5;
      margin-bottom:6px;
    }}
    .wa-time {{ font-size:10px; color:#8696a0; margin-top:2px; text-align:right; }}

    /* Voice recording animation */
    @keyframes pulse-rec {{ 0%,100%{{opacity:1}} 50%{{opacity:.4}} }}
    .rec-dot {{ animation: pulse-rec 1s infinite; display:inline-block;
      width:10px; height:10px; background:#ef4444; border-radius:50%; }}

    /* HITL confirm strip */
    .hitl-strip {{
      background: linear-gradient(135deg, #fff3cd 0%, #fff8e1 100%);
      border: 1.5px solid #f59e0b;
      border-radius: 10px;
      padding: 10px 14px;
      margin-top: 6px;
      font-size: 12px;
    }}

    /* Tables */
    table {{ border-collapse: collapse; width: 100%; }}
    th {{ background: #f9fafb; color: #6b7280; font-size: 10px; text-transform: uppercase; letter-spacing: .06em; padding: 8px 12px; }}
    td {{ padding: 6px 12px; font-size: 12px; border-bottom: 1px solid #f3f4f6; }}

    /* Formula editor modal */
    #formulaModal {{ display:none; }}
    #formulaModal.open {{ display:flex; }}
  </style>
</head>
<body class="min-h-screen font-sans antialiased">

<!-- ── HEADER ─────────────────────────────────────────────────────────────── -->
<header class="bg-white border-b border-gray-200 shadow-sm sticky top-0 z-50">
  <div class="max-w-[1700px] mx-auto px-4 py-3">
    <div class="flex flex-col lg:flex-row lg:items-center gap-3">

      <!-- Logo + Title -->
      <div class="flex items-center gap-3 flex-1">
        <div class="w-14 h-14 rounded-xl bg-white border-2 border-red-200 shadow flex items-center justify-center flex-shrink-0 overflow-hidden">
          <img src="data:image/png;base64,{logo_b64}" alt="FACOIMPEC" class="w-full h-full object-contain">
        </div>
        <div>
          <div class="flex items-center gap-2 flex-wrap">
            <span class="text-xs font-black tracking-widest text-red-600 uppercase">FACOIMPEC E.I.R.L.</span>
            <span class="text-[11px] text-gray-400 font-mono">RUC: 20539916379 · Huanchaco</span>
            <span class="text-[11px] bg-green-50 text-green-700 border border-green-200 px-2 py-0.5 rounded-full font-bold flex items-center gap-1">
              <span class="w-1.5 h-1.5 bg-green-500 rounded-full animate-pulse inline-block"></span>
              SQLite Local (facoimpec.db)
            </span>
          </div>
          <h1 class="text-base font-black text-gray-900 leading-tight">
            Sistema Integral MRP · Almacén · Retenciones OSCE
          </h1>
        </div>
      </div>

      <!-- Quick Stats -->
      <div class="flex items-center gap-3 flex-wrap">
        <button onclick="openPdfModal()" class="bg-red-600 hover:bg-red-700 text-white px-3 py-2 rounded-lg text-xs font-bold flex items-center gap-1.5 transition shadow-sm">
          📄 Cargar O.C. / Contrato PDF
        </button>
        <a href="Control stock 2026.xlsx" download class="bg-green-600 hover:bg-green-700 text-white px-3 py-2 rounded-lg text-xs font-bold flex items-center gap-1.5 transition shadow-sm">
          📊 Bajar Excel Original
        </a>
        <div class="flex gap-3 bg-gray-50 border border-gray-200 px-3 py-2 rounded-lg text-xs font-mono">
          <div class="text-right">
            <div class="text-[10px] text-gray-400 font-sans uppercase font-bold">Leche Stock</div>
            <div class="font-black text-blue-600">123,680 latas</div>
          </div>
          <div class="w-px bg-gray-200"></div>
          <div class="text-right">
            <div class="text-[10px] text-gray-400 font-sans uppercase font-bold">Demanda Oct</div>
            <div class="font-black text-red-600">112 TN avena</div>
          </div>
          <div class="w-px bg-gray-200"></div>
          <div class="text-right">
            <div class="text-[10px] text-gray-400 font-sans uppercase font-bold">Retenciones</div>
            <div class="font-black text-amber-600">S/. 62,000</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Nav Tabs -->
    <nav class="flex flex-wrap gap-1 mt-3 pt-2 border-t border-gray-100">
      <button onclick="setTab('cereal')" id="tab-cereal" class="tab-btn active px-3 py-1.5 rounded-lg text-xs font-bold border border-gray-200 text-gray-600 bg-white hover:border-red-300 transition">🥣 1. Cereal</button>
      <button onclick="setTab('leche')" id="tab-leche" class="tab-btn px-3 py-1.5 rounded-lg text-xs font-bold border border-gray-200 text-gray-600 bg-white hover:border-red-300 transition">🥛 2. Leche</button>
      <button onclick="setTab('produccion')" id="tab-produccion" class="tab-btn px-3 py-1.5 rounded-lg text-xs font-bold border border-gray-200 text-gray-600 bg-white hover:border-red-300 transition">⚙️ 3. Producción</button>
      <button onclick="setTab('entradas')" id="tab-entradas" class="tab-btn px-3 py-1.5 rounded-lg text-xs font-bold border border-gray-200 text-gray-600 bg-white hover:border-red-300 transition">📥 4. Entradas & Salidas</button>
      <button onclick="setTab('almacen')" id="tab-almacen" class="tab-btn px-3 py-1.5 rounded-lg text-xs font-bold border border-gray-200 text-gray-600 bg-white hover:border-red-300 transition">📦 5. Almacén & Proyecciones</button>
      <button onclick="setTab('formulas')" id="tab-formulas" class="tab-btn px-3 py-1.5 rounded-lg text-xs font-bold border border-gray-200 text-gray-600 bg-white hover:border-red-300 transition">📐 6. Fórmulas (161)</button>
      <button onclick="setTab('pendientes')" id="tab-pendientes" class="tab-btn px-3 py-1.5 rounded-lg text-xs font-bold border border-gray-200 text-gray-600 bg-white hover:border-red-300 transition">📋 7. Pendientes</button>
      <button onclick="setTab('entregado')" id="tab-entregado" class="tab-btn px-3 py-1.5 rounded-lg text-xs font-bold border border-gray-200 text-gray-600 bg-white hover:border-red-300 transition">✅ 8. Entregado</button>
      <button onclick="setTab('resumen')" id="tab-resumen" class="tab-btn px-3 py-1.5 rounded-lg text-xs font-bold border border-gray-200 text-gray-600 bg-white hover:border-red-300 transition">📊 9. Resumen Cereal</button>
      <button onclick="setTab('retenciones')" id="tab-retenciones" class="tab-btn px-3 py-1.5 rounded-lg text-xs font-bold border border-gray-200 text-amber-600 bg-amber-50 hover:border-amber-400 transition">💰 10. Retenciones OSCE</button>
      
    </nav>
  </div>
</header>

<!-- ── MAIN ───────────────────────────────────────────────────────────────── -->
<main class="max-w-[1700px] mx-auto px-4 py-4 space-y-4">

<!-- ═══════════════════════════════════════════════════════════
     1. CEREAL
═══════════════════════════════════════════════════════════ -->
<section id="pane-cereal" class="tab-pane active">
  <div class="bg-white rounded-xl border border-gray-200 shadow-sm">
    <div class="flex items-center justify-between px-4 pt-4 pb-2 border-b border-gray-100 flex-wrap gap-2">
      <div>
        <h2 class="font-black text-gray-900 flex items-center gap-2">🥣 Cronograma de Entregas — Cereal PVL
          <span class="text-xs font-normal text-gray-400">({len(pendientes_data.get('cereal',[]))} pendientes)</span>
        </h2>
      </div>
      <div class="flex items-center gap-2">
        <input type="text" id="search-cereal-input" oninput="filterTablesText()" placeholder="🔍 Buscar municipalidad..." class="border border-gray-300 rounded-lg px-3 py-1.5 text-xs focus:outline-none focus:border-red-500 w-48">
        <button onclick="openNewOrderModal()" class="text-xs bg-green-600 hover:bg-green-700 text-white px-3 py-1.5 rounded-lg font-bold transition flex items-center gap-1 shadow-sm">➕ Ingresar Orden</button>
        <button onclick="setTab('formulas')" class="text-xs bg-red-50 hover:bg-red-100 text-red-600 border border-red-200 px-3 py-1.5 rounded-lg font-bold transition hidden sm:block">⚙️ Fórmulas</button>
      </div>
    </div>
    {month_filter('cereal')}
    <div class="overflow-x-auto">
      <table>
        <thead><tr>
          <th class="text-left">Municipalidad</th>
          <th class="text-left">Mes</th>
          <th class="text-left">Fecha Plazo</th>
          <th class="text-left">Prod.</th>
          <th class="text-left">Envasado</th>
          <th class="text-left">Despacho</th>
          <th class="text-right">N° Bolsas</th>
          <th class="text-right">Kg/Bolsa</th>
          <th class="text-right">Total (kg)</th>
          <th class="text-right">Cap. Saco</th>
          <th class="text-right">N° Sacos</th>
        </tr></thead>
        <tbody id="tbody-cereal">
          {cereal_rows()}
        </tbody>
      </table>
    </div>
    <div class="px-4 py-3 bg-gray-50 border-t border-gray-100 flex gap-4 text-xs text-gray-500">
      <span>Total pendiente: <strong class="text-red-600" id="sum-cereal-kg">—</strong> kg</span>
      <span>Filas visibles: <strong id="count-cereal">—</strong></span>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════════════════════════
     2. LECHE
═══════════════════════════════════════════════════════════ -->
<section id="pane-leche" class="tab-pane">
  <div class="bg-white rounded-xl border border-gray-200 shadow-sm">
    <div class="px-4 pt-4 pb-2 border-b border-gray-100">
      <h2 class="font-black text-gray-900">🥛 Cronograma de Entregas — Leche Evaporada Gloria (Caja ×48 latas)
        <span class="text-xs font-normal text-gray-400 ml-2">{len(pendientes_data.get('leche',[]))} pendientes</span>
      </h2>
      <p class="text-xs text-gray-400 mt-0.5">1 Caja = 48 latas de 410g • Faltan 579 cajas por adquirir según proyección</p>
    </div>
    {month_filter('leche')}
    <div class="overflow-x-auto">
      <table>
        <thead><tr>
          <th class="text-left">Municipalidad</th>
          <th class="text-left">Mes</th>
          <th class="text-left">Fecha Plazo</th>
          <th class="text-right">N° Latas</th>
          <th class="text-right">Cajas (÷48)</th>
          <th class="text-right">Latas Sueltas</th>
        </tr></thead>
        <tbody id="tbody-leche">
          {leche_rows()}
        </tbody>
      </table>
    </div>
    <div class="px-4 py-3 bg-gray-50 border-t border-gray-100 flex gap-4 text-xs text-gray-500">
      <span>Total latas pendientes: <strong class="text-blue-600" id="sum-leche-latas">—</strong></span>
      <span class="ml-4 text-red-500 font-bold">⚠️ Déficit estimado: 579 cajas (27,792 latas)</span>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════════════════════════
     3. PRODUCCIÓN
═══════════════════════════════════════════════════════════ -->
<section id="pane-produccion" class="tab-pane">
  <div class="bg-white rounded-xl border border-gray-200 shadow-sm p-4">
    <h2 class="font-black text-gray-900 mb-4">⚙️ Registro de Producción & Envasado (BOM)</h2>
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-4">
      <div class="border border-gray-200 rounded-xl p-4 space-y-3">
        <h3 class="font-bold text-sm text-gray-700">Nueva Orden de Producción</h3>
        <div>
          <label class="block text-xs font-semibold text-gray-500 mb-1">Municipalidad / Distrito</label>
          <select id="prod-distrito" onchange="calcProduccion()" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-red-400">
            {formulas_options()}
          </select>
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-gray-500 mb-1">Kg a Producir</label>
            <input type="number" id="prod-kg" value="1000" oninput="calcProduccion()"
              class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-red-400">
          </div>
          <div>
            <label class="block text-xs font-semibold text-gray-500 mb-1">Fecha Mezclado</label>
            <input type="date" id="prod-fecha" class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-red-400">
          </div>
        </div>
        <button onclick="registrarProduccion()" class="w-full bg-red-600 hover:bg-red-700 text-white font-bold py-2 rounded-lg text-sm transition">
          ✅ Registrar Lote de Producción
        </button>
      </div>
      <div class="border border-gray-200 rounded-xl p-4">
        <h3 class="font-bold text-sm text-gray-700 mb-3">Explosión de Materiales (BOM)</h3>
        <table>
          <thead><tr>
            <th class="text-left">Ingrediente</th>
            <th class="text-right">%</th>
            <th class="text-right font-bold text-red-600">Kg a Pesar</th>
          </tr></thead>
          <tbody id="bom-body"></tbody>
          <tfoot>
            <tr class="font-bold border-t-2 border-gray-300">
              <td class="px-3 py-2">TOTAL</td>
              <td class="px-3 py-2 text-right" id="bom-pct-total">100%</td>
              <td class="px-3 py-2 text-right text-red-700" id="bom-kg-total">1,000.00 kg</td>
            </tr>
          </tfoot>
        </table>
      </div>
    </div>
    <!-- Historial lotes producción -->
    <div class="mt-4 border border-gray-200 rounded-xl overflow-hidden">
      <div class="bg-gray-50 px-4 py-2 border-b border-gray-200 text-xs font-bold text-gray-600 uppercase">Lotes Recientes</div>
      <table>
        <thead><tr>
          <th class="text-left">Código Lote</th>
          <th class="text-left">Distrito</th>
          <th class="text-right">Kg Prog.</th>
          <th class="text-left">Fecha</th>
          <th class="text-center">Estado</th>
          <th class="text-left">F. Entrega</th>
        </tr></thead>
        <tbody>
          <tr class="hover:bg-gray-50"><td class="px-3 py-2 font-mono text-xs">LOT-C26-095</td><td class="px-3 py-2 text-xs">Huamachuco</td><td class="px-3 py-2 text-right text-xs">4,606.80</td><td class="px-3 py-2 text-xs">23/09/2026</td><td class="px-3 py-2 text-center"><span class="text-xs bg-amber-100 text-amber-700 px-2 py-0.5 rounded-full border border-amber-200 font-bold">Envasado</span></td></tr>
          <tr class="hover:bg-gray-50"><td class="px-3 py-2 font-mono text-xs">LOT-C26-094</td><td class="px-3 py-2 text-xs">Encañada</td><td class="px-3 py-2 text-right text-xs">21,001.68</td><td class="px-3 py-2 text-xs">20/09/2026</td><td class="px-3 py-2 text-center"><span class="text-xs bg-green-100 text-green-700 px-2 py-0.5 rounded-full border border-green-200 font-bold">Entregado</span></td></tr>
          <tr class="hover:bg-gray-50"><td class="px-3 py-2 font-mono text-xs">LOT-C26-093</td><td class="px-3 py-2 text-xs">Alto Trujillo</td><td class="px-3 py-2 text-right text-xs">2,968.56</td><td class="px-3 py-2 text-xs">30/09/2026</td><td class="px-3 py-2 text-center"><span class="text-xs bg-blue-100 text-blue-700 px-2 py-0.5 rounded-full border border-blue-200 font-bold">Listo Despacho</span></td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════════════════════════
     4. ENTRADAS & SALIDAS (KARDEX)
═══════════════════════════════════════════════════════════ -->
<section id="pane-entradas" class="tab-pane">
  <div class="bg-white rounded-xl border border-gray-200 shadow-sm">
    <div class="px-4 pt-4 pb-2 border-b border-gray-100 flex items-center justify-between">
      <div>
        <h2 class="font-black text-gray-900">📥 Entradas & Salidas — Kardex de Materias Primas</h2>
        <p class="text-xs text-gray-400 mt-0.5">Historial Jul / Ago / Sep 2026 + registro de nuevas entradas</p>
      </div>
      <div class="flex gap-2">
      <button onclick="openModalEntrada()" class="bg-red-600 hover:bg-red-700 text-white text-xs font-bold px-3 py-2 rounded-lg transition">📥 Nueva Entrada</button>
      <button onclick="openModalSalida()" class="bg-orange-500 hover:bg-orange-600 text-white text-xs font-bold px-3 py-2 rounded-lg transition">📤 Registrar Salida</button>
      </div>
    </div>
    <!-- Filtros -->
    <div class="flex flex-wrap gap-2 px-4 py-2 border-b border-gray-100">
      {month_filter('kardex')}
      <div class="flex items-center gap-2 ml-2">
        <label class="text-xs text-gray-500 font-semibold">Producto:</label>
        <select id="kardex-producto-filter" onchange="filterKardex()" class="border border-gray-300 rounded-lg px-2 py-1 text-xs focus:outline-none">
          <option value="">Todos</option>
          <option>Trigo</option><option>Avena</option><option>Quinua</option>
          <option>Maca</option><option>Azúcar</option><option>Maíz chufla</option>
          <option>Maíz Pollo</option><option>Kiwicha</option><option>Leche en Polvo</option>
          <option>Soya</option><option>Cocoa</option><option>Sacos</option>
          <option>Quinua Qaliwarma</option>
        </select>
      </div>
    </div>
    <div class="overflow-x-auto">
      <table>
        <thead><tr>
          <th class="text-left">Fecha</th>
          <th class="text-left">Producto</th>
          <th class="text-left">Código</th>
          <th class="text-right">Lote</th>
          <th class="text-right">Cantidad</th>
          <th class="text-right">U/M</th>
          <th class="text-left">Proveedor</th>
          <th class="text-left">Notas</th>
        </tr></thead>
        <tbody id="tbody-kardex">
        </tbody>
      </table>
    </div>
    <div class="px-4 py-3 bg-gray-50 border-t border-gray-100 text-xs text-gray-500">
      Registros visibles: <strong id="kardex-count">—</strong>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════════════════════════
     5. ALMACÉN & PROYECCIONES
═══════════════════════════════════════════════════════════ -->
<section id="pane-almacen" class="tab-pane">
  <div class="grid grid-cols-1 xl:grid-cols-3 gap-4">

    <!-- Column: Stock + Notas -->
    <div class="xl:col-span-2 space-y-4">
      <!-- Stock actual -->
      <div class="bg-white rounded-xl border border-gray-200 shadow-sm">
        <div class="px-4 pt-4 pb-2 border-b border-gray-100 flex items-center justify-between">
          <h2 class="font-black text-gray-900">📦 Stock Actual de Almacén</h2>
          <div class="flex gap-2">
          <button onclick="openModalStock()" class="text-xs bg-blue-50 hover:bg-blue-100 text-blue-700 border border-blue-300 px-3 py-1.5 rounded-lg font-bold transition">📦 Actualizar Stock</button>
          <button onclick="hitlApproveAll()" class="text-xs bg-amber-50 hover:bg-amber-100 text-amber-700 border border-amber-300 px-3 py-1.5 rounded-lg font-bold transition">🔐 Aprobar HITL</button>
          </div>
        </div>
        <div class="overflow-x-auto">
          <table>
            <thead><tr>
              <th class="text-left">Material</th>
              <th class="text-right">Stock Físico</th>
              <th class="text-right">Comprometido</th>
              <th class="text-right font-bold">Disponible</th>
              <th class="text-right">Stock Mín</th>
              <th class="text-center">Estado</th>
              <th class="text-left">Nota</th>
            </tr></thead>
            <tbody>
              <tr class="hover:bg-red-50"><td class="px-3 py-2 font-semibold text-xs">Trigo en Grano</td><td class="px-3 py-2 text-right font-mono text-xs">9,076 kg</td><td class="px-3 py-2 text-right font-mono text-xs text-amber-600">25,608 kg</td><td class="px-3 py-2 text-right font-mono text-xs font-bold text-red-600">-16,532 kg</td><td class="px-3 py-2 text-right font-mono text-xs">5,000 kg</td><td class="px-3 py-2 text-center"><span class="text-[10px] bg-red-100 text-red-700 px-2 py-0.5 rounded-full font-bold border border-red-200">DÉFICIT</span></td><td class="px-3 py-2 text-xs text-amber-600 font-semibold">Pedir 16 TN más</td></tr>
              <tr class="hover:bg-amber-50"><td class="px-3 py-2 font-semibold text-xs">Avena Perlada</td><td class="px-3 py-2 text-right font-mono text-xs">18,320 kg</td><td class="px-3 py-2 text-right font-mono text-xs text-amber-600">51,478 kg</td><td class="px-3 py-2 text-right font-mono text-xs font-bold text-red-600">-33,158 kg</td><td class="px-3 py-2 text-right font-mono text-xs">10,000 kg</td><td class="px-3 py-2 text-center"><span class="text-[10px] bg-red-100 text-red-700 px-2 py-0.5 rounded-full font-bold border border-red-200">DÉFICIT</span></td><td class="px-3 py-2 text-xs text-amber-600 font-semibold">Faltan 33 TN</td></tr>
              <tr class="hover:bg-gray-50"><td class="px-3 py-2 font-semibold text-xs">Quinua Perlada</td><td class="px-3 py-2 text-right font-mono text-xs">2,900 kg</td><td class="px-3 py-2 text-right font-mono text-xs">3,218 kg</td><td class="px-3 py-2 text-right font-mono text-xs font-bold text-amber-600">-318 kg</td><td class="px-3 py-2 text-right font-mono text-xs">1,000 kg</td><td class="px-3 py-2 text-center"><span class="text-[10px] bg-amber-100 text-amber-700 px-2 py-0.5 rounded-full font-bold border border-amber-200">ALERTA</span></td><td class="px-3 py-2 text-xs text-gray-400">—</td></tr>
              <tr class="hover:bg-gray-50"><td class="px-3 py-2 font-semibold text-xs">Maca Gelatinizada</td><td class="px-3 py-2 text-right font-mono text-xs">2,300 kg</td><td class="px-3 py-2 text-right font-mono text-xs">2,289 kg</td><td class="px-3 py-2 text-right font-mono text-xs font-bold text-green-600">11 kg</td><td class="px-3 py-2 text-right font-mono text-xs">500 kg</td><td class="px-3 py-2 text-center"><span class="text-[10px] bg-green-100 text-green-700 px-2 py-0.5 rounded-full font-bold border border-green-200">OK</span></td><td class="px-3 py-2 text-xs text-gray-400">Stock cubierto</td></tr>
              <tr class="hover:bg-gray-50"><td class="px-3 py-2 font-semibold text-xs">Azúcar Rubia</td><td class="px-3 py-2 text-right font-mono text-xs">5,200 kg</td><td class="px-3 py-2 text-right font-mono text-xs">5,160 kg</td><td class="px-3 py-2 text-right font-mono text-xs font-bold text-green-600">40 kg</td><td class="px-3 py-2 text-right font-mono text-xs">1,000 kg</td><td class="px-3 py-2 text-center"><span class="text-[10px] bg-amber-100 text-amber-700 px-2 py-0.5 rounded-full font-bold border border-amber-200">ALERTA</span></td><td class="px-3 py-2 text-xs text-gray-400">Sacos 50 kg</td></tr>
              <tr class="hover:bg-gray-50"><td class="px-3 py-2 font-semibold text-xs">Soya Desgrasada</td><td class="px-3 py-2 text-right font-mono text-xs">1,450 kg</td><td class="px-3 py-2 text-right font-mono text-xs">1,485 kg</td><td class="px-3 py-2 text-right font-mono text-xs font-bold text-amber-600">-35 kg</td><td class="px-3 py-2 text-right font-mono text-xs">500 kg</td><td class="px-3 py-2 text-center"><span class="text-[10px] bg-amber-100 text-amber-700 px-2 py-0.5 rounded-full font-bold border border-amber-200">ALERTA</span></td><td class="px-3 py-2 text-xs text-gray-400">Comp. programar</td></tr>
              <tr class="hover:bg-blue-50"><td class="px-3 py-2 font-semibold text-xs">Leche Evaporada (latas)</td><td class="px-3 py-2 text-right font-mono text-xs">123,680</td><td class="px-3 py-2 text-right font-mono text-xs">151,506</td><td class="px-3 py-2 text-right font-mono text-xs font-bold text-red-600">-27,826</td><td class="px-3 py-2 text-right font-mono text-xs">10,000</td><td class="px-3 py-2 text-center"><span class="text-[10px] bg-red-100 text-red-700 px-2 py-0.5 rounded-full font-bold border border-red-200">DÉFICIT</span></td><td class="px-3 py-2 text-xs text-amber-600 font-semibold">Faltan 55 cajas+</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Notas de Proyección (Sticky Notes) -->
      <div class="bg-white rounded-xl border border-gray-200 shadow-sm p-4">
        <div class="flex items-center justify-between mb-3">
          <h3 class="font-black text-gray-900">📌 Notas de Proyección & Almacén</h3>
          <button onclick="addNote()" class="text-xs bg-yellow-50 hover:bg-yellow-100 text-yellow-700 border border-yellow-300 px-3 py-1.5 rounded-lg font-bold transition">+ Agregar Nota</button>
        </div>
        <div id="notes-grid" class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
          <!-- Notes rendered by JS from localStorage -->
        </div>
      </div>
    </div>

    <!-- Column: Requerimientos -->
    <div class="space-y-4">
      <div class="bg-white rounded-xl border border-gray-200 shadow-sm p-4">
        <div class="flex items-center justify-between mb-3">
          <h3 class="font-black text-gray-900 text-sm">📋 Requerimientos de Compra</h3>
          <span class="text-xs bg-gray-100 text-gray-500 px-2 py-0.5 rounded font-mono">000236 · 000237</span>
        </div>
        {req_cards_html}
      </div>

      <!-- Proyección Leche -->
      <div class="bg-white rounded-xl border border-gray-200 shadow-sm p-4">
        <h3 class="font-bold text-sm text-gray-900 mb-2">🥛 Balance Leche (Proyección)</h3>
        <div class="space-y-2 text-xs">
          <div class="flex justify-between py-1.5 border-b border-gray-100">
            <span class="text-gray-600">Stock en almacén</span>
            <span class="font-mono font-bold">123,680 latas (2,577 cajas)</span>
          </div>
          <div class="flex justify-between py-1.5 border-b border-gray-100">
            <span class="text-gray-600">Demanda pendiente total</span>
            <span class="font-mono font-bold text-red-600">151,506 latas (3,156 cajas)</span>
          </div>
          <div class="flex justify-between py-1.5 border-b border-gray-100 font-bold text-red-700">
            <span>DÉFICIT</span>
            <span class="font-mono">27,826 latas (579 cajas)</span>
          </div>
          <div class="flex justify-between py-1.5">
            <span class="text-gray-600">Costo estimado compra</span>
            <span class="font-mono font-bold text-amber-600">S/. 107,133 (a S/. 3.85/lata)</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════════════════════════
     6. FÓRMULAS (Editor completo 161 distritos)
═══════════════════════════════════════════════════════════ -->
<section id="pane-formulas" class="tab-pane">
  <div class="grid grid-cols-1 xl:grid-cols-5 gap-4">

    <!-- Lista de distritos -->
    <div class="xl:col-span-2 bg-white rounded-xl border border-gray-200 shadow-sm">
      <div class="px-4 pt-4 pb-3 border-b border-gray-100">
        <h2 class="font-black text-gray-900 mb-2">📐 Fórmulas PVL — 161 Distritos</h2>
        <input type="text" id="formula-search" oninput="filterFormulaList()" placeholder="🔍 Buscar distrito..."
          class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-red-400">
      </div>
      <div class="overflow-y-auto max-h-[65vh]" id="formula-list">
        <!-- Populated by JS -->
      </div>
      <div class="px-4 py-3 border-t border-gray-100 flex items-center justify-between">
        <span class="text-xs text-gray-400" id="formula-count-label">161 fórmulas</span>
        <button onclick="newDistritoFormula()" class="text-xs bg-red-600 hover:bg-red-700 text-white px-3 py-1.5 rounded-lg font-bold transition">+ Nuevo Distrito</button>
      </div>
    </div>

    <!-- Editor de fórmula seleccionada -->
    <div class="xl:col-span-3 bg-white rounded-xl border border-gray-200 shadow-sm">
      <div class="px-4 pt-4 pb-3 border-b border-gray-100 flex items-center justify-between">
        <div>
          <h3 class="font-black text-gray-900" id="formula-edit-title">Seleccione un distrito</h3>
          <p class="text-xs text-gray-400 mt-0.5">Edite los porcentajes — deben sumar 100%</p>
        </div>
        <div class="flex gap-2">
          <button onclick="deleteFormulaDistrict()" id="btn-delete-formula" class="hidden text-xs bg-red-50 hover:bg-red-100 text-red-600 border border-red-200 px-3 py-1.5 rounded-lg font-bold transition">🗑️ Eliminar</button>
          <button onclick="saveFormula()" id="btn-save-formula" class="hidden text-xs bg-red-600 hover:bg-red-700 text-white px-3 py-1.5 rounded-lg font-bold transition">💾 Guardar Cambios</button>
        </div>
      </div>

      <div id="formula-editor-empty" class="flex flex-col items-center justify-center py-16 text-gray-300">
        <span class="text-5xl mb-3">📐</span>
        <p class="text-sm font-semibold">Selecciona un distrito de la lista para editar su fórmula</p>
        <p class="text-xs text-gray-400 mt-1">O crea un nuevo distrito con el botón "Nuevo Distrito"</p>
      </div>

      <div id="formula-editor-form" class="hidden p-4 space-y-4">
        <div>
          <label class="block text-xs font-semibold text-gray-500 mb-1">Nombre del Distrito</label>
          <input type="text" id="fe-distrito-name"
            class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-red-400 font-semibold">
        </div>

        <div class="grid grid-cols-2 gap-3" id="formula-inputs-grid">
          <!-- Inputs for each ingredient -->
        </div>

        <!-- Total indicator -->
        <div class="bg-gray-50 border border-gray-200 rounded-xl p-3 flex items-center justify-between">
          <span class="text-sm font-bold text-gray-700">Total Fórmula:</span>
          <div class="flex items-center gap-3">
            <div class="w-40 bg-gray-200 rounded-full h-2">
              <div id="formula-pct-bar" class="bg-red-500 h-2 rounded-full transition-all" style="width:0%"></div>
            </div>
            <span class="font-black text-lg font-mono" id="formula-total-pct">0.00%</span>
          </div>
        </div>

        <!-- Calculadora rápida integrada -->
        <div class="border border-gray-200 rounded-xl p-4">
          <h4 class="font-bold text-sm text-gray-700 mb-2">🧪 Calculadora de Bache (vista previa)</h4>
          <div class="flex items-center gap-3 mb-3">
            <input type="number" id="fe-bache-kg" value="400" oninput="previewBache()"
              class="w-32 border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-red-400">
            <span class="text-xs text-gray-500 font-semibold">kg de bache</span>
          </div>
          <table class="text-xs w-full">
            <thead><tr>
              <th class="text-left text-gray-400 py-1">Ingrediente</th>
              <th class="text-right text-gray-400 py-1">%</th>
              <th class="text-right text-red-600 font-bold py-1">Kg a Pesar</th>
            </tr></thead>
            <tbody id="bache-preview-tbody"></tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════════════════════════
     7. PENDIENTES
═══════════════════════════════════════════════════════════ -->
<section id="pane-pendientes" class="tab-pane">
  <!-- Cereal -->
  <div class="bg-white rounded-xl border border-gray-200 shadow-sm mb-4">
    <div class="px-4 pt-4 pb-2 border-b border-gray-100">
      <h2 class="font-black text-gray-900">📋 Pendientes de Entrega — Cereal</h2>
    </div>
    {month_filter('pend-cereal')}
    <div class="overflow-x-auto">
      <table>
        <thead><tr>
          <th class="text-left">Municipalidad</th>
          <th class="text-left">Mes</th>
          <th class="text-left">Fecha Plazo</th>
          <th class="text-right">Bolsas</th>
          <th class="text-right">Kg/Bolsa</th>
          <th class="text-right">Total (kg)</th>
          <th class="text-right">N° Sacos</th>
          <th class="text-right">Unid.</th>
        </tr></thead>
        <tbody id="tbody-pend-cereal">
          {pendientes_cereal_rows()}
        </tbody>
      </table>
    </div>
  </div>
  <!-- Leche -->
  <div class="bg-white rounded-xl border border-gray-200 shadow-sm">
    <div class="px-4 pt-4 pb-2 border-b border-gray-100">
      <h2 class="font-black text-gray-900">📋 Pendientes de Entrega — Leche</h2>
      <p class="text-xs text-red-500 font-bold mt-0.5">⚠️ Déficit: 579 cajas (~27,826 latas) por adquirir</p>
    </div>
    {month_filter('pend-leche')}
    <div class="overflow-x-auto">
      <table>
        <thead><tr>
          <th class="text-left">Municipalidad</th>
          <th class="text-left">Mes</th>
          <th class="text-left">Fecha Plazo</th>
          <th class="text-right">Latas</th>
          <th class="text-right">Cajas</th>
          <th class="text-right">Latas Sueltas</th>
        </tr></thead>
        <tbody id="tbody-pend-leche">
          {leche_rows()}
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════════════════════════
     8. ENTREGADO
═══════════════════════════════════════════════════════════ -->
<section id="pane-entregado" class="tab-pane">
  <!-- Cereal Entregado -->
  <div class="bg-white rounded-xl border border-gray-200 shadow-sm mb-4">
    <div class="px-4 pt-4 pb-2 border-b border-gray-100">
      <h2 class="font-black text-gray-900">✅ Historial Entregas — Cereal ({len(entregado_data.get('cereal',[]))} registros)</h2>
    </div>
    {month_filter('ent-cereal')}
    <div class="overflow-x-auto">
      <table>
        <thead><tr>
          <th class="text-left">Municipalidad</th>
          <th class="text-left">Mes</th>
          <th class="text-left">Fecha O.C.</th>
          <th class="text-right">Bolsas</th>
          <th class="text-right">Kg/Bolsa</th>
          <th class="text-right">Total (kg)</th>
          <th class="text-right">N° Sacos</th>
          <th class="text-left">Fecha Entrega</th>
        </tr></thead>
        <tbody id="tbody-ent-cereal">
          {entregado_cereal_rows()}
        </tbody>
      </table>
    </div>
  </div>
  <!-- Leche Entregada -->
  <div class="bg-white rounded-xl border border-gray-200 shadow-sm">
    <div class="px-4 pt-4 pb-2 border-b border-gray-100">
      <h2 class="font-black text-gray-900">✅ Historial Entregas — Leche ({len(entregado_data.get('leche',[]))} registros)</h2>
    </div>
    {month_filter('ent-leche')}
    <div class="overflow-x-auto">
      <table>
        <thead><tr>
          <th class="text-left">Municipalidad</th>
          <th class="text-left">Mes</th>
          <th class="text-left">Fecha O.C.</th>
          <th class="text-right">Latas</th>
          <th class="text-right">Cajas</th>
          <th class="text-left">Fecha Entrega</th>
        </tr></thead>
        <tbody id="tbody-ent-leche">
          {entregado_leche_rows()}
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════════════════════════
     9. RESUMEN CEREAL
═══════════════════════════════════════════════════════════ -->
<section id="pane-resumen" class="tab-pane">
  <div class="bg-white rounded-xl border border-gray-200 shadow-sm">
    <div class="px-4 pt-4 pb-2 border-b border-gray-100 flex items-center justify-between">
      <div>
        <h2 class="font-black text-gray-900">📊 Resumen Cereal — Consumo de Insumos por Entrega</h2>
        <p class="text-xs text-gray-400 mt-0.5">Totales Sep: Trigo 49.4 TN · Avena 160.7 TN · Quinua 9.9 TN · Soya 4.6 TN · Maca 7.1 TN · Azúcar 16.0 TN</p>
      </div>
    </div>
    {month_filter('resumen')}
    <div class="overflow-x-auto">
      <table>
        <thead><tr>
          <th class="text-left">Municipalidad</th>
          <th class="text-left">Mes</th>
          <th class="text-left">Fecha</th>
          <th class="text-right font-bold text-red-600">Total (kg)</th>
          <th class="text-right">Trigo</th>
          <th class="text-right">Avena</th>
          <th class="text-right">Quinua</th>
          <th class="text-right">Soya</th>
          <th class="text-right">Maca</th>
          <th class="text-right">Azúcar</th>
        </tr></thead>
        <tbody id="tbody-resumen">
          {resumen_rows()}
        </tbody>
        <tfoot class="bg-red-50 font-bold border-t-2 border-red-200">
          <tr>
            <td colspan="3" class="px-3 py-2 text-xs">TOTALES ACUMULADOS (Sep 2026)</td>
            <td class="px-3 py-2 text-right text-xs text-red-700">—</td>
            <td class="px-3 py-2 text-right text-xs">49,400</td>
            <td class="px-3 py-2 text-right text-xs">160,700</td>
            <td class="px-3 py-2 text-right text-xs">9,900</td>
            <td class="px-3 py-2 text-right text-xs">4,600</td>
            <td class="px-3 py-2 text-right text-xs">7,100</td>
            <td class="px-3 py-2 text-right text-xs">16,000</td>
          </tr>
        </tfoot>
      </table>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════════════════════════
     10. RETENCIONES OSCE
═══════════════════════════════════════════════════════════ -->
<section id="pane-retenciones" class="tab-pane">
  <div class="grid grid-cols-1 xl:grid-cols-2 gap-4">
    <!-- Calculadora -->
    <div class="bg-white rounded-xl border border-gray-200 shadow-sm p-4">
      <h2 class="font-black text-gray-900 mb-1">💰 Calculadora Retenciones (Garantía Fiel Cumplimiento 10%)</h2>
      <p class="text-xs text-gray-400 mb-3">Art. 139 y 149 RLCE: Exonerado si monto ≤ 50 UIT (S/. 257,500)</p>

      <!-- Presets -->
      <div class="mb-3">
        <div class="text-xs font-bold text-gray-500 uppercase mb-1.5">Cargar contrato de ejemplo:</div>
        <div class="flex flex-wrap gap-1.5">
          <button onclick="setRetencionPreset('jmq')" class="px-2.5 py-1 rounded-lg text-xs bg-red-50 border border-red-200 text-red-700 font-bold hover:bg-red-100 transition">
            📜 JMQ (S/. 127k — Exonerado)
          </button>
          <button onclick="setRetencionPreset('huamachuco')" class="px-2.5 py-1 rounded-lg text-xs bg-gray-100 border border-gray-200 text-gray-700 font-semibold hover:bg-gray-200 transition">
            🏛️ Huamachuco (S/. 340k)
          </button>
          <button onclick="setRetencionPreset('encaanada')" class="px-2.5 py-1 rounded-lg text-xs bg-gray-100 border border-gray-200 text-gray-700 font-semibold hover:bg-gray-200 transition">
            🏛️ Encañada (S/. 280k)
          </button>
        </div>
      </div>

      <div class="space-y-3">
        <div>
          <label class="block text-xs font-semibold text-gray-600 mb-1">Monto Total Contrato (S/.)</label>
          <input type="number" id="retMontoInput" value="240000" step="1000" oninput="runRetencionCalc()"
            class="w-full border border-gray-300 rounded-xl px-3 py-2 text-sm font-mono font-bold focus:outline-none focus:border-red-400">
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-xs font-semibold text-gray-600 mb-1">N° Entregas</label>
            <input type="number" id="retEntregasInput" value="4" min="1" max="12" oninput="runRetencionCalc()"
              class="w-full border border-gray-300 rounded-xl px-3 py-2 text-sm focus:outline-none focus:border-red-400">
          </div>
          <div>
            <label class="block text-xs font-semibold text-gray-600 mb-1">Modalidad Garantía</label>
            <select id="retModoSelect" onchange="runRetencionCalc()"
              class="w-full border border-gray-300 rounded-xl px-3 py-2 text-sm focus:outline-none focus:border-red-400">
              <option value="10">Retención 10% MYPE</option>
              <option value="0">Carta Fianza / Exonerado</option>
            </select>
          </div>
        </div>
        <!-- Resultados -->
        <div class="bg-gray-50 border border-gray-200 rounded-xl p-3 space-y-2 text-sm font-mono">
          <div class="flex justify-between">
            <span class="text-gray-500 text-xs">Retención Total (10%):</span>
            <strong class="text-amber-600" id="resRetTotal">S/. 24,000.00</strong>
          </div>
          <div class="flex justify-between">
            <span class="text-gray-500 text-xs">Bruto por Entrega:</span>
            <span class="text-gray-800" id="resMontoBruto">S/. 60,000.00</span>
          </div>
          <div class="flex justify-between">
            <span class="text-gray-500 text-xs">Descuento/Entrega:</span>
            <span class="text-red-600 font-bold" id="resRetPorEntrega">-S/. 6,000.00</span>
          </div>
          <div class="flex justify-between pt-1 border-t border-gray-300">
            <span class="text-gray-800 font-bold font-sans text-xs">Neto a Cobrar:</span>
            <strong class="text-green-600 text-base" id="resMontoNeto">S/. 54,000.00</strong>
          </div>
        </div>
        <div id="retLegalWarning" class="p-3 rounded-xl text-xs leading-relaxed bg-amber-50 border border-amber-200 text-amber-800">
          <strong>Base Normativa:</strong> Contrato mayor a S/. 200,000. Retención 10% hasta Conformidad Final Diciembre.
        </div>
      </div>
    </div>

    <!-- Cartera de contratos -->
    <div class="bg-white rounded-xl border border-gray-200 shadow-sm p-4">
      <div class="flex items-center justify-between mb-3">
        <h3 class="font-black text-gray-900 text-sm">📁 Cartera de Retenciones Facoimpec</h3>
        <span class="text-xs font-bold text-amber-600 font-mono">Por Recuperar: S/. 62,000</span>
      </div>
      <div class="overflow-x-auto">
        <table>
          <thead><tr>
            <th class="text-left">Contrato / Entidad</th>
            <th class="text-right">Monto</th>
            <th class="text-center">Garantía</th>
            <th class="text-right">Retenido</th>
            <th class="text-right">Cobrado</th>
            <th class="text-center">Liberación</th>
          </tr></thead>
          <tbody>
            <tr class="hover:bg-red-50 bg-red-50/50">
              <td class="px-3 py-2 text-xs font-semibold">📜 MD José Manuel Quiroz (001-2026)</td>
              <td class="px-3 py-2 text-right text-xs font-mono">S/. 127,657</td>
              <td class="px-3 py-2 text-center"><span class="text-[10px] bg-green-100 text-green-700 border border-green-200 px-2 py-0.5 rounded-full font-bold">Exonerado</span></td>
              <td class="px-3 py-2 text-right text-xs font-mono text-green-600 font-bold">S/. 0</td>
              <td class="px-3 py-2 text-right text-xs font-mono text-green-600">100% Mensual</td>
              <td class="px-3 py-2 text-center text-xs text-gray-400">—</td>
            </tr>
            <tr class="hover:bg-gray-50">
              <td class="px-3 py-2 text-xs font-semibold">La Encañada (Licitación PVL)</td>
              <td class="px-3 py-2 text-right text-xs font-mono">S/. 280,000</td>
              <td class="px-3 py-2 text-center"><span class="text-[10px] bg-amber-100 text-amber-700 border border-amber-200 px-2 py-0.5 rounded-full font-bold">10% MYPE</span></td>
              <td class="px-3 py-2 text-right text-xs font-mono text-amber-600 font-bold">S/. 28,000</td>
              <td class="px-3 py-2 text-right text-xs font-mono text-green-600">S/. 21,000</td>
              <td class="px-3 py-2 text-center text-xs text-gray-500">Dic 2026</td>
            </tr>
            <tr class="hover:bg-gray-50">
              <td class="px-3 py-2 text-xs font-semibold">Huamachuco (Adquisición PVL)</td>
              <td class="px-3 py-2 text-right text-xs font-mono">S/. 340,000</td>
              <td class="px-3 py-2 text-center"><span class="text-[10px] bg-amber-100 text-amber-700 border border-amber-200 px-2 py-0.5 rounded-full font-bold">10% MYPE</span></td>
              <td class="px-3 py-2 text-right text-xs font-mono text-amber-600 font-bold">S/. 34,000</td>
              <td class="px-3 py-2 text-right text-xs font-mono text-green-600">S/. 30,600</td>
              <td class="px-3 py-2 text-center text-xs text-gray-500">Dic 2026</td>
            </tr>
            <tr class="hover:bg-gray-50">
              <td class="px-3 py-2 text-xs font-semibold">O.C. 089 El Ingenio</td>
              <td class="px-3 py-2 text-right text-xs font-mono">S/. 22,450</td>
              <td class="px-3 py-2 text-center"><span class="text-[10px] bg-green-100 text-green-700 border border-green-200 px-2 py-0.5 rounded-full font-bold">Exonerado</span></td>
              <td class="px-3 py-2 text-right text-xs font-mono text-green-600 font-bold">S/. 0</td>
              <td class="px-3 py-2 text-right text-xs font-mono text-green-600">100%</td>
              <td class="px-3 py-2 text-center text-xs text-gray-400">—</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════════════════════════════════════════════════════
     WHATSAPP ASISTENTE (HITL + Voz)
═══════════════════════════════════════════════════════════ -->

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

</main>


<!-- ══════════════════════════════════════════════════════════
     WHATSAPP FLOATING WIDGET
══════════════════════════════════════════════════════════ -->
<div id="wa-floating-btn" onclick="toggleWaWidget()" class="fixed bottom-6 right-6 w-14 h-14 bg-green-500 rounded-full flex items-center justify-center shadow-2xl cursor-pointer hover:bg-green-600 transition hover:scale-105 z-40 border-2 border-white">
  <span class="text-3xl text-white">💬</span>
  <div class="absolute -top-1 -right-1 bg-red-500 text-white text-[10px] font-bold w-5 h-5 flex items-center justify-center rounded-full border border-white animate-bounce">1</div>
</div>

<div id="wa-widget-panel" class="fixed bottom-24 right-6 w-96 bg-white rounded-2xl shadow-2xl z-50 flex flex-col hidden border border-gray-200 overflow-hidden transition-all duration-300 transform translate-y-4 opacity-0">
  
  <!-- WA header -->
  <div class="bg-gray-900 flex items-center gap-3 p-3">
    <div class="w-8 h-8 rounded-full bg-white overflow-hidden flex-shrink-0 p-0.5">
      <img src="data:image/png;base64,{logo_b64}" class="w-full h-full object-contain">
    </div>
    <div>
      <div class="font-bold text-white text-sm">Bot FACOIMPEC</div>
      <div class="text-[10px] text-green-400">● en línea</div>
    </div>
    <button onclick="toggleWaWidget()" class="ml-auto text-gray-400 hover:text-white">✕</button>
  </div>

  <!-- WA chat area -->
  <div class="wa-bg px-3 py-3 overflow-y-auto flex-1" style="height:350px;" id="wa-chat">
    <div class="wa-bubble-bot">
      👋 ¡Hola! Soy el asistente de FACOIMPEC.<br>
      Puedo registrar <strong>entregas, salidas, arribos y plazos</strong> directamente en el sistema.<br><br>
      Dime qué ocurrió o manda un audio 🎤
      <div class="wa-time">09:00</div>
    </div>
  </div>

  <!-- Quick actions -->
  <div class="bg-gray-100 px-2 py-2 flex gap-1.5 flex-wrap border-t border-gray-200">
    <button onclick="waQuickAction('camion')" class="text-[10px] bg-white border border-gray-300 text-gray-700 px-2 py-1 rounded-full font-semibold hover:bg-gray-50">🚛 Llegó</button>
    <button onclick="waQuickAction('envasado')" class="text-[10px] bg-white border border-gray-300 text-gray-700 px-2 py-1 rounded-full font-semibold hover:bg-gray-50">📦 Envasado</button>
    <button onclick="waQuickAction('despacho')" class="text-[10px] bg-white border border-gray-300 text-gray-700 px-2 py-1 rounded-full font-semibold hover:bg-gray-50">🚚 Despacho</button>
    <button onclick="waQuickAction('entrega')" class="text-[10px] bg-white border border-gray-300 text-gray-700 px-2 py-1 rounded-full font-semibold hover:bg-gray-50">✅ Entregado</button>
  </div>

  <!-- WA Input bar + Voz -->
  <div class="bg-white px-3 py-2 flex items-center gap-2 border-t border-gray-200">
    <input type="text" id="wa-input" placeholder="Escribe un mensaje..." onkeydown="if(event.key==='Enter')waSend()"
      class="flex-1 bg-gray-100 border-none rounded-full px-4 py-2 text-sm text-gray-800 placeholder-gray-500 focus:outline-none focus:ring-2 focus:ring-green-500">
    <button onclick="waVoice()" id="wa-voice-btn" title="Mensaje de voz"
      class="w-9 h-9 bg-red-600 hover:bg-red-700 rounded-full flex items-center justify-center text-white text-lg transition shadow-sm">
      🎤
    </button>
    <button onclick="waSend()"
      class="w-9 h-9 bg-green-600 hover:bg-green-700 rounded-full flex items-center justify-center text-white text-lg transition">
      ▶
    </button>
  </div>
</div>


<!-- ══════════════════════════════════════════════════════════
     MODALS: PDF Import
══════════════════════════════════════════════════════════ -->
<div id="modalPdfUpload" class="fixed inset-0 z-50 bg-black/40 hidden items-center justify-center">
  <div class="bg-white rounded-2xl shadow-2xl w-full max-w-md mx-4 p-6">
    <div class="flex items-center justify-between mb-4">
      <h3 class="font-black text-gray-900">📄 Importar Orden de Compra / Contrato</h3>
      <button onclick="closePdfModal()" class="text-gray-400 hover:text-gray-700 text-xl">✕</button>
    </div>
    <div class="border-2 border-dashed border-gray-300 hover:border-red-400 rounded-xl p-6 text-center cursor-pointer transition mb-4" onclick="document.getElementById('pdfFileInput').click()">
      <div class="text-3xl mb-2">📥</div>
      <div class="text-sm font-bold text-gray-700">Haz clic para seleccionar el PDF</div>
      <div class="text-xs text-gray-400 mt-1">Soporta SIAF, Contratos PVL y O.C. SEACE</div>
      <input type="file" id="pdfFileInput" accept=".pdf" class="hidden" onchange="handlePdfUpload(event)">
    </div>
    <div class="text-xs font-bold text-gray-400 uppercase mb-2">O elige un ejemplo:</div>
    <div class="space-y-2">
      <button onclick="simulatePdfParse('jmq')" class="w-full text-left p-3 bg-red-50 hover:bg-red-100 border border-red-200 rounded-xl transition">
        <div class="flex items-center justify-between">
          <span class="font-bold text-red-800 text-sm">📜 Contrato 001-2026 José Manuel Quiroz</span>
          <span class="text-xs font-mono text-red-600">S/. 127,657</span>
        </div>
        <div class="text-xs text-gray-500 mt-0.5">12 entregas · 13,680 latas + 9,914 kg cereal · 0% Retención</div>
      </button>
      <button onclick="simulatePdfParse('ingenio')" class="w-full text-left p-3 bg-gray-50 hover:bg-gray-100 border border-gray-200 rounded-xl transition">
        <span class="font-bold text-gray-800 text-sm">O.C. 089 El Ingenio</span>
        <span class="text-xs text-gray-400 ml-2">280 kg cereal + 1,610 latas</span>
      </button>
      <button onclick="simulatePdfParse('huamachuco')" class="w-full text-left p-3 bg-gray-50 hover:bg-gray-100 border border-gray-200 rounded-xl transition">
        <span class="font-bold text-gray-800 text-sm">O.C. 802/803 Huamachuco</span>
        <span class="text-xs text-gray-400 ml-2">4,606.8 kg cereal + 10,470 latas</span>
      </button>
    </div>
    <div id="pdfResult" class="hidden mt-4 p-3 bg-green-50 border border-green-200 rounded-xl text-xs">
      <div class="font-bold text-green-700 mb-1" id="pdfResultTitle">✓ Documento Analizado</div>
      <div class="grid grid-cols-2 gap-1 text-gray-700">
        <div>Entidad: <strong id="pdfResMun"></strong></div>
        <div>Ref.: <strong id="pdfResNum"></strong></div>
        <div>Cereal: <strong id="pdfResCereal"></strong></div>
        <div>Leche: <strong id="pdfResLeche"></strong></div>
      </div>
      <div id="pdfResExtra" class="hidden mt-2 text-amber-700 bg-amber-50 border border-amber-200 rounded-lg p-2"></div>
      <button onclick="commitParsedPdf()" class="mt-2 w-full bg-green-600 hover:bg-green-700 text-white py-1.5 rounded-lg font-bold text-xs transition">
        ➕ Incorporar a facoimpec.db
      </button>
    </div>
    <div class="mt-4 flex justify-end">
      <button onclick="closePdfModal()" class="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-700 rounded-lg text-sm font-bold transition">Cerrar</button>
    </div>
  </div>
</div>

<!-- ══════════════════════════════════════════════════════════
     VOICE RECORDING OVERLAY
══════════════════════════════════════════════════════════ -->
<div id="voiceOverlay" class="fixed inset-0 z-50 bg-black/70 hidden items-center justify-center">
  <div class="bg-gray-900 rounded-2xl p-8 text-center shadow-2xl max-w-xs mx-4">
    <div class="rec-dot mx-auto mb-3"></div>
    <div class="text-white font-bold text-lg mb-1" id="voiceStatus">Grabando...</div>
    <div class="text-gray-400 text-xs">Habla claro — el sistema captará la información</div>
    <div class="mt-4 text-xs text-gray-500">* Simulación de transcripción de audio</div>
    <button onclick="stopVoice()" class="mt-4 bg-red-600 hover:bg-red-700 text-white px-6 py-2 rounded-xl font-bold transition">⏹ Detener</button>
  </div>
</div>

<!-- ══════════════════════════════════════════════════════════
     JAVASCRIPT
══════════════════════════════════════════════════════════ -->
<script>
// ── DATA ────────────────────────────────────────────────────
const formulasDB  = {formulas_json};
const kardexDB    = {KARDEX_JSON};
const requerimientosDB = {REQ_JSON};

// LocalStorage notes
const NOTE_KEY = 'facoimpec_notes_v2';
let notes = JSON.parse(localStorage.getItem(NOTE_KEY) || 'null') || [
  {{id: Date.now()+1, text: "Pedir 16 TN de Trigo más a Molino San José"}},
  {{id: Date.now()+2, text: "Faltan 579 cajas de leche (27,826 latas)"}},
  {{id: Date.now()+3, text: "Faltan llegar 55 sacos vacíos para Encañada"}},
  {{id: Date.now()+4, text: "Avena lote 29: 6 TN en devolución al proveedor"}}
];;

function saveNotes() {{ localStorage.setItem(NOTE_KEY, JSON.stringify(notes)); }}

function renderNotes() {{
  const g = document.getElementById('notes-grid');
  if (!g) return;
  g.innerHTML = '';
  notes.forEach(n => {{
    const d = document.createElement('div');
    d.className = 'sticky-note';
    d.innerHTML = `<div class="note-label">📌 Nota</div>
      <textarea onblur="updateNote(${{n.id}}, this.value)">${{n.text}}</textarea>
      <button onclick="deleteNote(${{n.id}})" style="position:absolute;top:6px;right:8px;font-size:11px;color:#f57f17;background:transparent;border:none;cursor:pointer;">✕</button>`;
    d.style.position = 'relative';
    g.appendChild(d);
  }});
}}

function addNote() {{
  notes.push({{id: Date.now(), text: "Nueva nota..."}});
  saveNotes(); renderNotes();
}}
function updateNote(id, text) {{
  const n = notes.find(x => x.id === id);
  if (n) {{ n.text = text; saveNotes(); }}
}}
function deleteNote(id) {{
  notes = notes.filter(x => x.id !== id);
  saveNotes(); renderNotes();
}}

// ── TAB SYSTEM ──────────────────────────────────────────────
function setTab(name) {{
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  const pane = document.getElementById('pane-' + name);
  const btn  = document.getElementById('tab-' + name);
  if (pane) pane.classList.add('active');
  if (btn)  btn.classList.add('active');
  if (name === 'almacen') renderNotes();
  if (name === 'formulas') renderFormulaList();
  if (name === 'entradas') renderKardex();
  if (name === 'produccion') calcProduccion();
}}

// ── MONTH FILTER ────────────────────────────────────────────

// ── NEW: DYNAMIC FILTERS & DATE EDITS ───────────────────────────
let currentMonthFilter = 'Todos';

function filterMonth(filterId, btn, mes) {{
  currentMonthFilter = mes;
  const container = document.getElementById('mf-' + filterId);
  if (container) {{
    container.querySelectorAll('.month-pill').forEach(p => {{
      p.style.background = '';
      p.style.color = '';
      p.style.borderColor = '';
    }});
    btn.style.background = '#DC1B24';
    btn.style.color = '#fff';
    btn.style.borderColor = '#DC1B24';
  }}
  applyTableFilters(filterId);
}}

function filterTablesText() {{
  applyTableFilters('cereal');
}}

function applyTableFilters(filterId) {{
  const searchInput = document.getElementById('search-cereal-input');
  const searchText = searchInput ? searchInput.value.toLowerCase() : '';
  
  const tbodies = document.querySelectorAll('[id*="' + filterId + '"]');
  tbodies.forEach(tb => {{
    if (!tb.tagName || tb.tagName !== 'TBODY') return;
    let shown = 0, kgSum = 0, lataSum = 0;
    
    tb.querySelectorAll('tr.trow').forEach(row => {{
      const rowMes = row.getAttribute('data-mes') || '';
      const rowMun = row.getAttribute('data-mun') || (row.children[0] ? row.children[0].textContent.toLowerCase() : '');
      
      const matchMonth = (currentMonthFilter === 'Todos') || rowMes.toLowerCase().includes(currentMonthFilter.toLowerCase());
      const matchText = !searchText || rowMun.includes(searchText);
      
      const show = matchMonth && matchText;
      row.style.display = show ? '' : 'none';
      
      if (show) {{
        shown++;
        const kgCell = row.querySelector('td:nth-child(9)'); 
        const laCell = row.querySelector('td:nth-child(4)');
        if (kgCell && tb.id.includes('cereal')) kgSum += parseFloat(kgCell.textContent.replace(/[^0-9.]/g,'')) || 0;
        if (laCell && tb.id.includes('leche')) lataSum += parseFloat(laCell.textContent.replace(/[^0-9.]/g,'')) || 0;
      }}
    }});

    const countEl = document.getElementById('count-' + filterId);
    const kgEl    = document.getElementById('sum-' + filterId + '-kg');
    const lataEl  = document.getElementById('sum-' + filterId + '-latas');
    if (countEl) countEl.textContent = shown;
    if (kgEl)   kgEl.textContent = kgSum.toLocaleString('es-PE',{{minimumFractionDigits:2}}) + ' kg';
    if (lataEl) lataEl.textContent = lataSum.toLocaleString('es-PE') + ' latas';
  }});
}}

function markDateSaved(input) {{
  input.style.backgroundColor = '#ecfdf5';
  input.style.borderColor = '#34d399';
  setTimeout(() => {{
    input.style.backgroundColor = '#ffffff';
    input.style.borderColor = '#d1d5db';
  }}, 1500);
}}


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
  document.querySelectorAll('.no-mes-cb').forEach(cb => cb.checked = false);
  document.querySelectorAll('.no-mes-cb')[mesIdx].checked = true;
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
  if (!mun) {{ alert('Debes ingresar la municipalidad'); return; }}

  const checkedMeses = [...document.querySelectorAll('.no-mes-cb:checked')].map(cb => cb.value);
  if (checkedMeses.length === 0) {{ alert('Selecciona al menos un mes'); return; }}
  const mes = checkedMeses.join(' / ');
  const fecha = document.getElementById('no-fecha').value || 'Por definir';
  const tipo = document.getElementById('no-tipo').value;
  const cant = parseFloat(document.getElementById('no-cant').value) || 0;
  const peso = parseFloat(document.getElementById('no-peso').value) || 1;

  if (tipo === 'cereal') {{
    const tbody = document.getElementById('tbody-cereal');
    const tbodyPend = document.getElementById('tbody-pend-cereal');
    const totalKg = (cant * peso).toFixed(2);
    const newRow = document.createElement('tr');
    newRow.className = 'trow hover:bg-green-50 transition bg-green-50';
    newRow.setAttribute('data-mes', mes);
    newRow.setAttribute('data-mun', mun.toLowerCase());
    newRow.innerHTML = `<td class="px-3 py-2 font-semibold text-green-800 text-xs">${{mun}} <span class="text-[9px] bg-green-200 text-green-800 px-1 rounded uppercase ml-1">Nuevo</span></td>
      <td class="px-3 py-2 text-xs text-gray-600">${{mes}}</td>
      <td class="px-3 py-2 text-xs font-mono text-gray-700">${{fecha}}</td>
      <td class="px-2 py-1"><input type="date" onchange="markDateSaved(this)" class="text-[10px] border border-gray-300 rounded p-1 w-24 bg-white text-blue-700 font-mono"></td>
      <td class="px-2 py-1"><input type="date" onchange="markDateSaved(this)" class="text-[10px] border border-gray-300 rounded p-1 w-24 bg-white text-amber-700 font-mono"></td>
      <td class="px-2 py-1"><input type="date" onchange="markDateSaved(this)" class="text-[10px] border border-gray-300 rounded p-1 w-24 bg-white text-purple-700 font-mono"></td>
      <td class="px-3 py-2 text-xs font-mono text-right">${{cant}}</td>
      <td class="px-3 py-2 text-xs font-mono text-right">${{peso}}</td>
      <td class="px-3 py-2 text-xs font-mono text-right font-bold text-red-700">${{totalKg}}</td>
      <td class="px-3 py-2 text-xs font-mono text-right">-</td>
      <td class="px-3 py-2 text-xs font-mono text-right">-</td>`;
    if (tbody) tbody.insertBefore(newRow, tbody.firstChild);

    const pendRow = document.createElement('tr');
    pendRow.className = 'trow hover:bg-orange-50 transition bg-orange-50';
    pendRow.setAttribute('data-mes', mes);
    pendRow.innerHTML = `<td class="px-2 py-1 font-semibold text-gray-800 text-[11px]">${{mun}} <span class="text-[9px] bg-orange-200 text-orange-800 px-1 rounded uppercase ml-1">Nuevo</span></td>
      <td class="px-2 py-1 text-[11px] text-gray-600">${{mes}}</td>
      <td class="px-2 py-1 text-[11px] font-mono text-gray-700">${{fecha}}</td>
      <td class="px-2 py-1 text-[11px] font-mono text-right">${{cant}}</td>
      <td class="px-2 py-1 text-[11px] font-mono text-right">${{peso}}</td>
      <td class="px-2 py-1 text-[11px] font-mono text-right font-bold text-orange-700">${{totalKg}}</td>
      <td class="px-2 py-1 text-[11px] font-mono text-right">-</td>
      <td class="px-2 py-1 text-[11px] font-mono text-right">-</td>
      <td class="px-2 py-1 text-[11px] font-mono text-right">-</td>`;
    if (tbodyPend) tbodyPend.insertBefore(pendRow, tbodyPend.firstChild);
    applyTableFilters('cereal');

  }} else {{
    const tbody = document.getElementById('tbody-leche');
    const tbodyPend = document.getElementById('tbody-pend-leche');
    const cajas = (cant / 48).toFixed(1);
    const newRow = document.createElement('tr');
    newRow.className = 'trow hover:bg-green-50 transition bg-green-50';
    newRow.setAttribute('data-mes', mes);
    newRow.innerHTML = `<td class="px-3 py-2 font-semibold text-green-800 text-xs">${{mun}} <span class="text-[9px] bg-green-200 text-green-800 px-1 rounded uppercase ml-1">Nuevo</span></td>
      <td class="px-3 py-2 text-xs text-gray-600">${{mes}}</td>
      <td class="px-3 py-2 text-xs font-mono text-gray-700">${{fecha}}</td>
      <td class="px-3 py-2 text-xs font-mono text-right font-bold text-blue-700">${{cant}}</td>
      <td class="px-3 py-2 text-xs font-mono text-right">${{cajas}}</td>
      <td class="px-3 py-2 text-xs font-mono text-right">-</td>
      <td class="px-3 py-2 text-xs text-center">🟡</td>
      <td class="px-2 py-1"><input type="date" class="text-[10px] border border-gray-300 rounded p-1 w-24 bg-white focus:border-blue-500 font-mono"></td>`;
    if (tbody) tbody.insertBefore(newRow, tbody.firstChild);

    const pendRow = document.createElement('tr');
    pendRow.className = 'trow hover:bg-orange-50 transition bg-orange-50';
    pendRow.setAttribute('data-mes', mes);
    pendRow.innerHTML = `<td class="px-2 py-1 font-semibold text-gray-800 text-[11px]">${{mun}} <span class="text-[9px] bg-orange-200 text-orange-800 px-1 rounded uppercase ml-1">Nuevo</span></td>
      <td class="px-2 py-1 text-[11px] text-gray-600">${{mes}}</td>
      <td class="px-2 py-1 text-[11px] font-mono text-gray-700">${{fecha}}</td>
      <td class="px-2 py-1 text-[11px] font-mono text-right font-bold text-blue-700">${{cant}}</td>
      <td class="px-2 py-1 text-[11px] font-mono text-right">${{cajas}}</td>
      <td class="px-2 py-1 text-[11px] font-mono text-right">-</td>`;
    if (tbodyPend) tbodyPend.insertBefore(pendRow, tbodyPend.firstChild);
    applyTableFilters('leche');
  }}

  closeNewOrderModal();
}}


// ── KARDEX ──────────────────────────────────────────────────
let liveKardex = [...kardexDB];

function renderKardex() {{
  const mesFilter     = '';
  const productoFilter = (document.getElementById('kardex-producto-filter') || {{}}).value || '';
  const tbody = document.getElementById('tbody-kardex');
  if (!tbody) return;
  let html = '';
  let count = 0;
  liveKardex.slice().reverse().forEach(k => {{
    const matchProd = !productoFilter || k.producto.toLowerCase().includes(productoFilter.toLowerCase());
    if (!matchProd) return;
    const notasHtml = k.notas ? `<span class="text-amber-600 font-semibold">${{k.notas}}</span>` : '<span class="text-gray-300">—</span>';
    const qHtml = k.um === 'Und'
      ? `<span class="font-mono font-bold text-purple-600">${{(k.cantidad/1000).toFixed(1)}}k</span>`
      : `<span class="font-mono font-bold text-blue-600">${{(k.cantidad/1000).toFixed(1)}} TN</span>`;
    html += `<tr class="hover:bg-gray-50 trow" data-mes="${{getMonthFromFecha(k.fecha)}}">
      <td class="px-3 py-2 font-mono text-xs text-gray-600">${{k.fecha}}</td>
      <td class="px-3 py-2 font-semibold text-xs">${{k.producto}}</td>
      <td class="px-3 py-2 font-mono text-xs text-red-600">${{k.codigo}}</td>
      <td class="px-3 py-2 font-mono text-xs text-right">${{k.lote || '—'}}</td>
      <td class="px-3 py-2 text-xs text-right">${{qHtml}}</td>
      <td class="px-3 py-2 text-xs text-center text-gray-500">${{k.um}}</td>
      <td class="px-3 py-2 text-xs text-gray-500">${{k.proveedor || '—'}}</td>
      <td class="px-3 py-2 text-xs">${{notasHtml}}</td>
    </tr>`;
    count++;
  }});
  tbody.innerHTML = html;
  const cel = document.getElementById('kardex-count');
  if (cel) cel.textContent = count;
}}

function filterKardex() {{ renderKardex(); }}

function getMonthFromFecha(fecha) {{
  if (!fecha) return '';
  const parts = fecha.split('/');
  if (parts.length < 2) return '';
  const month = parseInt(parts[1], 10);
  const names = ['','Enero','Febrero','Marzo','Abril','Mayo','Junio',
                  'Julio','Agosto','Setiembre','Octubre','Noviembre','Diciembre'];
  return names[month] || '';
}}

function openNuevaEntrada() {{ openModalEntrada(); }}

// ── FÓRMULAS EDITOR ────────────────────────────────────────
let liveFormulas = JSON.parse(JSON.stringify(formulasDB));
let selectedDistrict = null;
const INGREDIENTS = ['Trigo','Avena','Quinua','Kiwicha','Haba','Soya','Maca','Maíz Chiclayano','Azúcar','Sal','Premix','Cacao'];

function renderFormulaList(filter='') {{
  const list = document.getElementById('formula-list');
  if (!list) return;
  const keys = Object.keys(liveFormulas).filter(k => k.toLowerCase().includes(filter.toLowerCase()));
  let html = '';
  keys.forEach(k => {{
    const active = k === selectedDistrict ? 'bg-red-50 border-l-4 border-red-500' : 'hover:bg-gray-50';
    const total = Object.values(liveFormulas[k]).reduce((a,b) => a+b, 0);
    const tag = Math.abs(total - 100) < 0.1
      ? '<span class="text-[9px] bg-green-100 text-green-700 px-1.5 py-0.5 rounded font-bold">100%</span>'
      : `<span class="text-[9px] bg-amber-100 text-amber-700 px-1.5 py-0.5 rounded font-bold">${{total.toFixed(0)}}%</span>`;
    html += `<div onclick="selectDistrict('${{k}}')" class="px-4 py-2.5 border-b border-gray-100 cursor-pointer ${{active}} flex items-center justify-between">
      <span class="text-xs font-semibold text-gray-800">${{k}}</span>
      ${{tag}}
    </div>`;
  }});
  list.innerHTML = html;
  document.getElementById('formula-count-label').textContent = keys.length + ' fórmulas';
}}

function filterFormulaList() {{
  renderFormulaList(document.getElementById('formula-search').value);
}}

function selectDistrict(dist) {{
  selectedDistrict = dist;
  document.getElementById('formula-edit-title').textContent = dist;
  document.getElementById('formula-editor-empty').classList.add('hidden');
  document.getElementById('formula-editor-form').classList.remove('hidden');
  document.getElementById('btn-save-formula').classList.remove('hidden');
  document.getElementById('btn-delete-formula').classList.remove('hidden');
  document.getElementById('fe-distrito-name').value = dist;

  const formula = liveFormulas[dist] || {{}};
  const grid = document.getElementById('formula-inputs-grid');
  grid.innerHTML = '';
  INGREDIENTS.forEach(ing => {{
    const val = formula[ing] || 0;
    if (val === 0 && !formula.hasOwnProperty(ing)) {{ /* skip zeros not in formula */ }}
    const div = document.createElement('div');
    div.innerHTML = `<label class="block text-xs font-semibold text-gray-500 mb-1">${{ing}} (%)</label>
      <input type="number" data-ing="${{ing}}" value="${{val}}" step="0.1" min="0" max="100"
        oninput="updateFormulaTotal()"
        class="w-full border border-gray-300 rounded-lg px-3 py-1.5 text-sm font-mono focus:outline-none focus:border-red-400">`;
    grid.appendChild(div);
  }});
  updateFormulaTotal();
  renderFormulaList(document.getElementById('formula-search').value);
  previewBache();
}}

function updateFormulaTotal() {{
  const inputs = document.querySelectorAll('#formula-inputs-grid input');
  let total = 0;
  inputs.forEach(inp => {{ total += parseFloat(inp.value) || 0; }});
  const bar = document.getElementById('formula-pct-bar');
  const lbl = document.getElementById('formula-total-pct');
  if (bar) bar.style.width = Math.min(total,100) + '%';
  if (bar) bar.style.background = Math.abs(total-100) < 0.1 ? '#16a34a' : total > 100 ? '#dc2626' : '#f59e0b';
  if (lbl) lbl.textContent = total.toFixed(2) + '%';
  if (lbl) lbl.className = 'font-black text-lg font-mono ' + (Math.abs(total-100) < 0.1 ? 'text-green-700' : total > 100 ? 'text-red-700' : 'text-amber-600');
  previewBache();
}}

function previewBache() {{
  const bacheKg = parseFloat((document.getElementById('fe-bache-kg') || {{}}).value) || 400;
  const tbody = document.getElementById('bache-preview-tbody');
  if (!tbody) return;
  const inputs = document.querySelectorAll('#formula-inputs-grid input');
  let html = '';
  inputs.forEach(inp => {{
    const pct = parseFloat(inp.value) || 0;
    if (pct === 0) return;
    const kg = (bacheKg * pct / 100).toFixed(2);
    html += `<tr>
      <td class="py-1 text-gray-700">${{inp.getAttribute('data-ing')}}</td>
      <td class="py-1 text-right font-mono text-gray-500">${{pct}}%</td>
      <td class="py-1 text-right font-mono font-bold text-red-700">${{kg}} kg</td>
    </tr>`;
  }});
  tbody.innerHTML = html || '<tr><td colspan="3" class="py-2 text-gray-400 text-center">Selecciona un distrito</td></tr>';
}}

function saveFormula() {{
  if (!selectedDistrict) return;
  const newName = document.getElementById('fe-distrito-name').value.trim();
  if (!newName) return alert('El nombre del distrito no puede estar vacío');
  const inputs = document.querySelectorAll('#formula-inputs-grid input');
  const formula = {{}};
  inputs.forEach(inp => {{
    const val = parseFloat(inp.value) || 0;
    if (val > 0) formula[inp.getAttribute('data-ing')] = val;
  }});
  const total = Object.values(formula).reduce((a,b)=>a+b,0);
  if (Math.abs(total - 100) > 0.5) {{
    if (!confirm(`La fórmula suma ${{total.toFixed(2)}}%, no exactamente 100%. ¿Guardar de todas formas?`)) return;
  }}
  if (newName !== selectedDistrict) {{
    delete liveFormulas[selectedDistrict];
    selectedDistrict = newName;
  }}
  liveFormulas[selectedDistrict] = formula;
  renderFormulaList(document.getElementById('formula-search').value);
  alert(`✅ Fórmula de "${{selectedDistrict}}" guardada correctamente`);
}}

function deleteFormulaDistrict() {{
  if (!selectedDistrict) return;
  if (!confirm(`¿Eliminar la fórmula de "${{selectedDistrict}}"? Esta acción no se puede deshacer.`)) return;
  delete liveFormulas[selectedDistrict];
  selectedDistrict = null;
  document.getElementById('formula-editor-empty').classList.remove('hidden');
  document.getElementById('formula-editor-form').classList.add('hidden');
  document.getElementById('btn-save-formula').classList.add('hidden');
  document.getElementById('btn-delete-formula').classList.add('hidden');
  renderFormulaList();
}}

function newDistritoFormula() {{
  const name = prompt('Nombre del nuevo distrito:');
  if (!name || !name.trim()) return;
  const trimmed = name.trim();
  if (liveFormulas[trimmed]) return alert('Ese distrito ya existe. Selecciónalo de la lista para editar.');
  liveFormulas[trimmed] = {{Trigo: 0, Avena: 0, Quinua: 0}};
  renderFormulaList();
  selectDistrict(trimmed);
}}

// ── PRODUCCIÓN BOM ──────────────────────────────────────────
function calcProduccion() {{
  const dist = (document.getElementById('prod-distrito') || {{}}).value;
  const kg   = parseFloat((document.getElementById('prod-kg') || {{}}).value) || 0;
  const formula = liveFormulas[dist] || {{}};
  const tbody = document.getElementById('bom-body');
  if (!tbody) return;
  let html = '';
  let sumPct = 0, sumKg = 0;
  Object.entries(formula).forEach(([ing, pct]) => {{
    const kgVal = (kg * pct / 100).toFixed(2);
    sumPct += pct; sumKg += parseFloat(kgVal);
    html += `<tr class="hover:bg-gray-50">
      <td class="px-3 py-2 text-xs font-semibold">${{ing}}</td>
      <td class="px-3 py-2 text-xs text-right font-mono">${{pct}}%</td>
      <td class="px-3 py-2 text-xs text-right font-mono font-bold text-red-700">${{kgVal}}</td>
    </tr>`;
  }});
  tbody.innerHTML = html;
  const sp = document.getElementById('bom-pct-total');
  const sk = document.getElementById('bom-kg-total');
  if (sp) sp.textContent = sumPct.toFixed(1) + '%';
  if (sk) sk.textContent = sumKg.toLocaleString('es-PE',{{minimumFractionDigits:2}}) + ' kg';
}}

function registrarProduccion() {{
  const dist = (document.getElementById('prod-distrito') || {{}}).value;
  const kg   = (document.getElementById('prod-kg') || {{}}).value;
  const fecha = (document.getElementById('prod-fecha') || {{}}).value;
  alert(`✅ Lote de Producción Registrado:\\n• Distrito: ${{dist}}\\n• Kg: ${{kg}}\\n• Fecha: ${{fecha || 'No especificada'}}\\n\\nPendiente confirmación HITL para descontar de Kardex.`);
}}

// ── RETENCIONES ─────────────────────────────────────────────
function setRetencionPreset(key) {{
  const presets = {{
    'jmq':       {{monto: 127657.08, entregas: 12, modo: '0'}},
    'huamachuco':{{monto: 340000,    entregas: 10, modo: '10'}},
    'encaanada': {{monto: 280000,    entregas: 4,  modo: '10'}},
  }};
  const p = presets[key];
  if (!p) return;
  document.getElementById('retMontoInput').value = p.monto;
  document.getElementById('retEntregasInput').value = p.entregas;
  document.getElementById('retModoSelect').value = p.modo;
  runRetencionCalc();
}}

function runRetencionCalc() {{
  const monto    = parseFloat(document.getElementById('retMontoInput').value) || 0;
  const entregas = parseInt(document.getElementById('retEntregasInput').value) || 1;
  const pct      = parseFloat(document.getElementById('retModoSelect').value) || 0;
  const LIMIT50UIT = 257500;
  const esMenor  = monto <= LIMIT50UIT;
  const totalRet = monto * pct / 100;
  const bruto    = monto / entregas;
  const retXent  = totalRet / entregas;
  const neto     = bruto - retXent;
  const fmt = v => 'S/. ' + v.toLocaleString('es-PE',{{minimumFractionDigits:2}});
  document.getElementById('resRetTotal').textContent      = fmt(totalRet);
  document.getElementById('resMontoBruto').textContent    = fmt(bruto);
  document.getElementById('resRetPorEntrega').textContent = (totalRet > 0 ? '-' : '') + fmt(retXent);
  document.getElementById('resMontoNeto').textContent     = fmt(neto);
  const warn = document.getElementById('retLegalWarning');
  if (esMenor && pct === 0) {{
    warn.className = 'p-3 rounded-xl text-xs leading-relaxed bg-green-50 border border-green-200 text-green-800';
    warn.innerHTML = `<strong>✅ EXONERADO (monto ≤ 50 UIT):</strong> Según Art. 139 y 149.2 del RLCE. El contrato no supera S/. 257,500 (50 UIT). Facoimpec cobra el <strong>100% íntegro</strong> de cada factura mensual (${{fmt(bruto)}}) sin retenciones.`;
  }} else if (monto > LIMIT50UIT || pct > 0) {{
    warn.className = 'p-3 rounded-xl text-xs leading-relaxed bg-amber-50 border border-amber-200 text-amber-800';
    warn.innerHTML = `<strong>⚠️ GARANTÍA FIEL CUMPLIMIENTO 10% (&gt; 50 UIT):</strong> La municipalidad retiene ${{fmt(retXent)}} en cada entrega. El fondo total (${{fmt(totalRet)}}) se libera con la Conformidad Final Anual de Diciembre.`;
  }}
}}

// ── PDF MODAL ───────────────────────────────────────────────
let pdfData = null;
function openPdfModal()  {{ document.getElementById('modalPdfUpload').style.display = 'flex'; }}
function closePdfModal() {{ document.getElementById('modalPdfUpload').style.display = 'none'; }}

function simulatePdfParse(key) {{
  const presets = {{
    'jmq': {{
      num:'Contrato 001-2026-MDJMQ/GM', mun:'MD José Manuel Quiroz',
      cereal:'9,914 kg/año (~826 kg/mes)', leche:'13,680 latas (285 cajas)',
      extra:'Monto: S/. 127,657.08 · 12 entregas · 0% Retención (< 50 UIT)'
    }},
    'ingenio': {{ num:'SIAF: 00089', mun:'El Ingenio', cereal:'280 kg (bolsas 1 kg)', leche:'1,610 latas (33 cajas)', extra:'' }},
    'huamachuco': {{ num:'SIAF: 802/803', mun:'Huamachuco', cereal:'4,606.8 kg (bolsas 1.32 kg)', leche:'10,470 latas (218 cajas)', extra:'' }},
  }};
  pdfData = presets[key];
  document.getElementById('pdfResMun').textContent    = pdfData.mun;
  document.getElementById('pdfResNum').textContent    = pdfData.num;
  document.getElementById('pdfResCereal').textContent = pdfData.cereal;
  document.getElementById('pdfResLeche').textContent  = pdfData.leche;
  const extra = document.getElementById('pdfResExtra');
  if (pdfData.extra) {{ extra.textContent = pdfData.extra; extra.classList.remove('hidden'); }}
  else extra.classList.add('hidden');
  document.getElementById('pdfResult').classList.remove('hidden');
}}

function handlePdfUpload(evt) {{ if (evt.target.files[0]) simulatePdfParse('jmq'); }}

function commitParsedPdf() {{
  if (!pdfData) return;
  alert(`🎉 Documento "${{pdfData.num}}" incorporado a facoimpec.db\\n• Entidad: ${{pdfData.mun}}`);
  closePdfModal();
}}

// ── REQUERIMIENTOS HITL ─────────────────────────────────────
function aprobarReq(numero) {{
  if (!confirm(`¿Confirmar aprobación del Requerimiento N° ${{numero}}?`)) return;
  alert(`✅ Requerimiento N° ${{numero}} APROBADO y registrado en facoimpec.db.\\nSe actualizará el kardex y las proyecciones.`);
}}

function hitlApproveAll() {{ alert('✅ Todas las compras pendientes aprobadas por HITL.'); }}
function hitlApprove(btn, label) {{
  const strip = btn.closest('.hitl-strip');
  strip.innerHTML = `<div class="text-green-700 font-bold text-xs">✅ Aprobado: ${{label}}</div>`;
  strip.style.background = '#f0fdf4';
  strip.style.borderColor = '#86efac';
}}
function hitlReject(btn) {{
  const strip = btn.closest('.hitl-strip');
  strip.innerHTML = `<div class="text-red-600 font-bold text-xs">❌ Rechazado — notificado al jefe de planta</div>`;
  strip.style.background = '#fef2f2';
  strip.style.borderColor = '#fca5a5';
}}

// ── WHATSAPP ASISTENTE ──────────────────────────────────────

function toggleWaWidget() {{
  const panel = document.getElementById('wa-widget-panel');
  if (panel.classList.contains('hidden')) {{
    panel.classList.remove('hidden');
    // slight delay for animation
    setTimeout(() => {{
      panel.classList.remove('translate-y-4', 'opacity-0');
      document.querySelector('#wa-floating-btn .absolute').style.display = 'none'; // hide badge
    }}, 10);
  }} else {{
    panel.classList.add('translate-y-4', 'opacity-0');
    setTimeout(() => {{
      panel.classList.add('hidden');
    }}, 300);
  }}
}}

const wa = document.getElementById('wa-chat');
let waTime = 1;

function waAppend(html, type) {{
  const div = document.createElement('div');
  div.className = type === 'user' ? 'wa-bubble-user' : 'wa-bubble-bot';
  div.innerHTML = html + `<div class="wa-time">09:3${{waTime++}}</div>`;
  wa.appendChild(div);
  wa.scrollTop = wa.scrollHeight;
}}

function waSend() {{
  const inp = document.getElementById('wa-input');
  const msg = inp.value.trim();
  if (!msg) return;
  inp.value = '';
  waAppend(msg, 'user');
  setTimeout(() => waProcessNL(msg), 600);
}}

function waProcessNL(msg) {{
  const lm = msg.toLowerCase();
  if (lm.includes('llegaron') || lm.includes('llegó') || lm.includes('camión') || lm.includes('lote')) {{
    waAppend(`<strong>📥 Entrada detectada</strong><br>He captado una llegada de materia prima. ¿Confirmas el registro en el Kardex?`, 'bot');
    waHitlPrompt(msg);
  }} else if (lm.includes('entregado') || lm.includes('acta') || lm.includes('confirmad')) {{
    waAppend(`<strong>✅ Entrega detectada</strong><br>Registraré la conformidad. ¿El N° de Acta es correcto?`, 'bot');
    waHitlPrompt(msg);
  }} else if (lm.includes('envasado') || lm.includes('bolsas') || lm.includes('terminad')) {{
    waAppend(`<strong>📦 Envasado registrado</strong><br>Lote marcado como "Listo para Despacho". ¿Confirmas?`, 'bot');
    waHitlPrompt(msg);
  }} else if (lm.includes('pendiente') || lm.includes('mañana') || lm.includes('sale')) {{
    waAppend(`<strong>📋 Pendiente anotado</strong><br>Lo agregué a la lista de pendientes. ¿Hay una fecha límite?`, 'bot');
  }} else {{
    waAppend(`Entendido. Puedo registrar llegadas, entregas, envasados y pendientes.<br><em style="font-size:11px;opacity:.7">Escribe con más detalle o usa los botones rápidos abajo.</em>`, 'bot');
  }}
}}

function waHitlPrompt(original) {{
  const div = document.createElement('div');
  div.className = 'hitl-strip';
  div.style.margin = '8px 0';
  div.innerHTML = `
    <div style="font-size:11px;font-weight:700;color:#92400e;margin-bottom:4px;">🔐 Confirma antes de guardar:</div>
    <div style="font-size:11px;color:#78350f;margin-bottom:6px;">"${{original}}"</div>
    <div style="display:flex;gap:6px;">
      <button onclick="waConfirm(this)" style="flex:1;background:#16a34a;color:#fff;border:none;padding:5px 0;border-radius:8px;font-weight:700;font-size:11px;cursor:pointer;">✅ Confirmar</button>
      <button onclick="waEdit(this)" style="flex:1;background:#e5e7eb;color:#374151;border:none;padding:5px 0;border-radius:8px;font-weight:700;font-size:11px;cursor:pointer;">✏️ Editar</button>
      <button onclick="waCancel(this)" style="flex:1;background:#fee2e2;color:#991b1b;border:none;padding:5px 0;border-radius:8px;font-weight:700;font-size:11px;cursor:pointer;">❌ Cancelar</button>
    </div>`;
  wa.appendChild(div);
  wa.scrollTop = wa.scrollHeight;
}}

function waConfirm(btn) {{
  const strip = btn.closest('.hitl-strip');
  const orig = strip.querySelector('div:nth-child(2)').textContent;
  strip.innerHTML = '<div style="color:#16a34a;font-weight:700;font-size:11px;">✅ Guardado en facoimpec.db</div>';
  strip.style.background = '#f0fdf4'; strip.style.borderColor = '#86efac';
  // Also add to kardex
  const kNew = {{fecha: new Date().toLocaleDateString('es-PE'), producto:'Registrado vía WA', codigo:'WA', lote:'', cantidad:0, um:'Kg', proveedor:'', notas: orig.replace(/['"]/g,'')}};
  liveKardex.push(kNew);
}}
function waEdit(btn) {{
  const txt = btn.closest('.hitl-strip').querySelector('div:nth-child(2)').textContent.replace(/['"]/g,'');
  document.getElementById('wa-input').value = txt;
  btn.closest('.hitl-strip').remove();
}}
function waCancel(btn) {{
  btn.closest('.hitl-strip').remove();
  waAppend('Cancelado. No se guardó ningún registro.', 'bot');
}}

function waQuickAction(type) {{
  const msgs = {{
    'camion':  'Llegaron 30 TN de Trigo Indurlac lote TG-26',
    'envasado':'Terminadas las 3,490 bolsas de Huamachuco',
    'despacho':'Salió camión T3K-881 con las 21 TN de Encañada',
    'entrega': 'Entregado a Cochan, acta N° 047, firma OK'
  }};
  document.getElementById('wa-input').value = msgs[type] || '';
  waSend();
}}

// ── VOICE SIMULATION ────────────────────────────────────────
const VOICE_SAMPLES = [
  'Llegaron 36 TN de avena lote 30 al almacén',
  'Mañana sale San Luis, EMHA, San Jose',
  'Terminado envasado 1,049 bolsas Chimban',
  'Pendiente Cochabamba 3 entregas más adicional',
  'Entregado Florencia de Mora, acta N° 081',
  'Llegaron 22 TN de azúcar lote AZ-22',
];

let voiceTimer = null;

function waVoice() {{
  const overlay = document.getElementById('voiceOverlay');
  overlay.style.display = 'flex';
  document.getElementById('voiceStatus').textContent = '🔴 Grabando...';
  voiceTimer = setTimeout(() => {{
    document.getElementById('voiceStatus').textContent = '⏳ Transcribiendo...';
    setTimeout(() => {{
      overlay.style.display = 'none';
      const sample = VOICE_SAMPLES[Math.floor(Math.random() * VOICE_SAMPLES.length)];
      document.getElementById('wa-input').value = sample;
      waAppend(`🎤 <em style="opacity:.7;font-size:11px;">[Audio transcrito]</em><br>${{sample}}`, 'user');
      setTimeout(() => waProcessNL(sample), 500);
    }}, 1200);
  }}, 2500);
}}

function stopVoice() {{
  clearTimeout(voiceTimer);
  document.getElementById('voiceOverlay').style.display = 'none';
  waAppend('Grabación cancelada.', 'bot');
}}


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
  alert('✅ Salida registrada en el Kardex\nDestino: ' + dest);
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
  alert('✅ Stock de ' + mat + ' actualizado\nMotivo: ' + motivo);
}}

// ── INIT ────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {{
  // Initial table counters
  ['cereal','leche','pend-cereal','pend-leche','ent-cereal','ent-leche','resumen'].forEach(id => {{
    const tbody = document.getElementById('tbody-' + id) || document.querySelector('[id*="' + id + '"]');
    if (tbody) {{
      const rows = tbody.querySelectorAll('tr.trow');
      const countEl = document.getElementById('count-' + id);
      if (countEl) countEl.textContent = rows.length;
      // Sum kg for cereal
      if (id === 'cereal') {{
        let kg = 0;
        rows.forEach(r => {{
          const c = r.querySelector('td:nth-child(6)');
          if (c) kg += parseFloat(c.textContent.replace(/[^0-9.]/g,'')) || 0;
        }});
        const el = document.getElementById('sum-cereal-kg');
        if (el) el.textContent = kg.toLocaleString('es-PE',{{minimumFractionDigits:2}}) + ' kg';
      }}
    }}
  }});
  calcProduccion();
  runRetencionCalc();
  renderNotes();
  renderKardex();
  renderFormulaList();
}});
</script>
</body>
</html>"""

# ─── Output ────────────────────────────────────────────────────────────────────
out_workspace = os.path.join(workspace_dir, "PROTOTIPO_FACOIMPEC.html")
out_artifact  = os.path.join(artifact_dir,  "prototipo_sistema_facoimpec.html")

with open(out_workspace, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"PROTOTIPO_FACOIMPEC.html generado: {len(html_content):,} chars")

os.makedirs(artifact_dir, exist_ok=True)
with open(out_artifact, "w", encoding="utf-8") as f:
    f.write(html_content)
print("prototipo_sistema_facoimpec.html actualizado en brain artifact")
