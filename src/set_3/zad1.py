import plotly.express as px
import pandas as pd


quiz = pd.DataFrame({"Odpowiedź": ["Tak", "Nie"], "Wartość": [4532, 2497]})
fig = px.pie(
    data_frame=quiz,
    names="Odpowiedź",
    values="Wartość",
    title="<span>Rozklad odpowiedzi z quizu</span>",
    color="Odpowiedź",
    color_discrete_sequence=["#6b8e23", "#b22222"],
)
fig.update_traces(
    textposition="inside",
    textinfo="label",
    textfont_size=25,
    marker={"line": {"color": "white", "width": 3}},
)
fig.update_layout(showlegend=False)


fig.show()
