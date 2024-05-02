import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from utils.gen_navbar import gen_navbar


from utils.graphs.HDC0102_graph_utils_13 import don_rate_avg_don_by_meth, don_rate_avg_don
from utils.data.HDC0102_data_utils_13 import get_data, process_data, get_region_names, get_region_values

from app import app
from homepage import  footer
from .layout_utils import gen_home_button

####################### Data processing ######################
# DonMethAvgDon_2013, DonMethDonRates_2013 = get_data()

# data = [DonMethAvgDon_2013, DonMethDonRates_2013]
# process_data(data)

# region_values = get_region_values()
# region_names = get_region_names()
# method_names = DonMethAvgDon_2013["QuestionText"].unique()
DonMethAvgDon_2013, DonMethDonRates_2013 = get_data()

data = [DonMethAvgDon_2013, DonMethDonRates_2013]
process_data(data)

region_values = get_region_values()
region_names = get_region_names()
method_names = DonMethAvgDon_2013["QuestionText"].unique()
status_names = ['État civil', "Situation d'activité", "Statut d'immigration"]

###################### App layout ######################

marginTop = 20
home_button = gen_home_button(is_2013=True, sat_link=False, bc_link=False)
navbar = gen_navbar("how_do_canadians_donate_2013")

layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1('Comment donne-t-on au Canada? (2013)'),
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
    dbc.Container([
        home_button,
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
                html.Div(["Sélectionnez une méthode de don:",
                        dcc.Dropdown(
                            id='method-selection',
                            options=[{'label': i, 'value': i} for i in method_names],
                            value='Demande par lettre',
                            style={'verticalAlign': 'middle'}
                        ),
                        html.Br(),
                    ], className="m-2 p-2"),
            ])
        ],
        )
            ], className='col-md-10 col-lg-8 mx-auto'),
    ], className='sticky-top select-region mb-2', fluid=True),
   dbc.Container(
       dbc.Row([
            html.Br(),
            # Starting text
            html.Div(
                [
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
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Donation rate & average donation amount by method graph
            html.Div(
                [
                    # html.H4('Forms of Giving'),
                    dcc.Graph(id='DonMethDonRateAvgDonAmt-Method-13', style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Key personal & economic characteristics
            html.Div(
                [
                    html.H3('Caractéristiques personnelles et économiques'),
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
                        # Donation rate & average donation amount by gender
                        html.Div([
                            # html.H6("Donation rate & average donation amount by gender"),
                            dcc.Graph(id='DonMethDonRateAvgDonAmt-Gndr-13', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("""
                       Dans le cadre de la majorité des méthodes de don, la probabilité de donner augmentait pour culminer chez les personnes d’âge moyen avant de diminuer, habituellement chez celles âgées de 65 ans et plus. Les principaux écarts par rapport à cette tendance étaient liés aux dons effectués à un lieu de culte et à la suite de sollicitations par courrier, dont la probabilité augmentait régulièrement avec l’âge dans un cas comme dans l’autre, et aux dons à la suite d’une sollicitation en ligne, dont la probabilité diminuait avec l’âge. En général, les montants moyens des dons avaient tendance à refléter la probabilité de donner (p. ex. quand la probabilité de donner était élevée, le montant moyen des dons l’était également).
                        """),
                        # Donation rate & average donation amount by age
                        html.Div([
                            # html.H6("Donation rate & average donation amount by age"),
                            dcc.Graph(id='DonMethDonRateAvgDonAmt-Age-13', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Formal Education
                    html.Div([
                        html.H5("Éducation formelle"),
                        html.P("""
                        Pratiquement sans exception, la probabilité de donner par n’importe quelle méthode augmentait avec le niveau d’éducation formelle. En règle générale, le montant moyen des dons avait également tendance à augmenter avec le niveau d’études, bien que cette tendance était légèrement moins uniforme que celle de la probabilité de donner.
                        """),
                        # Donation rate & average donation amount by Formal Education
                        html.Div([
                            # html.H6("Donation rate & average donation amount by formal education"),
                            dcc.Graph(id='DonMethDonRateAvgDonAmt-Educ-13', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # household income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("""
                        Comme pour le niveau d’éducation formelle, la probabilité de donner par la majorité des méthodes avait tendance à augmenter avec le revenu du ménage, bien que le montant moyen des dons par chaque méthode était plus variable et n’avait pas tendance à augmenter de manière prévisible en fonction du revenu. La probabilité de donner en mémoire d’une personne, à la suite d’une sollicitation par courrier ou d’un appel à la télévision ou à la radio, dans un lieu de culte, où à la suite d’une sollicitation publique avait tendance à être relativement constante entre les catégories de revenus.
                        """),
                        # Donation rate & average donation amount by household income
                        html.Div([
                            # html.H6("Donation rate & average donation amount by household income"),
                            dcc.Graph(id='DonMethDonRateAvgDonAmt-Inc-13', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Religious attendance
                    html.Div([
                        html.H5("Pratique religieuse"),
                        html.P("""
                        Dans le cadre de la majorité des méthodes de don, la probabilité de donner était légèrement supérieure chez les personnes assistant aux offices religieux au moins deux fois par an. Le montant moyen des dons par certaines méthodes était également supérieur chez les personnes qui y assistent plus fréquemment, mais cette tendance était beaucoup moins uniforme que la tendance de donner. C’est le don à un lieu de culte dont l’association avec la fréquence de la pratique religieuse était la plus forte et la plus nette; la probabilité de donner et les montants moyens des dons augmentaient avec l’assiduité aux offices religieux.
                        """),
                        html.Div([
                            # html.H6("Donation rate & average donation amount by household income"),
                           dcc.Graph(id='DonMethDonRateAvgDonAmt-Relig-13', style={'marginTop': marginTop}),
                        ]),
                    ]),

#
                    # Other personal & economic characteristics
                    html.Div([
                        html.H5("Autres facteurs "),
                        html.P("""
                        Quant aux autres facteurs, les personnes nées au Canada étaient souvent plus enclines à donner par l’une des méthodes de don que les personnes naturalisées. Les dons par le biais d’un lieu de culte, que les personnes nouvellement arrivées étaient plus enclines à employer, constituaient l’exception notable à cette tendance. Aucune tendance claire n’était associée à la situation d’emploi, bien que certaines méthodes de don (p. ex. donner au travail) étaient associées étroitement au travail et que d’autres (p. ex. donner à la suite d’une sollicitation par courriel) étaient associées étroitement à la non-appartenance à la population active. Pour la majorité des méthodes, l’association ne semblait pas tant liée à la situation d’emploi qu’à d’autres caractéristiques personnelles et économiques qui ont tendance à aller de pair avec la situation d’emploi. La situation semble similaire sur le plan de la situation matrimoniale, la majorité des associations semblant davantage liées à l’âge (c.-à-d. les personnes célibataires ont tendance à être plus jeunes, tandis que celles qui sont veuves ont tendance à être plus âgées).
                        """),
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
                        dcc.Graph(id='status-sel-13', style={'marginTop': marginTop}),
                        # Donation rate & average donation amount by religious attendance
                        # html.Div([
                            # html.H6("Donation rate & average donation amount by marital status"),
                            # dcc.Graph(id='DonMethDonRateAvgDonAmt-MarStat-13', style={'marginTop': marginTop}),

                            # html.Br(),
                        # ]),
                        # Donation rate & average donation amount per method by employment status.
                        # html.Div([
                            # html.H6("Donation rate & average donation amount per method by employment status."),
                            # dcc.Graph(id='DonRateAvgDonAmt-Labour-13', style={'marginTop': marginTop}),
                        # ]),
                        # Donation rate & average donation amount by immigration status
                        # html.Div([
                            # html.H6("Donation rate & average donation amount by immigration status"),
                            # dcc.Graph(id='DonMethDonRateAvgDonAmt-ImmStat-13', style={'marginTop': marginTop})

                        # ]),
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'

            ),
        ]),
   ),
   footer
])

################   Graphs  ###################



################ Callbacks ###################
@app.callback(

    dash.dependencies.Output('DonMethDonRateAvgDonAmt-Method-13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])

def update_graph(region):

    dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
    dff1 = dff1[dff1['Group'] == "All"]
    # name1 = "% donating"
    name1 = "Taux de donateur.trice.s"

    dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
    dff2 = dff2[dff2['Group'] == "All"]
    # name2 = "Average amount"
    name2 = "Dons annuels moyens"

    title = '{}, {}'.format("Taux et montant moyen des dons par méthode", region)

    return don_rate_avg_don_by_meth(dff1, dff2, name1, name2, title)

@app.callback(

    dash.dependencies.Output('DonMethDonRateAvgDonAmt-Age-13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('method-selection', 'value')
    ])
def update_graph(region, method):

    dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
    dff1 = dff1[dff1['QuestionText'] == method]
    dff1 = dff1[dff1['Group'] == "Groupe d'âge"]
    # name1 = "% donating"
    name1 = "Taux de donateur.trice.s"


    dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
    dff2 = dff2[dff2['QuestionText'] == method]
    # dff2 = dff2[dff2['Group'] == "Age group"]
    dff2 = dff2[dff2['Group'] == "Groupe d'âge"]
    # name2 = "Average amount"
    name2 = "Dons annuels moyens"


    title = '{}, {}'.format("Taux et montant moyen des dons " + str(method).lower() + " selon l’âge", region)


    return don_rate_avg_don(dff1, dff2, name1, name2, title)

@app.callback(

    dash.dependencies.Output('DonMethDonRateAvgDonAmt-Gndr-13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('method-selection', 'value')
    ])
def update_graph(region, method):
    dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
    dff1 = dff1[dff1['QuestionText'] == method]
    dff1 = dff1[dff1['Group'] == "Genre"]
    dff1 = dff1.replace("Male", "Hommes")
    dff1 = dff1.replace("Female", "Femmes")
    # name1 = "% donating"
    name1 = "Taux de donateur.trice.s"


    dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
    dff2 = dff2[dff2['QuestionText'] == method]
    dff2 = dff2[dff2['Group'] == "Genre"]
    dff2 = dff2.replace("Male", "Hommes")
    dff2 = dff2.replace("Female", "Femmes")
    # name2 = "Average amount"
    name2 = "Dons annuels moyens"


    title = '{}, {}'.format("Taux et montant moyen des dons " + str(method).lower() + " selon le genre", region)


    return don_rate_avg_don(dff1, dff2, name1, name2, title)

@app.callback(
    dash.dependencies.Output('DonMethDonRateAvgDonAmt-MarStat-13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('method-selection', 'value')
    ])
def update_graph(region, method):
    dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
    dff1 = dff1[dff1['QuestionText'] == method]
    dff1 = dff1[dff1['Group'] == "Marital status"]
    name1 = "% donating"


    dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
    dff2 = dff2[dff2['QuestionText'] == method]
    dff2 = dff2[dff2['Group'] == "Marital status"]
    name2 = "Average amount"


    title = '{}, {}'.format("Donation rate & average donation amount per method by marital status", region)


    return don_rate_avg_don(dff1, dff2, name1, name2, title)

@app.callback(

    dash.dependencies.Output('DonMethDonRateAvgDonAmt-Educ-13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('method-selection', 'value')
    ])
def update_graph(region, method):
    dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
    dff1 = dff1[dff1['QuestionText'] == method]
    dff1 = dff1[dff1['Group'] == "Éducation"]
    # name1 = "% donating"
    name1 = "Taux de donateur.trice.s"


    dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
    dff2 = dff2[dff2['QuestionText'] == method]
    dff2 = dff2[dff2['Group'] == "Éducation"]
    # name2 = "Average amount"
    name2 = "Dons annuels moyens"


    title = '{}, {}'.format("Taux et montant moyen des dons " + str(method).lower() + " selon l’éducation", region)


    return don_rate_avg_don(dff1, dff2, name1, name2, title)


@app.callback(

    dash.dependencies.Output('DonMethDonRateAvgDonAmt-Labour-13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('method-selection', 'value')
    ])
def update_graph(region, method):
    dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
    dff1 = dff1[dff1['QuestionText'] == method]
    dff1 = dff1[dff1['Group'] == "Labour force status"]
    # name1 = "% donating"
    name1 = "Taux de donateur.trice.s"


    dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
    dff2 = dff2[dff2['QuestionText'] == method]
    dff2 = dff2[dff2['Group'] == "Labour force status"]
    # name2 = "Average amount"
    name2 = "Dons annuels moyens"


    title = '{}, {}'.format("Donation rate & average donation amount per method by employment status", region)


    return don_rate_avg_don(dff1, dff2, name1, name2, title)

@app.callback(

    dash.dependencies.Output('DonMethDonRateAvgDonAmt-Relig-13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('method-selection', 'value')
    ])
def update_graph(region, method):
    dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
    dff1 = dff1[dff1['QuestionText'] == method]
    dff1 = dff1[dff1['Group'] == "Fréquence de la fréquentation religieuse"]
    # name1 = "% donating"
    name1 = "Taux de donateur.trice.s"


    dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
    dff2 = dff2[dff2['QuestionText'] == method]
    dff2 = dff2[dff2['Group'] == "Fréquence de la fréquentation religieuse"]
    # name2 = "Average amount"
    name2 = "Dons annuels moyens"


    title = '{}, {}'.format("Taux et montant moyen des dons " + str(method).lower() + " selon la pratique religieuse", region)


    return don_rate_avg_don(dff1, dff2, name1, name2, title)

@app.callback(

    dash.dependencies.Output('DonMethDonRateAvgDonAmt-Inc-13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('method-selection', 'value')
    ])
def update_graph(region, method):
    dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
    dff1 = dff1[dff1['QuestionText'] == method]
    dff1 = dff1[dff1['Group'] == "Catégorie de revenu personnel"]
    # name1 = "% donating"
    name1 = "Taux de donateur.trice.s"


    dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
    dff2 = dff2[dff2['QuestionText'] == method]
    dff2 = dff2[dff2['Group'] == "Catégorie de revenu personnel"]
    # name2 = "Average amount"
    name2 = "Dons annuels moyens"


    title = '{}, {}'.format("Taux et montant moyen des dons " + str(method).lower() + " selon le revenu", region)


    return don_rate_avg_don(dff1, dff2, name1, name2, title)

@app.callback(

    dash.dependencies.Output('DonMethDonRateAvgDonAmt-ImmStat-13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('method-selection', 'value')
    ])
def update_graph(region, method):
    dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
    dff1 = dff1[dff1['QuestionText'] == method]
    dff1 = dff1[dff1['Group'] == "Immigration status"]
    name1 = "% donating"


    dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
    dff2 = dff2[dff2['QuestionText'] == method]
    dff2 = dff2[dff2['Group'] == "Immigration status"]
    name2 = "Average amount"


    title = '{}, {}'.format("Donation rate & average donation amount per method by immigration status", region)


    return don_rate_avg_don(dff1, dff2, name1, name2, title)


# @app.callback(

#     dash.dependencies.Output('status-sel-13', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value'),
#         dash.dependencies.Input('method-selection', 'value'),
#         dash.dependencies.Input('status-selection', 'value')
#     ])
# def update_graph(region, method, status):
#     dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
#     dff1 = dff1[dff1['QuestionText'] == method]
#     dff1 = dff1[dff1['Group'] == status]
#     name1 = "Donation rate"


#     dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
#     dff2 = dff2[dff2['QuestionText'] == method]
#     dff2 = dff2[dff2['Group'] == status]
#     name2 = "Average donation"


#     # title = '{}, {}'.format("Donation rate & average donation amount per method by immigration status", region)
#     a = ['At work', 'Online', 'On own', 'In memoriam', 'Door-to-door canvassing']
#     b = ['Mail request', 'Telephone request', 'TV or radio request', 'Sponsoring someone']
#     c = ['Charity event', 'Public place', 'Place of worship']

#     if str(method) in a:
#         title = '{}, {}'.format("Donations made " + str(method).lower() + " by immigration status", region)
#     elif str(method) in b:
#         title = '{}, {}'.format("Donations made by " + str(method).lower() + " by immigration status", region)
#     elif str(method) in c:
#         title = '{}, {}'.format("Donations made at " + str(method).lower() + " by immigration status", region)
#     else:
#         title = '{}, {}'.format(str(method) + " by immigration status", region)

#     return don_rate_avg_don(dff1, dff2, name1, name2, title)

@app.callback(

    dash.dependencies.Output('status-sel-13', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('method-selection', 'value'),
        dash.dependencies.Input('status-selection', 'value')
    ])
def update_graph(region, method, status):
    dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
    dff1 = dff1[dff1['QuestionText'] == method]
    dff1 = dff1[dff1['Group'] == status]
    # name1 = "Donation rate"
    name1 = "Taux de donateur.trice.s"


    dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
    dff2 = dff2[dff2['QuestionText'] == method]
    dff2 = dff2[dff2['Group'] == status]
    name2 = "Dons annuels moyens"
    # name2 = "Average donation"


    title = '{}, {}'.format("Taux et montant moyen des dons " + str(method).lower() + " selon " + str(status).lower(), region)
    # a = ['At work', 'Online', 'On own', 'In memoriam', 'Door-to-door canvassing']
    # b = ['Mail request', 'Telephone request', 'TV or radio request', 'Sponsoring someone']
    # c = ['Charity event', 'Public place', 'Place of worship']

    # if str(method) in a:
    #     title = '{}, {}'.format("Donations made " + str(method).lower() + " by immigration status", region)
    # elif str(method) in b:
    #     title = '{}, {}'.format("Donations made by " + str(method).lower() + " by immigration status", region)
    # elif str(method) in c:
    #     title = '{}, {}'.format("Donations made at " + str(method).lower() + " by immigration status", region)
    # else:
    #     title = '{}, {}'.format(str(method) + " by immigration status", region)

    return don_rate_avg_don(dff1, dff2, name1, name2, title)
