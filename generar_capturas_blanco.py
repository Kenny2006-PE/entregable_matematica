import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd

# Directorio de salida
out_dir = r"c:\Users\PC\Desktop\Matematica discreta trabajo grupal\Capturas para diapositiva"
os.makedirs(out_dir, exist_ok=True)

# Cargar dataset de 23 rutas
df = pd.read_csv(r"c:\Users\PC\Desktop\Matematica discreta trabajo grupal\datos_logisticos.csv")
x = df["Distancia_km"].values.astype(float)
y1 = df["Costo_Total_Soles"].values.astype(float)
y2 = df["Consumo_Combustible_Gal"].values.astype(float)
n = len(x)

# Cálculos MCO
m1, b1 = np.polyfit(x, y1, 1)
r1 = np.corrcoef(x, y1)[0, 1]
r2_1 = r1**2
res1 = y1 - (m1 * x + b1)
steyx1 = np.sqrt(np.sum(res1**2) / (n - 2))

m2, b2 = np.polyfit(x, y2, 1)
r2 = np.corrcoef(x, y2)[0, 1]
r2_2 = r2**2
res2 = y2 - (m2 * x + b2)
steyx2 = np.sqrt(np.sum(res2**2) / (n - 2))

# Configuración global limpia
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.facecolor'] = '#FFFFFF'
plt.rcParams['axes.facecolor'] = '#FFFFFF'

# =============================================================================
# 1. GRÁFICO MODELO 1: DISTANCIA VS COSTOS (FONDO BLANCO, ESTILO CIENTÍFICO)
# =============================================================================
fig1, ax1 = plt.subplots(figsize=(10, 6.5), facecolor='#FFFFFF')
xs = np.linspace(0, x.max() * 1.05, 100)
ys1 = m1 * xs + b1
ci_sup1 = ys1 + 1.96 * steyx1
ci_inf1 = np.maximum(0, ys1 - 1.96 * steyx1)

ax1.fill_between(xs, ci_inf1, ci_sup1, color='#E0F2FE', alpha=0.8, label='Banda de Confianza 95% (MCO)')
ax1.plot(xs, ys1, color='#0284C7', linewidth=2.5, label=f'Recta Ajustada: Y = {m1:.4f}*X - {abs(b1):.2f}')
ax1.scatter(x, y1, color='#0369A1', edgecolor='#FFFFFF', s=65, zorder=5, label='23 Rutas Reales (Perú)')

# Decoración limpia
ax1.set_title("Modelo 1: Regresión Lineal — Distancia (km) vs Costo de Transporte (S/)", fontsize=13, fontweight='bold', color='#0F172A', pad=12)
ax1.set_xlabel("Distancia Recorrida (km)", fontsize=11, fontweight='bold', color='#334155')
ax1.set_ylabel("Costo Total de Flete (S/)", fontsize=11, fontweight='bold', color='#334155')
ax1.grid(True, linestyle='--', alpha=0.4, color='#CBD5E1')
ax1.tick_params(colors='#334155', labelsize=10)

# Caja de parámetros limpia
info1 = (
    f"Parámetros del Modelo 1:\n"
    f"• Pendiente (m1): S/ {m1:.4f}/km (+S/ {m1*100:.2f} / 100 km)\n"
    f"• Intersección (b1): -S/ {abs(b1):.2f}\n"
    f"• Coef. Determinación (R2): {r2_1*100:.2f}%\n"
    f"• Correlación (r): {r1:.4f} (Muy Fuerte)\n"
    f"• Error Típico (STEYX): S/ {steyx1:.2f}\n"
    f"• Proyección 500 km: S/ {m1*500+b1:.2f}"
)
ax1.text(0.04, 0.62, info1, transform=ax1.transAxes, fontsize=9.5, color='#0F172A',
         bbox=dict(boxstyle="round,pad=0.6", facecolor='#F8FAFC', edgecolor='#0284C7', linewidth=1.2))

ax1.legend(loc='lower right', frameon=True, facecolor='#FFFFFF', edgecolor='#CBD5E1', fontsize=9.5)
for spine in ax1.spines.values():
    spine.set_color('#94A3B8')

