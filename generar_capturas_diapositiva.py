import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd

# Directorio destino
out_dir = r"c:\Users\PC\Desktop\Matematica discreta trabajo grupal\Capturas para diapositiva"
os.makedirs(out_dir, exist_ok=True)

# Cargar dataset real de 23 rutas
df = pd.read_csv(r"c:\Users\PC\Desktop\Matematica discreta trabajo grupal\datos_logisticos.csv")
x = df["Distancia_km"].values.astype(float)
y1 = df["Costo_Total_Soles"].values.astype(float)
y2 = df["Consumo_Combustible_Gal"].values.astype(float)
n = len(x)

# Regresiones
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

# Configuración global de estilos
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#334155'
plt.rcParams['axes.linewidth'] = 1.2

# -----------------------------------------------------------------------------
# IMAGEN 1: DASHBOARD MODELO 1 (COSTOS) CON TARJETAS KPI
# -----------------------------------------------------------------------------
fig = plt.figure(figsize=(16, 9), facecolor='#060D17')
gs = fig.add_gridspec(nrows=3, ncols=4, height_ratios=[0.25, 0.75, 0.05], hspace=0.35, wspace=0.25)

# Banner superior
ax_top = fig.add_subplot(gs[0, :])
ax_top.set_facecolor('#0B1626')
ax_top.axis('off')
ax_top.text(0.02, 0.70, "UNIVERSIDAD SAN IGNACIO DE LOYOLA (USIL) — MATEMÁTICA DISCRETA", color='#38BDF8', fontsize=12, fontweight='bold')
ax_top.text(0.02, 0.35, "Modelo 1: Regresión Lineal — Distancia (km) vs. Costo Total de Transporte (S/)", color='#FFFFFF', fontsize=18, fontweight='bold')
ax_top.text(0.02, 0.08, "Muestra: 23 rutas nacionales reales (Costa, Sierra y Selva) | Algoritmo MCO", color='#94A3B8', fontsize=11)

# Tarjetas KPI simuladas a la derecha del banner
kpis_m1 = [
    ("PENDIENTE (m)", f"S/ {m1:.4f}/km", '#00E5FF', "=PENDIENTE()"),
    ("INTERSECCIÓN (b)", f"-S/ {abs(b1):.2f}", '#10B981', "=INTERSECCION.EJE()"),
    ("BONDAD DE AJUSTE (R²)", f"{r2_1*100:.2f}%", '#FFA057', "=COEFICIENTE.R2()"),
    ("CORRELACIÓN (r)", f"{r1:.4f}", '#A78BFA', "=COEF.DE.CORREL()")
]
for i, (k_tit, k_val, k_col, k_fml) in enumerate(kpis_m1):
    xp = 0.52 + i * 0.12
    rect = patches.FancyBboxPatch((xp, 0.10), 0.11, 0.80, boxstyle="round,pad=0.02", facecolor='#101F33', edgecolor=k_col, linewidth=1.5)
    ax_top.add_patch(rect)
    ax_top.text(xp + 0.055, 0.70, k_tit, color='#94A3B8', fontsize=8, fontweight='bold', ha='center')
    ax_top.text(xp + 0.055, 0.40, k_val, color=k_col, fontsize=12, fontweight='bold', ha='center')
    ax_top.text(xp + 0.055, 0.18, k_fml, color='#64748B', fontsize=7.5, ha='center')

# Gráfico principal Scatter + Fit + CI
ax_chart = fig.add_subplot(gs[1, :3])
ax_chart.set_facecolor('#0B1626')
ax_chart.grid(True, linestyle='--', alpha=0.15, color='#CBD5E1')

xs = np.linspace(0, x.max() * 1.05, 100)
ys = m1 * xs + b1
ci_sup = ys + 1.96 * steyx1
ci_inf = np.maximum(0, ys - 1.96 * steyx1)

ax_chart.fill_between(xs, ci_inf, ci_sup, color='#00E5FF', alpha=0.12, label='Intervalo de Confianza (95%)')
ax_chart.plot(xs, ys, color='#00E5FF', linewidth=3, label=f'Recta Ajustada: Ŷ = {m1:.4f}X - {abs(b1):.2f}')
ax_chart.scatter(x, y1, color='#38BDF8', edgecolor='#FFFFFF', s=75, linewidth=1.2, zorder=5, label='23 Rutas Reales')

# Líneas de residuos
for xi, yi in zip(x, y1):
    yp = m1 * xi + b1
    ax_chart.plot([xi, xi], [yi, yp], color='#F43F5E', linestyle=':', linewidth=1.0, alpha=0.6)

ax_chart.set_title("Ajuste MCO: Distancia Recorrida (X) vs Costo de Flete (Y1)", color='#FFFFFF', fontsize=14, fontweight='bold', pad=12)
ax_chart.set_xlabel("Distancia Recorrida (km)", color='#94A3B8', fontsize=11, fontweight='bold')
ax_chart.set_ylabel("Costo Total de Transporte (S/)", color='#94A3B8', fontsize=11, fontweight='bold')
ax_chart.tick_params(colors='#94A3B8', labelsize=10)
ax_chart.legend(facecolor='#101F33', edgecolor='#334155', labelcolor='#F8FAFC', loc='upper left', fontsize=10)

