import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ATTR_LABELS = {"age": "Wiek", "bmi": "BMI", "children": "Liczba dzieci"}


def histplot(data: pd.DataFrame, attr: str) -> None:
    sns.histplot(data=data, x=attr, kde=False, stat="density", bins=12)
    plt.title(f"Rozklad zmiennej {ATTR_LABELS[attr]} (histogram)")
    plt.show()


def kde(data: pd.DataFrame, attr: str) -> None:
    sns.kdeplot(data=data, x=attr, color="crimson")
    plt.title(f"Rozklad zmiennej {ATTR_LABELS[attr]} (KDE)")
    plt.show()


def reg_plot(data: pd.DataFrame, attr: str) -> None:
    g = sns.lmplot(x=attr, y="charges", data=data, line_kws={"color": "red"})
    g.set_axis_labels(f"{ATTR_LABELS[attr]} ({attr})", "Koszty leczenia (charges)")
    plt.title(f"Regresja: {ATTR_LABELS[attr]} a koszty leczenia")
    plt.show()


data = pd.read_csv("../../data/insurance.csv")
for attr in ("age", "bmi", "children"):
    histplot(data, attr)
    kde(data, attr)
    reg_plot(data, attr)
