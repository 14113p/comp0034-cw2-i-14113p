# Visualisation 2
# Budget & Revenue in the premiere week

import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dcc
from dash import Output, Input
import datetime as dt


def create_graph2(data, year=0):
    if year != 0:
        data = data[data["API Release Date"].dt.year == year]
    output = px.scatter(
        data,
        x="API Budget",
        y="Weekend Gross",
        size="Number of cinemas",
        size_max=4,
        hover_data=["Film", "Weekend Gross", "API Budget"],
        labels={
            "API Budget": "Budget [USD]",
            "Weekend Gross": "Premiere Week Revenue [USD]",
            "count": "Number of entries",
        },
        template="ggplot2",
        title="Opening week revenue by budget",
        height=600,
    )
    output.update_traces(marker_sizemode="area", selector=dict(type="scatter"))
    output.update_traces(marker_sizeref=1.2, selector=dict(type="scatter"))
    output.update_traces(marker_sizemin=3, selector=dict(type="scatter"))
    output.update_layout(xaxis_type="log")
    output.update_layout(yaxis_type="log")
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


data_page2 = pd.read_excel("../data/BFI_merged.xlsx")
data_page2 = data_page2.loc[data_page2["Weeks on release"] == 1]
data_page2 = data_page2.loc[data_page2["API Budget"] > 30000]  # 3 anomalies in data

graph2 = create_graph2(data_page2)

page2 = dbc.Container(
    [
        dbc.Row(
            dcc.Dropdown(
                id="year-select2",
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
        dbc.Row(dcc.Graph(figure=graph2, id="graph2")),
    ]
)