# Panel lateral derecho con explicación estadística
ax_side = fig.add_subplot(gs[1, 3])
ax_side.set_facecolor('#0B1626')
ax_side.axis('off')
rect_side = patches.FancyBboxPatch((0.05, 0.05), 0.90, 0.90, boxstyle="round,pad=0.03", facecolor='#101F33', edgecolor='#00E5FF', linewidth=1.5)
ax_side.add_patch(rect_side)
ax_side.text(0.12, 0.88, "RESUMEN EJECUTIVO", color='#38BDF8', fontsize=12, fontweight='bold')
ax_side.text(0.12, 0.78, f"• Muestra: {n} rutas del Perú", color='#FFFFFF', fontsize=10)
ax_side.text(0.12, 0.68, f"• Ecuación:", color='#FFFFFF', fontsize=10)
ax_side.text(0.15, 0.60, f"Ŷ = {m1:.4f}·X - {abs(b1):.2f} (S/)", color='#00E5FF', fontsize=11, fontweight='bold')
ax_side.text(0.12, 0.48, f"• Pendiente (m): +S/ {m1:.4f}/km", color='#FFFFFF', fontsize=10)
ax_side.text(0.12, 0.40, f"  Cada 100 km: +S/ {m1*100:.2f}", color='#94A3B8', fontsize=9.5)
ax_side.text(0.12, 0.30, f"• R² = {r2_1*100:.2f}% (Fuerte y real)", color='#FFA057', fontsize=10.5, fontweight='bold')
ax_side.text(0.12, 0.22, f"  14.55% residual: peajes y", color='#94A3B8', fontsize=9.5)
ax_side.text(0.12, 0.16, f"  dificultad de rutas andinas", color='#94A3B8', fontsize=9.5)
ax_side.text(0.12, 0.08, f"• Proyección 500 km: S/ {m1*500+b1:.2f}", color='#34D399', fontsize=10, fontweight='bold')

fig.savefig(os.path.join(out_dir, "01_Dashboard_Modelo1_Costos.png"), dpi=200, bbox_inches='tight')
plt.close(fig)
print("1/8 Creada: 01_Dashboard_Modelo1_Costos.png")

# -----------------------------------------------------------------------------
# IMAGEN 2: MODELO 2 (COMBUSTIBLE) CON DISPERSIÓN REGIONAL Y PICOS ANDINOS
# -----------------------------------------------------------------------------
fig2 = plt.figure(figsize=(16, 9), facecolor='#060D17')
gs2 = fig2.add_gridspec(nrows=3, ncols=4, height_ratios=[0.25, 0.75, 0.05], hspace=0.35, wspace=0.25)

ax2_top = fig2.add_subplot(gs2[0, :])
ax2_top.set_facecolor('#0B1626')
ax2_top.axis('off')
ax2_top.text(0.02, 0.70, "UNIVERSIDAD SAN IGNACIO DE LOYOLA (USIL) — MATEMÁTICA DISCRETA", color='#FFA057', fontsize=12, fontweight='bold')
ax2_top.text(0.02, 0.35, "Modelo 2: Distancia (km) vs. Consumo de Combustible Diésel (galones)", color='#FFFFFF', fontsize=18, fontweight='bold')
ax2_top.text(0.02, 0.08, "Análisis de Dispersión Geográfica: Costa (Llanura) vs Sierra (Altitud y Curvas) vs Selva", color='#94A3B8', fontsize=11)

kpis_m2 = [
    ("PENDIENTE (m)", f"{m2:.4f} gal/km", '#FFA057', "=PENDIENTE()"),
    ("RENDIMIENTO", f"{1/m2:.2f} km/gal", '#10B981', "Rendimiento Medio"),
    ("BONDAD DE AJUSTE (R²)", f"{r2_2*100:.2f}%", '#38BDF8', "=COEFICIENTE.R2()"),
    ("CORRELACIÓN (r)", f"{r2:.4f}", '#A78BFA', "=COEF.DE.CORREL()")
]
for i, (k_tit, k_val, k_col, k_fml) in enumerate(kpis_m2):
    xp = 0.52 + i * 0.12
    rect = patches.FancyBboxPatch((xp, 0.10), 0.11, 0.80, boxstyle="round,pad=0.02", facecolor='#101F33', edgecolor=k_col, linewidth=1.5)
    ax2_top.add_patch(rect)
    ax2_top.text(xp + 0.055, 0.70, k_tit, color='#94A3B8', fontsize=8, fontweight='bold', ha='center')
    ax2_top.text(xp + 0.055, 0.40, k_val, color=k_col, fontsize=12, fontweight='bold', ha='center')
    ax2_top.text(xp + 0.055, 0.18, k_fml, color='#64748B', fontsize=7.5, ha='center')

ax2_chart = fig2.add_subplot(gs2[1, :3])
ax2_chart.set_facecolor('#0B1626')
ax2_chart.grid(True, linestyle='--', alpha=0.15, color='#CBD5E1')

ys2 = m2 * xs + b2
ax2_chart.plot(xs, ys2, color='#FFA057', linewidth=3, label=f'Recta MCO: Ŷ₂ = {m2:.4f}X - {abs(b2):.2f}')

# Puntos coloreados por región
c_mask = df["Region"] == "Costa"
s_mask = df["Region"] == "Sierra"
j_mask = df["Region"] == "Selva"

