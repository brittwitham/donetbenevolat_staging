import dash_bootstrap_components as dbc
from dash import html

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
                    html.Img(src="/assets/centre+logo.png", alt="Don et Benevolat logo"),
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
