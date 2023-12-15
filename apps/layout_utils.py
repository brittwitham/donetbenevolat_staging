from dash import html
import dash_bootstrap_components as dbc


def gen_home_button(is_french = True, is_2013 = False):
    button_text = "Retour à la page d'accueil" if is_french else "Back to Home"
    button_link = "https://www.donetbenevolat.ca/" if is_french else "https://www.givingandvolunteering.ca/gssgvp-insights"
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


def gen_navbar(alt_lang_suffix="", is_french=True, is_2013=False):
    other_lang_base = "http://app.givingandvolunteering.ca" if is_french else "http://app.donetbenevolat.ca"

    # TODO: Add 2013 suffix for home link too?  
    home_link = "https://www.donetbenevolat.ca"

    other_lang_link = "{}/{}".format(other_lang_base, alt_lang_suffix)

    language = "EN" if is_french else "FR"

    navbar = dbc.Navbar( 
        dbc.Container(
            [           
                html.A(
                    html.Img(src="/assets/centre+logo.jpg", alt="Don et Benevolat logo"),
                    href=home_link
                ),
                html.Div(
                    [
                        dbc.NavItem(
                            dbc.NavLink(language, href=other_lang_link, external_link=True, className="header-link")
                        ),
                    ], 
                    className="d-flex py-2"
                )
            ], 
            className="d-flex justify-content-between"
        ),
        color="white",  # c7102e
        sticky='top',
        className="header"
    )

    return navbar

footer = html.Footer(
    dbc.Container(
        dbc.Row(
            html.Div(
                html.P("Ce site Web a été développé grâce au financement du gouvernement du Canada, par le biais du Programme de partenariats pour le développement social d'Emploi et Développement social Canada.",className="text-center"),
                className='col-12 mx-auto'
            ),
        )
    )
, className='footer')