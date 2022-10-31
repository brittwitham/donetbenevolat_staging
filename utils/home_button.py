from dash import html
import dash_bootstrap_components as dbc


def gen_home_button():
    home_button = dbc.Row(
        dbc.Col(
            html.Div(
                html.A(dbc.Button("Accueil", color="secondary", className="me-1"),
                       href="http://app.donetbenevolat.ca/"),
            ), className="text-center bg-secondary"
        )
    )

    return home_button