fig1.savefig(os.path.join(out_dir, "01_Grafico_Modelo1_Costos_Blanco.png"), dpi=220, bbox_inches='tight')
plt.close(fig1)
print("1/7 Creado: 01_Grafico_Modelo1_Costos_Blanco.png")

# =============================================================================
# 2. GRÁFICO MODELO 2: COMBUSTIBLE CON DISPERSIÓN REGIONAL (FONDO BLANCO)
# =============================================================================
fig2, ax2 = plt.subplots(figsize=(10.5, 6.5), facecolor='#FFFFFF')
ys2 = m2 * xs + b2

ax2.plot(xs, ys2, color='#EA580C', linewidth=2.5, label=f'Recta Ajustada: Y = {m2:.4f}*X - {abs(b2):.2f}')

c_mask = df["Region"] == "Costa"
s_mask = df["Region"] == "Sierra"
j_mask = df["Region"] == "Selva"

ax2.scatter(x[c_mask], y2[c_mask], color='#0284C7', edgecolor='#0F172A', s=70, label='Costa (Llanura / Menor Esfuerzo)', zorder=6)
ax2.scatter(x[s_mask], y2[s_mask], color='#EA580C', edgecolor='#0F172A', s=85, marker='^', label='Sierra (Altitud Andina / Pendientes)', zorder=6)
ax2.scatter(x[j_mask], y2[j_mask], color='#16A34A', edgecolor='#0F172A', s=85, marker='s', label='Selva (Rutas de Selva)', zorder=6)

# Anotación explicativa de picos
puno_idx = df[df["Ruta"].str.contains("Puno")].index[0]
ax2.annotate("Pico Sierra (Puno): 282.8 gal\n(Mayor consumo por altura y pendiente)",
             xy=(x[puno_idx], y2[puno_idx]), xytext=(x[puno_idx]-450, y2[puno_idx]+25),
             arrowprops=dict(facecolor='#EA580C', shrink=0.08, width=1.2, headwidth=5),
             fontsize=9, fontweight='bold', color='#9A3412',
             bbox=dict(boxstyle="round,pad=0.4", facecolor='#FFF7ED', edgecolor='#EA580C'))

tacna_idx = df[df["Ruta"].str.contains("Tacna")].index[0]
ax2.annotate("Ruta Costa (Tacna): 154.9 gal\n(Menor consumo en carretera plana)",
             xy=(x[tacna_idx], y2[tacna_idx]), xytext=(x[tacna_idx]+20, y2[tacna_idx]-45),
             arrowprops=dict(facecolor='#0284C7', shrink=0.08, width=1.2, headwidth=5),
             fontsize=9, fontweight='bold', color='#075985',
             bbox=dict(boxstyle="round,pad=0.4", facecolor='#F0F9FF', edgecolor='#0284C7'))

ax2.set_title("Modelo 2: Distancia (km) vs Consumo de Diésel (gal) — Dispersión por Relieve", fontsize=13, fontweight='bold', color='#0F172A', pad=12)
ax2.set_xlabel("Distancia Recorrida (km)", fontsize=11, fontweight='bold', color='#334155')
ax2.set_ylabel("Consumo de Combustible (Galones Diésel)", fontsize=11, fontweight='bold', color='#334155')
ax2.grid(True, linestyle='--', alpha=0.4, color='#CBD5E1')
ax2.tick_params(colors='#334155', labelsize=10)

info2 = (
    f"Parámetros del Modelo 2:\n"
    f"• Pendiente (m2): {m2:.4f} gal/km\n"
    f"• Rendimiento: {1/m2:.2f} km/galón\n"
    f"• Intersección (b2): -{abs(b2):.2f} gal\n"
    f"• R2 = {r2_2*100:.2f}% | r = {r2:.4f}\n"
    f"• Varianza residual: 18.43%\n"
    f"  (Refleja los picos andinos)"
)
ax2.text(0.04, 0.62, info2, transform=ax2.transAxes, fontsize=9.5, color='#0F172A',
         bbox=dict(boxstyle="round,pad=0.6", facecolor='#FFF7ED', edgecolor='#EA580C', linewidth=1.2))

