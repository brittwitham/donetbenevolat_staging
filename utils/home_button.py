from dash import html
import dash_bootstrap_components as dbc


def gen_home_button(is_french = True, is_2013 = False):
    button_text = "Retour à la page d'accueil" if is_french else "Back to Home"
     # TODO: Reenable french site when it's live
    # button_link = "https://www.donetbenevolat.ca/" if is_french else "https://www.givingandvolunteering.ca/gssgvp-insights"
    button_link="https://www.givingandvolunteering.ca/gssgvp-insights"

   
    button_link_with_year = button_link + "-2013" if is_2013 else button_link

    home_button = dbc.Row(
        dbc.Col(
            html.Div(
                html.A(
                    dbc.Button(button_text, color="secondary", className="main-button me-1 text-white"),
                    href=button_link_with_year),
            ), 
            className="main-button-container text-center"
        )
    )

    return home_button