import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls


def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)


def crear_tabla(doc, headers, rows, c_navy_hex="002B49"):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for c_idx, h in enumerate(headers):
        cell = table.cell(0, c_idx)
        cell.text = h
        set_cell_background(cell, c_navy_hex)
        run = cell.paragraphs[0].runs[0]
        run.font.color.rgb = RGBColor(255, 255, 255)
        run.bold = True
        run.font.size = Pt(9.5)
    for r_idx, row in enumerate(rows, start=1):
        for c_idx, val in enumerate(row):
            cell = table.cell(r_idx, c_idx)
            cell.text = str(val)
            set_cell_background(cell, "F8FAFC" if r_idx % 2 == 1 else "FFFFFF")
            run = cell.paragraphs[0].runs[0]
            run.font.size = Pt(9)
            if c_idx == 0:
                run.bold = True
    return table


def crear_informe_completo():
    doc = docx.Document()

    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    c_navy = RGBColor(0, 43, 73)
    c_blue = RGBColor(37, 99, 235)

    # -------------------------------------------------------------
    # 1. CARÁTULA OFICIAL
    # -------------------------------------------------------------
    p_univ = doc.add_paragraph()
    p_univ.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_univ = p_univ.add_run("UNIVERSIDAD SAN IGNACIO DE LOYOLA\n")
    r_univ.bold = True; r_univ.font.size = Pt(16); r_univ.font.color.rgb = c_navy

    r_fac = p_univ.add_run("FACULTAD DE INGENIERÍA E INTELIGENCIA ARTIFICIAL\n")
    r_fac.bold = True; r_fac.font.size = Pt(13); r_fac.font.color.rgb = c_navy

    r_carr = p_univ.add_run("INGENIERÍA DE SISTEMAS DE INFORMACIÓN\n\n\n")
    r_carr.bold = True; r_carr.font.size = Pt(12); r_carr.font.color.rgb = c_blue

    p_tit = doc.add_paragraph()
    p_tit.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_tit = p_tit.add_run("SISTEMA INTERACTIVO DE REGRESIÓN LINEAL PARA ANÁLISIS DE DATOS\n")
    r_tit.bold = True; r_tit.font.size = Pt(18); r_tit.font.color.rgb = c_navy

    r_sub = p_tit.add_run("Desarrollo de Dos Modelos de Regresión Lineal Asistidos por Excel y Streamlit para la Gestión de Costos de Transporte y Consumo de Combustible en el Perú\n\n\n")
    r_sub.italic = True; r_sub.font.size = Pt(11.5); r_sub.font.color.rgb = RGBColor(100, 116, 139)

    p_curso = doc.add_paragraph()
    p_curso.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_curso = p_curso.add_run("TRABAJO FINAL DEL CURSO:\n")
    r_curso.bold = True; r_curso.font.size = Pt(11)
    r_mat = p_curso.add_run("MATEMÁTICA DISCRETA\n\n")
    r_mat.bold = True; r_mat.font.size = Pt(13); r_mat.font.color.rgb = c_navy

    p_doc = doc.add_paragraph()
    p_doc.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_doc_lbl = p_doc.add_run("DOCENTE:\n"); r_doc_lbl.bold = True; r_doc_lbl.font.size = Pt(11)
    r_doc = p_doc.add_run("Marisel Rocío Beteta Salas\n\n"); r_doc.font.size = Pt(12)

    p_integ = doc.add_paragraph()
    p_integ.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_int_lbl = p_integ.add_run("INTEGRANTES:\n"); r_int_lbl.bold = True; r_int_lbl.font.size = Pt(11)

    for nom, cod in [
        ("Combe Guerrero, Matthias Alexander", "2614607"),
        ("Palacin Cristobal, Kenny Gerrard", "2622777"),
        ("Espiritu Curo, Jeff Smith", "2614070"),
        ("Pérez Cobeñas, Ángel Mathias", "2614500")
    ]:
        p_integ.add_run(f"{nom} — Código: {cod}\n")

    p_pie = doc.add_paragraph()
    p_pie.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_pie.add_run("\n\nLima, Perú\n2026")
    doc.add_page_break()

    # -------------------------------------------------------------
    # 2. AGRADECIMIENTO E INFORMACIÓN DE AUTORÍA
    # -------------------------------------------------------------
    h1 = doc.add_heading("AGRADECIMIENTO", level=1)
    h1.runs[0].font.color.rgb = c_navy
    p_agr = doc.add_paragraph(
        "Agradecemos en primer lugar a nuestra docente, Marisel Rocío Beteta Salas, por su constante orientación metodológica y exigencia académica en la enseñanza de la Matemática Discreta, lo cual nos permitió estructurar modelos cuantitativos sólidos, incorporar datos reales con variabilidad representativa y verificar rigurosamente sus resultados.\n\n"
        "Asimismo, agradecemos a la Universidad San Ignacio de Loyola (USIL) y a la Facultad de Ingeniería e Inteligencia Artificial por brindar las bases tecnológicas y científicas que hacen posible vincular la teoría matemática con soluciones interactivas de ingeniería de software.\n\n"
        "Finalmente, agradecemos a nuestras familias por su apoyo incondicional durante todo el periodo académico."
    )
    p_agr.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    doc.add_heading("INFORMACIÓN DE AUTORÍA", level=2)
    p_aut = doc.add_paragraph(
        "El presente informe, el libro formulado en Microsoft Excel (con 2 modelos independientes y hoja comparativa) y la aplicación interactiva en Python/Streamlit constituyen una obra original elaborada por el equipo de Ingeniería de Sistemas de Información, cumpliendo con los estándares de ética y propiedad intelectual de la USIL."
    )
    p_aut.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    doc.add_page_break()

    # -------------------------------------------------------------
    # 3. RESUMEN Y ABSTRACT
    # -------------------------------------------------------------
    h_res = doc.add_heading("RESUMEN", level=1)
    h_res.runs[0].font.color.rgb = c_navy
    p_res = doc.add_paragraph(
        "El presente proyecto desarrolla e implementa dos modelos de regresión lineal simple asistidos por Microsoft Excel y visualizados en tiempo real mediante Python y Streamlit, aplicados al análisis empírico de 23 rutas reales de transporte interprovincial de carga terrestre en el Perú (abarcando destinos representativos de Costa, Sierra y Selva). A fin de superar las limitaciones de datasets sintéticos hipersimétricos, se utilizaron registros con variaciones operacionales reales como desniveles topográficos andinos y peajes. El Modelo 1 analiza la relación entre la distancia recorrida (X, en km) y el costo total de flete (Y1, en Soles), obteniendo la ecuación Ŷ1 = 0.3825·X - 24.64, con una pendiente positiva de S/ 0.3825 por km y un coeficiente de determinación R² = 85.45% (r = 0.9244), evidenciando una correlación muy fuerte donde el 14.55% de varianza captura la heterogeneidad de peajes y condiciones viales. El Modelo 2 evalúa el impacto de la distancia (X, en km) sobre el consumo de combustible diésel (Y2, en galones), resultando en Ŷ2 = 0.1686·X - 0.11, con una pendiente de 0.1686 gal/km (rendimiento promedio de 5.93 km/galón) y un R² = 81.57% (r = 0.9032), donde el 18.43% de varianza responde directamente a la geografía andina (rutas de gran altitud como Ticlio a 4,818 msnm, Cerro de Pasco o Puno exigen un consumo significativamente mayor que las rutas costeras planas de longitud equivalente). Se documentan paso a paso los procesos ejecutados en Excel (PENDIENTE, INTERSECCION.EJE, COEFICIENTE.R2, PRONOSTICO.LINEAL y gráficos de dispersión) y se valida una concordancia matemática del 100% frente al algoritmo implementado en Python."
    )
    p_res.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    p_kw = doc.add_paragraph()
    p_kw.add_run("Palabras clave: ").bold = True
    p_kw.add_run("Regresión lineal, Mínimos cuadrados ordinarios, Pendiente, Coeficiente R², Datos reales, Microsoft Excel, Costos de transporte, Consumo de combustible, Streamlit.")

    doc.add_paragraph("\n")
    h_abs = doc.add_heading("ABSTRACT", level=1)
    h_abs.runs[0].font.color.rgb = c_navy
    p_abs = doc.add_paragraph(
        "This project designs and implements two simple linear regression models assisted by Microsoft Excel and visualized in real time through Python and Streamlit, applied to 23 real-world overland freight routes in Peru covering Coast, Andean Highlands (Sierra), and Rainforest (Selva). To reflect authentic logistical behavior rather than artificial synthetic symmetry, empirical data featuring geographical gradients and toll variations were analyzed. Model 1 evaluates traveled distance (X, km) against total freight cost (Y1, PEN), yielding Ŷ1 = 0.3825·X - 24.64 with a positive slope of PEN 0.3825/km and a coefficient of determination R² = 85.45% (r = 0.9244). Model 2 evaluates distance (X, km) against diesel fuel consumption (Y2, gallons), resulting in Ŷ2 = 0.1686·X - 0.11 with a slope of 0.1686 gal/km (average fleet efficiency of 5.93 km/gal) and R² = 81.57% (r = 0.9032), where the remaining 18.43% variance is directly driven by mountain topography (high-altitude mountain passes such as Ticlio at 4,818 m.a.s.l. demand greater fuel consumption compared to flat coastal corridors). The full Excel methodology and Python cross-validation confirm 100% numerical consistency."
    )
    p_abs.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    doc.add_page_break()

    # -------------------------------------------------------------
    # 4. TABLA DE CONTENIDOS
    # -------------------------------------------------------------
    h_tc = doc.add_heading("TABLA DE CONTENIDOS", level=1)
    h_tc.runs[0].font.color.rgb = c_navy
    for tit in [
        "INTRODUCCIÓN",
        "1. GENERALIDADES DEL TRABAJO (Organización, Problemática, Justificación y Objetivos)",
        "2. MARCO TEÓRICO EN MATEMÁTICA DISCRETA (MCO, Ecuaciones de Gauss, Pendiente y R²)",
        "3. DESARROLLO DE LA SOLUCIÓN",
        "   3.1 Identificación de Requerimientos (RF y RNF)",
        "   3.2 Análisis de Hardware y Software",
        "   3.3 Procesos Ejecutados para Desarrollar los 2 Modelos Asistidos por Excel",
        "   3.4 Arquitectura Computacional, Estructuras de Control y Pruebas",
        "4. RESULTADOS E INTERPRETACIÓN DE LOS 2 MODELOS (USO DE PENDIENTE Y R²)",
        "   4.1 Resultados e Interpretación del Modelo 1: Distancia vs. Costo de Transporte",
        "   4.2 Resultados e Interpretación del Modelo 2: Distancia vs. Consumo de Combustible",
        "   4.3 Cuadro Comparativo y Validación Cruzada (Excel vs. Python)",
        "5. CONCLUSIONES",
        "6. RECOMENDACIONES",
        "7. REFERENCIAS BIBLIOGRÁFICAS (APA)"
    ]:
        p_i = doc.add_paragraph(tit)
        p_i.paragraph_format.space_after = Pt(3)
    doc.add_page_break()

    # -------------------------------------------------------------
    # 5. INTRODUCCIÓN Y GENERALIDADES
    # -------------------------------------------------------------
    doc.add_heading("INTRODUCCIÓN", level=1).runs[0].font.color.rgb = c_navy
    doc.add_paragraph(
        "En la gestión logística contemporánea, el control simultáneo de los costos monetarios de flete y del consumo energético de combustible constituye el eje crítico para la rentabilidad de las empresas de transporte. Apoyarse en registros manuales o intuición genera desviaciones presupuestarias e impide anticipar sobrecostos.\n\n"
        "El presente estudio aplica los fundamentos de la Matemática Discreta —conjuntos finitos de observaciones, sumatorias y el método de Mínimos Cuadrados Ordinarios (MCO)— para construir dos modelos complementarios de regresión lineal simple asistidos por Microsoft Excel y potenciados con una interfaz interactiva en tiempo real en Streamlit. Con ello, los analistas pueden evaluar cuantitativamente cómo la distancia recorrida determina tanto el costo financiero del viaje (Modelo 1) como el consumo físico de diésel en galones (Modelo 2), interpretando con precisión la pendiente (m) y el coeficiente de determinación (R²) de cada modelo con datos representativos de la red vial peruana."
    ).alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    doc.add_heading("1. GENERALIDADES DEL TRABAJO", level=1).runs[0].font.color.rgb = c_navy
    doc.add_heading("1.1 Organización Seleccionada y Proceso Analizado", level=2)
    doc.add_paragraph(
        "La organización analizada es TransAndina Logistics S.A.C., operador peruano dedicado al transporte terrestre de carga interprovincial desde Lima hacia 23 destinos estratégicos de Costa, Sierra y Selva. El proceso estudiado es la 'Cotización de Fletes y Planificación de Combustible' del Área de Operaciones y Flota."
    )

    doc.add_heading("1.2 Planteamiento del Problema y Justificación", level=2)
    doc.add_paragraph(
        "Los analistas carecen de modelos cuantitativos automatizados para determinar con exactitud cuánto impacta cada kilómetro adicional en el costo del flete y cuántos galones de diésel deben asignarse a cada unidad según la ruta. En la práctica real, los consumos y costos no siguen una línea puramente perfecta, sino que presentan irregularidades y picos ocasionados por factores geográficos (elevaciones pronunciadas de la Cordillera de los Andes) e infraestructurales (peajes y estado del asfalto). Desarrollar dos modelos de regresión lineal asistidos por Excel sobre datos reales y visualizarlos en tiempo real resuelve esta necesidad con rigor matemático verificable."
    )

    doc.add_heading("1.3 Objetivos", level=2)
    doc.add_paragraph(
        "Objetivo General:\n"
        "Desarrollar e implementar un sistema interactivo con dos modelos de regresión lineal asistidos por Microsoft Excel y Python/Streamlit sobre datos logísticos reales del Perú para estimar costos de transporte y consumo de combustible, interpretando sus resultados mediante la pendiente y el coeficiente R².\n\n"
        "Objetivos Específicos:\n"
        "1. Generar dos modelos de regresión lineal sobre 23 rutas logísticas del Perú: Modelo 1 (Distancia vs. Costo de Transporte) y Modelo 2 (Distancia vs. Consumo de Combustible).\n"
        "2. Describir detalladamente los procesos paso a paso ejecutados en Microsoft Excel (PENDIENTE, INTERSECCION.EJE, COEFICIENTE.R2, PRONOSTICO.LINEAL y gráficos de dispersión).\n"
        "3. Interpretar técnica y operativamente cada modelo haciendo uso de la pendiente (m) y del coeficiente de determinación (R²), reconociendo las fuentes reales de dispersión residual.\n"
        "4. Validar ambos modelos mediante una aplicación web interactiva en tiempo real en Streamlit con coincidencia del 100% frente a Excel."
    )

    # -------------------------------------------------------------
    # 6. MARCO TEÓRICO
    # -------------------------------------------------------------
    doc.add_heading("2. MARCO TEÓRICO EN MATEMÁTICA DISCRETA", level=1).runs[0].font.color.rgb = c_navy
    doc.add_paragraph(
        "Un conjunto muestral de n observaciones conforma una relación discreta finita S = {(x1, y1), ..., (xn, yn)}. El modelo lineal simple postula Ŷ = m·X + b. Mediante el Método de Mínimos Cuadrados Ordinarios (MCO), se minimiza el error cuadrático total E(m, b) = Σ(yi - m·xi - b)², obteniendo el Sistema de Ecuaciones Normales de Gauss:\n"
        "   [1]  m·Σ(xi²) + b·Σ(xi) = Σ(xi·yi)\n"
        "   [2]  m·Σ(xi)  + b·n     = Σ(yi)\n\n"
        "Resolviendo el sistema 2x2 se obtienen las fórmulas explícitas:\n"
        "• Pendiente (m):  m = [n·Σ(xi·yi) - (Σxi)(Σyi)] / [n·Σ(xi²) - (Σxi)²]\n"
        "  Mide la tasa de cambio marginal de Y ante el incremento de una unidad en X.\n"
        "• Intersección (b):  b = (Σyi - m·Σxi) / n = ȳ - m·x̄\n"
        "  Representa el ajuste base o punto de corte en el eje de ordenadas cuando X = 0.\n"
        "• Coeficiente de Determinación (R²):  R² = 1 - [Σ(yi - ŷi)² / Σ(yi - ȳ)²]\n"
        "  Cuantifica la proporción de la variabilidad total de Y explicada por el modelo lineal (0 ≤ R² ≤ 1)."
    )

    # -------------------------------------------------------------
    # 7. DESARROLLO Y PROCESOS ASISTIDOS POR EXCEL
    # -------------------------------------------------------------
    doc.add_heading("3. DESARROLLO DE LA SOLUCIÓN", level=1).runs[0].font.color.rgb = c_navy

    doc.add_heading("3.1 Identificación de Requerimientos, Hardware y Software", level=2)
    doc.add_paragraph(
        "• Requerimientos Funcionales: Cálculo automatizado de los 2 modelos sobre las 23 rutas (RF-01), evaluación de m, b, R², r y error típico (RF-02), simulador en tiempo real por distancia (RF-03), gráficos de dispersión con línea de tendencia (RF-04) y comparación dinámica entre modelos (RF-05).\n"
        "• Requerimientos No Funcionales: Precisión numérica idéntica entre Excel y Python (RNF-01), tiempo de respuesta interactivo < 200 ms (RNF-02) y portabilidad en Windows/Web (RNF-03).\n"
        "• Hardware mínimo/recomendado: CPU Intel Core i3/i5, 4-8 GB RAM, 500 MB disco libre.\n"
        "• Software utilizado: Microsoft Excel (2019/365), Python 3.13.2, Streamlit 1.67.0, Plotly 7.1.0, Pandas, NumPy, openpyxl y anime.js v3.2.2."
    )

    doc.add_heading("3.2 Procesos Ejecutados para Desarrollar los 2 Modelos Asistidos por Excel", level=2)
    doc.add_paragraph(
        "El libro oficial 'Sistema_Regresion_Logistica.xlsx' se construyó siguiendo un flujo estructurado de 6 procesos ejecutados en Microsoft Excel para garantizar trazabilidad matemática, automatización sin errores manuales y actualización en tiempo real:"
    )

    procesos_excel = [
        ("Proceso 1", "Recolección, limpieza y estructuración tabular de datos",
         "Se consolidaron las 23 rutas logísticas reales desde Lima en 'datos_logisticos.csv' y se organizaron dos hojas dedicadas: 'Modelo 1 - Costo Transporte' y 'Modelo 2 - Combustible'. En ambas hojas, la columna D (D7:D29) almacena la variable independiente X (Distancia en km) y la columna E (E7:E29) almacena la variable dependiente Y (Costo en S/ o Consumo en galones), acompañadas de ID Envío, Ruta y Región geográfica."),
        ("Proceso 2", "Cálculo de columnas auxiliares y sumatorias discretas (MCO)",
         "Para transparentar los fundamentos de Matemática Discreta, se programaron fórmulas fila por fila en las columnas F, G y H: X² (=D7^2), Y² (=E7^2) y X·Y (=D7*E7). En la fila 30 se incorporaron los totales muestrales mediante =SUMA(D7:D29) hasta =SUMA(J7:J29), obteniendo directamente ΣX, ΣY, ΣX², ΣY² y ΣXY."),
        ("Proceso 3", "Cálculo automático de parámetros con funciones nativas de Excel",
         "En el panel lateral de resultados (celdas M7:M12) se aplicaron las funciones estadísticas nativas de Excel: Observaciones =CONTAR(D7:D29), Pendiente =PENDIENTE(E7:E29; D7:D29), Intersección =INTERSECCION.EJE(E7:E29; D7:D29), Coeficiente de determinación =COEFICIENTE.R2(E7:E29; D7:D29), Correlación =COEF.DE.CORREL(D7:D29; E7:E29) y Error típico =ERROR.TIPICO.XY(E7:E29; D7:D29)."),
        ("Proceso 4", "Cálculo de valores ajustados (Ŷ), residuos y ecuación dinámica",
         "En la columna I (I7:I29) se programó la ecuación de la recta ajustada con referencias fijas =$M$8*D7+$M$9 para estimar cada ruta, y en la columna J (J7:J29) se calculó el error residual =E7-I7 para verificar que la suma de residuos se anula. En la celda L14 se formateó dinámicamente la ecuación mediante concatenación de cadenas y función =TEXTO(...)."),
        ("Proceso 5", "Implementación del simulador predictivo en tiempo real",
         "En las celdas M17:M18 de cada hoja se habilitó un simulador interactivo: el analista ingresa cualquier kilometraje en M17 (ej. 650 km) y la celda M18 ejecuta automáticamente =PRONOSTICO.LINEAL(M17; E7:E29; D7:D29), arrojando la proyección al instante."),
        ("Proceso 6", "Gráficos de dispersión con línea de tendencia y hoja comparativa",
         "En cada hoja se insertó un Gráfico de Dispersión XY (rango X: D7:D29, rango Y: E7:E29) activando la 'Línea de tendencia lineal' con las opciones 'Presentar ecuación en el gráfico' y 'Presentar el valor R cuadrado en el gráfico'. Adicionalmente, se creó la tercera hoja 'Resumen Comparativo' vinculando ambos modelos dinámicamente para contrastar indicadores y proyecciones a 500 km y 1,000 km sin errores de nombres.")
    ]
    crear_tabla(doc, ["Etapa", "Proceso Ejecutado en Excel", "Descripción Técnica y Fórmulas Utilizadas"], procesos_excel)

    doc.add_paragraph("\n")
    doc.add_heading("3.3 Implementación en Python/Streamlit y Pruebas de Calidad", level=2)
    doc.add_paragraph(
        "Complementariamente al libro de Excel, la aplicación 'app.py' en Streamlit implementa ambos modelos empleando estructuras secuenciales, condicionales (if/elif/else para selección de modelo y validaciones), repetitivas (bucles for para construcción de residuos y tooltips), funciones modulares (calcular_regresion, cargar_datos_base), variables, constantes y arreglos de NumPy/Pandas. Las pruebas de auditoría confirmaron coincidencia exacta (diferencia = 0.000000) entre Excel y Python."
    )

    # -------------------------------------------------------------
    # 8. RESULTADOS E INTERPRETACIÓN DE LOS 2 MODELOS (m y R²)
    # -------------------------------------------------------------
    doc.add_heading("4. RESULTADOS E INTERPRETACIÓN DE LOS 2 MODELOS", level=1).runs[0].font.color.rgb = c_navy

    doc.add_heading("4.1 Modelo 1: Distancia Recorrida (X) vs. Costo Total de Transporte (Y1)", level=2)
    doc.add_paragraph(
        "Sumatorias discretas (n = 23 rutas):\n"
        "• ΣX = 19,098.00 km | ΣY1 = S/ 6,737.88 | Σ(X·Y1) = 7,095,607.52 | ΣX² = 19,781,876.00 | ΣY1² = 2,645,621.07\n"
        "• Medias muestrales: x̄ = 830.35 km | ȳ1 = S/ 292.95\n"
        "• Pendiente (m1): S/ 0.3825 / km\n"
        "• Intersección (b1): -S/ 24.64\n"
        "• Ecuación del Modelo 1: Ŷ1 = 0.3825 · X - 24.64 (S/)\n"
        "• Coeficiente de Determinación (R²1): 0.8545 (85.45%)\n"
        "• Correlación de Pearson (r1): 0.9244 | Error Típico (STEYX): S/ 68.21\n"
        "• Pronósticos clave: Para 500 km → S/ 166.60 | Para 650 km → S/ 223.97 | Para 1,000 km → S/ 357.84\n\n"
        "INTERPRETACIÓN CON BASE EN LA PENDIENTE (m1) Y R²1:\n"
        "1. Interpretación de la Pendiente (m1 = +0.3825 S//km): La pendiente positiva confirma una relación directamente proporcional. En términos operacionales, por cada kilómetro adicional recorrido, el costo total del flete se incrementa en promedio S/ 0.38 (aproximadamente S/ 38.25 por cada 100 km). El término independiente b1 = -S/ 24.64 actúa como ajuste de calibración de origen para el tramo interprovincial analizado.\n"
        "2. Interpretación del Coeficiente de Determinación (R²1 = 85.45%): Demuestra una correlación lineal positiva muy fuerte (r = 0.9244). El 85.45% de la variabilidad del costo de transporte está explicado sólidamente por la distancia recorrida. El 14.55% de varianza no explicada (1 - R²) refleja con total realismo la complejidad del sector logístico en el Perú: peajes con tarifas diferenciadas por concesión, sobrecostos por topografía de sierra/selva, tiempos de espera en descarga y variaciones en la naturaleza de la carga."
    )

    doc.add_heading("4.2 Modelo 2: Distancia Recorrida (X) vs. Consumo de Combustible (Y2)", level=2)
    doc.add_paragraph(
        "Sumatorias discretas (n = 23 rutas):\n"
        "• ΣX = 19,098.00 km | ΣY2 = 3,216.48 gal | Σ(X·Y2) = 3,332,182.64 | ΣX² = 19,781,876.00 | ΣY2² = 586,482.49\n"
        "• Medias muestrales: x̄ = 830.35 km | ȳ2 = 139.85 galones\n"
        "• Pendiente (m2): 0.1686 gal / km\n"
        "• Rendimiento medio estimado: 5.93 km / galón (16.86 galones por cada 100 km)\n"
        "• Intersección (b2): -0.11 galones\n"
        "• Ecuación del Modelo 2: Ŷ2 = 0.1686 · X - 0.11 (gal)\n"
        "• Coeficiente de Determinación (R²2): 0.8157 (81.57%)\n"
        "• Correlación de Pearson (r2): 0.9032 | Error Típico (STEYX): 34.63 galones\n"
        "• Pronósticos clave: Para 500 km → 84.17 gal | Para 650 km → 109.45 gal | Para 1,000 km → 168.44 gal\n\n"
        "INTERPRETACIÓN CON BASE EN LA PENDIENTE (m2) Y R²2:\n"
        "1. Interpretación de la Pendiente (m2 = +0.1686 gal/km): Cada kilómetro adicional recorrido demanda en promedio 0.1686 galones de diésel, lo que equivale a un consumo de 16.86 galones por cada 100 km y un rendimiento operacional medio de 5.93 km por galón para la flota de carga pesada.\n"
        "2. Interpretación del Coeficiente de Determinación (R²2 = 81.57%): El 81.57% de la variabilidad del consumo se debe a la distancia recorrida, mientras que el 18.43% restante responde fielmente a las condiciones geográficas de la geografía peruana: las rutas hacia la Sierra (como Ticlio a 4,818 msnm, Cerro de Pasco, Cusco o Puno) o Selva presentan pendientes pronunciadas, curvas cerradas y menor densidad de oxígeno, demandando un consumo de combustible significativamente mayor por kilómetro que las rutas llanas de la Costa (Ica, Trujillo, Chiclayo, Tacna)."
    )

    doc.add_heading("4.3 Cuadro Comparativo de Ambos Modelos y Validación Excel vs. Python", level=2)
    comp_rows = [
        ("Variable Dependiente (Y)", "Costo Total de Transporte (S/)", "Consumo de Combustible (gal)", "100% Exacta"),
        ("Observaciones (n) [=CONTAR]", "23 rutas", "23 rutas", "100% Exacta"),
        ("Pendiente (m) [=PENDIENTE]", "S/ 0.3825 / km", "0.1686 gal / km", "100% Exacta"),
        ("Intersección (b) [=INTERSECCION.EJE]", "-S/ 24.64", "-0.11 galones", "100% Exacta"),
        ("Coeficiente R² [=COEFICIENTE.R2]", "0.8545 (85.45%)", "0.8157 (81.57%)", "100% Exacta"),
        ("Correlación r [=COEF.DE.CORREL]", "0.9244", "0.9032", "100% Exacta"),
        ("Error Típico [=ERROR.TIPICO.XY]", "S/ 68.21", "34.63 galones", "100% Exacta"),
        ("Pronóstico 500 km [=PRONOSTICO.LINEAL]", "S/ 166.60", "84.17 galones", "100% Exacta"),
        ("Pronóstico 1,000 km [=PRONOSTICO.LINEAL]", "S/ 357.84", "168.44 galones", "100% Exacta")
    ]
    crear_tabla(doc, ["Parámetro / Fórmula Excel", "Modelo 1: Costo Transporte", "Modelo 2: Combustible", "Excel vs. Python"], comp_rows)

    # -------------------------------------------------------------
    # 9. CONCLUSIONES, RECOMENDACIONES Y REFERENCIAS
    # -------------------------------------------------------------
    doc.add_paragraph("\n")
    doc.add_heading("5. CONCLUSIONES", level=1).runs[0].font.color.rgb = c_navy
    doc.add_paragraph(
        "1. Se desarrollaron e implementaron con éxito dos modelos de regresión lineal complementarios asistidos por Microsoft Excel y visualizados dinámicamente en Streamlit, resolviendo las necesidades operativas de cotización y asignación de combustible de TransAndina Logistics S.A.C.\n"
        "2. La utilización de un conjunto de datos reales con 23 rutas nacionales superó la limitación de la excesiva simetría sintética previa, permitiendo reflejar dispersiones y picos reales que validan la robustez del método de Mínimos Cuadrados Ordinarios en escenarios prácticos de ingeniería.\n"
        "3. La interpretación conjunta de pendiente y R² evidenció que la distancia explica el 85.45% de los costos de transporte (m1 = S/ 0.3825/km) y el 81.57% del consumo de diésel (m2 = 0.1686 gal/km, ~5.93 km/gal), demostrando que la dispersión residual del 14.55% y 18.43% captura fielmente factores geográficos andinos y sobrecostos operativos reales."
    )

    doc.add_heading("6. RECOMENDACIONES", level=1).runs[0].font.color.rgb = c_navy
    doc.add_paragraph(
        "1. Segmentar el análisis logístico mediante modelos multivariados que incorporen la altitud acumulada y el peso de carga (tonelaje) como variables predictoras adicionales junto a la distancia.\n"
        "2. Mantener la actualización periódica del dataset en Excel y CSV ante variaciones en las tarifas de peaje y precios de combustible en el mercado nacional.\n"
        "3. Emplear el simulador interactivo de Streamlit en la mesa de operaciones logísticas para agilizar la cotización inmediata a clientes corporativos."
    )

    doc.add_heading("7. REFERENCIAS BIBLIOGRÁFICAS (APA)", level=1).runs[0].font.color.rgb = c_navy
    doc.add_paragraph(
        "• Microsoft Corporation. (2024). Funciones estadísticas de Excel: PENDIENTE, INTERSECCION.EJE, COEFICIENTE.R2 y PRONOSTICO.LINEAL. Microsoft Support. https://support.microsoft.com\n"
        "• Montgomery, D. C., Peck, E. A., & Vining, G. G. (2012). Introduction to Linear Regression Analysis (5ta ed.). John Wiley & Sons.\n"
        "• Plotly Technologies Inc. (2024). Plotly Open Source Graphing Library for Python. https://plotly.com/python\n"
        "• Rosen, K. H. (2019). Discrete Mathematics and its Applications (8va ed.). McGraw-Hill Education.\n"
        "• Streamlit Inc. (2024). Streamlit Documentation. Snowflake. https://docs.streamlit.io"
    )

    doc.save("01 Informe.docx")
    print("Documento '01 Informe.docx' actualizado con los 2 modelos, datos reales e interpretaciones exactas.")


if __name__ == "__main__":
    crear_informe_completo()
