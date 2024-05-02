import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
# from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ClientsideFunction

from utils.graphs.WDV0202_graph_utils import vol_rate_avg_hrs_qt, single_vertical_percentage_graph
from utils.data.WDV0202_data_utils_13 import get_data, get_region_values, process_data, get_region_names, get_region_values

from app import app
from homepage import footer
from .layout_utils import gen_home_button #navbar, footer
from utils.gen_navbar import gen_navbar

####################### Data processing ######################

ActivityVolRate_2018, AvgHoursVol_2018 = get_data()
data = [ActivityVolRate_2018, AvgHoursVol_2018]
process_data(data)

# Extract info from data for selection menus
region_values = get_region_values()
region_names = get_region_names()
activity_names = ActivityVolRate_2018.QuestionText.unique()
status_names = ["Situation d'activité", "Statut d'immigration"]

names = []
for i in activity_names:
    i.replace("<br>", '')
    names.append(i)

activity_names = names
###################### App layout ######################
navbar = gen_navbar("what_do_volunteers_do_2013")
home_button = gen_home_button(is_2013=True, sat_link=False, bc_link=False)
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
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2013, plus de deux personnes sur cinq (44 %) au Canada ont fait du bénévolat pour un organisme de bienfaisance ou à but non lucratif pendant la période d’un an qui l’a précédée. Ces bénévoles accomplissaient un large éventail de tâches, allant de la collecte de fonds à la lutte contre les incendies. Nous analysons ci-dessous à quelles tâches les bénévoles consacraient leur temps et leur tendance à se livrer à certaines activités, selon leurs caractéristiques personnelles et économiques. Dans le texte, nous décrivons les résultats au niveau national, mais, pour obtenir des précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer des résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.
                    """),
                    dcc.Markdown("""
                    À l’échelle nationale, environ un cinquième des bénévoles au Canada ont organisé des activités ou des événements ou des collectes de fonds. Entre un sur sept et un sur dix des bénévoles siégeait à des comités ou à des conseils d’administration, enseignaient à d’autres personnes ou leur servaient de mentor.e.s, offraient des services de counseling ou des conseils, collectaient de la nourriture et des biens et les distribuaient ou effectuaient une forme ou une autre travail de bureau, dont la comptabilité, la gestion d’une bibliothèque ou d’autres tâches administratives. Les activités bénévoles les moins courantes étaient le porte-à-porte pour un organisme ou les premiers soins, la lutte contre les incendies ou l’appui aux opérations de recherche et de sauvetage. Les bénévoles avaient tendance à consacrer plus de temps à certaines activités, plus précisément à prodiguer des soins de santé et les premiers soins ou à offrir des soutiens connexes, à enseigner ou à servir de mentor.e.s ou à réaliser du travail de bureau. En revanche, les bénévoles avaient tendance à consacrer moins de temps au porte-à-porte, aux activités de protection de l’environnement, aux collectes de fonds ou aux collectes ou à la livraison de biens.
                    """
                    ),
                    # Volunteer rate & average hours contributed by activity
                    dcc.Graph(id='ActivitiesVolRateAvgHrs_13', style={'marginTop': 20}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Key personal & economic characteristics
            html.Div(
                [
                    html.H3('Caractéristiques personnelles et économiques'),
                    html.P("""
                    Les activités bénévoles au Canada avaient tendance à varier selon les caractéristiques personnelles et économiques. Nous analysons ci-dessous comment la probabilité de faire du bénévolat variait, pour chaque type d’activité, selon les caractéristiques personnelles et économiques clés des bénévoles. Nous décrivons, là encore, des tendances générales au niveau national dans le texte, mais vous pourrez prendre connaissance des résultats régionaux en utilisant le menu déroulant lié aux visualisations de données.
                    """),
                    # Gender
                    html.Div([
                        html.H5("Genre"),
                        html.P("""
                        À l’échelle nationale, pour autant que les différences entre les genres étaient statistiquement significatives, les femmes avaient plus tendance que les hommes à prendre part à la majorité des activités bénévoles. S’agissant des exceptions particulières à cette tendance générale, les hommes étaient plus enclins que les femmes à servir d’entraîneurs, d’arbitres ou de présidents de cérémonie, à exécuter des travaux d’entretien ou de réparation et à offrir des services de counseling ou des conseils.
                        """),
                        # Donation rate & average donation amount by gender
                        dcc.Graph(id='ActivityVolRate-Gndr_13', style={'marginTop': marginTop}),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("""
                        Dans l’ensemble, le bénévolat dans le cadre de chaque activité particulière suivait globalement la tendance plus générale du bénévolat, les personnes de 15 à 25 ans étant fortement enclines à faire du bénévolat, cette tendance chutant de manière significative chez les personnes âgées de 25 à 34 ans, suivies par des proportions supérieures de bénévoles chez celles d’âge moyen, puis d’une baisse chez les groupes plus âgés. Pour chaque groupe d’âge particulier, la probabilité maximale de faire du bénévolat variait d’une activité à l’autre, mais cette tendance générale était très uniforme. Les seuls écarts importants par rapport à celle-ci avaient trait au rôle de membre d’un comité ou d’un conseil d’administration dont la popularité avait tendance à augmenter jusqu’à l’âge de 75 ans ou au-delà, et aux fonctions d’entraîneur.euse, d’arbitre et de président.e de cérémonie dont la popularité, sauf chez les bénévoles de 25 à 34 ans, moins enclins à les exercer, avait tendance à diminuer avec l’âge.
                        """),
                        # Volunteer rate per activity by age
                        dcc.Graph(id='ActivityVolRate-Age_13', style={'marginTop': marginTop}),
                    ]),
                    # Formal Education
                    html.Div([
                        html.H5("Éducation formelle"),
                        html.P("""
                        La probabilité d’exercer quasiment toutes les activités bénévoles avait tendance à augmenter avec le niveau d’éducation formelle. La probabilité d’exercer le rôle d’entraîneur.euse, d’arbitre ou de président.e de cérémonie se démarquait quelque peu en n’augmentant pas avec le niveau d’éducation formelle chez les personnes non titulaires d’un diplôme universitaire, et, dans une certaine mesure, c’était également le cas pour la collecte de biens ou de nourriture et leur distribution.
                        """),
                        # Donation rate & average donation amount by gender
                        dcc.Graph(id='ActivityVolRate-Educ_13', style={'marginTop': marginTop}),
                    ]),
                    # Marital Status
                    html.Div([
                        html.H5("Situation matrimoniale"),
                        html.P("""
                        Conformément à leur moindre probabilité de faire du bénévolat, les personnes veuves pratiquaient presque toutes les activités bénévoles moins souvent que les autres personnes, contrairement aux personnes célibataires et mariées ou en union de fait. Cette tendance était la plus prononcée pour des activités comme l’enseignement ou le mentorat ou celle de membre d’un conseil d’administration ou d’un comité, mais elle était quasiment universelle.
                        """),
                        # Volunteer rate per activity by marital status
                        dcc.Graph(id='ActivityVolRate-MarStat_13', style={'marginTop': marginTop}),
                    ]),
                    # Income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("""
                        La probabilité de participer à n’importe quelle activité donnée avait tendance à augmenter avec le revenu du ménage. Le seul écart important par rapport à cette tendance, du moins au niveau national, était lié aux ménages au revenu compris entre 120 000 $ et moins de 140 000 $, légèrement moins enclins à participer à certaines formes de bénévolat (p. ex. counseling ou conseils) que la tendance générale le donnerait à penser.
                        """),
                        # Volunteer rate per activity by household income
                        dcc.Graph(id='ActivityVolRate-Inc_13', style={'marginTop': marginTop}),
                    ]),
                    # Religious Attendance
                    html.Div([
                        html.H5("Pratique religieuse"),
                        html.P("""
                        Tout comme pour le revenu du ménage, la probabilité de participer à presque toutes les activités bénévoles augmentait avec l’assiduité aux offices religieux. Les seules exceptions à cette tendance étaient les activités de porte-à-porte pour un organisme, d’entraîneur.euse ou de président.e de cérémonie, de premiers soins et de lutte contre les incendies, ainsi que de protection de l’environnement. Les personnes assistant chaque semaine aux offices religieux étaient à peu près aussi susceptibles de participer à ces activités que celles y assistant une fois par mois.
                        """),
                        # Volunteer rate per activity by religious attendance
                        dcc.Graph(id='ActivityVolRate-Relig_13', style={'marginTop': marginTop}),
                    ]),
                    # Other Factors
                    html.Div([
                        html.H5("Autres facteurs"),
                        html.P("""
                        Comme les personnes non membres de la population active sont souvent plus âgées, elles étaient moins susceptibles de participer à la majorité des activités bénévoles. Du point de vue du statut d’immigration, les personnes nées au Canada avaient relativement plus tendance à exercer la majorité des activités bénévoles que les personnes nouvellement arrivées.
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
                        dcc.Graph(id='status-fig_13', style={'marginTop': marginTop})
                ], className='col-md-10 col-lg-8 mx-auto'

            ),
        ]),
   ),
   footer
])

