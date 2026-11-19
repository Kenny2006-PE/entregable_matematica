@echo off
title Sistema Interactivo de Regresion Lineal - USIL
echo ==============================================================
echo    UNIVERSIDAD SAN IGNACIO DE LOYOLA (USIL)
echo    Curso: Matematica Discreta
echo    Proyecto: Sistema Interactivo de Regresion Lineal (Datos Reales)
echo ==============================================================
echo.
echo [1/2] Verificando dependencias...
pip install -r requirements.txt
echo.
echo [2/2] Iniciando aplicacion interactiva en Streamlit...
echo La aplicacion se abrira en su navegador web en http://localhost:8501
streamlit run app.py
pause
