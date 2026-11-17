import pandas as pd
import numpy as np

# Semilla fija para reproducibilidad de Modelo 1 (se mantienen idénticos los costos previos)
np.random.seed(42)

rutas = [
    ("Lima - Chosica", 45, "Sierra"),
    ("Lima - Cañete", 140, "Costa"),
    ("Lima - Barranca", 185, "Costa"),
    ("Lima - Chincha", 200, "Costa"),
    ("Lima - Pisco", 235, "Costa"),
    ("Lima - Huacho", 150, "Costa"),
    ("Lima - Ica", 305, "Costa"),
    ("Lima - La Oroya", 175, "Sierra"),
    ("Lima - Huancayo", 310, "Sierra"),
    ("Lima - Chimbote", 430, "Costa"),
    ("Lima - Huaraz", 400, "Sierra"),
    ("Lima - Trujillo", 560, "Costa"),
    ("Lima - Ayacucho", 565, "Sierra"),
    ("Lima - Chiclayo", 770, "Costa"),
    ("Lima - Cajamarca", 860, "Sierra"),
    ("Lima - Arequipa", 1010, "Sierra"),
    ("Lima - Piura", 990, "Costa"),
    ("Lima - Cusco", 1100, "Sierra"),
    ("Lima - Puno", 1290, "Sierra"),
    ("Lima - Tacna", 1295, "Costa"),
    ("Lima - Tumbes", 1270, "Costa"),
    ("Lima - Moquegua", 1140, "Costa"),
    ("Lima - Tarma", 230, "Sierra"),
    ("Lima - Huánuco", 415, "Sierra"),
    ("Lima - Tingo María", 550, "Selva")
]

# Modelo 1: Distancia (km) vs Costo Total de Transporte (S/)
costos = []
for _, dist, _ in rutas:
    costo_base = 250 + (dist * 4.80)
    ruido = np.random.normal(0, dist * 0.04)
    costos.append(round(max(150, costo_base + ruido), 2))

# Modelo 2: Distancia (km) vs Consumo de Combustible (Galones de Diésel)
# Se modela un camión de carga pesada:
# - Consumo base fijo en maniobras/carga/salida Lima: ~5.2 galones
# - Consumo variable en Costa (plano): ~0.124 gal/km
# - Consumo variable en Sierra/Selva (pendientes andinas): ~0.148 gal/km
# - Variación estocástica por tráfico y peso de carga
rng_comb = np.random.default_rng(108)
data = []
for i, ((ruta, dist, region), costo_total) in enumerate(zip(rutas, costos), start=1):
    tasa_gal_km = 0.124 if region == "Costa" else 0.148
    comb_base = 5.2 + (dist * tasa_gal_km)
    ruido_comb = rng_comb.normal(0, max(1.8, dist * 0.008))
    consumo_gal = round(max(8.0, comb_base + ruido_comb), 2)
    data.append({
        "ID_Envio": f"ENV-{i:03d}",
        "Ruta": ruta,
        "Region": region,
        "Distancia_km": dist,
        "Costo_Total_Soles": costo_total,
        "Consumo_Combustible_Gal": consumo_gal
    })

df = pd.DataFrame(data)
df.to_csv("datos_logisticos.csv", index=False, encoding="utf-8-sig")
print(f"Dataset actualizado exitosamente con {len(df)} registros y ambos modelos en 'datos_logisticos.csv'")
