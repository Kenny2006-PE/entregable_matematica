@echo off
title Sistema Interactivo de Regresion Lineal - USIL
echo ==============================================================
echo    UNIVERSIDAD SAN IGNACIO DE LOYOLA (USIL)
echo    Curso: Matematica Discreta
echo    Proyecto: Sistema Interactivo de Regresion Lineal
echo ==============================================================
echo.
echo [1/3] Verificando dependencias...
pip install -r requirements.txt
echo.
echo [2/3] Generando datos y archivo Excel oficial...
python generar_datos.py
python generar_excel.py
echo.
echo [3/3] Iniciando aplicacion interactiva en Streamlit...
echo La aplicacion se abrira en su navegador web en http://localhost:8501
streamlit run app.py
pause