# ###################### CALLBACKS ######################
@app.callback(
    dash.dependencies.Output('ActivitiesVolRateAvgHrs_13', 'figure'),
    [

        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):

    dff1 = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "All"]
    dff1 = dff1.replace("Health care or support", "Soins de santé ou soutien")
    # name1 = "Volunteer rate"
    name1 = 'Taux de bénévolat'

    dff2 = AvgHoursVol_2018[AvgHoursVol_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "All"]
    dff2 = dff2.replace("Health care or support", "Soins de santé ou soutien")
    dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")

    # name2 = "Average hours"
    name2 = "Nombre d'heures moyen"

    title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures de bénévolat par activité", region)

    return vol_rate_avg_hrs_qt(dff1, dff2, name1, name2, title)


@app.callback(
    dash.dependencies.Output('ActivityVolRate-Gndr_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('activity-selection', 'value')
    ])
def update_graph(region, activity):
    dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
    dff = dff[dff['QuestionText'] == activity]
    dff = dff[dff['Group'] == "Genre"]

    title = '{}, {}'.format(str(activity) + " selon le genre", region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('ActivityVolRate-Age_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('activity-selection', 'value')
    ])
def update_graph(region, activity):
    dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
    dff = dff[dff['QuestionText'] == activity]
    dff = dff[dff['Group'] == "Groupe d'âge"]

    title = '{}, {}'.format(str(activity) + " selon l’âge", region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('ActivityVolRate-Educ_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('activity-selection', 'value')
    ])
