import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd

from utils.data.WDA0101_data_utils import get_region_values
from utils.data.WDC0105_data_utils import get_region_names
from utils.gen_navbar import gen_navbar
from utils.home_button import gen_home_button
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc
import os
import os.path as op

from utils.graphs.GAV0304_graph_utils import rate_avg_cause, vertical_percentage_graph
from utils.graphs.GAV0301_graph_utils import single_vertical_percentage_graph
from utils.data.GAV0304_data_utils import get_data, process_data, get_region_names, get_region_values

from app import app
from homepage import  footer

####################### Data processing ######################
SubSecAvgDon_2018, SubSecDonRates_2018, SubSecDonRatesFoc_2018, SubSecAvgHrs_2018, SubSecVolRates_2018, SubSecVolRatesFoc_2018, SocSerDonorsBarriers_2018, SocSerDonorsDonMeth_2018, SocSerDonorsDonRates_2018, SocSerDonorsMotivations_2018, SocSerVolsActivities_2018, SocSerVolsBarriers_2018, SocSerVolsMotivations_2018, SocSerVolsVolRates_2018 = get_data()
data = [SubSecAvgDon_2018,
        SubSecDonRates_2018,
        SubSecDonRatesFoc_2018,
        SubSecAvgHrs_2018,
        SubSecVolRates_2018,
        SubSecVolRatesFoc_2018,
        SocSerDonorsBarriers_2018,
        SocSerDonorsDonMeth_2018,
        SocSerDonorsDonRates_2018,
        SocSerDonorsMotivations_2018,
        SocSerVolsActivities_2018,
        SocSerVolsBarriers_2018,
        SocSerVolsMotivations_2018,
        SocSerVolsVolRates_2018]
process_data(data)

region_values = get_region_values()
region_names = get_region_names()
demo_names = ["Groupe d'âge", 'Genre', 'Éducation', 'État civil', "Situation d'activité", 'Catégorie de revenu personnel', 'Catégorie de revenu familial', 'Fréquence de la fréquentation religieuse', "Statut d'immigration"]


###################### App layout ######################

marginTop = 20
home_button = gen_home_button()
navbar = gen_navbar("giving_and_volunteering_for_social_services_organizations")

layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1('Dons et bénévolat pour les organismes de services sociaux (2018)'),
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
   dbc.Container([
       dbc.Row([
            html.Div([
                # html.H3('Giving'),
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
                # Donation rate and average donation amount by cause
                dcc.Graph(id='SocSerDonRateAvgDon', style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H4('Qui donne de l’argent'),
                    dcc.Markdown("""
                    Certaines personnes sont plus enclines que d’autres à donner aux organismes de services sociaux. Dans l’ensemble, les groupes qui soutiennent financièrement les organismes sociaux ne se démarquent pas aussi nettement que ceux qui soutiennent d’autres types d’organismes. En revanche, certaines tendances leur sont propres. En gros, la probabilité de donner a tendance à augmenter avec l’âge, avec le niveau d’éducation formelle et, dans une certaine mesure, avec l’assiduité aux offices religieux. Les femmes sont légèrement plus enclines à leur faire des dons que les hommes, de même que les personnes nées au Canada. En revanche, les personnes célibataires ou qui ne se sont jamais mariées se différencient en étant moins enclines à donner à ces organismes. 
                    """
                    ),
            html.Div([
                     html.Div(['Sélectionnez un catégorie démographique:',
                               dcc.Dropdown(
                                   id='demo-selection-don',
                                   options=[{'label': demo_names[i], 'value': demo_names[i]}
                                            for i in range(len(demo_names))],
                                   value='Groupe d\'âge',
                                   style={'verticalAlign': 'middle'}
                               ), ],
                              style={'width': '33%', 'display': 'inline-block'})
                 ]),
                 # Donation rate by key demographic characteristics
                 dcc.Graph(id="SocSerDonRateDemo_fr", style={'marginTop': marginTop})
            ], className='col-md-10 col-lg-8 mx-auto'),
            # html.Div([
            #     html.H4('Support for Other Organization Types'),
            #     # Rates of donating to other causes
            #     dcc.Graph(id='SocSerDonsCauses', style={'marginTop': marginTop}),
            #     ], className='col-md-10 col-lg-8 mx-auto'
            # ),
            html.Div([
                html.H4('Méthodes de dons'),
                    dcc.Markdown("""
                    On a demandé aux répondant.e.s à l’Enquête si l’un ou plusieurs de 13 types de sollicitations différents les conduisaient à donner. Bien que l’Enquête ne lie pas directement ces méthodes aux causes soutenues, la comparaison entre les donateur.trice.s au bénéfice des organismes de services sociaux et les autres (c.-à-d. les personnes qui ne soutenaient que d’autres causes) permet de comprendre comment les personnes ont tendance à soutenir financièrement cette catégorie d’organismes. À l’échelle nationale, ces dernières sont particulièrement enclines à donner à la suite de leur sollicitation dans un lieu public (par exemple, dans la rue ou un centre commercial), d’une sollicitation directe par courrier ou au porte-à-porte. Elles ne sont pas particulièrement enclines à donner dans un lieu de culte ou par d’autres méthodes non mentionnées expressément dans le questionnaire de l’Enquête. 
                    """),
                # Donation rate by method
                dcc.Graph(id='SocSerDonsMeth', style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Motivations des dons'),
                    dcc.Markdown("""
                    On a demandé aux répondant.e.s à l’Enquête si huit facteurs potentiels jouaient un rôle important dans leurs décisions de donner. Là encore, bien qu’il n’existe aucun lien direct entre les motivations et les causes soutenues, la comparaison des personnes qui donnent aux organismes de services sociaux et de celles qui donnent aux autres organismes permet de comprendre les raisons de leur soutien de cette catégorie d’organismes. À l’échelle nationale, les sentiments de compassion à l’égard des personnes dans le besoin et le désir de contribuer à la collectivité sont particulièrement importants pour les donateur.trice.s des organismes de services sociaux. À l’inverse, les croyances religieuses et spirituelles ne semblent pas constituer des facteurs de motivation significatifs pour ces personnes. 
                    """),
                # Motivations for donating
                dcc.Graph(id='SocSerMotivations', style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Freins aux dons'),
                    html.P("""
                    Afin de mieux comprendre les facteurs qui peuvent dissuader de donner, on a demandé aux donateur.trice.s si dix freins potentiels les empêchent de donner plus. À l’échelle nationale, les personnes qui font des dons aux services sociaux ont légèrement plus tendance à donner aux personnes dans le besoin au lieu de passer par un organisme, et ont plus tendance à ne pas aimer les méthodes de sollicitation. L’incidence de tous les autres freins est grosso modo identique sur les personnes qui donnent aux organismes de services sociaux et sur celles qui donnent aux autres causes. 
                    """
                    ),
                # Barriers to donating more
                dcc.Graph(id='SocSerBarriers', style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
       dbc.Row([
            html.Div([
                html.H4("Niveaux de bénévolat"),
                        html.P("""
                        À l’échelle nationale, environ une personne sur 9 (11 %) au Canada a fait du bénévolat pour un organisme de services sociaux pendant l’année qui a précédé l’Enquête, ce qui place les services sociaux aux deuxième rang des causes les plus soutenues au Canada, en suivant de près les organismes des arts et des loisirs. Quant au nombre d’heures de bénévolat au bénéfice de la cause, les organismes de services sociaux représentent environ 18 % du nombre total d’heures, à la traîne des organismes des arts et des loisirs, mais en devançant les organismes religieux (16 %) et ceux de l’éducation et de la recherche (9 %).
                        """),
                # Volunteer rate and average hours volunteered by cause
                dcc.Graph(id='SocSerVolRateAvgHrs', style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4("Qui fait du bénévolat"),
                        html.P("""
                        En gros, la probabilité de faire du bénévolat pour un organisme de services sociaux a tendance à aller de pair avec les niveaux de revenu du ménage et d’éducation formelle supérieurs, mais décline avec l’âge. Les femmes et les personnes nées au Canada se distinguent en étant les plus susceptibles de faire du bénévolat pour ces organismes, contrairement aux personnes qui assistent aux offices religieux. 
                        """),
                html.Div([
                     html.Div(['Sélectionnez un catégorie démographique:',
                               dcc.Dropdown(
                                   id='demo-selection-vol',
                                   options=[{'label': demo_names[i], 'value': demo_names[i]}
                                            for i in range(len(demo_names))],
                                   value='Groupe d\'âge',
                                   style={'verticalAlign': 'middle'}
                               ), ],
                              style={'width': '33%', 'display': 'inline-block'})
                 ]),
                 # Volunteer rate by key demographic characteristics
                 dcc.Graph(id="SocSerVolRateDemo_fr", style={'marginTop': marginTop})
                        ],
            className='col-md-10 col-lg-8 mx-auto'),
            # html.Div([
            #     html.H4('Support for other organization types'),
            #     # Rates of volunteering for other causes
            #     dcc.Graph(id='SocSerVolRateAvgHrs', style={'marginTop': marginTop}),
            #     ], className='col-md-10 col-lg-8 mx-auto'
            # ),
            html.Div([
                html.H4("Activités des bénévoles"),
                        html.P("""
                        On a demandé aux personnes si, parmi 14 types d’activité différents, elles participaient à 1 ou plusieurs d’entre elles pour un organisme. Bien que l’Enquête ne lie pas précisément les activités aux types d’organismes soutenus, la comparaison des bénévoles des organismes de services sociaux et des bénévoles des autres organismes permet de comprendre les activités des bénévoles pour cette catégorie d’organismes. À l’échelle nationale, les bénévoles des services sociaux sont relativement susceptibles de participer à de nombreux types d’activités, dont la collecte et la livraison de marchandises, la collecte d’aliments et le service de repas, l’enseignement ou le mentorat, les soins de santé et le soutien dans ce domaine et le counseling et l’offre de conseils. Les seules activités que ces bénévoles ont relativement tendance à éviter sont l’entraînement et l’arbitrage dans le cadre sportif ou la présidence de cérémonies.
                        """),
                # Volunteer rate by activity
                dcc.Graph(id='SocSerVolActivity', style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4("Motivations du bénévolat"),
                        html.P("""
                        On a demandé aux répondant.e.s si douze facteurs potentiels jouaient un rôle important dans leur décision de faire don de leur temps. Contrairement à de nombreux autres domaines de l’Enquête, ces motivations sont liées précisément au bénévolat au bénéfice de causes particulières. À l’échelle nationale, ce qui différencie le plus les bénévoles des organismes de services sociaux, c’est leur tendance légèrement supérieure à faire du bénévolat à l’appui d’une cause politique ou sociale et leur tendance légèrement inférieure à faire du bénévolat pour des raisons religieuses ou pour rencontrer des personnes ou réseauter. 
                        """),
                # Motivations for volunteering
                dcc.Graph(id='SocSerVolMotivations', style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4("Freins au bénévolat"),
                        html.P("""
                        On a demandé aux bénévoles si douze freins potentiels les avaient empêchés de faire don de plus de temps pendant l’année précédente. Bien que les freins ne soient pas liés directement aux causes soutenues, la comparaison des bénévoles des organismes de services sociaux et des personnes qui font don de leur temps aux autres organismes apporte une information importante sur les facteurs qui importent particulièrement aux bénévoles de cette catégorie d’organismes. Au niveau national du moins, les bénévoles des services sociaux réagissent aux divers freins d’une manière très comparable aux bénévoles des autres causes. Les bénévoles des services sociaux ont légèrement moins tendance à limiter leur bénévolat par manque d’intérêt pour en faire plus, ce qui constitue la seule différence importante avec les bénévoles des autres causes.
                        """),
                # Barriers to volunteering more
                dcc.Graph(id='SocSerVolBarriers', style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
   ]),
   footer
])

@app.callback(
    dash.dependencies.Output('SocSerDonRateAvgDon', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = SubSecDonRates_2018[SubSecDonRates_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "All"]

    dff1 = dff1.replace("Donation rate", "Taux de donateur.trice.s")
    # name1 = "Donation rate"
    name1 = "Taux de donateur.trice.s"


    dff2 = SubSecAvgDon_2018[SubSecAvgDon_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "All"]


    dff2 = dff2.replace("Average donation", "Dons annuels moyens")
#     name2 = "Average donation"
    name2 = "Dons annuels moyens"

    title = '{}, {}'.format("Taux et montant moyen des dons selon la cause", region)

    return rate_avg_cause(dff1, dff2, name1, name2, title)

# @app.callback(
#     dash.dependencies.Output('SocSerDonRateAvgDon', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     dff1 = SubSecDonRates_2018[SubSecDonRates_2018['Region'] == region]
#     # dff1 = dff1.replace("Donation rate", "Taux de donateur.trice.s")
#     name1 = "Donation rate"
#     # name1 = "Taux de donateur.trice.s"

#     dff2 = SubSecAvgDon_2018[SubSecAvgDon_2018['Region'] == region]
#     # dff2 = dff2.replace("Average donation", "Dons annuels moyens")
#     name2 = "Average donation"
#     # name2 = "Dons annuels moyens"

#     title = '{}, {}'.format("Taux et montant moyen des dons selon la cause", region)

#     return rate_avg_cause(dff1, dff2, name1, name2, title)


@app.callback(
    dash.dependencies.Output('SocSerDonsCauses', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SocSerDonorsDonRates_2018[SocSerDonorsDonRates_2018['Region'] == region]
    dff = dff.replace("Social services donor", "Donateur.trice.s des services sociaux")
    dff = dff.replace("Non-social services donor", "Autres donateur.trice.s")

    # name1 = "Social services donor"
    # name2 = "Non-social services donor"
    name1 = "Donateur.trice.s des services sociaux"
    name2 = "Autres donateur.trice.s"

    title = '{}, {}'.format("Rates of donating to other causes", region)
    return vertical_percentage_graph(dff, title, name1, name2)

@app.callback(
    dash.dependencies.Output('SocSerDonsMeth', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SocSerDonorsDonMeth_2018[SocSerDonorsDonMeth_2018['Region'] == region]
    dff = dff.replace("Social services donors", "Donateur.trice.s des services sociaux")
    dff = dff.replace("Non-social services donors", "Autres donateur.trice.s")

    # name1 = "Social services donor"
    # name2 = "Non-social services donor"
    name1 = "Donateur.trice.s des services sociaux"
    name2 = "Autres donateur.trice.s"

    title = '{}, {}'.format("Taux de donateur.trice.s par méthode", region)
    return vertical_percentage_graph(dff, title, name1, name2)

@app.callback(
    dash.dependencies.Output('SocSerMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SocSerDonorsMotivations_2018[SocSerDonorsMotivations_2018['Region'] == region]
    dff = dff.replace("Social services donors", "Donateur.trice.s des services sociaux")
    dff = dff.replace("Non-social services donors", "Autres donateur.trice.s")

    # name1 = "Social services donor"
    # name2 = "Non-social services donor"
    name1 = "Donateur.trice.s des services sociaux"
    name2 = "Autres donateur.trice.s"

    title = '{}, {}'.format("Motivations des dons", region)
    return vertical_percentage_graph(dff, title, name1, name2)

@app.callback(
    dash.dependencies.Output('SocSerBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SocSerDonorsBarriers_2018[SocSerDonorsBarriers_2018['Region'] == region]
    dff = dff.replace("Social services donors", "Donateur.trice.s des services sociaux")
    dff = dff.replace("Non-social services donors", "Autres donateur.trice.s")

    # name1 = "Social services donor"
    # name2 = "Non-social services donor"
    name1 = "Donateur.trice.s des services sociaux"
    name2 = "Autres donateur.trice.s"

    title = '{}, {}'.format("Freins à donner plus", region)
    return vertical_percentage_graph(dff, title, name1, name2)


# @app.callback(
#     dash.dependencies.Output('SocSerVolRateAvgHrs', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     dff1 = SubSecVolRates_2018[SubSecVolRates_2018['Region'] == region]
#     dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")
#     # name1 = "Volunteer rate"
#     name1 = "Taux de bénévolat"

#     dff2 = SubSecAvgHrs_2018[SubSecAvgHrs_2018['Region'] == region]
#     dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
#     # name2 = "Average hours"
#     name2 = "Nombre d'heures moyen"

#     title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures de bénévolat selon la cause", region)

#     return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)

@app.callback(
    dash.dependencies.Output('SocSerVolRateAvgHrs', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = SubSecVolRates_2018[SubSecVolRates_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "All"]
    dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")
#     # name1 = "Volunteer rate"
    name1 = "Taux de bénévolat"

    dff2 = SubSecAvgHrs_2018[SubSecAvgHrs_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "All"]
    dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
#     # name2 = "Average hours"
    name2 = "Nombre d'heures moyen"

    title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures de bénévolat selon la cause", region)

    return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)


@app.callback(
    dash.dependencies.Output('SocSerHrsCauses', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SocSerVolsVolRates_2018[SocSerVolsVolRates_2018['Region'] == region]
    name1 = "Donateur.trice.s des services sociaux"
    name2 = "Autres donateur.trice.s"

    title = '{}, {}'.format("Rates of volunteering for other causes", region)
    return vertical_percentage_graph(dff, title, name1, name2)

@app.callback(
    dash.dependencies.Output('SocSerVolActivity', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SocSerVolsActivities_2018[SocSerVolsActivities_2018['Region'] == region]
    dff = dff.replace("Social services volunteer", "Bénévoles des services sociaux")
    dff = dff.replace("Non-social services volunteer", "Autres bénévoles")
    name1 = "Bénévoles des services sociaux"
    name2 = "Autres bénévoles"

    title = '{}, {}'.format("Taux de bénévolat par activité", region)
    return vertical_percentage_graph(dff, title, name1, name2)

@app.callback(
    dash.dependencies.Output('SocSerVolMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SocSerVolsMotivations_2018[SocSerVolsMotivations_2018['Region'] == region]
    dff = dff.replace("Social services volunteer", "Bénévoles des services sociaux")
    dff = dff.replace("Non-social services volunteer", "Autres bénévoles")
    name1 = "Bénévoles des services sociaux"
    name2 = "Autres bénévoles"

    title = '{}, {}'.format("Motivations des bénévoles", region)
    return vertical_percentage_graph(dff, title, name1, name2)

@app.callback(
    dash.dependencies.Output('SocSerVolBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SocSerVolsBarriers_2018[SocSerVolsBarriers_2018['Region'] == region]
    dff = dff.replace("Social services volunteer", "Bénévoles des services sociaux")
    dff = dff.replace("Non-social services volunteer", "Autres bénévoles")
    name1 = "Bénévoles des services sociaux"
    name2 = "Autres bénévoles"

    title = '{}, {}'.format("Freins à faire plus de bénévolat", region)
    return vertical_percentage_graph(dff, title, name1, name2)

@app.callback(
    dash.dependencies.Output('SocSerDonRateDemo_fr', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('demo-selection-don', 'value'),
    ])
def update_graph(region, demo):
    dff = SubSecDonRatesFoc_2018[SubSecDonRatesFoc_2018['Region'] == region]
    dff = dff[dff['Group'] == demo]

    title = 'Taux de donateur.trice.s par {}, {}'.format(demo.lower(), region)

    return single_vertical_percentage_graph(dff, title)


@app.callback(
    dash.dependencies.Output('SocSerVolRateDemo_fr', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('demo-selection-vol', 'value'),
    ])
def update_graph(region, demo):
    dff = SubSecVolRatesFoc_2018[SubSecVolRatesFoc_2018['Region'] == region]
    dff = dff[dff['Group'] == demo]

    title = 'Taux de bénévoles par {}, {}'.format(demo.lower(), region)

    return single_vertical_percentage_graph(dff, title)
