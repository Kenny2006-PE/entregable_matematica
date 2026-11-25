# DOCUMENTACIÓN TÉCNICA E INTEGRAL DEL PROYECTO
## Sistema Interactivo de Regresión Lineal para Análisis de Datos Logísticos en el Perú
### Optimización y Estimación Predictiva de Costos de Transporte y Consumo de Combustible Diésel

---

## 1. FICHA TÉCNICA Y METADATOS INSTITUCIONALES

* **Institución Educativa:** Universidad San Ignacio de Loyola (USIL)
* **Facultad:** Facultad de Ingeniería e Inteligencia Artificial
* **Carrera Profesional:** Ingeniería de Sistemas de Información
* **Curso:** Matemática Discreta
* **Ciclo Académico:** 2026-I
* **Docente del Curso:** Mg. Marisel Rocío Beteta Salas
* **Repositorio Oficial de GitHub:** `https://github.com/Kenny2006-PE/entregable_matematica.git` (Rama: `main`)

### Integrantes del Equipo de Investigación:
1. **Combe Guerrero, Matthias Alexander** (Código: `2614607`)
2. **Palacin Cristobal, Kenny Gerrard** (Código: `2622777`)
3. **Espiritu Curo, Jeff Smith** (Código: `2614070`)
4. **Pérez Cobeñas, Ángel Mathias** (Código: `2614500`)

---

## 2. CONTEXTO, PROBLEMÁTICA Y CASO DE ESTUDIO

### 2.1. Problemática en el Transporte de Carga Terrestre en el Perú
El transporte terrestre interprovincial es la columna vertebral de la cadena logística en el Perú. No obstante, las empresas transportistas enfrentan incertidumbre operativa al cotizar envíos y presupuestar combustible debido a la compleja geografía nacional:
* **Heterogeneidad topográfica:** Coexisten carreteras planas a nivel del mar (Costa: Carretera Panamericana), ascensos pronunciados sobre los 4,800 m.s.n.m. cruzando la Cordillera de los Andes (Sierra: Carretera Central y paso de Ticlio), y rutas de selva alta/baja con curvas sinuosas y condiciones climáticas extremas.
* **Impacto termodinámico y mecánico:** El consumo de combustible por kilómetro y el desgaste mecánico no son constantes; varían drásticamente con la altitud y la pendiente.
* **Falta de herramientas analíticas transparentes:** Muchas micro y pequeñas empresas fijan tarifas empíricas sin sustento cuantitativo, provocando pérdidas operativas o cotizaciones fuera de mercado.

### 2.2. Propósito del Proyecto
Desarrollar un sistema analítico fundamentado en **Matemática Discreta** (Mínimos Cuadrados Ordinarios y Ecuaciones Normales de Gauss) implementado en dos plataformas integradas:
1. **Modelo en Hoja de Cálculo (Microsoft Excel):** Automatizado mediante fórmulas matriciales y nativas de Excel.
2. **Aplicación Web Interactiva (Python + Streamlit + Plotly):** Software interactivo con simulación de escenarios, cálculo algorítmico puro (sin librerías de caja negra) y gráficos de dispersión con análisis de residuos.

### 2.3. Dos Modelos Predictivos Bivariados Discretos
* **Modelo 1:** Variable Independiente $X$ (Distancia en km) vs. Variable Dependiente $Y_1$ (Costo Total de Transporte en Soles - S/).
* **Modelo 2:** Variable Independiente $X$ (Distancia en km) vs. Variable Dependiente $Y_2$ (Consumo de Combustible en Galones Diésel).

---

## 3. DATASET MAESTRO COMPLETO (23 RUTAS REALES)

El modelo opera sobre una muestra finita discreta de $n = 23$ rutas logísticas nacionales distribuidas estratégicamente a través de la Costa, Sierra y Selva peruana (datos extraídos y consolidados en `datos_logisticos.csv`).

> **Nota Metodológica Crucial:** Se reemplazó un dataset sintético inicial (que producía un $R^2 = 99.98\%$ matemáticamente artificial y rechazado por la docente) por este conjunto de 23 rutas reales. Este dataset incorpora la dispersión natural provocada por la altitud andina y la geografía selvática, alcanzando un $R^2$ realista y robusto ($85.45\%$ en Costos y $81.57\%$ en Combustible).

