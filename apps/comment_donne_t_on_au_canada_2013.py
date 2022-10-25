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
                dbc.NavLink("EN", href="http://app.givingandvolunteering.ca/What_types_of_organizations_do_Canadians_volunteer_for_2018",external_link=True)
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
                            html.H1('Comment Donne-t-on au Canada? (2013)'),
                            ],
                            className='post-heading'
                        ),
                        className='col-md-10 col-lg-8 mx-auto position-relative'
                    )
                )
            ),
        ], className="bg-secondary text-white text-center py-4",
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
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2013, un peu plus de trois quarts des personnes (78 %) au Canada ont fait un don à un organisme de bienfaisance ou à but non lucratif pendant l’année qui l’a précédée. Chacune d’elles a donné en moyenne 532 $ et le total général des dons s’est chiffré approximativement à 12,8 milliards $. Pour obtenir des précisions sur les variations des montants des dons en fonction des caractéristiques personnelles et par province, veuillez vous reporter à la version 2013 de Qui donne et combien? sur ce site Web.
                    """),
                    dcc.Markdown("""
                    Nous décrivons ci-dessous les méthodes employées par les personnes au Canada pour donner en 2013. Dans le texte, nous décrivons les résultats au niveau national et vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer légèrement par rapport aux résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.
                    """),
                    dcc.Markdown("""
                    Les personnes ont donné de nombreuses façons différentes au Canada. À l’échelle nationale, elles ont donné le plus souvent après une sollicitation dans un lieu public, comme dans la rue ou un centre commercial, en assistant aux offices religieux, en parrainant une personne pour qu’elle participe à un événement ou à la suite d’une sollicitation par courrier. Elles étaient moins enclines à donner à la suite d’une forme ou d’une autre de sollicitation électronique, que ce soit en ligne, à la télévision ou au téléphone. Les personnes avaient tendance à donner les montants les plus importants dans les lieux de culte, après avoir pris contact avec des organismes de leur propre initiative ou en utilisant une méthode de don non mentionnée expressément par le questionnaire de l’enquête. Bien qu’étant beaucoup moins enclines à donner après une sollicitation en ligne qu’après une sollicitation traditionnelle par courrier, les personnes avaient tendance à donner des montants très proches quand elles décidaient de le faire. C’est quand on les sollicite dans un lieu public, au porte-à-porte ou pour parrainer une personne qui participe à un événement qu’elles ont tendance à donner le moins, bien que toutes ces méthodes soient relativement courantes.
                    """
                    ),  
                    # Donation rate & average donation amount by method graph
                    dcc.Graph(id='FormsGiving', style={'marginTop': 20}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            
            # Key personal & economic characteristics
            html.Div(
                [
                    html.H3('Caractéristiques Personnelles et Économiques'),
                    html.P("""
                    Les méthodes employées pour les personnes au Canada pour leurs dons et les montants qu’elles avaient tendance à donner variaient selon leurs caractéristiques personnelles et économiques. Nous montrons ci-dessous les variations de la probabilité de donner et du montant moyen donné selon des caractéristiques clés, dont le genre, l’âge, le niveau d’éducation formelle, le revenu du ménage et l’assiduité aux offices religieux. Nous décrivons, là encore, des tendances générales au niveau national dans le texte, mais vous pouvez prendre connaissance des résultats régionaux en utilisant le menu déroulant.
                    """
                    ),
                    
                   
                
                    # Gender
                    html.Div([
                        html.H5("Genre"),
                        html.P("""
                        Dans le cadre de la majorité des méthodes, les femmes étaient plus enclines à donner que les hommes. Quand des différences statistiquement significatives étaient constatées dans les montants moyens des dons, les femmes donnaient moins que les hommes.
                        """),
                        # Donation rate & average donation amount per method by gender graph
                        dcc.Graph(id='DonRateAvgDonAmt-Gndrr', style={'marginTop': marginTop}),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("""
                       Dans le cadre de la majorité des méthodes de don, la probabilité de donner augmentait pour culminer chez les personnes d’âge moyen avant de diminuer, habituellement chez celles âgées de 65 ans et plus. Les principaux écarts par rapport à cette tendance étaient liés aux dons effectués à un lieu de culte et à la suite de sollicitations par courrier, dont la probabilité augmentait régulièrement avec l’âge dans un cas comme dans l’autre, et aux dons à la suite d’une sollicitation en ligne, dont la probabilité diminuait avec l’âge. En général, les montants moyens des dons avaient tendance à refléter la probabilité de donner (p. ex. quand la probabilité de donner était élevée, le montant moyen des dons l’était également).
                        """),
                        # Donation rate & average donation amount per method by age graph
                        dcc.Graph(id='DonRateAvgDonAmt-Age_13', style={'marginTop': marginTop}),
                    ]),
                    # Formal Education
                    html.Div([
                        html.H5("Éducation Formelle"),
                        html.P("""
                        Pratiquement sans exception, la probabilité de donner par n’importe quelle méthode augmentait avec le niveau d’éducation formelle. En règle générale, le montant moyen des dons avait également tendance à augmenter avec le niveau d’études, bien que cette tendance était légèrement moins uniforme que celle de la probabilité de donner.
                        """),
                        # Donation rate & average donation amount per method by formal education graph
                        dcc.Graph(id='DonRateAvgDonAmt-Educ_13', style={'marginTop': marginTop}),
                    ]),
                    # Income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("""
                        Comme pour le niveau d’éducation formelle, la probabilité de donner par la majorité des méthodes avait tendance à augmenter avec le revenu du ménage, bien que le montant moyen des dons par chaque méthode était plus variable et n’avait pas tendance à augmenter de manière prévisible en fonction du revenu. La probabilité de donner en mémoire d’une personne, à la suite d’une sollicitation par courrier ou d’un appel à la télévision ou à la radio, dans un lieu de culte, où à la suite d’une sollicitation publique avait tendance à être relativement constante entre les catégories de revenus.
                        """),
                        # Donation rate & average donation amount per method by household income graph
                        dcc.Graph(id='DonRateAvgDonAmt-Inc_13', style={'marginTop': marginTop}),
                    ]),
                    # Religious Attendance
                    html.Div([
                        html.H5("Pratique Religieuse"),
                        html.P("""
                        Dans le cadre de la majorité des méthodes de don, la probabilité de donner était légèrement supérieure chez les personnes assistant aux offices religieux au moins deux fois par an. Le montant moyen des dons par certaines méthodes était également supérieur chez les personnes qui y assistent plus fréquemment, mais cette tendance était beaucoup moins uniforme que la tendance de donner. C’est le don à un lieu de culte dont l’association avec la fréquence de la pratique religieuse était la plus forte et la plus nette; la probabilité de donner et les montants moyens des dons augmentaient avec l’assiduité aux offices religieux.
                        """),
                        # Donation rate & average donation amount per method by household income graph
                        dcc.Graph(id='DonRateAvgDonAmt-Relig_13', style={'marginTop': marginTop}),
                    ]),
                    # Other Factors
                    html.Div([
                        html.H5("Autres facteurs "),
                        html.P("""
                        Quant aux autres facteurs, les personnes nées au Canada étaient souvent plus enclines à donner par l’une des méthodes de don que les personnes naturalisées. Les dons par le biais d’un lieu de culte, que les personnes nouvellement arrivées étaient plus enclines à employer, constituaient l’exception notable à cette tendance. Aucune tendance claire n’était associée à la situation d’emploi, bien que certaines méthodes de don (p. ex. donner au travail) étaient associées étroitement au travail et que d’autres (p. ex. donner à la suite d’une sollicitation par courriel) étaient associées étroitement à la non-appartenance à la population active. Pour la majorité des méthodes, l’association ne semblait pas tant liée à la situation d’emploi qu’à d’autres caractéristiques personnelles et économiques qui ont tendance à aller de pair avec la situation d’emploi. La situation semble similaire sur le plan de la situation matrimoniale, la majorité des associations semblant davantage liées à l’âge (c.-à-d. les personnes célibataires ont tendance à être plus jeunes, tandis que celles qui sont veuves ont tendance à être plus âgées).
                        """),
                        # Donation rate & average donation amount per method by marital status graph
                        # dcc.Graph(id='ActivityVolRate-Labour', style={'marginTop': marginTop}),
                        # Donation rate & average donation amount per method by employment status graph
                        # dcc.Graph(id='ActivityVolRate-ImmStat', style={'marginTop': marginTop}),
                        # Donation rate & average donation amount per method by immigration status graph
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
