import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def crear_planificacion():
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Cronograma y Planificación"
    ws.views.sheetView[0].showGridLines = True
    
    c_navy = "002B49"
    c_blue = "2563EB"
    c_header = "1E293B"
    c_accent = "FF6B00"
    c_done = "10B981"
    
    font_title = Font(name="Segoe UI", size=14, bold=True, color="FFFFFF")
    font_subtitle = Font(name="Segoe UI", size=10, color="CBD5E1")
    font_header = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
    font_cell = Font(name="Segoe UI", size=9, color="1E293B")
    font_bold = Font(name="Segoe UI", size=9, bold=True, color="1E293B")
    
    fill_title = PatternFill(start_color=c_navy, end_color=c_navy, fill_type="solid")
    fill_header = PatternFill(start_color=c_header, end_color=c_header, fill_type="solid")
    fill_done = PatternFill(start_color="D1FAE5", end_color="D1FAE5", fill_type="solid")
    fill_bar = PatternFill(start_color="38BDF8", end_color="38BDF8", fill_type="solid")
    
    thin = Side(border_style="thin", color="CBD5E1")
    border_all = Border(left=thin, right=thin, top=thin, bottom=thin)
    
    # 1. ENCABEZADO
    ws.merge_cells("A1:K1")
    ws["A1"] = "UNIVERSIDAD SAN IGNACIO DE LOYOLA (USIL) — MATEMÁTICA DISCRETA 2026"
    ws["A1"].font = font_title
    ws["A1"].fill = fill_title
    ws["A1"].alignment = Alignment(horizontal="center", vertical="center")
    
    ws.merge_cells("A2:K2")
    ws["A2"] = "04 PLANIFICACIÓN Y CRONOGRAMA DE ACTIVIDADES DEL TRABAJO FINAL (SEMANAS 9 A 15)"
    ws["A2"].font = font_subtitle
    ws["A2"].fill = fill_title
    ws["A2"].alignment = Alignment(horizontal="center", vertical="center")
    
    ws.row_dimensions[1].height = 26
    ws.row_dimensions[2].height = 20
    
    headers = [
        "Fase / Hito", "Actividad Específica", "Responsable(s)", "Semana", 
        "Fecha Inicio", "Fecha Fin", "Estado", "Sem 9-10", "Sem 11-12", "Sem 13-14", "Sem 15"
    ]
    start_row = 4
    for c_idx, h in enumerate(headers, start=1):
        cell = ws.cell(row=start_row, column=c_idx, value=h)
        cell.font = font_header
        cell.fill = fill_header
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = border_all
    ws.row_dimensions[start_row].height = 26
    
    actividades = [
        ("Hito 1: Avance 1", "Definición del caso de estudio logístico y problemática", "Matthias Combe / Kenny Palacin", "Sem 9", "01/09/2026", "08/09/2026", "COMPLETADO", [8]),
        ("Hito 1: Avance 1", "Formulación de objetivos y redacción inicial", "Jeff Espiritu / Ángel Pérez", "Sem 9", "04/09/2026", "12/09/2026", "COMPLETADO", [8]),
        ("Hito 2: Avance 2", "Levantamiento de requerimientos y análisis HW/SW", "Matthias Combe", "Sem 10", "15/09/2026", "22/09/2026", "COMPLETADO", [8, 9]),
        ("Hito 2: Avance 2", "Deducción matemática MCO y ecuaciones normales de Gauss", "Kenny Palacin", "Sem 11", "23/09/2026", "02/10/2026", "COMPLETADO", [9]),
        ("Hito 2: Avance 2", "Implementación del modelo en Microsoft Excel con fórmulas", "Jeff Espiritu", "Sem 12", "03/10/2026", "14/10/2026", "COMPLETADO", [9]),
        ("Hito 3: Entrega Final", "Desarrollo de aplicación interactiva en Python y Streamlit", "Ángel Pérez", "Sem 13", "16/10/2026", "26/10/2026", "COMPLETADO", [10]),
        ("Hito 3: Entrega Final", "Integración de animaciones web con anime.js y Plotly", "Matthias Combe / Ángel Pérez", "Sem 14", "27/10/2026", "03/11/2026", "COMPLETADO", [10]),
        ("Hito 3: Entrega Final", "Ejecución de pruebas de validación cruzada Excel vs Python", "Kenny Palacin / Jeff Espiritu", "Sem 14", "01/11/2026", "05/11/2026", "COMPLETADO", [10]),
        ("Hito 3: Entrega Final", "Consolidación de '01 Informe.docx' con normas APA", "Todo el equipo", "Sem 15", "04/11/2026", "07/11/2026", "COMPLETADO", [11]),
        ("Hito 3: Entrega Final", "Elaboración de diapositivas '02 Presentación.pptx'", "Todo el equipo", "Sem 15", "06/11/2026", "08/11/2026", "COMPLETADO", [11]),
        ("Hito 3: Exposición", "Preparación y simulación de la defensa oral (20 min)", "Todo el equipo", "Sem 15", "08/11/2026", "12/11/2026", "EN CURSO", [11])
    ]
    
    for idx, act in enumerate(actividades):
        r = start_row + 1 + idx
        ws.cell(row=r, column=1, value=act[0]).font = font_bold
        ws.cell(row=r, column=2, value=act[1]).font = font_cell
        ws.cell(row=r, column=3, value=act[2]).font = font_cell
        ws.cell(row=r, column=4, value=act[3]).font = font_bold
        ws.cell(row=r, column=5, value=act[4]).font = font_cell
        ws.cell(row=r, column=6, value=act[5]).font = font_cell
        
        status_cell = ws.cell(row=r, column=7, value=act[6])
        status_cell.font = Font(name="Segoe UI", size=9, bold=True, color="047857" if act[6] == "COMPLETADO" else "B45309")
        status_cell.fill = fill_done if act[6] == "COMPLETADO" else PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")
        status_cell.alignment = Alignment(horizontal="center", vertical="center")
        
        for c in range(1, 8):
            ws.cell(row=r, column=c).border = border_all
            if c in [1, 4, 5, 6]:
                ws.cell(row=r, column=c).alignment = Alignment(horizontal="center", vertical="center")
                
        # Diagrama de Gantt en columnas 8 a 11
        for col_gantt in range(8, 12):
            g_cell = ws.cell(row=r, column=col_gantt)
            g_cell.border = border_all
            if col_gantt in act[7]:
                g_cell.fill = fill_bar
                g_cell.value = "████"
                g_cell.font = Font(color="0284C7", size=8)
                g_cell.alignment = Alignment(horizontal="center", vertical="center")
                
    widths = [18, 38, 26, 12, 14, 14, 16, 12, 12, 12, 12]
    for c_idx, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(c_idx)].width = w
        
    wb.save("04 Planificación.xlsx")
    print("Archivo '04 Planificación.xlsx' generado con éxito.")

if __name__ == "__main__":
    crear_planificacion()

