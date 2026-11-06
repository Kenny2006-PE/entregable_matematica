import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.chart import ScatterChart, Reference, Series
import pandas as pd

def crear_excel_regresion():
    df = pd.read_csv("datos_logisticos.csv")
    n = len(df)
    
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Regresión Lineal Logística"
    ws.views.sheetView[0].showGridLines = True
    
    # Colores corporativos USIL
    c_navy = "002B49"       # Azul Marino USIL
    c_blue_light = "E6F0FA"  # Celeste claro
    c_accent = "F37021"     # Naranja acento
    c_gray_header = "2C3E50"
    c_kpi_bg = "F8FAFC"
    c_sim_bg = "FEF3C7"     # Amarillo suave para simulador
    c_sim_border = "D97706"
    
    # Estilos
    font_title = Font(name="Segoe UI", size=15, bold=True, color="FFFFFF")
    font_subtitle = Font(name="Segoe UI", size=10, bold=False, color="E0E7FF")
    font_section = Font(name="Segoe UI", size=11, bold=True, color=c_navy)
    font_header = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
    font_data = Font(name="Segoe UI", size=10, color="1F2937")
    font_bold = Font(name="Segoe UI", size=10, bold=True, color="1F2937")
    font_kpi_val = Font(name="Segoe UI", size=13, bold=True, color=c_navy)
    font_formula = Font(name="Segoe UI", size=11, bold=True, color="047857")
    
    fill_title = PatternFill(start_color=c_navy, end_color=c_navy, fill_type="solid")
    fill_header = PatternFill(start_color=c_gray_header, end_color=c_gray_header, fill_type="solid")
    fill_subtotal = PatternFill(start_color="EDF2F7", end_color="EDF2F7", fill_type="solid")
    fill_kpi = PatternFill(start_color=c_kpi_bg, end_color=c_kpi_bg, fill_type="solid")
    fill_sim = PatternFill(start_color=c_sim_bg, end_color=c_sim_bg, fill_type="solid")
    
    thin = Side(border_style="thin", color="CBD5E1")
    thick_sim = Side(border_style="medium", color=c_sim_border)
    border_all = Border(left=thin, right=thin, top=thin, bottom=thin)
    border_sim = Border(left=thick_sim, right=thick_sim, top=thick_sim, bottom=thick_sim)
    
    # 1. ENCABEZADO INSTITUCIONAL
    ws.merge_cells("A1:K1")
    ws["A1"] = "UNIVERSIDAD SAN IGNACIO DE LOYOLA (USIL) - FACULTAD DE INGENIERÍA E INTELIGENCIA ARTIFICIAL"
    ws["A1"].font = font_title
    ws["A1"].fill = fill_title
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center")
    
    ws.merge_cells("A2:K2")
    ws["A2"] = "Carrera: Ing. de Sistemas de Información | Curso: Matemática Discreta | Sistema Interactivo de Regresión Lineal"
    ws["A2"].font = font_subtitle
    ws["A2"].fill = fill_title
    ws["A2"].alignment = Alignment(horizontal="center", vertical="center")
    
    ws.merge_cells("A3:K3")
    ws["A3"] = "Equipo: Combe, Matthias (2614607) | Palacin, Kenny (2622777) | Espiritu, Jeff (2614070) | Pérez, Ángel (2614500) | Docente: Marisel Rocío Beteta Salas"
    ws["A3"].font = Font(name="Segoe UI", size=9, italic=True, color="CBD5E1")
    ws["A3"].fill = fill_title
    ws["A3"].alignment = Alignment(horizontal="center", vertical="center")
    
    ws.row_dimensions[1].height = 28
    ws.row_dimensions[2].height = 20
    ws.row_dimensions[3].height = 18
    ws.row_dimensions[5].height = 24
    ws.row_dimensions[6].height = 24
    
    # Título de Tabla
    ws.merge_cells("A5:I5")
    ws["A5"] = "CASO DE ESTUDIO: DISTANCIA RECORRIDA (X) vs. COSTO DE TRANSPORTE LOGÍSTICO (Y)"
    ws["A5"].font = font_section
    ws["A5"].alignment = Alignment(vertical="center")
    
    # 2. ENCABEZADOS DE TABLA DE DATOS
    headers = [
        "ID Envío", "Ruta de Carga", "Distancia (km) [X]", "Costo Real (S/) [Y]", 
        "X²", "Y²", "X · Y", "Estimación Ŷ", "Residuo (Y - Ŷ)"
    ]
    start_row = 6
    for col_idx, h in enumerate(headers, start=1):
        cell = ws.cell(row=start_row, column=col_idx, value=h)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = border_all
    
    # 3. LLENADO DE DATOS Y FÓRMULAS
    data_start = 7
    for i, row in df.iterrows():
        r = data_start + i
        ws.cell(row=r, column=1, value=row["ID_Envio"]).alignment = Alignment(horizontal="center")
        ws.cell(row=r, column=2, value=row["Ruta"]).alignment = Alignment(horizontal="left")
        ws.cell(row=r, column=3, value=row["Distancia_km"]).number_format = "#,##0"
        ws.cell(row=r, column=4, value=row["Costo_Total_Soles"]).number_format = '"S/ "#,##0.00'
        
        # Fórmulas de matemática discreta para regresión por mínimos cuadrados
        ws.cell(row=r, column=5, value=f"=C{r}^2").number_format = "#,##0"
        ws.cell(row=r, column=6, value=f"=D{r}^2").number_format = "#,##0.00"
        ws.cell(row=r, column=7, value=f"=C{r}*D{r}").number_format = "#,##0.00"
        ws.cell(row=r, column=8, value=f"=$L$9*C{r}+$L$10").number_format = '"S/ "#,##0.00'
        ws.cell(row=r, column=9, value=f"=D{r}-H{r}").number_format = '"S/ "#,##0.00'
        
        for c in range(1, 10):
            ws.cell(row=r, column=c).border = border_all
            ws.cell(row=r, column=c).font = font_data
            if c in [3, 5]:
                ws.cell(row=r, column=c).alignment = Alignment(horizontal="right")
            elif c in [4, 6, 7, 8, 9]:
                ws.cell(row=r, column=c).alignment = Alignment(horizontal="right")
    
    data_end = data_start + n - 1
    sum_row = data_end + 1
    
    # Fila de Sumatorias (Esencial en Matemática Discreta / Mínimos Cuadrados)
    ws.cell(row=sum_row, column=1, value="SUMATORIAS").alignment = Alignment(horizontal="center")
    ws.cell(row=sum_row, column=2, value=f"N = {n} registros").alignment = Alignment(horizontal="center")
    ws.cell(row=sum_row, column=3, value=f"=SUM(C{data_start}:C{data_end})").number_format = "#,##0"
    ws.cell(row=sum_row, column=4, value=f"=SUM(D{data_start}:D{data_end})").number_format = '"S/ "#,##0.00'
    ws.cell(row=sum_row, column=5, value=f"=SUM(E{data_start}:E{data_end})").number_format = "#,##0"
    ws.cell(row=sum_row, column=6, value=f"=SUM(F{data_start}:F{data_end})").number_format = "#,##0.00"
    ws.cell(row=sum_row, column=7, value=f"=SUM(G{data_start}:G{data_end})").number_format = "#,##0.00"
    ws.cell(row=sum_row, column=8, value=f"=SUM(H{data_start}:H{data_end})").number_format = '"S/ "#,##0.00'
    ws.cell(row=sum_row, column=9, value=f"=SUM(I{data_start}:I{data_end})").number_format = '"S/ "#,##0.00'
    
    for c in range(1, 10):
        c_cell = ws.cell(row=sum_row, column=c)
        c_cell.font = font_bold
        c_cell.fill = fill_subtotal
        c_cell.border = Border(top=thin, bottom=Side(style="double", color=c_navy), left=thin, right=thin)
    
    # 4. PANEL LATERAL: PARÁMETROS DEL MODELO Y FÓRMULAS EXCEL
    ws.merge_cells("K5:N5")
    ws["K5"] = "PARÁMETROS DEL MODELO (Fórmulas Excel Oficiales)"
    ws["K5"].font = font_section
    ws["K5"].alignment = Alignment(vertical="center")
    
    kpis = [
        ("Número de Envíos (n):", f"=COUNT(C{data_start}:C{data_end})", "#,##0", "Total de observaciones analizadas"),
        ("Pendiente (m) [PENDIENTE]:", f"=SLOPE(D{data_start}:D{data_end}, C{data_start}:C{data_end})", "0.0000", "Costo variable marginal por kilómetro adicional (S//km)"),
        ("Intersección (b) [INTERSECCION.EJE]:", f"=INTERCEPT(D{data_start}:D{data_end}, C{data_start}:C{data_end})", '"S/ "#,##0.00', "Costo fijo base de despacho/estiba sin recorrido"),
        ("Coef. Determinación (R²) [COEFICIENTE.R2]:", f"=RSQ(D{data_start}:D{data_end}, C{data_start}:C{data_end})", "0.0000", "% de variación del costo explicado por la distancia"),
        ("Coef. Correlación de Pearson (r):", f"=CORREL(C{data_start}:C{data_end}, D{data_start}:D{data_end})", "0.0000", "Fuerza y dirección de la relación lineal entre X e Y"),
        ("Error Típico Estándar:", f"=STEYX(D{data_start}:D{data_end}, C{data_start}:C{data_end})", '"S/ "#,##0.00', "Dispersión media de los errores de estimación")
    ]
    
    kpi_start = 7
    for idx, (label, formula, num_format, desc) in enumerate(kpis):
        kr = kpi_start + idx
        ws.cell(row=kr, column=11, value=label).font = font_bold
        ws.cell(row=kr, column=11).border = border_all
        ws.cell(row=kr, column=11).alignment = Alignment(vertical="center")
        
        val_cell = ws.cell(row=kr, column=12, value=formula)
        val_cell.font = font_kpi_val
        val_cell.number_format = num_format
        val_cell.border = border_all
        val_cell.alignment = Alignment(horizontal="right", vertical="center")
        
        ws.merge_cells(start_row=kr, start_column=13, end_row=kr, end_column=14)
        desc_cell = ws.cell(row=kr, column=13, value=desc)
        desc_cell.font = Font(name="Segoe UI", size=9, italic=True, color="4B5563")
        desc_cell.border = border_all
        desc_cell.alignment = Alignment(vertical="center")
        ws.cell(row=kr, column=14).border = border_all
        ws.row_dimensions[kr].height = 22
        
    # Ecuación del Modelo
    eq_row = kpi_start + len(kpis) + 1
    ws.merge_cells(start_row=eq_row, start_column=11, end_row=eq_row, end_column=14)
    ws.cell(row=eq_row, column=11, value='="ECUACIÓN FINAL:   Ŷ = " & TEXT(L8,"0.0000") & " · X + " & TEXT(L9,"0.00")')
    ws.cell(row=eq_row, column=11).font = font_formula
    ws.cell(row=eq_row, column=11).fill = PatternFill(start_color="D1FAE5", end_color="D1FAE5", fill_type="solid")
    ws.cell(row=eq_row, column=11).alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[eq_row].height = 26
    
    # 5. SIMULADOR INTERACTIVO PREDICTIVO EN TIEMPO REAL (PRONOSTICO.LINEAL)
    sim_title_row = eq_row + 2
    ws.merge_cells(start_row=sim_title_row, start_column=11, end_row=sim_title_row, end_column=14)
    ws.cell(row=sim_title_row, column=11, value="SIMULADOR PREDICTIVO EN TIEMPO REAL (PRONOSTICO.LINEAL)")
    ws.cell(row=sim_title_row, column=11).font = font_section
    ws.cell(row=sim_title_row, column=11).alignment = Alignment(vertical="center")
    
    sim_r1 = sim_title_row + 1
    ws.cell(row=sim_r1, column=11, value="Ingrese Distancia a Cotizar (km):").font = font_bold
    ws.cell(row=sim_r1, column=11).border = border_sim
    ws.cell(row=sim_r1, column=11).fill = fill_sim
    input_cell = ws.cell(row=sim_r1, column=12, value=650) # Valor interactivo editable
    input_cell.font = Font(name="Segoe UI", size=13, bold=True, color=c_navy)
    input_cell.number_format = "#,##0"
    input_cell.border = border_sim
    input_cell.fill = fill_sim
    input_cell.alignment = Alignment(horizontal="right", vertical="center")
    
    ws.merge_cells(start_row=sim_r1, start_column=13, end_row=sim_r1, end_column=14)
    ws.cell(row=sim_r1, column=13, value="<- Modifique este valor para recalcular").font = Font(name="Segoe UI", size=9, bold=True, color="B45309")
    ws.cell(row=sim_r1, column=13).border = border_sim
    ws.cell(row=sim_r1, column=13).fill = fill_sim
    ws.cell(row=sim_r1, column=14).border = border_sim
    
    sim_r2 = sim_r1 + 1
    ws.cell(row=sim_r2, column=11, value="Costo Estimado [PRONOSTICO.LINEAL]:").font = font_bold
    ws.cell(row=sim_r2, column=11).border = border_sim
    ws.cell(row=sim_r2, column=11).fill = fill_sim
    pred_cell = ws.cell(row=sim_r2, column=12, value=f"=FORECAST.LINEAR(L{sim_r1}, D{data_start}:D{data_end}, C{data_start}:C{data_end})")
    pred_cell.font = Font(name="Segoe UI", size=14, bold=True, color="B45309")
    pred_cell.number_format = '"S/ "#,##0.00'
    pred_cell.border = border_sim
    pred_cell.fill = fill_sim
    pred_cell.alignment = Alignment(horizontal="right", vertical="center")
    
    ws.merge_cells(start_row=sim_r2, start_column=13, end_row=sim_r2, end_column=14)
    ws.cell(row=sim_r2, column=13, value="Cálculo automático en tiempo real").font = Font(name="Segoe UI", size=9, italic=True, color="78350F")
    ws.cell(row=sim_r2, column=13).border = border_sim
    ws.cell(row=sim_r2, column=13).fill = fill_sim
    ws.cell(row=sim_r2, column=14).border = border_sim
    
    ws.row_dimensions[sim_r1].height = 26
    ws.row_dimensions[sim_r2].height = 26
    
    # 6. GRÁFICO DE DISPERSIÓN CON LÍNEA DE REGRESIÓN
    chart = ScatterChart()
    chart.title = "Ajuste de Regresión Lineal: Distancia vs Costo de Transporte"
    chart.style = 13
    chart.x_axis.title = "Distancia Recorrida (km)"
    chart.y_axis.title = "Costo de Transporte (S/)"
    chart.width = 19
    chart.height = 12
    
    xvalues = Reference(ws, min_col=3, min_row=data_start, max_row=data_end)
    yvalues = Reference(ws, min_col=4, min_row=data_start, max_row=data_end)
    series = Series(yvalues, xvalues, title_from_data=False)
    series.marker.symbol = "circle"
    series.marker.graphicalProperties.solidFill = "002B49"
    series.marker.graphicalProperties.line.solidFill = "002B49"
    series.graphicalProperties.line.noFill = True
    
    # Línea de tendencia lineal
    from openpyxl.chart.trendline import Trendline
    trendline = Trendline()
    trendline.trendlineType = "linear"
    trendline.dispRSqr = True
    trendline.dispEq = True
    series.trendline = trendline
    
    chart.series.append(series)
    ws.add_chart(chart, f"K{sim_r2 + 3}")
    
    # Ajustar anchos de columnas
    col_widths = {
        "A": 12, "B": 22, "C": 18, "D": 20, "E": 14, "F": 16, "G": 18, "H": 18, "I": 18,
        "J": 4, "K": 36, "L": 20, "M": 32, "N": 16
    }
    for col_letter, width in col_widths.items():
        ws.column_dimensions[col_letter].width = width
        
    wb.save("Sistema_Regresion_Logistica.xlsx")
    print("Archivo Excel 'Sistema_Regresion_Logistica.xlsx' generado con éxito.")

if __name__ == "__main__":
    crear_excel_regresion()

