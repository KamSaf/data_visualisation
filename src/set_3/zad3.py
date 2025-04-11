import plotly.express as px
import pandas as pd


sprzedaz = pd.DataFrame(
    {
        "Miasto": ["Katowice", "Kraków", "Wrocław"],
        "Desktop": [2, 7, 3],
        "Laptop": [12, 7, 13],
    }
)

sprzedaz_waska = pd.melt(
    sprzedaz, id_vars="Miasto", value_name="Sprzedaż", var_name="Produkt"
)

print(sprzedaz_waska)
fig = px.bar(
    sprzedaz_waska,
    x="Produkt",
    y="Sprzedaż",
    color="Miasto",
    template="gridon",
    title="<span>Rozkład sprzedaży produktów w miastach</span>",
)
wart = [*range(0, 40, 10)]
tekst = [f"{w}k" for w in wart]
fig.update_layout(yaxis=dict(tickvals=["0", "10", "20", "30"], ticktext=tekst))


fig.show()
