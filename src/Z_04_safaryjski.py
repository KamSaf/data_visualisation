import plotly.express as px
import pandas as pd

TICKS_INTERVAL = 2

sprzedaz = pd.DataFrame(
    {
        "Miasto": ["Katowice", "Kraków", "Wrocław"],
        "Desktop": [2, 7, 3],
        "Laptop": [12, 7, 13],
    }
)

sprzedaz_waska = pd.melt(
    sprzedaz, id_vars=["Miasto"], value_name="Sprzedaż", var_name="Produkt"
)

fig = px.bar(
    sprzedaz_waska,
    x="Miasto",
    y="Sprzedaż",
    color="Produkt",
    template="gridon",
    title="<span>Rozkład sprzedaży produktów w miastach</span>",
)
ticks = [*range(0, 16, TICKS_INTERVAL)]
fig.update_layout(yaxis=dict(tickvals=ticks))


fig.show()