def update_graph(region, activity):
    dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
    dff = dff[dff['QuestionText'] == activity]
    dff = dff[dff['Group'] == "Éducation"]
    dff = dff[dff['Attribute'] != "Non indiqué"]

    title = '{}, {}'.format(str(activity) + " l’éducation formelle", region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('ActivityVolRate-MarStat_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('activity-selection', 'value')
    ])
def update_graph(region, activity):
    dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
    dff = dff[dff['QuestionText'] == activity]
    dff = dff[dff['Group'] == "État civil"]

    title = '{}, {}'.format(str(activity) + " selon la situation matrimoniale", region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('ActivityVolRate-Inc_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('activity-selection', 'value')
    ])
def update_graph(region, activity):
    dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
    dff = dff[dff['QuestionText'] == activity]
    dff = dff[dff['Group'] == "Catégorie de revenu familial"]

    title = '{}, {}'.format(str(activity) + " selon le revenu du ménage", region)
    return single_vertical_percentage_graph(dff, title)


@app.callback(
    dash.dependencies.Output('ActivityVolRate-Relig_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('activity-selection', 'value')
    ])
def update_graph(region, activity):
    dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
    dff = dff[dff['QuestionText'] == activity]
    dff = dff[dff['Group'] == "Fréquence de la fréquentation religieuse"]
    dff = dff[dff['Attribute'] != "Non indiqué"]

    title = '{}, {}'.format(str(activity) + " selon la pratique religieuse", region)
    return single_vertical_percentage_graph(dff, title)


# @app.callback(
#     dash.dependencies.Output('ActivityVolRate-Labour', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value'),
#         dash.dependencies.Input('activity-selection', 'value')
#     ])
# def update_graph(region, activity):
#     dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
#     dff = dff[dff['QuestionText'] == activity]
#     dff = dff[dff['Group'] == "Situation d'activité"]

#     title = '{}, {}'.format(str(activity) + " selon la situation d’emploi", region)
#     return single_vertical_percentage_graph(dff, title)


# @app.callback(
#     dash.dependencies.Output('ActivityVolRate-ImmStat', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value'),
#         dash.dependencies.Input('activity-selection', 'value')
#     ])
# def update_graph(region, activity):
#     dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
#     dff = dff[dff['QuestionText'] == activity]
#     dff = dff[dff['Group'] == "Statut d'immigration"]

#     title = '{}, {}'.format(str(activity) + " selon le statut d’immigration", region)
#     return single_vertical_percentage_graph(dff, title)


@app.callback(
    dash.dependencies.Output('status-fig_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('activity-selection', 'value'),
        dash.dependencies.Input('status-selection', 'value')

    ])
def update_graph(region, activity, status):
    dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
    dff = dff[dff['QuestionText'] == activity]
    dff = dff[dff['Group'] == status]

    title = '{}, {}'.format(str(activity) + " selon " + str(status).lower(), region)
    return single_vertical_percentage_graph(dff, title)
