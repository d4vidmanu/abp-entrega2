# Diferentes valores de h
h_values = [5, 10, 20]  # W/m²°C

plt.figure(figsize=(8, 6))
for h in h_values:
    lambda_val = np.sqrt(h * p / (k * Ac))
    T = C1 * np.exp(lambda_val * x) + C2 * np.exp(-lambda_val * x) + T_inf + q_dot / (k * lambda_val**2)
    plt.plot(x, T, label=f"h = {h} W/m²°C")
plt.xlabel("Posición a lo largo del conductor (m)")
plt.ylabel("Temperatura (°C)")
plt.title("Efecto del Coeficiente de Convección (h)")
plt.legend()
plt.grid(True)
plt.show()
