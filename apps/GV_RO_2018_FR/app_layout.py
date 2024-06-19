# App layout file for GV_RO_2018_FR converted from GAV0302_fr.py

from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app
from ..layout_utils import gen_home_button, gen_navbar, footer
from .callbacks import register_callbacks
from .data_processing import *

register_callbacks(app)
marginTop = 20
home_button = gen_home_button()
navbar = gen_navbar("giving_and_volunteering_for_religious_organizations_2018")

layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1(
                            ('Dons et bénévolat pour les organismes religieux').capitalize()),
                        # html.Span(
                        #     'David Lasby',
                        #     className='meta'
                        # )
                    ],
                        className='post-heading'
                    ),
                    className='col-md-10 col-lg-8 mx-auto position-relative'
                )
            )
        ),
    ],
        # className='masthead'
        className="sub-header bg-secondary text-white text-center pt-5",
    ),
    # Note: filters put in separate container to make floating element later
    dbc.Container([
        home_button,
        dbc.Row(
            dbc.Col(
                html.Div([
                    "Sélectionnez une région:",
                    dcc.Dropdown(
                        id='region-selection',
                        options=[{'label': region_values[i], 'value': region_values[i]}
                                 for i in range(len(region_values))],
                        value='CA',
                    ),
                    html.Br(),
                ], className="m-2 p-2"),
            ), id='sticky-dropdown'),
    ], className='sticky-top select-region mb-2', fluid=True),
    dbc.Container([
        dbc.Row([
            html.Div([
                # html.H3('Giving'),
                dcc.Markdown("""
                    En plus de mesurer l’importance générale des dons et du bénévolat à divers niveaux, l’Enquête sociale générale sur les dons, le bénévolat et la participation mesure l’importance des niveaux de soutien pour 15 types de causes (appelées communément « domaines d’activité »), dont la religion. Ces organismes sont axés principalement sur la pratique des rituels religieux et la promotion des croyances religieuses. Ce sont des congrégations individuelles (c.-à-d. mosquées, églises, synagogues, temples, etc. uniques), des associations de congrégations et des organismes axés sur une éducation religieuse particulière, comme les séminaires.
                    """),
                dcc.Markdown("""
                    Nous analysons ci-dessous les tendances des dons et du bénévolat au bénéfice de ces organismes. Nous décrivons dans le texte ci-dessous les résultats au niveau national et, pour obtenir des précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer des résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.
                    """),
                html.H4('Montants des dons'),
                dcc.Markdown("""
                    À l’échelle nationale, une personne sur quatre au Canada a fait au moins un don à un organisme religieux pendant la période d’une année qui a précédé l’Enquête, ce qui place la religion au troisième rang des causes les plus soutenues au Canada. Le classement des organismes religieux sur le plan des montants donnés était largement supérieur, en représentant près de la moitié de la valeur totale (46 %) des dons, plus que toutes les autres causes. Quant au montant moyen des dons, les donateur.trice.s aux organismes religieux donnaient des montants très supérieurs aux montants des dons au bénéfice des autres causes, ce qui en fait, et de loin, les partisan.e.s les plus engagé.e.s.
                    """),
                # Donation rate and average donation amount by cause
                dcc.Graph(id='DonRateAvgDon2', style={'marginTop': marginTop}),
            ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H4('Qui donne de l’argent'),
                    dcc.Markdown("""
                    Certaines personnes sont plus enclines que d’autres à donner aux organismes religieux. À l’échelle nationale, la probabilité de donner à ces organismes augmente de manière significative avec l’assiduité aux offices religieux et avec l’âge. Les autres groupes plus enclins à donner aux organismes religieux sont les femmes, les veuves et les veufs, les personnes non membres de la population active, celles titulaires d’un diplôme universitaire et celles qui sont nouvellement arrivées au Canada.
                    """
                                 ),
                    html.Div([
                        html.Div(['Sélectionnez un catégorie démographique:',
                                 dcc.Dropdown(
                                     id='demo-selection-don',
                                     options=[{'label': demo_names[i], 'value': demo_names[i]}
                                              for i in range(len(demo_names))],
                                     value='Groupe d\'âge',
                                     style={'verticalAlign': 'middle'}
                                 ), ],
                                 style={'width': '33%', 'display': 'inline-block'})
                    ]),
                    # Donation rate by key demographic characteristics
                    dcc.Graph(
                        id="ReligionDonRateDemo_fr", style={
                            'marginTop': marginTop})
                ],
                className='col-md-10 col-lg-8 mx-auto'),
            # html.Div([
            #     html.H4('Support for Other Organization Types'),
            #     # Rates of donating to other causes
            #     dcc.Graph(id='HealthDonsCauses-2', style={'marginTop': marginTop}),
            #     ], className='col-md-10 col-lg-8 mx-auto'
            # ),
            html.Div([
                html.H4('Méthodes de dons'),
                dcc.Markdown("""
                    On a demandé aux répondant.e.s à l’Enquête si l’un ou plusieurs de 13 types de sollicitations différents les conduisaient à donner. Bien que l’Enquête ne lie pas directement ces méthodes aux causes soutenues, la comparaison entre les donateur.trice.s au bénéfice des organismes religieux et les autres (c.-à-d. les personnes qui ne soutenaient que d’autres causes) permet de comprendre comment les personnes ont tendance à soutenir financièrement cette catégorie d’organismes. À l’échelle nationale, comme on pouvait s’y attendre, ces personnes sont largement plus susceptibles de donner dans un lieu de culte, mais aussi plus susceptibles de donner en mémoire de quelqu’un, de leur propre initiative et en réponse à une sollicitation par courrier. Elles sont également moins susceptibles que les autres donateur.trice.s de donner en réponse à une sollicitation en ligne, dans un lieu public ou de toute autre façon non mentionnée expressément dans le questionnaire de l’Enquête.
                    """),
                # Donation rate by method
                dcc.Graph(
                    id='ReligionDonsMeth', style={
                        'marginTop': marginTop}),
            ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Motivations des dons'),
                dcc.Markdown("""
                    On a demandé aux répondant.e.s à l’Enquête si huit facteurs potentiels jouaient un rôle important dans leurs décisions de donner. Là encore, bien qu’il n’existe aucun lien direct entre les motivations et les causes soutenues, la comparaison des personnes qui donnent aux organismes religieux et de celles qui donnent aux autres organismes permet de comprendre les raisons de leur soutien des organismes religieux. Comme on pouvait s’y attendre, les personnes qui donnent aux organismes religieux sont beaucoup plus enclines à donner en raison de leurs croyances religieuses et spirituelles. De plus, elles ont relativement tendance à donner pour contribuer à la collectivité et parce qu’elles reçoivent des crédits d’impôt en échange de leurs dons.
                    """),
                # Barriers to donating more
                # dcc.Graph(id='ReligionMotivations', style={'marginTop': marginTop}),
                dcc.Graph(
                    id='ReligionMotivations', style={
                        'marginTop': marginTop}),
            ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Freins aux dons'),
                html.P("""
                    Afin de mieux comprendre les facteurs qui peuvent dissuader de donner, on a demandé aux donateur.trice.s si dix freins potentiels les empêchent de donner plus. À l’échelle nationale, les personnes qui donnent aux organismes religieux ont beaucoup plus tendance que celles qui donnent aux autres organismes à donner directement aux personnes dans le besoin au lieu de donner plus à un organisme et à faire du bénévolat de préférence à des dons d’argent. Tous les autres freins ont grosso modo une incidence comparable sur les personnes qui donnent aux organismes religieux et sur celles qui qui donnent aux autres types d’organismes.
                    """
                       ),
                # Barriers to donating more
                dcc.Graph(
                    id='ReligionBarriers', style={
                        'marginTop': marginTop}),
            ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
        dbc.Row([
            html.Div([
                html.H4("Niveaux de bénévolat"),
                html.P("""
                        À l’échelle nationale, environ une personne sur 12 (8 %) au Canada a fait du bénévolat pour un organisme religieux pendant l’année qui a précédé l’Enquête. Par comparaison avec les autres organismes, les organismes religieux disposent de la cinquième base de bénévoles par ordre d’importance, derrière le secteur des arts et loisirs (12 %), des services sociaux, de l’éducation et de la recherche (9 %), et de la santé (9 %). Comme les bénévoles des organismes religieux ont tendance à faire don d’un nombre d’heures de leur temps relativement élevé, les organismes religieux représentent la troisième proportion des heures de bénévolat par ordre d’importance (16 %), après les organismes des secteurs des arts et loisirs (23 %) et des services sociaux (18 %), et avant ceux des secteurs de l’éducation et de la recherche, et de la santé (9 % chacun).
                        """),
                # Volunteer rate and average hours volunteered by cause
                dcc.Graph(id='VolRateAvgHrs2', style={'marginTop': marginTop}),
            ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4("Qui fait du bénévolat"),
                html.P("""
                        À l’échelle nationale, la probabilité de faire du bénévolat pour un organisme religieux augmente avec l’assiduité aux offices religieux et avec l’âge (chez les personnes âgées de 25 ans ou plus). Dans un sens très large, les associations entre le profil démographique et le bénévolat sont très semblables à ces associations avec les dons, bien qu’elles ne soient pas aussi nettes.
                        """),
                html.Div([
                    html.Div(['Sélectionnez un catégorie démographique:',
                             dcc.Dropdown(
                                 id='demo-selection-vol',
                                 options=[{'label': demo_names[i], 'value': demo_names[i]}
                                          for i in range(len(demo_names))],
                                 value='Groupe d\'âge',
                                 style={'verticalAlign': 'middle'}
                             ), ],
                             style={'width': '33%', 'display': 'inline-block'})
                ]),
                # Volunteer rate by key demographic characteristics
                dcc.Graph(
                    id="ReligionVolRateDemo_fr", style={
                        'marginTop': marginTop})
            ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # html.Div([
            #     html.H4('Support for other organization types'),
            #     # Rates of volunteering for other causes
            #     dcc.Graph(id='HealthHrsCauses-2', style={'marginTop': marginTop}),
            #     ], className='col-md-10 col-lg-8 mx-auto'
            # ),
            html.Div([
                html.H4("Activités des bénévoles"),
                html.P("""
                        On a demandé aux personnes si, parmi 14 types d’activité différents, elles participaient à 1 ou plusieurs d’entre elles pour un organisme. Bien que l’Enquête ne lie pas précisément les activités aux types d’organismes soutenus, la comparaison des bénévoles des organismes religieux et des bénévoles des autres organismes permet de comprendre les activités des bénévoles pour cette catégorie d’organismes. À l’échelle nationale, les bénévoles des organismes religieux sont relativement susceptibles de participer à de nombreuses activités, plus particulièrement collecter et livrer des marchandises ou collecter de la nourriture et servir des repas, enseigner ou mentorer, réparer, entretenir ou construire des installations et conduire. Ces bénévoles sont relativement moins susceptibles d’entraîner, d’enseigner ou d’arbitrer dans le cadre sportif et de participer à des activités de protection de l’environnement.
                        """),
                # Volunteer rate by activity
                dcc.Graph(
                    id='ReligionVolActivity', style={
                        'marginTop': marginTop}),
            ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4("Motivations du bénévolat"),
                html.P("""
                        On a demandé aux répondant.e.s si douze facteurs potentiels jouaient un rôle important dans leur décision de faire don de leur temps. Contrairement à de nombreux autres domaines de l’Enquête, ces motivations sont liées précisément au bénévolat au bénéfice de causes particulières. À l’échelle nationale, les différences les plus importantes qui distinguent les bénévoles des organismes religieux sont liées au rôle beaucoup plus important de leurs motivations religieuses ou spirituelles. De plus, ces personnes sont légèrement plus enclines à faire du bénévolat parce qu’un membre de leur famille ou des amis sont des bénévoles et parce qu’elles sont touchées personnellement par la cause. Elles ont légèrement moins tendance à chercher à améliorer leurs possibilités d’emploi en faisant du bénévolat ou à soutenir une cause politique ou sociale.
                        """),
                # Motivations for volunteering
                dcc.Graph(
                    id='ReligionVolMotivations', style={
                        'marginTop': marginTop}),
            ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4("Freins au bénévolat"),
                html.P("""
                        On a demandé aux bénévoles si douze freins potentiels les avaient empêchés de faire don de plus de temps pendant l’année précédente. Bien que les freins ne soient pas liés directement aux causes soutenues, la comparaison des bénévoles des organismes religieux et des personnes qui font don de leur temps aux autres organismes apporte une information importante sur les facteurs qui peuvent importer particulièrement aux bénévoles de cette catégorie d’organismes. À l’échelle nationale, les bénévoles des organismes religieux ont légèrement plus tendance à limiter leur bénévolat en raison de problèmes de santé ou de limitations physiques. Ces personnes sont moins susceptibles de penser que les activités bénévoles qu’on demande d’elles ne sont pas suffisamment importantes ou de ne pas avoir été sollicitées pour en faire plus. La majorité des autres différences ne sont pas individuellement significatives, bien qu’il importe de signaler que les bénévoles des organismes religieux signalent plutôt moins souvent la plupart des freins potentiels.
                        """),
                # Barriers to volunteering more
                dcc.Graph(
                    id='ReligionVolBarriers', style={
                        'marginTop': marginTop}),
            ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
    ]),
    footer
])
