import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc
import os
import os.path as op

from utils.graphs.WTO0207_graph_utils import rate_avg_cause, single_vertical_percentage_graph
from utils.data.WTO0207_data_utils import get_data, process_data, get_region_names, get_region_values


from app import app
from homepage import footer #navbar, footer

####################### Data processing ######################
BarriersVol_2018, SubSecAvgHrs_2018, SubSecVolRates_2018, AllocationVol_2018 = get_data()

data = [SubSecVolRates_2018, SubSecAvgHrs_2018, AllocationVol_2018]
process_data(data)

region_values = get_region_values()
# region_names = get_region_names()
region_names = ['CA', 'BC', 'AB', 'PR', 'ON', 'QC', 'AT']
###################### App layout ######################
navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                # dcc.Link("Home", href="/")
                dbc.NavLink("À propos", href="https://www.donetbenevolat.ca/",external_link=True)
            ),
            dbc.NavItem(
                dbc.NavLink("EN", href="http://app.givingandvolunteering.ca/what_do_volunteers_do_2013",external_link=True)
            ),
        ],
        brand="Centre Canadien de Connaissances sur les Dons et le Bénévolat",
        brand_href="/",
        color="#4B161D",
        dark=True,
        sticky='top'
    )

marginTop = 20

layout = html.Div([
    navbar,
    html.Header([
            html.Div(className='overlay'),
            dbc.Container(
                dbc.Row(
                    html.Div(
                        html.Div([
                            html.H1('Quelles sont les activités des bénévoles? (2013)'),
                            ],
                            className='post-heading'
                        ),
                        className='col-md-10 col-lg-8 mx-auto position-relative'
                    )
                )
            ),
        ], className="bg-secondary text-white text-center pt-4",
    ),
    dbc.Container([
        dbc.Row([
            dbc.Col(
               html.Div([
                   "Select a region:",
                   dcc.Dropdown(
                       id='region-selection',
                       options=[{'label': region_values[i], 'value': region_values[i]} for i in range(len(region_values))],
                       value='CA',
                       ),
                    html.Br(),
                ],className="m-2 p-2"),
            ),
            # dbc.Col(
            #    html.Div([
            #     "Choose a volunteer activity: ",
            #     dcc.Dropdown(id='activity-selection',
            #         options=[{'label': i, 'value': i} for i in activity_names],
            #         value="Canvassing")
            #     ],className="m-2 p-2"),
            # )
            ],
            id='sticky-dropdown'),
    ], className='sticky-top bg-light mb-2', fluid=True),

   dbc.Container([
       dbc.Row([
            # Starting text
            html.Div([
                    dcc.Markdown("""
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2013, plus de deux personnes sur cinq (44 %) au Canada ont fait du bénévolat pour un organisme de bienfaisance ou à but non lucratif pendant la période d’un an qui l’a précédée. Ces bénévoles accomplissaient un large éventail de tâches, allant de la collecte de fonds à la lutte contre les incendies. Nous analysons ci-dessous à quelles tâches les bénévoles consacraient leur temps et leur tendance à se livrer à certaines activités, selon leurs caractéristiques personnelles et économiques. Dans le texte, nous décrivons les résultats au niveau national, mais, pour obtenir des précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer des résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.
                    """),
                    dcc.Markdown("""
                    À l’échelle nationale, environ un cinquième des bénévoles au Canada ont organisé des activités ou des événements ou des collectes de fonds. Entre un sur sept et un sur dix des bénévoles siégeait à des comités ou à des conseils d’administration, enseignaient à d’autres personnes ou leur servaient de mentor.e.s, offraient des services de counseling ou des conseils, collectaient de la nourriture et des biens et les distribuaient ou effectuaient une forme ou une autre travail de bureau, dont la comptabilité, la gestion d’une bibliothèque ou d’autres tâches administratives. Les activités bénévoles les moins courantes étaient le porte-à-porte pour un organisme ou les premiers soins, la lutte contre les incendies ou l’appui aux opérations de recherche et de sauvetage. Les bénévoles avaient tendance à consacrer plus de temps à certaines activités, plus précisément à prodiguer des soins de santé et les premiers soins ou à offrir des soutiens connexes, à enseigner ou à servir de mentor.e.s ou à réaliser du travail de bureau. En revanche, les bénévoles avaient tendance à consacrer moins de temps au porte-à-porte, aux activités de protection de l’environnement, aux collectes de fonds ou aux collectes ou à la livraison de biens.
                    """
                    ),
                    # Volunteer rate & average hours contributed by activity graph
                    dcc.Graph(id='FormsGiving', style={'marginTop': 20}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),

            # Personal and economic characteristics
            html.Div(
                [
                    html.H3('Caractéristiques personnelles et économiques'),
                    html.P("""
                    Les activités bénévoles au Canada avaient tendance à varier selon les caractéristiques personnelles et économiques. Nous analysons ci-dessous comment la probabilité de faire du bénévolat variait, pour chaque type d’activité, selon les caractéristiques personnelles et économiques clés des bénévoles. Nous décrivons, là encore, des tendances générales au niveau national dans le texte, mais vous pourrez prendre connaissance des résultats régionaux en utilisant le menu déroulant lié aux visualisations de données.
                    """),

                    #Gender
                    html.Div([
                        html.H5("Genre"),
                        html.P("""
                        À l’échelle nationale, pour autant que les différences entre les genres étaient statistiquement significatives, les femmes avaient plus tendance que les hommes à prendre part à la majorité des activités bénévoles. S’agissant des exceptions particulières à cette tendance générale, les hommes étaient plus enclins que les femmes à servir d’entraîneurs, d’arbitres ou de présidents de cérémonie, à exécuter des travaux d’entretien ou de réparation et à offrir des services de counseling ou des conseils.
                        """),
                        # Volunteer rate by activity by gender graph
                        dcc.Graph(id='DonRateAvgDonAmt-Gndrr', style={'marginTop': marginTop}),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("""
                        Dans l’ensemble, le bénévolat dans le cadre de chaque activité particulière suivait globalement la tendance plus générale du bénévolat, les personnes de 15 à 25 ans étant fortement enclines à faire du bénévolat, cette tendance chutant de manière significative chez les personnes âgées de 25 à 34 ans, suivies par des proportions supérieures de bénévoles chez celles d’âge moyen, puis d’une baisse chez les groupes plus âgés. Pour chaque groupe d’âge particulier, la probabilité maximale de faire du bénévolat variait d’une activité à l’autre, mais cette tendance générale était très uniforme. Les seuls écarts importants par rapport à celle-ci avaient trait au rôle de membre d’un comité ou d’un conseil d’administration dont la popularité avait tendance à augmenter jusqu’à l’âge de 75 ans ou au-delà, et aux fonctions d’entraîneur.euse, d’arbitre et de président.e de cérémonie dont la popularité, sauf chez les bénévoles de 25 à 34 ans, moins enclins à les exercer, avait tendance à diminuer avec l’âge.
                        """),
                        # Volunteer rate by activity by age graph
                        dcc.Graph(id='DonRateAvgDonAmt-Age_13', style={'marginTop': marginTop}),
                    ]),
                    # Formal Education
                    html.Div([
                        html.H5("Éducation formelle"),
                        html.P("""
                        La probabilité d’exercer quasiment toutes les activités bénévoles avait tendance à augmenter avec le niveau d’éducation formelle. La probabilité d’exercer le rôle d’entraîneur.euse, d’arbitre ou de président.e de cérémonie se démarquait quelque peu en n’augmentant pas avec le niveau d’éducation formelle chez les personnes non titulaires d’un diplôme universitaire, et, dans une certaine mesure, c’était également le cas pour la collecte de biens ou de nourriture et leur distribution.
                        """),
                        # Volunteer rate by activity by formal education graph
                        dcc.Graph(id='DonRateAvgDonAmt-Educ_13', style={'marginTop': marginTop}),
                    ]),
                    # Marital Status
                    html.Div([
                        html.H5("Situation matrimoniale"),
                        html.P("""
                        Conformément à leur moindre probabilité de faire du bénévolat, les personnes veuves pratiquaient presque toutes les activités bénévoles moins souvent que les autres personnes, contrairement aux personnes célibataires et mariées ou en union de fait. Cette tendance était la plus prononcée pour des activités comme l’enseignement ou le mentorat ou celle de membre d’un conseil d’administration ou d’un comité, mais elle était quasiment universelle.
                        """),
                        # Volunteer rate by activity by marital status graph
                        dcc.Graph(id='DonRateAvgDonAmt-Inc_13', style={'marginTop': marginTop}),
                    ]),
                        
                    # Income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("""
                        La probabilité de participer à n’importe quelle activité donnée avait tendance à augmenter avec le revenu du ménage. Le seul écart important par rapport à cette tendance, du moins au niveau national, était lié aux ménages au revenu compris entre 120 000 $ et moins de 140 000 $, légèrement moins enclins à participer à certaines formes de bénévolat (p. ex. counseling ou conseils) que la tendance générale le donnerait à penser.
                        """),
                        # Volunteer rate by activity by household income graph
                        dcc.Graph(id='DonRateAvgDonAmt-Inc_13', style={'marginTop': marginTop}),
                    ]),
                    # Religious Attendance
                    html.Div([
                        html.H5("Pratique religieuse"),
                        html.P("""
                        Tout comme pour le revenu du ménage, la probabilité de participer à presque toutes les activités bénévoles augmentait avec l’assiduité aux offices religieux. Les seules exceptions à cette tendance étaient les activités de porte-à-porte pour un organisme, d’entraîneur.euse ou de président.e de cérémonie, de premiers soins et de lutte contre les incendies, ainsi que de protection de l’environnement. Les personnes assistant chaque semaine aux offices religieux étaient à peu près aussi susceptibles de participer à ces activités que celles y assistant une fois par mois.
                        """),
                        # Volunteer rate by activity by religious attendance graph
                        dcc.Graph(id='DonRateAvgDonAmt-Relig_13', style={'marginTop': marginTop}),
                    ]),
                    # Other Factors
                    html.Div([
                        html.H5("Autres facteurs"),
                        html.P("""
                        Comme les personnes non membres de la population active sont souvent plus âgées, elles étaient moins susceptibles de participer à la majorité des activités bénévoles. Du point de vue du statut d’immigration, les personnes nées au Canada avaient relativement plus tendance à exercer la majorité des activités bénévoles que les personnes nouvellement arrivées.
                        """),
                        # Volunteer rate by activity by labour force status graph
                        # dcc.Graph(id='ActivityVolRate-Labour', style={'marginTop': marginTop}),
                        # Volunteer rate by activity by immigration status graph
                        # dcc.Graph(id='ActivityVolRate-ImmStat', style={'marginTop': marginTop}),

                            
                        # html.Div(['Select status:',
                        #               dcc.Dropdown(
                        #                   id='status-selection1',
                        #                   options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                        #                   value='Marital status',
                        #                   style={'verticalAlign': 'middle'}
                        #               ),],
                        #              style={'width': '50%', 'display': 'inline-block'}),
                        html.Div([
                            # html.H6("Donation rate & average donation amount by immigration status"),
                            dcc.Graph(id='DonRateAvgDonAmt-other_13', style={'marginTop': marginTop}),
                            #html.P("Overall, those who were married or in a common-law relationship accounted to a significantly higher fraction of total donations than their numbers would suggest, as did New Canadians and, to a more modest extent, those who were employed."),
                            html.Br(),
                        ]),
                        # html.Div(['Select status:',
                        #               dcc.Dropdown(
                        #                   id='status-selection2',
                        #                   options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                        #                   value='Marital status',
                        #                   style={'verticalAlign': 'middle'}
                        #               ),],
                        #              style={'width': '50%', 'display': 'inline-block'}),
                        html.Div([
                            # html.H6("Percentage of donors & total donation value by immigration status"),
                            dcc.Graph(id='PercDon-other_13', style={'marginTop': marginTop}),
                            html.Br(),
                            # html.P("The degree to which Canadians focus on the primary cause they support does not seem to vary significantly according to their marital or labour force status. Married, widowed, and to a certain extent divorced Canadians tend to support a somewhat wider range of causes, as do those who are not in the labour force. Turning to immigration status, New Canadians and those residing in Canada who have not yet obtained landed immigrant status tend to focus more of their support on the primary cause and to support fewer causes than do native-born Canadians."),
                        ]),
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'

            ),
        ]),
]),
footer
]) 


################## CALLBACKS ##################

# @app.callback(

#     dash.dependencies.Output('DonRateAvgDonAmt-Cause-2', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):

#     dff1 = SubSecVolRates_2018[SubSecVolRates_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == "All"]
#     dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")
#     # name1 = "Volunteer rate"
#     name1 = "Taux de bénévolat"

#     dff2 = SubSecAvgHrs_2018[SubSecAvgHrs_2018['Region'] == region]
#     dff2 = dff2[dff2['Group'] == "All"]
#     dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
#     # name2 = "Average hours"
#     name2 = "Nombre d'heures moyen"

#     title = '{}, {}'.format("Niveaux de soutien par cause", region)

#     return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)


# @app.callback(

#     dash.dependencies.Output('AllocationSupport-Cause-2', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):

#     dff = AllocationVol_2018[AllocationVol_2018['Region'] == region]
#     title = '{}, {}'.format("Répartition du soutien par cause", region)

#     return single_vertical_percentage_graph(dff, title, by="QuestionText", sort=True)
