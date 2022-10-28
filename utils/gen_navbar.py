import dash_bootstrap_components as dbc


def gen_navbar(alt_lang_link):
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                dbc.NavLink("About", href="https://www.donetbenevolat.ca/", external_link=True)
            ),
            dbc.NavItem(
                dbc.NavLink("FR", href="http://app.givingandvolunteering.ca/{}".format(alt_lang_link), external_link=True)
            ),

        ],
        brand="Canadian Knowledge Hub for Giving and Volunteering",
        brand_href="/",
        color="#4B161D",
        dark=True,
        sticky='top'
    )

    return navbar
