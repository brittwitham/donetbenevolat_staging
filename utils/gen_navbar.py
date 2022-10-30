import dash_bootstrap_components as dbc


def gen_navbar(alt_lang_link):
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                dbc.NavLink("About", href="https://www.givingandvolunteering.ca/", external_link=True)
            ),
            dbc.NavItem(
                dbc.NavLink("FR", href="http://app.donetbenevolat.ca/{}".format(alt_lang_link), external_link=True)
            ),

        ],
        brand="Canadian Knowledge Hub for Giving and Volunteering",
        brand_href="/",
        color="#4B161D",  # c7102e
        dark=True,
        sticky='top'
    )

    return navbar
