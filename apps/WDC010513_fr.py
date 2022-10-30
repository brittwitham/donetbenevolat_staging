import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc
import os
import os.path as op

from utils.graphs.WDC0105_graph_utils import single_vertical_percentage_graph, vertical_dollar_graph, vertical_percentage_graph
from utils.data.WDC0105_data_utils import get_data, process_data, get_region_names, get_region_values

from app import app
from homepage import footer #navbar, footer

####################### Data processing ######################

Reasons_2018, AvgAmtReasons_2018, MotivationsByCause_2018 = get_data()

data = [Reasons_2018, AvgAmtReasons_2018, MotivationsByCause_2018]

cause_names = MotivationsByCause_2018["Group"].unique()
motivations_names = Reasons_2018["QuestionText"].unique()
status_names = ["État civil", "Situation d'activité", "Statut d'immigration"]

process_data(data)

region_values = get_region_values()
region_names = get_region_names()

###################### App layout ######################
navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                # dcc.Link("Home", href="/")
                dbc.NavLink("À propos", href="https://www.donetbenevolat.ca/",external_link=True)
            ),
            dbc.NavItem(
                dbc.NavLink("EN", href="http://app.givingandvolunteering.ca/why_do_canadians_give_2013",external_link=True)
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
                        html.H1('Pourquoi donne-t-on au Canada? (2013)'),
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
        className="bg-secondary text-white text-center py-4",
    ),
    # Note: filters put in separate container to make floating element later
    dbc.Container([
        dbc.Row([
           dbc.Col([
                    html.Div([
                        "Sélectionnez une région:",
                        dcc.Dropdown(
                            id='region-selection',
                            options=[{'label': region_values[i], 'value': region_values[i]} for i in range(len(region_values))],
                            value='CA',
                            ),
                        ],className="m-2 p-2"),
                    html.Div([
                        "Sélectionnez une motivation:",
                        dcc.Dropdown(
                          id='motivation_selection',
                          options=[{'label': motivations_names[i], 'value': motivations_names[i]} for i in range(len(motivations_names)) if isinstance(motivations_names[i], str)],
                          value='Touché.e personnellement par la cause',
                          style={'verticalAlgin': 'middle'}
                      ),
                ],className="m-2 p-2")
           ]),
            ]),
    ],className='sticky-top bg-light mb-2', fluid=True), 
   dbc.Container(
       dbc.Row([
            html.Div(
                [
                    dcc.Markdown("""
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2013, un peu plus de quatre cinquièmes des personnes au Canada (82 %) ont fait un don à un organisme de bienfaisance ou à but non lucratif pendant l’année qui l’a précédée. Afin de mieux comprendre pourquoi les motivations des personnes qui soutiennent les organismes, on leur a demandé ensuite si chacun des sept facteurs ci-dessous jouait un rôle important dans leurs décisions de donner.
                    """),
                    dcc.Markdown("""
                    Nous présentons ci-dessous leurs motivations, puis nous décrivons l’importance relative de ces motivations selon leurs caractéristiques personnelles et économiques. Dans le texte, nous décrivons les résultats au niveau national et vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer légèrement par rapport aux résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.
                    """),
                    dcc.Markdown("""
                    Dans l’ensemble, c’est le sentiment de compassion envers les personnes dans le besoin qui motivait le plus les personnes à donner, ainsi que leur conviction personnelle à l’égard de la cause des organismes qu’ils ont soutenus. À l’échelle nationale, environ quatre personnes sur cinq ont été motivées par le désir de contribuer à la communauté et deux sur trois parce qu’elles étaient touchées personnellement ou parce qu’une personne de leur connaissance était touchée par la cause des organismes qu’elles ont soutenus. Un nombre relativement moins important de personnes ont contribué parce qu’une personne de leur connaissance, une personne amie ou un membre de leur famille le leur a demandé. Les personnes étaient moins enclines à être motivées par leurs obligations ou croyances religieuses ou par le crédit d’impôt qu’elles recevraient en échange de leur don.
                    """
                    ),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Motivations reported by donors.
            html.Div(
                [
                    dcc.Graph(id='MotivationsOverall_13', style={'marginTop': marginTop}),
                    dcc.Markdown('''
                    Quant à l’incidence de ces motivations éventuelles sur les montants des dons, certaines motivations ont tendance à être associées à des dons beaucoup plus importants que d’autres. Les convictions religieuses et spirituelles semblent être, et de loin, les facteurs les plus significatifs. Bien que les personnes motivées par ce facteur aient tendance à réserver leur soutien à des organismes religieux, elles ont également tendance à donner des montants relativement plus élevés à des causes laïques. Bien que seulement une minorité de personnes déclarent que les crédits d’impôt qu’elles reçoivent constituent un facteur pertinent pour leurs décisions de donner, les personnes motivées par ce facteur ont également tendance à donner des montants nettement plus importants. Au chapitre de certaines motivations plus courantes, les personnes qui donnent par motivation envers une cause ou pour contribuer à la communauté ou par compassion envers les personnes dans le besoin donnent des montants environ deux fois plus supérieurs à ceux des personnes non motivées par ces facteurs. Les relations personnelles avec la cause et donner à la suite d’une sollicitation par une personne amie ou un proche parent sont associés à des différences plus petites dans les montants habituels des dons.
                    '''),
                    # Average amounts contributed by donors reporting and not reporting specific motivations.
                    dcc.Graph(id='MotivationsAvgAmts_13', style={'marginTop': marginTop}),

                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Personal & economic characteristics
            html.Div(
                [
                    html.H3('Caractéristiques personnelles et économiques'),
                    html.P("""
                    Bien que les motivations des dons soient fréquemment très personnelles, elles ont également tendance à varier selon leurs caractéristiques personnelles et économiques. Nous analysons ci-dessous les variations des motivations des dons en fonction de certains des facteurs démographiques les plus importants.
                    """
                    ),
                    # Gender
                    html.Div([
                         html.H5("Genre"),
                        html.P("""
                        Dans l’ensemble, les femmes avaient plus tendance que les hommes à faire état de quasiment toutes les motivations pour leurs dons. À l’échelle nationale, ce sont les crédits d’impôt possibles qui constituaient la seule exception à cette tendance, les hommes et les femmes étant tout aussi susceptibles de faire état de cette motivation.
                        """),
                        #Donor motivations by gender
                        html.Div([
                            dcc.Graph(id='Motivations-Gndr_13', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("""
                        L’importance (nombre plus ou moins important de personnes à faire état d’un facteur de motivation) des croyances religieuses et des crédits d’impôt augmentait avec l’âge. L’importance des autres motivations avait tendance à augmenter jusqu’à l’âge moyen, puis à diminuer. Le désir d’offrir une contribution à la communauté et la sollicitation par une personne proche culminaient l’un et d’autre chez les personnes âgées de 35 à 44 ans, tandis que le fait d’être touché par la cause et la conviction à l’égard de la cause culminaient chez celles légèrement plus âgées, de 45 à 54 ans.
                        """),
                        # Donor motivations by age
                        html.Div([
                            dcc.Graph(id='Motivations-Age_13', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Formal Education
                    html.Div([
                        html.H5("Éducation formelle"),
                        html.P("""
                        La probabilité de faire état de la majorité des motivations augmentait avec le niveau d’éducation formelle. Les seules exceptions à cette tendance, du moins au niveau national, étaient les obligations et les convictions religieuses (qui avaient tendance à être importantes à la fois pour les personnes au niveau d’éducation formelle très élevé et très bas) et les sentiments de compassion envers les personnes dans le besoin (qui avaient fortement tendance à être constants, indépendamment du niveau d’éducation formelle). 
                        """),
                        # Donor motivations by formal education
                        html.Div([
                            dcc.Graph(id='Motivations-Educ_13', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # household income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("""
                        Dans l’ensemble, la majorité des motivations ne variaient pas beaucoup en fonction du niveau de revenu du ménage. Pour autant que des tendances étaient significatives, les convictions religieuses avaient tendance à devenir moins importantes avec l’augmentation du revenu, tandis que la sollicitation par une connaissance ou par un membre de la famille gagnait en importance.
                        """),
                        # Donor motivations by household income
                        html.Div([
                            dcc.Graph(id='Motivations-Inc_13', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Religious attendance
                    html.Div([
                        html.H5("Pratique Religieuse"),
                        html.P("""
                        À quelques exceptions près, l’augmentation de l’importance des motivations allait de pair avec l’assiduité aux offices religieux. Cette association était la plus étroite avec les convictions religieuses, mais la plupart des autres motivations étaient également plus importantes pour les personnes assidues aux offices religieux. Les seules motivations qui n’étaient pas plus courantes chez les personnes assidues étaient le fait d’être touchées par la cause et la sollicitation par une personne amie ou membre de leur famille.
                        """),
                        # Donor motivations by religious attendance
                        html.Div([
                           dcc.Graph(id='Motivations-Relig_13', style={'marginTop': marginTop}),
                        ]),
                    ]),
                           
#
                    # Other personal & economic characteristics
                    html.Div([
                        html.H5("Autres facteurs"),
                        html.P("""
                       En ce qui concerne les autres caractéristiques, la majorité des motivations variaient très peu en fonction de la situation d’emploi. Les principales exceptions étaient les dons à la suite de la demande par une connaissance, nettement moins importants pour les personnes qui n’appartenaient pas à la population active (tendance vraisemblablement liée aux dons en milieu de travail), et les motivations religieuses, nettement plus importantes pour les personnes qui n’appartenaient pas à la population active (vraisemblablement plus âgées et à la retraite). Une tendance similaire se constate pour la situation matrimoniale, les associations des personnes veuves et des dons étant identiques à celles des personnes non membres de la population active, en plus de la motivation supérieure des personnes veuves par les crédits d’impôt. Au chapitre du statut d’immigration, les personnes naturalisées étaient nettement plus motivées à donner en raison de leurs croyances religieuses et légèrement plus susceptibles d’être motivées par la plupart des autres croyances. La seule motivation significativement plus importante chez les personnes nées au Canada était le fait d’être personnellement touchées par la cause de l’organisme ou de connaître une personne qui l’était, ce qui dénote peut-être le temps nécessaire pour établir des liens sociaux solides dans un nouveau pays.
                        """),
                        # Donor motivations by marital status
                        # html.Div([
                            # dcc.Graph(id='Motivations-Marstat', style={'marginTop': marginTop}),
                        # ]),
                        # Donor motivations by labour force status
                        # html.Div([
                            # dcc.Graph(id='Motivations-Labour', style={'marginTop': marginTop}),
                        # ]),
                        # Donor motivations by immigration status
                        # html.Div([
                            # dcc.Graph(id='Motivations-Immstat', style={'marginTop': marginTop})
                        # ]),
                        html.Div([
                            html.Div(['Sélectionner le statut:',
                                      dcc.Dropdown(
                                          id='status-selection',
                                          options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                                          value='État civil',
                                          style={'verticalAlign': 'middle'}
                                      ),],
                                     style={'width': '33%', 'display': 'inline-block'})
                        ]),
                        dcc.Graph(id='status-sel13', style={'marginTop': marginTop})
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'

            ),
            html.Div(
                [
                    html.Div([
                       html.H5("Causes soutenues"),
                        html.P("""
                        Bien que l’ESG DBP de 2013 ne recueillait pas directement de l’information sur les motivations du soutien de causes précises, la comparaison des motivations générales des personnes qui soutenaient une cause particulière et de celles qui ne la soutenaient pas peut expliquer ce qui a motivé le soutien de certaines causes. Pour la majorité des motivations et des causes, les personnes qui soutenaient une cause particulière étaient également plus susceptibles de faire état d’une motivation particulière que celles qui s’en abstenaient. En effet, tout bien considéré, les personnes qui soutenaient une cause donnée avaient plus tendance à soutenir de multiples causes et à donner des montants plus importants. Les motivations pouvaient constituer des facteurs significatifs quand le nombre de personnes de chacune de ces deux catégories était inhabituellement élevé ou quand les personnes qui soutenaient une cause étaient moins susceptibles de faire état d’une motivation particulière que celles qui s’en abstenaient.
                        """),
                        html.P("""
                        Le graphique ci-dessous montre le pourcentage de personnes ayant fait état de chaque motivation, ventilé en fonction de leur don ou de leur abstention de donner au bénéfice de chaque cause particulière. Plusieurs associations se constatent à l’échelle nationale. Par exemple, les personnes qui donnaient aux organismes religieux avaient plus tendance à faire état de croyances et de convictions religieuses à titre de motivation pour leurs dons, de même que celles qui donnaient aux organismes du développement international et de l’aide internationale. Dans le même ordre d’idées, les personnes qui donnaient aux organismes du secteur de la santé avaient particulièrement tendance à être touchées personnellement par la cause des organismes soutenus ou à connaître une personne qui l’était, tandis que les personnes qui donnaient aux organismes des services sociaux avaient particulièrement tendance à être motivées par des sentiments de compassion envers les personnes dans le besoin. Vous pouvez utiliser le menu déroulant dans la visualisation des données ci-dessous pour choisir un sous-secteur particulier qui les intéresse.
                        """),
                        # Percentages of cause supporters and non-supporters reporting each motivation, by cause
                        html.Div([
                            html.Div(["Sélectionnez une cause:",
                                dcc.Dropdown(
                                    id='cause-selection',
                                    options=[{'label': cause_names[i], 'value': cause_names[i]} for i in range(len(cause_names))],
                                    value='Arts et culture',
                                    style={'verticalAlgin': 'middle'}
                                ),],
                                style={'width': '33%', 'display': 'inline-block'})
                        ]),
                        dcc.Graph(id='MotivationsCauses_13', style={'marginTop': marginTop}),
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
   ),
   footer
])

################## Callbacks #################

@app.callback(
    dash.dependencies.Output('MotivationsOverall_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = Reasons_2018[Reasons_2018['Region'] == region]
    dff = dff[dff["Group"] == "All"]
    title = '{}, {}'.format("Motivations signalées par les donateur.trice.s", region)
    return single_vertical_percentage_graph(dff, title, by="QuestionText", sort=True)

@app.callback(
    dash.dependencies.Output('MotivationsAvgAmts_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = AvgAmtReasons_2018[AvgAmtReasons_2018['Region'] == region]
    # name1 = "Report motivation"
    # name2 = "Do not report motivation"
    name1 = 'Signalent une motivation'
    name2 = 'Ne signalent aucune motivation'
    title = '{}, {}'.format("Montants moyens des contributions des donateur.trice.s faisant état ou non de motivations précises", region)
    return vertical_dollar_graph(dff, name1, name2, title)

@app.callback(
    dash.dependencies.Output('Motivations-Gndr_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('motivation_selection', 'value')

    ])
def update_graph(region, motivation):
    dff = Reasons_2018[Reasons_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == "Genre"]
    dff = dff[dff["QuestionText"] == motivation]
    title = '{}, {}'.format("Motivations des donateur.trice.s: " + str(motivation) + " selon le genre", region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('Motivations-Age_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('motivation_selection', 'value')

    ])
def update_graph(region, motivation):
    dff = Reasons_2018[Reasons_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == "Groupe d'âge"]
    dff = dff[dff["QuestionText"] == motivation]
    # title = '{}, {}'.format("Donor motivations by age", region)
    title = '{}, {}'.format("Motivations des donateur.trice.s: " + str(motivation) + " selon l’âge", region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('Motivations-Educ_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('motivation_selection', 'value')

    ])
def update_graph(region, motivation):
    dff = Reasons_2018[Reasons_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == "Éducation"]
    dff = dff[dff["QuestionText"] == motivation]
    title = '{}, {}'.format("Motivations des donateur.trice.s: " + str(motivation) + " selon l’éducation formelle", region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('Motivations-Inc_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('motivation_selection', 'value')

    ])
def update_graph(region, motivation):
    dff = Reasons_2018[Reasons_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == "Catégorie de revenu familial"]
    dff = dff[dff["QuestionText"] == motivation]
    title = '{}, {}'.format("Motivations des donateur.trice.s: " + str(motivation) + " selon le revenu du ménage", region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('Motivations-Relig_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('motivation_selection', 'value')

    ])
def update_graph(region, motivation):
    dff = Reasons_2018[Reasons_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == "Fréquence de la fréquentation religieuse"]
    dff = dff[dff["QuestionText"] == motivation]
    title = '{}, {}'.format("Motivations des donateur.trice.s: " + str(motivation) + " selon la pratique religieuse", region)
    return single_vertical_percentage_graph(dff, title)

# @app.callback(
#     dash.dependencies.Output('Motivations-Marstat', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value'),
#         dash.dependencies.Input('motivation_selection', 'value')

#     ])
# def update_graph(region, motivation):
#     dff = Reasons_2018[Reasons_2018['Region'] == region]
#     dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
#     dff = dff[dff["Group"] == "Marital status"]
#     dff = dff[dff["QuestionText"] == motivation]
#     title = '{}, {}'.format("Donor motivation: " + str(motivation) + " by marital status", region)
#     return single_vertical_percentage_graph(dff, title)

# @app.callback(
#     dash.dependencies.Output('Motivations-Labour', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value'),
#         dash.dependencies.Input('motivation_selection', 'value')

#     ])
# def update_graph(region, motivation):
#     dff = Reasons_2018[Reasons_2018['Region'] == region]
#     dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
#     dff = dff[dff["Group"] == "Labour force status"]
#     dff = dff[dff["QuestionText"] == motivation]
#     title = '{}, {}'.format("Donor motivation: " + str(motivation) + " by labour force status", region)
#     return single_vertical_percentage_graph(dff, title)


# @app.callback(
#     dash.dependencies.Output('Motivations-Immstat', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value'),
#         dash.dependencies.Input('motivation_selection', 'value')
#     ])
# def update_graph(region, motivation):
#     dff = Reasons_2018[Reasons_2018['Region'] == region]
#     dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
#     dff = dff[dff["Group"] == "Immigration status"]
#     dff = dff[dff["QuestionText"] == motivation]
#     title = '{}, {}'.format("Donor motivation: " + str(motivation) + " by immigration status", region)
#     return single_vertical_percentage_graph(dff, title)


@app.callback(
    dash.dependencies.Output('status-sel13', 'figure'),
    [ 
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('motivation_selection', 'value'),
        dash.dependencies.Input('status-selection', 'value')
    ])

def update_graph(region, motivation, status):
    dff = Reasons_2018[Reasons_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == status]
    dff = dff[dff["QuestionText"] == motivation]
    title = '{}, {}'.format("Motivations des donateur.trice.s " + str(motivation) + " selon " + str(status).lower(), region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('MotivationsCauses_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('cause-selection', 'value')
    ])
def update_graph(region, cause):
    dff = MotivationsByCause_2018[MotivationsByCause_2018['Region'] == region]
    dff = dff[dff["Group"] == cause]
    name1 = "Soutenir la cause"
    # name1 = 'Support cause'
    name2 = "Ne pas soutenir la cause"
    # name2 = 'Do not support cause'
    title = '{}, {}'.format("Pourcentages de partisan.e.s et de non-partisan.e.s d’une cause faisant état de chaque motivation, selon la cause", region)
    return vertical_percentage_graph(dff, title, name1, name2)