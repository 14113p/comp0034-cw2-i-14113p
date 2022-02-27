# Visualisation 3
# Viewership over time

import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dcc
from dash import Output, Input
import pandas as pd


def create_graph3(data, year=0):
    if year != 0:
        data = data[data["API Release Date"].dt.year == year]
    output = px.line(
        data,
        x="Weeks on release",
        y="Site average",
        color="Film",
        labels={},
        title="Viewership over time",
        markers=True,
        log_y=True,
        height=700,
        template="ggplot2",
    )
    output.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=False,
            showticklabels=True,
            linecolor="rgb(204, 204, 204)",
            linewidth=2,
            ticks="outside",
            tickfont=dict(
                family="Arial",
                size=12,
                color="rgb(82, 82, 82)",
            ),
        )
    )
    return output


data_page3 = pd.read_excel(
    "../data/BFI_Merged.xlsx",
    usecols=["Film", "Weeks on release", "Site average", "API Release Date"],
)
data_page3 = data_page3[data_page3["Weeks on release"] < 35]
data_page3 = data_page3[data_page3.groupby("Film")["Film"].transform("size") > 10]
data_page3 = data_page3.reset_index()
data_page3.drop_duplicates(subset=["Film", "Weeks on release"])
data_page3 = data_page3.sort_values(by=["Film", "Weeks on release"], axis=0, ascending=[1, 1])

graph3 = create_graph3(data_page3, 0)

page3 = dbc.Container(
    [
        dbc.Row(
            dcc.Dropdown(
                id="year-select3",
                options=[
                    {"label": "All years", "value": 0},
                    {"label": "2017", "value": 2017},
                    {"label": "2018", "value": 2018},
                    {"label": "2019", "value": 2019},
                    {"label": "2020", "value": 2020},
                    {"label": "2021", "value": 2021},
                ],
                value=0,
            )
        ),
        dcc.Graph(figure=graph3, id="graph3"),
    ]
)


