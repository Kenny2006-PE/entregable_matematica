from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
import os

def crear_presentacion():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5) # Pantalla panorámica 16:9
    
    # Paleta de colores USIL
    c_navy = RGBColor(0, 43, 73)      # #002B49
    c_cyan = RGBColor(0, 229, 255)    # #00E5FF
    c_orange = RGBColor(255, 107, 0)  # #FF6B00
    c_white = RGBColor(255, 255, 255)
    c_gray = RGBColor(148, 163, 184)
    c_dark = RGBColor(10, 22, 40)
    
    blank_layout = prs.slide_layouts[6] # Layout en blanco para control total
    
    def agregar_fondo_oscuro(slide):
        bg = slide.shapes.add_shape(1, 0, 0, Inches(13.333), Inches(7.5)) # 1 = MSO_SHAPE.RECTANGLE
        bg.fill.solid()
        bg.fill.fore_color.rgb = c_dark
        bg.line.color.rgb = c_dark
        return bg

    def agregar_encabezado(slide, titulo, seccion):
        agregar_fondo_oscuro(slide)
        
        # Barra superior decorativa
        bar = slide.shapes.add_shape(1, Inches(0.8), Inches(0.5), Inches(0.1), Inches(0.7))
        bar.fill.solid()
        bar.fill.fore_color.rgb = c_cyan
        bar.line.color.rgb = c_cyan
        
        txBox = slide.shapes.add_textbox(Inches(1.1), Inches(0.4), Inches(11), Inches(0.9))
        tf = txBox.text_frame
        tf.word_wrap = True
        
        p_sec = tf.paragraphs[0]
        p_sec.text = seccion.upper()
        p_sec.font.size = Pt(10)
        p_sec.font.bold = True
        p_sec.font.color.rgb = c_cyan
        
        p_tit = tf.add_paragraph()
        p_tit.text = titulo
        p_tit.font.size = Pt(22)
        p_tit.font.bold = True
        p_tit.font.color.rgb = c_white
        
        # Pie de página
        footBox = slide.shapes.add_textbox(Inches(0.8), Inches(7.0), Inches(11.7), Inches(0.4))
        ftf = footBox.text_frame
        p_foot = ftf.paragraphs[0]
        p_foot.text = "USIL 2026 | Matemática Discreta — Trabajo Final: Sistema Interactivo de Regresión Lineal"
        p_foot.font.size = Pt(9)
        p_foot.font.color.rgb = c_gray
        
    # -------------------------------------------------------------
    # SLIDE 1: PORTADA
    # -------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    agregar_fondo_oscuro(s1)
    
    # Caja central
    tbox = s1.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.333), Inches(5.0))
    tf1 = tbox.text_frame
    tf1.word_wrap = True
    
    p = tf1.paragraphs[0]
    p.text = "UNIVERSIDAD SAN IGNACIO DE LOYOLA (USIL)"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = c_cyan
    p.alignment = PP_ALIGN.CENTER
    
    p = tf1.add_paragraph()
    p.text = "FACULTAD DE INGENIERÍA E INTELIGENCIA ARTIFICIAL — ING. DE SISTEMAS"
    p.font.size = Pt(11)
    p.font.color.rgb = c_gray
    p.alignment = PP_ALIGN.CENTER
    
    p = tf1.add_paragraph()
    p.text = "\nSISTEMA INTERACTIVO DE REGRESIÓN LINEAL\nPARA ANÁLISIS DE DATOS"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = c_white
    p.alignment = PP_ALIGN.CENTER
    
    p = tf1.add_paragraph()
    p.text = "Optimización y Proyección en Tiempo Real de Costos de Transporte Logístico en el Perú"
    p.font.size = Pt(14)
    p.font.italic = True
    p.font.color.rgb = c_orange
    p.alignment = PP_ALIGN.CENTER
    
    p = tf1.add_paragraph()
    p.text = "\nCurso: Matemática Discreta  |  Docente: Marisel Rocío Beteta Salas"
    p.font.size = Pt(12)
    p.font.color.rgb = c_white
    p.alignment = PP_ALIGN.CENTER
    
    p = tf1.add_paragraph()
    p.text = "Equipo: Matthias Combe (2614607) • Kenny Palacin (2622777) • Jeff Espiritu (2614070) • Ángel Pérez (2614500)"
    p.font.size = Pt(11)
    p.font.color.rgb = c_gray
    p.alignment = PP_ALIGN.CENTER
    
    # -------------------------------------------------------------
    # SLIDE 2: AGENDA
    # -------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    agregar_encabezado(s2, "Estructura de la Exposición (20 Minutos)", "Agenda")
    
    cbox = s2.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(11), Inches(4.8))
    ctf = cbox.text_frame
    items = [
        "1. Caso de Estudio: TransAndina Logistics S.A.C. y Problemática de Fletes",
        "2. Objetivos del Proyecto y Requerimientos de Software",
        "3. Fundamentación en Matemática Discreta: Mínimos Cuadrados y Gauss",
        "4. Arquitectura de la Solución: Microsoft Excel + Python Streamlit + anime.js",
        "5. Demostración en Tiempo Real de la Aplicación y Simulador",
        "6. Auditoría y Validación Cruzada: Excel vs. Python (100% Coincidencia)",
        "7. Conclusiones y Medición de Atributos del Graduado (CP1, CP3, CP5)"
    ]
    for i, it in enumerate(items):
        p = ctf.paragraphs[0] if i == 0 else ctf.add_paragraph()
        p.text = it
        p.font.size = Pt(16)
        p.font.color.rgb = c_white
        p.space_after = Pt(14)
        
    # -------------------------------------------------------------
    # SLIDE 3: PROBLEMÁTICA Y CASO REAL
    # -------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    agregar_encabezado(s3, "TransAndina Logistics S.A.C. — Contexto Operativo", "Caso de Estudio")
    
    # 2 columnas
    b1 = s3.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.3), Inches(4.5))
    tf = b1.text_frame
    p = tf.paragraphs[0]
    p.text = "EL PROBLEMA LOGÍSTICO"
    p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = c_orange
    p = tf.add_paragraph()
    p.text = "• Fijación manual de tarifas de transporte basada en aproximaciones empíricas.\n• Errores humanos frecuentes de digitación al cotizar a clientes corporativos.\n• Pérdida de margen por sobrecostos imprevistos de ruta (diésel y peajes no calculados).\n• Dificultad para desglosar el Costo Fijo de Despacho frente al Costo Variable por Kilómetro."
    p.font.size = Pt(13); p.font.color.rgb = c_white; p.space_after = Pt(10)
    
    b2 = s3.shapes.add_textbox(Inches(6.8), Inches(1.8), Inches(5.5), Inches(4.5))
    tf = b2.text_frame
    p = tf.paragraphs[0]
    p.text = "VARIABLES DEL MODELO (25 RUTAS PERÚ)"
    p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = c_cyan
    p = tf.add_paragraph()
    p.text = "• Variable Independiente (X): Distancia recorrida en Kilómetros (km) desde Lima.\n• Variable Dependiente (Y): Costo total facturado del servicio en Soles (S/).\n• Cobertura Geográfica: Rutas desde Chosica (45 km), Ica, Trujillo, Arequipa hasta Tacna (1,295 km)."
    p.font.size = Pt(13); p.font.color.rgb = c_white
    
    # -------------------------------------------------------------
    # SLIDE 4: MATEMÁTICA DISCRETA Y GAUSS
    # -------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    agregar_encabezado(s4, "Fundamentación Matemática: Mínimos Cuadrados Ordinarios", "Marco Teórico")
    
    b_mat = s4.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(4.8))
    tf = b_mat.text_frame
    
    p = tf.paragraphs[0]
    p.text = "1. Conjunto Discreto de Observaciones:"
    p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = c_cyan
    p = tf.add_paragraph()
    p.text = "S = {(x1, y1), (x2, y2), ..., (xn, yn)} con n = 25 pares ordenados finitos."
    p.font.size = Pt(12); p.font.color.rgb = c_white; p.space_after = Pt(8)
    
    p = tf.add_paragraph()
    p.text = "2. Sistema Canónico de Ecuaciones Normales de Gauss:"
    p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = c_cyan
    p = tf.add_paragraph()
    p.text = "    [1]  m · Σ(xi²) + b · Σ(xi) = Σ(xi · yi)\n    [2]  m · Σ(xi)  + b · n      = Σ(yi)"
    p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = c_orange; p.space_after = Pt(8)
    
    p = tf.add_paragraph()
    p.text = "3. Fórmulas de Optimización MCO:"
    p.font.size = Pt(13); p.font.bold = True; p.font.color.rgb = c_cyan
    p = tf.add_paragraph()
    p.text = "• Pendiente (m): [n · Σ(xy) - (Σx)(Σy)] / [n · Σ(x²) - (Σx)²]  -->  m = S/ 4.8214 / km\n• Intercepto (b): (Σy - m·Σx) / n = ȳ - m·x̄  -->  b = S/ 236.42\n• Coeficiente R²: 1 - (SSres / SStot) = 99.82%  (Precisión predictiva superior)"
    p.font.size = Pt(12); p.font.color.rgb = c_white
    
    # -------------------------------------------------------------
    # SLIDE 5: ARQUITECTURA DEL SISTEMA
    # -------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    agregar_encabezado(s5, "Arquitectura Tecnológica Dual: Excel + Python Streamlit", "Desarrollo")
    
    c1 = s5.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(5.4), Inches(4.5))
    tf = c1.text_frame
    p = tf.paragraphs[0]
    p.text = "MICROSOFT EXCEL ANALÍTICO"
    p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = RGBColor(34, 197, 94)
    p = tf.add_paragraph()
    p.text = "• Fórmulas Nativas: =PENDIENTE(), =INTERSECCION.EJE(), =COEFICIENTE.R2().\n• Simulador en Celda: =PRONOSTICO.LINEAL().\n• Matriz Discreta: Columnas para X², Y², X·Y, Estimación Ŷ y Residuos.\n• Gráfico Integrado: Dispersión con línea de tendencia y ecuación visual."
    p.font.size = Pt(13); p.font.color.rgb = c_white
    
    c2 = s5.shapes.add_textbox(Inches(6.8), Inches(1.8), Inches(5.5), Inches(4.5))
    tf = c2.text_frame
    p = tf.paragraphs[0]
    p.text = "APLICACIÓN EN PYTHON & STREAMLIT"
    p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = c_cyan
    p = tf.add_paragraph()
    p.text = "• Visualización en Tiempo Real con Plotly y bandas de confianza (95%).\n• Animaciones fluidas con anime.js (odómetro numérico y camión interactivo).\n• Simulador de Sensibilidad: Variación de diésel (%), peajes y márgenes.\n• Interfaz Dark Glassmorphism de calidad profesional (SaaS)."
    p.font.size = Pt(13); p.font.color.rgb = c_white
    
    # -------------------------------------------------------------
    # SLIDE 6: VALIDACIÓN CRUZADA
    # -------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    agregar_encabezado(s6, "Auditoría de Consistencia Numérica: Excel vs. Python", "Validación Cruzada")
    
    tb = s6.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(4.5))
    tf = tb.text_frame
    p = tf.paragraphs[0]
    p.text = "RESULTADOS COMPARATIVOS AL 100% DE PRECISIÓN:"
    p.font.size = Pt(14); p.font.bold = True; p.font.color.rgb = c_orange
    
    tabla_txt = [
        ("Pendiente (m)", "=PENDIENTE(Y, X)", "4.8214 S//km", "4.8214 S//km", "Diferencia: 0.000000 (Exacta)"),
        ("Intersección (b)", "=INTERSECCION.EJE(Y, X)", "S/ 236.42", "S/ 236.42", "Diferencia: 0.000000 (Exacta)"),
        ("Coeficiente R²", "=COEFICIENTE.R2(Y, X)", "0.9982 (99.82%)", "0.9982 (99.82%)", "Diferencia: 0.000000 (Exacta)"),
        ("Proyección (500 km)", "=PRONOSTICO.LINEAL(500, Y, X)", "S/ 2,647.12", "S/ 2,647.12", "Diferencia: S/ 0.00 (Exacta)")
    ]
    for row in tabla_txt:
        p = tf.add_paragraph()
        p.text = f"• {row[0]}: Excel = {row[2]}  |  Python = {row[3]}  -->  {row[4]}"
        p.font.size = Pt(13); p.font.color.rgb = c_white; p.space_after = Pt(8)
        
    # -------------------------------------------------------------
    # SLIDE 7: CONCLUSIONES
    # -------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    agregar_encabezado(s7, "Conclusiones y Atributos del Graduado (USIL)", "Cierre")
    
    tb = s7.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(4.8))
    tf = tb.text_frame
    concls = [
        "1. Cumplimiento Integral: Se integró exitosamente el modelo de regresión lineal en Excel y Python con visualización interactiva en tiempo real.",
        "2. Aplicación Práctica: La Matemática Discreta permitió resolver un problema real de ingeniería, identificando un Costo Fijo de S/ 236.42 y un Costo Variable de S/ 4.82 por km.",
        "3. Solidez del Ajuste: El coeficiente R² de 99.82% valida que la distancia explica con alta fidelidad el comportamiento de las tarifas.",
        "4. Impacto Gerencial: TransAndina Logistics S.A.C. cuenta ahora con una plataforma para simular escenarios y proteger su rentabilidad.",
        "5. Competencias Logradas: Evidencia de CP1 (diseño de soluciones), CP3 (calidad de software y métricas) y CP5 (adaptación tecnológica continua)."
    ]
    for i, c in enumerate(concls):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = c
        p.font.size = Pt(13); p.font.color.rgb = c_white; p.space_after = Pt(10)
        
    prs.save("02 Presentación.pptx")
    print("Presentación '02 Presentación.pptx' generada exitosamente.")

if __name__ == "__main__":
    crear_presentacion()

