def clasificar_usuario(edad, nivel):
    nivel = nivel.lower().strip()
    if edad < 18:
        return "🟡 Acceso limitado. Se requiere supervisión."
    elif "avanzado" in nivel:
        return "🟢 Acceso completo a funciones profesionales."
    elif "básico" in nivel:
        return "🟢 Bienvenido. Acceso básico habilitado."
    elif "intermedio" in nivel:
        return "🟢 Acceso intermedio habilitado."
    else:
        return "🔴 Nivel desconocido. Contacta soporte."

def main():
    print("\n💼 Bienvenido a IA-Automation-Hub – Módulo RUIN\n")

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
