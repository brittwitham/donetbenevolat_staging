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
                dbc.NavLink("EN", href="http://app.givingandvolunteering.ca/what_keeps_canadians_from_volunteering_more_2013",external_link=True)
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
                            html.H1('Qu’est-ce qui empêche de faire du bénévolat? (2013)'),
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
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2013, plus de deux personnes sur cinq au Canada (44 %) au Canada ont fait du bénévolat pour un organisme de bienfaisance ou à but non lucratif pendant l’année qui l’a précédée. Nous analysons ci-dessous les facteurs qui ont peut-être dissuadé des personnes de faire du bénévolat. Nous décrivons dans le texte les résultats au niveau national; pour obtenir plus de précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer légèrement par rapport aux résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.
                    """),
                    dcc.Markdown("""
                    Afin de mieux comprendre les facteurs susceptibles de limiter le soutien des personnes au Canada, on a demandé aux bénévoles et aux non-bénévoles si, parmi dix facteurs différents, un ou plusieurs de ceux-ci les empêchaient soit de faire don de plus d’heures qu’ils l’auraient fait autrement (bénévoles), soit de faire du bénévolat (non-bénévoles).
                    """),
                    dcc.Markdown("""
                    Les principaux freins au bénévolat, dans la mesure où ils étaient signalés le plus souvent, étaient tous liés au temps. Le manque de temps était le frein le plus courant, suivi par l’impossibilité de s’engager à long terme. Pour les bénévoles, le sentiment d’avoir déjà fait suffisamment don de leur temps était le troisième frein, bien qu’il était légèrement moins fréquent chez les non-bénévoles. Les freins les moins fréquents étaient ne pas savoir comment s’engager, les coûts financiers liés au bénévolat et l’insatisfaction à l’égard des expériences de bénévolat passées, les autres freins se situant dans la moyenne.
                    """),
                    dcc.Markdown("""
                    Quant aux différences entre les bénévoles et les non-bénévoles, la majorité des freins avaient tendance à être plus courants pour les non-bénévoles que pour les bénévoles. Les deux exceptions majeures à cette tendance étaient liées au temps : ne pas avoir le temps de faire du bénévolat et le sentiment d’y avoir déjà consacré suffisamment de temps étaient citées l’une et l’autre plus souvent par les bénévoles que par les non-bénévoles. Les freins particulièrement importants pour les non-bénévoles (dans la mesure où ces derniers avaient nettement plus tendance à les signaler) étaient le don d’argent de préférence au bénévolat, l’absence de sollicitation et le manque d’intérêt pour le bénévolat. 
                    """
                    ),

                    #  Barriers to volunteering, volunteers & non-volunteers graph
                    dcc.Graph(id='FormsGiving', style={'marginTop': 20}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                    dcc.Markdown("""
                    Les bénévoles qui signalaient un frein particulier avaient souvent tendance à faire don de moins d’heures que les personnes qui ne le signalaient pas. À l’échelle nationale, les freins les plus lourds de conséquences, en raison de leur corrélation avec les plus grandes différences dans le nombre d’heures moyen, étaient le don d’argent, de préférence au bénévolat, et l’impossibilité de s’engager à faire plus de bénévolat à long terme. L’inefficacité de la sollicitation des bénévoles semble également très problématique, comme le montrent les importantes différences associées à l’absence de sollicitation pour faire don de plus d’heures et ne pas savoir comment s’engager. 
                    """),
                    dcc.Markdown("""
                    Il est important de comprendre que, bien que ces freins réduisent effectivement le nombre d’heures de bénévolat, ils ne sont pas tous associés à des contributions horaires inférieures en nombre absolu, puisque certains d’entre eux sont associés à des bénévoles qui font don de davantage d’heures. Au niveau national, les bénévoles qui disaient limiter leur heures de bénévolat parce qu’ils pensaient y avoir déjà consacré suffisamment de temps faisaient don, en moyenne, de deux fois plus d’heures, tandis que le nombre d’heures de bénévolat des personnes qui citaient les coûts financiers du bénévolat était supérieur, en moyenne, d’un peu plus du quart du nombre d’heures de bénévolat des personnes qui ne signalaient pas ces freins. Il est important de préciser qu’il ne faut pas en conclure que ces facteurs ne freinaient pas le bénévolat, mais seulement que les personnes qui faisaient don de moins d’heures avait tendance à être moins influencées par ceux-ci.
                    """
                    ),
                    # Average hours volunteered by volunteers reporting and not reporting specific barriers graph
                    # dcc.Graph(id='DonRateAvgDonAmt-prv', figure=don_rate_avg_don_amt_prv(DonRates_2018, AvgTotDon_2018), style={'marginTop': 20}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Key personal & economic characteristics
            html.Div(
                [
                    html.H3('Caractéristiques personnelles et économiques'),
                    html.P("""
                    Bien que de nombreux facteurs différents restreignaient potentiellement le bénévolat, leur incidence avait tendance à varier selon des tendances assez générales liées aux caractéristiques personnelles et économiques des bénévoles. Nous analysons ci-dessous comment les freins au bénévolat avaient tendance à varier selon certains des facteurs démographiques les plus importants. Là encore, nous présentons dans le texte les résultats au niveau national, mais vous pourrez utiliser le menu déroulant pour passer en revue les résultats au niveau régional.
                    """
                    ),
                
                    # Gender
                    html.Div([
                        html.H5("Genre"),
                        html.P("""
                        À l’échelle nationale, les hommes étaient nettement plus enclins que les femmes à ne pas faire de bénévolat, ou à limiter leurs heures de bénévolat parce que personne ne les avait sollicités ou parce que le bénévolat ne présentait aucun intérêt pour eux et ils étaient légèrement plus enclins à préférer donner de l’argent plutôt qu’à faire du bénévolat. Les femmes, en revanche, étaient plus susceptibles de ne pas faire de bénévolat ou de limiter leur bénévolat en raison de problèmes de santé ou de leur impossibilité de s’engager à long terme. Les hommes et les femmes étaient à peu près tout aussi susceptibles de signaler la majorité des autres freins au bénévolat.  
                        """),
                        # Barriers to volunteering by gender graph
                        dcc.Graph(id='DonRateAvgDonAmt-Gndrr', style={'marginTop': marginTop}),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("""
                        À l’échelle nationale, la probabilité de limiter ses heures de bénévolat par manque de temps avait tendance à augmenter avec l’âge, de même que le nombre de personnes ayant cité dans leur questionnaire le facteur limitatif des problèmes de santé (plus particulièrement parmi les personnes âgées de 55 ans ou plus). De même, la préférence pour les dons plutôt que pour le bénévolat augmentait jusqu’à l’âge d’environ 45 ans. À l’inverse, la probabilité de l’absence de sollicitation pour faire du bénévolat et de ne pas savoir comment s’engager diminuait, ainsi que le manque de temps pour faire du bénévolat, du moins chez les personnes de 55 ans et plus. Les coûts financiers du bénévolat et l’impossibilité de s’engager à long terme pour faire du bénévolat étaient les plus importants chez les personnes au début de la cinquantaine. 
                        """),
                        # Barriers to volunteering by age graph
                        dcc.Graph(id='DonRateAvgDonAmt-Age_13', style={'marginTop': marginTop}),
                    ]),

                    # Income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("""
                        Le frein des coûts financiers du bénévolat diminuait avec l’augmentation du revenu du ménage, de même que celui des problèmes de santé. En revanche, l’augmentation de l’importance du frein du manque de temps allait de pair avec l’augmentation du revenu du ménage. La majorité des autres freins ne variaient pas de manière significative selon le revenu du ménage. 
                        """),
                        # Barriers to volunteering by income graph
                        dcc.Graph(id='DonRateAvgDonAmt-Inc_13', style={'marginTop': marginTop}),
                    ]),
                    
                    # Labor force status
                    html.Div([
                        html.H5("Situation d’emploi"),
                        html.P("""
                        Les personnes au chômage avaient légèrement plus tendance à se préoccuper des coûts financiers du bénévolat et à ne pas savoir comment s’engager. En revanche, les personnes qui occupaient un emploi étaient légèrement plus enclines à préférer faire des dons d’argent et à avoir de la difficulté à trouver le temps de faire du bénévolat. Quelques variations selon la situation d’emploi semblent principalement liées à l’âge. Par exemple, les personnes qui n’étaient pas membres de la population active (généralement plus âgées) étaient beaucoup plus susceptibles de faire état du frein des problèmes de santé et légèrement moins susceptibles de se préoccuper des coûts financiers du bénévolat.
                        """),
                        # Barriers to volunteering by labour force status graph
                        dcc.Graph(id='DonRateAvgDonAmt-Inc_13', style={'marginTop': marginTop}),
                    ]),

                        
                    # Other factors
                    html.Div([
                        html.H5("Autres facteurs "),
                        html.P("""
                        Quant aux variations significatives en fonction des autres caractéristiques personnelles, les personnes veuves étaient beaucoup plus susceptibles de signaler que des problèmes de santé freinaient leur bénévolat et beaucoup moins susceptibles de ne pas avoir le temps de faire du bénévolat. Aucune corrélation forte n’a été constatée entre l’assiduité aux offices religieux et des freins particuliers au bénévolat. Au chapitre du statut d’immigration, les personnes naturalisées étaient légèrement plus enclines à penser avoir déjà fait suffisamment don de leur temps et à avoir eu une mauvaise expérience du bénévolat. Bien que les personnes naturalisées étaient moins susceptibles de limiter leurs heures de bénévolat par manque d’intérêt, elles signalaient plus fréquemment leur difficulté pour savoir comment s’engager.
                        """),
                        # Barriers to volunteering by marital status graph
                        # dcc.Graph(id='ActivityVolRate-Labour', style={'marginTop': marginTop}),
                        # Barriers to volunteering by religious attendance graph
                        # dcc.Graph(id='ActivityVolRate-ImmStat', style={'marginTop': marginTop}),
                        # Barriers to volunteering by immigration status graph
                        # dcc.Graph(id='ActivityVolRate-ImmStat', style={'marginTop': marginTop}),

                    ]),
                        
                    # Causes supported
                    html.Div([
                        html.H3("Causes soutenues "),
                        html.P("""
                        Bien que l’ESG DBP ne recueillait pas directement de l’information sur les freins qui empêchaient les bénévoles de faire don de plus de temps à chaque cause, la comparaison des freins rencontrés par les personnes qui soutiennent une cause donnée et par celles qui ne la soutiennent pas peut nous éclairer. Le graphique ci-dessous montre les pourcentages de bénévoles qui ont fait état de chaque frein, subdivisés en fonction de leur bénévolat ou de leur absence de bénévolat au service d’une cause particulière.
                        """),
                        html.P("""
                        Quelques différences significatives se constatent au niveau national. Par exemple, le manque de temps semble avoir été un frein au bénévolat particulièrement important pour les bénévoles des organismes d’éducation et de recherche, comme pour les bénévoles des universités et lds collèges. De même, les bénévoles des secteurs des arts et de la culture et des sports et des loisirs étaient relativement susceptibles de limiter leurs heures de bénévolat parce qu’ils pensaient avoir déjà fait suffisamment don de leur temps. Les bénévoles des organismes des secteurs des arts et de la culture, du droit, du plaidoyer et de la politique et des universités et des collèges étaient moins enclins à préférer donner de l’argent plutôt qu’à faire du bénévolat, contrairement aux bénévoles du secteur de la santé. Enfin, les bénévoles des hôpitaux étaient beaucoup moins susceptibles de limiter leurs heures de bénévolat parce que personne ne leur avait demandé de faire don de plus d’heures. 
                        """
                        ),
                        # Percentages of cause supporters and non-supporters reporting each barrier, by cause graph
                        # dcc.Graph(id='ActivityVolRate-Labour', style={'marginTop': marginTop}),
                            
                            
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
