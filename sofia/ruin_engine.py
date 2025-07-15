# Módulo de decisiones RUIN – IA-Automation-Hub
from datetime import datetime

def clasificar_usuario(edad, nivel):
    nivel = nivel.lower().strip()
    if edad < 18:
        return "🟡 Acceso limitado. Se requiere supervisión."
    elif "avanzado" in nivel:
        return "🟢 Acceso completo a funciones profesionales."
    elif "basico" in nivel or "básico" in nivel:
        return "🟢 Bienvenido. Acceso básico habilitado."
    elif "intermedio" in nivel:
        return "🟢 Acceso intermedio habilitado."
    else:
        return "🔴 Nivel desconocido. Contacta soporte."

def registrar(nombre, edad, nivel, resultado):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{now}] {nombre} | Edad: {edad} | Nivel: {nivel} => {resultado}\n"

    with open("logs/usuarios.txt", "a") as archivo:
        archivo.write(linea)