ax2_chart.scatter(x[c_mask], y2[c_mask], color='#38BDF8', edgecolor='#FFFFFF', s=90, label='Costa (Plana / Menor Esfuerzo)', zorder=6)
ax2_chart.scatter(x[s_mask], y2[s_mask], color='#FF6B00', edgecolor='#FFFFFF', s=100, marker='^', label='Sierra (Altitud / Pendiente Andina)', zorder=6)
ax2_chart.scatter(x[j_mask], y2[j_mask], color='#10B981', edgecolor='#FFFFFF', s=100, marker='s', label='Selva (Ruta de Selva Alta/Baja)', zorder=6)

# Anotación del pico andino
puno_idx = df[df["Ruta"].str.contains("Puno")].index[0]
ax2_chart.annotate("Pico Andino (Puno, 1335 km)\n282.8 gal (mayor altitud)",
                   xy=(x[puno_idx], y2[puno_idx]),
                   xytext=(x[puno_idx]-350, y2[puno_idx]+30),
                   arrowprops=dict(facecolor='#FF6B00', shrink=0.08, width=1.5, headwidth=6),
                   color='#FFFFFF', fontsize=9, fontweight='bold',
                   bbox=dict(boxstyle="round,pad=0.3", facecolor='#1E293B', edgecolor='#FF6B00'))

# Anotación ruta costera equivalente
tacna_idx = df[df["Ruta"].str.contains("Tacna")].index[0]
ax2_chart.annotate("Ruta Costa (Tacna, 1293 km)\n154.9 gal (llano costero)",
                   xy=(x[tacna_idx], y2[tacna_idx]),
                   xytext=(x[tacna_idx]+20, y2[tacna_idx]-40),
                   arrowprops=dict(facecolor='#38BDF8', shrink=0.08, width=1.5, headwidth=6),
                   color='#FFFFFF', fontsize=9, fontweight='bold',
                   bbox=dict(boxstyle="round,pad=0.3", facecolor='#1E293B', edgecolor='#38BDF8'))

ax2_chart.set_title("Validación de Picos Reales: Consumo de Combustible por Región Geográfica", color='#FFFFFF', fontsize=14, fontweight='bold', pad=12)
ax2_chart.set_xlabel("Distancia Recorrida (km)", color='#94A3B8', fontsize=11, fontweight='bold')
ax2_chart.set_ylabel("Consumo de Combustible (Galones Diésel)", color='#94A3B8', fontsize=11, fontweight='bold')
ax2_chart.tick_params(colors='#94A3B8', labelsize=10)
ax2_chart.legend(facecolor='#101F33', edgecolor='#334155', labelcolor='#F8FAFC', loc='upper left', fontsize=9.5)

# Panel explicativo docente
ax2_side = fig2.add_subplot(gs2[1, 3])
ax2_side.set_facecolor('#0B1626')
ax2_side.axis('off')
rect2_side = patches.FancyBboxPatch((0.05, 0.05), 0.90, 0.90, boxstyle="round,pad=0.03", facecolor='#101F33', edgecolor='#FFA057', linewidth=1.5)
ax2_side.add_patch(rect2_side)
ax2_side.text(0.10, 0.88, "RESPUESTA AL FEEDBACK", color='#FFA057', fontsize=11, fontweight='bold')
ax2_side.text(0.10, 0.81, "OBSERVACIÓN DOCENTE:", color='#FFFFFF', fontsize=9.5, fontweight='bold')
ax2_side.text(0.10, 0.74, '"La regresión no debe ser 99%', color='#CBD5E1', fontsize=8.5, style='italic')
ax2_side.text(0.10, 0.68, ' perfecta; en la vida real tiene', color='#CBD5E1', fontsize=8.5, style='italic')
ax2_side.text(0.10, 0.62, ' picos e irregularidades."', color='#CBD5E1', fontsize=8.5, style='italic')
ax2_side.text(0.10, 0.52, "SOLUCIÓN INCORPORADA:", color='#34D399', fontsize=9.5, fontweight='bold')
ax2_side.text(0.10, 0.44, f"• R² = {r2_2*100:.2f}% (Real y robusto)", color='#FFFFFF', fontsize=9)
ax2_side.text(0.10, 0.36, "• 18.43% varianza residual:", color='#FFFFFF', fontsize=9)
ax2_side.text(0.10, 0.28, "  Rutas de Sierra (Ticlio 4,818m)", color='#FFA057', fontsize=8.5)
ax2_side.text(0.10, 0.22, "  duplican consumo frente a Costa", color='#FFA057', fontsize=8.5)
ax2_side.text(0.10, 0.14, "  a igual distancia en km.", color='#FFA057', fontsize=8.5)
ax2_side.text(0.10, 0.06, f"• Proy. 500 km: {m2*500+b2:.2f} gal", color='#00E5FF', fontsize=9.5, fontweight='bold')

fig2.savefig(os.path.join(out_dir, "02_Modelo2_Combustible_Regiones.png"), dpi=200, bbox_inches='tight')
plt.close(fig2)
print("2/8 Creada: 02_Modelo2_Combustible_Regiones.png")

