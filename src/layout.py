from dash import Dash, html
import dash_bootstrap_components as dbc
from data.schemas.layout_schema import LayoutSchema
from data.schemas import ids
from data.schemas.df_schema import TableSchema
from src.components import chart_area_selection, chart, table_date_selection, tables


def create_layout(app: Dash):
    return dbc.Container([
        html.Br(),

        # Header
        dbc.Row(
            [
                dbc.Col(
                    html.Div(app.title),
                    width={"size": 10},
                    style={"font-size": LayoutSchema.HEADER1_SIZE,
                           "font-weight": "bold",
                           "color": LayoutSchema.HEADER1_COLOR}
                ),
                dbc.Col(
                    html.Div("EUR|USD"),
                    style={"font-size": 15,
                           "color": LayoutSchema.HEADER1_COLOR},
                    width={"size": 1}
                ),
                dbc.Col(
                    html.Div("Export"),
                    style={"font-size": 15,
                           "color": LayoutSchema.HEADER1_COLOR},
                    width={"size": 1}
                )
            ],
            align="center",
            style={"backgroundColor": LayoutSchema.HEADER1_BG}
        ),

        html.Br(),
        html.Br(),

        # Table
        dbc.Row(
            [
                dbc.Col(
                    html.Div("Returns"),
                    width={"size": 10},
                ),
                dbc.Col(
                    html.Div(className="table-date-container", children=[table_date_selection.render(app)]),
                    width={"size": 2, "order": "last"}
                )
            ],
            align="center",
            style={"backgroundColor": LayoutSchema.HEADER2_BG,
                   "font-size": LayoutSchema.HEADER2_SIZE,
                   "font-weight": "bold",
                   "color": LayoutSchema.HEADER1_COLOR}
        ),

        html.Br(),

        dbc.Row(
            [
                dbc.Col(
                    tables.render(app),
                    width={"size": 6})
            ],
            align="center"
        ),

        html.Br(),
        html.Br(),

        # Chart
        dbc.Row(
            [
                dbc.Col(
                    html.Div("YTD chart"))
            ],
            align="center",
            style={"backgroundColor": LayoutSchema.HEADER2_BG,
                   "font-size": LayoutSchema.HEADER2_SIZE,
                   "font-weight": "bold",
                   "color": LayoutSchema.HEADER1_COLOR}
        ),

        dbc.Row(
            [
                dbc.Col(
                    chart.render(app))
            ],
            align="center"
        ),

        html.Br(),

        # Area selection
        dbc.Row(
            [
                dbc.Col(
                    html.Div(className="checklist-container", children=[chart_area_selection.render(app)]))
            ],
            align="center"
        ),

        html.Br()
    ])

    # return html.Div(
    #     className="ap-div",
    #     children=[
    #         html.H1(app.title),
    #         html.Hr(),
    #         html.Div(className="table-date-container", children=[table_date_selection.render(app)]),
    #         tables.render(app),
    #         chart.render(app),
    #         html.Div(className="checklist-container", children=[chart_area_selection.render(app)])
    #     ]
    # )
