import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FixedLocator, FuncFormatter

data = pd.read_csv("../data/sprzedaz_percepcja.csv", sep=",", decimal=".")


def plot_1(data: pd.DataFrame) -> None:
    _, ax = plt.subplots(figsize=(17, 9))
    y_scale = [float(i) for i in range(0, 301, 50)]
    plt.ylim((y_scale[0], y_scale[-1]))
    for threshold in y_scale[1:]:
        plt.axhline(y=threshold, color="black", alpha=0.8, linewidth=1)
    plt.plot(
        data["Miesiąc"],
        data["SmartTV"],
        marker="D",
        color="steelblue",
        linestyle="-",
        label="SmartTV",
        linewidth=2,
    )
    plt.plot(
        data["Miesiąc"],
        data["TV"],
        marker="s",
        color="firebrick",
        markersize=12,
        linestyle="-",
        label="TV",
        linewidth=2,
    )
    ax.xaxis.set_minor_locator(FixedLocator([i + 0.5 for i in range(0, 12, 1)]))
    ax.set_xticklabels(data["Miesiąc"], rotation=45)
    ax.tick_params(axis="x", which="major", bottom=False)
    plt.gca().tick_params(axis="x", which="minor", width=1, length=4)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y:.2f}"))
    plt.yticks(y_scale)
    plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=5)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.show()


# 1. Usuń elementy nie wnoszące nic do zrozumienia prezentowanego problemu. Zastosuj:
#     Prawo domykania
#     FactorInk
def plot_2(data: pd.DataFrame) -> None:
    _, ax = plt.subplots(figsize=(17, 9))
    y_scale = [float(i) for i in range(0, 301, 50)]
    plt.ylim((y_scale[0], y_scale[-1]))
    plt.plot(
        data["Miesiąc"],
        data["SmartTV"],
        color="steelblue",
        linestyle="-",
        label="SmartTV",
        linewidth=2,
    )
    plt.plot(
        data["Miesiąc"],
        data["TV"],
        color="firebrick",
        linestyle="-",
        label="TV",
        linewidth=2,
    )
    ax.xaxis.set_minor_locator(FixedLocator([i + 0.5 for i in range(0, 12, 1)]))
    ax.set_xticklabels(data["Miesiąc"], rotation=45)
    ax.tick_params(axis="x", which="major", bottom=False)
    plt.gca().tick_params(axis="x", which="minor", width=1, length=4)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{y:.2f}"))
    plt.yticks(y_scale)
    plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=5)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.show()


# 2. Użyj najkrótszych jak to tylko możliwe etykiet danych, pozwól odbiorcy czytać "naturalnie". Zastosuj:
#     Prawo kontynuacji
def plot_3(data: pd.DataFrame) -> None:
    _, ax = plt.subplots(figsize=(17, 9))
    y_scale = [float(i) for i in range(0, 301, 50)]
    plt.ylim((y_scale[0], y_scale[-1]))
    plt.plot(
        data["Miesiąc"],
        data["SmartTV"],
        color="steelblue",
        linestyle="-",
        label="SmartTV",
        linewidth=2,
    )
    plt.plot(
        data["Miesiąc"],
        data["TV"],
        color="firebrick",
        linestyle="-",
        label="TV",
        linewidth=2,
    )
    ax.xaxis.set_minor_locator(FixedLocator([i + 0.5 for i in range(0, 12, 1)]))
    ax.set_xticklabels(m[:3] for m in data["Miesiąc"])
    ax.tick_params(axis="x", which="major", bottom=False)
    plt.gca().tick_params(axis="x", which="minor", width=1, length=4)
    plt.yticks(y_scale)
    plt.legend(loc="upper center", bbox_to_anchor=(0.5, -0.05), ncol=5)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.show()


# 3. Usuń elementy rozpraszające (legendę). Zastosuj:
#     Prawo bliskości
#     Prawo podobieństwa
def plot_4(data: pd.DataFrame) -> None:
    _, ax = plt.subplots(figsize=(17, 9))
    y_scale = [float(i) for i in range(0, 301, 50)]
    plt.ylim((y_scale[0], y_scale[-1]))
    plt.plot(
        data["Miesiąc"],
        data["SmartTV"],
        color="steelblue",
        linestyle="-",
        label="SmartTV",
        linewidth=2,
    )
    plt.plot(
        data["Miesiąc"],
        data["TV"],
        color="firebrick",
        linestyle="-",
        label="TV",
        linewidth=2,
    )
    ax.xaxis.set_minor_locator(FixedLocator([i + 0.5 for i in range(0, 12, 1)]))
    ax.set_xticklabels(m[:3] for m in data["Miesiąc"])
    ax.tick_params(axis="x", which="major", bottom=False)
    plt.gca().tick_params(axis="x", which="minor", width=1, length=4)
    plt.yticks(y_scale)
    plt.text(11.3, 180, "SmartTV", fontsize=10, color="steelblue", weight="bold")
    plt.text(11.3, 150, "TV", fontsize=10, color="firebrick", weight="bold")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.show()