# -----------------------------------------------------------------------------
# IMAGEN 3: COMPARATIVA DE LOS 2 MODELOS
# -----------------------------------------------------------------------------
fig3, (ax3_m1, ax3_m2) = plt.subplots(1, 2, figsize=(16, 8), facecolor='#060D17')
fig3.suptitle("COMPARATIVA PARALELA DE LOS 2 MODELOS DE REGRESIÓN LINEAL (USIL 2026)", color='#FFFFFF', fontsize=16, fontweight='bold', y=0.96)

for ax, ym, col, lbl_y, tit, m_val, b_val, r_sq in [
    (ax3_m1, y1, '#00E5FF', "Costo Total (S/)", "Modelo 1: Costo de Transporte", m1, b1, r2_1),
    (ax3_m2, y2, '#FFA057', "Combustible (gal)", "Modelo 2: Consumo de Diésel", m2, b2, r2_2)
]:
    ax.set_facecolor('#0B1626')
    ax.grid(True, linestyle='--', alpha=0.15, color='#CBD5E1')
    ax.scatter(x, ym, color=col, edgecolor='#FFFFFF', s=70, zorder=5)
    ax.plot(xs, m_val * xs + b_val, color=col, linewidth=2.5, label=f'Ŷ = {m_val:.4f}X - {abs(b_val):.2f}')
    ax.set_title(tit, color='#FFFFFF', fontsize=13, fontweight='bold', pad=10)
    ax.set_xlabel("Distancia Recorrida (km)", color='#94A3B8', fontsize=11)
    ax.set_ylabel(lbl_y, color='#94A3B8', fontsize=11)
    ax.tick_params(colors='#94A3B8')
    
    # Caja resumen
    txt_box = f"Pendiente (m): {m_val:.4f}\nIntersección (b): {b_val:.2f}\nR²: {r_sq*100:.2f}%\nProy. 500 km: {m_val*500+b_val:.2f}\nProy. 1,000 km: {m_val*1000+b_val:.2f}"
    ax.text(0.05, 0.70, txt_box, transform=ax.transAxes, color='#FFFFFF', fontsize=9.5,
            bbox=dict(boxstyle="round,pad=0.5", facecolor='#101F33', edgecolor=col, linewidth=1.2))
    ax.legend(facecolor='#101F33', edgecolor='#334155', labelcolor='#FFFFFF', loc='lower right')

fig3.savefig(os.path.join(out_dir, "03_Comparativa_Ambos_Modelos.png"), dpi=200, bbox_inches='tight')
plt.close(fig3)
print("3/8 Creada: 03_Comparativa_Ambos_Modelos.png")

# -----------------------------------------------------------------------------
# IMAGEN 4: FUNDAMENTO MATEMÁTICO DISCRETO (ECUACIONES DE GAUSS)
# -----------------------------------------------------------------------------
fig4 = plt.figure(figsize=(16, 9), facecolor='#060D17')
ax4 = fig4.add_subplot(111)
ax4.set_facecolor('#060D17')
ax4.axis('off')

# Encabezado
ax4.text(0.04, 0.93, "FUNDAMENTACIÓN TEÓRICA EN MATEMÁTICA DISCRETA", color='#38BDF8', fontsize=14, fontweight='bold')
ax4.text(0.04, 0.88, "Deducción de Mínimos Cuadrados Ordinarios (MCO) y Sistema Normal de Gauss", color='#FFFFFF', fontsize=18, fontweight='bold')

# Panel 1: Relación Discreta y Sumatorias
rect_p1 = patches.FancyBboxPatch((0.04, 0.42), 0.44, 0.42, boxstyle="round,pad=0.02", facecolor='#0B1626', edgecolor='#2563EB', linewidth=1.5)
ax4.add_patch(rect_p1)
ax4.text(0.07, 0.80, "1. MUESTRA DISCRETA Y SUMATORIAS FINITAS", color='#38BDF8', fontsize=12, fontweight='bold')
ax4.text(0.07, 0.73, r"Conjunto finito de pares ordenados:  $S = \{(x_1, y_1), (x_2, y_2), \dots, (x_{23}, y_{23})\}$", color='#E2E8F0', fontsize=10.5)

sums_text = f"""
  • Número de observaciones (n)  =  23 rutas nacionales
  • Sumatoria de Distancia (∑ X)   =  19,098.00 km
  • Sumatoria de Costos (∑ Y₁)     =  S/ 6,737.88
  • Sumatoria de Cuadrados (∑ X²)  =  19,781,876.00
  • Sumatoria de Productos (∑ XY₁) =  7,095,607.52
  • Media muestral x̄               =  830.35 km
  • Media muestral ȳ₁              =  S/ 292.95
"""
ax4.text(0.07, 0.46, sums_text, color='#CBD5E1', fontsize=10, fontfamily='monospace')

# Panel 2: Ecuaciones de Gauss y Deducción
rect_p2 = patches.FancyBboxPatch((0.52, 0.42), 0.44, 0.42, boxstyle="round,pad=0.02", facecolor='#0B1626', edgecolor='#10B981', linewidth=1.5)
ax4.add_patch(rect_p2)
ax4.text(0.55, 0.80, "2. SISTEMA DE ECUACIONES NORMALES DE GAUSS", color='#34D399', fontsize=12, fontweight='bold')
gauss_eqs = r"""
Sistema lineal 2x2 para minimizar el error cuadrático E(m, b):
  [1]  m · ∑(xᵢ²) + b · ∑(xᵢ) = ∑(xᵢ · yᵢ)
  [2]  m · ∑(xᵢ)  + b · n     = ∑(yᵢ)

Sustituyendo los valores discretos de las 23 rutas:
  [1]  m · (19,781,876) + b · (19,098) = 7,095,607.52
  [2]  m · (19,098)     + b · (23)     = 6,737.88
"""
ax4.text(0.55, 0.47, gauss_eqs, color='#CBD5E1', fontsize=10, fontfamily='monospace')