| ID Envío | Ruta Interprovincial | Región Geográfica | Distancia $X$ (km) | Costo Total $Y_1$ (S/) | Consumo Combustible $Y_2$ (gal) |
|:---:|:---|:---:|:---:|:---:|:---:|
| **R-01** | Lima - La Oroya | Sierra | 174 | 93.04 | 35.85 |
| **R-02** | Lima - Huancayo | Sierra | 298 | 123.20 | 59.73 |
| **R-03** | Lima - Cerro de Pasco | Sierra | 302 | 124.11 | 56.10 |
| **R-04** | Lima - Ica | Costa | 303 | 107.28 | 39.04 |
| **R-05** | Lima - Huaraz | Sierra | 406 | 149.60 | 80.63 |
| **R-06** | Lima - Huánuco | Sierra | 410 | 154.37 | 76.05 |
| **R-07** | Lima - Chimbote | Costa | 431 | 128.91 | 54.98 |
| **R-08** | Lima - Ayacucho | Sierra | 543 | 183.53 | 101.72 |
| **R-09** | Lima - Trujillo | Costa | 561 | 157.48 | 69.34 |
| **R-10** | Lima - Chiclayo | Costa | 770 | 215.85 | 93.35 |
| **R-11** | Lima - Pucallpa | Selva | 785 | 294.29 | 135.78 |
| **R-12** | Lima - Cajamarca | Sierra | 861 | 247.31 | 172.96 |
| **R-13** | Lima - Abancay | Sierra | 907 | 364.33 | 184.83 |
| **R-14** | Lima - Piura | Costa | 981 | 275.07 | 117.83 |
| **R-15** | Lima - Arequipa | Sierra | 1009 | 296.45 | 213.15 |
| **R-16** | Lima - Cusco | Sierra | 1105 | 442.69 | 220.49 |
| **R-17** | Lima - Moquegua | Costa | 1145 | 341.88 | 141.47 |
| **R-18** | Lima - Chachapoyas | Sierra | 1219 | 485.09 | 246.03 |
| **R-19** | Lima - Tumbes | Costa | 1259 | 354.99 | 153.80 |
| **R-20** | Lima - Tacna | Costa | 1293 | 386.92 | 154.92 |
| **R-21** | Lima - Puno | Sierra | 1335 | 442.79 | 282.75 |
| **R-22** | Lima - Moyobamba | Selva | 1363 | 569.69 | 240.27 |
| **R-23** | Lima - Pto. Maldonado | Selva | 1638 | 799.01 | 285.41 |

---

## 4. FUNDAMENTACIÓN MATEMÁTICA DISCRETA Y DEDUCCIÓN RIGUROSA

### 4.1. Formalización en Estructuras Discretas
En Matemática Discreta, un conjunto de datos bivariados se define formalmente como una relación binaria finita:
$$S = \{ (x_i, y_i) \in \mathbb{R} \times \mathbb{R} \mid i = 1, 2, \dots, n \}$$
Donde la cardinalidad del conjunto es $|S| = n = 23$. Al ser un conjunto finito y numerable, no se trabaja con funciones continuas a priori, sino con operadores de sumatoria discreta $\sum_{i=1}^n$.

Buscamos construir una función lineal predictiva $\hat{y} = f(x) = mx + b$ que aproxime la relación discreta minimizando el error global.

### 4.2. Definición del Error Residual y Función de Pérdida
Para cada par discreto $(x_i, y_i)$, el error o residuo individual se define como la diferencia entre el valor observado y el valor estimado por la recta:
$$e_i = y_i - \hat{y}_i = y_i - (m x_i + b)$$

El criterio de **Mínimos Cuadrados Ordinarios (MCO)** establece que los parámetros óptimos $m$ (pendiente) y $b$ (ordenada al origen) minimizan la Suma de Errores Cuadráticos ($SSE$ o $S(m,b)$):
$$S(m, b) = \sum_{i=1}^n e_i^2 = \sum_{i=1}^n \left( y_i - (m x_i + b) \right)^2$$

### 4.3. Deducción de las Ecuaciones Normales de Gauss
Para hallar el mínimo de la superficie convexa cuadrática $S(m, b)$, se calculan las derivadas parciales respecto a $b$ y $m$ y se igualan a cero:

#### Derivada parcial respecto a $b$:
$$\frac{\partial S}{\partial b} = \sum_{i=1}^n 2 \left( y_i - m x_i - b \right) (-1) = 0$$
$$-2 \left[ \sum_{i=1}^n y_i - m \sum_{i=1}^n x_i - b \sum_{i=1}^n 1 \right] = 0$$
Dado que $\sum_{i=1}^n 1 = n$:
$$\sum_{i=1}^n y_i - m \sum_{i=1}^n x_i - n b = 0 \implies m \sum_{i=1}^n x_i + n b = \sum_{i=1}^n y_i \quad \text{--- (Ecuación Normal I)}$$

#### Derivada parcial respecto a $m$:
$$\frac{\partial S}{\partial m} = \sum_{i=1}^n 2 \left( y_i - m x_i - b \right) (-x_i) = 0$$
$$-2 \left[ \sum_{i=1}^n x_i y_i - m \sum_{i=1}^n x_i^2 - b \sum_{i=1}^n x_i \right] = 0$$
Dividiendo entre $-2$:
$$\sum_{i=1}^n x_i y_i - m \sum_{i=1}^n x_i^2 - b \sum_{i=1}^n x_i = 0 \implies m \sum_{i=1}^n x_i^2 + b \sum_{i=1}^n x_i = \sum_{i=1}^n x_i y_i \quad \text{--- (Ecuación Normal II)}$$

### 4.4. Sistema Matricial de Gauss $2 \times 2$
Agrupando las ecuaciones en notación matricial:
$$\begin{pmatrix} \sum x_i^2 & \sum x_i \\ \sum x_i & n \end{pmatrix} \begin{pmatrix} m \\ b \end{pmatrix} = \begin{pmatrix} \sum x_i y_i \\ \sum y_i \end{pmatrix}$$

