# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = {
    "Tiempo": [1, 3, 6, 12, 24, 36, 48, 70],
    "Consumo NaCN": [700, 950, 1000, 1060, 1080, 1180, 1300, 1550],
    "Consumo NaOH": [680, 1300, 1600, 2000, 2600, 3100, 3200, 3250],
    "%Recuperación": [36, 53.5, 65.3, 72, 78.3, 81.8, 86.3, 89.3],
}


# df = pd.DataFrame(data)
# Frame = pd.read_excel(
#     "Z:/TECSUP/CICLO V/Hidrometalurgia/2020/Prácticas/Práctica calificada 04 - Carrillo Correa Julio Isaias.xlsx"
# )

# print(df)

plt.plot(data["Tiempo"], data["%Recuperación"], "b--p")
plt.title("Recuperación de Cu")
plt.ylim(0, 100)
plt.grid(color="b", linestyle="-", linewidth=0.1)
plt.xticks(np.arange(0, max(data["Tiempo"]) + 5, 5), size="xx-small")
plt.xlabel("Tiempo(s)")
plt.yticks(np.arange(0, 100, 5), size="xx-small")
plt.ylabel("Recuperación(%)")
plt.show()


# plt.plot(data["Tiempo"],data["Consumo NaCN"])

# plt.show()

# plt.plot(data["Tiempo"],data["Consumo NaOH"])
# plt.show()