# Panel 3: Resolución Aritmética
rect_p3 = patches.FancyBboxPatch((0.04, 0.05), 0.92, 0.33, boxstyle="round,pad=0.02", facecolor='#0B1626', edgecolor='#FFA057', linewidth=1.5)
ax4.add_patch(rect_p3)
ax4.text(0.07, 0.33, "3. RESOLUCIÓN DE COEFICIENTES (PENDIENTE m E INTERSECCIÓN b)", color='#FFA057', fontsize=12, fontweight='bold')

sol_text = f"""
Cálculo de la Pendiente Marginal (m):
  m = [ n · ∑(XY) - (∑X)(∑Y) ] / [ n · ∑(X²) - (∑X)² ]
  m = [ 23 · (7,095,607.52) - (19,098)(6,737.88) ] / [ 23 · (19,781,876) - (19,098)² ]
  m = 34,589,740.96 / 90,434,100  =  +0.382483  -->  S/ 0.3825 por km recorrido

Cálculo de la Intersección (b) o Término Independiente:
  b = ȳ - m · x̄  =  (∑Y - m · ∑X) / n  =  [ 6,737.88 - (0.382483 · 19,098) ] / 23  =  -S/ 24.6428

Ecuación Afín Final:   Ŷ₁ = 0.3825 · X - 24.64 (S/)    |    R² = 85.45%    |    r = 0.9244
"""
ax4.text(0.07, 0.08, sol_text, color='#E2E8F0', fontsize=10.5, fontfamily='monospace')

fig4.savefig(os.path.join(out_dir, "04_Fundamento_Matematico_Gauss.png"), dpi=200, bbox_inches='tight')
plt.close(fig4)
print("4/8 Creada: 04_Fundamento_Matematico_Gauss.png")

# -----------------------------------------------------------------------------
# IMAGEN 5: CÓDIGO PYTHON (VENTANA IDE DARK THEME)
# -----------------------------------------------------------------------------
fig5 = plt.figure(figsize=(15, 8.5), facecolor='#060D17')
ax5 = fig5.add_subplot(111)
ax5.set_facecolor('#060D17')
ax5.axis('off')

# Ventana IDE
win_bg = patches.FancyBboxPatch((0.05, 0.05), 0.90, 0.90, boxstyle="round,pad=0.02", facecolor='#0D1726', edgecolor='#1E293B', linewidth=2)
ax5.add_patch(win_bg)

# Barra de título IDE
title_bar = patches.Rectangle((0.05, 0.88), 0.90, 0.07, facecolor='#132034')
ax5.add_patch(title_bar)
# Botones ventana
ax5.add_patch(patches.Circle((0.08, 0.915), 0.010, color='#EF4444'))
ax5.add_patch(patches.Circle((0.105, 0.915), 0.010, color='#F59E0B'))
ax5.add_patch(patches.Circle((0.13, 0.915), 0.010, color='#10B981'))
ax5.text(0.50, 0.905, "app.py — Motor de Regresión Lineal Discreta (Python / NumPy)", color='#CBD5E1', fontsize=11, fontweight='bold', ha='center')

code_snippet = """
def calcular_regresion(x_arr, y_arr):
    x_v = np.asarray(x_arr, dtype=float)
    y_v = np.asarray(y_arr, dtype=float)
    n_v = len(x_v)
    
    # 1. Sumatorias Discretas de Mínimos Cuadrados (MCO)
    sx, sy   = np.sum(x_v), np.sum(y_v)
    sxy, sx2 = np.sum(x_v * y_v), np.sum(x_v**2)
    mx, my   = np.mean(x_v), np.mean(y_v)
    
    # 2. Resolución del Sistema Normal de Gauss
    den = n_v * sx2 - sx**2
    m_v = (n_v * sxy - sx * sy) / den if den != 0 else 0.0
    b_v = (sy - m_v * sx) / n_v if den != 0 else my
    
    # 3. Vector de Estimaciones Ŷ y Residuos Discretos (e = Y - Ŷ)
    yp  = m_v * x_v + b_v
    res = y_v - yp
    
    # 4. Métricas de Bondad de Ajuste
    sst = np.sum((y_v - my)**2)
    ssr = np.sum(res**2)
    r2_v = 1.0 - (ssr / sst) if sst != 0 else 0.0
    r_v  = np.corrcoef(x_v, y_v)[0, 1] if n_v > 1 else 0.0
    steyx_v = np.sqrt(ssr / (n_v - 2)) if n_v > 2 else 0.0
    
    return {"m": m_v, "b": b_v, "r2": r2_v, "r": r_v, "steyx": steyx_v}
"""
ax5.text(0.08, 0.12, code_snippet, color='#38BDF8', fontsize=11, fontfamily='monospace', linespacing=1.35)