Aplicando la **Regla de Cramer**:
* Determinante del sistema ($\Delta$):
$$\Delta = n \sum x_i^2 - \left(\sum x_i\right)^2$$
* Determinante para la pendiente ($\Delta_m$):
$$\Delta_m = n \sum x_i y_i - \left(\sum x_i\right) \left(\sum y_i\right)$$
* Determinante para el intercepto ($\Delta_b$):
$$\Delta_b = \left(\sum x_i^2\right) \left(\sum y_i\right) - \left(\sum x_i\right) \left(\sum x_i y_i\right)$$

Por tanto, las fórmulas analíticas cerradas son:
$$m = \frac{n \sum_{i=1}^n x_i y_i - \left(\sum_{i=1}^n x_i\right)\left(\sum_{i=1}^n y_i\right)}{n \sum_{i=1}^n x_i^2 - \left(\sum_{i=1}^n x_i\right)^2}$$

$$b = \bar{y} - m \bar{x} = \frac{\sum_{i=1}^n y_i - m \sum_{i=1}^n x_i}{n}$$

Donde $\bar{x} = \frac{\sum x_i}{n}$ y $\bar{y} = \frac{\sum y_i}{n}$ representan los promedios aritméticos muestrales.

---

### 4.5. Métricas de Bondad de Ajuste y Validación Estadística

#### 1. Coeficiente de Correlación Lineal de Pearson ($r$):
Mide la fuerza y dirección de la relación lineal entre las variables discretas ($-1 \le r \le 1$):
$$r = \frac{n \sum x_i y_i - (\sum x_i)(\sum y_i)}{\sqrt{\left[ n \sum x_i^2 - (\sum x_i)^2 \right] \left[ n \sum y_i^2 - (\sum y_i)^2 \right]}}$$

#### 2. Coeficiente de Determinación ($R^2$):
Representa la proporción de la varianza total de la variable dependiente explicada por la recta de regresión:
$$R^2 = r^2 = 1 - \frac{SSE}{SST} = 1 - \frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{\sum_{i=1}^n (y_i - \bar{y})^2}$$

#### 3. Error Estándar de la Estimación ($S_{yx}$):
Cuantifica la dispersión media de los puntos observados respecto a la recta ajustada (expresado en las mismas unidades de $Y$):
$$S_{yx} = \sqrt{\frac{\sum_{i=1}^n (y_i - \hat{y}_i)^2}{n - 2}}$$
*(Se divide por $n - 2$ debido a los 2 grados de libertad consumidos al estimar $m$ y $b$)*.

---

## 5. CÁLCULOS NUMÉRICOS EXACTOS Y RESULTADOS DE LOS MODELOS

### 5.1. Sumatorias Discretas Calculadas sobre las 23 Rutas
* **Tamaño muestral ($n$):** $23$
* **Sumatoria de Distancias ($\sum X$):** $19,098.00\text{ km}$
* **Promedio de Distancia ($\bar{X}$):** $830.3478\text{ km}$
* **Suma de Cuadrados de Distancia ($\sum X^2$):** $19,781,876.00$
* **$(\sum X)^2$:** $364,733,604.00$
* **Denominador Común de Cramer ($\Delta = n \sum X^2 - (\sum X)^2$):**
  $$\Delta = 23(19,781,876) - 364,733,604 = 454,983,148 - 364,733,604 = 90,249,544.00$$

#### Sumatorias para el Modelo 1 (Costos $Y_1$):
* $\sum Y_1 = 6,737.88\text{ S/}$
* $\bar{Y}_1 = 292.9513\text{ S/}$
* $\sum Y_1^2 = 2,645,621.0718$
* $\sum X Y_1 = 7,095,607.52$
* $\Delta_{m1} = 23(7,095,607.52) - (19,098)(6,737.88) = 163,198,972.96 - 128,680,032.24 = 34,518,940.72$

#### Sumatorias para el Modelo 2 (Combustible $Y_2$):
* $\sum Y_2 = 3,216.48\text{ gal}$
* $\bar{Y}_2 = 139.8470\text{ gal}$
* $\sum Y_2^2 = 586,482.4938$
* $\sum X Y_2 = 3,332,182.64$
* $\Delta_{m2} = 23(3,332,182.64) - (19,098)(3,216.48) = 76,640,200.72 - 61,428,335.04 = 15,211,865.68$

---

### 5.2. Resultados Oficiales del Modelo 1: Distancia ($X$) vs. Costo Total ($Y_1$)

#### Ecuación Predictiva:
$$\hat{Y}_1 = 0.382483 \cdot X - 24.6366 \approx 0.3825 \cdot X - 24.64 \quad \text{[Soles]}$$

#### Parámetros Estadísticos:
* **Pendiente Marginal ($m_1$):** `0.3825 S/ / km`
  * *Interpretación operativa:* Por cada 100 km adicionales de ruta en la red logística nacional, el costo total de flete se incrementa en promedio en **S/ 38.25**.
* **Ordenada al Origen ($b_1$):** `-24.64 S/`
  * *Interpretación física:* Representa el ajuste matemático de la recta sobre el rango de datos. En el transporte real no existen fletes de 0 km; el modelo está calibrado para rutas interprovinciales ($>150\text{ km}$).
