# Homepage

import dash_bootstrap_components as dbc
from dash import html

homepage = html.Div(
    children=[
        dbc.Container(
            children=[
                dbc.Col(
                    [
                        html.H3(
                            children=[
                                "Dataset: UK-screened movies alongside details and box office information",
                                html.Br(),
                                "Number of entries: 4216",
                                html.Br(),
                                "Number of unique movies: 1089",
                                html.Br(),
                                "Release Dates: 2017-2021",
                            ]
                        )
                    ]
                )
            ]
        )
    ]
)
