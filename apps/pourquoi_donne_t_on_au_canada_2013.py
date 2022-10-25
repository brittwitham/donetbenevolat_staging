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
                            html.H1('Pourquoi donne-t-on au Canada? (2013)'),
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
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2013, un peu plus de quatre cinquièmes des personnes au Canada (82 %) ont fait un don à un organisme de bienfaisance ou à but non lucratif pendant l’année qui l’a précédée. Afin de mieux comprendre pourquoi les motivations des personnes qui soutiennent les organismes, on leur a demandé ensuite si chacun des sept facteurs ci-dessous jouait un rôle important dans leurs décisions de donner.
                    """),
                    dcc.Markdown("""
                    Nous présentons ci-dessous leurs motivations, puis nous décrivons l’importance relative de ces motivations selon leurs caractéristiques personnelles et économiques. Dans le texte, nous décrivons les résultats au niveau national et vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer légèrement par rapport aux résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.
                    """),
                    dcc.Markdown("""
                    Dans l’ensemble, c’est le sentiment de compassion envers les personnes dans le besoin qui motivait le plus les personnes à donner, ainsi que leur conviction personnelle à l’égard de la cause des organismes qu’ils ont soutenus. À l’échelle nationale, environ quatre personnes sur cinq ont été motivées par le désir de contribuer à la communauté et deux sur trois parce qu’elles étaient touchées personnellement ou parce qu’une personne de leur connaissance était touchée par la cause des organismes qu’elles ont soutenus. Un nombre relativement moins important de personnes ont contribué parce qu’une personne de leur connaissance, une personne amie ou un membre de leur famille le leur a demandé. Les personnes étaient moins enclines à être motivées par leurs obligations ou croyances religieuses ou par le crédit d’impôt qu’elles recevraient en échange de leur don.
                    """
                    ),
                                
                    # Motivations reported by donors graph
                    dcc.Graph(id='FormsGiving', style={'marginTop': 20}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                    dcc.Markdown("""
                    Certaines motivations ont clairement tendance à être associées à des dons beaucoup plus importants que d’autres. Les croyances et les obligations religieuses constituaient le facteur le plus significatif, en étant associées à des dons beaucoup plus importants. Bien que les personnes motivées par ce facteur étaient enclines à réserver leur soutien à des organismes religieux, elles avaient également tendance à donner des montants relativement plus élevés à des causes laïques. Bien que seulement une petite minorité de personnes ait déclaré que les crédits d’impôt qu’elles recevraient étaient un facteur important dans leurs décisions de donner, les personnes motivées par ce facteur avaient tendance à donner beaucoup plus. Au chapitre des motivations les plus courantes, les personnes qui donnaient par motivation envers une cause et par compassion envers les personnes dans le besoin donnaient nettement plus que les personnes non motivées par ces facteurs. Le fait d’être touché personnellement par la cause et la sollicitation par une personne amie ou un proche parent avaient la plus faible incidence sur les montants moyens des dons, tout en demeurant des facteurs de motivation positifs.
                    """
                    ),
                    # Average amounts contributed by donors reporting and not reporting specific motivations graph
                    # dcc.Graph(id='DonRateAvgDonAmt-prv', figure=don_rate_avg_don_amt_prv(DonRates_2018, AvgTotDon_2018), style={'marginTop': 20}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Key personal & economic characteristics
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
                        # Donor motivations by gender graph
                        dcc.Graph(id='DonRateAvgDonAmt-Gndrr', style={'marginTop': marginTop}),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("""
                        L’importance (nombre plus ou moins important de personnes à faire état d’un facteur de motivation) des croyances religieuses et des crédits d’impôt augmentait avec l’âge. L’importance des autres motivations avait tendance à augmenter jusqu’à l’âge moyen, puis à diminuer. Le désir d’offrir une contribution à la communauté et la sollicitation par une personne proche culminaient l’un et d’autre chez les personnes âgées de 35 à 44 ans, tandis que le fait d’être touché par la cause et la conviction à l’égard de la cause culminaient chez celles légèrement plus âgées, de 45 à 54 ans.
                        """),
                        # Donor motivations by age graph
                        dcc.Graph(id='DonRateAvgDonAmt-Age_13', style={'marginTop': marginTop}),
                    ]),
                    # Formal Education
                    html.Div([
                        html.H5("Éducation formelle"),
                        html.P("""
                        La probabilité de faire état de la majorité des motivations augmentait avec le niveau d’éducation formelle. Les seules exceptions à cette tendance, du moins au niveau national, étaient les obligations et les convictions religieuses (qui avaient tendance à être importantes à la fois pour les personnes au niveau d’éducation formelle très élevé et très bas) et les sentiments de compassion envers les personnes dans le besoin (qui avaient fortement tendance à être constants, indépendamment du niveau d’éducation formelle). 
                        """),
                        # Donor motivations by formal education graph
                        dcc.Graph(id='DonRateAvgDonAmt-Educ_13', style={'marginTop': marginTop}),
                    ]),
                    # Income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("""
                        Dans l’ensemble, la majorité des motivations ne variaient pas beaucoup en fonction du niveau de revenu du ménage. Pour autant que des tendances étaient significatives, les convictions religieuses avaient tendance à devenir moins importantes avec l’augmentation du revenu, tandis que la sollicitation par une connaissance ou par un membre de la famille gagnait en importance.
                        """),
                        # Donor motivations by household income graph
                        dcc.Graph(id='DonRateAvgDonAmt-Inc_13', style={'marginTop': marginTop}),
                    ]),
                    # Religious Attendance
                    html.Div([
                        html.H5("Pratique Religieuse"),
                        html.P("""
                        À quelques exceptions près, l’augmentation de l’importance des motivations allait de pair avec l’assiduité aux offices religieux. Cette association était la plus étroite avec les convictions religieuses, mais la plupart des autres motivations étaient également plus importantes pour les personnes assidues aux offices religieux. Les seules motivations qui n’étaient pas plus courantes chez les personnes assidues étaient le fait d’être touchées par la cause et la sollicitation par une personne amie ou membre de leur famille.
                        """),
                        # Donor motivations by religious attendance graph
                        dcc.Graph(id='DonRateAvgDonAmt-Relig_13', style={'marginTop': marginTop}),
                    ]),
                    # Other Factors
                    html.Div([
                        html.H5("Autres facteurs"),
                        html.P("""
                       En ce qui concerne les autres caractéristiques, la majorité des motivations variaient très peu en fonction de la situation d’emploi. Les principales exceptions étaient les dons à la suite de la demande par une connaissance, nettement moins importants pour les personnes qui n’appartenaient pas à la population active (tendance vraisemblablement liée aux dons en milieu de travail), et les motivations religieuses, nettement plus importantes pour les personnes qui n’appartenaient pas à la population active (vraisemblablement plus âgées et à la retraite). Une tendance similaire se constate pour la situation matrimoniale, les associations des personnes veuves et des dons étant identiques à celles des personnes non membres de la population active, en plus de la motivation supérieure des personnes veuves par les crédits d’impôt. Au chapitre du statut d’immigration, les personnes naturalisées étaient nettement plus motivées à donner en raison de leurs croyances religieuses et légèrement plus susceptibles d’être motivées par la plupart des autres croyances. La seule motivation significativement plus importante chez les personnes nées au Canada était le fait d’être personnellement touchées par la cause de l’organisme ou de connaître une personne qui l’était, ce qui dénote peut-être le temps nécessaire pour établir des liens sociaux solides dans un nouveau pays.
                        """),
                        # Donor motivations by marital status graph
                        # dcc.Graph(id='ActivityVolRate-Labour', style={'marginTop': marginTop}),
                        # Donor motivations by labour force status graph
                        # dcc.Graph(id='ActivityVolRate-ImmStat', style={'marginTop': marginTop}),
                        # Donor motivations by immigration status graph
                        # dcc.Graph(id='ActivityVolRate-ImmStat', style={'marginTop': marginTop}),
                    ]),
                    #Causes Supported
                    html.Div([
                        html.H5("Causes soutenues"),
                        html.P("""
                        Bien que l’ESG DBP de 2013 ne recueillait pas directement de l’information sur les motivations du soutien de causes précises, la comparaison des motivations générales des personnes qui soutenaient une cause particulière et de celles qui ne la soutenaient pas peut expliquer ce qui a motivé le soutien de certaines causes. Pour la majorité des motivations et des causes, les personnes qui soutenaient une cause particulière étaient également plus susceptibles de faire état d’une motivation particulière que celles qui s’en abstenaient. En effet, tout bien considéré, les personnes qui soutenaient une cause donnée avaient plus tendance à soutenir de multiples causes et à donner des montants plus importants. Les motivations pouvaient constituer des facteurs significatifs quand le nombre de personnes de chacune de ces deux catégories était inhabituellement élevé ou quand les personnes qui soutenaient une cause étaient moins susceptibles de faire état d’une motivation particulière que celles qui s’en abstenaient.
                        """),
                        html.P("""
                        Le graphique ci-dessous montre le pourcentage de personnes ayant fait état de chaque motivation, ventilé en fonction de leur don ou de leur abstention de donner au bénéfice de chaque cause particulière. Plusieurs associations se constatent à l’échelle nationale. Par exemple, les personnes qui donnaient aux organismes religieux avaient plus tendance à faire état de croyances et de convictions religieuses à titre de motivation pour leurs dons, de même que celles qui donnaient aux organismes du développement international et de l’aide internationale. Dans le même ordre d’idées, les personnes qui donnaient aux organismes du secteur de la santé avaient particulièrement tendance à être touchées personnellement par la cause des organismes soutenus ou à connaître une personne qui l’était, tandis que les personnes qui donnaient aux organismes des services sociaux avaient particulièrement tendance à être motivées par des sentiments de compassion envers les personnes dans le besoin. Vous pouvez utiliser le menu déroulant dans la visualisation des données ci-dessous pour choisir un sous-secteur particulier qui les intéresse.
                        """),
                        # Percentages of cause supporters and non-supporters reporting each motivation, by cause graph
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
