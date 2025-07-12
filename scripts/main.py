# main.py
import pandas as pd
import matplotlib.pyplot as plt

# Crear un DataFrame de ejemplo
data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'],
    'Ventas': [1200, 1500, 1700, 1600]
}

df = pd.DataFrame(data)

# Mostrar el DataFrame en consola
print("Resumen de ventas:")
print(df)

# Graficar
plt.plot(df['Mes'], df['Ventas'], marker='o', color='blue')
plt.title('Ventas por mes')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.grid(True)
plt.tight_layout()
plt.show()
