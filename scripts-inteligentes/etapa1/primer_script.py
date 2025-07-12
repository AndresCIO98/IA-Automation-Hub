# primer_script.py
# Autor: CEO Andrés & Sofía AI
# Proyecto: IA-Automation-Hub
# Descripción: Primer script inteligente

def saludar_usuario():
    nombre = input("Hola, ¿cómo te llamas? ")
    print(f"¡Hola {nombre}! Soy Sofía, tu asistente personal.")
    
    respuesta = input("¿Estás listo para automatizar tu mundo? (sí/no): ").lower()
    
    if respuesta == "sí":
        print("¡Excelente! Vamos a crear cosas increíbles juntos. 💪🤖")
    elif respuesta == "no":
        print("Está bien, cuando estés listo aquí estaré contigo. 🌱")
    else:
        print("No entendí tu respuesta, pero seguiré aquí para ayudarte. 😊")

if __name__ == "__main__":
    saludar_usuario()
