import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import re

# --- 1. PREPARACIÓN DE CARPETA ---
output_dir = 'analisis_poblacion_2026'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# --- 2. CARGA Y LIMPIEZA PROFUNDA ---
df_raw = pd.read_csv('Numero_Personas.csv', dtype=str)
df_raw.columns = [str(c).strip() for c in df_raw.columns]
col_ccaa = df_raw.columns[0]

# Extraer años (1 de enero de 2025 -> 2025)
years_raw = [c for c in df_raw.columns if '1 de enero de' in c]
year_cols = {c: int(re.search(r'\d{4}', c).group()) for c in years_raw}
df_raw = df_raw.rename(columns=year_cols)
years = sorted(year_cols.values())

def limpiar_profundo(x):
    if pd.isna(x): return np.nan
    # Eliminamos puntos de miles, cambiamos comas y quitamos CUALQUIER espacio
    s = str(x).replace('.', '').replace(',', '.').replace(' ', '').strip()
    try:
        return float(s)
    except:
        return np.nan

# --- 3. EXTRACCIÓN DE TOTALES POR CCAA ---
data_clean = []
ccaa_actual = None

for i in range(len(df_raw)):
    label_original = str(df_raw.iloc[i, 0])
    label_strip = label_original.strip()
    
    # Identificar la Comunidad (Fila sin sangría)
    if not label_original.startswith(' '):
        ccaa_actual = label_strip
    
    # Capturar la fila "Total" que está bajo "Todas las edades"
    if label_strip == "Total" and ccaa_actual:
        row_vals = df_raw.iloc[i][years].apply(limpiar_profundo).astype(float)
        
        # Filtro de seguridad para no pillar desgloses pequeños
        if not row_vals.isnull().all() and row_vals.max() > 100000:
            data_clean.append({'CCAA': ccaa_actual, **row_vals.to_dict()})
            ccaa_actual = None 

df_final = pd.DataFrame(data_clean).drop_duplicates(subset=['CCAA'])

# --- 4. MODELO DE PREDICCIÓN (Suavizado Exponencial Simple) ---
kpis = []

for _, row in df_final.iterrows():
    nombre = row['CCAA']
    y_hist = row[years].values.astype(float)
    
    # Manejo de NaNs en el histórico
    y_hist_clean = y_hist[~np.isnan(y_hist)]
    x_hist_clean = np.array(years)[~np.isnan(y_hist)]
    
    if len(y_hist_clean) < 2: continue

    # Calculamos la tasa de crecimiento reciente (últimos 3 periodos) para proyectar
    # Esto evita que una caída en 2010 arruine la predicción de 2026
    tasa_reciente = (y_hist_clean[-1] / y_hist_clean[-3])**(1/2) if len(y_hist_clean) >= 3 else (y_hist_clean[-1] / y_hist_clean[-2])
    
    val_2026 = y_hist_clean[-1] * (tasa_reciente ** 1) # Proyección a 1 año vista (2025 -> 2026)
    
    # Métricas
    variacion_26 = ((val_2026 - y_hist_clean[-1]) / y_hist_clean[-1]) * 100
    crecimiento_anual_medio = (np.diff(y_hist_clean).mean() / y_hist_clean.mean()) * 100
    
    kpis.append({
        'Comunidad Autónoma': nombre,
        'Población (2025)': int(y_hist_clean[-1]),
        'Predicción (2026)': int(val_2026),
        'Variación % (25-26)': round(variacion_26, 2),
        'Crecimiento Anual Medio %': round(crecimiento_anual_medio, 2)
    })

    # --- 5. GENERACIÓN DE GRÁFICAS ---
    safe_name = re.sub(r'[\\/*?:"<>|]', "", nombre).replace(" ", "_")
    
    # Gráfica SIN Predicción
    plt.figure(figsize=(10, 5))
    plt.plot(x_hist_clean, y_hist_clean, marker='o', color='#2ca02c', linewidth=2)
    plt.title(f'{nombre} - Histórico Población Real', fontweight='bold')
    plt.ticklabel_format(style='plain', axis='y')
    plt.grid(True, alpha=0.3)
    plt.savefig(f'{output_dir}/{safe_name}_HISTORICO.png')
    plt.close()

    # Gráfica CON Predicción
    plt.figure(figsize=(10, 5))
    plt.plot(x_hist_clean, y_hist_clean, color='#2ca02c', label='Histórico', linewidth=2)
    plt.plot([2025, 2026], [y_hist_clean[-1], val_2026], 'r--o', label='Proyección (Modelo Inercial)')
    plt.title(f'{nombre} - Predicción Población 2026 (Tendencia Actual)', fontweight='bold')
    plt.ticklabel_format(style='plain', axis='y')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(f'{output_dir}/{safe_name}_PREDICCION.png')
    plt.close()

# --- 6. GUARDAR EXCEL DENTRO DE LA CARPETA ---
df_kpi_final = pd.DataFrame(kpis)
df_kpi_final.to_excel(f'{output_dir}/KPIs_Poblacion_2026.xlsx', index=False)

print(f"Finalizado. Los resultados (gráficas y Excel) están en: {output_dir}")