time =np.linspace(0, 10, 500)  # Tiempo en segundos
X, T_time = np.meshgrid(x, time)
Temperature = T_inf + (T0 - T_inf) * np.exp(-lambda_val * X)

plt.figure(figsize=(10, 6))
plt.contourf(X, T_time, Temperature, cmap="coolwarm", levels=50)
plt.colorbar(label="Temperatura (°C)")
plt.xlabel("Posición a lo largo del conductor (m)")
plt.ylabel("Tiempo (s)")
plt.title("Evolución de la Temperatura a lo Largo del Tiempo")
plt.show()