ax2.legend(loc='lower right', frameon=True, facecolor='#FFFFFF', edgecolor='#CBD5E1', fontsize=9.5)
for spine in ax2.spines.values():
    spine.set_color('#94A3B8')

fig2.savefig(os.path.join(out_dir, "02_Grafico_Modelo2_Combustible_Regiones_Blanco.png"), dpi=220, bbox_inches='tight')
plt.close(fig2)
print("2/7 Creado: 02_Grafico_Modelo2_Combustible_Regiones_Blanco.png")

# =============================================================================
# 3. IMAGEN DE APOYO: FUNDAMENTO MATEMÁTICO DE GAUSS (FONDO BLANCO, TARJETA LIMPIA)
# =============================================================================
fig3 = plt.figure(figsize=(11, 8.5), facecolor='#FFFFFF')
ax3 = fig3.add_subplot(111)
ax3.axis('off')

# Marco elegante
card = patches.FancyBboxPatch((0.02, 0.02), 0.96, 0.96, boxstyle="round,pad=0.02", facecolor='#FFFFFF', edgecolor='#2563EB', linewidth=1.5)
ax3.add_patch(card)

# Título
ax3.text(0.05, 0.93, "FUNDAMENTACIÓN TEÓRICA EN MATEMÁTICA DISCRETA", fontsize=13, fontweight='bold', color='#1E40AF')
ax3.text(0.05, 0.89, "Método de Mínimos Cuadrados Ordinarios (MCO) y Deducción de Gauss", fontsize=11, color='#475569')

# Sección 1
ax3.text(0.05, 0.82, "1. Definición del Conjunto Muestral Finito Discreto:", fontsize=10.5, fontweight='bold', color='#0F172A')
ax3.text(0.07, 0.77, r"$S = \{(x_1, y_1), (x_2, y_2), \dots, (x_{23}, y_{23})\} \subset \mathbb{R}^2$", fontsize=11, color='#1E40AF')

# Tabla de sumatorias
ax3.text(0.05, 0.70, "2. Sumatorias Discretas Calculadas sobre las 23 Rutas Reales:", fontsize=10.5, fontweight='bold', color='#0F172A')

sums_box = (
    f"  • Muestra (n) = 23 rutas              • Sumatoria X (∑ xᵢ)  = 19,098.00 km\n"
    f"  • Sumatoria Y₁ (∑ yᵢ) = S/ 6,737.88   • Sumatoria X² (∑ xᵢ²) = 19,781,876.00\n"
    f"  • Sumatoria XY₁ (∑ xᵢyᵢ) = 7,095,607.52\n"
    f"  • Media Distancia (x̄) = 830.35 km     • Media Costo (ȳ₁)    = S/ 292.95"
)
ax3.text(0.06, 0.57, sums_box, fontsize=9.5, fontfamily='monospace', color='#1E293B',
         bbox=dict(boxstyle="round,pad=0.5", facecolor='#F1F5F9', edgecolor='#CBD5E1', linewidth=1))

# Sección 2: Sistema de Gauss
ax3.text(0.05, 0.50, "3. Sistema de Ecuaciones Normales de Gauss (2x2):", fontsize=10.5, fontweight='bold', color='#0F172A')
gauss_text = (
    "  [1]   m · ∑(xᵢ²) + b · ∑(xᵢ) = ∑(xᵢ · yᵢ)     -->   m(19,781,876) + b(19,098) = 7,095,607.52\n"
    "  [2]   m · ∑(xᵢ)  + b · n     = ∑(yᵢ)          -->   m(19,098)     + b(23)     = 6,737.88"
)
ax3.text(0.06, 0.40, gauss_text, fontsize=9.5, fontfamily='monospace', color='#0F172A',
         bbox=dict(boxstyle="round,pad=0.5", facecolor='#EFF6FF', edgecolor='#3B82F6', linewidth=1))

# Sección 3: Fórmulas y resultados
ax3.text(0.05, 0.33, "4. Resolución Analítica de los Coeficientes (m y b):", fontsize=10.5, fontweight='bold', color='#0F172A')

