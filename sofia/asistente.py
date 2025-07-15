# Asistente Sofía – integración con motor RUIN
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sofia.ruin_engine import clasificar_usuario, registrar

def iniciar_sofia():
    print("\n🤖 Sofía activada – Evaluación inteligente con RUIN\n")

    nombre = input("👤 Tu nombre: ")
    try:
        edad = int(input("🎂 Tu edad: "))
    except ValueError:
        print("❌ Edad inválida.")
        return

    nivel = input("📊 Tu nivel (básico/intermedio/avanzado): ")
    resultado = clasificar_usuario(edad, nivel)

    print(f"\n✅ Hola {nombre}, resultado de Sofía:")
    print(resultado)

    registrar(nombre, edad, nivel, resultado)

if __name__ == "__main__":
    iniciar_sofia()
