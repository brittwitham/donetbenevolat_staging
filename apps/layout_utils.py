from dash import html
import dash_bootstrap_components as dbc


def gen_home_button(is_2013 = False, sat_link= False, bc_link=False):
    button_text = "Retour à la page d'accueil"
    # button_text = "Retour à la page d'accueil" if is_french else "Back to Home"

    # if is_french:
    #     button_link = "https://www.donetbenevolat.ca/"
    if sat_link: 
        button_link = "https://donetbenevolat.ca/apercu-des-donnees-sur-les-comptes-satellites/"
    elif bc_link:
        button_link = "https://donetbenevolat.ca/apercu-des-donnees-sur-la-situation-des-entreprises/"
    else:
        # button_link = "https://www.donetbenevolat.ca/"
        button_link = "https://donetbenevolat.ca/apercu-de-lesgvp"

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
    # home_link = "https://www.donetbenevolat.ca"
    home_link = "https://donetbenevolat.ca/apercu-du-gssgvp/"

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

# footer = html.Footer(
#     dbc.Container(
#         dbc.Row(
#             html.Div(
#                 html.P("Ce site Web a été développé grâce au financement du gouvernement du Canada, par le biais du Programme de partenariats pour le développement social d'Emploi et Développement social Canada.",className="text-center"),
#                 className='col-12 mx-auto'
#             ),
#         )
#     )
# , className='footer')

footer = html.Footer([
    html.Div([
       html.H1(["Centre canadien de connaissances", html.Br(), "sur les dons et le bénévolat"], className="footer-h1-text"),
       html.Span("Si vous avez d’autres commentaires pour nous aider à développer le\nCarrefour, communiquez avec Bénévoles Canada à l’adresse suivante ", className="footer-span-text"),
       html.A('datadriven@volunteer.ca.', href='datadriven@volunteer.ca', className="footer-email"),
    ], style={'width':'100%'}),
    html.Div([html.Img(src="/assets/footer-logo-fr.png", style={'height':'auto', 'width':'75%', 'float':'right'})]),
    html.Hr(),
], style={'padding': '30px'}, 
                     className='footer')