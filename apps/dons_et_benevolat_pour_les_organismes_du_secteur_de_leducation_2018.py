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
region_names = get_region_names()
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
                            html.H1('Dons et bénévolat pour les organismes du secteur de l’éducation (2018)'),
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
                    En plus de mesurer l’importance générale des dons et du bénévolat à divers niveaux, l’Enquête sociale générale sur les dons, le bénévolat et la participation mesure l’importance des niveaux de soutien pour 15 types de causes (appelées communément « domaines d’activité »), dont l’éducation. Selon la définition de l’Enquête, la catégorie de l’éducation se compose des universités et des collèges et des organismes d’éducation et de recherche. Les universités et les collèges, selon cette définition, sont les établissements qui décernent des diplômes postsecondaires, dont les facultés professionnelles associées (facultés d’administration des affaires, de droit et de médecine, etc.). Les organismes d’éducation et de recherche sont axés sur l’enseignement élémentaire, primaire et secondaire, l’enseignement professionnel et technique et la formation des adultes ou formation continue ou la recherche en sciences sociales, médicales, physiques ou technologiques.
                    """),
                    dcc.Markdown("""
                    Nous analysons ci-dessous les tendances des dons et du bénévolat au bénéfice de ces organismes. Nous décrivons dans le texte ci-dessous les résultats au niveau national et, pour obtenir des précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer des résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.
                    """),
                    html.H3('Montants des dons'),
                    dcc.Markdown("""
                    À l’échelle nationale, un peu plus d’une personne sur huit (13 %) au Canada a fait au moins un don à un organisme d’éducation et de recherche par rapport à environ une sur cinquante aux universités et aux collèges (moins de 1 % d’entre elles ont donné aux deux sous-causes) pendant l’année précédant l’Enquête, ce qui place l’éducation au cinquième rang des causes les plus soutenues au Canada. Sur le plan des deux sous-causes, plus d’une personne sur dix au Canada a donné aux organismes d’éducation et de recherche, par comparaison avec une sur cinquante aux universités et aux collèges (moins de 1 % d’entre elles ont donné aux deux sous-causes). Malgré une base de donateur.trice.s relativement large, les organismes d’éducation ont seulement reçu environ 4 % de la valeur totale de dons, répartis à raison de 60 % pour les organismes d’éducation et de recherche et de 40 % pour les universités et les collèges. L’écart entre les dons au bénéfice des deux sous-causes est loin de se limiter à l’écart entre le nombre de personnes qui donnent à l’une ou à l’autre. En effet, en moyenne, les montants donnés aux universités et aux collèges sont plus de quatre fois supérieurs à ceux donnés aux organismes d’éducation et de recherche. Par comparaison avec les niveaux de soutien caractéristiques des autres causes, les donateur.trice.s aux universités et collèges se classaient parmi les partisan.e.s les plus engagé.e.s, tandis que ceux des organismes d’éducation et de recherche faisaient partie des partisan.e.s les moins engagé.e.s. 
                    """),        
                    # Donation rate and average donation amount by cause graph
                    dcc.Graph(id='FormsGiving', style={'marginTop': 20}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                    html.H4('Qui donne de l’argent'),
                    dcc.Markdown("""
                    Certaines personnes sont plus enclines que d’autres à donner aux organismes du secteur de l’éducation. À l’échelle nationale, la probabilité de donner augmente avec le niveau d’études et le revenu du ménage. Quant à l’âge, la probabilité de donner augmente fortement jusqu’à l’âge de 35 à 44 ans, puis décline légèrement. Les autres groupes qui se distinguent en étant plus enclins à donner, sont les femmes, les personnes mariées ou en union de fait, les personnes qui occupent un emploi et les personnes nées au Canada. 
                    """
                    ),
                    # Donation rate by key demographic characteristics graph
                    # dcc.Graph(id='DonRateAvgDonAmt-prv', figure=don_rate_avg_don_amt_prv(DonRates_2018, AvgTotDon_2018), style={'marginTop': 20}),
                    html.H4('Méthodes de dons'),
                    dcc.Markdown("""
                    On a demandé aux répondant.e.s à l’Enquête si l’un ou plusieurs de 13 types de sollicitations différents les conduisaient à donner. Bien que l’Enquête ne lie pas directement ces méthodes aux causes soutenues, la comparaison entre les donateur.trice.s au bénéfice des organismes du secteur de l’éducation et les autres (c.-à-d. les personnes qui ne soutenaient que d’autres causes) permet de comprendre comment les personnes ont tendance à soutenir financièrement cette catégorie d’organismes. À l’échelle nationale, les donateur.trice.s du secteur de l’éducation ont particulièrement tendance à donner en parrainant quelqu’un (par exemple, lors d’un événement), en réponse à une sollicitation au porte-à-porte, à leur lieu de travail, en assistant à un événement de bienfaisance ou en mémoire de quelqu’un. Ces personnes ne sont pas particulièrement plus susceptibles de donner dans un lieu de culte, en réponse à un appel à la télévision ou la radio ou par d’autres méthodes non mentionnées expressément dans le questionnaire de l’Enquête.
                    """),
                    #Donation rate by method graph
                    # dcc.Graph(id='DonRateAvgDonAmt-prv', figure=don_rate_avg_don_amt_prv(DonRates_2018, AvgTotDon_2018), style={'marginTop': 20}),
                    html.H4('Motivations des dons'),
                    dcc.Markdown("""
                    On a demandé aux répondant.e.s à l’Enquête si huit facteurs potentiels jouaient un rôle important dans leurs décisions de donner. Là encore, bien qu’il n’existe aucun lien direct entre les motivations et les causes soutenues, la comparaison des personnes qui donnent aux organismes du secteur de l’éducation et de celles qui donnent aux autres organismes permet de comprendre les raisons de leur soutien de cette catégorie d’organismes. À l’échelle nationale, les donateur.trice.s aux organismes du secteur de l’éducation sont plus susceptibles que les personnes qui donnent aux autres organismes de contribuer financièrement à la suite de leur sollicitation par une personne de leur connaissance, parce que la cause de l’organisme les touche personnellement ou parce qu’elles connaissent une personne dans ce cas, pour apporter une contribution à la collectivité et parce qu’elles recevront un crédit d’impôt pour leur don. Les motivations religieuses et spirituelles ne semblent pas jouer un rôle particulièrement significatif dans les décisions de donner aux organismes du secteur de l’éducation. 
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
                    Afin de mieux comprendre les facteurs qui peuvent dissuader de donner, on a demandé aux donateur.trice.s si dix freins potentiels les empêchent de donner plus. À l’échelle nationale, les personnes qui donnent aux organismes du secteur de l’éducation ont plus tendance que les autres donateur.trice.s à limiter leurs dons parce qu’elles n’aiment pas les méthodes de sollicitation et parce qu’elles croient avoir déjà donné assez. Les autres freins ont grosso modo une incidence similaire sur les personnes qui donnent aux organismes d’éducation et sur celles qui donnent aux autres types d’organismes.
                    """
                    ),
                    # Barriers to donating more graph
                   # dcc.Graph(id='DonRateAvgDonAmt-Gndrr', style={'marginTop': marginTop}),

                
                    # Volunteering levels
                    html.Div([
                        html.H4("Niveaux de bénévolat"),
                        html.P("""
                        À l’échelle nationale, environ une personne sur 11 (9 %) au Canada a fait du bénévolat pour un organisme d’éducation et de recherche pendant l’année qui a précédé l’Enquête, ce qui fait de de la base de bénévoles de l’éducation la quatrième par ordre d’importance. Sur le plan des deux sous-causes, les personnes sont nettement moins enclines à faire du bénévolat pour les universités et les collèges que pour autres types d’organismes d’éducation et de recherche. Quant au nombre d’heures de bénévolat par cause, les organismes d’éducation et de recherche reçoivent un peu plus de 9 % du nombre total d’heures de bénévolat, à raison d’un tiers des heures pour les universités et les collèges et de deux tiers des heures pour les autres types d’organismes d’éducation et de recherche. À l’échelle nationale, les organismes du secteur de l’éducation et de la recherche se classent au quatrième rang du point de vue de la proportion du nombre total d’heures de bénévolat, derrière les organismes des arts et loisirs (22 %), les organismes des services sociaux (18 %) et les organismes religieux (16 %).
                        """),
                        # Volunteer rate and average hours volunteered by cause graph
                        #dcc.Graph(id='DonRateAvgDonAmt-Gndrr', style={'marginTop': marginTop}),
                    ]),
                    # Who volunteers
                    html.Div([
                        html.H4("Qui fait du bénévolat"),
                        html.P("""
                        À l’échelle nationale, les groupes les plus enclins à faire du bénévolat pour les organismes du secteur de l’éducation sont les femmes, les personnes célibataires et qui ne se sont jamais mariées et celles titulaires soit d’un diplôme universitaire, soit titulaires ou non d’un diplôme d’études secondaires. Quant à l’effet de l’âge, la probabilité de faire du bénévolat est la plus élevée à l’âge de 15 à 24 ans, chute de 25 à 34 ans, culmine de 35 à 44 ans, puis baisse, ce qui correspond vraisemblablement aux différents stades de la vie. Le bénévolat a également tendance à augmenter avec le revenu du ménage, bien que les ménages au revenu inférieur à 20 000 $ s’écartent légèrement de cette tendance, au niveau national du moins.
                        """),
                        # Volunteer rate by key demographic characteristics graph
                        #dcc.Graph(id='DonRateAvgDonAmt-Age_13', style={'marginTop': marginTop}),
                    ]),
                    # Volunteer activities
                    html.Div([
                        html.H4("Activités des bénévoles"),
                        html.P("""
                        On a demandé aux personnes si, parmi 14 types d’activité différents, elles participaient à 1 ou plusieurs d’entre elles pour un organisme. Bien que l’Enquête ne lie pas précisément les activités aux types d’organismes soutenus, la comparaison des bénévoles des organismes du secteur de l’éducation et de la recherche et des bénévoles des autres organismes permet de comprendre les activités des bénévoles font pour cette catégorie d’organismes. Comme on pouvait s’y attendre, les bénévoles des organismes d’éducation et de recherche ont relativement tendance à enseigner et à servir de mentors, mais aussi à organiser des activités et des événements, à entraîner et à arbitrer dans le cadre sportif et à collecter des fonds. Ces bénévoles sont relativement peu susceptibles de fournir des soins de santé ou du soutien dans ce domaine ou de participer à des activités bénévoles non mentionnées expressément dans le questionnaire. 
                        """),
                        # Volunteer rate by activity graph
                        #dcc.Graph(id='DonRateAvgDonAmt-Educ_13', style={'marginTop': marginTop}),
                    ]),
                    # Motivations for volunteering
                    html.Div([
                        html.H4("Motivations du bénévolat"),
                        html.P("""
                        On a demandé aux répondant.e.s si douze facteurs potentiels jouaient un rôle important dans leur décision de faire don de leur temps. Contrairement à de nombreux autres domaines de l’Enquête, ces motivations sont liées précisément au bénévolat au bénéfice de causes particulières. À l’échelle nationale, les personnes qui font du bénévolat pour le secteur de l’éducation sont plus enclines à chercher à améliorer leurs possibilités d’emploi et à réseauter ou à rencontrer des personnes. Elles ont moins tendance à être motivées par des croyances religieuses ou spirituelles, parce qu’un membre de leur famille fait du bénévolat ou par le soutien d’une forme ou d’une autre de cause politique, environnementale ou sociale. 
                        """),
                        # Motivations for volunteering graph
                        #dcc.Graph(id='DonRateAvgDonAmt-Inc_13', style={'marginTop': marginTop}),
                    ]),
                    # Barriers to volunteering
                    html.Div([
                        html.H4("Freins au bénévolat"),
                        html.P("""
                        On a demandé aux bénévoles si douze freins potentiels les avaient empêchés de faire don de plus de temps pendant l’année précédente. Bien que les freins ne soient pas liés directement aux causes soutenues, la comparaison des bénévoles des organismes d’éducation et de recherche et de ceux des autres organismes apporte une information importante sur les facteurs pouvant importer particulièrement aux bénévoles de cette catégorie d’organismes. À l’échelle nationale, les bénévoles du secteur de l’éducation ont plus tendance à limiter leur bénévolat par manque de temps. Ces personnes ont légèrement moins tendance à penser avoir déjà fait don d’assez de temps ou à limiter leur bénévolat en raison de problèmes de santé ou d’obstacles physiques. 
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
