import dash
from dash import dcc, html
import dash_bootstrap_components as dbc


from utils.graphs.HDC0102_graph_utils import don_rate_avg_don_by_meth, don_rate_avg_don
from utils.data.HDC0102_data_utils import get_data, process_data, get_region_names, get_region_values

from app import app
from homepage import footer #navbar, footer

####################### Data processing ######################
DonMethAvgDon_2018, DonMethDonRates_2018 = get_data()

data = [DonMethAvgDon_2018, DonMethDonRates_2018]

# translate_data(data)
process_data(data)

region_values = get_region_values()
region_names = get_region_names()
method_names = DonMethAvgDon_2018["QuestionText"].unique()

status_names = ['État civil', "Situation d'activité", "Statut d'immigration"]

###################### App layout ######################
navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                # dcc.Link("Home", href="/")
                dbc.NavLink("Home", href="/",external_link=True)
            ),
            dbc.NavItem(
                dbc.NavLink("EN", href="http://app.givingandvolunteering.ca/How_do_Canadians_donate_2018",external_link=True)
            ),
        ],
        brand="Don et Benevolat",
        brand_href="/",
        color="#c7102e",
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
                        html.H1('Comment donne-t-on au Canada?'),
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
    dbc.Container([
        dbc.Row([
           dbc.Col(
               html.Div([
                   "Sélectionnez une région:",
                   dcc.Dropdown(
                       id='region-selection',
                       options=[{'label': region_names[i], 'value': region_values[i]} for i in range(len(region_values))],
                       value='CA',
                       ),
                    html.Br(),
                ],className="m-2 p-2"),
            ),
           dbc.Col(
               html.Div([
                   "Sélectionnez une méthode de don:",
                   dcc.Dropdown(
                      id='method-selection',
                      options=[{'label': i, 'value': i} for i in method_names],
                      value='Au travail',
                      style={'verticalAlign': 'middle'}
                  ),
                    html.Br(),
                ],className="m-2 p-2"),
            )]),
    ],className='sticky-top bg-light mb-2', fluid=True),
   dbc.Container(
       dbc.Row([
            html.Br(),
            # Starting text
            html.Div(
                [
                    dcc.Markdown('''
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, à peine plus de deux tiers des personnes (68 %) au Canada ont fait un don à un organisme de bienfaisance ou à but non lucratif pendant l’année qui l’a précédée. Chacune d’elles a donné en moyenne 569 $ et le total national des dons s’est chiffré approximativement à 11,9 milliards $. Pour obtenir des précisions sur les variations des montants des dons en fonction des caractéristiques personnelles et par province, veuillez vous reporter à [*Qui donne et combien?*](/WDA0101_fr) sur ce site Web.
                    '''),
                    dcc.Markdown('''
                    Nous décrivons ci-dessous les méthodes employées par les personnes au Canada pour donner. Dans le texte, nous décrivons les résultats au niveau national et vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer légèrement par rapport aux résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.
                                 '''),
                    dcc.Markdown('''
                    Les personnes donnent de nombreuses façons différentes au Canada. À l’échelle nationale, elles donnent le plus souvent à la suite d’une sollicitation en public (comme dans la rue ou dans un centre commercial), en assistant aux offices religieux ou en parrainant une personne qui participe à un événement. Elles donnent le moins souvent à la suite d’une sollicitation au téléphone ou d’une publicité ou d’un événement télévisé ou radiophonique. Les donateur.trice.s ont tendance à donner des montants très différents par les différentes méthodes. C’est quand on les sollicite dans un lieu public, au porte-à-porte ou pour parrainer une personne qui participe à un événement qu’elles ont tendance à donner très peu, bien que toutes ces méthodes soient toutes très courantes. Les personnes donnent habituellement des montants beaucoup plus importants dans un lieu de culte ou après avoir pris contact avec des organismes de leur propre initiative.
                    '''),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Donation rate & average donation amount by method graph
            html.Div(
                [
                    # html.H4('Forms of Giving'),
                    dcc.Graph(id='DonMethDonRateAvgDonAmt-Method', style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Key personal & economic characteristics
            html.Div(
                [
                    html.H3('Caractéristiques personnelles et économiques'),
                    html.P("Les méthodes que les personnes emploient pour donner au Canada et les montants qu’elles ont tendance à donner varient selon leurs caractéristiques personnelles et économiques. Nous montrons ci-dessous les variations de la probabilité de donner et du montant moyen donné selon des caractéristiques clés, dont le genre, l’âge, le niveau d’éducation formelle, le revenu du ménage et l’assiduité aux offices religieux. Nous décrivons, là encore, des tendances générales au niveau national dans le texte, mais vous pourrez prendre connaissance des résultats régionaux en utilisant le menu déroulant."),
                    #html.Ul([
                     #   html.Li('Likelihood of donating via a given method, and'),
                      #  html.Li('Average amount contributed by that method.'),
                    #]),
                    html.P("In the text, we describe general patterns at the national level. Readers can manipulate the interactive graphs to explore levels of support via any given method at both the national and regional levels."),
                    # Gender
                    html.Div([
                        html.H5("Genre"),
                        html.P("Dans le cadre de la majorité des méthodes de don, les femmes sont légèrement plus enclines à donner que les hommes, bien qu’ayant tendance à donner des montants légèrement inférieurs. Les différences dans le montant moyen des dons par n’importe quelle méthode ne sont généralement pas assez importantes pour être statistiquement significatives à 0,05, mais cette tendance est identique dans presque toutes les méthodes de don."),
                        # Donation rate & average donation amount by gender
                        html.Div([
                            # html.H6("Donation rate & average donation amount by gender"),
                            dcc.Graph(id='DonMethDonRateAvgDonAmt-Gndr', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("En général, la probabilité de donner par une méthode de don particulière augmente avec l’âge. C’est vrai pour les dons par courrier, pour les dons à la suite d’une sollicitation téléphonique ou après une publicité ou un événement télévisé ou radiophonique, pour les dons en mémoire d’une personne, à un lieu de culte et pour parrainer une personne qui participe à un événement. Ce n’est que pour les dons en ligne que la probabilité de donner a tendance à diminuer avec l’âge. Les pourcentages de personnes au Canada qui donnent de leur propre initiative, en assistant à une activité de bienfaisance ou à la suite d’une sollicitation dans un lieu public sont relativement constants dans tous les groupes d’âge. Enfin, donner à son lieu de travail et en réponse à une sollicitation au porte-à-porte sont les plus fréquents chez les personnes d’âge moyen et moins fréquents à la fois chez les jeunes et chez les personnes âgées. Pour la majorité des méthodes de don, les montants moyens des dons ne sont pas suffisamment différents entre les groupes d’âge pour être statistiquement significatifs. Dans la mesure où on peut se fier à une tendance, les personnes plus âgées ont tendance à donner plus que les plus jeunes."),
                        # Donation rate & average donation amount by age
                        html.Div([
                            # html.H6("Donation rate & average donation amount by age"),
                            dcc.Graph(id='DonMethDonRateAvgDonAmt-Age', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Formal Education
                    html.Div([
                        html.H5("Éducation Formelle"),
                        html.P("Pratiquement sans exception, la probabilité de donner par n’importe quelle méthode augmente avec le niveau d’éducation formelle, de même que le montant habituel des dons. Seuls les dons en réponse à une publicité télévisée ou radiophonique ou à la suite d’une sollicitation dans un lieu public ou dans un lieu de culte s’écartent de cette tendance."),
                        # Donation rate & average donation amount by Formal Education
                        html.Div([
                            # html.H6("Donation rate & average donation amount by formal education"),
                            dcc.Graph(id='DonMethDonRateAvgDonAmt-Educ', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # household income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("Comme pour le niveau d’éducation formelle, la probabilité de donner par la majorité des méthodes a tendance à augmenter avec le revenu du ménage, bien que le montant habituel des dons soit beaucoup plus variable et qu’il n’ait pas tendance à augmenter de manière prévisible en fonction du revenu. La probabilité de donner à la suite d’une sollicitation par courrier, dans un lieu public ou dans un lieu de culte a tendance à être relativement constante entre les catégories de revenus. Seuls les dons en réponse à une publicité télévisée ou radiophonique diminuent avec l’augmentation du revenu du ménage."),
                        # Donation rate & average donation amount by household income
                        html.Div([
                            # html.H6("Donation rate & average donation amount by household income"),
                            dcc.Graph(id='DonMethDonRateAvgDonAmt-Inc', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Religious attendance
                    html.Div([
                        html.H5("Pratique Religieuse"),
                        html.P("Dans le cadre de la majorité des méthodes de don, la probabilité de donner augmente avec la fréquence de l’assiduité aux offices religieux. Cette association est la plus forte avec les dons à un lieu de culte, mais elle se constate également pour différentes méthodes de don, comme les dons par courrier, la participation à une activité de bienfaisance et en mémoire d’une personne. Au contraire, la probabilité de donner en ligne, à son lieu de travail, en réponse à une sollicitation au porte-à-porte et à une sollicitation en public ne semble pas varier énormément selon la fréquence de la pratique religieuse. Bien qu’il existe une forte association entre les dons plus importants et une participation fréquente aux offices religieux, les associations avec les autres méthodes de don semblent beaucoup plus faibles, si tant est qu’elles existent."),
                        html.Div([
                            # html.H6("Donation rate & average donation amount by household income"),
                           dcc.Graph(id='DonMethDonRateAvgDonAmt-Relig', style={'marginTop': marginTop}),
                        ]),
                    ]),
                           
#
                    # Other personal & economic characteristics
                    html.Div([
                        html.H5("Autres Facteurs"),
                        html.P(" Quant aux autres facteurs, les personnes nées au Canada sont, en général, relativement plus enclines à donner par la majorité des méthodes de don que les personnes naturalisées, à l’exception notable de la méthode des dons à un lieu de culte que les personnes naturalisées sont nettement plus enclines à utiliser. Les conséquences de la situation d’emploi sont très variées, certaines méthodes étant fortement associées aux personnes occupant un emploi (p. ex. donner au travail) ou à celles n’appartenant pas à la population active (p. ex. donner à un lieu de culte). Dans l’ensemble, les tendances des dons selon la situation matrimoniale semblent très étroitement liées aux tendances des dons selon l’âge (c.-à-d. les personnes célibataires ont tendance à être plus jeunes, tandis que celles qui sont veuves ont tendance à être plus âgées)."),
                        # Donation rate & average donation amount by religious attendance
                        # html.Div([
                        #     # html.H6("Donation rate & average donation amount by marital status"),
                        #     dcc.Graph(id='DonMethDonRateAvgDonAmt-MarStat', style={'marginTop': marginTop}),

                            # html.Br(),
                        # ]),
                        # Donation rate & average donation amount per method by employment status.
                        # html.Div([
                        #     # html.H6("Donation rate & average donation amount per method by employment status."),
                        #     dcc.Graph(id='DonMethDonRateAvgDonAmt-Labour', style={'marginTop': marginTop}),
                        # ]),
                        # # Donation rate & average donation amount by immigration status
                        # html.Div([
                        #     # html.H6("Donation rate & average donation amount by immigration status"),
                        #     dcc.Graph(id='DonMethDonRateAvgDonAmt-ImmStat', style={'marginTop': marginTop})

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
                        dcc.Graph(id='status-sel3', style={'marginTop': marginTop})
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

    dash.dependencies.Output('DonMethDonRateAvgDonAmt-Method', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])

def update_graph(region):

    dff1 = DonMethDonRates_2018[DonMethDonRates_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "All"]
    name1 = "Taux de donateur.trice.s"

    dff2 = DonMethAvgDon_2018[DonMethAvgDon_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "All"]
    name2 = "Dons annuels moyens"

    title = '{}, {}'.format("Taux et montant moyen des dons par méthode", region)

    return don_rate_avg_don_by_meth(dff1, dff2, name1, name2, title)

@app.callback(

    dash.dependencies.Output('DonMethDonRateAvgDonAmt-Gndr', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('method-selection', 'value')
    ])
def update_graph(region, method):
    dff1 = DonMethDonRates_2018[DonMethDonRates_2018['Region'] == region]
    dff1 = dff1[dff1['QuestionText'] == method]
    dff1 = dff1[dff1['Group'] == "Genre"]
    name1 = "Taux de donateur.trice.s"


    dff2 = DonMethAvgDon_2018[DonMethAvgDon_2018['Region'] == region]
    dff2 = dff2[dff2['QuestionText'] == method]
    dff2 = dff2[dff2['Group'] == "Genre"]
    name2 = "Dons annuels moyens"


    title = '{}, {}'.format("Taux et montant moyen des dons " + str(method).lower() + " selon le genre", region)
    # a = ['At work', 'Online', 'On own', 'In memoriam', 'Door-to-door canvassing']
    # b = ['Mail request', 'Telephone request', 'TV or radio request', 'Sponsoring someone']
    # c = ['Charity event', 'Public place', 'Place of worship']
    
    # if str(method) in a:
    #     title = '{}, {}'.format("Donations made " + str(method).lower() + " by gender", region)
    # elif str(method) in b:
    #     title = '{}, {}'.format("Donations made by " + str(method).lower() + " by gender", region)
    # elif str(method) in c:
    #     title = '{}, {}'.format("Donations made at " + str(method).lower() + " by gender", region)
    # else:
    #     title = '{}, {}'.format(str(method) + " by gender", region)
    
    return don_rate_avg_don(dff1, dff2, name1, name2, title)

@app.callback(

    dash.dependencies.Output('DonMethDonRateAvgDonAmt-Age', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('method-selection', 'value')
    ])
def update_graph(region, method):

    dff1 = DonMethDonRates_2018[DonMethDonRates_2018['Region'] == region]
    dff1 = dff1[dff1['QuestionText'] == method]
    dff1 = dff1[dff1['Group'] == "Groupe d'âge"]
    name1 = "Taux de donateur.trice.s"


    dff2 = DonMethAvgDon_2018[DonMethAvgDon_2018['Region'] == region]
    dff2 = dff2[dff2['QuestionText'] == method]
    dff2 = dff2[dff2['Group'] == "Groupe d'âge"]
    name2 = "Dons annuels moyens"


    title = '{}, {}'.format("Taux et montant moyen des dons " + str(method).lower() + " selon l’âge", region)
    # a = ['At work', 'Online', 'On own', 'In memoriam', 'Door-to-door canvassing']
    # b = ['Mail request', 'Telephone request', 'TV or radio request', 'Sponsoring someone']
    # c = ['Charity event', 'Public place', 'Place of worship']
    
    # if str(method) in a:
    #     title = '{}, {}'.format("Donations made " + str(method).lower() + " by age group", region)
    # elif str(method) in b:
    #     title = '{}, {}'.format("Donations made by " + str(method).lower() + " by age group", region)
    # elif str(method) in c:
    #     title = '{}, {}'.format("Donations made at " + str(method).lower() + " by age group", region)
    # else:
    #     title = '{}, {}'.format(str(method) + " by age group", region)

    return don_rate_avg_don(dff1, dff2, name1, name2, title)

@app.callback(

    dash.dependencies.Output('DonMethDonRateAvgDonAmt-Educ', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('method-selection', 'value')
    ])
def update_graph(region, method):
    dff1 = DonMethDonRates_2018[DonMethDonRates_2018['Region'] == region]
    dff1 = dff1[dff1['QuestionText'] == method]
    dff1 = dff1[dff1['Group'] == "Éducation"]
    name1 = "Taux de donateur.trice.s"


    dff2 = DonMethAvgDon_2018[DonMethAvgDon_2018['Region'] == region]
    dff2 = dff2[dff2['QuestionText'] == method]
    dff2 = dff2[dff2['Group'] == "Éducation"]
    name2 = "Dons annuels moyens"


    title = '{}, {}'.format("Taux et montant moyen des dons " + str(method).lower() + " selon l’éducation", region)
    # a = ['At work', 'Online', 'On own', 'In memoriam', 'Door-to-door canvassing']
    # b = ['Mail request', 'Telephone request', 'TV or radio request', 'Sponsoring someone']
    # c = ['Charity event', 'Public place', 'Place of worship']
    
    # if str(method) in a:
    #     title = '{}, {}'.format("Donations made " + str(method).lower() + " by education", region)
    # elif str(method) in b:
    #     title = '{}, {}'.format("Donations made by " + str(method).lower() + " by education", region)
    # elif str(method) in c:
    #     title = '{}, {}'.format("Donations made at " + str(method).lower() + " by education", region)
    # else:
    #     title = '{}, {}'.format(str(method) + " by education", region)

    return don_rate_avg_don(dff1, dff2, name1, name2, title)

@app.callback(

    dash.dependencies.Output('DonMethDonRateAvgDonAmt-Inc', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('method-selection', 'value')
    ])
def update_graph(region, method):
    dff1 = DonMethDonRates_2018[DonMethDonRates_2018['Region'] == region]
    dff1 = dff1[dff1['QuestionText'] == method]
    dff1 = dff1[dff1['Group'] == "Catégorie de revenu personnel"]
    name1 = "Taux de donateur.trice.s"


    dff2 = DonMethAvgDon_2018[DonMethAvgDon_2018['Region'] == region]
    dff2 = dff2[dff2['QuestionText'] == method]
    dff2 = dff2[dff2['Group'] == "Catégorie de revenu personnel"]
    name2 = "Dons annuels moyens"


    title = '{}, {}'.format("Taux et montant moyen des dons " + str(method).lower() + " selon le revenu", region)
    # a = ['At work', 'Online', 'On own', 'In memoriam', 'Door-to-door canvassing']
    # b = ['Mail request', 'Telephone request', 'TV or radio request', 'Sponsoring someone']
    # c = ['Charity event', 'Public place', 'Place of worship']
    
    # if str(method) in a:
    #     title = '{}, {}'.format("Donations made " + str(method).lower() + " by income", region)
    # elif str(method) in b:
    #     title = '{}, {}'.format("Donations made by " + str(method).lower() + " by income", region)
    # elif str(method) in c:
    #     title = '{}, {}'.format("Donations made at " + str(method).lower() + " by income", region)
    # else:
    #     title = '{}, {}'.format(str(method) + " by income", region)

    return don_rate_avg_don(dff1, dff2, name1, name2, title)

@app.callback(

    dash.dependencies.Output('DonMethDonRateAvgDonAmt-Relig', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('method-selection', 'value')
    ])
def update_graph(region, method):
    dff1 = DonMethDonRates_2018[DonMethDonRates_2018['Region'] == region]
    dff1 = dff1[dff1['QuestionText'] == method]
    dff1 = dff1[dff1['Group'] == "Fréquence de la fréquentation religieuse"]
    name1 = "Taux de donateur.trice.s"


    dff2 = DonMethAvgDon_2018[DonMethAvgDon_2018['Region'] == region]
    dff2 = dff2[dff2['QuestionText'] == method]
    dff2 = dff2[dff2['Group'] == "Fréquence de la fréquentation religieuse"]
    name2 = "Dons annuels moyens"


    title = '{}, {}'.format("Taux et montant moyen des dons " + str(method).lower() + " selon la pratique religieuse", region)
    # a = ['At work', 'Online', 'On own', 'In memoriam', 'Door-to-door canvassing']
    # b = ['Mail request', 'Telephone request', 'TV or radio request', 'Sponsoring someone']
    # c = ['Charity event', 'Public place', 'Place of worship']
    
    # if str(method) in a:
    #     title = '{}, {}'.format("Donations made " + str(method).lower() + " by religious attendance", region)
    # elif str(method) in b:
    #     title = '{}, {}'.format("Donations made by " + str(method).lower() + " by religious attendance", region)
    # elif str(method) in c:
    #     title = '{}, {}'.format("Donations made at " + str(method).lower() + " by religious attendance", region)
    # else:
    #     title = '{}, {}'.format(str(method) + " by religious attendance", region)

    return don_rate_avg_don(dff1, dff2, name1, name2, title)

@app.callback(
    dash.dependencies.Output('DonMethDonRateAvgDonAmt-MarStat', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('method-selection', 'value')
    ])
def update_graph(region, method):
    dff1 = DonMethDonRates_2018[DonMethDonRates_2018['Region'] == region]
    dff1 = dff1[dff1['QuestionText'] == method]
    dff1 = dff1[dff1['Group'] == "Marital status"]
    name1 = "Taux de donateur.trice.s"


    dff2 = DonMethAvgDon_2018[DonMethAvgDon_2018['Region'] == region]
    dff2 = dff2[dff2['QuestionText'] == method]
    dff2 = dff2[dff2['Group'] == "Marital status"]
    name2 = "Dons annuels moyens"


    title = '{}, {}'.format("Taux et montant moyen des dons " + str(method).lower() + " selon la situation matrimoniale", region)
    # a = ['At work', 'Online', 'On own', 'In memoriam', 'Door-to-door canvassing']
    # b = ['Mail request', 'Telephone request', 'TV or radio request', 'Sponsoring someone']
    # c = ['Charity event', 'Public place', 'Place of worship']
    
    # if str(method) in a:
    #     title = '{}, {}'.format("Donations made " + str(method).lower() + " by marital status", region)
    # elif str(method) in b:
    #     title = '{}, {}'.format("Donations made by " + str(method).lower() + " by marital status", region)
    # elif str(method) in c:
    #     title = '{}, {}'.format("Donations made at " + str(method).lower() + " by marital status", region)
    # else:
    #     title = '{}, {}'.format(str(method) + " by marital status", region)

    return don_rate_avg_don(dff1, dff2, name1, name2, title)

@app.callback(

    dash.dependencies.Output('DonMethDonRateAvgDonAmt-Labour', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('method-selection', 'value')
    ])
def update_graph(region, method):
    dff1 = DonMethDonRates_2018[DonMethDonRates_2018['Region'] == region]
    dff1 = dff1[dff1['QuestionText'] == method]
    dff1 = dff1[dff1['Group'] == "Labour force status"]
    name1 = "Taux de donateur.trice.s"


    dff2 = DonMethAvgDon_2018[DonMethAvgDon_2018['Region'] == region]
    dff2 = dff2[dff2['QuestionText'] == method]
    dff2 = dff2[dff2['Group'] == "Labour force status"]
    name2 = "Dons annuels moyens"


    title = '{}, {}'.format("Taux et montant moyen des dons " + str(method).lower() + " selon la situation d’emploi", region)
    # a = ['At work', 'Online', 'On own', 'In memoriam', 'Door-to-door canvassing']
    # b = ['Mail request', 'Telephone request', 'TV or radio request', 'Sponsoring someone']
    # c = ['Charity event', 'Public place', 'Place of worship']
    
    # if str(method) in a:
    #     title = '{}, {}'.format("Donations made " + str(method).lower() + " by employment status", region)
    # elif str(method) in b:
    #     title = '{}, {}'.format("Donations made by " + str(method).lower() + " by employment status", region)
    # elif str(method) in c:
    #     title = '{}, {}'.format("Donations made at " + str(method).lower() + " by employment status", region)
    # else:
    #     title = '{}, {}'.format(str(method) + " by employment status", region)

    return don_rate_avg_don(dff1, dff2, name1, name2, title)

@app.callback(

    dash.dependencies.Output('DonMethDonRateAvgDonAmt-ImmStat', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('method-selection', 'value')
    ])
def update_graph(region, method):
    dff1 = DonMethDonRates_2018[DonMethDonRates_2018['Region'] == region]
    dff1 = dff1[dff1['QuestionText'] == method]
    dff1 = dff1[dff1['Group'] == "Immigration status"]
    name1 = "Taux de donateur.trice.s"


    dff2 = DonMethAvgDon_2018[DonMethAvgDon_2018['Region'] == region]
    dff2 = dff2[dff2['QuestionText'] == method]
    dff2 = dff2[dff2['Group'] == "Immigration status"]
    name2 = "Dons annuels moyens"


    title = '{}, {}'.format("Taux et montant moyen des dons " + str(method).lower() + " selon le statut d’immigration", region)
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

@app.callback(

    dash.dependencies.Output('status-sel3', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('method-selection', 'value'),
        dash.dependencies.Input('status-selection', 'value')
    ])
def update_graph(region, method, status):
    dff1 = DonMethDonRates_2018[DonMethDonRates_2018['Region'] == region]
    dff1 = dff1[dff1['QuestionText'] == method]
    dff1 = dff1[dff1['Group'] == status]
    # name1 = "Donation rate"
    name1 = "Taux de donateur.trice.s"


    dff2 = DonMethAvgDon_2018[DonMethAvgDon_2018['Region'] == region]
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
