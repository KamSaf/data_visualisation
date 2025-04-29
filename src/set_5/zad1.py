import matplotlib.pyplot as plt


base_r = 0.2
startx = 0
starty = 0
margines = 0.1
modifier = 1.1

china_pop = 1408000000
india_pop = 1454000000
ratio = india_pop / float(china_pop)
india_r = base_r * ratio

fig, ax = plt.subplots()
circle = plt.Circle((-base_r * modifier, starty), base_r, color="red")
ax.add_patch(circle)
ax.annotate(
    "Chiny",
    (-base_r * modifier, starty),
    color="w",
    fontsize=10,
    ha="center",
    va="center",
)

circle = plt.Circle((base_r * modifier, starty), india_r, color="orange")
ax.add_patch(circle)
ax.annotate(
    "Indie",
    (base_r * modifier, starty),
    color="w",
    fontsize=10,
    ha="center",
    va="center",
)
plt.hlines(
    y=[starty + base_r, starty - base_r],
    xmin=startx - base_r * 2,
    xmax=starty + india_r * 2,
    color="black",
    linewidth=0.7,
)


ax.set_xlim(startx - 2 * base_r - margines, startx + 2 * base_r + margines)
ax.set_ylim(starty - base_r - margines, starty + base_r + margines)
ax.set_aspect(1)
ax.axis("off")
plt.title(
    f"Udział populacji Chin w populacji Indii {round(china_pop/float(india_pop)*100, 2)}%"
)
plt.show()
