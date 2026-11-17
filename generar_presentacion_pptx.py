from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor


def crear_presentacion():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    c_cyan = RGBColor(0, 229, 255)
    c_orange = RGBColor(255, 107, 0)
    c_white = RGBColor(255, 255, 255)
    c_gray = RGBColor(148, 163, 184)
    c_dark = RGBColor(10, 22, 40)
    c_green = RGBColor(52, 211, 153)

    blank_layout = prs.slide_layouts[6]

    def agregar_fondo_oscuro(slide):
        bg = slide.shapes.add_shape(1, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = c_dark
        bg.line.color.rgb = c_dark
        return bg

    def agregar_encabezado(slide, titulo, seccion):
        agregar_fondo_oscuro(slide)
        bar = slide.shapes.add_shape(1, Inches(0.8), Inches(0.5), Inches(0.1), Inches(0.7))
        bar.fill.solid(); bar.fill.fore_color.rgb = c_cyan; bar.line.color.rgb = c_cyan

        txBox = slide.shapes.add_textbox(Inches(1.1), Inches(0.4), Inches(11.4), Inches(0.9))
        tf = txBox.text_frame; tf.word_wrap = True
        p_sec = tf.paragraphs[0]
        p_sec.text = seccion.upper(); p_sec.font.size = Pt(10); p_sec.font.bold = True; p_sec.font.color.rgb = c_cyan
        p_tit = tf.add_paragraph()
        p_tit.text = titulo; p_tit.font.size = Pt(22); p_tit.font.bold = True; p_tit.font.color.rgb = c_white

        footBox = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.7), Inches(0.4))
        p_foot = footBox.text_frame.paragraphs[0]
        p_foot.text = "USIL 2026 | Matemática Discreta — 2 Modelos de Regresión Lineal Asistidos por Excel y Streamlit"
        p_foot.font.size = Pt(9); p_foot.font.color.rgb = c_gray

    # SLIDE 1: PORTADA
    s1 = prs.slides.add_slide(blank_layout)
    agregar_fondo_oscuro(s1)
    tbox = s1.shapes.add_textbox(Inches(1.0), Inches(1.1), Inches(11.333), Inches(5.4))
    tf1 = tbox.text_frame; tf1.word_wrap = True
    for txt, sz, bld, col, ital in [
        ("UNIVERSIDAD SAN IGNACIO DE LOYOLA (USIL)", 14, True, c_cyan, False),
        ("FACULTAD DE INGENIERÍA E INTELIGENCIA ARTIFICIAL — ING. DE SISTEMAS", 11, False, c_gray, False),
        ("\nSISTEMA INTERACTIVO DE REGRESIÓN LINEAL\nPARA ANÁLISIS DE DATOS", 28, True, c_white, False),
        ("Dos Modelos Asistidos por Excel y Streamlit: Costos de Transporte y Consumo de Combustible", 14, False, c_orange, True),
        ("\nCurso: Matemática Discreta  |  Docente: Marisel Rocío Beteta Salas", 12, False, c_white, False),
        ("Equipo: Matthias Combe (2614607) • Kenny Palacin (2622777) • Jeff Espiritu (2614070) • Ángel Pérez (2614500)", 11, False, c_gray, False)
    ]:
        p = tf1.paragraphs[0] if txt.startswith("UNIVERSIDAD") else tf1.add_paragraph()
        p.text = txt; p.font.size = Pt(sz); p.font.bold = bld; p.font.italic = ital; p.font.color.rgb = col
        p.alignment = PP_ALIGN.CENTER

    # SLIDE 2: PROCESOS EN EXCEL
    s2 = prs.slides.add_slide(blank_layout)
    agregar_encabezado(s2, "Procesos Ejecutados para Desarrollar los Modelos Asistidos por Excel", "Metodología Excel")
    b = s2.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(11.4), Inches(5.1))
    tf = b.text_frame; tf.word_wrap = True
    pasos = [
        "1. Estructuración de Datos: 25 rutas del Perú organizadas en dos hojas independientes ('Modelo 1 - Costo Transporte' y 'Modelo 2 - Combustible'), con X en D7:D31 e Y en E7:E31.",
        "2. Sumatorias Discretas (MCO): Columnas formuladas X² (=D7^2), Y² (=E7^2), X·Y (=D7*E7) y totales en fila 32 con =SUMA(...).",
        "3. Funciones Estadísticas Nativas: =PENDIENTE(E7:E31; D7:D31), =INTERSECCION.EJE(...), =COEFICIENTE.R2(...), =COEF.DE.CORREL(...) y =ERROR.TIPICO.XY(...).",
        "4. Estimaciones y Residuos: Recta ajustada Ŷ (=$M$8*D7+$M$9) y error residual (=E7-I7) por cada ruta.",
        "5. Simulador Predictivo en Vivo: Celda editable M17 vinculada a =PRONOSTICO.LINEAL(M17; E7:E31; D7:D31).",
        "6. Gráficos y Hoja Comparativa: Dispersión XY con línea de tendencia (ecuación y R²) + hoja 'Resumen Comparativo' enlazada dinámicamente."
    ]
    for i, txt in enumerate(pasos):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = txt; p.font.size = Pt(13.5); p.font.color.rgb = c_white; p.space_after = Pt(10)

    # SLIDE 3: MODELO 1
    s3 = prs.slides.add_slide(blank_layout)
    agregar_encabezado(s3, "Modelo 1: Distancia Recorrida (X) vs. Costo de Transporte (Y1)", "Resultados e Interpretación")
    b1 = s3.shapes.add_textbox(Inches(0.9), Inches(1.7), Inches(5.4), Inches(4.8))
    tf = b1.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "PARÁMETROS EXACTOS (n = 25)"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = c_cyan
    for line in [
        "• Ecuación: Ŷ1 = 4.7776 · X + 253.94 (S/)",
        "• Pendiente (m1): S/ 4.7776 / km",
        "• Intersección (b1): S/ 253.94",
        "• Coeficiente R²1: 0.9998 (99.98%)",
        "• Correlación r1: 0.9999 | STEYX: S/ 29.44",
        "• Pronóstico 500 km: S/ 2,642.74",
        "• Pronóstico 1,000 km: S/ 5,031.55"
    ]:
        p = tf.add_paragraph(); p.text = line; p.font.size = Pt(13); p.font.color.rgb = c_white; p.space_after = Pt(6)

    b2 = s3.shapes.add_textbox(Inches(6.6), Inches(1.7), Inches(5.8), Inches(4.8))
    tf = b2.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "INTERPRETACIÓN (PENDIENTE Y R²)"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = c_orange
    for line in [
        "• Pendiente (m1 = +4.7776 S//km): Relación directa positiva. Cada km adicional eleva el flete en S/ 4.78 promedio, sobre un costo fijo base de S/ 253.94 (despacho, carga y gestión).",
        "• Coeficiente R²1 = 99.98%: Ajuste casi perfecto. El 99.98% de la variabilidad del costo es explicado por la distancia; solo el 0.02% responde a variaciones mínimas. Confiabilidad máxima para cotizaciones."
    ]:
        p = tf.add_paragraph(); p.text = line; p.font.size = Pt(13); p.font.color.rgb = c_white; p.space_after = Pt(12)

    # SLIDE 4: MODELO 2
    s4 = prs.slides.add_slide(blank_layout)
    agregar_encabezado(s4, "Modelo 2: Distancia Recorrida (X) vs. Consumo de Combustible (Y2)", "Resultados e Interpretación")
    b1 = s4.shapes.add_textbox(Inches(0.9), Inches(1.7), Inches(5.4), Inches(4.8))
    tf = b1.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "PARÁMETROS EXACTOS (n = 25)"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = c_cyan
    for line in [
        "• Ecuación: Ŷ2 = 0.1293 · X + 9.71 (gal)",
        "• Pendiente (m2): 0.1293 gal / km",
        "• Rendimiento medio: 7.74 km / galón",
        "• Intersección (b2): 9.71 galones",
        "• Coeficiente R²2: 0.9513 (95.13%)",
        "• Correlación r2: 0.9753 | STEYX: 12.42 gal",
        "• Pronóstico 500 km: 74.35 gal | 1,000 km: 139.00 gal"
    ]:
        p = tf.add_paragraph(); p.text = line; p.font.size = Pt(13); p.font.color.rgb = c_white; p.space_after = Pt(6)

    b2 = s4.shapes.add_textbox(Inches(6.6), Inches(1.7), Inches(5.8), Inches(4.8))
    tf = b2.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "INTERPRETACIÓN (PENDIENTE Y R²)"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = c_orange
    for line in [
        "• Pendiente (m2 = +0.1293 gal/km): Cada km recorrido consume en promedio 0.1293 galones de diésel (12.93 gal cada 100 km), partiendo de 9.71 gal de consumo fijo inicial (maniobras y tráfico de salida).",
        "• Coeficiente R²2 = 95.13%: Ajuste muy fuerte. El 4.87% no explicado (1 - R²) se debe a la geografía peruana: las rutas andinas (Sierra/Selva) demandan más combustible por km que las rutas planas de Costa."
    ]:
        p = tf.add_paragraph(); p.text = line; p.font.size = Pt(13); p.font.color.rgb = c_white; p.space_after = Pt(12)

    # SLIDE 5: COMPARATIVA Y VALIDACIÓN
    s5 = prs.slides.add_slide(blank_layout)
    agregar_encabezado(s5, "Comparativa de Ambos Modelos y Validación Cruzada Excel vs. Python", "Auditoría Matemática")
    tb = s5.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(11.3), Inches(4.8))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "CONCORDANCIA EXACTA DEL 100% ENTRE MICROSOFT EXCEL Y STREAMLIT:"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = c_green
    for line in [
        "• Modelo 1 (Costos): m1 = S/ 4.7776/km | b1 = S/ 253.94 | R²1 = 99.98% | 500 km = S/ 2,642.74",
        "• Modelo 2 (Combustible): m2 = 0.1293 gal/km | b2 = 9.71 gal | R²2 = 95.13% | 500 km = 74.35 gal",
        "• Diferencia numérica (Excel - Python): 0.000000 en todos los parámetros.",
        "• Valor Gerencial: Permite cotizar el flete (Modelo 1) y asignar los vales exactos de diésel (Modelo 2) en tiempo real desde la plataforma web."
    ]:
        p = tf.add_paragraph(); p.text = line; p.font.size = Pt(13.5); p.font.color.rgb = c_white; p.space_after = Pt(12)

    # SLIDE 6: CONCLUSIONES
    s6 = prs.slides.add_slide(blank_layout)
    agregar_encabezado(s6, "Conclusiones y Recomendaciones", "Cierre")
    tb = s6.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(11.3), Inches(4.8))
    tf = tb.text_frame; tf.word_wrap = True
    for i, c in enumerate([
        "1. Se generaron y validaron 2 modelos lineales complementarios en Excel (3 hojas formuladas) y Python/Streamlit.",
        "2. Los 6 procesos asistidos por Excel automatizan sumatorias discretas, coeficientes, residuos, gráficos y pronósticos.",
        "3. La interpretación de m y R² demostró que el costo (R² = 99.98%) sigue una estructura tarifaria casi lineal, mientras que el combustible (R² = 95.13%) refleja el impacto real de las pendientes andinas (4.87% residual).",
        "4. Recomendación: Ampliar el Modelo 2 a regresión múltiple incorporando altitud y tonelaje para superar el 99% de ajuste."
    ]):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = c; p.font.size = Pt(14); p.font.color.rgb = c_white; p.space_after = Pt(12)

    prs.save("02 Presentación.pptx")
    print("Presentación '02 Presentación.pptx' actualizada con los 2 modelos e interpretaciones.")


if __name__ == "__main__":
    crear_presentacion()
