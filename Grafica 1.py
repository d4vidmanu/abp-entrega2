import numpy as np
import matplotlib.pyplot as plt

# Parámetros generales
T_inf = 25  # Temperatura ambiente (°C)
T0 = 75  # Temperatura inicial (°C)
q_dot = 50000  # Generación interna de calor (W/m³)
k = 237  # Conductividad térmica (W/m°C)
h = 10  # Coeficiente de convección (W/m²°C)
Ac = 0.0007098  # Área transversal (m²)
p = 0.03  # Perímetro (m)
L = 1.0  # Longitud del conductor (m)

# Calcular lambda
lambda_val = np.sqrt(h * p / (k * Ac))

# Distribución de temperatura
x = np.linspace(0, L, 500)
C1 = (T0 - T_inf - q_dot / (k * lambda_val**2)) / 2
C2 = (T0 - T_inf - q_dot / (k * lambda_val**2)) / 2
T = C1 * np.exp(lambda_val * x) + C2 * np.exp(-lambda_val * x) + T_inf + q_dot / (k * lambda_val**2)

# Graficar
plt.figure(figsize=(8, 6))
plt.plot(x, T, label='T(x)')
plt.xlabel("Posición a lo largo del conductor (m)")
plt.ylabel("Temperatura (°C)")
plt.title("Distribución de Temperatura a lo Largo del Conductor")
plt.legend()
plt.grid(True)
plt.show()
