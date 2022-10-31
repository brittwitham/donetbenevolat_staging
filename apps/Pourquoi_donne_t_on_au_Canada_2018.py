import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd

from utils.home_button import gen_home_button
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
                dbc.NavLink("EN", href="http://app.givingandvolunteering.ca/Why_do_Canadians_give_2018",external_link=True)
            ),
        ],
        brand="Centre Canadien de Connaissances sur les Dons et le Bénévolat",
        brand_href="/",
        color="#4B161D",
        dark=True,
        sticky='top'
    )
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
                        html.H1('Pourquoi donne-t-on au Canada?'),
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
        className="bg-secondary text-white text-center pt-4",
    ),
    # Note: filters put in separate container to make floating element later
    dbc.Container([
        home_button,
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
                    dcc.Markdown('''
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, un peu plus de deux tiers des personnes au Canada (68 %) ont fait un don à un organisme de bienfaisance ou à but non lucratif pendant l’année qui l’a précédée. Afin de mieux comprendre pourquoi les donateur.trice.s soutiennent les organismes, on leur a demandé ensuite si chacun des huit facteurs ci-dessous jouait un rôle important dans leurs décisions de donner. 
                    ''',className='mt-4'),
                    dcc.Markdown('''
                                 Nous présentons ci-dessous leurs motivations, puis nous décrivons l’importance de la variation de ces motivations selon leurs caractéristiques personnelles et économiques. Dans le texte, nous décrivons les résultats au niveau national et vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer légèrement par rapport aux résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.'''),
                    dcc.Markdown('''
                    Dans l’ensemble, c’est leur conviction personnelle à l’égard de la cause d’un organisme qui motivent le plus les personnes à donner, ainsi que leur sentiment de compassion envers les personnes dans le besoin. À l’échelle nationale, environ sept personnes sur dix sont motivées par le désir de contribuer à leur communauté ou parce qu’elles sont touchées personnellement par la cause ou parce que c’est le cas d’une personne qu’elles connaissent. Environ la moitié d’entre elles donnent parce qu’elles ont été sollicitées par une personne de leur connaissance et un peu moins d’un tiers d’entre elles en raison de leurs croyances religieuses ou spirituelles. C’est le crédit d’impôt pour les dons qui motive le moins les personnes à donner.
                    '''),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Motivations reported by donors.
            html.Div(
                [
                    dcc.Graph(id='MotivationsOverall', style={'marginTop': marginTop}),
                    dcc.Markdown('''
                    Quant à l’incidence de ces motivations éventuelles sur les montants des dons, certaines motivations ont tendance à être associées à des dons beaucoup plus importants que d’autres. Les convictions religieuses et spirituelles semblent être, et de loin, les facteurs les plus significatifs. Bien que les personnes motivées par ce facteur aient tendance à réserver leur soutien à des organismes religieux, elles ont également tendance à donner des montants relativement plus élevés à des causes laïques. Bien que seulement une minorité de personnes déclarent que les crédits d’impôt qu’elles reçoivent constituent un facteur pertinent pour leurs décisions de donner, les personnes motivées par ce facteur ont également tendance à donner des montants nettement plus importants. Au chapitre de certaines motivations plus courantes, les personnes qui donnent par motivation envers une cause ou pour contribuer à la communauté ou par compassion envers les personnes dans le besoin donnent des montants environ deux fois plus supérieurs à ceux des personnes non motivées par ces facteurs. Les relations personnelles avec la cause et donner à la suite d’une sollicitation par une personne amie ou un proche parent sont associés à des différences plus petites dans les montants habituels des dons.
                    '''),
                    # Average amounts contributed by donors reporting and not reporting specific motivations.
                    dcc.Graph(id='MotivationsAvgAmts', style={'marginTop': marginTop}),

                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Personal & economic characteristics
            html.Div(
                [
                    html.H3('Caractéristiques personnelles et économiques'),
                    html.P("Bien que les raisons qui motivent les personnes à donner soient fréquemment très personnelles, elles varient également selon leurs caractéristiques personnelles et économiques. Nous analysons ci-dessous les variations générales des motivations des dons en fonction de certains des facteurs démographiques les plus importants. Là encore, nous présentons dans le texte les tendances générales au niveau national, mais vous pourrez utiliser le menu déroulant pour passer en revue les résultats au niveau régional."),
                    # Gender
                    html.Div([
                        html.H5("Genre"),
                        html.P("À l’échelle nationale, la majorité des motivations incitent davantage les femmes à donner, puisqu’elles signalent plus souvent que ces motivations sont des facteurs importants dans leurs décisions de donner. Par comparaison avec les hommes, les femmes sont particulièrement enclines à donner parce qu’elles sont touchées personnellement ou parce qu’une personne de leur connaissance est touchée personnellement par la cause, par conviction personnelle à l’égard de la cause soutenue par l’organisme ou parce qu’elles ont été sollicitées par quelqu’un qu’elles connaissent. Les différences sont moins prononcées pour les autres motivations. Les crédits d’impôt et les croyances religieuses sont les seules motivations à avoir une incidence comparable pour les hommes comme pour les femmes."),
                        #Donor motivations by gender
                        html.Div([
                            dcc.Graph(id='Motivations-Gndr', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("La probabilité de donner en raison de croyances religieuses ou spirituelles a tendance à augmenter avec l’âge, tandis que l’incidence de facteurs plus laïques, comme la compassion envers les personnes dans le besoin ou la conviction personnelle à l’égard de la cause semble plus uniforme dans les divers groupes d’âge. Être personnellement touché par la cause et les crédits d’impôt gagnent en importance avec l’âge (la deuxième tendance étant vraisemblablement liée aux dons habituellement plus importants des donateurs.trices plus âgés). Donner en réponse à la demande d’une personne de sa connaissance culmine chez les personnes âgées de 45 à 54 ans, puis diminue, tandis que le don pour contribuer à la communauté diminue lentement après la mi-trentaine."),
                        # Donor motivations by age
                        html.Div([
                            dcc.Graph(id='Motivations-Age', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Formal Education
                    html.Div([
                        html.H5("Éducation formelle"),
                        html.P("L’importance d’un petit nombre de motivations va de pair avec celle du niveau d’éducation formelle. À l’échelle nationale, cette tendance est la plus claire pour les dons à la suite de la sollicitation par une connaissance et pour ceux à titre de contribution à la communauté. Le rôle des crédits d’impôt va également de pair avec le niveau d’études, mais principalement chez les titulaires d’un diplôme supérieur au diplôme d’études secondaires. Fait intéressant, les motivations religieuses et spirituelles sont les plus importantes pour les personnes non titulaires du diplôme d’études secondaires et pour les titulaires d’un diplôme universitaire. La conviction à l’égard de la cause, la compassion envers les personnes dans le besoin et le fait d’être personnellement touché par la cause sont des motivations qui ne semblent pas varier beaucoup selon le niveau d’éducation formelle."),
                        # Donor motivations by formal education
                        html.Div([
                            dcc.Graph(id='Motivations-Educ', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # household income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("À l’échelle nationale, seulement quelques motivations varient clairement en fonction du revenu du ménage. Il n’est pas surprenant que l’importance des crédits d’impôt augmente avec le revenu du ménage, mais les facteurs personnels, comme le fait d’être touché par la cause et la sollicitation par une connaissance augmentent également avec le revenu du ménage. La majorité des autres facteurs, comme les motivations religieuses ou spirituelles ou les autres convictions personnelles, ne semblent pas varier fortement selon le revenu."),
                        # Donor motivations by household income
                        html.Div([
                            dcc.Graph(id='Motivations-Inc', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Religious attendance
                    html.Div([
                        html.H5("Pratique religieuse"),
                        html.P("Comme on pouvait s’y attendre, l’importance des motivations religieuses et spirituelles augmente fortement avec l’assiduité aux offices religieux. Cette tendance est également vraie pour les crédits d’impôt (vraisemblablement en raison des dons habituellement plus importants des personnes assidues), ainsi que pour la compassion envers les personnes dans le besoin et le désir de contribuer à la communauté, tout en étant moins forte pour ces deux dernières motivations. Le fait d’être personnellement touché par la cause et la conviction personnelle à l’égard de la cause ne semblent pas varier beaucoup en fonction de la pratique religieuse. De plus, les dons après leur sollicitation par une personne de leur connaissance sont relativement moins fréquents chez les personnes plus assidues aux offices religieux."),
                        # Donor motivations by religious attendance
                        html.Div([
                           dcc.Graph(id='Motivations-Relig', style={'marginTop': marginTop}),
                        ]),
                    ]),
                           
#
                    # Other personal & economic characteristics
                    html.Div([
                        html.H5("Autres facteurs"),
                        html.P("En ce qui concerne les autres caractéristiques, les motivations ne semblent pas varier beaucoup en fonction de la situation d’emploi. Le don après avoir été sollicité par une connaissance constitue la seule exception majeure en étant nettement plus fréquente chez les personnes qui occupent un emploi. L’incidence de la situation matrimoniale est très variée; l’association la plus claire est celle des crédits d’impôt et des motivations religieuses qui semblent avoir plus d’importance pour les personnes mariées ou veuves. Quant au statut d’immigration, les motivations religieuses et spirituelles sont nettement plus importantes pour les personnes naturalisées, tandis que les relations personnelles avec la cause ou la sollicitation par une personne de leur connaissance sont plus importantes pour les personnes nées au Canada."),
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
                        dcc.Graph(id='status-sel', style={'marginTop': marginTop})
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'

            ),
            html.Div(
                [
                    html.Div([
                        html.H4('Causes soutenues',className='mt-3'),
                        html.P("Bien que l’ESG DBP ne recueille pas directement de l’information sur les motivations du soutien de causes précises, la comparaison des motivations des personnes qui soutiennent une cause particulière et de celles qui ne la soutiennent pas peut expliquer ce qui motive les dons au bénéfice de certaines causes. Pour la majorité des motivations et des causes, les personnes qui soutiennent une cause donnée sont également plus susceptibles de faire état d’une motivation particulière que celles qui ne la soutiennent pas. En effet, tout bien considéré, les personnes qui soutiennent une cause donnée ont plus tendance à soutenir de multiples causes et à donner des montants plus importants en général. Les motivations peuvent constituer des facteurs significatifs quand la différence entre leurs caractéristiques personnelles respectives est inhabituellement importante ou quand les partisan.e.s sont moins susceptibles de faire état d’une motivation particulière que les non-partisan.e.s."),
                        html.P("Le graphique ci-dessous montre le pourcentage de donateur.trice.s ayant fait état de chaque motivation, ventilé en fonction de leur don ou de leur abstention de donner au bénéfice de chaque cause particulière. Plusieurs associations se constatent à l’échelle nationale. Par exemple, les personnes qui donnent aux organismes religieux ont plus tendance à faire état de croyances et de convictions religieuses à titre de motivation pour leurs dons, de même que celles qui donnent aux organismes du développement international et de l’aide internationale. Au contraire, les personnes qui donnent aux organismes environnementaux sont légèrement moins susceptibles de faire état de croyances religieuses à titre de motivation. De même, les personnes qui donnent aux organismes du secteur de la santé ont plus tendance à être touchées personnellement par la cause des organismes soutenus ou à donner parce qu’une personne qu’elles connaissent le leur a demandé. Les données sont classées par sous-secteur et vous pourrez choisir soit les données nationales, soit les données régionales."),
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
                        dcc.Graph(id='MotivationsCauses', style={'marginTop': marginTop}),
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
   ),
   footer
])

################## Callbacks #################

@app.callback(
    dash.dependencies.Output('MotivationsOverall', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = Reasons_2018[Reasons_2018['Region'] == region]
    dff = dff[dff["Group"] == "All"]
    title = '{}, {}'.format("Motivations signalées par les donateur.trice.s", region)
    return single_vertical_percentage_graph(dff, title, by="QuestionText", sort=True)

@app.callback(
    dash.dependencies.Output('MotivationsAvgAmts', 'figure'),
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
    dash.dependencies.Output('Motivations-Gndr', 'figure'),
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
    dash.dependencies.Output('Motivations-Age', 'figure'),
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
    dash.dependencies.Output('Motivations-Educ', 'figure'),
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
    dash.dependencies.Output('Motivations-Inc', 'figure'),
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
    dash.dependencies.Output('Motivations-Relig', 'figure'),
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
    dash.dependencies.Output('status-sel', 'figure'),
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
    dash.dependencies.Output('MotivationsCauses', 'figure'),
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