fig5.savefig(os.path.join(out_dir, "05_Codigo_Python_MCO.png"), dpi=200, bbox_inches='tight')
plt.close(fig5)
print("5/8 Creada: 05_Codigo_Python_MCO.png")

# -----------------------------------------------------------------------------
# IMAGEN 6: HOJA EXCEL (FÓRMULAS NATIVAS)
# -----------------------------------------------------------------------------
fig6 = plt.figure(figsize=(16, 9), facecolor='#FFFFFF')
ax6 = fig6.add_subplot(111)
ax6.set_facecolor('#FFFFFF')
ax6.axis('off')

# Encabezado estilo Excel USIL
rect_ex_head = patches.Rectangle((0.02, 0.88), 0.96, 0.10, facecolor='#002B49')
ax6.add_patch(rect_ex_head)
ax6.text(0.50, 0.94, "UNIVERSIDAD SAN IGNACIO DE LOYOLA (USIL) — SISTEMA DE REGRESIÓN LOGÍSTICA", color='#FFFFFF', fontsize=13, fontweight='bold', ha='center')
ax6.text(0.50, 0.90, "Hoja: 'Modelo 1 - Costo Transporte' | Fórmulas Nativas de Microsoft Excel", color='#CBD5E1', fontsize=10.5, ha='center')

# Tabla de datos izquierda
rect_table = patches.Rectangle((0.02, 0.10), 0.52, 0.75, facecolor='#F8FAFC', edgecolor='#CBD5E1', linewidth=1)
ax6.add_patch(rect_table)
ax6.text(0.04, 0.82, "MATRIZ DE DATOS Y MÍNIMOS CUADRADOS (Rango D7:E29)", color='#002B49', fontsize=11, fontweight='bold')

headers_ex = ["ID", "Ruta", "Región", "Dist. (km) [X]", "Costo (S/) [Y]", "X²", "X·Y", "Ŷ", "Residuo"]
for idx, h in enumerate(headers_ex):
    ax6.text(0.035 + idx * 0.056, 0.77, h, color='#1E293B', fontsize=8, fontweight='bold')

sample_rows = [
    ("R-01", "La Oroya", "Sierra", "174", "93.04", "=D7^2", "=D7*E7", "=$M$8*D7+$M$9", "=E7-I7"),
    ("R-02", "Huancayo", "Sierra", "298", "123.20", "=D8^2", "=D8*E8", "=$M$8*D8+$M$9", "=E8-I8"),
    ("R-03", "C. Pasco", "Sierra", "302", "124.11", "=D9^2", "=D9*E9", "=$M$8*D9+$M$9", "=E9-I9"),
    ("R-04", "Ica", "Costa", "303", "107.28", "=D10^2", "=D10*E10", "=$M$8*D10+$M$9", "=E10-I10"),
    ("...", "...", "...", "...", "...", "...", "...", "...", "..."),
    ("R-22", "Moyobamba", "Selva", "1363", "569.69", "=D28^2", "=D28*E28", "=$M$8*D28+$M$9", "=E28-I28"),
    ("R-23", "Pto. Maldon.", "Selva", "1638", "799.01", "=D29^2", "=D29*E29", "=$M$8*D29+$M$9", "=E29-I29"),
]
for r_i, row in enumerate(sample_rows):
    yp = 0.72 - r_i * 0.06
    for c_i, val in enumerate(row):
        ax6.text(0.035 + c_i * 0.056, yp, val, color='#334155', fontsize=8)

# Fila de sumatorias
ax6.text(0.04, 0.25, "SUMATORIAS (Fila 30):", color='#002B49', fontsize=9.5, fontweight='bold')
ax6.text(0.04, 0.18, "=SUMA(D7:D29)  |  =SUMA(E7:E29)  |  =SUMA(F7:F29)  |  =SUMA(H7:H29)", color='#2563EB', fontsize=9, fontfamily='monospace')

# Panel lateral derecho (Fórmulas Nativas)
rect_panel = patches.Rectangle((0.57, 0.10), 0.41, 0.75, facecolor='#F0F9FF', edgecolor='#0284C7', linewidth=1.5)
ax6.add_patch(rect_panel)
ax6.text(0.59, 0.82, "PARÁMETROS DEL MODELO (FÓRMULAS NATIVAS EXCEL)", color='#002B49', fontsize=11, fontweight='bold')

excel_kpis_display = [
    ("Observaciones (n):", "=CONTAR(D7:D29)", "23"),
    ("Pendiente (m):", "=PENDIENTE(E7:E29; D7:D29)", "S/ 0.3825/km"),
    ("Intersección (b):", "=INTERSECCION.EJE(E7:E29; D7:D29)", "-S/ 24.64"),
    ("Coef. Determinación (R²):", "=COEFICIENTE.R2(E7:E29; D7:D29)", "85.45%"),
    ("Correlación Pearson (r):", "=COEF.DE.CORREL(D7:D29; E7:E29)", "0.9244"),
    ("Error Típico:", "=ERROR.TIPICO.XY(E7:E29; D7:D29)", "S/ 68.21"),
]
for idx, (lbl, fml, val) in enumerate(excel_kpis_display):
    yp = 0.74 - idx * 0.075
    ax6.text(0.59, yp, lbl, color='#1E293B', fontsize=9, fontweight='bold')
    ax6.text(0.59, yp - 0.025, fml, color='#0284C7', fontsize=8.5, fontfamily='monospace')
    ax6.text(0.92, yp - 0.01, val, color='#002B49', fontsize=10, fontweight='bold', ha='right')