sol_box = (
    "  Fórmula de la Pendiente Marginal (m):\n"
    "    m = [ n · ∑(XY) - (∑X)(∑Y) ] / [ n · ∑(X²) - (∑X)² ]\n"
    "    m = [ 23(7,095,607.52) - (19,098)(6,737.88) ] / [ 23(19,781,876) - (19,098)² ]\n"
    "    m = 34,589,740.96 / 90,434,100  =  +0.382483  -->  S/ 0.3825 / km\n\n"
    "  Fórmula de la Intersección Base (b):\n"
    "    b = ȳ - m · x̄ = [ 6,737.88 - (0.382483 · 19,098) ] / 23  =  -S/ 24.6428\n\n"
    "  Ecuación Afín Final:   Ŷ₁ = 0.3825 · X - 24.64 (S/)    |    R² = 85.45%    |    r = 0.9244"
)
ax3.text(0.06, 0.06, sol_box, fontsize=9.5, fontfamily='monospace', color='#0F172A',
         bbox=dict(boxstyle="round,pad=0.5", facecolor='#F0FDF4', edgecolor='#16A34A', linewidth=1))

fig3.savefig(os.path.join(out_dir, "03_Fundamento_Matematico_Gauss_Blanco.png"), dpi=220, bbox_inches='tight')
plt.close(fig3)
print("3/7 Creado: 03_Fundamento_Matematico_Gauss_Blanco.png")

# =============================================================================
# 4. IMAGEN DE APOYO: ALGORITMO PYTHON MCO (FONDO BLANCO / TARJETA DE CÓDIGO)
# =============================================================================
fig4 = plt.figure(figsize=(10.5, 7.5), facecolor='#FFFFFF')
ax4 = fig4.add_subplot(111)
ax4.axis('off')

# Tarjeta
card4 = patches.FancyBboxPatch((0.03, 0.03), 0.94, 0.94, boxstyle="round,pad=0.02", facecolor='#F8FAFC', edgecolor='#334155', linewidth=1.2)
ax4.add_patch(card4)

# Cabecera
head_bar = patches.Rectangle((0.03, 0.88), 0.94, 0.09, facecolor='#1E293B')
ax4.add_patch(head_bar)
ax4.text(0.06, 0.93, "app.py  |  Motor Matemático de Mínimos Cuadrados en Python (MCO)", fontsize=11, fontweight='bold', color='#FFFFFF')
ax4.text(0.06, 0.895, "Implementación algorítmica sin librerías de caja negra (cálculo explícito con NumPy)", fontsize=9, color='#94A3B8')

code_text = (
    "def calcular_regresion(x_arr, y_arr):\n"
    "    x_v = np.asarray(x_arr, dtype=float)\n"
    "    y_v = np.asarray(y_arr, dtype=float)\n"
    "    n_v = len(x_v)\n\n"
    "    # 1. Sumatorias Discretas\n"
    "    sx, sy   = np.sum(x_v), np.sum(y_v)\n"
    "    sxy, sx2 = np.sum(x_v * y_v), np.sum(x_v**2)\n"
    "    mx, my   = np.mean(x_v), np.mean(y_v)\n\n"
    "    # 2. Resolución de las Ecuaciones de Gauss\n"
    "    den = n_v * sx2 - sx**2\n"
    "    m_v = (n_v * sxy - sx * sy) / den if den != 0 else 0.0\n"
    "    b_v = (sy - m_v * sx) / n_v if den != 0 else my\n\n"
    "    # 3. Vector de Predicciones y Residuos (e = Y - Ŷ)\n"
    "    yp  = m_v * x_v + b_v\n"
    "    res = y_v - yp\n\n"
    "    # 4. Coeficiente de Determinación (R²) y Correlación (r)\n"
    "    sst = np.sum((y_v - my)**2)\n"
    "    ssr = np.sum(res**2)\n"
    "    r2_v = 1.0 - (ssr / sst) if sst != 0 else 0.0\n"
    "    r_v  = np.corrcoef(x_v, y_v)[0, 1] if n_v > 1 else 0.0\n"
    "    steyx_v = np.sqrt(ssr / (n_v - 2)) if n_v > 2 else 0.0\n\n"
    "    return {'m': m_v, 'b': b_v, 'r2': r2_v, 'r': r_v, 'steyx': steyx_v}"
)
ax4.text(0.06, 0.08, code_text, fontsize=9.5, fontfamily='monospace', color='#0F172A', linespacing=1.3)

