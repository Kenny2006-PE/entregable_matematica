import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.chart import ScatterChart, Reference, Series
from openpyxl.chart.trendline import Trendline
import pandas as pd


def construir_hoja_modelo(wb, ws, df, titulo_modelo, col_y, label_y, unidad_y,
                          fmt_y, fmt_m, desc_m, desc_b, desc_r2,
                          interpretacion_m, interpretacion_r2, dist_sim=650):
    n = len(df)
    ws.views.sheetView[0].showGridLines = True

    # Colores corporativos USIL
    c_navy = "002B49"
    c_gray_header = "1E293B"
    c_sim_bg = "FEF3C7"
    c_sim_border = "D97706"
    c_interp_bg = "EFF6FF"
    c_interp_border = "2563EB"

    font_title = Font(name="Segoe UI", size=14, bold=True, color="FFFFFF")
    font_subtitle = Font(name="Segoe UI", size=10, color="E0E7FF")
    font_section = Font(name="Segoe UI", size=11, bold=True, color=c_navy)
    font_header = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
    font_data = Font(name="Segoe UI", size=10, color="1F2937")
    font_bold = Font(name="Segoe UI", size=10, bold=True, color="1F2937")
    font_kpi_val = Font(name="Segoe UI", size=12, bold=True, color=c_navy)
    font_formula = Font(name="Segoe UI", size=11, bold=True, color="047857")

    fill_title = PatternFill(start_color=c_navy, end_color=c_navy, fill_type="solid")
    fill_header = PatternFill(start_color=c_gray_header, end_color=c_gray_header, fill_type="solid")
    fill_subtotal = PatternFill(start_color="EDF2F7", end_color="EDF2F7", fill_type="solid")
    fill_sim = PatternFill(start_color=c_sim_bg, end_color=c_sim_bg, fill_type="solid")
    fill_interp = PatternFill(start_color=c_interp_bg, end_color=c_interp_bg, fill_type="solid")

    thin = Side(border_style="thin", color="CBD5E1")
    thick_sim = Side(border_style="medium", color=c_sim_border)
    thick_interp = Side(border_style="medium", color=c_interp_border)
    border_all = Border(left=thin, right=thin, top=thin, bottom=thin)
    border_sim = Border(left=thick_sim, right=thick_sim, top=thick_sim, bottom=thick_sim)
    border_interp = Border(left=thick_interp, right=thick_interp, top=thick_interp, bottom=thick_interp)

    # 1. ENCABEZADO INSTITUCIONAL
    ws.merge_cells("A1:O1")
    ws["A1"] = "UNIVERSIDAD SAN IGNACIO DE LOYOLA (USIL) — FACULTAD DE INGENIERÍA E INTELIGENCIA ARTIFICIAL"
    ws["A1"].font = font_title
    ws["A1"].fill = fill_title
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center")

    ws.merge_cells("A2:O2")
    ws["A2"] = f"Curso: Matemática Discreta | {titulo_modelo}"
    ws["A2"].font = font_subtitle
    ws["A2"].fill = fill_title
    ws["A2"].alignment = Alignment(horizontal="center", vertical="center")

    ws.merge_cells("A3:O3")
    ws["A3"] = "Equipo: Combe, Matthias (2614607) | Palacin, Kenny (2622777) | Espiritu, Jeff (2614070) | Pérez, Ángel (2614500) | Docente: Marisel Rocío Beteta Salas"
    ws["A3"].font = Font(name="Segoe UI", size=9, italic=True, color="CBD5E1")
    ws["A3"].fill = fill_title
    ws["A3"].alignment = Alignment(horizontal="center", vertical="center")

    ws.row_dimensions[1].height = 28
    ws.row_dimensions[2].height = 20
    ws.row_dimensions[3].height = 18
    ws.row_dimensions[5].height = 24
    ws.row_dimensions[6].height = 28

    # Título de Tabla
    ws.merge_cells("A5:J5")
    ws["A5"] = f"MATRIZ DE DATOS Y MÍNIMOS CUADRADOS: DISTANCIA (X) vs. {label_y.upper()} (Y)"
    ws["A5"].font = font_section
    ws["A5"].alignment = Alignment(vertical="center")

    # 2. ENCABEZADOS DE TABLA (Columnas A a J)
    headers = [
        "ID Envío", "Ruta de Carga", "Región", "Distancia (km) [X]",
        f"{label_y} [Y]", "X²", "Y²", "X · Y", "Estimación Ŷ", "Residuo (Y - Ŷ)"
    ]
    start_row = 6
    for col_idx, h in enumerate(headers, start=1):
        cell = ws.cell(row=start_row, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = border_all

    # 3. LLENADO DE DATOS Y FÓRMULAS
    # Nota: En el panel lateral, M8 = Pendiente (m), M9 = Intersección (b)
    data_start = 7
    for i, row in df.iterrows():
        r = data_start + i
        ws.cell(row=r, column=1, value=row["ID_Envio"]).alignment = Alignment(horizontal="center")
        ws.cell(row=r, column=2, value=row["Ruta"]).alignment = Alignment(horizontal="left")
        ws.cell(row=r, column=3, value=row["Region"]).alignment = Alignment(horizontal="center")
        ws.cell(row=r, column=4, value=float(row["Distancia_km"])).number_format = "#,##0"
        ws.cell(row=r, column=5, value=float(row[col_y])).number_format = fmt_y

        # Fórmulas discretas MCO
        ws.cell(row=r, column=6, value=f"=D{r}^2").number_format = "#,##0"
        ws.cell(row=r, column=7, value=f"=E{r}^2").number_format = "#,##0.00"
        ws.cell(row=r, column=8, value=f"=D{r}*E{r}").number_format = "#,##0.00"
        # Estimación Ŷ = m*X + b (m está en M8, b está en M9)
        ws.cell(row=r, column=9, value=f"=$M$8*D{r}+$M$9").number_format = fmt_y
        ws.cell(row=r, column=10, value=f"=E{r}-I{r}").number_format = fmt_y

        for c in range(1, 11):
            ws.cell(row=r, column=c).border = border_all
            ws.cell(row=r, column=c).font = font_data
            if c >= 4:
                ws.cell(row=r, column=c).alignment = Alignment(horizontal="right")

    data_end = data_start + n - 1
    sum_row = data_end + 1

    # Fila de Sumatorias
    ws.cell(row=sum_row, column=1, value="SUMATORIAS").alignment = Alignment(horizontal="center")
    ws.cell(row=sum_row, column=2, value=f"n = {n} envíos").alignment = Alignment(horizontal="center")
    ws.cell(row=sum_row, column=3, value="—").alignment = Alignment(horizontal="center")
    ws.cell(row=sum_row, column=4, value=f"=SUM(D{data_start}:D{data_end})").number_format = "#,##0"
    ws.cell(row=sum_row, column=5, value=f"=SUM(E{data_start}:E{data_end})").number_format = fmt_y
    ws.cell(row=sum_row, column=6, value=f"=SUM(F{data_start}:F{data_end})").number_format = "#,##0"
    ws.cell(row=sum_row, column=7, value=f"=SUM(G{data_start}:G{data_end})").number_format = "#,##0.00"
    ws.cell(row=sum_row, column=8, value=f"=SUM(H{data_start}:H{data_end})").number_format = "#,##0.00"
    ws.cell(row=sum_row, column=9, value=f"=SUM(I{data_start}:I{data_end})").number_format = fmt_y
    ws.cell(row=sum_row, column=10, value=f"=SUM(J{data_start}:J{data_end})").number_format = fmt_y

    for c in range(1, 11):
        c_cell = ws.cell(row=sum_row, column=c)
        c_cell.font = font_bold
        c_cell.fill = fill_subtotal
        c_cell.border = Border(top=thin, bottom=Side(style="double", color=c_navy), left=thin, right=thin)

    # 4. PANEL LATERAL: PARÁMETROS DEL MODELO (Columnas L a O)
    ws.merge_cells("L5:O5")
    ws["L5"] = "PARÁMETROS DEL MODELO (Fórmulas Nativas de Excel)"
    ws["L5"].font = font_section
    ws["L5"].alignment = Alignment(vertical="center")

    kpis = [
        ("Observaciones (n) [CONTAR]:", f"=COUNT(D{data_start}:D{data_end})", "#,##0", "Total de rutas analizadas"),
        ("Pendiente (m) [PENDIENTE]:", f"=SLOPE(E{data_start}:E{data_end}, D{data_start}:D{data_end})", fmt_m, desc_m),
        ("Intersección (b) [INTERSECCION.EJE]:", f"=INTERCEPT(E{data_start}:E{data_end}, D{data_start}:D{data_end})", fmt_y, desc_b),
        ("Coef. Determinación (R²) [COEFICIENTE.R2]:", f"=RSQ(E{data_start}:E{data_end}, D{data_start}:D{data_end})", "0.00%", desc_r2),
        ("Correlación Pearson (r) [COEF.DE.CORREL]:", f"=CORREL(D{data_start}:D{data_end}, E{data_start}:E{data_end})", "0.0000", "Fuerza y dirección lineal entre X e Y"),
        ("Error Típico [ERROR.TIPICO.XY]:", f"=STEYX(E{data_start}:E{data_end}, D{data_start}:D{data_end})", fmt_y, "Dispersión estándar de los residuos")
    ]

    kpi_start = 7
    for idx, (label, formula, num_format, desc) in enumerate(kpis):
        kr = kpi_start + idx
        ws.cell(row=kr, column=12, value=label).font = font_bold
        ws.cell(row=kr, column=12).border = border_all
        ws.cell(row=kr, column=12).alignment = Alignment(vertical="center")

        val_cell = ws.cell(row=kr, column=13, value=formula)
        val_cell.font = font_kpi_val
        val_cell.number_format = num_format
        val_cell.border = border_all
        val_cell.alignment = Alignment(horizontal="right", vertical="center")

        ws.merge_cells(start_row=kr, start_column=14, end_row=kr, end_column=15)
        desc_cell = ws.cell(row=kr, column=14, value=desc)
        desc_cell.font = Font(name="Segoe UI", size=9, italic=True, color="4B5563")
        desc_cell.border = border_all
        desc_cell.alignment = Alignment(vertical="center")
        ws.cell(row=kr, column=15).border = border_all
        ws.row_dimensions[kr].height = 22

    # Ecuación del Modelo (M8 = m, M9 = b)
    eq_row = kpi_start + len(kpis) + 1  # Fila 14
    ws.merge_cells(start_row=eq_row, start_column=12, end_row=eq_row, end_column=15)
    ws.cell(row=eq_row, column=12, value=f'="ECUACIÓN DEL MODELO:   Ŷ = " & TEXT(M8,"0.0000") & " · X + " & TEXT(M9,"0.00") & " ({unidad_y})"')
    ws.cell(row=eq_row, column=12).font = font_formula
    ws.cell(row=eq_row, column=12).fill = PatternFill(start_color="D1FAE5", end_color="D1FAE5", fill_type="solid")
    ws.cell(row=eq_row, column=12).alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[eq_row].height = 26

    # 5. SIMULADOR INTERACTIVO PREDICTIVO (PRONOSTICO.LINEAL)
    sim_title_row = eq_row + 2  # Fila 16
    ws.merge_cells(start_row=sim_title_row, start_column=12, end_row=sim_title_row, end_column=15)
    ws.cell(row=sim_title_row, column=12, value="SIMULADOR PREDICTIVO EN TIEMPO REAL (PRONOSTICO.LINEAL)")
    ws.cell(row=sim_title_row, column=12).font = font_section
    ws.cell(row=sim_title_row, column=12).alignment = Alignment(vertical="center")

    sim_r1 = sim_title_row + 1  # Fila 17
    ws.cell(row=sim_r1, column=12, value="Distancia a Evaluar (km):").font = font_bold
    ws.cell(row=sim_r1, column=12).border = border_sim
    ws.cell(row=sim_r1, column=12).fill = fill_sim
    input_cell = ws.cell(row=sim_r1, column=13, value=dist_sim)
    input_cell.font = Font(name="Segoe UI", size=13, bold=True, color=c_navy)
    input_cell.number_format = "#,##0"
    input_cell.border = border_sim
    input_cell.fill = fill_sim
    input_cell.alignment = Alignment(horizontal="right", vertical="center")

    ws.merge_cells(start_row=sim_r1, start_column=14, end_row=sim_r1, end_column=15)
    ws.cell(row=sim_r1, column=14, value="<- Modifique esta celda para simular").font = Font(name="Segoe UI", size=9, bold=True, color="B45309")
    ws.cell(row=sim_r1, column=14).border = border_sim
    ws.cell(row=sim_r1, column=14).fill = fill_sim
    ws.cell(row=sim_r1, column=15).border = border_sim

    sim_r2 = sim_r1 + 1  # Fila 18
    ws.cell(row=sim_r2, column=12, value=f"Pronóstico {unidad_y} [PRONOSTICO.LINEAL]:").font = font_bold
    ws.cell(row=sim_r2, column=12).border = border_sim
    ws.cell(row=sim_r2, column=12).fill = fill_sim
    pred_cell = ws.cell(row=sim_r2, column=13, value=f"=FORECAST.LINEAR(M{sim_r1}, E{data_start}:E{data_end}, D{data_start}:D{data_end})")
    pred_cell.font = Font(name="Segoe UI", size=14, bold=True, color="B45309")
    pred_cell.number_format = fmt_y
    pred_cell.border = border_sim
    pred_cell.fill = fill_sim
    pred_cell.alignment = Alignment(horizontal="right", vertical="center")

    ws.merge_cells(start_row=sim_r2, start_column=14, end_row=sim_r2, end_column=15)
    ws.cell(row=sim_r2, column=14, value="Proyección automática en tiempo real").font = Font(name="Segoe UI", size=9, italic=True, color="78350F")
    ws.cell(row=sim_r2, column=14).border = border_sim
    ws.cell(row=sim_r2, column=14).fill = fill_sim
    ws.cell(row=sim_r2, column=15).border = border_sim

    ws.row_dimensions[sim_r1].height = 26
    ws.row_dimensions[sim_r2].height = 26

    # 6. CUADRO DE INTERPRETACIÓN (PENDIENTE Y R²)
    interp_start = sum_row + 2
    ws.merge_cells(start_row=interp_start, start_column=1, end_row=interp_start, end_column=10)
    ws.cell(row=interp_start, column=1, value="INTERPRETACIÓN ESTADÍSTICA DE RESULTADOS (PENDIENTE m Y COEFICIENTE R²)").font = font_section

    ws.merge_cells(start_row=interp_start + 1, start_column=1, end_row=interp_start + 2, end_column=10)
    c_im = ws.cell(row=interp_start + 1, column=1, value=f"• Interpretación de la Pendiente (m): {interpretacion_m}")
    c_im.font = Font(name="Segoe UI", size=10, color="1E3A8A")
    c_im.fill = fill_interp
    c_im.alignment = Alignment(vertical="center", wrap_text=True)

    ws.merge_cells(start_row=interp_start + 3, start_column=1, end_row=interp_start + 4, end_column=10)
    c_ir = ws.cell(row=interp_start + 3, column=1, value=f"• Interpretación del Coeficiente R²: {interpretacion_r2}")
    c_ir.font = Font(name="Segoe UI", size=10, color="1E3A8A")
    c_ir.fill = fill_interp
    c_ir.alignment = Alignment(vertical="center", wrap_text=True)

    for rr in range(interp_start + 1, interp_start + 5):
        ws.row_dimensions[rr].height = 22
        for cc in range(1, 11):
            ws.cell(row=rr, column=cc).border = border_interp if rr in [interp_start + 1, interp_start + 4] else border_all
            ws.cell(row=rr, column=cc).fill = fill_interp

    # 7. GRÁFICO DE DISPERSIÓN CON LÍNEA DE TENDENCIA
    chart = ScatterChart()
    chart.title = f"Regresión Lineal: Distancia (km) vs {label_y}"
    chart.style = 13
    chart.x_axis.title = "Distancia Recorrida (km)"
    chart.y_axis.title = label_y
    chart.width = 20
    chart.height = 13

    xvalues = Reference(ws, min_col=4, min_row=data_start, max_row=data_end)
    yvalues = Reference(ws, min_col=5, min_row=data_start, max_row=data_end)
    series = Series(yvalues, xvalues, title_from_data=False)
    series.marker.symbol = "circle"
    series.marker.graphicalProperties.solidFill = "002B49"
    series.marker.graphicalProperties.line.solidFill = "002B49"
    series.graphicalProperties.line.noFill = True

    trendline = Trendline()
    trendline.trendlineType = "linear"
    trendline.dispRSqr = True
    trendline.dispEq = True
    series.trendline = trendline

    chart.series.append(series)
    ws.add_chart(chart, f"L{sim_r2 + 2}")

    # Anchos de columnas
    col_widths = {
        "A": 12, "B": 21, "C": 10, "D": 17, "E": 19, "F": 13, "G": 15, "H": 16, "I": 17, "J": 16,
        "K": 3, "L": 38, "M": 18, "N": 28, "O": 16
    }
    for col_letter, width in col_widths.items():
        ws.column_dimensions[col_letter].width = width


def construir_hoja_comparativa(wb):
    ws = wb.create_sheet(title="Resumen Comparativo")
    ws.views.sheetView[0].showGridLines = True

    c_navy = "002B49"
    c_header = "1E293B"
    font_title = Font(name="Segoe UI", size=14, bold=True, color="FFFFFF")
    font_sub = Font(name="Segoe UI", size=10, color="CBD5E1")
    font_header = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
    font_bold = Font(name="Segoe UI", size=10, bold=True, color="0F172A")
    font_data = Font(name="Segoe UI", size=10, color="1E293B")

    fill_title = PatternFill(start_color=c_navy, end_color=c_navy, fill_type="solid")
    fill_header = PatternFill(start_color=c_header, end_color=c_header, fill_type="solid")
    fill_alt = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")

    thin = Side(border_style="thin", color="CBD5E1")
    border_all = Border(left=thin, right=thin, top=thin, bottom=thin)

    ws.merge_cells("A1:E1")
    ws["A1"] = "RESUMEN COMPARATIVO DE LOS 2 MODELOS DE REGRESIÓN LINEAL — USIL 2026"
    ws["A1"].font = font_title
    ws["A1"].fill = fill_title
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 28

    ws.merge_cells("A2:E2")
    ws["A2"] = "Comparación dinámica vinculada mediante fórmulas a las hojas del Modelo 1 (Costos) y Modelo 2 (Combustible)"
    ws["A2"].font = font_sub
    ws["A2"].fill = fill_title
    ws["A2"].alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[2].height = 20

    headers = [
        "Indicador / Parámetro",
        "Fórmula Excel Aplicada",
        "Modelo 1: Costo de Transporte (S/)",
        "Modelo 2: Consumo de Combustible (gal)",
        "Interpretación Comparativa"
    ]
    for c_idx, h in enumerate(headers, start=1):
        cell = ws.cell(row=4, column=c_idx, value=h)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = border_all
    ws.row_dimensions[4].height = 26

    s1 = "'Modelo 1 - Costo Transporte'"
    s2 = "'Modelo 2 - Combustible'"

    rows = [
        ("Variable Independiente (X)", "Rango D7:D31", "Distancia Recorrida (km)", "Distancia Recorrida (km)", "Misma variable predictora en las 25 rutas"),
        ("Variable Dependiente (Y)", "Rango E7:E31", "Costo Total de Transporte (S/)", "Consumo de Combustible (gal)", "Evalúa impacto económico y energético"),
        ("Observaciones (n)", "=CONTAR(X)", f"={s1}!M7", f"={s2}!M7", "Muestra homogénea de 25 rutas nacionales"),
        ("Pendiente (m)", "=PENDIENTE(Y, X)", f"={s1}!M8", f"={s2}!M8", "M1: +S/ 4.78 por km | M2: +0.1293 gal por km (~7.74 km/gal)"),
        ("Intersección (b)", "=INTERSECCION.EJE(Y, X)", f"={s1}!M9", f"={s2}!M9", "M1: S/ 253.94 costo fijo | M2: 9.71 gal consumo base"),
        ("Coef. Determinación (R²)", "=COEFICIENTE.R2(Y, X)", f"={s1}!M10", f"={s2}!M10", "M1: 99.98% (casi perfecto) vs M2: 95.13% (afectado por topografía)"),
        ("Correlación Pearson (r)", "=COEF.DE.CORREL(X, Y)", f"={s1}!M11", f"={s2}!M11", "Correlación positiva muy fuerte en ambos modelos"),
        ("Error Típico Estándar", "=ERROR.TIPICO.XY(Y, X)", f"={s1}!M12", f"={s2}!M12", "Dispersión promedio respecto a la recta ajustada"),
        ("Proyección a 500 km", "=PRONOSTICO.LINEAL(500, Y, X)", f"=FORECAST.LINEAR(500, {s1}!E7:E31, {s1}!D7:D31)", f"=FORECAST.LINEAR(500, {s2}!E7:E31, {s2}!D7:D31)", "Estimación conjunta para un flete de 500 km"),
        ("Proyección a 1,000 km", "=PRONOSTICO.LINEAL(1000, Y, X)", f"=FORECAST.LINEAR(1000, {s1}!E7:E31, {s1}!D7:D31)", f"=FORECAST.LINEAR(1000, {s2}!E7:E31, {s2}!D7:D31)", "Estimación conjunta para ruta larga (ej. Lima - Arequipa/Piura)")
    ]

    fmts_m1 = [None, None, "#,##0", '"S/ "0.0000"/km"', '"S/ "#,##0.00', "0.00%", "0.0000", '"S/ "#,##0.00', '"S/ "#,##0.00', '"S/ "#,##0.00']
    fmts_m2 = [None, None, "#,##0", '0.0000" gal/km"', '0.00" gal"', "0.00%", "0.0000", '0.00" gal"', '0.00" gal"', '0.00" gal"']

    for idx, row_vals in enumerate(rows):
        r = 5 + idx
        ws.row_dimensions[r].height = 24
        for c_idx, val in enumerate(row_vals, start=1):
            cell = ws.cell(row=r, column=c_idx, value=val)
            cell.border = border_all
            cell.font = font_bold if c_idx == 1 else font_data
            if idx % 2 == 1:
                cell.fill = fill_alt
            if c_idx == 3 and fmts_m1[idx]:
                cell.number_format = fmts_m1[idx]
                cell.alignment = Alignment(horizontal="right", vertical="center")
            elif c_idx == 4 and fmts_m2[idx]:
                cell.number_format = fmts_m2[idx]
                cell.alignment = Alignment(horizontal="right", vertical="center")
            else:
                cell.alignment = Alignment(vertical="center", wrap_text=True)

    widths = {"A": 26, "B": 30, "C": 28, "D": 30, "E": 56}
    for col, w in widths.items():
        ws.column_dimensions[col].width = w


def crear_excel_regresion():
    df = pd.read_csv("datos_logisticos.csv")
    wb = openpyxl.Workbook()

    # Hoja 1: Modelo 1 (Distancia vs Costo de Transporte)
    ws1 = wb.active
    ws1.title = "Modelo 1 - Costo Transporte"
    construir_hoja_modelo(
        wb, ws1, df,
        titulo_modelo="Modelo 1: Regresión Lineal — Distancia Recorrida (X) vs. Costo Total de Transporte (Y1)",
        col_y="Costo_Total_Soles",
        label_y="Costo Real (S/)",
        unidad_y="S/",
        fmt_y='"S/ "#,##0.00',
        fmt_m='"S/ "0.0000',
        desc_m="Costo variable marginal por cada km adicional (S//km)",
        desc_b="Costo fijo base de despacho, estiba y gestión (X = 0)",
        desc_r2="% de variación del costo explicado por la distancia",
        interpretacion_m="La pendiente positiva m = S/ 4.7776/km indica que por cada kilómetro adicional recorrido, el costo total de transporte se incrementa en promedio S/ 4.78, partiendo de un costo fijo base de S/ 253.94.",
        interpretacion_r2="El coeficiente R² = 99.98% demuestra un ajuste lineal prácticamente perfecto: el 99.98% de la variabilidad del costo total se explica por la distancia recorrida, brindando altísima confiabilidad para cotizaciones.",
        dist_sim=650
    )

    # Hoja 2: Modelo 2 (Distancia vs Consumo de Combustible)
    ws2 = wb.create_sheet(title="Modelo 2 - Combustible")
    construir_hoja_modelo(
        wb, ws2, df,
        titulo_modelo="Modelo 2: Regresión Lineal — Distancia Recorrida (X) vs. Consumo de Combustible (Y2)",
        col_y="Consumo_Combustible_Gal",
        label_y="Combustible (gal)",
        unidad_y="gal",
        fmt_y='#,##0.00" gal"',
        fmt_m='0.0000" gal/km"',
        desc_m="Consumo marginal de diésel por km adicional (~7.74 km/gal)",
        desc_b="Consumo fijo inicial (maniobras, carga y salida de Lima)",
        desc_r2="% de variación del combustible explicado por la distancia",
        interpretacion_m="La pendiente positiva m = 0.1293 gal/km indica que por cada kilómetro adicional recorrido la unidad consume en promedio 0.1293 galones de diésel (12.93 galones cada 100 km, rendimiento medio de 7.74 km/galón), con un consumo fijo inicial de 9.71 galones.",
        interpretacion_r2="El coeficiente R² = 95.13% refleja un ajuste lineal muy fuerte y altamente confiable. El 4.87% de variabilidad no explicada (1 - R²) se atribuye a factores topográficos de la red vial peruana (mayor consumo en rutas andinas de sierra/selva frente a rutas planas costeras).",
        dist_sim=650
    )

    # Hoja 3: Resumen Comparativo
    construir_hoja_comparativa(wb)

    wb.save("Sistema_Regresion_Logistica.xlsx")
    print("Archivo Excel 'Sistema_Regresion_Logistica.xlsx' (3 hojas con 2 modelos completos) generado con éxito.")


if __name__ == "__main__":
    crear_excel_regresion()
