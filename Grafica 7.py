# Importar bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros generales
T_inf = 25  # Temperatura ambiente (°C)
T0 = 75  # Temperatura inicial (°C)
q_dot = 50000  # Generación interna de calor (W/m³)
k = 237  # Conductividad térmica (W/m°C)
Ac = 0.0007098  # Área transversal (m²)
p = 0.03  # Perímetro (m)
L = 1.0  # Longitud del conductor (m)

# Rango de coeficientes de convección (h)
h_values = np.linspace(5, 20, 50)  # (W/m²°C)
x_values = np.linspace(0, L, 50)  # Posiciones a lo largo del conductor

# Crear malla para h y x
H, X = np.meshgrid(h_values, x_values)

# Calcular lambda para cada valor de h
Lambda = np.sqrt(H * p / (k * Ac))

# Calcular temperatura T(x, h)
T = (
    (T0 - T_inf - q_dot / (k * Lambda**2)) * np.cosh(Lambda * (L - X)) / np.cosh(Lambda * L)
    + T_inf
    + q_dot / (k * Lambda**2)
)

# Crear gráfica 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Graficar superficie
surf = ax.plot_surface(X, H, T, cmap="viridis", edgecolor='k')

# Añadir etiquetas
ax.set_xlabel("Posición a lo largo del conductor (m)")
ax.set_ylabel("Coeficiente de convección h (W/m²°C)")
ax.set_zlabel("Temperatura (°C)")
ax.set_title("Distribución de Temperatura en Función de h y Posición")

# Añadir barra de colores
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label="Temperatura (°C)")

plt.show()

