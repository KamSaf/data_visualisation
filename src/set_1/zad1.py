from math import floor, ceil
import matplotlib.pyplot as plt
import pandas as pd

dane = pd.read_csv("../../data/dane.csv", sep=";", decimal=",", index_col=0)
dane["Sprzedaz calkowita"] = dane["prodA"] + dane["prodB"]
sprzedaz = dane.drop(["prodA", "prodB"], axis=1)

sprzedaz["mies_cat"] = pd.Categorical(
    sprzedaz.Miesiac, categories=["styczen", "luty", "marzec"], ordered=True
)
sprzedaz.sort_values(["mies_cat", "dzien"], inplace=True, ignore_index=True)

s_min = floor(dane["Sprzedaz calkowita"].min())
s_max = ceil(dane["Sprzedaz calkowita"].max())
s_half = s_min + (s_max - s_min) / 2
y_scale = [s_min, s_min + 2, s_half, s_max - 2, s_max]

plt.xlabel("Sprzedaż w tyś.")
plt.ylabel("Dzień")
plt.title("Sprzedaż całkowita w kolejnych dniach kwartału 1.")
plt.plot(sprzedaz["Sprzedaz calkowita"])
plt.ylim((y_scale[0], y_scale[-1]))
plt.xticks([0, 30, 31, 58, 59, 89], ["1", "31", "1", "28", "1", "31"])
plt.yticks(y_scale, [f"{int(el)}k" for el in y_scale])
for threshold in y_scale[1:4]:
    plt.axhline(y=threshold, color="gray", linestyle="dashed", alpha=0.5)
# plt.grid(axis="y", linestyle="--") - linie powstają tam, gdzie są ticksy
plt.show()