fig4.savefig(os.path.join(out_dir, "04_Algoritmo_Python_MCO_Blanco.png"), dpi=220, bbox_inches='tight')
plt.close(fig4)
print("4/7 Creado: 04_Algoritmo_Python_MCO_Blanco.png")

# =============================================================================
# 5. TABLA RESUMEN COMPARATIVO EXCEL (FONDO BLANCO, LISTA PARA PEGAR)
# =============================================================================
fig5 = plt.figure(figsize=(11, 7.5), facecolor='#FFFFFF')
ax5 = fig5.add_subplot(111)
ax5.axis('off')

ax5.text(0.50, 0.94, "RESUMEN COMPARATIVO DE LOS 2 MODELOS DE REGRESIÓN (USIL 2026)", fontsize=12, fontweight='bold', color='#002B49', ha='center')
ax5.text(0.50, 0.90, "Hoja 3 del Libro Excel: Vinculación Dinámica mediante Fórmulas Nativas", fontsize=10, color='#475569', ha='center')

cols = ["Indicador / Parámetro", "Fórmula Excel", "Modelo 1 (Costo S/)", "Modelo 2 (Combustible)", "Concordancia"]
x_coords = [0.03, 0.28, 0.50, 0.70, 0.88]

# Encabezado
rect_h = patches.Rectangle((0.02, 0.82), 0.96, 0.06, facecolor='#002B49')
ax5.add_patch(rect_h)
for xc, hc in zip(x_coords, cols):
    ax5.text(xc, 0.84, hc, fontsize=9, fontweight='bold', color='#FFFFFF')

table_rows = [
    ("Variable Predictora (X)", "Rango D7:D29", "Distancia (km)", "Distancia (km)", "100% Exacta"),
    ("Variable Respuesta (Y)", "Rango E7:E29", "Costo Total (S/)", "Combustible (gal)", "100% Exacta"),
    ("Observaciones (n)", "=CONTAR()", "23 rutas", "23 rutas", "100% Exacta"),
    ("Pendiente (m)", "=PENDIENTE()", "S/ 0.3825 / km", "0.1686 gal / km", "100% Exacta"),
    ("Intersección (b)", "=INTERSECCION.EJE()", "-S/ 24.64", "-0.11 gal", "100% Exacta"),
    ("Coef. Determinación (R²)", "=COEFICIENTE.R2()", "85.45%", "81.57%", "100% Exacta"),
    ("Correlación Pearson (r)", "=COEF.DE.CORREL()", "0.9244", "0.9032", "100% Exacta"),
    ("Error Típico Estándar", "=ERROR.TIPICO.XY()", "S/ 68.21", "34.63 gal", "100% Exacta"),
    ("Proyección a 500 km", "=PRONOSTICO.LINEAL()", "S/ 166.60", "84.17 gal", "100% Exacta"),
    ("Proyección a 1,000 km", "=PRONOSTICO.LINEAL()", "S/ 357.84", "168.44 gal", "100% Exacta")
]

for idx, row in enumerate(table_rows):
    yp = 0.75 - idx * 0.068
    bg = '#F8FAFC' if idx % 2 == 1 else '#FFFFFF'
    rect_r = patches.Rectangle((0.02, yp - 0.015), 0.96, 0.06, facecolor=bg, edgecolor='#E2E8F0', linewidth=0.7)
    ax5.add_patch(rect_r)
    for xc, val in zip(x_coords, row):
        fw = 'bold' if xc in [0.03, 0.50, 0.70] else 'normal'
        col = '#0284C7' if xc == 0.28 else ('#16A34A' if xc == 0.88 else '#1E293B')
        ax5.text(xc, yp, val, fontsize=8.5, fontweight=fw, color=col)

