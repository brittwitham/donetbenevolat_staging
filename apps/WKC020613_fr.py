import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd

from .layout_utils import gen_home_button
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc
import os
import os.path as op
import textwrap

from utils.graphs.WKC0206_graph_utils import vertical_percentage_graph_volunteers, vertical_hours_graph, vertical_percentage_graph
from utils.data.WKC0206_data_utils_13 import get_data, process_data, get_region_names, get_region_values

from app import app
from homepage import footer #navbar, footer
from utils.gen_navbar import gen_navbar

####################### Data processing ######################
BarriersVol_2018, BarriersVolMore_2018, AvgHoursBarriersVol_2018, BarriersVolByCause_2018, BarriersVolMore_20188 = get_data()

data = [BarriersVol_2018, BarriersVolMore_2018, AvgHoursBarriersVol_2018, BarriersVolByCause_2018, BarriersVolMore_20188]
process_data(data)

cause_names = BarriersVolByCause_2018["Group"].unique()
barriers_names = BarriersVol_2018["QuestionText"].unique()
region_values = get_region_values()
region_names = get_region_names()
status_names = ['État civil', 'Fréquence de la fréquentation religieuse', "Statut d'immigration"]

###################### App layout ######################
navbar = gen_navbar("what_keeps_canadians_from_volunteering_more_2013")
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
                        html.H1('Qu’est-ce qui empêche de faire du bénévolat? (2013)'),
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
    #  Dropdown menu
    dbc.Container([
        home_button,
        dbc.Row(
           dbc.Col(
               html.Div(["Sélectionnez une région:",
                  dcc.Dropdown(
                      id='region-selection',
                      options=[{'label': region_values[i], 'value': region_values[i]} for i in range(len(region_values))],
                      value='CA',
                      style={'verticalAlign': 'middle'}
                  ),
                  ],className="m-2 p-2"),
            ),id='sticky-dropdown'),
    ],className='sticky-top select-region mb-2', fluid=True),
   dbc.Container(
       dbc.Row([
            html.Div(
                [
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
                    # Barriers to volunteering, volunteers & non-volunteers
                    dcc.Graph(id='BarriersVolOverall_13', style={'marginTop': marginTop}),
                   dcc.Markdown("""
                    Les bénévoles qui signalaient un frein particulier avaient souvent tendance à faire don de moins d’heures que les personnes qui ne le signalaient pas. À l’échelle nationale, les freins les plus lourds de conséquences, en raison de leur corrélation avec les plus grandes différences dans le nombre d’heures moyen, étaient le don d’argent, de préférence au bénévolat, et l’impossibilité de s’engager à faire plus de bénévolat à long terme. L’inefficacité de la sollicitation des bénévoles semble également très problématique, comme le montrent les importantes différences associées à l’absence de sollicitation pour faire don de plus d’heures et ne pas savoir comment s’engager. 
                    """),
                    dcc.Markdown("""
                    Il est important de comprendre que, bien que ces freins réduisent effectivement le nombre d’heures de bénévolat, ils ne sont pas tous associés à des contributions horaires inférieures en nombre absolu, puisque certains d’entre eux sont associés à des bénévoles qui font don de davantage d’heures. Au niveau national, les bénévoles qui disaient limiter leur heures de bénévolat parce qu’ils pensaient y avoir déjà consacré suffisamment de temps faisaient don, en moyenne, de deux fois plus d’heures, tandis que le nombre d’heures de bénévolat des personnes qui citaient les coûts financiers du bénévolat était supérieur, en moyenne, d’un peu plus du quart du nombre d’heures de bénévolat des personnes qui ne signalaient pas ces freins. Il est important de préciser qu’il ne faut pas en conclure que ces facteurs ne freinaient pas le bénévolat, mais seulement que les personnes qui faisaient don de moins d’heures avait tendance à être moins influencées par ceux-ci.
                    """
                    ),
                    # Average hours contributed by volunteers reporting and not reporting specific motivations
                    dcc.Graph(id='BarriersVolAvgHrs_13', style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Personal & economic characteristics
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
                        html.Div([
                    "Sélectionnez une barrière:",
                        dcc.Dropdown(
                          id='barrier-selection',
                          options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(len(barriers_names))],
                          value='Assez de temps déjà donné',
                          style={'verticalAlgin': 'middle'}
                      ),
                      ],className="m-2 p-2"),
                        # Barriers to volunteering by gender
                        html.Div([
                            dcc.Graph(id='BarriersVol-Gndr_13', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Age
                    html.Div([
                       html.H5("Âge"),
                        html.P("""
                        À l’échelle nationale, la probabilité de limiter ses heures de bénévolat par manque de temps avait tendance à augmenter avec l’âge, de même que le nombre de personnes ayant cité dans leur questionnaire le facteur limitatif des problèmes de santé (plus particulièrement parmi les personnes âgées de 55 ans ou plus). De même, la préférence pour les dons plutôt que pour le bénévolat augmentait jusqu’à l’âge d’environ 45 ans. À l’inverse, la probabilité de l’absence de sollicitation pour faire du bénévolat et de ne pas savoir comment s’engager diminuait, ainsi que le manque de temps pour faire du bénévolat, du moins chez les personnes de 55 ans et plus. Les coûts financiers du bénévolat et l’impossibilité de s’engager à long terme pour faire du bénévolat étaient les plus importants chez les personnes au début de la cinquantaine. 
                        """),
                        # Barriers to volunteering by age
                        html.Div([
                    "Sélectionnez une barrière:",
                        dcc.Dropdown(
                          id='barrier-selection-age',
                          options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(len(barriers_names))],
                          value='Assez de temps déjà donné',
                          style={'verticalAlgin': 'middle'}
                      ),
                      ],className="m-2 p-2"),
                        html.Div([
                            dcc.Graph(id='BarriersVol-Age_13', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Formal Education
                    # html.Div([
                    #     html.H5("Éducation formelle"),
                    #     html.P("""
                    #     Les bénévoles non titulaires du diplôme de fin d’études secondaires ont légèrement plus tendance à limiter leurs heures de bénévolat parce qu’ils ne savent pas comment s’engager ou parce que personne ne leur a demandé d’en faire plus. Les bénévoles comme les non-bénévoles non titulaires du diplôme de fin d’études secondaires sont plus enclins à penser avoir déjà consacré suffisamment de temps au bénévolat. Pour les bénévoles comme pour les non-bénévoles, le manque de temps et les dons d’argent de préférence au bénévolat sont des freins qui prennent plus d’importance avec les niveaux d’éducation formelle supérieurs, de même que l’impossibilité de s’engager à long terme pour les non-bénévoles. Enfin, exclusivement pour les non-bénévoles, les coûts financiers du bénévolat et le manque d’intérêt perdent de leur importance et l’impossibilité de mettre en application leurs compétences ou leurs expériences ou celle de s’engager d’une manière qui leur importe sont des freins qui prennent plus d’importance aux yeux des personnes aux niveaux d’études supérieurs.
                    #     """),
                    #     # Barriers to volunteering by formal education
                    #     html.Div([
                    # "Sélectionnez une barrière:",
                    #     dcc.Dropdown(
                    #       id='barrier-selection-educ',
                    #       options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(len(barriers_names))],
                    #       value='Assez de temps déjà donné',
                    #       style={'verticalAlgin': 'middle'}
                    #   ),
                    #   ],className="m-2 p-2"),
                    #     html.Div([
                    #         dcc.Graph(id='BarriersVol-Educ', style={'marginTop': marginTop}),
                    #     ]),
                    # ]),
                    # household income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("""
                        Le frein des coûts financiers du bénévolat diminuait avec l’augmentation du revenu du ménage, de même que celui des problèmes de santé. En revanche, l’augmentation de l’importance du frein du manque de temps allait de pair avec l’augmentation du revenu du ménage. La majorité des autres freins ne variaient pas de manière significative selon le revenu du ménage. 
                        """),
                        html.Div([
                    "Sélectionnez une barrière:",
                        dcc.Dropdown(
                          id='barrier-selection-income',
                          options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(len(barriers_names))],
                          value='Assez de temps déjà donné',
                          style={'verticalAlgin': 'middle'}
                      ),
                      ],className="m-2 p-2"),
                        # Barriers to volunteering by income
                        html.Div([
                            dcc.Graph(id='BarriersVol-Inc_13', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Labour force status.
                    html.Div([
                        html.H5("Situation d’emploi"),
                        html.P("""
                        Les personnes au chômage avaient légèrement plus tendance à se préoccuper des coûts financiers du bénévolat et à ne pas savoir comment s’engager. En revanche, les personnes qui occupaient un emploi étaient légèrement plus enclines à préférer faire des dons d’argent et à avoir de la difficulté à trouver le temps de faire du bénévolat. Quelques variations selon la situation d’emploi semblent principalement liées à l’âge. Par exemple, les personnes qui n’étaient pas membres de la population active (généralement plus âgées) étaient beaucoup plus susceptibles de faire état du frein des problèmes de santé et légèrement moins susceptibles de se préoccuper des coûts financiers du bénévolat.
                        """),
                        # Barriers to volunteering by labour force status
                        html.Div([
                    "Sélectionnez une barrière:",
                        dcc.Dropdown(
                          id='barrier-selection-labour',
                          options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(len(barriers_names))],
                          value='Assez de temps déjà donné',
                          style={'verticalAlgin': 'middle'}
                      ),
                      ],className="m-2 p-2"),
                        html.Div([
                           dcc.Graph(id='BarriersVol-Labour_13', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Other factors
                    html.Div([
                        html.H5("Autres facteurs "),
                        html.P("""
                        Quant aux variations significatives en fonction des autres caractéristiques personnelles, les personnes veuves étaient beaucoup plus susceptibles de signaler que des problèmes de santé freinaient leur bénévolat et beaucoup moins susceptibles de ne pas avoir le temps de faire du bénévolat. Aucune corrélation forte n’a été constatée entre l’assiduité aux offices religieux et des freins particuliers au bénévolat. Au chapitre du statut d’immigration, les personnes naturalisées étaient légèrement plus enclines à penser avoir déjà fait suffisamment don de leur temps et à avoir eu une mauvaise expérience du bénévolat. Bien que les personnes naturalisées étaient moins susceptibles de limiter leurs heures de bénévolat par manque d’intérêt, elles signalaient plus fréquemment leur difficulté pour savoir comment s’engager.
                        """),
                        # Barriers to volunteering by marital status
                        # html.Div([
                        #     dcc.Graph(id='BarriersVol-Marstat', style={'marginTop': marginTop}),
                        # ]),
                        # # Barriers to volunteering by religious attendance
                        # html.Div([
                        #     dcc.Graph(id='BarriersVol-Labour', style={'marginTop': marginTop}),
                        # ]),
                        # # VBarriers to volunteering by immigration status
                        # html.Div([
                        #     dcc.Graph(id='BarriersVol-Immstat', style={'marginTop': marginTop})
                        # ]),
                        html.Div([
                            html.Div(['Sélectionner le statut:',
                                      dcc.Dropdown(
                                          id='status-selection-volbarrier',
                                          options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                                          value='État civil',
                                          style={'verticalAlign': 'middle'}
                                      ),],
                                     style={'width': '33%', 'display': 'inline-block'}),
                                        html.Div(["Sélectionnez une barrière:",
                                            dcc.Dropdown(
                                            id='barrier-selection-other',
                                            options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(len(barriers_names))],
                                            value='Assez de temps déjà donné',
                                            style={'verticalAlign': 'middle'}
                                      ),],
                                     style={'width': '66%', 'display': 'inline-block'}),
                        ]),
                                        dcc.Graph(id='status-sel-volbarrier_13', style={'marginTop': marginTop})

                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'

            ),
            html.Div(
                [
                    html.Div([
                        html.H3("Causes soutenues "),
                        html.P("""
                        Bien que l’ESG DBP ne recueillait pas directement de l’information sur les freins qui empêchaient les bénévoles de faire don de plus de temps à chaque cause, la comparaison des freins rencontrés par les personnes qui soutiennent une cause donnée et par celles qui ne la soutiennent pas peut nous éclairer. Le graphique ci-dessous montre les pourcentages de bénévoles qui ont fait état de chaque frein, subdivisés en fonction de leur bénévolat ou de leur absence de bénévolat au service d’une cause particulière.
                        """),
                        html.P("""
                        Quelques différences significatives se constatent au niveau national. Par exemple, le manque de temps semble avoir été un frein au bénévolat particulièrement important pour les bénévoles des organismes d’éducation et de recherche, comme pour les bénévoles des universités et lds collèges. De même, les bénévoles des secteurs des arts et de la culture et des sports et des loisirs étaient relativement susceptibles de limiter leurs heures de bénévolat parce qu’ils pensaient avoir déjà fait suffisamment don de leur temps. Les bénévoles des organismes des secteurs des arts et de la culture, du droit, du plaidoyer et de la politique et des universités et des collèges étaient moins enclins à préférer donner de l’argent plutôt qu’à faire du bénévolat, contrairement aux bénévoles du secteur de la santé. Enfin, les bénévoles des hôpitaux étaient beaucoup moins susceptibles de limiter leurs heures de bénévolat parce que personne ne leur avait demandé de faire don de plus d’heures. 
                        """
                        ),
                        html.Div(["Sélectionnez une cause:",
                      dcc.Dropdown(
                          id='cause-selection',
                          options=[{'label': cause_names[i], 'value': cause_names[i]} for i in range(len(cause_names))],
                          value='Arts et culture',
                          style={'verticalAlign': 'middle'}
                      ),
                      ],className="m-2 p-2"),
                        # Percentages of cause supporters and non-supporters reporting each barrier, by cause
                        dcc.Graph(id='BarriersVolCauses_13', style={'marginTop': marginTop}),
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
   ),
   footer
])

################### CALLBACKS ###################

@app.callback(
    dash.dependencies.Output('BarriersVolOverall_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
    ])
def update_graph(region):
    dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
    dff["QuestionText"] = dff["QuestionText"].str.wrap(27)
    dff["QuestionText"] = dff["QuestionText"].replace({'\n': '<br>'}, regex=True)
    dff = dff[dff['Region'] == region]
    dff = dff[dff["Group"] == "All"]
    title = '{}, {}'.format("Freins au bénévolat, bénévoles et non-bénévoles", region)
    return vertical_percentage_graph_volunteers(dff, title, by="QuestionText")

@app.callback(
    dash.dependencies.Output('BarriersVolAvgHrs_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),

    ])
def update_graph(region):
    dff = AvgHoursBarriersVol_2018[AvgHoursBarriersVol_2018['Region'] == region]
    dff["Group"] = dff["Group"].str.wrap(28)
    dff["Group"] = dff["Group"].replace({'\n': '<br>'}, regex=True)
    dff = dff.replace("Report barrier", "Signalent un frein")
    dff = dff.replace("Do not report barrier", "Ne signalent aucun frein")

    # name1 = "Report barrier"
    name1 = "Signalent un frein"
    # name2 = "Do not report barrier"
    name2 = "Ne signalent aucun frein"
    # title_text = 'Average hours volunteered by volunteers reporting and not reporting specific barriers'
    # title_text =  textwrap.fill(text = title_text, width=25)
    title = '{}, {}'.format('Nombre moyen d’heures de bénévolat des bénévoles <br> faisant ou non état de freins précis', region)
    return vertical_hours_graph(dff, name1, name2, title)

##################### Callbacks #####################

@app.callback(
    dash.dependencies.Output('BarriersVol-Gndr_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection', 'value')

    ])
def update_graph(region, barrier):
    dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
    dff["Attribute"] = dff["Attribute"].str.wrap(20, break_long_words=False)
    dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
    dff = dff[dff['Region'] == region]
    dff = dff[dff["Group"] == "Genre"]
    dff = dff[dff["QuestionText"] == barrier]
    title = '{}, {}'.format("Barrière de bénévoles: " + str(barrier) + " selon le genre", region)
    return vertical_percentage_graph_volunteers(dff, title)


@app.callback(
    dash.dependencies.Output('BarriersVol-Age_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection-age', 'value')

    ])
def update_graph(region, barrier):
    dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
    dff["Attribute"] = dff["Attribute"].str.wrap(20, break_long_words=False)
    dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
    dff = dff[dff['Region'] == region]
    dff = dff[dff["Group"] == "Groupe d'âge"]
    dff = dff[dff["QuestionText"] == barrier]
    title = '{}, {}'.format("Barrière de bénévoles: " + str(barrier) + " selon l’âge", region)
    return vertical_percentage_graph_volunteers(dff, title)


# @app.callback(
#     dash.dependencies.Output('BarriersVol-Educ', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value'),
#         dash.dependencies.Input('barrier-selection-educ', 'value')

#     ])
# def update_graph(region, barrier):
#     dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
#     dff["Attribute"] = dff["Attribute"].str.wrap(20, break_long_words=False)
#     dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
#     dff = dff[dff['Region'] == region]
#     dff = dff[dff["Group"] == "Éducation"]
#     dff = dff[dff["QuestionText"] == barrier]
#     title = '{}, {}'.format("Barrière de bénévoles: " + str(barrier) + " selon l’éducation formelle", region)
#     return vertical_percentage_graph_volunteers(dff, title)


# @app.callback(
#     dash.dependencies.Output('BarriersVol-Inc_13', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value'),
#         dash.dependencies.Input('barrier-selection-income', 'value')

#     ])
# def update_graph(region, barrier):
#     dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
#     dff["Attribute"] = dff["Attribute"].str.wrap(20, break_long_words=False)
#     dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
#     dff = dff[dff['Region'] == region]
#     dff = dff[dff["Group"] == "Catégorie de revenu familial"]
#     dff = dff[dff["QuestionText"] == barrier]
#     title = '{}, {}'.format("Barrière de bénévoles: " + str(barrier) + " selon le revenu", region)
#     return vertical_percentage_graph_volunteers(dff, title)

@app.callback(
    dash.dependencies.Output('BarriersVol-Inc_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection-income', 'value')

    ])
def update_graph(region, barrier):
    df = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
    df["Attribute"] = df["Attribute"].str.wrap(20, break_long_words=False)
    df["Attribute"] = df["Attribute"].replace({'\n': '<br>'}, regex=True)


    df = df.replace('15 Ã\xa0 24 ans', '15 à 24 ans')
    df = df.replace('25 Ã\xa0 34 ans', '25 à 34 ans')
    df = df.replace('35 Ã\xa0 44 ans', '35 à 44 ans')
    df = df.replace('45 Ã\xa0 54 ans', '45 à 54 ans')
    df = df.replace('55 Ã\xa0 64 ans', '55 à 64 ans')
    df = df.replace('65 Ã\xa0 74 ans', '65 à 74 ans')
    df = df.replace('75 ans et plus', '75 ans et plus')

    #EDUCATION
    df = df.replace("Sans diplÃ´me d'Ã©tudes secondaires", "Sans diplôme d'études secondaires")
    df = df.replace("DiplÃ´me d'Ã©tudes secondaires", "Diplôme d'études secondaires")
    df = df.replace('DiplÃ´me post-secondaire', 'Diplôme post-secondaire')
    df = df.replace('DiplÃ´me universtaire', "Diplôme universtaire")

    #INCOME
    df = df.replace('Less than $25,000', 'Moins de 25 000 $')
    df = df.replace('25 000 $ Ã\xa0 49 999 $', '25 000 $ à 49 999 $')
    df = df.replace('50 000 $ a 74 999 $', '50 000 $ a 74 999 $')
    df = df.replace('75 000 $ Ã\xa0 99 999 $', '75 000 $ à 99 999 $')
    df = df.replace('100 000 $ Ã\xa0 124 999 $', '100 000 $ à 124 999 $')
    df = df.replace('125 000 $ et plus', '125 000 $ et plus')

    #RELIGIOUS ATTENDANCE
    df = df.replace('At least once a week', 'Au moins 1 fois par semaine')
    df = df.replace('At least once a month', 'Au moins 1 fois par mois')
    df = df.replace('At least 3 times a year', 'Au moins 3 fois par mois')
    df = df.replace('Once or twice a year', '1 ou 2 fois par an')
    df = df.replace('Not at all', 'Pas du tout')

    #MARITAL STATUS
    df = df.replace('MariÃ©.e/union de fait', 'Marié.e/union de fait')
    df = df.replace('SÃ©parÃ©.e/divorcÃ©.e', 'Séparé.e/divorcé.e')

    df = df.replace('MariÃ©.e', 'Marié.e')
    df = df.replace('Living common-law', 'Union de fait')
    df = df.replace('SÃ©parÃ©.e', 'Séparé.e')
    df = df.replace('divorcÃ©.e', 'divorcé.e')
    df = df.replace("Divorcé.e", 'divorcé.e')
    df = df.replace('Widowed', 'Veuf.ve')
    df = df.replace('CÃ©libataire, jamais mariÃ©.e', 'Célibataire, jamais marié.e')


    #EMPLOYMENT STATUS
    df = df.replace('EmployÃ©.e', 'Employé.e')
    df = df.replace('Au chÃ´mage', 'Au chômage')
    df = df.replace('Not in labour force', 'Pas dans la population active')

    #IMMIGRATON STATUS
    df = df.replace('NÃ©.e au Canada', 'Né.e au Canada')
    df = df.replace('NaturalisÃ©.e', 'Naturalisé.e')
    df = df.replace('Non-Canadian', 'Non canadien.ne')

    df = df.replace("Groupe d'Ã¢ge", "Groupe d'âge")
    df = df.replace('Gender', "Genre")
    df = df.replace("Ã\x89ducation", "Éducation")
    df = df.replace('Ã\x89tat civil (original)', "État civil (original)")
    df = df.replace('Ã\x89tat civil (Original)', "État civil (original)")
    df = df.replace('Ã\x89tat civil', "État civil")
    df = df.replace("Situation d'activitÃ©", "Situation d'activité")
    df = df.replace('CatÃ©gorie de revenu personnel', "Catégorie de revenu personnel")
    df = df.replace("CatÃ©gorie de revenu familial", "Catégorie de revenu familial")
    df = df.replace("CatÃ©gorie de revenu familial", "Catégorie de revenu familial")
    df = df.replace('FrÃ©quence de la frÃ©quentation religieuse', "Fréquence de la fréquentation religieuse")
    df = df.replace('Immigration status', "Statut d'immigration")


    df = df[df['Region'] == region]
    df = df[df["Group"] == "Catégorie de revenu familial"]
    df = df[df["QuestionText"] == barrier]
    title = '{}, {}'.format("Barrière de bénévoles: " + str(barrier) + " selon le revenu income", region)
    return vertical_percentage_graph_volunteers(df, title)

@app.callback(
    dash.dependencies.Output('BarriersVol-Labour_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection-labour', 'value')

    ])
def update_graph(region, barrier):
    dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
    dff["Attribute"] = dff["Attribute"].str.wrap(20, break_long_words=False)
    dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
    dff = dff[dff['Region'] == region]
    dff = dff[dff["Group"] == "Situation d'activité"]
    dff = dff[dff["QuestionText"] == barrier]
    title = '{}, {}'.format("Barrière de bénévoles: " + str(barrier) + " selon la situation d’emploi", region)
    return vertical_percentage_graph_volunteers(dff, title)


# @app.callback(
#     dash.dependencies.Output('BarriersVol-Marstat', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value'),
#         dash.dependencies.Input('barrier-selection', 'value')

#     ])
# def update_graph(region, barrier):
#     dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
#     dff["Attribute"] = dff["Attribute"].str.wrap(20, break_long_words=False)
#     dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
#     dff = dff[dff['Region'] == region]
#     dff = dff[dff["Group"] == "Marital status"]
#     dff = dff[dff["QuestionText"] == barrier]
#     title = '{}, {}'.format("Barriers to volunteering by marital status", region)
#     return vertical_percentage_graph_volunteers(dff, title)

# @app.callback(
#     dash.dependencies.Output('BarriersVol-Labour', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value'),
#         dash.dependencies.Input('barrier-selection', 'value')

#     ])
# def update_graph(region, barrier):
#     dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
#     dff["Attribute"] = dff["Attribute"].str.wrap(20, break_long_words=False)
#     dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
#     dff = dff[dff['Region'] == region]
#     dff = dff[dff["Group"] == "Labour force status"]
#     dff = dff[dff["QuestionText"] == barrier]
#     title = '{}, {}'.format("Barriers to volunteering by labour force status", region)
#     return vertical_percentage_graph_volunteers(dff, title)


# @app.callback(
#     dash.dependencies.Output('BarriersVol-Immstat', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value'),
#         dash.dependencies.Input('barrier-selection', 'value')
#     ])
# def update_graph(region, barrier, status):
#     dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
#     dff["Attribute"] = dff["Attribute"].str.wrap(20, break_long_words=False)
#     dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
#     dff = dff[dff['Region'] == region]
#     dff = dff[dff["Group"] == status]
#     dff = dff[dff["QuestionText"] == barrier]
#     title = '{}, {}'.format("Barriers to volunteering by immigration status", region)
#     return vertical_percentage_graph_volunteers(dff, title)

@app.callback(
    dash.dependencies.Output('status-sel-volbarrier_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection-other', 'value'),
        dash.dependencies.Input('status-selection-volbarrier', 'value')
    ])

def update_graph(region, barrier, status):
    dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
    # dff["Attribute"] = dff["Attribute"].str.wrap(20, break_long_words=False)
    # dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
    dff = dff[dff['Region'] == region]
    dff = dff[dff["Group"] == status]
    dff = dff[dff["QuestionText"] == barrier]
    title = '{}, {}'.format("Barrière de bénévoles: " + str(barrier).lower() + '<br>' + ' selon ' + str(status).lower(), region)
    return vertical_percentage_graph_volunteers(dff, title)



@app.callback(
    dash.dependencies.Output('BarriersVolCauses_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('cause-selection', 'value')
    ])
def update_graph(region, cause):
    dff = BarriersVolByCause_2018[BarriersVolByCause_2018['Region'] == region]
    dff = dff[dff["Group"] == cause]
    dff["QuestionText"] = dff["QuestionText"].str.wrap(28)
    dff["QuestionText"] = dff["QuestionText"].replace({'\n': '<br>'}, regex=True)
    dff = dff.replace("Support cause", "Soutiennent la cause")
    dff = dff.replace("Do not support cause", "Ne soutiennent pas la cause")

    # name1 = "Support cause"
    name1 = "Soutiennent la cause"
    name2 = "Ne soutiennent pas la cause"
    # name2 = "Do not support cause"
    title = '{}, {}'.format(str(cause) + " les partisan.e.s et de non-partisan.e.s signalent chaque frein", region)
    return vertical_percentage_graph(dff, title, name1, name2)
