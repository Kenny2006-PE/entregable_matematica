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
        "Agradecemos en primer lugar a nuestra docente, Marisel Rocío Beteta Salas, por su constante orientación metodológica y exigencia académica en la enseñanza de la Matemática Discreta, lo cual nos permitió estructurar modelos cuantitativos sólidos y verificar rigurosamente sus resultados.\n\n"
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
        "El presente proyecto desarrolla e implementa dos modelos de regresión lineal simple asistidos por Microsoft Excel y visualizados en tiempo real mediante Python y Streamlit, aplicados al análisis operativo de 25 rutas de transporte de carga terrestre en el Perú de la empresa modelo TransAndina Logistics S.A.C. El Modelo 1 analiza la relación entre la distancia recorrida (X, en km) y el costo total de transporte (Y1, en Soles), obteniendo la ecuación Ŷ1 = 4.7776·X + 253.94, con una pendiente positiva de S/ 4.78 por kilómetro adicional y un coeficiente de determinación R² = 99.98% (r = 0.9999), evidenciando un ajuste prácticamente perfecto. El Modelo 2 evalúa el impacto de la distancia recorrida (X, en km) sobre el consumo de combustible diésel (Y2, en galones), resultando en la ecuación Ŷ2 = 0.1293·X + 9.71, con una pendiente de 0.1293 gal/km (rendimiento promedio de 7.74 km/galón) y un R² = 95.13% (r = 0.9753), donde el 4.87% de variabilidad no explicada responde a la geografía andina (rutas de sierra/selva frente a rutas costeras planas). Se documentan paso a paso los procesos ejecutados en Excel (PENDIENTE, INTERSECCION.EJE, COEFICIENTE.R2, PRONOSTICO.LINEAL y gráficos de dispersión) y se demuestra una concordancia del 100% frente al algoritmo en Python."
    )
    p_res.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    p_kw = doc.add_paragraph()
    p_kw.add_run("Palabras clave: ").bold = True
    p_kw.add_run("Regresión lineal, Mínimos cuadrados ordinarios, Pendiente, Coeficiente R², Microsoft Excel, Costos de transporte, Consumo de combustible, Streamlit.")

    doc.add_paragraph("\n")
    h_abs = doc.add_heading("ABSTRACT", level=1)
    h_abs.runs[0].font.color.rgb = c_navy
    p_abs = doc.add_paragraph(
        "This project designs and implements two simple linear regression models assisted by Microsoft Excel and visualized in real time through Python and Streamlit, applied to 25 overland freight routes in Peru for TransAndina Logistics S.A.C. Model 1 evaluates traveled distance (X, km) against total transport cost (Y1, PEN), yielding Ŷ1 = 4.7776·X + 253.94 with a positive slope of PEN 4.78/km and a coefficient of determination R² = 99.98% (r = 0.9999). Model 2 evaluates distance (X, km) against diesel fuel consumption (Y2, gallons), resulting in Ŷ2 = 0.1293·X + 9.71 with a slope of 0.1293 gal/km (average efficiency 7.74 km/gal) and R² = 95.13% (r = 0.9753), where the remaining 4.87% variance reflects Peru's Andean topography. The complete Excel workflow and cross-validation against Python confirm 100% numerical precision."
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
        "El presente estudio aplica los fundamentos de la Matemática Discreta —conjuntos finitos de observaciones, sumatorias y el método de Mínimos Cuadrados Ordinarios (MCO)— para construir dos modelos complementarios de regresión lineal simple asistidos por Microsoft Excel y potenciados con una interfaz interactiva en tiempo real en Streamlit. Con ello, los analistas pueden evaluar cuantitativamente cómo la distancia recorrida determina tanto el costo financiero del viaje (Modelo 1) como el consumo físico de diésel en galones (Modelo 2), interpretando con precisión la pendiente (m) y el coeficiente de determinación (R²) de cada modelo."
    ).alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    doc.add_heading("1. GENERALIDADES DEL TRABAJO", level=1).runs[0].font.color.rgb = c_navy
    doc.add_heading("1.1 Organización Seleccionada y Proceso Analizado", level=2)
    doc.add_paragraph(
        "La organización analizada es TransAndina Logistics S.A.C., operador peruano dedicado al transporte terrestre de carga interprovincial desde Lima hacia 25 destinos de Costa, Sierra y Selva. El proceso estudiado es la 'Cotización de Fletes y Planificación de Combustible' del Área de Operaciones y Flota."
    )

    doc.add_heading("1.2 Planteamiento del Problema y Justificación", level=2)
    doc.add_paragraph(
        "Los analistas carecen de modelos cuantitativos automatizados para determinar con exactitud cuánto impacta cada kilómetro adicional en el costo total del flete y cuántos galones de diésel deben asignarse a cada unidad según la ruta. Esto provoca cotizaciones inexactas, faltantes o excesos de combustible y pérdidas operativas. Desarrollar dos modelos de regresión lineal asistidos por Excel y visualizados en tiempo real resuelve esta brecha con respaldo matemático verificable."
    )

    doc.add_heading("1.3 Objetivos", level=2)
    doc.add_paragraph(
        "Objetivo General:\n"
        "Desarrollar e implementar un sistema interactivo con dos modelos de regresión lineal asistidos por Microsoft Excel y Python/Streamlit para estimar costos de transporte y consumo de combustible en operaciones logísticas, interpretando sus resultados mediante la pendiente y el coeficiente R².\n\n"
        "Objetivos Específicos:\n"
        "1. Generar dos modelos de regresión lineal sobre 25 rutas logísticas del Perú: Modelo 1 (Distancia vs. Costo de Transporte) y Modelo 2 (Distancia vs. Consumo de Combustible).\n"
        "2. Describir detalladamente los procesos paso a paso ejecutados en Microsoft Excel (PENDIENTE, INTERSECCION.EJE, COEFICIENTE.R2, PRONOSTICO.LINEAL y gráficos de dispersión).\n"
        "3. Interpretar técnica y operativamente cada modelo haciendo uso de la pendiente (m) y del coeficiente de determinación (R²).\n"
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
        "  Representa el valor base fijo esperado de Y cuando X = 0.\n"
        "• Coeficiente de Determinación (R²):  R² = 1 - [Σ(yi - ŷi)² / Σ(yi - ȳ)²]\n"
        "  Cuantifica el porcentaje de la variabilidad total de Y que es explicado linealmente por X (0 ≤ R² ≤ 1)."
    )

    # -------------------------------------------------------------
    # 7. DESARROLLO Y PROCESOS ASISTIDOS POR EXCEL
    # -------------------------------------------------------------
    doc.add_heading("3. DESARROLLO DE LA SOLUCIÓN", level=1).runs[0].font.color.rgb = c_navy

    doc.add_heading("3.1 Identificación de Requerimientos, Hardware y Software", level=2)
    doc.add_paragraph(
        "• Requerimientos Funcionales: Cálculo automatizado de los 2 modelos (RF-01), evaluación de m, b, R², r y error típico (RF-02), simulador en tiempo real por distancia (RF-03), gráficos de dispersión con línea de tendencia (RF-04) y comparación dinámica entre modelos (RF-05).\n"
        "• Requerimientos No Funcionales: Precisión exacta a 6 decimales entre Excel y Python (RNF-01), tiempo de respuesta interactivo < 200 ms (RNF-02) y portabilidad en Windows/Web (RNF-03).\n"
        "• Hardware mínimo/recomendado: CPU Intel Core i3/i5, 4-8 GB RAM, 500 MB disco libre.\n"
        "• Software utilizado: Microsoft Excel (2019/365), Python 3.13.2, Streamlit 1.67.0, Plotly 7.1.0, Pandas, NumPy, openpyxl y anime.js v3.2.2."
    )

    doc.add_heading("3.2 Procesos Ejecutados para Desarrollar los 2 Modelos Asistidos por Excel", level=2)
    doc.add_paragraph(
        "El libro oficial 'Sistema_Regresion_Logistica.xlsx' se construyó siguiendo un flujo estructurado de 6 procesos ejecutados en Microsoft Excel para garantizar trazabilidad matemática, automatización sin errores manuales y actualización en tiempo real:"
    )

    procesos_excel = [
        ("Proceso 1", "Recolección, limpieza y estructuración tabular de datos",
         "Se consolidaron las 25 rutas logísticas desde Lima en 'datos_logisticos.csv' y se organizaron dos hojas dedicadas: 'Modelo 1 - Costo Transporte' y 'Modelo 2 - Combustible'. En ambas hojas, la columna D (D7:D31) almacena la variable independiente X (Distancia en km) y la columna E (E7:E31) almacena la variable dependiente Y (Costo en S/ o Consumo en galones), acompañadas de ID Envío, Ruta y Región."),
        ("Proceso 2", "Cálculo de columnas auxiliares y sumatorias discretas (MCO)",
         "Para demostrar la base de Matemática Discreta, se programaron fórmulas fila por fila en las columnas F, G y H: X² (=D7^2), Y² (=E7^2) y X·Y (=D7*E7). En la fila 32 se incorporaron totales mediante =SUMA(D7:D31) hasta =SUMA(J7:J31), obteniendo directamente ΣX, ΣY, ΣX², ΣY² y ΣXY."),
        ("Proceso 3", "Cálculo automático de parámetros con funciones nativas de Excel",
         "En el panel lateral de resultados (celdas M7:M12) se aplicaron las funciones estadísticas integradas de Excel en lugar de cálculos manuales: Observaciones =CONTAR(D7:D31), Pendiente =PENDIENTE(E7:E31; D7:D31) [=SLOPE], Intersección =INTERSECCION.EJE(E7:E31; D7:D31) [=INTERCEPT], Coeficiente de determinación =COEFICIENTE.R2(E7:E31; D7:D31) [=RSQ], Correlación =COEF.DE.CORREL(D7:D31; E7:E31) [=CORREL] y Error típico =ERROR.TIPICO.XY(E7:E31; D7:D31) [=STEYX]."),
        ("Proceso 4", "Cálculo de valores ajustados (Ŷ), residuos y ecuación dinámica",
         "En la columna I (I7:I31) se programó la ecuación de la recta ajustada con referencias absolutas =$M$8*D7+$M$9 para estimar cada envío, y en la columna J (J7:J31) se calculó el error residual =E7-I7 para verificar que la suma de residuos tiende a cero. En la celda L14 se construyó dinámicamente el texto de la ecuación mediante concatenación y formato =TEXTO(...)."),
        ("Proceso 5", "Implementación del simulador predictivo en tiempo real",
         "En las celdas M17:M18 de cada hoja se implementó un simulador interactivo: el analista digita cualquier distancia nueva en M17 (ej. 650 km) y la celda M18 ejecuta automáticamente =PRONOSTICO.LINEAL(M17; E7:E31; D7:D31) [=FORECAST.LINEAR], proyectando el costo o combustible al instante."),
        ("Proceso 6", "Gráficos de dispersión con línea de tendencia y hoja comparativa",
         "En cada hoja se insertó un Gráfico de Dispersión XY (rango X: D7:D31, rango Y: E7:E31) activando la 'Línea de tendencia lineal' con las opciones 'Presentar ecuación en el gráfico' y 'Presentar el valor R cuadrado en el gráfico'. Finalmente, se creó la tercera hoja 'Resumen Comparativo' vinculando ambos modelos mediante referencias entre hojas para contrastar m, b, R² y proyecciones a 500 km y 1,000 km.")
    ]
    crear_tabla(doc, ["Etapa", "Proceso Ejecutado en Excel", "Descripción Técnica y Fórmulas Utilizadas"], procesos_excel)

    doc.add_paragraph("\n")
    doc.add_heading("3.3 Implementación en Python/Streamlit y Pruebas de Calidad", level=2)
    doc.add_paragraph(
        "Complementariamente al libro de Excel, la aplicación 'app.py' en Streamlit implementa ambos modelos empleando estructuras secuenciales, condicionales (if/elif/else para selección de modelo y validaciones), repetitivas (bucles for para construcción de residuos y tooltips), funciones modulares (calcular_regresion, cargar_datos_base), variables, constantes y arreglos de NumPy/Pandas. Las pruebas de auditoría (CP-01 a CP-05) confirmaron coincidencia exacta (diferencia = 0.000000) entre Excel y Python."
    )

    # -------------------------------------------------------------
    # 8. RESULTADOS E INTERPRETACIÓN DE LOS 2 MODELOS (m y R²)
    # -------------------------------------------------------------
    doc.add_heading("4. RESULTADOS E INTERPRETACIÓN DE LOS 2 MODELOS", level=1).runs[0].font.color.rgb = c_navy

    doc.add_heading("4.1 Modelo 1: Distancia Recorrida (X) vs. Costo Total de Transporte (Y1)", level=2)
    doc.add_paragraph(
        "Sumatorias discretas (n = 25): ΣX = 14,620 km | ΣY1 = S/ 76,197.13 | Σ(X·Y1) = 64,364,356.00 | ΣX² = 12,695,000\n"
        "• Pendiente (m1): 4.7776 S//km\n"
        "• Intersección (b1): S/ 253.94\n"
        "• Ecuación del Modelo 1: Ŷ1 = 4.7776 · X + 253.94\n"
        "• Coeficiente de Determinación (R²1): 0.9998 (99.98%)\n"
        "• Correlación de Pearson (r1): 0.9999 | Error Típico (STEYX): S/ 29.44\n"
        "• Pronósticos clave: Para 500 km → S/ 2,642.74 | Para 650 km → S/ 3,359.39 | Para 1,000 km → S/ 5,031.55\n\n"
        "INTERPRETACIÓN CON BASE EN LA PENDIENTE (m1) Y R²1:\n"
        "1. Interpretación de la Pendiente (m1 = +4.7776 S//km): Al ser positiva, confirma una relación directamente proporcional entre distancia y costo. Operativamente, por cada kilómetro adicional que recorre un vehículo de carga, el costo total de transporte aumenta en promedio S/ 4.78 (cubriendo combustible, desgaste vehicular, viáticos y peajes). Además, la intersección b1 = S/ 253.94 representa el costo fijo base de despacho, estiba y gestión administrativa antes de iniciar ruta.\n"
        "2. Interpretación del Coeficiente de Determinación (R²1 = 99.98%): Indica un ajuste lineal prácticamente perfecto. El 99.98% de la variabilidad total del costo de transporte es explicado de manera directa por la distancia recorrida, mientras que únicamente el 0.02% restante (1 - R²) se atribuye a variaciones aleatorias menores. Esto valida que el Modelo 1 posee una precisión sobresaliente para presupuestar y cotizar fletes comerciales."
    )

    doc.add_heading("4.2 Modelo 2: Distancia Recorrida (X) vs. Consumo de Combustible (Y2)", level=2)
    doc.add_paragraph(
        "Sumatorias discretas (n = 25): ΣX = 14,620 km | ΣY2 = 2,132.95 gal | Σ(X·Y2) = 1,783,247.55 | ΣX² = 12,695,000\n"
        "• Pendiente (m2): 0.1293 gal/km\n"
        "• Intersección (b2): 9.71 galones\n"
        "• Ecuación del Modelo 2: Ŷ2 = 0.1293 · X + 9.71\n"
        "• Coeficiente de Determinación (R²2): 0.9513 (95.13%)\n"
        "• Correlación de Pearson (r2): 0.9753 | Error Típico (STEYX): 12.42 galones\n"
        "• Pronósticos clave: Para 500 km → 74.35 gal | Para 650 km → 93.75 gal | Para 1,000 km → 139.00 gal\n\n"
        "INTERPRETACIÓN CON BASE EN LA PENDIENTE (m2) Y R²2:\n"
        "1. Interpretación de la Pendiente (m2 = +0.1293 gal/km): Al ser positiva, demuestra que el consumo de diésel crece linealmente con la longitud del viaje. En términos técnicos, por cada kilómetro adicional recorrido la unidad consume en promedio 0.1293 galones de combustible, lo cual equivale a 12.93 galones cada 100 km y refleja un rendimiento medio de la flota de 7.74 km por galón (1 / 0.129281). La intersección b2 = 9.71 galones representa el consumo base fijo por viaje (maniobras de carga, ralentí y congestión de salida en Lima Metropolitana).\n"
        "2. Interpretación del Coeficiente de Determinación (R²2 = 95.13%): Evidencia un ajuste lineal muy fuerte y altamente confiable para la asignación de combustible. El 95.13% de la variabilidad del consumo de diésel se explica por la distancia recorrida. A diferencia del Modelo 1, existe un 4.87% de variabilidad no explicada (1 - R² = 0.0487), lo cual tiene una explicación física y geográfica concreta: las rutas andinas de Sierra y Selva (La Oroya, Huancayo, Ayacucho, Cajamarca, Cusco y Puno) demandan mayor esfuerzo del motor por pendientes pronunciadas y altura, generando un consumo ligeramente superior al de las rutas planas de la Costa (Cañete, Ica, Trujillo, Chiclayo, Piura y Tacna)."
    )

    doc.add_heading("4.3 Cuadro Comparativo de Ambos Modelos y Validación Excel vs. Python", level=2)
    comp_rows = [
        ("Variable Dependiente (Y)", "Costo Total de Transporte (S/)", "Consumo de Combustible (gal)", "100% Exacta"),
        ("Pendiente (m) [=PENDIENTE]", "S/ 4.7776 / km", "0.1293 gal / km", "100% Exacta"),
        ("Intersección (b) [=INTERSECCION.EJE]", "S/ 253.94", "9.71 galones", "100% Exacta"),
        ("Coeficiente R² [=COEFICIENTE.R2]", "0.9998 (99.98%)", "0.9513 (95.13%)", "100% Exacta"),
        ("Correlación r [=COEF.DE.CORREL]", "0.9999", "0.9753", "100% Exacta"),
        ("Error Típico [=ERROR.TIPICO.XY]", "S/ 29.44", "12.42 galones", "100% Exacta"),
        ("Pronóstico 500 km [=PRONOSTICO.LINEAL]", "S/ 2,642.74", "74.35 galones", "100% Exacta"),
        ("Pronóstico 1,000 km [=PRONOSTICO.LINEAL]", "S/ 5,031.55", "139.00 galones", "100% Exacta")
    ]
    crear_tabla(doc, ["Parámetro / Fórmula Excel", "Modelo 1: Costo Transporte", "Modelo 2: Combustible", "Excel vs. Python"], comp_rows)

    # -------------------------------------------------------------
    # 9. CONCLUSIONES, RECOMENDACIONES Y REFERENCIAS
    # -------------------------------------------------------------
    doc.add_paragraph("\n")
    doc.add_heading("5. CONCLUSIONES", level=1).runs[0].font.color.rgb = c_navy
    doc.add_paragraph(
        "1. Se generaron e implementaron exitosamente dos modelos de regresión lineal complementarios asistidos por Microsoft Excel y visualizados en tiempo real en Streamlit, resolviendo integralmente las necesidades de cotización financiera y asignación de combustible en logística.\n"
        "2. La sistematización del proceso en Excel (sumatorias discretas, funciones PENDIENTE, INTERSECCION.EJE, COEFICIENTE.R2, PRONOSTICO.LINEAL y gráficos de dispersión) elimina errores manuales y garantiza una concordancia exacta del 100% frente a Python.\n"
        "3. La interpretación conjunta de pendiente y R² reveló hallazgos críticos para la gerencia: el Modelo 1 explica el 99.98% del costo con una tasa de S/ 4.78/km, mientras que el Modelo 2 explica el 95.13% del combustible con una tasa de 0.1293 gal/km (7.74 km/galón), dejando en evidencia que el 4.87% residual obedece a la geografía andina de las rutas de sierra y selva."
    )

    doc.add_heading("6. RECOMENDACIONES", level=1).runs[0].font.color.rgb = c_navy
    doc.add_paragraph(
        "1. Segmentar el Modelo 2 (Combustible) en submodelos regionales (Costa vs. Sierra/Selva) o migrar a regresión lineal múltiple incluyendo la altitud promedio y el tonelaje transportado para elevar el R² por encima del 99%.\n"
        "2. Actualizar mensualmente el libro de Excel y el dataset CSV ante variaciones del precio del diésel en el mercado peruano para mantener vigentes las proyecciones del Modelo 1.\n"
        "3. Integrar la aplicación Streamlit con APIs cartográficas para capturar automáticamente la distancia y el desnivel geográfico de cada nueva ruta."
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
    print("Documento '01 Informe.docx' actualizado con los 2 modelos, procesos Excel e interpretaciones exactas.")


if __name__ == "__main__":
    crear_informe_completo()