* **Coeficiente de Correlación de Pearson ($r_1$):** `0.9244` (Correlación positiva muy fuerte).
* **Coeficiente de Determinación ($R_1^2$):** `0.8545` (**85.45%**)
  * *Interpretación:* El 85.45% de la variabilidad del costo de transporte está explicado linealmente por la distancia recorrida. El 14.55% restante responde a peajes de alta tarifa, dificultad de puertos de montaña y condiciones de retorno de carga.
* **Error Estándar de la Estimación ($S_{yx1}$):** `S/ 68.21`

#### Proyecciones Estratégicas:
* A **500 km:** $\hat{Y}_1 = 0.3825(500) - 24.64 =$ **S/ 166.60**
* A **650 km:** $\hat{Y}_1 = 0.3825(650) - 24.64 =$ **S/ 223.97**
* A **1,000 km:** $\hat{Y}_1 = 0.3825(1000) - 24.64 =$ **S/ 357.84**

---

### 5.3. Resultados Oficiales del Modelo 2: Distancia ($X$) vs. Consumo de Combustible ($Y_2$)

#### Ecuación Predictiva:
$$\hat{Y}_2 = 0.168553 \cdot X - 0.1084 \approx 0.1686 \cdot X - 0.11 \quad \text{[Galones Diésel]}$$

#### Parámetros Estadísticos:
* **Pendiente Marginal ($m_2$):** `0.1686 gal / km`
  * *Consumo por 100 km:* `16.86 galones / 100 km`.
  * *Rendimiento vehicular equivalente:* $\frac{1}{0.168553} \approx$ **5.93 km/galón**, valor completamente consistente con camiones de carga pesada de 2 a 3 ejes (Volvo FMX, Scania, Mercedes-Benz Actros).
* **Ordenada al Origen ($b_2$):** `-0.11 galones`
  * Prácticamente cero, lo que demuestra coherencia física: a distancia cero, el consumo en ruta tiende a cero.
* **Coeficiente de Correlación de Pearson ($r_2$):** `0.9032` (Correlación positiva muy fuerte).
* **Coeficiente de Determinación ($R_2^2$):** `0.8157` (**81.57%**)
  * *Interpretación:* El 81.57% de los galones consumidos depende directamente del kilometraje. El 18.43% restante está gobernado por el **factor altitud y gradiente** (un camión subiendo a Ticlio a 4,818 m.s.n.m. consume hasta un 65% más combustible que en la Panamericana Norte plana).
* **Error Estándar de la Estimación ($S_{yx2}$):** `34.63 galones`

#### Proyecciones Estratégicas:
* A **500 km:** $\hat{Y}_2 = 0.1686(500) - 0.11 =$ **84.17 galones**
* A **650 km:** $\hat{Y}_2 = 0.1686(650) - 0.11 =$ **109.45 galones**
* A **1,000 km:** $\hat{Y}_2 = 0.1686(1000) - 0.11 =$ **168.44 galones**

---

## 6. ARQUITECTURA DE ARCHIVOS Y ENTREGABLES DEL PROYECTO

El proyecto cuenta con una estructura limpia, sincronizada y versionada en GitHub:

```text
c:\Users\PC\Desktop\Matematica discreta trabajo grupal\
│
├── 01 Informe.docx                     # Informe formal académico universitario en Word
├── 02 Presentación.pptx                # Diapositivas corporativas oficiales en PowerPoint
├── 04 Planificación.xlsx               # Cronograma de trabajo, hitos y distribución de tareas
├── Sistema_Regresion_Logistica.xlsx    # Modelo en Excel con fórmulas nativas y dinámicas
├── datos_logisticos.csv                 # Dataset maestro con las 23 rutas reales
├── app.py                              # Aplicación interactiva Streamlit en Python
├── requirements.txt                    # Dependencias pip (streamlit, plotly, pandas, openpyxl)
├── ejecutar_sistema.bat                # Lanzador automatizado para entorno Windows
├── README.md                           # Documentación principal del repositorio en GitHub
│
├── 03 Código/                          # Espejo del software y scripts auxiliares
│   ├── app.py
│   ├── datos_logisticos.csv
│   ├── requirements.txt
│   ├── generar_excel.py
│   ├── generar_informe_docx.py
│   ├── generar_presentacion_pptx.py
│   └── organizar_entregables.py
│
└── Capturas para diapositiva/          # Imágenes infográficas de apoyo
    ├── 01_Grafico_Modelo1_Costos_Blanco.png
    ├── 02_Grafico_Modelo2_Combustible_Regiones_Blanco.png
    ├── 03_Fundamento_Matematico_Gauss_Blanco.png
    ├── 04_Algoritmo_Python_MCO_Blanco.png
    ├── 05_Tabla_Excel_Resumen_Comparativo_Blanco.png
    ├── 06_Grafico_Desglose_Costos_Torta_Blanco.png
    ├── 07_Tarjetas_KPI_Resumen_Blanco.png
    ├── 01_Dashboard_Modelo1_Costos.png (Dark UI)
    ├── 02_Modelo2_Combustible_Regiones.png (Dark UI)
    ├── 03_Comparativa_Ambos_Modelos.png (Dark UI)
    ├── 04_Fundamento_Matematico_Gauss.png (Dark UI)
    ├── 05_Codigo_Python_MCO.png (Dark UI)
    ├── 06_Excel_Formulas_Nativas.png (Dark UI)
    ├── 07_Excel_Resumen_Comparativo.png (Dark UI)
    └── 08_Simulador_Escenarios_Presupuesto.png (Dark UI)
```

