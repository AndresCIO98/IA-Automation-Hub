print("Bienvenido a tu segundo script inteligente")

respuesta = input("¿Te gusta programar en Python? (sí/no): ").strip().lower()

if respuesta == "sí":
    print("¡Excelente! Python es muy poderoso y divertido.")
elif respuesta == "no":
    print("No te preocupes, ¡ya verás que poco a poco te encantará!")
else:
    print("Lo siento, no entendí tu respuesta. Intenta escribir 'sí' o 'no'.")
