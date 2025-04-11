import plotly.express as px
import pandas as pd


# dokończyć legendę

sprzedaz = pd.DataFrame(
    {
        "Miasto": ["Katowice", "Kraków", "Wrocław"],
        "Desktop": [2, 7, 3],
        "Laptop": [12, 7, 13],
    }
)
fig = px.bar(
    data_frame=sprzedaz,
    x="Miasto",
    y=["Desktop", "Laptop"],
    labels={"Miasto": "Miasto", "value": "Sprzedaż (w tyś.)", "variable": "Produkty"},
    barmode="group",
    template="ygridoff",
    title="<span>Sprzedaż produktów w miastach</span>",
)
fig.update_layout(font=dict(size=16, color="darkgreen", family="monospace"))


fig.show()
