# App layout file for WDVD_2018_FR converted from Quelles_sont_les_activites_des_benevoles_2018.py

from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app
from ..layout_utils import gen_home_button, gen_navbar, footer
from .callbacks import register_callbacks
from .data_processing import *

register_callbacks(app)

from utils.gen_navbar import gen_navbar
navbar = gen_navbar("What_do_volunteers_do_2018")

home_button = gen_home_button()
marginTop = 20

layout = html.Div([
    navbar,
    html.Header([
            html.Div(className='overlay'),
            dbc.Container(
                dbc.Row(
                    html.Div(
                        html.Div([
                            html.H1('Quelles sont les activités des bénévoles?'),
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
        ], className="sub-header bg-secondary text-white text-center pt-5",
    ),
    dbc.Container([
        home_button,
        # dbc.Row([
        #     dbc.Col(
        #        html.Div([
        #            "Sélectionnez une région:",
        #            dcc.Dropdown(
        #                id='region-selection',
        #                options=[{'label': region_values[i], 'value': region_values[i]} for i in range(len(region_values))],
        #                value='CA',
        #                ),
        #             html.Br(),
        #         ],className="m-2 p-2"),
        #     ),
        #     dbc.Col(
        #        html.Div([
        #         "Choisissez une activité bénévole: ",
        #         dcc.Dropdown(id='activity-selection',
        #             options=[{'label': i, 'value': i} for i in activity_names],
        #             value="Porte-à-porte")
        #         ],className="m-2 p-2"),
        #     )],
        #     id='sticky-dropdown'),
        html.Div([
            dbc.Row([
            dbc.Col(
                html.Div(["Sélectionnez une région:",
                           dcc.Dropdown(
                               id='region-selection',
                               options=[{'label': region_values[i], 'value': region_values[i]} for i in range(len(region_values))],
                               value='CA',
                               ),
                            html.Br(),
                        ],className="m-2 p-2"), className='col'
                ),
            dbc.Col([
                html.Div(["Choisissez une activité bénévole: ",
                        dcc.Dropdown(id='activity-selection',
                            options=[{'label': i, 'value': i} for i in activity_names],
                            value="Porte-à-porte")
                        ],className="m-2 p-2"),
            ])
        ],
        )
            ], className='col-md-10 col-lg-8 mx-auto'),
    ], className='sticky-top select-region mb-2', fluid=True),

   dbc.Container(
       dbc.Row([
            # Starting text
            html.Div([
                    dcc.Markdown("""
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, un peu plus de deux personnes sur cinq (41 %) au Canada ont fait du bénévolat pour un organisme de bienfaisance ou à but non lucratif pendant la période d’un an qui l’a précédée. En moyenne, ces bénévoles ont fait don de 131 heures chacun, soit un peu moins de 1,7 milliard d’heures par année. Pour obtenir de plus amples renseignements sur les variations du bénévolat selon les provinces et les caractéristiques personnelles, veuillez vous reporter à Qui sont les bénévoles et combien d’heures donnent-ils?, également sur ce site.
                    """),
                    dcc.Markdown("""
                    Les bénévoles accomplissent un large éventail de tâches, allant de la collecte de fonds à la lutte contre les incendies. Nous analysons ci-dessous à quelles tâches les bénévoles consacrent leur temps et leur tendance à se livrer à certaines activités, selon leurs caractéristiques personnelles et économiques. Nous décrivons dans le texte les résultats au niveau national, mais, pour obtenir des précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer des résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.
                    """),
                    dcc.Markdown("""
                    Dans l’ensemble, au Canada, les bénévoles organisent le plus fréquemment des activités ou des événements ou collectent des fonds pour un organisme. À l’extrémité inférieure de l’éventail des heures de bénévolat, moins d’une personne sur vingt fait du porte-à-porte pour un organisme (c.-à-d. sensibilise à une question ou à un organisme sans chercher à collecter des fonds) ou participe à des services de premiers soins et de lutte contre les incendies. Les bénévoles ont tendance à consacrer plus de temps à certaines activités qu’à d’autres. Par exemple, bien que la collecte de fonds soit très répandue, ils ont tendance à y consacrer très peu d’heures. À l’échelle nationale, les types d’activités pour lesquelles les heures de bénévolat sont habituellement les plus nombreuses sont les fonctions d’entraîneur.euse, d’arbitre et de président.e de cérémonie, l’enseignement ou le mentorat, et les soins ou les soutiens en matière de santé.
                                 """),
                    # Volunteer rate & average hours contributed by activity
                    dcc.Graph(id='ActivitiesVolRateAvgHrs', style={'marginTop': 20}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Key personal & economic characteristics
            html.Div(
                [
                    html.H3('Caractéristiques personnelles et économiques'),
                    html.P("""
                    Les activités des bénévoles au Canada ont tendance à varier selon leurs caractéristiques personnelles et économiques. Nous analysons ci-dessous comment la probabilité de faire du bénévolat varie, pour chaque type d’activité, selon les caractéristiques personnelles et économiques clés des bénévoles. Là encore, nous présentons dans le texte les tendances générales au niveau national, mais vous pourrez utiliser le menu déroulant lié aux visualisations de données pour passer en revue les résultats au niveau régional.
                    """),
                    # Gender
                    html.Div([
                        html.H4("Genre"),
                        html.P("""
                        À l’échelle nationale, les femmes ont plus tendance que les hommes à prendre part à la majorité des activités bénévoles, principalement organiser, superviser ou coordonner des événements, collecter des fonds ou siéger à un comité ou à un conseil d’administration. Les hommes sont plus enclins à participer à quelques activités bénévoles, notamment à titre d’entraîneurs, d’arbitres ou de présidents de cérémonie ou à participer à l’entretien, à la réparation ou à la construction d’installations ou aux services de premiers soins, de lutte contre les incendies ou aux opérations de recherche et de sauvetage.
                        """),
                        # Donation rate & average donation amount by gender
                        dcc.Graph(id='ActivityVolRate-Gndr', style={'marginTop': marginTop}),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("""
                        Les bénévoles de moins de 25 ans sont particulièrement enclins à faire don de leur temps pour organiser, superviser ou coordonner des événements et pour des activités d’enseignement ou de mentorat. Les bénévoles plus âgés sont relativement moins susceptibles de participer à la majorité des activités bénévoles, à l’exception des soins ou du soutien en matière de santé. Les personnes des groupes d’âge moyens, de 35 à 64 ans, ont relativement tendance à organiser ou à superviser des événements et à siéger à des comités ou à des conseils d’administration. La probabilité d’exercer les fonctions d’entraîneur.euse et d’arbitre et, dans une certaine mesure, des activités d’enseignement ou de mentorat, diminue dans un cas comme dans l’autre avec l’âge. 
                        """),
                        # Volunteer rate per activity by age
                        dcc.Graph(id='ActivityVolRate-Age', style={'marginTop': marginTop}),
                    ]),
                    # Formal Education
                    html.Div([
                        html.H5("Éducation formelle"),
                        html.P("""
                        La probabilité d’exercer de nombreuses activités bénévoles a tendance à augmenter avec le niveau d’éducation formelle. L’entretien, la réparation ou la construction d’installations, le porte-à-porte et les premiers soins ou la lutte contre les incendies constituent des exceptions à cette tendance. L’enseignement ou le mentorat, l’organisation ou la coordination d’événements, les soins ou le soutien en matière de santé, les fonctions d’entraîneur.euse ou d’arbitre, et la préservation ou la protection de l’environnement sont toutes des activités pratiquées relativement souvent par les personnes ayant suivi des études supérieures par rapport à celles au niveau d’éducation formelle inférieur.
                        """),
                        # Donation rate & average donation amount by gender
                        dcc.Graph(id='ActivityVolRate-Educ', style={'marginTop': marginTop}),
                    ]),
                    # Marital Status
                    html.Div([
                        html.H5("Situation matrimoniale"),
                        html.P("""
                        Conformément à leur moindre probabilité de faire du bénévolat dans l’ensemble, les personnes veuves sont moins enclines à pratiquer presque toutes les activités bénévoles du champ de l’enquête. Les personnes mariées ou en union de fait sont, au contraire, plus susceptibles d’exercer plusieurs activités bénévoles, dont siéger à un comité ou à un conseil d’administration ou s’occuper du travail de bureau, de la comptabilité ou d’autres tâches administratives. Les célibataires se distinguent en étant particulièrement enclins à enseigner ou à mentorer ou à organiser, superviser ou coordonner des événements.
                        """),
                        # Volunteer rate per activity by marital status
                        dcc.Graph(id='ActivityVolRate-MarStat', style={'marginTop': marginTop}),
                    ]),
                    # Income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("""
                        La probabilité de participer à n’importe quelle activité bénévole augmente avec le revenu du ménage. Les seules exceptions à cette tendance sont les activités de counseling ou de conseils, les soins ou le soutien en matière de santé ou diverses autres activités de ce type, qui varient toutes très peu en fonction du niveau de revenu du ménage.
                        """),
                        # Volunteer rate per activity by household income
                        dcc.Graph(id='ActivityVolRate-Inc', style={'marginTop': marginTop}),
                    ]),
                    # Religious Attendance
                    html.Div([
                        html.H5("Pratique religieuse"),
                        html.P("""
                        Tout comme pour le revenu du ménage, la probabilité de participer à presque toutes les activités bénévoles augmente avec l’assiduité aux offices religieux. Les seules exceptions à cette tendance sont l’exercice des fonctions d’entraîneur.euse, d’arbitre ou de président.e de cérémonie, les premiers soins, la lutte contre les incendies ou les opérations de recherche et de sauvetage ou la préservation et la protection de l’environnement qui varient toutes très peu en fonction de l’assiduité aux offices religieux.
                        """),
                        # Volunteer rate per activity by religious attendance
                        dcc.Graph(id='ActivityVolRate-Relig', style={'marginTop': marginTop}),
                    ]),
                    # Other Factors
                    html.Div([
                        html.H5("Autres facteurs"),
                        html.P("""
                        Dans l’ensemble, la probabilité d’exercer des activités bénévoles particulières ne varie guère en fonction de la situation d’emploi. Étant donné leur participation supérieure aux activités bénévoles, les personnes nées au Canada pratiquent la majorité des activités bénévoles légèrement plus souvent que les personnes naturalisées.
                        """),
                        # Volunteer rate per activity by labour force status
                        # dcc.Graph(id='ActivityVolRate-Labour', style={'marginTop': marginTop}),
                        # Volunteer rate per activity by immigration status
                        # dcc.Graph(id='ActivityVolRate-ImmStat', style={'marginTop': marginTop}),
                    ]),

                    html.Div([
                            html.Div(['Sélectionner le statut:',
                                      dcc.Dropdown(
                                          id='status-selection',
                                          options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                                          value="Situation d'activité",
                                          style={'verticalAlign': 'middle'}
                                      ),],
                                     style={'width': '33%', 'display': 'inline-block'})
                        ]),
                        dcc.Graph(id='status-fig', style={'marginTop': marginTop})
                ], className='col-md-10 col-lg-8 mx-auto'

            ),
        ]),
   ),
   footer
])

# 