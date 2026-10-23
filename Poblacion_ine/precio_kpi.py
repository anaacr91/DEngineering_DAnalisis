import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import os

# --- 1. CONFIGURACIÓN DE CARPETA ---
output_dir = 'graficas_precio_vivienda'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- 2. PROCESAMIENTO DE DATOS HISTÓRICOS ---
df_hist_raw = pd.read_csv('Precio_Vivienda.csv')
data_rows = []
current_ccaa = None
index_cols = [c for c in df_hist_raw.columns if c.endswith('_1')]

for idx, row in df_hist_raw.iterrows():
    val = str(row['CCAA']).strip()
    if val == "Nacional" or (len(val) > 2 and val[:2].isdigit()):
        current_ccaa = re.sub(r'^\d+\s+', '', val)
    elif val == "General":
        row_dict = {'CCAA': current_ccaa}
        for col in index_cols:
            raw_val = str(row[col]).replace('.', '').replace(',', '.')
            try:
                row_dict[col] = float(raw_val)
            except:
                row_dict[col] = np.nan
        data_rows.append(row_dict)

df_hist = pd.DataFrame(data_rows)
df_melted = df_hist.melt(id_vars=['CCAA'], var_name='Periodo', value_name='Precio')
df_melted['Anio'] = df_melted['Periodo'].str.extract(r'(\d{4})').astype(int)
df_melted['Trimestre'] = df_melted['Periodo'].str.extract(r'T(\d)').astype(int)

# Filtro 2008 - 2025T3
df_plot_h = df_melted[(df_melted['Anio'] >= 2008) & ~((df_melted['Anio'] == 2025) & (df_melted['Trimestre'] > 3))].copy()

# --- 3. CARGA DE PREDICCIONES 2026 ---
df_pred_2026 = pd.read_csv('predicciones_trimestrales_2026.csv')
mapping = {
    'Asturias': 'Asturias, Principado de', 'Balears': 'Balears, Illes',
    'Castilla-La Mancha': 'Castilla - La Mancha', 'Valencia': 'Comunitat Valenciana',
    'Madrid': 'Madrid, Comunidad de', 'Murcia': 'Murcia, Región de',
    'Navarra': 'Navarra, Comunidad Foral de', 'Rioja': 'Rioja, La'
}
df_pred_2026['ccaa_join'] = df_pred_2026['ccaa'].replace(mapping)

# --- 4. BUCLE DE GENERACIÓN ---
ccaas = sorted(df_plot_h['CCAA'].unique())

for ccaa in ccaas:
    subset_h = df_plot_h[df_plot_h['CCAA'] == ccaa].sort_values(['Anio', 'Trimestre'])
    x_h = subset_h['Anio'] + (subset_h['Trimestre'] - 1) / 4
    safe_name = re.sub(r'[\\/*?:"<>|]', "", ccaa).replace(" ", "_")

    # --- GRÁFICA 1: SOLO HISTÓRICO (SIN PREDICCIÓN) ---
    plt.figure(figsize=(10, 6))
    plt.plot(x_h, subset_h['Precio'], label='Índice Histórico Real', color='#1f77b4', linewidth=2)
    plt.title(f'{ccaa} - Evolución Histórica (Sin Predicción)', fontsize=13, fontweight='bold')
    plt.xlabel('Año')
    plt.ylabel('Índice de Precios (Base 2015)')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.savefig(f'{output_dir}/{safe_name}_HISTORICO_LIMPIO.png')
    # No cerramos aún si queremos que plt.show() las muestre todas, 
    # pero si son muchas (60+), mejor comentar plt.show() y usar plt.close()

    # --- GRÁFICA 2: CON PREDICCIÓN 2026 ---
    plt.figure(figsize=(10, 6))
    plt.plot(x_h, subset_h['Precio'], color='#1f77b4', label='Histórico Real', linewidth=2)
    
    subset_p = df_pred_2026[(df_pred_2026['ccaa_join'] == ccaa) & (df_pred_2026['tipo_vivienda'] == 'General')]
    if not subset_p.empty:
        subset_p = subset_p.sort_values(['anio', 'trimestre'])
        x_p = subset_p['anio'] + (subset_p['trimestre'] - 1) / 4
        plt.plot(np.append(x_h.iloc[-1], x_p), np.append(subset_h['Precio'].iloc[-1], subset_p['precio_predicho']), 
                 color='#d62728', linestyle='--', marker='o', label='Predicción 2026')

    plt.title(f'{ccaa} - Evolución y Predicción 2026', fontsize=13, fontweight='bold')
    plt.xlabel('Año')
    plt.ylabel('Índice de Precios (Base 2015)')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.savefig(f'{output_dir}/{safe_name}_CON_PREDICCION.png')

print(f"Archivos guardados en '{output_dir}'.")
plt.show()