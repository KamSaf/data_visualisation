import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

# import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

np.random.seed(42)

# Zmiany wartości w czasie
okres = 61
data = pd.date_range(start="2024-05-01", periods=okres)
wartosci = np.random.randn(
    okres,
).cumsum()
dane = pd.DataFrame({"Wartość": wartosci, "Data": data})

# Bilans sprzedaży
miesiace = [
    "Start",
    "Styczeń",
    "Luty",
    "Marzec",
    "Kwiecień",
    "Maj",
    "Czerwiec",
    "Lipiec",
    "Bilans",
]
sprzedaz = pd.Series([0, 244, 354, 287, 159, 234, 345, 456, 0])

# Ceny utrzymania nieruchomości (2011)
rok = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
y = [205, 205.8, 206, 206.6, 205, 208, 209, 210, 211, 212]

# Punkty Pucharu Narodów w skokach narciarskich w latach 2016-2019
puchar = pd.read_csv("../../data/puchar.csv")


# ZADANIE 1 ------------------------------------------


def plot_1():
    dane.plot(y="Wartość", figsize=(12, 8))
    plt.show()

    dane.plot(
        x="Data",
        y="Wartość",
        figsize=(12, 8),
        title="Wykres liniowy zmian zjawiska w czasie",
    )
    plt.show()


# ZADANIE 2 ------------------------------------------


def demo_plot_2():
    fig, ax = plt.subplots(figsize=(12, 6))
    dane.index = dane.Data  # type: ignore
    dane.plot(y="Wartość", ax=ax)
    ax.set_title("Wykres liniowy zmian zjawiska w czasie")
    ax.set_xlabel("Data")
    ax.set_ylabel("Wartość")
    cut = dane.Wartość.mean()
    ax.axhline(y=cut, color="r", linestyle="--", label=f"Linia: {cut:.2f}")
    ax.fill_between(
        x=dane.index,
        y1=dane.Wartość,
        y2=cut,
        where=dane.Wartość > cut,  # type: ignore
        color="green",
        label="Wartości dodatnie",
    )
    ax.fill_between(
        x=dane.index,
        y1=dane.Wartość,
        y2=cut,
        where=dane.Wartość <= cut,  # type: ignore
        color="red",
        label="Wartości dodatnie",
    )
    ax.legend(loc="lower left")
    plt.show()


def plot_2():
    np.random.seed(41)
    dane["Inne"] = np.random.randn(
        okres,
    ).cumsum()
    fig, ax = plt.subplots(figsize=(12, 6))

    dane.plot(y=["Wartość", "Inne"], ax=ax)
    ax.set_title("Wykres liniowy zmian zjawiska w czasie")
    ax.set_xlabel("Data")
    ax.set_ylabel("Wartość")

    ax.fill_between(
        x=dane.index,
        y1=dane.Wartość,
        y2=dane.Inne,
        where=dane.Wartość > dane.Inne,  # type: ignore
        color="green",
        label="Wartości dodatnie",
    )
    ax.fill_between(
        x=dane.index,
        y1=dane.Wartość,
        y2=dane.Inne,
        where=dane.Wartość <= dane.Inne,  # type: ignore
        color="red",
        label="Wartości dodatnie",
    )
    ax.legend(loc="lower left")
    plt.show()


# ZADANIE 3 ------------------------------------------


def demo_plot_3():
    zmiany = sprzedaz.diff().fillna(sprzedaz)  # type: ignore
    fig = go.Figure(
        go.Waterfall(
            x=miesiace,
            y=zmiany,
            measure=["absolute"] + ["relative"] * (len(miesiace) - 2) + ["total"],
            connector={
                "line": {"color": "rgb(63, 63, 63)", "width": 0.5, "dash": "dot"}
            },
            increasing={"marker": {"color": "lime"}},
            decreasing={"marker": {"color": "magenta"}},
            totals={"marker": {"color": "skyblue"}},
        )
    )

    fig.update_layout(
        title="Wykres kosztów użytkowania nieruchomości w kolejnych miesiącach 2011",
        showlegend=False,
        xaxis_title="Miesiące",
        yaxis_title="Koszty",
        yaxis_ticksuffix=" zł",
        template="simple_white",
    )
    fig.show()


def plot_3():
    # line plot
    margin = 10
    fig, ax = plt.subplots(figsize=(12, 6))
    plt.plot(rok, y)
    ymax = max(y) + margin
    plt.ylim(0, ymax)
    plt.yticks(range(0, ymax, 25))
    plt.show()

    # bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.barh(rok, y)
    plt.show()

    # waterfall plot
    y_series = pd.Series(y)
    zmiany = y_series.diff().fillna(y_series)  # type: ignore
    fig = go.Figure(
        go.Waterfall(
            x=rok + ["bilans"],
            y=zmiany + [0],
            measure=["absolute"] + ["relative"] * (len(rok) - 2) + ["total"],
            connector={
                "line": {"color": "rgb(63, 63, 63)", "width": 0.5, "dash": "dot"}
            },
            increasing={"marker": {"color": "lime"}},
            decreasing={"marker": {"color": "magenta"}},
            totals={"marker": {"color": "skyblue"}},
        )
    )

    fig.update_layout(
        title="Wykres kaskadowy (z total) – analiza sprzedaży",
        showlegend=False,
        xaxis_title="Miesiące",
        yaxis_title="Spzredaż",
        yaxis_ticksuffix=" zł",
        template="simple_white",
    )
    fig.show()


# ZADANIE 4 ------------------------------------------


def demo_plot_4():
    print(puchar)
    fig = px.parallel_coordinates(
        puchar,
        color="Kraj",
        dimensions=["Sezon16", "Sezon17", "Sezon18", "Sezon19"],
    )
    fig.show()  # nie dziala (?)

    # podpowiedź fig = go.Figure(data= go.Parcoords(line=?, dimensions=?))


if "__main__" == __name__:
    # plot_1()
    # plot_2()
    # plot_3()
    # demo_plot_3()
    # plot_3()
    demo_plot_4()
