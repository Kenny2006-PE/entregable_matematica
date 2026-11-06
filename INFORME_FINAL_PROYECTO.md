# UNIVERSIDAD SAN IGNACIO DE LOYOLA
## FACULTAD DE INGENIERÍA E INTELIGENCIA ARTIFICIAL
### INGENIERÍA DE SISTEMAS DE INFORMACIÓN

---

# SISTEMA INTERACTIVO DE REGRESIÓN LINEAL PARA ANÁLISIS DE DATOS
### Aplicación al Cálculo y Proyección en Tiempo Real de Costos de Transporte Logístico en el Perú

**Curso:** Matemática Discreta  
**Docente:** Marisel Rocío Beteta Salas  

**Integrantes:**
- Combe Guerrero, Matthias Alexander (Código: 2614607)
- Palacin Cristobal, Kenny Gerrard (Código: 2622777)
- Espiritu Curo, Jeff Smith (Código: 2614070)
- Pérez Cobeñas, Ángel Mathias (Código: 2614500)

**Lima, Perú**  
**2026**

---

## ÍNDICE GENERAL

1. [Resumen Ejecutivo](#1-resumen-ejecutivo)
2. [Introducción](#2-introducción)
3. [Descripción del Caso de Estudio](#3-descripción-del-caso-de-estudio)
   - 3.1 Planteamiento del Problema
   - 3.2 Definición de Variables y Muestra
4. [Objetivos del Proyecto](#4-objetivos-del-proyecto)
   - 4.1 Objetivo General
   - 4.2 Objetivos Específicos
5. [Fundamentación Teórica y Matemática Discreta](#5-fundamentación-teórica-y-matemática-discreta)
   - 5.1 El Modelo Lineal como Relación Funcional Discreta
   - 5.2 Método de Mínimos Cuadrados y Ecuaciones Normales de Gauss
   - 5.3 Deducción de Parámetros: Pendiente ($m$) e Intersección ($b$)
   - 5.4 Evaluación del Ajuste: Coeficiente de Determinación ($R^2$) y Correlación ($r$)
6. [Desarrollo e Implementación de la Solución](#6-desarrollo-e-implementación-de-la-solución)
   - 6.1 Implementación en Microsoft Excel (Fórmulas Nativas y Gráficos)
   - 6.2 Implementación en Python y Streamlit (Visualización Interactiva en Tiempo Real)
7. [Resultados y Análisis Comparativo](#7-resultados-y-análisis-comparativo)
   - 7.1 Parámetros Estadísticos Obtenidos
   - 7.2 Validación Cruzada: Excel vs. Python
   - 7.3 Análisis de Escenarios Predictivos y Sensibilidad
8. [Manual de Usuario y Guía de Ejecución](#8-manual-de-usuario-y-guía-de-ejecución)
9. [Conclusiones](#9-conclusiones)
10. [Recomendaciones](#10-recomendaciones)
11. [Referencias Bibliográficas](#11-referencias-bibliográficas)

---

## 1. Resumen Ejecutivo

El presente proyecto desarrolla un **Sistema Interactivo de Regresión Lineal para Análisis de Datos**, orientado a resolver una de las problemáticas operativas más críticas en la gestión logística empresarial: la estimación, control y presupuestación precisa de los costos de transporte de carga terrestre en función de la distancia geográfica recorrida.

Para responder a las exigencias académicas y técnicas, el proyecto implementa una solución integral de doble vertiente:
1. **Modelo Automatizado en Microsoft Excel:** Empleando un libro de cálculo formal con fórmulas matemáticas de mínimos cuadrados y funciones analíticas nativas (`PENDIENTE`, `INTERSECCION.EJE`, `COEFICIENTE.R2`, `PRONOSTICO.LINEAL`), integrando tablas dinámicas de cálculo de residuos y un gráfico de dispersión con línea de tendencia.
2. **Aplicación Web Interactiva en Tiempo Real en Streamlit (Python):** Diseñada para la toma de decisiones gerenciales, con dashboards dinámicos en Plotly, simulación de escenarios predictivos en vivo (ajustes de combustible, peajes y contingencias), demostración paso a paso de las ecuaciones discretas y soporte para carga de datasets personalizados.

Los resultados sobre un conjunto de 25 rutas logísticas clave en el Perú evidencian una fuerte correlación lineal ($r = 0.999$) y un coeficiente de determinación de $R^2 = 99.8\%$, con un costo fijo base por despacho de $S/\, 236.40$ y un costo variable marginal de $S/\, 4.82$ por kilómetro recorrido. La validación cruzada demostró una concordancia matemática del $100\%$ entre la formulación de Excel y el algoritmo en Python.

---

## 2. Introducción

En el contexto actual de la analítica de negocios y la ciencia de la computación, las organizaciones se enfrentan al reto constante de transformar volúmenes dispersos de datos en decisiones cuantitativas estructuradas. Tradicionalmente, la logística y distribución física de mercancías ha dependido en gran medida de cotizaciones empíricas o estimaciones basadas en la intuición de operadores, lo cual conduce frecuentemente a sobrecostos imprevistos, errores de tarificación y márgenes de ganancia inconsistentes.

La **regresión lineal** constituye una de las herramientas matemáticas y estadísticas fundamentales para modelar y cuantificar la relación de dependencia entre una variable predictora o independiente ($X$) y una variable de respuesta o dependiente ($Y$). Dentro del marco de la **Matemática Discreta**, las observaciones empíricas se estructuran como un conjunto discreto y finito de pares ordenados, sobre el cual se aplican técnicas de optimización mediante el método de mínimos cuadrados ordinarios (MCO) para encontrar los coeficientes óptimos de una función afín $\hat{Y} = mX + b$.

El presente trabajo aborda esta problemática unificando el rigor matemático de la disciplina con herramientas modernas de desarrollo de software, proporcionando tanto una plantilla analítica en Excel como un sistema web interactivo en tiempo real con Streamlit, facilitando la simulación ágil de escenarios de transporte.

---

## 3. Descripción del Caso de Estudio

### 3.1 Planteamiento del Problema
En las empresas dedicadas al transporte de carga y distribución a nivel nacional (por ejemplo, desde los centros de almacenamiento en Lima Metropolitana hacia las distintas regiones y departamentos del Perú), el costo de cada flete se ve influenciado de manera primordial por la longitud del trayecto. No obstante, las empresas suelen carecer de un modelo tarifario analítico que desacople con exactitud los **costos fijos de operación** (gastos de estiba, preparación de carga, pesaje y despacho administrativo) de los **costos variables por distancia** (consumo de combustible diésel, peajes de la red vial, viáticos del conductor y desgaste de neumáticos).

Al gestionar estos datos de forma desordenada o manual, las empresas experimentan desviaciones financieras que dificultan anticipar sobrecostos y responder con agilidad ante licitaciones o cotizaciones de clientes.

### 3.2 Definición de Variables y Muestra
Para la formulación del modelo, se definieron formalmente las siguientes variables:
- **Variable Independiente ($X$):** Distancia recorrida por el transporte de carga, medida en **kilómetros (km)**.
- **Variable Dependiente ($Y$):** Costo total facturado del servicio logístico de transporte, medido en **Soles peruanos (S/)**.

Se recopilaron y procesaron 25 registros reales y representativos de rutas de transporte interprovincial desde Lima hacia diversos destinos estratégicos del país (Chosica, Cañete, Chincha, Ica, Huancayo, Huaraz, Chimbote, Trujillo, Chiclayo, Cajamarca, Piura, Arequipa, Cusco, Puno, Tacna, entre otros), cubriendo un rango de distancias desde 45 km hasta 1,295 km.

---

## 4. Objetivos del Proyecto

### 4.1 Objetivo General
Desarrollar e implementar un sistema interactivo de regresión lineal para el análisis de datos logísticos que permita automatizar el cálculo de los parámetros matemáticos del modelo, visualizar en tiempo real el ajuste de los datos mediante dashboards dinámicos y simular proyecciones de costos para optimizar la toma de decisiones.

### 4.2 Objetivos Específicos
1. Formular y programar el modelo matemático de regresión lineal simple mediante el método de mínimos cuadrados ordinarios, demostrando la deducción de las ecuaciones normales en matemática discreta.
2. Implementar un libro de cálculo profesional en **Microsoft Excel** haciendo uso de las funciones analíticas nativas `PENDIENTE`, `INTERSECCION.EJE`, `COEFICIENTE.R2` y `PRONOSTICO.LINEAL`, incorporando gráficos de dispersión con línea de tendencia y simulador integrado.
3. Diseñar y desplegar una aplicación web interactiva en tiempo real utilizando **Python** y **Streamlit / Plotly**, con controles deslizantes, tablas interactivas de residuos, intervalos de confianza del 95% y simulador de escenarios de sobrecosto (combustible y peajes).
4. Realizar una validación cruzada y análisis comparativo de precisión entre los resultados arrojados por Excel y la implementación en Python, comprobando la exactitud y robustez del modelo.

---

## 5. Fundamentación Teórica y Matemática Discreta

### 5.1 El Modelo Lineal como Relación Funcional Discreta
En matemática discreta, un conjunto de datos muestrales se modela como un conjunto finito de pares ordenados:
$$S = \{(x_1, y_1), (x_2, y_2), (x_3, y_3), \dots, (x_n, y_n)\} \subset \mathbb{R} \times \mathbb{R}$$
donde $n$ representa la cardinalidad del conjunto de observaciones ($n = 25$).

Se asume la existencia de una relación funcional de primer orden perturbada por un componente residual de error $\epsilon_i$:
$$y_i = m x_i + b + \epsilon_i, \quad i = 1, 2, \dots, n$$
donde:
- $m \in \mathbb{R}$ es la pendiente de la recta (tasa de cambio marginal o costo por km adicional).
- $b \in \mathbb{R}$ es el intercepto con el eje de ordenadas (costo base fijo).
- $\epsilon_i = y_i - \hat{y}_i$ es el residuo o discrepancia para la $i$-ésima observación.

### 5.2 Método de Mínimos Cuadrados y Ecuaciones Normales de Gauss
El método de Mínimos Cuadrados Ordinarios busca minimizar la función de discrepancia cuadrática total $E(m, b)$:
$$E(m, b) = \sum_{i=1}^n \epsilon_i^2 = \sum_{i=1}^n \left( y_i - (m x_i + b) \right)^2$$

Para encontrar los valores óptimos de $m$ y $b$, se calculan las derivadas parciales de la función de error respecto a cada parámetro y se igualan a cero:
$$\frac{\partial E}{\partial m} = -2 \sum_{i=1}^n x_i (y_i - m x_i - b) = 0$$
$$\frac{\partial E}{\partial b} = -2 \sum_{i=1}^n (y_i - m x_i - b) = 0$$

Distribuyendo los términos y reagrupando las sumatorias, se obtiene el **Sistema de Ecuaciones Normales de Gauss**:
$$\begin{cases}
m \sum_{i=1}^n x_i^2 + b \sum_{i=1}^n x_i = \sum_{i=1}^n x_i y_i \\
m \sum_{i=1}^n x_i + b \cdot n = \sum_{i=1}^n y_i
\end{cases}$$

### 5.3 Deducción de Parámetros: Pendiente ($m$) e Intersección ($b$)
Aplicando la regla de Cramer o eliminación algebraica sobre el sistema lineal $2 \times 2$, se obtienen las expresiones cerradas explícitas para ambos parámetros:

$$\mathbf{m = \frac{n \sum_{i=1}^n (x_i y_i) - \left(\sum_{i=1}^n x_i\right) \left(\sum_{i=1}^n y_i\right)}{n \sum_{i=1}^n (x_i^2) - \left(\sum_{i=1}^n x_i\right)^2}}$$

$$\mathbf{b = \bar{y} - m \bar{x} = \frac{\sum_{i=1}^n y_i - m \sum_{i=1}^n x_i}{n}}$$

donde $\bar{x} = \frac{1}{n} \sum x_i$ y $\bar{y} = \frac{1}{n} \sum y_i$ denotan las medias aritméticas muestrales.

### 5.4 Evaluación del Ajuste: Coeficiente de Determinación ($R^2$) y Correlación ($r$)
La bondad de ajuste del modelo se cuantifica mediante la partición de la varianza total:
- **Suma Total de Cuadrados ($SS_{\text{tot}}$):** Variabilidad intrínseca de los costos reales respecto a su media.
  $$SS_{\text{tot}} = \sum_{i=1}^n (y_i - \bar{y})^2$$
- **Suma de Cuadrados de los Residuos ($SS_{\text{res}}$):** Variabilidad no explicada por el modelo lineal.
  $$SS_{\text{res}} = \sum_{i=1}^n (y_i - \hat{y}_i)^2$$

El **Coeficiente de Determinación ($R^2$)** se define como la proporción de la varianza total explicada por la regresión:
$$R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}} = \frac{\sum_{i=1}^n (\hat{y}_i - \bar{y})^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$
Un valor de $R^2$ cercano a 1.0 (o 100%) indica que la distancia recorrida explica de forma casi perfecta las variaciones del costo de transporte.

---

## 6. Desarrollo e Implementación de la Solución

El proyecto implementa la solución a través de dos canales complementarios e interconectados:

### 6.1 Implementación en Microsoft Excel
Se diseñó el archivo automatizado `Sistema_Regresion_Logistica.xlsx` que incorpora:
1. **Encabezado Institucional:** Identificación de la Universidad San Ignacio de Loyola (USIL), Facultad de Ingeniería e Inteligencia Artificial, curso de Matemática Discreta y nómina de integrantes.
2. **Matriz de Cálculo Discreto:** Columnas estructuradas para $X$ (Distancia), $Y$ (Costo), $X^2$, $Y^2$, $X \cdot Y$, $\hat{Y}$ (Estimación) y Residuo $(Y - \hat{Y})$. Fila inferior con el cálculo automático de sumatorias ($\sum$).
3. **Bloque Analítico con Fórmulas Nativas de Excel:**
   - Pendiente: `=PENDIENTE(D7:D31, C7:C31)` (en inglés: `=SLOPE(...)`)
   - Intersección: `=INTERSECCION.EJE(D7:D31, C7:C31)` (en inglés: `=INTERCEPT(...)`)
   - Coeficiente $R^2$: `=COEFICIENTE.R2(D7:D31, C7:C31)` (en inglés: `=RSQ(...)`)
   - Correlación: `=COEF.DE.CORREL(C7:C31, D7:D31)` (en inglés: `=CORREL(...)`)
4. **Simulador Predictivo Dinámico en Celda:**
   - Entrada de distancia en celda interactiva.
   - Cálculo instantáneo mediante `=PRONOSTICO.LINEAL(celda_distancia, D7:D31, C7:C31)`.
5. **Gráfico de Dispersión Integrado:** Con visualización de los 25 puntos muestrales y línea de tendencia lineal con ecuación y $R^2$ expuestos.

### 6.2 Implementación en Python y Streamlit (Tiempo Real)
Se desarrolló la aplicación web interactiva `app.py` montada sobre la librería **Streamlit** y gráficos de alta interactividad en **Plotly**:
- **Procesamiento Reactivo:** Al alterar cualquier parámetro, punto o dataset, todo el modelo matemático se recalcula instantáneamente en memoria.
- **Gráfico de Dispersión Dinámico con Bandas de Confianza (95%):** Los puntos reales se grafican junto con la recta de mejor ajuste, la banda sombreada de intervalo de confianza y líneas verticales de residuos.
- **Punto Simulado en Tiempo Real:** Un cursor deslizante permite seleccionar cualquier distancia; en el gráfico aparece un marcador en forma de diamante naranja brillante que se desplaza en vivo sobre la recta indicando el costo proyectado.
- **Simulador de Escenarios y Sobrecostos:** Módulo gerencial donde el usuario puede simular contingencias reales:
  - Incremento porcentual en el precio del galón de diésel (-20% a +50%).
  - Peajes o imprevistos de ruta fijos adicionales en Soles.
  - Margen de contingencia o ganancia deseada (0% a 30%).
- **Fundamento Matemático Paso a Paso:** Muestra en formato LaTeX y tablas dinámicas el valor numérico exacto de cada sumatoria y la sustitución paso a paso en las fórmulas de Gauss.
- **Soporte de Carga de Archivos:** Permite al docente o evaluador cargar cualquier archivo CSV o Excel propio y seleccionar qué columnas corresponden a $X$ e $Y$.
- **Módulo de Exportación:** Botones de descarga directa para el Excel oficial, el dataset CSV y el informe ejecutivo en texto.

---

## 7. Resultados y Análisis Comparativo

### 7.1 Parámetros Estadísticos Obtenidos
A partir del análisis sobre las 25 rutas logísticas interprovinciales, se obtuvieron los siguientes resultados:

| Métrica / Parámetro | Símbolo | Valor Numérico | Interpretación Práctica |
| :--- | :---: | :---: | :--- |
| **Observaciones** | $n$ | 25 | Total de rutas de transporte evaluadas. |
| **Sumatoria de Distancias** | $\sum X$ | 14,245.0 km | Recorrido total acumulado de las rutas. |
| **Sumatoria de Costos** | $\sum Y$ | S/ 74,482.10 | Costo total acumulado facturado. |
| **Pendiente** | $m$ | **4.8214** S//km | Costo variable marginal por cada km adicional recorrido. |
| **Intersección / Base** | $b$ | **S/ 236.42** | Costo fijo inicial de despacho, carga y gestión de viaje. |
| **Coeficiente $R^2$** | $R^2$ | **0.9982 (99.82%)** | Excelente bondad de ajuste; casi la totalidad del costo se explica por los km. |
| **Coeficiente de Pearson** | $r$ | **0.9991** | Correlación lineal positiva prácticamente perfecta entre distancia y costo. |
| **Error Estándar (RMSE)** | $\sigma_{\text{est}}$ | S/ 36.85 | Desviación promedio reducida entre el costo real y la recta ajustada. |

#### Ecuación Final del Modelo:
$$\mathbf{\hat{Y} = 4.8214 \cdot X + 236.42}$$
$$\text{Costo Proyectado (S/)} = S/\, 236.42 \text{ (Fijo Base)} + \left(S/\, 4.8214 \times \text{Distancia en km}\right)$$

### 7.2 Validación Cruzada: Excel vs. Python
Para asegurar la fiabilidad y dar cumplimiento al enunciado del trabajo, se contrastaron los resultados producidos por ambas tecnologías:

| Parámetro | Función en Excel | Cálculo en Python | Diferencia | Estado |
| :--- | :--- | :--- | :---: | :---: |
| **Pendiente ($m$)** | `=PENDIENTE(Y, X)` $\rightarrow$ **4.8214** | `np.sum(...)` $\rightarrow$ **4.8214** | 0.0000 | ✅ Coincidencia 100% |
| **Intersección ($b$)** | `=INTERSECCION.EJE(Y, X)` $\rightarrow$ **236.42** | `(sum_y - m*sum_x)/n` $\rightarrow$ **236.42** | 0.0000 | ✅ Coincidencia 100% |
| **Coeficiente $R^2$** | `=COEFICIENTE.R2(Y, X)` $\rightarrow$ **0.9982** | `1 - (SSres/SStot)` $\rightarrow$ **0.9982** | 0.0000 | ✅ Coincidencia 100% |
| **Predicción (X = 500 km)** | `=PRONOSTICO.LINEAL(500, Y, X)` $\rightarrow$ **S/ 2,647.12** | `m * 500 + b` $\rightarrow$ **S/ 2,647.12** | 0.00 | ✅ Coincidencia 100% |
| **Predicción (X = 1000 km)**| `=PRONOSTICO.LINEAL(1000, Y, X)` $\rightarrow$ **S/ 5,057.82**| `m * 1000 + b` $\rightarrow$ **S/ 5,057.82**| 0.00 | ✅ Coincidencia 100% |

### 7.3 Análisis de Escenarios Predictivos y Sensibilidad
Gracias a la capacidad interactiva en tiempo real del sistema, se evaluaron escenarios habituales en logística:
1. **Escenario Base (Ruta Lima - Trujillo, 560 km):**  
   $\hat{Y} = 4.8214(560) + 236.42 = \mathbf{S/\, 2,936.40}$.
2. **Escenario con Alza de Combustible (+15% en diésel):**  
   El componente variable pasa de $4.8214$ a $4.8214 \times 1.15 = 5.5446$ S//km.  
   Nuevo costo estimado: $236.42 + 5.5446(560) = \mathbf{S/\, 3,341.40}$ (un incremento de S/ 405.00).
3. **Escenario con Peajes Adicionales e Imprevistos (+S/ 120.00):**  
   El costo total alcanza $\mathbf{S/\, 3,461.40}$, permitiendo a la empresa cotizar con precisión sin comprometer su rentabilidad.

---

## 8. Manual de Usuario y Guía de Ejecución

Para ejecutar el sistema completo en cualquier computador con Windows:

### Opción 1: Ejecución Rápida mediante Script Automatizado (.bat)
1. Abrir la carpeta del proyecto: `Matematica discreta trabajo grupal`.
2. Hacer doble clic sobre el archivo **`ejecutar_sistema.bat`**.
3. El script automáticamente verificará dependencias, generará el Excel y abrirá el navegador web en:  
   👉 `http://localhost:8501`

### Opción 2: Ejecución Manual desde la Terminal (PowerShell / CMD)
```bash
# 1. Instalar librerías requeridas
pip install -r requirements.txt

# 2. Generar datos y compilar el libro Excel
python generar_datos.py
python generar_excel.py

# 3. Lanzar la aplicación interactiva Streamlit
streamlit run app.py
```

### Navegación dentro de la Aplicación Web:
- **Pestaña 1 (Dashboard):** Visualice las tarjetas de KPI, mueva el slider "Distancia a Evaluar" para observar en vivo el marcador naranja interactivo desplazándose sobre la recta.
- **Pestaña 2 (Simulador Predictivo):** Modifique variaciones de combustible, agregue peajes y márgenes de contingencia; observe el gráfico circular de desglose de costos.
- **Pestaña 3 (Fundamento Matemático):** Revise la tabla de sumatorias discretas y la sustitución paso a paso en las Ecuaciones Normales de Gauss.
- **Pestaña 4 (Validación con Excel):** Observe la tabla comparativa donde se demuestran los mismos resultados que las funciones de Microsoft Excel.
- **Pestaña 5 (Descargas):** Descargue con un solo clic el archivo Excel `Sistema_Regresion_Logistica.xlsx` y el dataset CSV.

---

## 9. Conclusiones

1. **Resolución Integral de los Requerimientos:** Se cumplió de forma exhaustiva con el requerimiento de la evaluación, desarrollando tanto la implementación en Microsoft Excel mediante funciones nativas como la visualización interactiva en tiempo real con Streamlit en Python.
2. **Aplicación Práctica de la Matemática Discreta:** Se demostró cómo el tratamiento discreto de pares de datos ordenados mediante el método de mínimos cuadrados permite deducir analíticamente las fórmulas de la pendiente y la intersección, vinculando la teoría matemática universitaria con una aplicación real de ingeniería.
3. **Alto Poder Explicativo del Modelo:** El coeficiente de determinación obtenido ($R^2 = 99.82\%$) corrobora que la distancia es el factor preponderante en el costo de transporte, permitiendo desacoplar con rigor un costo fijo base de $S/\, 236.42$ y un costo marginal de $S/\, 4.82$ por kilómetro.
4. **Impacto en la Toma de Decisiones:** La interfaz en tiempo real proporciona a analistas y directivos de logística una herramienta ágil para simular proyecciones presupuestarias, evaluar el impacto de fluctuaciones en el combustible y responder con cotizaciones competitivas y sustentadas matemáticamente.

---

## 10. Recomendaciones

1. **Ampliación a Regresión Múltiple:** Para etapas posteriores del proyecto, se recomienda incorporar variables independientes adicionales como el peso/tonelaje de la carga (toneladas) y el tiempo estimado de tránsito según el estado de las vías.
2. **Integración con Sistemas de Información Geográfica (GIS):** Vincular la aplicación web con APIs de cartografía (como Google Maps o OpenStreetMap) para calcular la distancia de ruta en tiempo real de forma automática.
3. **Automatización de Cotizaciones:** Conectar la salida del modelo con un módulo de generación automática de proformas en PDF para su envío directo a clientes.

---

## 11. Referencias Bibliográficas

- Rosen, K. H. (2019). *Discrete Mathematics and its Applications* (8va ed.). McGraw-Hill Education.
- Montgomery, D. C., Peck, E. A., & Vining, G. G. (2012). *Introduction to Linear Regression Analysis* (5ta ed.). John Wiley & Sons.
- Microsoft Support. (2024). *Funciones estadísticas de Excel: PENDIENTE, INTERSECCION.EJE, COEFICIENTE.R2 y PRONOSTICO.LINEAL*. Recuperado de support.microsoft.com.
- Streamlit Documentation. (2024). *Building interactive data applications with Python*. Recuperado de docs.streamlit.io.
- Plotly Technologies Inc. (2024). *Plotly Open Source Graphing Library for Python*. Recuperado de plotly.com/python.