fig5.savefig(os.path.join(out_dir, "05_Tabla_Excel_Resumen_Comparativo_Blanco.png"), dpi=220, bbox_inches='tight')
plt.close(fig5)
print("5/7 Creado: 05_Tabla_Excel_Resumen_Comparativo_Blanco.png")

# =============================================================================
# 6. GRÁFICO DESGLOSE DE COSTOS LOGÍSTICOS (TORTA / DONA FONDO BLANCO)
# =============================================================================
fig6, ax6 = plt.subplots(figsize=(8.5, 6), facecolor='#FFFFFF')

pie_vals = [24.64, 214.19, 60.00, 29.88]
pie_labels = [
    'Costo Base de Despacho (S/ 24.64)',
    'Diésel y Kilometraje (S/ 214.19)',
    'Peajes e Imprevistos (S/ 60.00)',
    'Margen Operativo 10% (S/ 29.88)'
]
pie_colors = ['#2563EB', '#0284C7', '#EA580C', '#16A34A']

wedges, texts, autotexts = ax6.pie(
    pie_vals, labels=pie_labels, autopct='%1.1f%%', startangle=140,
    colors=pie_colors, pctdistance=0.75,
    wedgeprops=dict(width=0.45, edgecolor='#FFFFFF', linewidth=2),
    textprops=dict(color="#1E293B", fontsize=9.5)
)
for at in autotexts:
    at.set_color('#FFFFFF')
    at.set_fontweight('bold')
    at.set_fontsize(9.5)

ax6.set_title("Simulación de Flete (560 km - Lima a Trujillo):\nDesglose Porcentual del Costo Cotizado (Total: S/ 328.71)",
              fontsize=11.5, fontweight='bold', color='#0F172A', pad=15)

fig6.savefig(os.path.join(out_dir, "06_Grafico_Desglose_Costos_Torta_Blanco.png"), dpi=220, bbox_inches='tight')
plt.close(fig6)
print("6/7 Creado: 06_Grafico_Desglose_Costos_Torta_Blanco.png")

# =============================================================================
# 7. TARJETA RESUMEN DE KPIS (FONDO BLANCO, PARA INSERTAR AL LADO DE TEXTO)
# =============================================================================
fig7, ax7 = plt.subplots(figsize=(10, 3.2), facecolor='#FFFFFF')
ax7.axis('off')

kpis_boxes = [
    ("PENDIENTE MARGINAL (m)", f"S/ {m1:.4f} / km", "+S/ 38.25 cada 100 km", '#0284C7'),
    ("INTERSECCIÓN BASE (b)", f"-S/ {abs(b1):.2f}", "Ajuste en origen (X=0)", '#16A34A'),
    ("BONDAD DE AJUSTE (R²)", f"{r2_1*100:.2f}%", "Varianza 14.55% (peajes)", '#EA580C'),
    ("CORRELACIÓN PEARSON (r)", f"{r1:.4f}", "Relación directa muy fuerte", '#7C3AED')
]

for idx, (title, val, sub, color) in enumerate(kpis_boxes):
    xp = 0.02 + idx * 0.245
    box = patches.FancyBboxPatch((xp, 0.08), 0.23, 0.84, boxstyle="round,pad=0.03", facecolor='#F8FAFC', edgecolor=color, linewidth=1.5)
    ax7.add_patch(box)
    ax7.text(xp + 0.115, 0.72, title, fontsize=7.5, fontweight='bold', color='#64748B', ha='center')
    ax7.text(xp + 0.115, 0.42, val, fontsize=12, fontweight='bold', color=color, ha='center')
    ax7.text(xp + 0.115, 0.20, sub, fontsize=7.5, color='#475569', ha='center')

fig7.savefig(os.path.join(out_dir, "07_Tarjetas_KPI_Resumen_Blanco.png"), dpi=220, bbox_inches='tight')
plt.close(fig7)
print("7/7 Creado: 07_Tarjetas_KPI_Resumen_Blanco.png")

print("\n¡Las 7 imágenes simples en fondo blanco se han generado exitosamente!")