# 4. Pomóż czytelnikowi zwrócić uwagę na istotne elementy. Pokaż mu to co chcesz żeby zobaczył.
def plot_5(data: pd.DataFrame) -> None:
    df_1 = data.iloc[:5, :]
    df_2 = data.iloc[4:, :]

    _, ax = plt.subplots(figsize=(17, 9))
    y_scale = [float(i) for i in range(0, 301, 50)]
    plt.ylim((y_scale[0], y_scale[-1]))
    plt.plot(
        df_1["Miesiąc"],
        df_1["SmartTV"],
        color="gray",
        linestyle="-",
        label="SmartTV",
        linewidth=2,
    )
    plt.plot(
        df_1["Miesiąc"],
        df_1["TV"],
        color="gray",
        linestyle="-",
        label="TV",
        linewidth=2,
    )

    plt.plot(
        df_2["Miesiąc"],
        df_2["SmartTV"],
        color="lightseagreen",
        linestyle="-",
        label="SmartTV",
        linewidth=2,
    )
    plt.plot(
        df_2["Miesiąc"],
        df_2["TV"],
        color="firebrick",
        linestyle="-",
        label="TV",
        linewidth=2,
    )
    ax.xaxis.set_minor_locator(FixedLocator([i + 0.5 for i in range(0, 12, 1)]))
    ax.set_xticklabels(m[:3] for m in data["Miesiąc"])
    ax.tick_params(axis="x", which="major", bottom=False)
    plt.gca().tick_params(axis="x", which="minor", width=1, length=4)
    plt.yticks(y_scale)
    plt.text(11.3, 180, "SmartTV", fontsize=10, color="lightseagreen", weight="bold")
    plt.text(11.3, 150, "TV", fontsize=10, color="firebrick", weight="bold")
    plt.text(11.3, 165, "-33", fontsize=10, color="red", weight="bold")
    plt.text(3.75, 270, "Netflix", fontsize=15, color="black", weight="bold")
    plt.text(6.92, 220, "217", fontsize=10, color="lightseagreen", weight="bold")
    plt.text(8.92, 95, "105", fontsize=10, color="firebrick", weight="bold")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.axvline(x=4.35, ymin=0.1, ymax=1, color="gray", alpha=0.6, linewidth=60)
    plt.title(label="Sprzedaż", loc="right", weight="bold")
    plt.show()


# 4. Pomóż czytelnikowi zwrócić uwagę na istotne elementy. Pokaż mu to co chcesz żeby zobaczył.
def plot_6(data: pd.DataFrame) -> None:
    df_1 = data.iloc[:5, :]
    df_2 = data.iloc[4:, :]

    _, ax = plt.subplots(figsize=(17, 9))
    y_scale = [float(i) for i in range(0, 301, 50)]
    plt.ylim((y_scale[0], y_scale[-1]))
    plt.plot(
        df_1["Miesiąc"],
        df_1["SmartTV"],
        color="gray",
        linestyle="-",
        label="SmartTV",
        linewidth=2,
    )
    plt.plot(
        df_1["Miesiąc"],
        df_1["TV"],
        color="gray",
        linestyle="-",
        label="TV",
        linewidth=2,
    )

    plt.plot(
        df_2["Miesiąc"],
        df_2["SmartTV"],
        color="midnightblue",
        linestyle="-",
        label="SmartTV",
        linewidth=2,
    )
    plt.plot(
        df_2["Miesiąc"],
        df_2["TV"],
        color="midnightblue",
        linestyle="-",
        label="TV",
        linewidth=2,
    )
    ax.xaxis.set_minor_locator(FixedLocator([i + 0.5 for i in range(0, 12, 1)]))
    ax.set_xticklabels(m[:3] for m in data["Miesiąc"])
    ax.tick_params(axis="x", which="major", bottom=False)
    plt.gca().tick_params(axis="x", which="minor", width=1, length=4)
    plt.yticks(y_scale)
    plt.text(11.3, 180, "SmartTV", fontsize=10, color="midnightblue", weight="bold")
    plt.text(11.3, 150, "TV", fontsize=10, color="midnightblue", weight="bold")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.title(label="Sprzedaż", loc="right", weight="bold")
    plt.show()


if "__main__" == __name__:
    # 1.
    plot_1(data)
    # 2.
    plot_2(data)
    # 3.
    plot_3(data)
    # 4.
    plot_4(data)
    # 5.
    plot_5(data)
    plot_6(data)
