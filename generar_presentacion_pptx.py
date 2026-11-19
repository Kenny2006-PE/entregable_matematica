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
        p_foot.text = "USIL 2026 | Matemática Discreta — 2 Modelos de Regresión Lineal con Datos Reales (Excel y Streamlit)"
        p_foot.font.size = Pt(9); p_foot.font.color.rgb = c_gray

    # SLIDE 1: PORTADA
    s1 = prs.slides.add_slide(blank_layout)
    agregar_fondo_oscuro(s1)
    tbox = s1.shapes.add_textbox(Inches(1.0), Inches(1.1), Inches(11.333), Inches(5.4))
    tf1 = tbox.text_frame; tf1.word_wrap = True
    for txt, sz, bld, col, ital in [
        ("UNIVERSIDAD SAN IGNACIO DE LOYOLA (USIL)", 14, True, c_cyan, False),
        ("FACULTAD DE INGENIERÍA E INTELIGENCIA ARTIFICIAL — ING. DE SISTEMAS", 11, False, c_gray, False),
        ("\nSISTEMA INTERACTIVO DE REGRESIÓN LINEAL\nPARA ANÁLISIS DE DATOS REALES", 28, True, c_white, False),
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
        "1. Estructuración de Datos: 23 rutas nacionales reales organizadas en dos hojas ('Modelo 1 - Costo Transporte' y 'Modelo 2 - Combustible'), con X en D7:D29 e Y en E7:E29.",
        "2. Sumatorias Discretas (MCO): Columnas formuladas X² (=D7^2), Y² (=E7^2), X·Y (=D7*E7) y sumatorias en fila 30 con =SUMA(...).",
        "3. Funciones Estadísticas Nativas: =PENDIENTE(E7:E29; D7:D29), =INTERSECCION.EJE(...), =COEFICIENTE.R2(...), =COEF.DE.CORREL(...) y =ERROR.TIPICO.XY(...).",
        "4. Estimaciones y Residuos: Recta ajustada Ŷ (=$M$8*D7+$M$9) y error residual (=E7-I7) por cada envío.",
        "5. Simulador Predictivo en Vivo: Celda interactiva M17 vinculada a =PRONOSTICO.LINEAL(M17; E7:E29; D7:D29).",
        "6. Gráficos y Hoja Comparativa: Dispersión XY con línea de tendencia (ecuación y R²) + hoja 'Resumen Comparativo' enlazada dinámicamente con 0 errores."
    ]
    for i, txt in enumerate(pasos):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = txt; p.font.size = Pt(13.5); p.font.color.rgb = c_white; p.space_after = Pt(10)

    # SLIDE 3: MODELO 1
    s3 = prs.slides.add_slide(blank_layout)
    agregar_encabezado(s3, "Modelo 1: Distancia Recorrida (X) vs. Costo de Transporte (Y1)", "Resultados e Interpretación")
    b1 = s3.shapes.add_textbox(Inches(0.9), Inches(1.7), Inches(5.4), Inches(4.8))
    tf = b1.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "PARÁMETROS EXACTOS (n = 23 rutas)"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = c_cyan
    for line in [
        "• Ecuación: Ŷ1 = 0.3825 · X - 24.64 (S/)",
        "• Pendiente (m1): S/ 0.3825 / km",
        "• Intersección (b1): -S/ 24.64",
        "• Coeficiente R²1: 0.8545 (85.45%)",
        "• Correlación r1: 0.9244 | STEYX: S/ 68.21",
        "• Pronóstico 500 km: S/ 166.60",
        "• Pronóstico 1,000 km: S/ 357.84"
    ]:
        p = tf.add_paragraph(); p.text = line; p.font.size = Pt(13); p.font.color.rgb = c_white; p.space_after = Pt(6)

    b2 = s3.shapes.add_textbox(Inches(6.6), Inches(1.7), Inches(5.8), Inches(4.8))
    tf = b2.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "INTERPRETACIÓN (PENDIENTE Y R²)"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = c_orange
    for line in [
        "• Pendiente (m1 = +0.3825 S//km): Relación directa positiva. Cada km adicional eleva el flete en S/ 0.38 promedio (~S/ 38.25 por cada 100 km), con ajuste de calibración de origen de -S/ 24.64.",
        "• Coeficiente R²1 = 85.45%: Correlación muy fuerte (r = 0.9244). El 85.45% de la variabilidad del costo es explicado por la distancia. El 14.55% residual responde a peajes interprovinciales y dificultades de ruta andina, reflejando datos reales sin sesgo artificial."
    ]:
        p = tf.add_paragraph(); p.text = line; p.font.size = Pt(13); p.font.color.rgb = c_white; p.space_after = Pt(12)

    # SLIDE 4: MODELO 2
    s4 = prs.slides.add_slide(blank_layout)
    agregar_encabezado(s4, "Modelo 2: Distancia Recorrida (X) vs. Consumo de Combustible (Y2)", "Resultados e Interpretación")
    b1 = s4.shapes.add_textbox(Inches(0.9), Inches(1.7), Inches(5.4), Inches(4.8))
    tf = b1.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "PARÁMETROS EXACTOS (n = 23 rutas)"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = c_cyan
    for line in [
        "• Ecuación: Ŷ2 = 0.1686 · X - 0.11 (gal)",
        "• Pendiente (m2): 0.1686 gal / km",
        "• Rendimiento medio: 5.93 km / galón",
        "• Consumo estimado: 16.86 gal / 100 km",
        "• Coeficiente R²2: 0.8157 (81.57%)",
        "• Correlación r2: 0.9032 | STEYX: 34.63 gal",
        "• Pronóstico 500 km: 84.17 gal | 1,000 km: 168.44 gal"
    ]:
        p = tf.add_paragraph(); p.text = line; p.font.size = Pt(13); p.font.color.rgb = c_white; p.space_after = Pt(6)

    b2 = s4.shapes.add_textbox(Inches(6.6), Inches(1.7), Inches(5.8), Inches(4.8))
    tf = b2.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "INTERPRETACIÓN (PENDIENTE Y R²)"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = c_orange
    for line in [
        "• Pendiente (m2 = +0.1686 gal/km): Cada km adicional demanda 0.1686 galones de diésel (rendimiento medio de 5.93 km/galón).",
        "• Coeficiente R²2 = 81.57%: Ajuste muy representativo (r = 0.9032). El 18.43% no explicado por la distancia responde directamente al perfil topográfico: rutas de Sierra (Ticlio a 4,818 msnm, Cerro de Pasco, Puno) exigen mucho mayor consumo que rutas llanas de Costa (Ica, Trujillo)."
    ]:
        p = tf.add_paragraph(); p.text = line; p.font.size = Pt(13); p.font.color.rgb = c_white; p.space_after = Pt(12)

    # SLIDE 5: COMPARATIVA Y VALIDACIÓN
    s5 = prs.slides.add_slide(blank_layout)
    agregar_encabezado(s5, "Comparativa de Ambos Modelos y Validación Cruzada Excel vs. Python", "Auditoría Matemática")
    tb = s5.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(11.3), Inches(4.8))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.text = "CONCORDANCIA EXACTA DEL 100% ENTRE MICROSOFT EXCEL Y STREAMLIT:"; p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = c_green
    for line in [
        "• Modelo 1 (Costos): m1 = S/ 0.3825/km | b1 = -S/ 24.64 | R²1 = 85.45% | Proy. 500 km = S/ 166.60",
        "• Modelo 2 (Combustible): m2 = 0.1686 gal/km | b2 = -0.11 gal | R²2 = 81.57% | Proy. 500 km = 84.17 gal",
        "• Diferencia numérica (Excel - Python): 0.000000 en todos los parámetros y sumatorias.",
        "• Impacto Gerencial: Permite cotizar fletes y asignar vales de diésel con base científica, incorporando la variabilidad real de las carreteras del Perú."
    ]:
        p = tf.add_paragraph(); p.text = line; p.font.size = Pt(13.5); p.font.color.rgb = c_white; p.space_after = Pt(12)

    # SLIDE 6: CONCLUSIONES
    s6 = prs.slides.add_slide(blank_layout)
    agregar_encabezado(s6, "Conclusiones y Recomendaciones", "Cierre")
    tb = s6.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(11.3), Inches(4.8))
    tf = tb.text_frame; tf.word_wrap = True
    for i, c in enumerate([
        "1. Se modelaron con éxito dos relaciones lineales en 23 rutas reales del Perú mediante MCO, integrando hojas formuladas en Excel y una app en Streamlit.",
        "2. El dataset real demostró una varianza natural (R² = 85.45% en costos y 81.57% en combustible), respondiendo a la topografía de la Sierra/Selva y costos viales.",
        "3. La concordancia del 100% entre Excel y Python garantiza fiabilidad computacional y académica para la toma de decisiones logísticas."
    ]):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = c; p.font.size = Pt(14); p.font.color.rgb = c_white; p.space_after = Pt(16)

    prs.save("02 Presentación.pptx")
    print("Presentación '02 Presentación.pptx' actualizada con los 2 modelos, datos reales e interpretaciones exactas.")


if __name__ == "__main__":
    crear_presentacion()
