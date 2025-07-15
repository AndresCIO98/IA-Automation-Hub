# Autor: Andrés Varon
# Script: RUIN Pro 2.0 – Automatización avanzada con registro de usuarios

from datetime import datetime

def clasificar_usuario(edad, nivel):
    nivel = nivel.lower().strip()
    if edad < 18:
        return "🟡 Acceso limitado. Se requiere supervisión."
    elif "avanzado" in nivel:
        return "🟢 Acceso completo a funciones profesionales."
    elif "básico" in nivel or "basico" in nivel:
        return "🟢 Bienvenido. Acceso básico habilitado."
    elif "intermedio" in nivel:
        return "🟢 Acceso intermedio habilitado."
    else:
        return "🔴 Nivel desconocido. Contacta soporte."

def guardar_resultado(nombre, edad, nivel, resultado):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{now}] {nombre} | Edad: {edad} | Nivel: {nivel} => {resultado}\n"

    with open("logs/usuarios.txt", "a") as archivo:
        archivo.write(linea)

def main():
    print("\n💼 Bienvenido a IA-Automation-Hub – RUIN Pro 2.0\n")

    nombre = input("👤 Ingresa tu nombre: ")
    try:
        edad = int(input("🎂 Ingresa tu edad: "))
    except ValueError:
        print("❌ Edad inválida. Usa un número.")
        return

    nivel = input("📊 ¿Cuál es tu nivel de usuario? (básico/intermedio/avanzado): ")

    print("\n🧠 Procesando tu perfil...\n")
    resultado = clasificar_usuario(edad, nivel)

    print(f"✅ Hola {nombre}, resultado de acceso:")
    print(resultado)

    guardar_resultado(nombre, edad, nivel, resultado)

if __name__ == "__main__":
    main()