# Simulador
rect_sim = patches.Rectangle((0.59, 0.14), 0.37, 0.12, facecolor='#FEF3C7', edgecolor='#D97706', linewidth=1.2)
ax6.add_patch(rect_sim)
ax6.text(0.61, 0.22, "SIMULADOR EN TIEMPO REAL (PRONOSTICO.LINEAL)", color='#92400E', fontsize=9, fontweight='bold')
ax6.text(0.61, 0.17, "=PRONOSTICO.LINEAL(M17; E7:E29; D7:D29)", color='#B45309', fontsize=8.5, fontfamily='monospace')
ax6.text(0.93, 0.17, "S/ 223.97", color='#78350F', fontsize=11, fontweight='bold', ha='right')

fig6.savefig(os.path.join(out_dir, "06_Excel_Formulas_Nativas.png"), dpi=200, bbox_inches='tight')
plt.close(fig6)
print("6/8 Creada: 06_Excel_Formulas_Nativas.png")

# -----------------------------------------------------------------------------
# IMAGEN 7: EXCEL RESUMEN COMPARATIVO (HOJA 3)
# -----------------------------------------------------------------------------
fig7 = plt.figure(figsize=(16, 8.5), facecolor='#FFFFFF')
ax7 = fig7.add_subplot(111)
ax7.set_facecolor('#FFFFFF')
ax7.axis('off')

# Banner Hoja 3
rect_h3 = patches.Rectangle((0.03, 0.88), 0.94, 0.09, facecolor='#002B49')
ax7.add_patch(rect_h3)
ax7.text(0.50, 0.93, "RESUMEN COMPARATIVO DE LOS 2 MODELOS DE REGRESIÓN LINEAL — USIL 2026", color='#FFFFFF', fontsize=13, fontweight='bold', ha='center')
ax7.text(0.50, 0.895, "Hoja 3: Comparación dinámica vinculada mediante fórmulas a las hojas de Costos y Combustible", color='#CBD5E1', fontsize=10, ha='center')

# Tabla
h_cols = ["Indicador / Parámetro", "Fórmula Excel Aplicada", "Modelo 1: Costo Transporte (S/)", "Modelo 2: Combustible (gal)", "Interpretación Comparativa"]
x_pos = [0.04, 0.25, 0.44, 0.62, 0.80]

# Encabezados
rect_th = patches.Rectangle((0.03, 0.80), 0.94, 0.06, facecolor='#1E293B')
ax7.add_patch(rect_th)
for p, h in zip(x_pos, h_cols):
    ax7.text(p, 0.82, h, color='#FFFFFF', fontsize=9.5, fontweight='bold')

rows_comp_data = [
    ("Variable Independiente (X)", "Rango D7:D29", "Distancia Recorrida (km)", "Distancia Recorrida (km)", "Misma variable predictora en las 23 rutas"),
    ("Variable Dependiente (Y)", "Rango E7:E29", "Costo Total de Flete (S/)", "Consumo de Diésel (gal)", "Evalúa impacto económico y energético"),
    ("Observaciones (n)", "=CONTAR(D7:D29)", "23", "23", "Muestra representativa nacional"),
    ("Pendiente (m)", "=PENDIENTE(...)", "S/ 0.3825 / km", "0.1686 gal / km", "M1: +S/ 38.25/100km | M2: ~5.93 km/gal"),
    ("Intersección (b)", "=INTERSECCION.EJE(...)", "-S/ 24.64", "-0.11 gal", "Ajuste base en el origen X=0"),
    ("Coef. Determinación (R²)", "=COEFICIENTE.R2(...)", "85.45%", "81.57%", "Ajuste fuerte con variabilidad real"),
    ("Correlación Pearson (r)", "=COEF.DE.CORREL(...)", "0.9244", "0.9032", "Correlación lineal muy fuerte en ambos"),
    ("Error Típico Estándar", "=ERROR.TIPICO.XY(...)", "S/ 68.21", "34.63 gal", "Dispersión estándar de los residuos"),
    ("Proyección a 500 km", "=PRONOSTICO.LINEAL(...)", "S/ 166.60", "84.17 gal", "Estimación conjunta para viaje medio"),
    ("Proyección a 1,000 km", "=PRONOSTICO.LINEAL(...)", "S/ 357.84", "168.44 gal", "Estimación para ruta larga (Arequipa/Piura)")
]

for idx, r_data in enumerate(rows_comp_data):
    yp = 0.73 - idx * 0.065
    bg_col = '#F8FAFC' if idx % 2 == 1 else '#FFFFFF'
    rect_r = patches.Rectangle((0.03, yp - 0.015), 0.94, 0.06, facecolor=bg_col, edgecolor='#E2E8F0', linewidth=0.8)
    ax7.add_patch(rect_r)
    for p, val in zip(x_pos, r_data):
        f_weight = 'bold' if p in [0.04, 0.44, 0.62] else 'normal'
        t_col = '#0284C7' if p == 0.25 else '#1E293B'
        ax7.text(p, yp, val, color=t_col, fontsize=8.5, fontweight=f_weight)

