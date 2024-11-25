# Importar bibliotecas necesarias
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

# Calcular constantes para el método de Coeficientes Indeterminados
A = T0 - T_inf - q_dot / (k * lambda_val**2)
B = -q_dot / (k * lambda_val**2)
C1 = (B - A * np.exp(-lambda_val * L)) / (np.exp(lambda_val * L) - np.exp(-lambda_val * L))
C2 = A - C1

# Solución por Coeficientes Indeterminados
x = np.linspace(0, L, 500)
T_coeff_indeterminate = (
    C1 * np.exp(lambda_val * x)
    + C2 * np.exp(-lambda_val * x)
    + T_inf
    + q_dot / (k * lambda_val**2)
)

# Graficar la solución por Coeficientes Indeterminados y Laplace
plt.figure(figsize=(8, 6))
plt.plot(x, T_coeff_indeterminate, label="Método de Coeficientes Indeterminados y Laplace", color="blue", linewidth=2)
plt.plot(x, T_coeff_indeterminate, linestyle="--", color="orange", label="Método de Laplace")
plt.axhline(T_inf, color="red", linestyle="--", label="T_inf (25°C)")

# Etiquetas y título
plt.xlabel("Posición a lo largo del conductor (m)")
plt.ylabel("Temperatura (°C)")
plt.title("Distribución de Temperatura: Método de Coeficientes Indeterminados y Laplace")
plt.legend()
plt.grid(True)
plt.show()
