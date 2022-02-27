# Visualisation 1
# Genres by popularity

import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html

df = pd.read_excel("../data/genres.xlsx")
graph1 = px.histogram(
    df,
    x="API Genres",
    y="API Genres",
    color="API Release Date",
    histfunc="count",
    labels={
        "API Genres": "Genre",
        "y": "Number of movies",
        "API Release Date": "Release Year",
    },
    title="New Releases by genre",
    height=600,
    template="ggplot2",
)
graph1.update_layout(
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
graph1.update_xaxes(categoryorder="total descending")

page1 = dbc.Container(
    [
        dbc.Col(dcc.Graph(figure=graph1)),
        dbc.Col(
            children=[
                html.H5(
                    children=("Total number of movies: " + str(df["Film"].nunique()))
                ),
                html.H5(
                    children=(
                        "Total number of genre entries: "
                        + str(df["API Genres"].count())
                    )
                ),
            ]
        ),
    ]
)
