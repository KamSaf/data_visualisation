import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def zad_1():
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


def zad_2():
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
        3,
        wydatki[3] + 100,
        "Planowane\n(łącznie)",
        ha="center",
        va="bottom",
        fontsize=9,
    )

    hist_patch = mpatches.Patch(color="steelblue", label="Dane historyczne")
    plan_patch = mpatches.Patch(
        facecolor="gold", hatch="//", label="Planowane (łącznie)"
    )
    ax.legend(handles=[hist_patch, plan_patch])

    plt.tight_layout()
    plt.title("Wydatki na badania i rozwój w Polsce")
    plt.show()


if __name__ == "__main__":
    zad_1()
    zad_2()
