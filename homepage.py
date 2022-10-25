from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                # dcc.Link("Home", href="/")
                dbc.NavLink("À propos", href="https://www.donetbenevolat.ca/",external_link=True)
            ),
            dbc.NavItem(
                dbc.NavLink("EN", href="http://app.givingandvolunteering.ca/",external_link=True)
            ),
        ],
        brand="Centre Canadien de Connaissances sur les Dons et le Bénévolat",
        brand_href="/",
        color="#4B161D",
        dark=True,
        sticky='top'
    )

footer = html.Footer(
       dbc.Container(
           dbc.Row(
               html.Div([
                #    html.P('© Imagine Canada 2021',className="text-center"),
                   html.P("Ce site Web a été développé grâce au financement du gouvernement du Canada, par le biais du Programme de partenariats pour le développement social d'Emploi et Développement social Canada.",className="text-center")
               ]
                   ,className='col-md-10 col-lg-8 mx-auto mt-5'
               ),
           )
       )
   )

content = dbc.Container(
    [
        dcc.Location(id='url', refresh=False),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Qui donne aux organismes caritatifs et combien?",className='card-title'), href='/Qui_donne_aux_organismes_caritatifs_et_combien_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("Plus de deux tiers des personnes au Canada donnent de l’argent aux organismes de bienfaisance et à but non lucratif et leur contribution se chiffre approximativement à 11,9 milliards $. Cette analyse montre comment les tendances des dons (probabilité de donner, montants caractéristiques, etc.) varient souvent selon le profil démographique des personnes.",className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
                dcc.Location(id='url', refresh=False),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Comment donne-t-on au Canada?",className='card-title'), href='/Comment_donne_t_on_au_Canada_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("Les personnes donnent de nombreuses façons différentes au Canada. Cette analyse détaille combien de personnes donnent par chaque méthode, le montant qu’elles ont tendance à donner et la variation de leurs méthodes de dons selon leur profil démographique.",className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
                dcc.Location(id='url', refresh=False),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Comprendre les grand.e.s. donateur.trice.s",className='card-title'), href='/Comprendre_les_grands_donateurs_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("Bien qu’approximativement neuf personnes sur dix donnent de l’argent au Canada, plus de quatre cinquièmes de la valeur totale des dons provient des grand.e.s donateur.trice.s (le quart de ces personnes qui donnent les montants les plus importants). Cette analyse porte sur le profil démographique des grand.e.s donateur.trice.s, sur les causes que ces personnes soutiennent, sur leurs motivations et sur les freins qui les empêchent de donner plus.",className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Pourquoi donne-t-on au Canada?",className='card-title'), href='/Pourquoi_donne_t_on_au_Canada_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("Les personnes donnent pour de nombreuses raisons différentes au Canada. Cette analyse révèle les différentes motivations courantes, comment ces motivations varient selon le profil démographique des donateur.trice.s et les liens de celles-ci avec les montants donnés et les causes soutenues.",className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Qu'est-ce qui empeche de donner plus?",className='card-title'), href='/Qu_est_ce_qui_empeche_de_donner_plus_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Bien que les personnes soient généreuses au Canada, plusieurs facteurs peuvent limiter leurs dons et les empêchent de donner plus. Cette analyse identifie les facteurs qui limitent les dons, leur incidence sur les montants donnés, la variation des freins potentiels selon le profil démographique des donateur.trice.s et leurs liens avec certaines causes.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Quels types d'organismes soutient-on au Canada?",className='card-title'), href='/Quels_types_organismes_soutient_on_au_Canada_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Cette analyse mesure les niveaux de soutien selon les causes, le nombre de personnes soutenant chaque cause, les montants caractéristiques des dons et la répartition de la valeur totale des dons.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Qui sont les bénévoles et combien d'heures donnent-ils?" ,className='card-title'), href='/Qui_sont_les_benevoles_et_combien_heures_donnent_ils_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Un peu plus de deux cinquièmes des personnes au Canada font don de 1,7 million d’heures de leur temps aux organismes de bienfaisance et à but non lucratif. Cette analyse montre comment les tendances du bénévolat (probabilité de faire du bénévolat, nombres d’heures de bénévolat caractéristiques, etc.) varient souvent selon le profil démographique des bénévoles.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Quelles sont les activités des bénévoles?",className='card-title'), href='/Quelles_sont_les_activites_des_benevoles_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Le bénévolat prend de nombreuses formes différentes au Canada, de la collecte de fonds à la lutte contre les incendies. Cette analyse détaille les activités des bénévoles et la tendance de leurs activités à varier selon leur profil démographique.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Comprendre les bénévoles très engagé.e.s",className='card-title'), href='/Comprendre_les_benevoles_tres_engages_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Au niveau national, environ quatre cinquièmes des heures de bénévolat sont attribuables aux bénévoles très engagé.e.s (le quart des bénévoles qui donnent le plus d’heures). Cette analyse porte sur le profil démographique des bénévoles très engagé.e.s, sur les causes que ces personnes soutiennent, sur leurs motivations et sur les freins qui les empêchent de faire plus de bénévolat.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Aide d’autrui et amélioration communautaire",className='card-title'), href='/Aide_autrui_et_amelioration_communautaire_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                En plus de faire du bénévolat pour les organismes de bienfaisance et à but non lucratif, les personnes aident aussi directement autrui au Canada (sans faire appel à un organisme) et participent à diverses formes d’améliorations communautaires. Cette analyse identifie les personnes qui pratiquent ces autres formes de soutien, leurs types d’activités et le nombre d’heures dont elles font don habituellement.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Pourquoi fait-on du bénévolat?",className='card-title'), href='/Pourquoi_fait_on_du_benevolat_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Les personnes font du bénévolat pour de nombreuses raisons différentes au Canada. Cette analyse révèle les différentes motivations courantes, leur incidence habituelle sur les niveaux de bénévolat, comment ces motivations varient selon le profil démographique des bénévoles et les liens entre les motivations et le soutien de certaines causes.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Qu’est-ce qui empêche de faire du bénévolat?",className='card-title'), href='/Qu_est_ce_qui_empeche_de_faire_du_benevolat_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Cette analyse porte sur les facteurs qui peuvent limiter les heures de bénévolat au Canada ou même qui empêchent totalement les personnes de faire du bénévolat. Elle décrit l’incidence des divers freins, leur incidence habituelle sur le nombre d’heures de bénévolat, leurs variations selon le profil démographique des bénévoles et les liens entre ces freins et certaines causes.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("À quels types d’organismes fait-on don de son temps au Canada?",className='card-title'), href='/A_quels_types_organismes_fait_on_don_de_son_temps_au_Canada_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Cette analyse est axée sur les causes soutenues par les bénévoles au Canada. Elle mesure l’importance du bassin de bénévoles pour chaque cause, le nombre d’heures de bénévolat caractéristique au bénéfice de chaque cause et la répartition du nombre total d’heures de bénévolat entre les causes.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        html.Hr(),
        html.H2("Giving and Volunteering by Demographic"),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Giving and Volunteering for Health Organizations",className='card-title'), href='/GAV0301'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                # html.P("""
                                # On average, volunteers contributed time to 1.4 causes. Most volunteers contributed time to one cause, just over a quarter to two, and the balance to three.
                                # """,
                                # className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Giving and Volunteering for Religious Organizations",className='card-title'), href='/GAV0302'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                # html.P("""
                                # On average, volunteers contributed time to 1.4 causes. Most volunteers contributed time to one cause, just over a quarter to two, and the balance to three.
                                # """,
                                # className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Giving and Volunteering for Education and Research Organizations",className='card-title'), href='/GAV0303'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                # html.P("""
                                # On average, volunteers contributed time to 1.4 causes. Most volunteers contributed time to one cause, just over a quarter to two, and the balance to three.
                                # """,
                                # className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Giving and Volunteering for Social Services Organizations",className='card-title'), href='/GAV0304'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                # html.P("""
                                # On average, volunteers contributed time to 1.4 causes. Most volunteers contributed time to one cause, just over a quarter to two, and the balance to three.
                                # """,
                                # className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Giving and Volunteering for Arts, Culture and Rec Organizations",className='card-title'), href='/GAV0305'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                # html.P("""
                                # On average, volunteers contributed time to 1.4 causes. Most volunteers contributed time to one cause, just over a quarter to two, and the balance to three.
                                # """,
                                # className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Giving and Volunteering Among New Canadians",className='card-title'), href='/les_dons_et_le_benevolat_des_personnes_nouvellement_arrivees_au_canada_2018'),
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Giving and Volunteering by Seniors",className='card-title'), href='/les_dons_et_le_benevolat_des_personnes_agees_2018'),
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Giving and Volunteering by Youth",className='card-title'), href='/les_dons_et_le_benevolat_des_jeunes_2018'),
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        # html.Hr(),
        html.H2("2013 Data"),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("How Do Canadians Donate? (2013)",className='card-title'), href='/HDC01002_13'),
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Why Do Canadians Give? (2013)",className='card-title'), href='/WDC0105_13'),
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br()
 
    ]
)


layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                [
                    html.Div(
                        html.Div(
                            html.H1("Des données pour propulser l'impact communautaire"),
                            # className='site-heading data-catalyst'
                            className='data-catalyst'
                        ),
                        className="col-md-10 col-lg-8 mx-auto position-relative"
                    ),
                ]
            )
        ), 
    ],
        className='masthead',
        style={'backgroundImage':"url('./assets/portal_image.png')"}
    ),
    content,
    footer
])

