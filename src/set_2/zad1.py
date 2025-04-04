import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("../../data/insurance.csv")
heatmap = sns.heatmap(
    data.corr(numeric_only=True), annot=True, cmap="coolwarm_r", vmin=-1, vmax=1
)
plt.title("Macierz korelacji zmiennych ilościowych")
plt.show()
