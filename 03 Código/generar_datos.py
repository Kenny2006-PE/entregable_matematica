import pandas as pd
import numpy as np

# Semilla fija para reproducibilidad
np.random.seed(42)

rutas = [
    ("Lima - Chosica", 45),
    ("Lima - Cañete", 140),
    ("Lima - Barranca", 185),
    ("Lima - Chincha", 200),
    ("Lima - Pisco", 235),
    ("Lima - Huacho", 150),
    ("Lima - Ica", 305),
    ("Lima - La Oroya", 175),
    ("Lima - Huancayo", 310),
    ("Lima - Chimbote", 430),
    ("Lima - Huaraz", 400),
    ("Lima - Trujillo", 560),
    ("Lima - Ayacucho", 565),
    ("Lima - Chiclayo", 770),
    ("Lima - Cajamarca", 860),
    ("Lima - Arequipa", 1010),
    ("Lima - Piura", 990),
    ("Lima - Cusco", 1100),
    ("Lima - Puno", 1290),
    ("Lima - Tacna", 1295),
    ("Lima - Tumbes", 1270),
    ("Lima - Moquegua", 1140),
    ("Lima - Tarma", 230),
    ("Lima - Huánuco", 415),
    ("Lima - Tingo María", 550)
]

# Modelo realista de transporte de carga terrestre en Perú:
# Costo Fijo Base (b) aprox S/ 250 (preparación de carga, estiba, guías, peajes iniciales)
# Costo Variable (m) aprox S/ 4.80 por km recorrido (combustible, desgaste, chofer)
# Con una pequeña variación estocástica realista (desvíos, tráfico, peajes de ruta)
data = []
for i, (ruta, dist) in enumerate(rutas, start=1):
    costo_base = 250 + (dist * 4.80)
    ruido = np.random.normal(0, dist * 0.04) # ruido proporcional al viaje
    costo_total = round(max(150, costo_base + ruido), 2)
    data.append({
        "ID_Envio": f"ENV-{i:03d}",
        "Ruta": ruta,
        "Distancia_km": dist,
        "Costo_Total_Soles": costo_total
    })

df = pd.DataFrame(data)
df.to_csv("datos_logisticos.csv", index=False, encoding="utf-8-sig")
print(f"Dataset generado exitosamente con {len(df)} registros en 'datos_logisticos.csv'")

