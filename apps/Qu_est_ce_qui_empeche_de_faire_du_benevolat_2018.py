import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc
import os
import os.path as op
import textwrap

from utils.graphs.WKC0206_graph_utils import vertical_percentage_graph_volunteers, vertical_hours_graph, vertical_percentage_graph
from utils.data.WKC0206_data_utils import get_data, process_data, get_region_names, get_region_values

from app import app
from homepage import footer #navbar, footer

####################### Data processing ######################
BarriersVol_2018, BarriersVolMore_2018, AvgHoursBarriersVol_2018, BarriersVolByCause_2018= get_data()

data = [BarriersVol_2018, BarriersVolMore_2018, AvgHoursBarriersVol_2018, BarriersVolByCause_2018]
process_data(data)

cause_names = BarriersVolByCause_2018["Group"].unique()
barriers_names = BarriersVol_2018["QuestionText"].unique()
region_values = get_region_values()
region_names = get_region_names()
status_names = ['État civil', 'Fréquence de la fréquentation religieuse', "Statut d'immigration"]

###################### App layout ######################
navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                # dcc.Link("Home", href="/")
                dbc.NavLink("À propos", href="https://www.donetbenevolat.ca/",external_link=True)
            ),
            dbc.NavItem(
                dbc.NavLink("EN", href="http://app.givingandvolunteering.ca/What_keeps_Canadians_from_volunteering_2018",external_link=True)
            ),
        ],
        brand="Don et Benevolat",
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
                        html.H1('Qu’est-ce qui empêche de faire du bénévolat?'),
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
    #  Dropdown menu
    dbc.Container([
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
    ],className='sticky-top bg-light mb-2', fluid=True),
   dbc.Container(
       dbc.Row([
            html.Div(
                [
                    dcc.Markdown('''
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, un peu plus de deux personnes sur cinq au Canada (41 %) au Canada ont fait du bénévolat pour un organisme de bienfaisance ou à but non lucratif pendant l’année qui l’a précédée. Nous analysons ci-dessous les facteurs qui ont peut-être dissuadé des personnes de faire du bénévolat. Nous décrivons dans le texte les résultats au niveau national; pour obtenir plus de précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer légèrement par rapport aux résultats au niveau national décrits dans le texte, les tendances générales sont très similaires.
                    ''',className='mt-4'),
                    dcc.Markdown('''
                    Afin de mieux comprendre les facteurs susceptibles de limiter le soutien des personnes au Canada, on a demandé aux bénévoles et aux non-bénévoles si, parmi douze facteurs différents, un ou plusieurs de ceux-ci les empêchaient soit de faire don de plus d’heures qu’ils l’auraient fait autrement (bénévoles), soit de faire du bénévolat (non-bénévoles).
                    '''),
                    dcc.Markdown('''
                    À l’échelle nationale, les freins les plus importants au bénévolat, dans la mesure où de nombreuses personnes les signalent, sont liés au temps. Le manque de temps était le frein signalé le plus souvent, suivi par l’impossibilité de s’engager à long terme à faire du bénévolat. Pour les bénévoles, le sentiment d’avoir déjà fait suffisamment don de leur temps est le troisième frein par ordre d’importance (au niveau national), bien qu’il soit légèrement moins important pour les non-bénévoles. Les coûts financiers liés au bénévolat et l’insatisfaction à l’égard des expériences de bénévolat passées sont les freins les moins courants, tous les autres freins se situant entre ces extrêmes.
                    '''),
                    # Barriers to volunteering, volunteers & non-volunteers
                    dcc.Graph(id='BarriersVolOverall', style={'marginTop': marginTop}),
                    dcc.Markdown('''
                    Habituellement, les bénévoles qui signalent un frein particulier ont tendance à faire don de moins d’heures que les personnes qui ne signalent pas ce frein. Parmi les freins les plus lourds de conséquences, en raison de leur corrélation avec les plus grandes différences dans le nombre moyen d’heures de bénévolat, citons le don d’argent de préférence au bénévolat et la difficulté à s’engager à long terme. Les autres difficultés importantes ont trait à l’efficacité de la mobilisation des bénévoles (comme le montrent les différences importantes associées à ne pas savoir comment s’engager davantage et l’absence de sollicitation pour faire plus de bénévolat) et à la nature des tâches confiées aux bénévoles (ne pas avoir l’occasion de mettre en application ses compétences et l’absence de sollicitation en vue d’un engagement qui importe à la personne sollicitée).
                    '''),
                    dcc.Markdown('''
                    Il est important de comprendre que, bien que ces freins réduisent effectivement le nombre d’heures de bénévolat, ils ne sont pas tous associés à des contributions horaires inférieures en nombre absolu, puisque certains d’entre eux sont associés à des bénévoles qui font don d’un nombre d’heures supérieur à la moyenne. Par exemple, les bénévoles qui limitent leur nombre d’heures de bénévolat en croyant y avoir déjà consacré suffisamment de temps ont tendance à faire don de plus d’heures de bénévolat, comme les personnes qui trouvent que le coût financier du bénévolat constitue un frein, de même que celles ayant des problèmes de santé. Cela ne veut pas dire que ces facteurs ne freinent pas le bénévolat, mais seulement que les bénévoles qui font don de moins d’heures sont moins influencés par ceux-ci.
                    '''),
                    # Average hours contributed by volunteers reporting and not reporting specific motivations
                    dcc.Graph(id='BarriersVolAvgHrs', style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Personal & economic characteristics
            html.Div(
                [
                    html.H3('Caractéristiques personnelles et économiques'),
                    html.P("""
                    Bien que les freins au bénévolat soient nombreux et variés, la réaction des personnes au Canada face à ces freins a tendance à varier selon leurs caractéristiques personnelles et économiques. Nous analysons ci-dessous comment les freins au bénévolat ont tendance à varier selon certains des facteurs démographiques parmi les plus importants. Là encore, nous présentons dans le texte les résultats au niveau national, mais vous pourrez utiliser le menu déroulant pour passer en revue les résultats au niveau régional.
                    """),
                    
                    html.Div([
                        html.H5("Genre"),
                        html.P("""
                        À l’échelle nationale, les hommes sont légèrement plus enclins que les femmes à ne pas faire de bénévolat ou à limiter leurs heures de bénévolat parce que personne ne les a sollicités, parce qu’ils ne savent pas comment s’engager, parce qu’ils n’ont pas l’occasion de mettre en application leurs compétences et leurs expériences ou parce qu’ils sont mécontents d’expériences de bénévolat passées. Plus particulièrement parmi les non-bénévoles, les hommes ont relativement plus tendance à ne pas faire de bénévolat par manque d’intérêt ou parce que personne ne leur a demandé d’apporter une contribution qui leur importe. En revanche, les femmes sont légèrement plus enclines que les hommes à ne pas faire de bénévolat ou à limiter leurs heures de bénévolat en raison de problèmes de santé ou par manque de temps. Les hommes et les femmes sont à peu près tout aussi susceptibles de signaler la majorité des autres freins au bénévolat.
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
                            dcc.Graph(id='BarriersVol-Gndr', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("""
                         Au fur et à mesure que les personnes prennent de l’âge, elles sont moins susceptibles de ne pas faire de bénévolat (ou de limiter leurs heures de bénévolat) parce que personne ne leur a demandé de faire du bénévolat ou d’en faire plus, parce qu’elles ne savent pas comment s’engager ou parce qu’elles ne peuvent pas mettre en application leurs compétences ou leurs expériences. À l’échelle nationale, à partir de l’âge de 45 ans, le frein du manque de temps perd régulièrement de son importance, bien que les problèmes de santé ou la conviction d’avoir déjà fait suffisamment de bénévolat augmentent avec l’âge (de même que le manque d’intérêt des bénévoles pour augmenter leurs activités). Les coûts financiers du bénévolat semblent particulièrement problématiques pour les non-bénévoles âgés de 25 à 34 ans, mais ce frein perd de son importance avec l’âge. 
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
                            dcc.Graph(id='BarriersVol-Age', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Formal Education
                    html.Div([
                        html.H5("Éducation formelle"),
                        html.P("""
                        Les bénévoles non titulaires du diplôme de fin d’études secondaires ont légèrement plus tendance à limiter leurs heures de bénévolat parce qu’ils ne savent pas comment s’engager ou parce que personne ne leur a demandé d’en faire plus. Les bénévoles comme les non-bénévoles non titulaires du diplôme de fin d’études secondaires sont plus enclins à penser avoir déjà consacré suffisamment de temps au bénévolat. Pour les bénévoles comme pour les non-bénévoles, le manque de temps et les dons d’argent de préférence au bénévolat sont des freins qui prennent plus d’importance avec les niveaux d’éducation formelle supérieurs, de même que l’impossibilité de s’engager à long terme pour les non-bénévoles. Enfin, exclusivement pour les non-bénévoles, les coûts financiers du bénévolat et le manque d’intérêt perdent de leur importance et l’impossibilité de mettre en application leurs compétences ou leurs expériences ou celle de s’engager d’une manière qui leur importe sont des freins qui prennent plus d’importance aux yeux des personnes aux niveaux d’études supérieurs.
                        """),
                        # Barriers to volunteering by formal education
                        html.Div([
                    "Sélectionnez une barrière:",
                        dcc.Dropdown(
                          id='barrier-selection-educ',
                          options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(len(barriers_names))],
                          value='Assez de temps déjà donné',
                          style={'verticalAlgin': 'middle'}
                      ),
                      ],className="m-2 p-2"),
                        html.Div([
                            dcc.Graph(id='BarriersVol-Educ', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # household income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("""
                        L’augmentation de leur revenu rend les bénévoles et les non-bénévoles plus susceptibles de faire état de leur manque de temps pour faire du bénévolat, mais moins susceptibles de faire face à des difficultés liées aux coûts financiers du bénévolat ou aux problèmes de santé. L’augmentation de leur revenu rend les non-bénévoles moins susceptibles de croire avoir déjà consacré suffisamment de temps au bénévolat, tandis que les bénévoles dans ce cas sont plus enclins à préférer donner de l’argent.
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
                            dcc.Graph(id='BarriersVol-Inc', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Labour force status.
                    html.Div([
                        html.H5("Situation d’emploi"),
                        html.P("""
                        Quelques-unes de ces tendances semblent principalement liées à l’âge. Par exemple, les personnes qui ne sont pas membres de la population active (généralement plus âgées) ont plus tendance à croire avoir déjà consacré suffisamment de temps au bénévolat, à avoir des problèmes de santé ou à n’avoir aucun intérêt pour faire davantage de bénévolat. D’autres tendances semblent plus directement liées à la situation d’emploi; les personnes au chômage ayant plus tendance à avoir de la difficulté à savoir comment s’engager ou à assumer les coûts financiers du bénévolat et moins tendance à donner de l’argent de préférence à faire don de leur temps. Les bénévoles qui ne sont pas membres de la population active sont beaucoup plus susceptibles d’avoir de la difficulté à s’engager à long terme."""),
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
                           dcc.Graph(id='BarriersVol-Labour', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Other factors
                    html.Div([
                        html.H5("Autres facteurs"),
                        html.P("""
                        Tout comme pour la situation d’emploi, la variation selon la situation matrimoniale semble en grande partie réellement liée à l’âge. Par exemple, les célibataires (généralement plus jeunes) ont plus tendance à dire que personne ne leur a demandé de faire du bénévolat ou d’en faire plus et à ne pas savoir comment s’engager. Au contraire, les personnes veuves (généralement plus âgées) ont plus tendance à faire état de problèmes de santé et à croire avoir déjà consacré suffisamment d’heures au bénévolat. Dans l’ensemble, les freins au bénévolat ne semblent pas varier beaucoup selon l’assiduité aux offices religieux. Dans la mesure où une tendance nette se dessine, certains freins sont légèrement plus importants pour les non-bénévoles assidus aux offices religieux, comme les coûts financiers du bénévolat et les dons d’argent de préférence au bénévolat. Enfin, de nombreux freins créent une difficulté supérieure pour les personnes naturalisées, surtout pour les non-bénévoles, comme l’absence de sollicitation, ne pas savoir comment s’engager, le manque de temps et les coûts financiers du bénévolat, entre autres.
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
                                        dcc.Graph(id='status-sel-volbarrier', style={'marginTop': marginTop})

                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'

            ),
            html.Div(
                [
                    html.Div([
                        html.H4('Causes soutenues',className='mt-3'),
                        html.P("""
                        Bien que l’ESG DBP ne recueille pas directement de l’information sur les freins qui empêchent les bénévoles de faire don de plus de temps à chaque cause, la comparaison des freins auxquels les personnes qui soutiennent et celles qui ne soutiennent pas une cause particulière font face peut nous éclairer. Le graphique ci-dessous montre les pourcentages de bénévoles qui ont fait état de chaque frein, subdivisés en fonction de leur bénévolat ou de leur absence de bénévolat au service d’une cause donnée.
                        """),
                        html.P("""
                        À l’échelle nationale, plusieurs associations se constatent. Par exemple, le manque de temps semble être particulièrement important pour les bénévoles des organismes d’éducation et de recherche, et des universités et des collèges, tandis que les bénévoles des organismes des secteurs des arts et de la culture, du développement et du logement, et des sports et des loisirs sont tous particulièrement enclins à penser avoir fait suffisamment don de leur temps. Les bénévoles des organismes des secteurs du développement international et de l’aide internationale, et de la santé sont tous plus enclins à donner de l’argent de préférence à faire don de plus de temps. Les bénévoles des universités et des collèges, en revanche, ont moins tendance à déclarer n’avoir aucun intérêt pour faire plus de bénévolat et les bénévoles du secteur des arts et de la culture ont moins tendance à être dans l’impossibilité de s’engager à long terme pour faire du bénévolat.
                        """),
                        html.Div(["Sélectionnez une cause:",
                      dcc.Dropdown(
                          id='cause-selection',
                          options=[{'label': cause_names[i], 'value': cause_names[i]} for i in range(len(cause_names))],
                          value='Arts et culture',
                          style={'verticalAlign': 'middle'}
                      ),
                      ],className="m-2 p-2"),
                        # Percentages of cause supporters and non-supporters reporting each barrier, by cause
                        dcc.Graph(id='BarriersVolCauses', style={'marginTop': marginTop}),
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
   ),
   footer
])

################### CALLBACKS ###################

@app.callback(
    dash.dependencies.Output('BarriersVolOverall', 'figure'),
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
    dash.dependencies.Output('BarriersVolAvgHrs', 'figure'),
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
    dash.dependencies.Output('BarriersVol-Gndr', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection', 'value')

    ])
def update_graph(region, barrier):
    dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
    dff["Attribute"] = dff["Attribute"].str.wrap(20)
    dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
    dff = dff[dff['Region'] == region]
    dff = dff[dff["Group"] == "Genre"]
    dff = dff[dff["QuestionText"] == barrier]
    title = '{}, {}'.format("Barrière de bénévoles: " + str(barrier) + " selon le genre", region)
    return vertical_percentage_graph_volunteers(dff, title)


@app.callback(
    dash.dependencies.Output('BarriersVol-Age', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection-age', 'value')

    ])
def update_graph(region, barrier):
    dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
    dff["Attribute"] = dff["Attribute"].str.wrap(20)
    dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
    dff = dff[dff['Region'] == region]
    dff = dff[dff["Group"] == "Groupe d'âge"]
    dff = dff[dff["QuestionText"] == barrier]
    title = '{}, {}'.format("Barrière de bénévoles: " + str(barrier) + " selon l’âge", region)
    return vertical_percentage_graph_volunteers(dff, title)


@app.callback(
    dash.dependencies.Output('BarriersVol-Educ', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection-educ', 'value')

    ])
def update_graph(region, barrier):
    dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
    dff["Attribute"] = dff["Attribute"].str.wrap(20)
    dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
    dff = dff[dff['Region'] == region]
    dff = dff[dff["Group"] == "Éducation"]
    dff = dff[dff["QuestionText"] == barrier]
    title = '{}, {}'.format("Barrière de bénévoles: " + str(barrier) + " selon l’éducation formelle", region)
    return vertical_percentage_graph_volunteers(dff, title)


@app.callback(
    dash.dependencies.Output('BarriersVol-Inc', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection-income', 'value')

    ])
def update_graph(region, barrier):
    dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
    dff["Attribute"] = dff["Attribute"].str.wrap(20)
    dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
    dff = dff[dff['Region'] == region]
    dff = dff[dff["Group"] == "Catégorie de revenu familial"]
    dff = dff[dff["QuestionText"] == barrier]
    title = '{}, {}'.format("Barrière de bénévoles: " + str(barrier) + " selon le revenu", region)
    return vertical_percentage_graph_volunteers(dff, title)

@app.callback(
    dash.dependencies.Output('BarriersVol-Labour', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection-labour', 'value')

    ])
def update_graph(region, barrier):
    dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
    dff["Attribute"] = dff["Attribute"].str.wrap(20)
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
#     dff["Attribute"] = dff["Attribute"].str.wrap(20)
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
#     dff["Attribute"] = dff["Attribute"].str.wrap(20)
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
#     dff["Attribute"] = dff["Attribute"].str.wrap(20)
#     dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
#     dff = dff[dff['Region'] == region]
#     dff = dff[dff["Group"] == status]
#     dff = dff[dff["QuestionText"] == barrier]
#     title = '{}, {}'.format("Barriers to volunteering by immigration status", region)
#     return vertical_percentage_graph_volunteers(dff, title)

@app.callback(
    dash.dependencies.Output('status-sel-volbarrier', 'figure'),
    [ 
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection-other', 'value'),
        dash.dependencies.Input('status-selection-volbarrier', 'value')
    ])

def update_graph(region, barrier, status):
    dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
    # dff["Attribute"] = dff["Attribute"].str.wrap(20)
    # dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
    dff = dff[dff['Region'] == region]
    dff = dff[dff["Group"] == status]
    dff = dff[dff["QuestionText"] == barrier]
    title = '{}, {}'.format("Barrière de bénévoles: " + str(barrier).lower() + '<br>' + ' selon ' + str(status).lower(), region)
    return vertical_percentage_graph_volunteers(dff, title)



@app.callback(
    dash.dependencies.Output('BarriersVolCauses', 'figure'),
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
