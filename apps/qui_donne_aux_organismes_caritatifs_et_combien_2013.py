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

####################### Data processing #####################
BarriersVol_2018, SubSecAvgHrs_2018, SubSecVolRates_2018, AllocationVol_2018 = get_data()

data = [SubSecVolRates_2018, SubSecAvgHrs_2018, AllocationVol_2018]
process_data(data)

# region_values = get_region_values()
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
                        html.H1('Qui donne aux organismes caritatifs et combien? (2013)'),
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
    # Dropdown menu
    dbc.Container([
        dbc.Row(
           dbc.Col(
               html.Div([
                   "Sélectionnez une région:",
                   dcc.Dropdown(
                       id='region-selection',
                       options=[{'label': region_names[i], 'value': region_names[i]} for i in range(len(region_names))],
                       value='CA',
                       ),
                    html.Br(),
                ],className="m-2 p-2"),
            ),id='sticky-dropdown'),
    ],className='sticky-top bg-light mb-2', fluid=True),
   dbc.Container([
       dbc.Row([
            # Starting text
            html.Div([
                    dcc.Markdown("""
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2013, un peu plus de neuf personnes sur dix (92 %) au Canada ont contribué financièrement ou en nature, sous une forme ou une autre, aux organismes de bienfaisance ou à but non lucratif pendant l’année qui l’a précédée. À peine plus de quatre cinquièmes de ces personnes ont fait un don en argent, dont environ trois quarts ont fait un don en nature sous forme d’articles ménagers, de jouets ou de vêtements. Trois cinquièmes d’entre elles ont donné des aliments et environ une sur trente a fait un legs ou pris une forme d’engagement dans son testament. Le montant moyen des dons est de 532 $ et leur total général s’élève approximativement à 12,8 milliards $.
                    """
                    ),
                    # Forms of giving graph
                    #dcc.Graph(id='FormsGiving', style={'marginTop': 20}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                    dcc.Markdown("""
                    La probabilité de faire un don financier et le montant habituel des dons variaient légèrement selon les lieux de résidence. Dans l’ensemble, la probabilité de donner ne variait pas de manière statistiquement significative, les personnes vivant en Colombie-Britannique étant les seules relativement moins enclines à faire des dons. Quant au montant moyen des dons, les personnes du Québec et du Canada atlantique avaient tendance à donner moins que celles des Prairies et de l’Ouest canadien.
                    """
                    ),
                    # Donation rate & average donation amount by province graph
                    #dcc.Graph(id='DonRateAvgDonAmt-prv', figure=don_rate_avg_don_amt_prv(DonRates_2018, AvgTotDon_2018), style={'marginTop': 20}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Key personal & economic characteristics
            html.Div(
                [
                    html.H3('Caractéristiques Personnelles et Économiques Clés'),
                    html.P("""
                    En plus des variations provinciales, les tendances des dons fluctuaient également selon les caractéristiques personnelles et économiques. Nous examinons ci-dessous les deux mesures clés des dons :
                    """),
                    html.Ul([
                        html.Li('la probabilité de donner et le montant moyen des contributions, '),
                        html.Li('les pourcentages de donateur.trice.s et le total des dons pour chaque sous-groupe.'),
                    ]),
                    html.P("""
                    Ces mesures brossent un tableau détaillé du bassin de donateur.trice.s et fournissent un aperçu de la concentration du soutien financier des organismes de bienfaisance et à but non lucratif. Dans le texte, nous décrivons les résultats au niveau national et, pour obtenir des précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer des résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.
                    """
                    ),
                    
                   
                
                    # Gender
                    html.Div([
                        html.H4("Genre"),
                        html.P("""
                        Au niveau national, les femmes étaient relativement plus enclines à donner que les hommes, mais avaient tendance à donner des montants plutôt inférieurs.
                        """),
                        # Donation rate & average donation amount by gender graph
                        #dcc.Graph(id='DonRateAvgDonAmt-Gndrr', style={'marginTop': marginTop}),
                        
                        html.P("""
                        En raison de leurs dons plus importants en moyenne, les hommes représentaient une proportion du total des dons supérieure à celle que leur nombre portait à croire. Bien qu’ils étaient légèrement minoritaires parmi les Canadiens, la valeur totale de leurs dons était légèrement majoritaire.
                        """),
                        #Percentage of population & total donation value by gender
                        #dcc.Graph(id='PercDon-Gndrr', style={'marginTop': marginTop}),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("""
                        La probabilité de donner était la plus faible chez les personnes de 15 à 24 ans, puis augmentait à un niveau relativement constant chez celles âgées de 35 ans et plus. La légère baisse apparente après l’âge de 65 ans n’était pas assez importante pour être statistiquement significative. Les montants moyens des contributions augmentaient jusqu’à l’âge d’environ 45 ans en étant plus ou moins uniformes chez les personnes plus âgées. Là encore, les différences entre ces groupes n’étaient pas statistiquement significatives, du moins au niveau national.
                        """),
                        # Donation rate & average donation amount by age
                        #dcc.Graph(id='DonRateAvgDonAmt-Age_13', style={'marginTop': marginTop}),
                        
                        html.P("""
                        Étant donné leur plus forte tendance à donner et les montants habituellement supérieurs de leurs dons, les personnes âgées de 45 ans et plus représentaient une proportion de la valeur totale des dons supérieure à celle que leur représentation au sein de la population laissait présager. Au contraire, les personnes âgées de moins de 45 ans (et surtout celles de moins de 25 ans) représentaient des proportions de la valeur totale des dons très inférieures à leur représentation au sein de la population.
                        """),
                        # Percentage of population & total donation value by age
                        #dcc.Graph(id='PercDon-Age_13', style={'marginTop': marginTop}),
                    ]),
                    # Formal Education
                    html.Div([
                        html.H5("Éducation Formelle"),
                        html.P("""
                        L’augmentation de la probabilité de donner allait de pair avec le niveau d’éducation formelle pour culminer chez les titulaires d’un diplôme postsecondaire. Les montants moyens des dons augmentaient également avec le niveau d’éducation formelle, les titulaires d’un diplôme universitaire donnant nettement plus que les personnes à l’éducation formelle moindre.
                        """),
                        # Donation rate & average donation amount by gender
                        #dcc.Graph(id='DonRateAvgDonAmt-Educ_13', style={'marginTop': marginTop}),
                        
                        html.P("""
                        Principalement du fait de leur tendance à donner des montants supérieurs, les titulaires d’un diplôme universitaire représentaient une proportion de la totalité des dons très supérieure à celle que leur représentation au sein de la population donnait à penser. Les personnes à l’éducation formelle moindre représentaient une proportion très inférieure du total des dons, notamment celles non diplômées du palier secondaire. 
                        """),
                        #Percentage of population & total donation value by formal education
                        #dcc.Graph(id='PercDon-Educ_13', style={'marginTop': marginTop}),
                    ]),
                    # Income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("""
                        À seulement quelques divergences près, la probabilité de donner et les montants moyens augmentaient avec le revenu du ménage. Les ménages au revenu annuel égal ou supérieur à 140 000 $ donnaient souvent beaucoup plus que les ménages au revenu inférieur. 
                        """),
                        # Donation rate & average donation amount by household income graph
                        #dcc.Graph(id='DonRateAvgDonAmt-Inc_13', style={'marginTop': marginTop}),
                        
                        html.P("""
                        En raison de leurs dons souvent supérieurs, les ménages au revenu annuel égal ou supérieur à 140 000 $ représentaient un pourcentage de la totalité des dons très supérieur à celui que leur représentation au sein de la population pouvait laisser penser.
                        """),
                        #Percentage of population & total donation value by household income
                        #dcc.Graph(id='PercDon-Inc_13', style={'marginTop': marginTop}),
                    ]),
                    # Religious Attendance
                    html.Div([
                        html.H5("Pratique Religieuse"),
                        html.P("""
                        La probabilité de donner et les montants moyens des dons augmentaient avec la fréquence de la pratique religieuse. Bien que la valeur des dons des personnes assidues aux offices religieux bénéficiait majoritairement aux organisations religieuses, ce n’était pas exclusivement le cas. En effet, elles avaient aussi davantage tendance à donner à des organisations laïques et à leur donner des montants plus importants. 
                        """),
                        # Donation rate & average donation amount by religious attendance
                        #dcc.Graph(id='DonRateAvgDonAmt-Relig_13', style={'marginTop': marginTop}),
                        
                        html.P("""
                        Étant donné leur tendance plus forte à donner et, plus particulièrement, le montant moyen supérieur de leurs dons, les personnes assidues aux offices religieux, surtout celles qui y assistaient chaque semaine, représentaient des pourcentages disproportionnés du total des dons, compte tenu de leur représentation au sein de la population. Au contraire, celles qui n’assistaient pas ou qu’épisodiquement aux offices représentaient des pourcentages beaucoup plus petits du total des dons. 
                        """),
                        #Percentage of population & total donation value by religious attendance
                        #dcc.Graph(id='PercDon-Relig_13', style={'marginTop': marginTop}),
                    ]),
                    # Other Personal & Economic Characteristics
                    html.Div([
                        html.H5("Autres Caractéristiques Personnelles et Économiques "),
                        html.P("""
                        Les autres caractéristiques personnelles et économiques significatives sont la situation matrimoniale, la situation d’emploi et le statut d’immigration. D’une façon générale, les personnes mariées ou en union de fait ou veuves étaient plus susceptibles de donner, et ce, en montants supérieurs, de même que les salariés. Les personnes non membres de la population active avaient légèrement moins tendance à donner, mais étaient enclines à se montrer très généreuses quand elles le faisaient. Au chapitre du statut d’immigration, les personnes nouvellement arrivées au Canada donnaient tout aussi souvent que celles nées au Canada, mais le montant de leurs dons était souvent légèrement supérieur. 
                        """),
                        # Donation rate & average donation amount by marital status graph
                        # dcc.Graph(id='ActivityVolRate-Labour', style={'marginTop': marginTop}),
                        # Donation rate & average donation amount by labour force status graph
                        # dcc.Graph(id='ActivityVolRate-ImmStat', style={'marginTop': marginTop}),
                        # Donation rate & average donation amount by immigration status graph
                        # dcc.Graph(id='ActivityVolRate-ImmStat', style={'marginTop': marginTop}),
                        
                        html.P("""
                        En général, les personnes mariées ou en union de fait représentaient une proportion du total des dons significativement supérieure à celle que leur nombre laissait présager, de même que les personnes nouvellement arrivées au Canada et, dans une moindre mesure, les salarié.e.s. 
                        """),
                        # Percentage of population & total donation value by marital status graph
                        # dcc.Graph(id='ActivityVolRate-Labour', style={'marginTop': marginTop}),
                        # Percentage of population & total donation value by labour force status graph
                        # dcc.Graph(id='ActivityVolRate-ImmStat', style={'marginTop': marginTop}),
                        # Percentage of population & total donation value by immigration status graph
                        # dcc.Graph(id='ActivityVolRate-ImmStat', style={'marginTop': marginTop}),
                        
                        #html.Div(['Select status:',
                                      #dcc.Dropdown(
                                         # id='status-selection1',
                                          #options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                                          #value='Marital status',
                                          #style={'verticalAlign': 'middle'}
                                     # ),],
                                     #style={'width': '50%', 'display': 'inline-block'}),
                        ]),
                        html.Div(['Select status:',
                                      dcc.Dropdown(
                                          id='status-selection2',
                                          options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                                          value='Marital status',
                                          style={'verticalAlign': 'middle'}
                                      ),],
                                     #style={'width': '50%', 'display': 'inline-block'}),
                       # html.Div([
                            # html.H6("Percentage of donors & total donation value by immigration status"),
                           # dcc.Graph(id='PercDon-other_13', style={'marginTop': marginTop}),
                           # html.Br(),
                            # html.P("The degree to which Canadians focus on the primary cause they support does not seem to vary significantly according to their marital or labour force status. Married, widowed, and to a certain extent divorced Canadians tend to support a somewhat wider range of causes, as do those who are not in the labour force. Turning to immigration status, New Canadians and those residing in Canada who have not yet obtained landed immigrant status tend to focus more of their support on the primary cause and to support fewer causes than do native-born Canadians."),
                       # ]),
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
