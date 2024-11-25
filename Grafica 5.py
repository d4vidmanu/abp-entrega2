lengths = np.linspace(0.1, 5, 100)  # Diferentes longitudes
T_average = T_inf + q_dot / (k * lambda_val**2) * (1 - np.exp(-lambda_val * lengths))

plt.figure(figsize=(8, 6))
plt.plot(lengths, T_average, label="Temperatura Promedio vs. Longitud")
plt.xlabel("Longitud del Conductor (m)")
plt.ylabel("Temperatura Promedio (°C)")
plt.title("Efecto de la Longitud del Conductor")
plt.legend()
plt.grid(True)
plt.show()
