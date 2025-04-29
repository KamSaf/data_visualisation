import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

rok = ["2010", "2011", "2012", "2013–2016"]
wydatki = [258, 363, 1282, 4862]

colors = ["steelblue" for i in range(len(rok) - 1)] + ["gold"]
hatch = ["" for i in range(len(rok) - 1)] + ["//"]

fig, ax = plt.subplots()
bars = ax.bar(rok, wydatki, color=colors)

for i in range(len(bars)):
    if hatch[i]:
        bars[i].set_hatch(hatch[i])

ax.set_ylabel("Wydatki (mln zł)")
ax.set_title("Wydatki w latach 2010–2016")
ax.set_ylim(0, 5500)
ax.text(
    3, wydatki[3] + 100, "Planowane\n(łącznie)", ha="center", va="bottom", fontsize=9
)

hist_patch = mpatches.Patch(color="steelblue", label="Dane historyczne")
plan_patch = mpatches.Patch(facecolor="gold", hatch="//", label="Planowane (łącznie)")
ax.legend(handles=[hist_patch, plan_patch])


plt.tight_layout()
plt.title("Wydatki na badania i rozwój w Polsce")
plt.show()
