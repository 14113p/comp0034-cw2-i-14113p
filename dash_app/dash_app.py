import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
import dash
from dash.dependencies import Input, Output

from dash_app.homepage import homepage
from dash_app.page1 import page1
from dash_app.page2 import page2, create_graph2
from dash_app.page3 import page3, create_graph3

from flask import url_for, request


def init_dashboard(flask_app):
    dash_app = dash.Dash(server=flask_app,
                         routes_pathname_prefix="/dash_app/",
                         suppress_callback_exceptions=True,
                         external_stylesheets=[dbc.themes.FLATLY],
                         )
    dash_app.layout = html.Div(
        [
            dcc.Location(id="url", refresh=False),
            dbc.Navbar(
                dbc.Container(
                    [
                        dbc.Collapse(
                            dbc.Nav([
                                dbc.Button("Back", href='/home'),
                                dbc.DropdownMenu(
                                    children=[
                                        dbc.DropdownMenuItem("Home", href="/home"),
                                        dbc.DropdownMenuItem("Genres", href="/vis1"),
                                        dbc.DropdownMenuItem(
                                            "Budget & Profits", href="/vis2"
                                        ),
                                        dbc.DropdownMenuItem("Viewership", href="/vis3"),
                                    ],
                                    label="Pages",
                                ),],
                                navbar=True,
                            ),
                            navbar=True,
                        ),
                    ]
                ),
                color="dark",
                className="mb-4",
            ),
            html.Div(id="content"),
        ]
    )

    init_callbacks(dash_app)

    return dash_app.server

from dash_app.page3 import data_page3
from dash_app.page2 import data_page2

def init_callbacks(dash_app):
    @dash_app.callback(Output("content", "children"), [Input("url", "pathname")])
    def display_page(pathname):
        if pathname == "/vis1":
            return page1
        elif pathname == "/vis2":
            return page2
        elif pathname == "/vis3":
            return page3
        else:
            return homepage

    @dash_app.callback(Output("graph2", "figure"), [Input("year-select2", "value")])
    def update_graph2(year_select3):
        return create_graph2(data_page2, year_select3)
        
    @dash_app.callback(Output("graph3", "figure"), [Input("year-select3", "value")])
    def update_graph3(year_select3):
        return create_graph3(data_page3, year_select3)

    

