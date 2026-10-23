import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import re

# --- 1. CONFIGURACIÓN ---
output_dir = 'graficas_vivienda'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- 2. CARGA DE DATOS ROBUSTA ---
try:
    # Intentamos leer con diferentes codificaciones por si acaso
    df_total = pd.read_csv('Total_Vivienda.csv', encoding='utf-8')
except UnicodeDecodeError:
    df_total = pd.read_csv('Total_Vivienda.csv', encoding='latin-1')

# LIMPIEZA CRÍTICA: Eliminamos filas que sean totalmente nulas
df_total = df_total.dropna(how='all')
# Eliminamos la fila de comas vacía si existe al principio
if df_total.iloc[0].isnull().all() or (df_total.iloc[0].astype(str).str.contains(',,,').any()):
    df_total = df_total.iloc[1:]

df_total.columns = [str(c).strip() for c in df_total.columns]
col_ccaa = df_total.columns[0]

# --- 3. LIMPIEZA DE NÚMEROS ---
def limpiar_dato(x):
    if pd.isna(x) or str(x).strip() in ['', 'nan', 'None', '.']: return np.nan
    # Quitar puntos de miles y cambiar comas por puntos
    s = str(x).replace('.', '').replace(',', '.').strip()
    try:
        return float(s)
    except:
        return np.nan

for col in df_total.columns[1:]:
    df_total[col] = df_total[col].apply(limpiar_dato)

# --- 4. FILTRADO DE AÑOS ---
anios_hist = [c for c in df_total.columns if c.isdigit() and 2008 <= int(c) <= 2024]
print(f"Años detectados: {anios_hist}")

# --- 5. CARGA DE KPIs ---
df_kpis = pd.read_csv('kpis_numero_viviendas.csv')
df_kpis.columns = [str(c).strip() for c in df_kpis.columns]

# --- 6. BUCLE DE GENERACIÓN ---
for _, row in df_total.iterrows():
    nombre_ccaa = str(row[col_ccaa]).strip()
    if nombre_ccaa == 'nan' or not nombre_ccaa: continue
    
    # Extraer valores y asegurar que son números
    datos = row[anios_hist].values.astype(float)
    
    # Si la fila no tiene datos numéricos, la ignoramos
    if np.all(np.isnan(datos)):
        continue

    print(f"-> Creando gráfica para: {nombre_ccaa}")
    
    x_hist = [int(a) for a in anios_hist]
    
    # Generar la figura
    plt.figure(figsize=(10, 6))
    plt.plot(x_hist, datos, marker='o', color='#1f77b4', linewidth=2, label='Histórico Real')
    
    # Unir con Predicciones 2026
    nombre_clean = nombre_ccaa.lower().replace(" ", "")
    match = df_kpis[df_kpis['ccaa'].str.lower().str.replace(" ", "").str.contains(nombre_clean, na=False)]
    
    if not match.empty:
        k = match.iloc[0]
        # Puntos: 2024 (último real), 2025, 2026, 2027
        x_pred = [2024, 2025, 2026, 2027]
        y_pred = [datos[-1], k['pred_viviendas_inicio'], 
                  (k['pred_viviendas_inicio'] + k['pred_viviendas_fin'])/2, 
                  k['pred_viviendas_fin']]
        
        plt.plot(x_pred, y_pred, color='#d62728', linestyle='--', marker='s', label='Predicción')
        
        info = f"Var. 2026: {k['pred_variacion_pct']}%\nCrec. Medio: {k['pred_crecimiento_anual_medio_pct']}%"
        plt.gca().text(0.05, 0.9, info, transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.8))

    plt.title(f'Stock de Viviendas: {nombre_ccaa}', fontweight='bold')
    plt.ticklabel_format(style='plain', axis='y')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Guardar archivo limpiando caracteres prohibidos en Windows
    safe_name = re.sub(r'[\\/*?:"<>|]', "", nombre_ccaa).replace(" ", "_")
    plt.savefig(f'{output_dir}/{safe_name}.png')
    plt.close()

print(f"\nPROCESO TERMINADO. Revisa la carpeta '{output_dir}'.")