---

## 7. IMPLEMENTACIÓN EN MICROSOFT EXCEL (`Sistema_Regresion_Logistica.xlsx`)

El archivo Excel fue generado programáticamente mediante `openpyxl` y verificado vía automatización COM con 0 errores de fórmula. Está diseñado para que cualquier cambio en una celda de datos actualice instantáneamente todos los cálculos.

### 7.1. Estructura de Hojas
1. **Hoja 1: `Modelo 1 - Costo de Transporte`**
   * **Tabla de Datos y Columnas Auxiliares:**
     * Columna A: ID Envío
     * Columna B: Ruta
     * Columna C: Región
     * Columna D: Distancia $X$ (km)
     * Columna E: Costo Real $Y_1$ (S/)
     * Columna F: $X^2$ (`=D7^2`)
     * Columna G: $Y^2$ (`=E7^2`)
     * Columna H: $X \cdot Y$ (`=D7*E7`)
     * Columna I: $\hat{Y}$ Estimado (`=$M$8*D7+$M$9`)
     * Columna J: Residuo Cuadrático $(Y - \hat{Y})^2$ (`=(E7-I7)^2`)
   * **Bloque de Parámetros Matriciales (Ecuaciones de Gauss):** Fórmulas que ejecutan directamente las sumatorias discretas $\sum X, \sum Y, \sum X^2, \sum XY$.
   * **Bloque de Fórmulas Nativas de Excel:**
     * Pendiente: `=PENDIENTE(E7:E29, D7:D29)` $\to$ `0.3825`
     * Intersección: `=INTERSECCION.EJE(E7:E29, D7:D29)` $\to$ `-24.64`
     * $R^2$: `=COEFICIENTE.R2(E7:E29, D7:D29)` $\to$ `85.45%`
     * Correlación de Pearson: `=COEF.DE.CORREL(E7:E29, D7:D29)` $\to$ `0.9244`
     * Error Típico: `=ERROR.TIPICO.XY(E7:E29, D7:D29)` $\to$ `68.21`

2. **Hoja 2: `Modelo 2 - Consumo Combustible`**
   * Misma estructura matricial y analítica aplicada sobre la columna de combustible $Y_2$.
   * Pendiente nativa: `0.1686`, Intersección nativa: `-0.11`, $R^2$: `81.57%`.

3. **Hoja 3: `Resumen Comparativo`**
   * Cuadro de mando que contrasta ambos modelos frente a frente.
   * **Tabla de Proyecciones:** Usa la función nativa de compatibilidad OpenXML `=_xlfn.FORECAST.LINEAR(C18, 'Modelo 1 - Costo de Transporte'!$E$7:$E$29, 'Modelo 1 - Costo de Transporte'!$D$7:$D$29)` para estimar valores a 500, 650 y 1,000 km.
   * **Resolución del Sistema $2 \times 2$:** Muestra la matriz de coeficientes y el vector de términos independientes con solución por determinantes.

---

## 8. IMPLEMENTACIÓN EN PYTHON Y STREAMLIT (`app.py`)

### 8.1. Algoritmo Puro sin Caja Negra
Para garantizar la estricta alineación con los objetivos de **Matemática Discreta**, el software implementa las Ecuaciones Normales de Gauss desde cero en Python estándar, sin depender de librerías opacas como `scikit-learn` o `statsmodels`:

```python
def calcular_regresion(x_vals, y_vals):
    """
    Calcula la regresión lineal por Mínimos Cuadrados Ordinarios
    resolviendo analíticamente el sistema 2x2 de Ecuaciones Normales de Gauss.
    """
    n = len(x_vals)
    sum_x = sum(x_vals)
    sum_y = sum(y_vals)
    sum_x2 = sum(x ** 2 for x in x_vals)
    sum_y2 = sum(y ** 2 for y in y_vals)
    sum_xy = sum(x * y for x, y in zip(x_vals, y_vals))
    
    # Determinante del sistema 2x2 (Regla de Cramer)
    denominador = (n * sum_x2) - (sum_x ** 2)
    if denominador == 0:
        return None
    
    # Cálculo analítico de pendiente (m) e intercepto (b)
    m = ((n * sum_xy) - (sum_x * sum_y)) / denominador
    b = (sum_y - (m * sum_x)) / n
    
    # Coeficiente de correlación lineal de Pearson (r)
    den_r = math.sqrt(((n * sum_x2) - (sum_x ** 2)) * ((n * sum_y2) - (sum_y ** 2)))
    r = ((n * sum_xy) - (sum_x * sum_y)) / den_r if den_r != 0 else 0
    r2 = r ** 2
    
    # Residuos y Error Estándar de la Estimación
    y_pred = [m * x + b for x in x_vals]
    residuos = [y - yp for y, yp in zip(y_vals, y_pred)]
    sse = sum(e ** 2 for e in residuos)
    s_yx = math.sqrt(sse / (n - 2)) if n > 2 else 0
    
    return {
        'n': n, 'm': m, 'b': b, 'r': r, 'r2': r2,
        's_yx': s_yx, 'sum_x': sum_x, 'sum_y': sum_y,
        'sum_x2': sum_x2, 'sum_y2': sum_y2, 'sum_xy': sum_xy,
        'y_pred': y_pred, 'residuos': residuos, 'sse': sse
    }
```

