# Diferentes valores de generación interna de calor
q_values = [20000, 50000, 100000]  # W/m³

plt.figure(figsize=(8, 6))
for q in q_values:
    T = C1 * np.exp(lambda_val * x) + C2 * np.exp(-lambda_val * x) + T_inf + q / (k * lambda_val**2)
    plt.plot(x, T, label=f"q = {q} W/m³")
plt.xlabel("Posición a lo largo del conductor (m)")
plt.ylabel("Temperatura (°C)")
plt.title("Efecto de la Generación Interna de Calor")
plt.legend()
plt.grid(True)
plt.show()
