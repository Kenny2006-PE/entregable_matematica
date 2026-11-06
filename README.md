# Sistema Interactivo de Regresión Lineal para Análisis de Datos (USIL)

## 📌 Datos del Proyecto
- **Universidad:** Universidad San Ignacio de Loyola (USIL)
- **Facultad:** Ingeniería e Inteligencia Artificial
- **Carrera:** Ingeniería de Sistemas de Información
- **Curso:** Matemática Discreta
- **Docente:** Marisel Rocío Beteta Salas
- **Integrantes:**
  - Combe Guerrero, Matthias Alexander (2614607)
  - Palacin Cristobal, Kenny Gerrard (2622777)
  - Espiritu Curo, Jeff Smith (2614070)
  - Pérez Cobeñas, Ángel Mathias (2614500)

---

## 🎯 Cumplimiento de Requerimientos
Este proyecto cumple al 100% con los dos incisos solicitados:
- **a. Implementar un modelo basado en regresión lineal en Excel o Python:**  
  Se implementó en **ambos** entornos (Excel y Python) con coincidencia matemática del 100%.
- **b. Visualización interactiva en Streamlit o Dash, en tiempo real:**  
  Desarrollado en **Streamlit** con gráficos reactivos en **Plotly**, simulación predictiva en vivo, bandas de confianza y cálculo paso a paso.

---

## 📂 Estructura de Archivos en la Carpeta

| Archivo | Descripción |
| :--- | :--- |
| **`app.py`** | Aplicación web interactiva en tiempo real en **Streamlit** con Plotly. |
| **`Sistema_Regresion_Logistica.xlsx`** | Libro oficial en **Microsoft Excel** con fórmulas `PENDIENTE`, `INTERSECCION.EJE`, `COEFICIENTE.R2`, `PRONOSTICO.LINEAL`, tabla de residuos y gráfico de dispersión. |
| **`INFORME_FINAL_PROYECTO.md`** | Informe académico completo listo para entrega/sustentación, continuando y expandiendo el Avance 1. |
| **`datos_logisticos.csv`** | Dataset con 25 rutas logísticas interprovinciales en el Perú (Distancia vs Costo). |
| **`generar_excel.py`** | Script generador que compila y estiliza el archivo Excel oficial. |
| **`generar_datos.py`** | Script que genera el dataset realista de logística. |
| **`ejecutar_sistema.bat`** | Lanzador rápido en Windows: doble clic para iniciar todo automáticamente. |
| **`requirements.txt`** | Dependencias necesarias (`streamlit`, `pandas`, `plotly`, `openpyxl`, etc.). |

---

## 🚀 ¿Cómo Ejecutar la Aplicación?

### Método 1 (El más fácil):
Hacer doble clic en el archivo **`ejecutar_sistema.bat`**.

### Método 2 (Por consola / PowerShell):
```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Iniciar Streamlit
streamlit run app.py
```
Se abrirá automáticamente en tu navegador en:
👉 `http://localhost:8501`

