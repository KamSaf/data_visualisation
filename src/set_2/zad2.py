import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def histplot(data: pd.DataFrame) -> None:
    sns.histplot(data=data, x="charges", kde=False, stat="density", bins=12)
    plt.title("Rozklad zmiennej objaśnianej: charges (histogram)")
    plt.show()


def kde(data: pd.DataFrame) -> None:
    sns.kdeplot(data=data, x="charges", color="crimson")
    plt.title("Rozklad zmiennej objaśnianej: charges (kde)")
    plt.show()


data = pd.read_csv("../../data/insurance.csv")
histplot(data)
kde(data)
