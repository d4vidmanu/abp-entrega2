heat_sources = ["Generación Interna (q)", "Conducción (k)", "Convección (h)"]
values = [q_dot, k, h]  # Magnitudes aproximadas

fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(heat_sources, values, color=["red", "blue", "green"])
ax.set_ylabel("Magnitud")
ax.set_title("Contribuciones Energéticas en el Modelo Térmico")
plt.show()