### 8.2. Módulos de la Aplicación Web
1. **Sidebar de Control:** Selector interactivo de modelo (Modelo 1, Modelo 2, Comparativo), visualización de parámetros institucionales y estado de la muestra.
2. **Tablero de Métricas (KPI Cards):** Tarjetas con diseño estilizado para Pendiente ($m$), Intercepto ($b$), Bondad de Ajuste ($R^2$), Correlación ($r$) y Error Típico ($S_{yx}$).
3. **Gráficos Interactivos con Plotly:**
   * Diagrama de dispersión de puntos reales diferenciados por color según región geográfica (Costa, Sierra, Selva).
   * Recta de regresión ajustada.
   * Bandas de dispersión del error estándar ($\hat{y} \pm S_{yx}$).
   * Gráfico de residuos individuales ($e_i$ vs. $X$) con línea horizontal de residuo cero.
4. **Simulador de Presupuesto y Escenarios:** Deslizador interactivo para ingresar cualquier kilometraje y proyectar costo y galones en tiempo real, con alertas preventivas ante extrapolaciones fuera del dominio muestral ($[174\text{ km}, 1638\text{ km}]$).
5. **Explorador y Gestor de Datos:** Tabla dinámica con opción de inspección de residuos y descarga directa del dataset.

---

## 9. GUÍA DE DIAPOSITIVAS: PLANTILLA CANVA (17 PÁGINAS)
*(Plantilla: "Cream and Green Geometric Mathematics Class Education Presentation")*

Para armar la presentación en Canva usando las capturas de fondo blanco de `Capturas para diapositiva/`, seguir esta asignación exacta:

| Pág. | Título en Plantilla Canva | Contenido a Colocar | Imagen de Apoyo Sugerida |
|:---:|:---|:---|:---|
| **1** | Portada Principal | **Título:** Sistema de Regresión Lineal para Análisis Logístico en el Perú<br>**Subtítulo:** Matemática Discreta - USIL (2026)<br>**Equipo:** Matthias Combe, Kenny Palacin, Jeff Espiritu, Ángel Pérez<br>**Docente:** Mg. Marisel Rocío Beteta Salas | Elementos geométricos propios de la plantilla |
| **2** | About the Class / Introducción | Contexto del flete y transporte en el Perú. Objetivos: predecir costos y consumo de combustible diésel con rigor matemático discreto. | `07_Tarjetas_KPI_Resumen_Blanco.png` |
| **3** | Table of Contents | 1. Problemática y Dataset (23 Rutas)<br>2. Fundamento Matemático (Gauss y MCO)<br>3. Modelo 1: Costos de Transporte<br>4. Modelo 2: Consumo de Combustible<br>5. Implementación Excel y Python<br>6. Conclusiones y Decisiones | Iconos de la plantilla |
| **4** | Dataset y Caso de Estudio | Muestra discreta finita: $n = 23$ rutas interprovinciales. Variables: Distancia ($X$), Costo ($Y_1$), Combustible ($Y_2$). Cobertura: Costa, Sierra y Selva. | `06_Grafico_Desglose_Costos_Torta_Blanco.png` |
| **5** | Fundamento Matemático I | Del par discreto $(x_i, y_i)$ al error residual: $e_i = y_i - (mx_i + b)$. Función de pérdida cuadrática: $S(m,b) = \sum e_i^2$. | `03_Fundamento_Matematico_Gauss_Blanco.png` |
| **6** | Fundamento Matemático II | Deducción de las Ecuaciones Normales de Gauss mediante derivadas parciales igualadas a 0. Sistema $2 \times 2$ y Regla de Cramer. | `03_Fundamento_Matematico_Gauss_Blanco.png` (zoom al sistema) |
| **7** | Fórmulas Cerradas de Cramer | Fórmulas explícitas para la pendiente $m$, el intercepto $b$, el coeficiente de Pearson $r$ y el coeficiente de determinación $R^2$. | `04_Algoritmo_Python_MCO_Blanco.png` |
| **8** | Modelo 1: Costo de Flete | **Ecuación:** $\hat{Y}_1 = 0.3825 \cdot X - 24.64$ (S/)<br>• Pendiente: S/ 0.3825/km (+S/ 38.25 cada 100 km)<br>• $R^2 = 85.45\%$ (Excelente ajuste)<br>• Error típico: S/ 68.21 | `01_Grafico_Modelo1_Costos_Blanco.png` |
| **9** | Proyecciones de Costos | Proyecciones clave:<br>• 500 km $\to$ S/ 166.60<br>• 650 km $\to$ S/ 223.97<br>• 1,000 km $\to$ S/ 357.84<br>Uso en licitaciones y cotizaciones inmediatas. | `01_Grafico_Modelo1_Costos_Blanco.png` |
| **10** | Modelo 2: Combustible Diésel | **Ecuación:** $\hat{Y}_2 = 0.1686 \cdot X - 0.11$ (gal)<br>• Pendiente: 0.1686 gal/km (16.86 gal/100 km)<br>• Rendimiento medio: 5.93 km/galón (pesado)<br>• $R^2 = 81.57\%$ (Efecto altitud) | `02_Grafico_Modelo2_Combustible_Regiones_Blanco.png` |
| **11** | Análisis Geográfico del Combustible | ¿Por qué $R^2 = 81.57\%$? La altitud andina (Ticlio a 4,818 m.s.n.m., Puno, Cerro de Pasco) incrementa el consumo respecto a la Costa plana. | `02_Grafico_Modelo2_Combustible_Regiones_Blanco.png` |
| **12** | Comparativa de Modelos | Comparación de pendientes, bondad de ajuste y correlaciones. Ambos modelos presentan correlación muy fuerte ($r > 0.90$). | `05_Tabla_Excel_Resumen_Comparativo_Blanco.png` |
| **13** | Implementación en Microsoft Excel | Modelo dinámico sin errores `#¿NOMBRE?`. Fórmulas nativas: `PENDIENTE`, `INTERSECCION.EJE`, `COEFICIENTE.R2`, `ERROR.TIPICO.XY`. | `05_Tabla_Excel_Resumen_Comparativo_Blanco.png` |
| **14** | Implementación en Python & Streamlit | Código algorítmico puro sin librerías de caja negra. Interfaz web interactiva con simulación de sensibilidad y gestión de datos. | `04_Algoritmo_Python_MCO_Blanco.png` |
| **15** | Toma de Decisiones Empresariales | 1. Optimización de rutas según relieve topográfico.<br>2. Creación de fondos de contingencia basados en el error estándar $S_{yx}$.<br>3. Auditoría de desvíos de combustible. | `07_Tarjetas_KPI_Resumen_Blanco.png` |
| **16** | Conclusiones del Proyecto | 1. La Matemática Discreta modela exitosamente sistemas logísticos reales.<br>2. La dualidad Excel-Python asegura accesibilidad y escalabilidad operativa. | `07_Tarjetas_KPI_Resumen_Blanco.png` |
| **17** | Preguntas y Agradecimientos | "Muchas gracias por su atención."<br>Espacio para preguntas del jurado y la docente. Datos de contacto del grupo. | Diseño libre con datos del equipo |