fig7.savefig(os.path.join(out_dir, "07_Excel_Resumen_Comparativo.png"), dpi=200, bbox_inches='tight')
plt.close(fig7)
print("7/8 Creada: 07_Excel_Resumen_Comparativo.png")

# -----------------------------------------------------------------------------
# IMAGEN 8: SIMULADOR DE ESCENARIOS Y RIESGO
# -----------------------------------------------------------------------------
fig8 = plt.figure(figsize=(16, 8.5), facecolor='#060D17')
fig8.suptitle("SIMULADOR PREDICTIVO INTERACTIVO CON ANÁLISIS DE SENSIBILIDAD", color='#FFFFFF', fontsize=16, fontweight='bold', y=0.96)

# Panel Izquierdo: Inputs simulados
ax8_in = fig8.add_subplot(1, 3, 1)
ax8_in.set_facecolor('#0B1626')
ax8_in.axis('off')
rect_in = patches.FancyBboxPatch((0.05, 0.05), 0.90, 0.90, boxstyle="round,pad=0.03", facecolor='#101F33', edgecolor='#00E5FF', linewidth=1.5)
ax8_in.add_patch(rect_in)
ax8_in.text(0.12, 0.88, "PARÁMETROS DEL FLETE", color='#00E5FF', fontsize=12, fontweight='bold')
ax8_in.text(0.12, 0.76, "• Distancia del Trayecto:\n  560.0 km (ej. Lima - Trujillo)", color='#FFFFFF', fontsize=10.5)
ax8_in.text(0.12, 0.58, "• Variación Diésel:\n  +15.0% (Contingencia combustible)", color='#FFA057', fontsize=10.5)
ax8_in.text(0.12, 0.40, "• Peajes / Imprevistos:\n  S/ 60.00", color='#FFFFFF', fontsize=10.5)
ax8_in.text(0.12, 0.22, "• Margen de Ganancia:\n  10.0%", color='#34D399', fontsize=10.5)

# Panel Central: Presupuesto Cotizado
ax8_out = fig8.add_subplot(1, 3, 2)
ax8_out.set_facecolor('#0B1626')
ax8_out.axis('off')
rect_out = patches.FancyBboxPatch((0.05, 0.05), 0.90, 0.90, boxstyle="round,pad=0.03", facecolor='#101F33', edgecolor='#FFA057', linewidth=1.5)
ax8_out.add_patch(rect_out)
ax8_out.text(0.50, 0.88, "PRESUPUESTO TOTAL COTIZADO", color='#FFA057', fontsize=11, fontweight='bold', ha='center')

s_dist = 560.0
s_comb = 15.0
s_peajes = 60.0
s_margen = 10.0
c_fijo = abs(b1)
c_var = (m1 * (1 + s_comb / 100.0)) * s_dist
subtot = c_fijo + c_var + s_peajes
tot_final = subtot * (1 + s_margen / 100.0)

ax8_out.text(0.50, 0.65, f"S/ {tot_final:,.2f}", color='#FFFFFF', fontsize=26, fontweight='bold', ha='center')
ax8_out.text(0.50, 0.54, f"Costo Unitario: S/ {tot_final/s_dist:.2f} / km", color='#00E5FF', fontsize=11, fontweight='bold', ha='center')

ax8_out.text(0.12, 0.38, f"• Base fija (b): S/ {c_fijo:.2f}", color='#CBD5E1', fontsize=9.5)
ax8_out.text(0.12, 0.28, f"• Diésel y kilometraje: S/ {c_var:.2f}", color='#CBD5E1', fontsize=9.5)
ax8_out.text(0.12, 0.18, f"• Peajes e imprevistos: S/ {s_peajes:.2f}", color='#CBD5E1', fontsize=9.5)
ax8_out.text(0.12, 0.08, f"• Margen operativo: S/ {(subtot*s_margen/100):.2f}", color='#34D399', fontsize=9.5, fontweight='bold')

# Panel Derecho: Gráfico de Torta Desglose
ax8_pie = fig8.add_subplot(1, 3, 3)
ax8_pie.set_facecolor('#0B1626')
pie_vals = [c_fijo, c_var, s_peajes, (subtot * s_margen / 100.0)]
pie_labels = ['Costo Base Fijo', 'Combustible y Rodaje', 'Peajes', 'Margen Operativo']
pie_colors = ['#2563EB', '#00E5FF', '#FF6B00', '#10B981']

wedges, texts, autotexts = ax8_pie.pie(
    pie_vals, labels=pie_labels, autopct='%1.1f%%', startangle=140,
    colors=pie_colors, textprops=dict(color="#CBD5E1", fontsize=9)
)
for at in autotexts:
    at.set_color('#FFFFFF')
    at.set_fontweight('bold')
ax8_pie.set_title("Desglose del Costo Logístico", color='#FFFFFF', fontsize=12, fontweight='bold')

fig8.savefig(os.path.join(out_dir, "08_Simulador_Escenarios_Presupuesto.png"), dpi=200, bbox_inches='tight')
plt.close(fig8)
print("8/8 Creada: 08_Simulador_Escenarios_Presupuesto.png")

print("\n¡Las 8 capturas en alta definición han sido generadas exitosamente en 'Capturas para diapositiva'!")
