import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd

from utils.home_button import gen_home_button
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc

from utils.graphs.WDC0205_graph_utils import single_vertical_percentage_graph, vertical_hours_graph, vertical_percentage_graph
from utils.data.WDC0205_data_utils_13 import get_data, process_data, get_region_names, get_region_values, translate

from app import app
from homepage import footer #navbar, footer

####################### Data processing ######################
ReasonsVol_2018, AvgHrsReasons_2018, MotivationsVolByCause_2018 = get_data()
data = [ReasonsVol_2018, AvgHrsReasons_2018, MotivationsVolByCause_2018]
process_data(data)

# ReasonsVol_2018 = translate(ReasonsVol_2018)
# AvgHrsReasons_2018 = translate(AvgHrsReasons_2018)
# MotivationsVolByCause_2018 = translate(MotivationsVolByCause_2018)

region_values = get_region_values()
region_names = get_region_names()
cause_names = MotivationsVolByCause_2018["Group"].unique()
motivations_names = ReasonsVol_2018["QuestionText"].unique()
status_names = ['État civil', "Situation d'activité", "Statut d'immigration", "Fréquence de la fréquentation religieuse"]

clean_names = []
for i in motivations_names:
    x = i.replace('<br>', ' ')
    clean_names.append(x)

motivations_names = clean_names

###################### App layout ######################
navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                # dcc.Link("Home", href="/")
                dbc.NavLink("À propos", href="https://www.donetbenevolat.ca/",external_link=True)
            ),
            dbc.NavItem(
                dbc.NavLink("EN", href="http://app.givingandvolunteering.ca/why_do_canadians_volunteer_2013",external_link=True)
            ),
        ],
        brand="Centre Canadien de Connaissances sur les Dons et le Bénévolat",
        brand_href="/",
        color="#4B161D",
        dark=True,
        sticky='top'
    )
marginTop = 20
home_button = gen_home_button()

layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1('Pourquoi fait-on du bénévolat? (2013)'),
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
    # Dropdown menu
    dbc.Container([
        home_button,
        dbc.Row(
           dbc.Col(
               html.Div([
                   "Sélectionnez une région:",
                   dcc.Dropdown(
                       id='region-selection',
                       options=[{'label': region_values[i], 'value': region_values[i]} for i in range(len(region_values))],
                       value='CA',
                       ),
                    html.Br(),
                ],className="m-2 p-2"),
            ),id='sticky-dropdown'),
    ],className='sticky-top bg-light mb-2', fluid=True),
   dbc.Container(
       dbc.Row([
            html.Div(
                [
                    dcc.Markdown("""
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2013, plus de deux personnes sur cinq (44 %) au Canada ont fait du bénévolat pour un organisme de bienfaisance ou à but non lucratif pendant la période d’un an qui l’a précédée. Dans le texte, nous décrivons les résultats au niveau national, mais vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer légèrement par rapport aux résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.
                    """),
                    dcc.Markdown("""
                    Pour mieux comprendre les facteurs susceptibles d’inciter les bénévoles à augmenter leur soutien, on leur a demandé si l’un ou plusieurs de onze facteurs jouaient un rôle important dans leur décision de faire du bénévolat pour l’organisme qui en bénéficiait le plus. Dans l’ensemble, ces personnes étaient les plus enclines à faire du bénévolat pour apporter une contribution à leur communauté, pour mettre leurs compétences et leurs expériences au service d’une bonne cause et parce qu’elles étaient touchées personnellement par la cause de l’organisme ou des organismes qu’elles soutenaient ou parce qu’elles connaissaient une personne dans ce cas. À l’échelle nationale, environ la moitié des bénévoles étaient motivés par le désir d’améliorer leur état de santé ou leur sentiment de bien-être, de prendre conscience de leurs points forts ou de réseauter ou de rencontrer d’autres personnes. Entre un tiers et deux cinquièmes de ces personnes faisaient du bénévolat parce que leurs ami.e.s étaient des bénévoles ou pour soutenir des causes politiques, environnementales ou sociales particulières. Les personnes étaient relativement moins motivées par le fait qu’un membre de leur famille était bénévole ou par le désir d’augmenter leurs possibilités d’emploi ou par leurs obligations ou croyances religieuses.
                    """),
                    # Motivations Reported reported by donors.
                    dcc.Graph(id='MotivationsOverall-13', style={'marginTop': marginTop}),
                    dcc.Markdown("""
                    Certaines motivations avaient tendance à être associées à des dons de temps plus importants que d’autres, les bénévoles motivés par ces facteurs faisant don de plus de temps, en moyenne, que les bénévoles motivés par d’autres facteurs. D’après cette mesure, c’est le désir de mettre en application bénévolement leurs compétences qui avait la plus forte incidence, suivi par le désir de prendre conscience de leurs points forts. À l’inverse, le désir d’augmenter leurs possibilités d’emploi motivait relativement peu les bénévoles et le fait que des personnes amies ou des membres de leur famille étaient bénévoles avait peut-être même une incidence négative sur le nombre habituel d’heures de bénévolat. La comparaison de l’incidence caractéristique sur le nombre d’heures de bénévolat et de la fréquence des diverses motivations permet de conclure que l’incidence des facteurs liés principalement aux autres personnes et à l’avantage déterminant (p. ex. possibilités d’emploi) avait tendance à être inférieure et que celle des facteurs liés à la réalisation de soi et aux convictions personnelles avait tendance à être supérieure.
                    """
                    ),
                    # Average hours contributed by volunteers reporting and not reporting specific motivations
                    dcc.Graph(id='MotivationsAvgHrs_13', style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Personal & economic characteristics
            
            html.Div(
                [
                    # html.H3('Caractéristiques personnelles et économiques'),
                    
                   html.H3('Caractéristiques personnelles et économiques'),
                    html.P("""
                    Bien que les raisons de faire du bénévolat aient tendance à être très personnelles, au niveau de la population, les motivations variaient fréquemment d’une manière relativement prévisible en fonction des caractéristiques personnelles et économiques des bénévoles. Nous analysons ci-dessous les variations tendancielles des motivations des bénévoles en fonction de certains facteurs démographiques parmi les plus importants. Là encore, nous décrivons dans le texte les résultats au niveau national, mais vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les résultats régionaux puissent différer légèrement dans les détails par rapport aux résultats au niveau national décrits dans le texte, les tendances générales étaient généralement très similaires. 
                    """
                    ),
                
                    # Gender
                    html.Div([
                        html.H5("Genre"),
                        html.P("""
                        Dans l’ensemble, les motivations du bénévolat variaient très peu selon le genre. Les hommes et les femmes avaient tendance à réagir d’une manière très similaire à la majorité des motivations. La plupart des différences entre les genres n’étaient pas statistiquement significatives. Pour autant que celles-ci l’étaient, les femmes étaient légèrement plus enclines à faire du bénévolat pour prendre conscience de leurs points forts, tandis que les hommes étaient légèrement plus enclins à être motivés par le fait que leurs ami.e.s faisaient du bénévolat.
                        """),
                        html.Div(["Sélectionnez une motivation:",
                      dcc.Dropdown(
                          id='motivation_selection',
                          options=[{'label': motivations_names[i], 'value': motivations_names[i]} for i in range(len(motivations_names))], # if isinstance(motivations_names[i], str)],
                          value='Touché.e personnellement par la cause',
                          style={'verticalAlign': 'middle'}
                      ),
                      ],
                     className='bg-light m-2 p-2'),
                        # Volunteer motivations by gender
                        html.Div([
                            dcc.Graph(id='Motivations-Gndr-13', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("""
                        L’importance de la majorité des motivations (la probabilité selon laquelle les bénévoles en faisaient état) variait de manière significative avec l’âge. L’importance de l’amélioration des possibilités d’emploi diminuait fortement avec l’âge, contrairement à l’importance d’améliorer son état de santé ou son bien-être qui augmentait avec l’âge, de même que le rôle des obligations ou des croyances religieuses (bien que cette motivation était relativement plus importante chez les personnes de moins de 35 ans que chez celles âgées de 35 à 44 ans). Le fait que des personnes amies étaient des bénévoles ou le désir de réseauter ou de rencontrer d’autres personnes était la motivation la plus répandue chez les bénévoles plus jeunes ou plus âgés, tandis que l’incidence de la relation personnelle avec la cause d’un organisme suivait la tendance inverse, en culminant chez les bénévoles âgés de 35 à 54 ans, pour diminuer ensuite. Enfin, le désir de prendre conscience de leurs points forts ou celui de soutenir une cause politique, environnementale ou sociale était plus importants l’un et l’autre chez les bénévoles de moins de 35 ans.
                        """),
                        html.Div(["Sélectionnez une motivation:",
                            dcc.Dropdown(
                                id='motivation_selection-age',
                                options=[{'label': motivations_names[i], 'value': motivations_names[i]} for i in range(len(motivations_names))],# if isinstance(motivations_names[i], str)],
                                value='Touché.e personnellement par la cause',
                                style={'verticalAlign': 'middle'}
                            ),
                            ],
                     className='bg-light m-2 p-2'),
                        # Volunteer motivations by age
                        html.Div([
                            dcc.Graph(id='Motivations-Age-13', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Formal Education
                    html.Div([
                         html.H5("Éducation formelle"),
                        html.P("""
                        Dans une large mesure, les variations des motivations selon le niveau d’éducation formelle semblent plus liées à l’âge des bénévoles qu’à leur niveau d’éducation formelle en soi. Par exemple, les personnes titulaires tout au plus d’un diplôme d’études secondaires (qui ont tendance à être plus jeunes) étaient plus enclines à faire du bénévolat pour améliorer leurs possibilités d’emploi et pour prendre conscience de leurs points forts. Elles avaient aussi plus tendance à faire du bénévolat parce que des personnes amies et des membres de leurs familles étaient des bénévoles et pour réseauter ou rencontrer d’autres personnes. Tous ces facteurs étaient plus fréquents à la fois chez les jeunes et les personnes plus âgées (moins susceptibles de détenir un diplôme universitaire). Quant aux autres tendances significatives, une relation personnelle avec la cause et le désir d’apporter une contribution à la communauté étaient des motivations qui augmentaient l’une et l’autre avec le niveau d’éducation formelle des bénévoles.
                        """),
                        html.Div(["Sélectionnez une motivation:",
                            dcc.Dropdown(
                                id='motivation_selection-educ',
                                options=[{'label': motivations_names[i], 'value': motivations_names[i]} for i in range(len(motivations_names)) if isinstance(motivations_names[i], str)],
                                value='Touché.e personnellement par la cause',
                                style={'verticalAlign': 'middle'}
                      ),
                      ],
                     className='bg-light m-2 p-2'),
                        # Volunteer motivations by formal education
                        html.Div([
                            dcc.Graph(id='Motivations-Educ-13', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # household income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("""
                        Dans l’ensemble, les motivations pour le bénévolat variaient relativement peu selon le revenu du ménage. Pour autant que des tendances étaient statistiquement significatives, la probabilité de faire du bénévolat pour réseauter ou pour rencontrer d’autres personnes diminuait avec l’augmentation des revenus du ménage, de même que le bénévolat en raison de croyances ou d’obligations religieuses. Fait intéressant, le bénévolat à l’appui d’une cause politique, environnementale ou sociale particulière était relativement plus fréquent chez les ménages au revenu annuel inférieur à 40 000 $.
                        """),
                        html.Div(["Sélectionnez une motivation:",
                            dcc.Dropdown(
                                id='motivation_selection-income',
                                options=[{'label': motivations_names[i], 'value': motivations_names[i]} for i in range(len(motivations_names)) if isinstance(motivations_names[i], str)],
                                value='Touché.e personnellement par la cause',
                                style={'verticalAlign': 'middle'}
                            ),
                            ],
                     className='bg-light m-2 p-2'),
                        # Volunteer motivations by household income
                        html.Div([
                            dcc.Graph(id='Motivations-Inc-13', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Religious attendance
                    # html.Div([
                    #     html.H5("Religious Attendance"),
                    #     html.P("The clearest association between barriers to donating and the frequency of religious attendance is with giving time instead of donating more with more frequent attenders being more likely to report this barrier. Most other barriers do not vary by religious attendance in clear, predictable ways. The most notable exception is that non-attenders and very infrequent attenders are somewhat less likely to give directly to those in need instead of donating to an organization."),
                    #     html.Div(["Sélectionnez une motivation:",
                    #         dcc.Dropdown(
                    #             id='motivation_selection-relig',
                    #             options=[{'label': motivations_names[i], 'value': motivations_names[i]} for i in range(len(motivations_names)) if isinstance(motivations_names[i], str)],
                    #             value='Touché.e personnellement par la cause',
                    #             style={'verticalAlign': 'middle'}
                    #         ),
                    #         ],
                    #  className='bg-light m-2 p-2'),
                    #     # Barriers to giving more by religious attendance
                    #     html.Div([
                    #        dcc.Graph(id='Motivations-Relig-2', style={'marginTop': marginTop}),
                    #     ]),
                    # ]),
                    # Other factors
                    html.Div([
                        html.H5("Autres facteurs "),
                        html.P("""
                        L’augmentation de l’importance de la majorité des motivations semble aller de pair avec celle de l’assiduité aux offices religieux. La corrélation la plus forte était avec les obligations et les croyances religieuses, nettement plus importantes chez les personnes plus assidues, mais cette tendance était également vraie pour plusieurs autres motivations, comme le désir de prendre conscience de leurs points forts ou le bénévolat de membres de leur famille. Bien que la force de cette tendance était parfois faible, seul le bénévolat à l’appui d’une cause politique, environnementale ou sociale ne variait pas en fonction de l’assiduité. Comme dans le cas de l’éducation, de nombreuses variations selon la situation matrimoniale et d’emploi semblent principalement liées à l’âge ou à l’étape de la vie, et sans lien direct avec la situation d’emploi ou matrimoniale. Par exemple, les personnes non membres de la population active (qui sont plus susceptibles d’être très jeunes ou très âgées) étaient plus enclines à faire du bénévolat parce que leurs ami.e.s en faisaient ou pour réseauter ou rencontrer d’autres personnes, de même que les célibataires (qui ont tendance à être très jeunes) ou les personnes veuves (qui ont tendance à être très âgées). Au chapitre du statut d’immigration, les personnes nouvellement arrivées au Canada avaient nettement plus tendance à faire du bénévolat en raison de leurs croyances ou obligations religieuses et étaient relativement plus enclines à soutenir une cause particulière, à prendre conscience de leurs points forts et à réseauter et à rencontrer d’autres personnes.
                        """),
                        # # Volunteer motivations by religious attendance
                        # html.Div([
                        #     dcc.Graph(id='Motivations-Relig-2', style={'marginTop': marginTop}),
                        # ]),
                        # Volunteer motivations by marital status
                        # html.Div([
                        #     dcc.Graph(id='Motivations-Marstat-2', style={'marginTop': marginTop}),
                        # ]),
                        # # Volunteer motivations by labour force status
                        # html.Div([
                        #     dcc.Graph(id='Motivations-Labour-2', style={'marginTop': marginTop})
                        # ]),
                        # # Volunteer motivations by immigration status
                        # html.Div([
                        #     dcc.Graph(id='Motivations-Immstat-2', style={'marginTop': marginTop})
                        # ]),
                        html.Div([
                            html.Div(['Sélectionner le statut:',
                                      dcc.Dropdown(
                                          id='status-selection',
                                          options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                                          value='État civil',
                                          style={'verticalAlign': 'middle'}
                                      ),],
                                     style={'width': '33%', 'display': 'inline-block'}),
                          html.Div(['Sélectionnez une motivation:',
                                      dcc.Dropdown(
                                          id='motivation_selection-other',
                                          options=[{'label': motivations_names[i], 'value': motivations_names[i]} for i in range(len(motivations_names)) if isinstance(motivations_names[i], str)],
                                value='Touché.e personnellement par la cause',
                                          style={'verticalAlign': 'middle'}
                                      ),],
                                     style={'width': '66%', 'display': 'inline-block'}),
                            
                        ]),
                        dcc.Graph(id='status-selfr-13', style={'marginTop': marginTop})
             
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'

            ),
            html.Div(
                [
                    html.Div([
                        html.H3("Causes soutenues "),
                        html.P("""
                        Le graphique ci-dessous montre les pourcentages de bénévoles qui ont fait état de chaque motivation, subdivisés en fonction de leur bénévolat ou de leur absence de bénévolat pour la cause particulière sélectionnée. À l’échelle nationale, plusieurs associations se constatent. Par exemple, les bénévoles des organismes du secteur de la santé et des hôpitaux étaient nettement plus susceptibles de déclarer être touchés personnellement par la cause de l’organisme ou de connaître une personne qui l’était. Les bénévoles des organismes religieux étaient particulièrement enclins à être motivés par leurs convictions religieuses, par le fait qu’un membre de leur famille faisait du bénévolat et par le désir de prendre conscience de leurs points forts et de mettre leurs compétences au service d’une cause digne de leur soutien. Les bénévoles des organismes de protection de l’environnement, des organismes du développement international et de l’aide internationale, ainsi que des organismes de plaidoyer étaient tous particulièrement susceptibles de déclarer faire du bénévolat pour soutenir une cause politique, environnementale ou sociale. 
                        """),
                        html.Div(["Sélectionnez une cause:",
                            dcc.Dropdown(
                                id='cause-selection',
                                options=[{'label': cause_names[i], 'value': cause_names[i]} for i in range(len(cause_names))],
                                value='Arts et culture',
                                style={'verticalAlgin': 'middle'}
                            ),
                        ],
                        className='bg-light m-2 p-2'),
                        # Percentages of cause supporters and non-supporters reporting each motivation, by cause
                        dcc.Graph(id='MotivationsCauses-13', style={'marginTop': marginTop}),
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
   ),
   footer
])

################ CALLBACKS ################

@app.callback(
    dash.dependencies.Output('MotivationsOverall-13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = ReasonsVol_2018[ReasonsVol_2018['Region'] == region]
    dff = dff[dff["Group"] == "All"]
    title = '{}, {}'.format("Motivations signalées par les bénévoles", region)
    return single_vertical_percentage_graph(dff, title, by="QuestionText", sort=True)

@app.callback(
    dash.dependencies.Output('MotivationsAvgHrs_13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    df = AvgHrsReasons_2018[AvgHrsReasons_2018['Region'] == region]
    df["Group"] = df["Group"].str.wrap(30)
    df["Group"] = df["Group"].replace({'\n': '<br>'}, regex=True)
    df = df.replace("Report motivation", "Signalent une motivation")
    df = df.replace("Do not report motivation", "Ne signalent aucune motivation")
    
    name1 = "Signalent une motivation"
    # name1 = "Report motivation"
    name2 = "Ne signalent aucune motivation"
    # name2 = "Do not report motivation"
    title = '{}, {}'.format("Nombre moyen d’heures de bénévolat pour les bénévoles faisant état ou non de motivations précises", region)
    return vertical_hours_graph(df, name1, name2, title)


@app.callback(
    dash.dependencies.Output('Motivations-Gndr-13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('motivation_selection', 'value')

    ])
def update_graph(region, motivation):
    dff = ReasonsVol_2018[ReasonsVol_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == "Genre"]
    dff = dff.replace("Male", "Hommes")
    dff = dff.replace("Female", "Femmes")
    dff = dff[dff["QuestionText"] == motivation]
    title = '{}, {}'.format("La motivation des bénévoles: " + str(motivation) + " selon le genre", region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('Motivations-Age-13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('motivation_selection-age', 'value')

    ])
def update_graph(region, motivation):
    dff = ReasonsVol_2018[ReasonsVol_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == "Groupe d'âge"]
    dff = dff[dff["QuestionText"] == motivation]
    title = '{}, {}'.format("La motivation des bénévoles: " + str(motivation) + " selon l’âge", region)
    return single_vertical_percentage_graph(dff, title)


@app.callback(
    dash.dependencies.Output('Motivations-Educ-13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('motivation_selection-educ', 'value')

    ])
def update_graph(region, motivation):
    dff = ReasonsVol_2018[ReasonsVol_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == "Éducation"]
    dff = dff[dff["QuestionText"] == motivation]
    title = '{}, {}'.format("La motivation des bénévoles: " + str(motivation) + " selon l’éducation formelle", region)
    return single_vertical_percentage_graph(dff, title)


@app.callback(
    dash.dependencies.Output('Motivations-Inc-13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('motivation_selection-income', 'value')

    ])
def update_graph(region, motivation):
    dff = ReasonsVol_2018[ReasonsVol_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == "Catégorie de revenu familial"]
    dff = dff[dff["QuestionText"] == motivation]
    title = '{}, {}'.format("La motivation des bénévoles: " + str(motivation) + " <br> selon le revenu du ménage", region)
    return single_vertical_percentage_graph(dff, title)


@app.callback(
    dash.dependencies.Output('status-selfr-13', 'figure'),
    [ 
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('motivation_selection-other', 'value'),
        dash.dependencies.Input('status-selection', 'value')
    ])

def update_graph(region, motivation, status):
    dff = ReasonsVol_2018[ReasonsVol_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == status]
    dff = dff[dff["QuestionText"] == motivation]
    title = '{}, {}'.format("La motivation des bénévoles: " + str(motivation) + ' selon ' + str(status).lower(), region)
    return single_vertical_percentage_graph(dff, title)





@app.callback(
    dash.dependencies.Output('MotivationsCauses-13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('cause-selection', 'value')
    ])
def update_graph(region, cause):
    dff = MotivationsVolByCause_2018[MotivationsVolByCause_2018['Region'] == region]
    dff = dff[dff["Group"] == cause]
    dff = dff.replace("Support cause", "Soutiennent la cause")
    dff = dff.replace("Do not support cause", "Ne soutiennent pas la cause")
    
    # name1 = "Support cause"
    name1 = "Soutiennent la cause"
    # name2 = "Do not support cause"
    name2 = "Ne soutiennent pas la cause"
    
    title = '{}, {}'.format("Pourcentages de partisan.e.s et de non-partisan.e.s d’une cause faisant état de chaque motivation, selon la cause", region)
    return vertical_percentage_graph(dff, title, name1, name2)