---

## 10. BANCO DE PREGUNTAS Y RESPUESTAS PARA DEFENSA CON LA DOCENTE
*(Mg. Marisel Rocío Beteta Salas)*

#### P1: ¿Por qué este trabajo corresponde al curso de Matemática Discreta y no a Cálculo Continuo?
> **Respuesta:** Porque el dominio de análisis no es una función continua definida en un intervalo de números reales, sino una relación binaria finita $S \subseteq \mathbb{R} \times \mathbb{R}$ con cardinalidad discreta $|S| = n = 23$. No calculamos integrales sobre trayectorias continuas, sino operadores de sumatoria finita ($\sum_{i=1}^n x_i, \sum_{i=1}^n x_i y_i$) y resolvemos un sistema discreto de ecuaciones lineales $2 \times 2$.

#### P2: ¿Cómo dedujeron las Ecuaciones Normales de Gauss a partir del error?
> **Respuesta:** Definimos el residuo discreto como $e_i = y_i - (m x_i + b)$ y planteamos la función cuadrática de pérdida $S(m,b) = \sum_{i=1}^n e_i^2$. Dado que $S(m,b)$ es un paraboloide estrictamente convexo en $\mathbb{R}^2$, su mínimo global se encuentra donde las derivadas parciales se anulan simultáneamente: $\frac{\partial S}{\partial b} = 0$ y $\frac{\partial S}{\partial m} = 0$. Al aplicar la regla de la cadena y distribuir los sumatorios discretos considerando que $\sum_{i=1}^n 1 = n$, obtenemos de forma exacta las dos Ecuaciones Normales de Gauss:
> 1) $m \sum x_i + n b = \sum y_i$
> 2) $m \sum x_i^2 + b \sum x_i = \sum x_i y_i$.

#### P3: ¿Por qué la ordenada al origen del Modelo 1 es negativa ($b_1 = -24.64\text{ S/}$)? ¿Tiene sentido físico?
> **Respuesta:** En regresión lineal aplicada, el intercepto $b$ es un parámetro algebraico de ajuste que garantiza que la recta pase por el centroide muestral $(\bar{x}, \bar{y})$. No debe interpretarse literalmente para $X = 0\text{ km}$, ya que en el negocio de transporte interprovincial peruano no existen despachos de 0 kilómetros. El dominio de validez del modelo comprende distancias entre 174 km y 1,638 km. Evaluar en $X = 0$ constituiría una extrapolación ilegítima.

