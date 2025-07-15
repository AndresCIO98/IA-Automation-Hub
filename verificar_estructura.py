# Autor: Andrés Varon
# Proyecto: IA-Automation-Hub
# Script de verificación de estructura inicial

import os
import sys

# Archivos requeridos
archivos = [
    "LICENSE-MIT",
    "LICENSE-APACHE",
    "LICENSE-GPLv3",
    "LICENSE-PRIVATE",
    "LICENSE-COMMERCIAL.txt",
    "README.md",
    "requirements.txt"
]

# Carpetas requeridas
carpetas = [
    "scripts",
    "sofia",
    "docs"
]

def verificar_archivos():
    print("🔍 Verificando archivos esenciales...")
    faltantes = []
    for archivo in archivos:
        if not os.path.isfile(archivo):
            faltantes.append(archivo)
            print(f"❌ Falta archivo: {archivo}")
        else:
            print(f"✅ Archivo presente: {archivo}")
    return faltantes

def verificar_carpetas():
    print("\n📁 Verificando carpetas requeridas...")
    faltantes = []
    for carpeta in carpetas:
        if not os.path.isdir(carpeta):
            faltantes.append(carpeta)
            print(f"❌ Falta carpeta: {carpeta}")
        else:
            print(f"✅ Carpeta presente: {carpeta}")
    return faltantes

def verificar_entorno_python():
    print("\n🐍 Verificando entorno Python...")
    try:
        import pip
        print(f"✅ Python funcionando correctamente. Versión: {sys.version.split()[0]}")
    except Exception as e:
        print("❌ Python no está funcionando correctamente.")
        print(e)

if __name__ == "__main__":
    errores = 0
    if verificar_archivos():
        errores += 1
    if verificar_carpetas():
        errores += 1
    verificar_entorno_python()

    if errores == 0:
        print("\n🎉 Todo está listo. Puedes continuar con tu clase y el módulo RUIN.")
    else:
        print("\n⚠️ Faltan elementos. Revisa lo anterior antes de continuar.")

