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
                            html.H1('Dons et bénévolat pour les organismes de services sociaux (2018)'),
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
                    En plus de mesurer l’importance générale des dons et du bénévolat à divers niveaux, l’Enquête sociale générale sur les dons, le bénévolat et la participation mesure l’importance des niveaux de soutien pour 15 types de causes (appelées communément « domaines d’activité »), dont les services sociaux. Les organismes de services sociaux offrent un large éventail de services à la personne à la collectivité ou à une population particulière. Ces services sont notamment offerts aux enfants, aux jeunes et aux familles, aux personnes handicapées, âgées ou infirmes et prennent la forme de refuges, de banques alimentaires, d’aide aux réfugiés, de prévention des urgences et d’interventions en cas d’urgence et de soutien du revenu.
                    """),
                    dcc.Markdown("""
                    Nous analysons ci-dessous les tendances des dons et du bénévolat au bénéfice de ces organismes. Nous décrivons dans le texte ci-dessous les résultats au niveau national et, pour obtenir des précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer des résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.
                    """),
                    html.H4('Montants des dons'),
                    dcc.Markdown("""
                    À l’échelle nationale, un peu plus d’une personne sur trois au Canada a fait au moins un don aux organismes de services sociaux pendant la période qui a précédé l’Enquête, ce qui place les services sociaux au deuxième rang des causes les plus soutenues au Canada. Sur le plan des montants des dons, les services sociaux ont représenté 10  % de la valeur totale des dons, ce qui les place au troisième rang, après les organismes religieux et les organismes de santé. La place de cette catégorie d’organismes parmi les premières au classement s’explique par sa large base de donateur.trice.s, puisque les montants des dons à son bénéfice étaient relativement modestes. Par comparaison avec les niveaux de soutien caractéristiques des autres causes, les donateur.trice.s des services sociaux se situent vers la limite inférieure de la fourchette.
                    """),        
                    # Donation rate and average donation amount by cause graph
                    dcc.Graph(id='FormsGiving', style={'marginTop': 20}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                    html.H4('Qui donne de l’argent'),
                    dcc.Markdown("""
                    Certaines personnes sont plus enclines que d’autres à donner aux organismes de services sociaux. Dans l’ensemble, les groupes qui soutiennent financièrement les organismes sociaux ne se démarquent pas aussi nettement que ceux qui soutiennent d’autres types d’organismes. En revanche, certaines tendances leur sont propres. En gros, la probabilité de donner a tendance à augmenter avec l’âge, avec le niveau d’éducation formelle et, dans une certaine mesure, avec l’assiduité aux offices religieux. Les femmes sont légèrement plus enclines à leur faire des dons que les hommes, de même que les personnes nées au Canada. En revanche, les personnes célibataires ou qui ne se sont jamais mariées se différencient en étant moins enclines à donner à ces organismes. 
                    """
                    ),
                    # Donation rate by key demographic characteristics graph
                    # dcc.Graph(id='DonRateAvgDonAmt-prv', figure=don_rate_avg_don_amt_prv(DonRates_2018, AvgTotDon_2018), style={'marginTop': 20}),
                    html.H4('Méthodes de dons'),
                    dcc.Markdown("""
                    On a demandé aux répondant.e.s à l’Enquête si l’un ou plusieurs de 13 types de sollicitations différents les conduisaient à donner. Bien que l’Enquête ne lie pas directement ces méthodes aux causes soutenues, la comparaison entre les donateur.trice.s au bénéfice des organismes de services sociaux et les autres (c.-à-d. les personnes qui ne soutenaient que d’autres causes) permet de comprendre comment les personnes ont tendance à soutenir financièrement cette catégorie d’organismes. À l’échelle nationale, ces dernières sont particulièrement enclines à donner à la suite de leur sollicitation dans un lieu public (par exemple, dans la rue ou un centre commercial), d’une sollicitation directe par courrier ou au porte-à-porte. Elles ne sont pas particulièrement enclines à donner dans un lieu de culte ou par d’autres méthodes non mentionnées expressément dans le questionnaire de l’Enquête. 
                    """),
                    #Donation rate by method graph
                    # dcc.Graph(id='DonRateAvgDonAmt-prv', figure=don_rate_avg_don_amt_prv(DonRates_2018, AvgTotDon_2018), style={'marginTop': 20}),
                    html.H4('Motivations des dons'),
                    dcc.Markdown("""
                    On a demandé aux répondant.e.s à l’Enquête si huit facteurs potentiels jouaient un rôle important dans leurs décisions de donner. Là encore, bien qu’il n’existe aucun lien direct entre les motivations et les causes soutenues, la comparaison des personnes qui donnent aux organismes de services sociaux et de celles qui donnent aux autres organismes permet de comprendre les raisons de leur soutien de cette catégorie d’organismes. À l’échelle nationale, les sentiments de compassion à l’égard des personnes dans le besoin et le désir de contribuer à la collectivité sont particulièrement importants pour les donateur.trice.s des organismes de services sociaux. À l’inverse, les croyances religieuses et spirituelles ne semblent pas constituer des facteurs de motivation significatifs pour ces personnes. 
                    """),
                    #Motivations for donating graph
                    # dcc.Graph(id='DonRateAvgDonAmt-prv', figure=don_rate_avg_don_amt_prv(DonRates_2018, AvgTotDon_2018), style={'marginTop': 20}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Barriers to donating
            html.Div(
                [
                    html.H4('Freins aux dons'),
                    html.P("""
                    Afin de mieux comprendre les facteurs qui peuvent dissuader de donner, on a demandé aux donateur.trice.s si dix freins potentiels les empêchent de donner plus. À l’échelle nationale, les personnes qui font des dons aux services sociaux ont légèrement plus tendance à donner aux personnes dans le besoin au lieu de passer par un organisme, et ont plus tendance à ne pas aimer les méthodes de sollicitation. L’incidence de tous les autres freins est grosso modo identique sur les personnes qui donnent aux organismes de services sociaux et sur celles qui donnent aux autres causes. 
                    """
                    ),
                    # Barriers to donating more graph
                   # dcc.Graph(id='DonRateAvgDonAmt-Gndrr', style={'marginTop': marginTop}),

                
                    # Volunteering levels
                    html.Div([
                        html.H4("Niveaux de bénévolat"),
                        html.P("""
                        À l’échelle nationale, environ une personne sur 9 (11 %) au Canada a fait du bénévolat pour un organisme de services sociaux pendant l’année qui a précédé l’Enquête, ce qui place les services sociaux aux deuxième rang des causes les plus soutenues au Canada, en suivant de près les organismes des arts et des loisirs. Quant au nombre d’heures de bénévolat au bénéfice de la cause, les organismes de services sociaux représentent environ 18 % du nombre total d’heures, à la traîne des organismes des arts et des loisirs, mais en devançant les organismes religieux (16 %) et ceux de l’éducation et de la recherche (9 %).
                        """),
                        # Volunteer rate and average hours volunteered by cause graph
                        #dcc.Graph(id='DonRateAvgDonAmt-Gndrr', style={'marginTop': marginTop}),
                    ]),
                    # Who volunteers
                    html.Div([
                        html.H4("Qui fait du bénévolat"),
                        html.P("""
                        En gros, la probabilité de faire du bénévolat pour un organisme de services sociaux a tendance à aller de pair avec les niveaux de revenu du ménage et d’éducation formelle supérieurs, mais décline avec l’âge. Les femmes et les personnes nées au Canada se distinguent en étant les plus susceptibles de faire du bénévolat pour ces organismes, contrairement aux personnes qui assistent aux offices religieux. 
                        """),
                        # Volunteer rate by key demographic characteristics graph
                        #dcc.Graph(id='DonRateAvgDonAmt-Age_13', style={'marginTop': marginTop}),
                    ]),
                    # Volunteer activities
                    html.Div([
                        html.H4("Activités des bénévoles"),
                        html.P("""
                        On a demandé aux personnes si, parmi 14 types d’activité différents, elles participaient à 1 ou plusieurs d’entre elles pour un organisme. Bien que l’Enquête ne lie pas précisément les activités aux types d’organismes soutenus, la comparaison des bénévoles des organismes de services sociaux et des bénévoles des autres organismes permet de comprendre les activités des bénévoles pour cette catégorie d’organismes. À l’échelle nationale, les bénévoles des services sociaux sont relativement susceptibles de participer à de nombreux types d’activités, dont la collecte et la livraison de marchandises, la collecte d’aliments et le service de repas, l’enseignement ou le mentorat, les soins de santé et le soutien dans ce domaine et le counseling et l’offre de conseils. Les seules activités que ces bénévoles ont relativement tendance à éviter sont l’entraînement et l’arbitrage dans le cadre sportif ou la présidence de cérémonies.
                        """),
                        # Volunteer rate by activity graph
                        #dcc.Graph(id='DonRateAvgDonAmt-Educ_13', style={'marginTop': marginTop}),
                    ]),
                    # Motivations for volunteering
                    html.Div([
                        html.H4("Motivations du bénévolat"),
                        html.P("""
                        On a demandé aux répondant.e.s si douze facteurs potentiels jouaient un rôle important dans leur décision de faire don de leur temps. Contrairement à de nombreux autres domaines de l’Enquête, ces motivations sont liées précisément au bénévolat au bénéfice de causes particulières. À l’échelle nationale, ce qui différencie le plus les bénévoles des organismes de services sociaux, c’est leur tendance légèrement supérieure à faire du bénévolat à l’appui d’une cause politique ou sociale et leur tendance légèrement inférieure à faire du bénévolat pour des raisons religieuses ou pour rencontrer des personnes ou réseauter. 
                        """),
                        # Motivations for volunteering graph
                        #dcc.Graph(id='DonRateAvgDonAmt-Inc_13', style={'marginTop': marginTop}),
                    ]),
                    # Barriers to volunteering
                    html.Div([
                        html.H4("Freins au bénévolat"),
                        html.P("""
                        On a demandé aux bénévoles si douze freins potentiels les avaient empêchés de faire don de plus de temps pendant l’année précédente. Bien que les freins ne soient pas liés directement aux causes soutenues, la comparaison des bénévoles des organismes de services sociaux et des personnes qui font don de leur temps aux autres organismes apporte une information importante sur les facteurs qui importent particulièrement aux bénévoles de cette catégorie d’organismes. Au niveau national du moins, les bénévoles des services sociaux réagissent aux divers freins d’une manière très comparable aux bénévoles des autres causes. Les bénévoles des services sociaux ont légèrement moins tendance à limiter leur bénévolat par manque d’intérêt pour en faire plus, ce qui constitue la seule différence importante avec les bénévoles des autres causes.
                        """),
                        # Barriers to volunteering more graph
                        #dcc.Graph(id='DonRateAvgDonAmt-Relig_13', style={'marginTop': marginTop}),
               
                    
                    
                        
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