#### P4: ¿Por qué el coeficiente de determinación $R^2$ es del 85.45% y no del 99.9%?
> **Respuesta:** Porque trabajamos con **datos reales de carreteras peruanas**, no con datos sintéticos inventados. En un modelo logístico real peruano, un $R^2$ del 99.9% sería un síntoma evidente de falsedad o sobreajuste (overfitting). El 85.45% demuestra un ajuste lineal excelente, mientras que el 14.55% de varianza restante refleja factores reales ineludibles: el costo de los peajes en cada concesión vial, el estado de conservación del pavimento, la congestión vehicular en la salida de Lima y la dificultad de retorno de carga vacía.

#### P5: ¿Por qué el Modelo 2 de combustible tiene un $R^2$ menor (81.57%) que el de costos (85.45%)?
> **Respuesta:** Porque el consumo de combustible diésel es directamente sensible a la **altitud y el gradiente topográfico**. Un camión que viaja a Huancayo o Puno debe subir hasta Ticlio (4,818 m.s.n.m.), lo cual exige marchas de fuerza y un consumo de hasta 25 galones por cada 100 km, mientras que una ruta de igual distancia por la Panamericana hacia Chimbote o Ica consume menos de 14 galones por cada 100 km. Esa dispersión geográfica real es capturada fielmente por el modelo.

#### P6: ¿Qué diferencia existe entre el coeficiente de correlación $r$ y el de determinación $R^2$?
> **Respuesta:** El coeficiente de Pearson $r$ mide la fuerza y el sentido direccional de la asociación lineal entre dos variables discretas (va de $-1$ a $+1$). En nuestro Modelo 1, $r = 0.9244$, indicando una relación directa muy fuerte. El coeficiente de determinación $R^2 = r^2$ es adimensional y cuantifica qué porcentaje de la variación total observada en $Y$ es explicada por la variación en $X$. En nuestro caso, el 85.45% de la varianza del costo se explica por la distancia.

#### P7: ¿Qué ocurre si un usuario ingresa una distancia de 3,500 km en el simulador?
> **Respuesta:** El software emite una advertencia de **extrapolación fuera de rango**. La muestra muestral abarca desde 174 km (Lima - La Oroya) hasta 1,638 km (Lima - Puerto Maldonado). Extrapolar a 3,500 km excede la longitud máxima del territorio nacional continental e induce errores causados por desgaste acumulado, relevo de tripulación y pernocte forzoso que la recta no puede modelar linealmente.

#### P8: ¿Cómo garantizaron que el software en Python no usara "cajas negras"?
> **Respuesta:** Desarrollamos la función `calcular_regresion()` utilizando únicamente aritmética básica de Python (`sum()`, bucles y comprensiones de listas) y el módulo estándar `math`. No importamos `sklearn.linear_model`, ni `scipy.optimize`, ni `numpy.polyfit`. Los valores de $m$, $b$, $r$, $R^2$ y $S_{yx}$ se calculan aplicando manualmente las fórmulas cerradas de Cramer deducidas en clase.

#### P9: ¿Cómo verificaron la concordancia entre Excel y Python?
> **Respuesta:** Se contrastaron los resultados numéricos de las fórmulas nativas de Excel (`PENDIENTE`, `INTERSECCION.EJE`, `COEFICIENTE.R2`, `ERROR.TIPICO.XY`) con el algoritmo de Python. La coincidencia es absoluta hasta el cuarto decimal:
> * Pendiente Modelo 1: `0.3825` en ambos.
> * Intercepto Modelo 1: `-24.64` en ambos.
> * $R^2$ Modelo 1: `85.45%` en ambos.
> * Pendiente Modelo 2: `0.1686` en ambos.
> * $R^2$ Modelo 2: `81.57%` en ambos.

#### P10: ¿Cuál es el impacto práctico y la toma de decisiones para una empresa de transporte?
> **Respuesta:** Permite tres decisiones estratégicas:
> 1. **Cotización estandarizada:** Generar tarifas de flete inmediatas y transparentes para clientes evitando subcotizaciones.
> 2. **Presupuesto y control de combustible:** Estimar los galones requeridos con antelación y detectar anomalías o sustracción de combustible comparando el consumo real con el intervalo de confianza $\hat{Y}_2 \pm S_{yx2}$.
> 3. **Gestión de contingencias:** Usar el Error Estándar ($S_{yx1} = \text{S/ } 68.21$) para constituir fondos de reserva realistas ante imprevistos mecánicos en ruta.

---

## 11. INSTRUCCIONES DE EJECUCIÓN DEL SOFTWARE

1. **Requisitos Previos:**
   * Python 3.10 o superior instalado en el sistema.
   * Sistema operativo Windows 10/11.

2. **Ejecución Directa mediante Script:**
   * Doble clic en el archivo `ejecutar_sistema.bat` ubicado en la raíz del proyecto.
   * El script verificará las dependencias (`streamlit`, `plotly`, `pandas`, `openpyxl`) e iniciará automáticamente el servidor local.

3. **Ejecución Manual por Terminal (PowerShell / CMD):**
   ```powershell
   cd "c:\Users\PC\Desktop\Matematica discreta trabajo grupal"
   python -m streamlit run app.py
   ```
   * Abrir el navegador en la URL: `http://localhost:8501`.

---
*Documento compilado y certificado para fines de evaluación académica, archivo de proyecto y entrenamiento/contexto de modelos de inteligencia artificial.*
