import os
import shutil
import zipfile

def organizar_entregables():
    base_dir = r"c:\Users\PC\Desktop\Matematica discreta trabajo grupal"
    codigo_dir = os.path.join(base_dir, "03 Código")
    os.makedirs(codigo_dir, exist_ok=True)
    
    archivos_codigo = [
        "app.py",
        "generar_excel.py",
        "generar_datos.py",
        "Sistema_Regresion_Logistica.xlsx",
        "datos_logisticos.csv",
        "requirements.txt",
        "ejecutar_sistema.bat",
        "README.md"
    ]
    
    for f in archivos_codigo:
        src = os.path.join(base_dir, f)
        dst = os.path.join(codigo_dir, f)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"Copiado a 03 Código/: {f}")
            
    print("Estructura de entregables organizada con éxito.")

if __name__ == "__main__":
    organizar_entregables()

