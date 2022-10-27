import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc
import os
import os.path as op

from utils.graphs.GAV0301_graph_utils import vertical_percentage_graph
from utils.graphs.HOA0204_graph_utils import rate_avg_cause
from utils.data.GAV0301_data_utils import get_data, process_data, get_region_names, get_region_values

from app import app
from homepage import navbar, footer

####################### Data processing ######################
SubSecAvgDon_2018, SubSecDonRates_2018, SubSecAvgHrs_2018, SubSecVolRates_2018, HealthDonorsBarriers_2018, HealthDonorsDonMeth_2018, HealthDonorsDonRates_2018, HealthDonorsMotivations_2018, HealthVolsActivities_2018, HealthVolsBarriers_2018, HealthVolsMotivations_2018, HealthVolsVolRates_2018 = get_data()
data = [SubSecAvgDon_2018, SubSecDonRates_2018, HealthDonorsBarriers_2018, HealthDonorsDonMeth_2018, HealthDonorsDonRates_2018, HealthDonorsMotivations_2018, HealthVolsActivities_2018, HealthVolsBarriers_2018, HealthVolsMotivations_2018, HealthVolsVolRates_2018, SubSecAvgHrs_2018, SubSecVolRates_2018]
process_data(data)

region_values = get_region_values()
region_names = get_region_names()

###################### App layout ######################

marginTop = 20

layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1(('Dons d’argent et bénévolat pour les organismes santé').capitalize()),
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
    # dropdown menu
    dbc.Container([
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
                    En plus de mesurer l’importance générale des dons et du bénévolat à divers niveaux, l’Enquête sociale générale sur les dons, le bénévolat et la participation mesure l’importance des niveaux de soutien pour 15 types de causes (appelées communément « domaines d’activité »), dont la santé. Selon la définition de l’Enquête, la catégorie de la santé au sens large se compose des hôpitaux et des organismes de santé généralistes. Les hôpitaux sont principalement axés sur les soins aux patients hospitalisés, tandis que les organismes de santé généralistes sont principalement axés sur les soins aux patients externes et sur d’autres services médicaux, comme la promotion de la santé, la formation en secourisme et les services d’urgence.
                    """),
                dcc.Markdown("""
                    Nous analysons ci-dessous les tendances des dons et du bénévolat au bénéfice des organismes de santé. Nous décrivons dans le texte ci-dessous les résultats au niveau national et, pour obtenir des précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer des résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.
                    """),
                html.H4('Montants des dons'),
                dcc.Markdown("""
                    À l’échelle nationale, un peu plus de deux personnes sur cinq (41 %) au Canada ont fait des dons aux organismes de santé pendant la période d’une année qui a précédé l’Enquête, ce qui place la santé en tête des causes les plus soutenues au Canada. Sur le plan des deux sous-causes, une personne sur trois a donné de l’argent aux organismes de santé généralistes et une sur six aux hôpitaux (9 % d’entre elles ont donné aux deux sous-causes). Quant aux montants des dons, la catégorie des organismes de santé au sens large a représenté la deuxième proportion, par ordre d’importance, de la valeur totale des dons (17 %), derrière les organismes religieux. Les organismes de santé généralistes ont reçu la majorité de ce soutien (11 %) et le reste est allé aux hôpitaux (6 %). L’écart entre les deux sous-causes est presque exclusivement lié à l’importance relative de leurs bases de donateur.trice.s, puisque ces personnes ont donné des montants quasiment identiques à l’une comme à l’autre. 
                    """),
                
                # Donation rate and average donation amount by cause
                dcc.Graph(id='DonRateAvgDon', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                # [
                # # html.H4('Who Gives'),
                # #  html.P('Some Canadians are more likely to give to health organizations than others. Nationally, women are more likely to donate than men, those who are married or widowed are more likely to donate than those who are single, those who are employed or not in the labour force are more likely to donate than those who are unemployed, and those born in Canada are more likely to donate than New Canadians. In terms of major trends, the likelihood of donating tends to increase with age, level of formal education, frequency of attendance at religious services, and household income.')
                # ],

                html.H4('Qui donne de l’argent'),
                dcc.Markdown("""
                    Certaines personnes sont plus enclines que d’autres à donner aux organismes de santé. À l’échelle nationale, les femmes ont plus tendance à donner que les hommes, les personnes mariées ou veuves sont plus susceptibles de donner que les célibataires, les personnes qui occupent un emploi ou qui ne sont pas membres de la population active donnent plus fréquemment que celles au chômage, et celles qui sont nées au Canada sont plus susceptibles de donner que les personnes nouvellement arrivées. Au chapitre des grandes tendances, la probabilité de donner a tendance à augmenter avec l’âge, le niveau d’éducation formelle, l’assiduité aux offices religieux et le revenu du ménage.  
                    """
                    )],

                className='col-md-10 col-lg-8 mx-auto'
            
                
            ),
            # html.Div([
            #     html.H4('Support for Other Organization Types'),
            #     # Donation rate and average donation amount by cause
            #     dcc.Graph(id='HealthDonsCauses', style={'marginTop': marginTop}), 
            #     ], className='col-md-10 col-lg-8 mx-auto'
            # ),
            html.Div([
                html.H4('Méthodes de dons'),
                    dcc.Markdown("""
                    On a demandé aux répondant.e.s à l’Enquête si l’un ou plusieurs de 13 types de sollicitations différents les conduisaient à donner. Bien que l’Enquête ne lie pas directement ces méthodes aux causes soutenues, la comparaison entre les donateur.trice.s au bénéfice des organismes de santé et les autres (c.-à-d. les personnes qui ne soutenaient que d’autres causes) permet de comprendre comment les personnes ont tendance à soutenir financièrement cette catégorie d’organismes. À l’échelle nationale, ces dernières sont particulièrement enclines à donner en mémoire d’une personne, en parrainant une personne lors d’un événement (comme un cyclothon ou un tournoi de golf) et à la suite d’une sollicitation dans un lieu public (par exemple dans la rue ou un centre commercial). Elles sont légèrement moins enclines à donner dans un lieu de culte.
                    """),
                # Donation rate by method
                dcc.Graph(id='HealthDonsMeth', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Motivations des dons'),
                    dcc.Markdown("""
                    On a demandé aux répondant.e.s à l’Enquête si huit facteurs potentiels jouaient un rôle important dans leurs décisions de donner. Là encore, bien qu’il n’existe aucun lien direct entre les motivations et les causes soutenues, la comparaison des personnes qui donnent aux organismes de santé et de celles qui donnent aux autres organismes permet de comprendre les raisons de leur soutien des organismes de santé. Les personnes qui donnent aux organismes de santé sont nettement plus enclines à donner parce qu’elles sont touchées personnellement par la cause de l’organisme ou parce qu’elles connaissent une personne dans ce cas et parce qu’elles ont été sollicitées par une personne de leur connaissance. Elles sont relativement moins enclines à donner en raison de croyances religieuses ou spirituelles. 
                    """),
                # Barriers to donating more
                dcc.Graph(id='HealthMotivations', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Freins aux dons'),
                    html.P("""
                    Afin de mieux comprendre les facteurs qui peuvent dissuader de donner, on a demandé aux donateur.trice.s si dix freins potentiels les empêchent de donner plus. À l’échelle nationale, la différence la plus importante entre ces deux catégories de donateur.trice.s a trait à la satisfaction relativement supérieure des personnes qui donnent aux organismes de santé à l’égard du montant qu’elles ont déjà donné et à leur tendance relativement inférieure à faire du bénévolat au lieu de donner et à limiter leurs dons parce qu’elles trouvent difficilement une cause digne de leur soutien. 
                    """
                    ),
                # Barriers to donating more
                dcc.Graph(id='HealthBarriers', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            
        ]),
       dbc.Row([
            html.Div([
                html.H4("Niveaux de bénévolat"),
                        html.P("""
                        À l’échelle nationale, environ une personne sur 17 (6 %) au Canada a fait du bénévolat pour un organisme de santé pendant l’année qui a précédé l’Enquête, ce qui place la santé au cinquième rang des causes les plus soutenues au Canada. Sur le plan des deux sous-causes, les personnes sont deux fois plus susceptibles de faire du bénévolat pour les organismes de santé généralistes que pour les hôpitaux. Quant au nombre d’heures de bénévolat au bénéfice de la cause, les organismes de santé reçoivent un peu moins de 9 % du total des heures. Bien que la base de bénévoles des hôpitaux soit considérablement plus petite, ces bénévoles ont tendance à faire don de plus d’heures et, par conséquent, les heures de bénévolat totales se répartissent grosso modo à égalité entre les hôpitaux et les organismes de santé généralistes. À l’échelle nationale, les organismes de santé reçoivent la cinquième proportion des heures de bénévolat par ordre d’importance, après les organismes des arts et loisirs (23 %), les organismes des services sociaux (18 %), les organismes religieux (16 %) et ceux du secteur de l’éducation et de la recherche (9 %).
                        """),
                # Volunteer rate and average hours volunteered by cause
                dcc.Graph(id='VolRateAvgHrs', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                html.H4("Qui fait du bénévolat"),
                        html.P("""
                        Les groupes qui se distinguent en étant plus susceptibles de faire du bénévolat pour les organismes de santé sont les femmes, les titulaires d’un diplôme postsecondaire ou les personnes au niveau d’éducation formelle supérieur et celles nées au Canada. Sur le plan des tendances, la probabilité de faire du bénévolat a tendance à augmenter avec le revenu du ménage et avec l’assiduité aux offices religieux. 
                        """),
                 ],
            className='col-md-10 col-lg-8 mx-auto'),
            # html.Div([
            #     html.H4('Support for other organization types'),
            #     # Rates of volunteering for other causes
            #     dcc.Graph(id='HealthHrsCauses', style={'marginTop': marginTop}), 
            #     ], className='col-md-10 col-lg-8 mx-auto'
            # ),
            html.Div([
                html.H4("Activités des bénévoles"),
                        html.P("""
                        On a demandé aux personnes si, parmi 14 types d’activité différents, elles participaient à 1 ou plusieurs d’entre elles pour un organisme. Bien que l’Enquête ne lie pas précisément les activités aux types d’organismes soutenus, la comparaison des bénévoles des organismes de santé et des bénévoles des autres organismes permet de comprendre les activités des bénévoles pour cette catégorie d’organismes. Comme on pouvait s’y attendre, les bénévoles des organismes de santé sont particulièrement susceptibles d’offrir des soins de santé ou du soutien dans ce domaine, mais aussi plus susceptibles de participer aux activités de collecte de fonds et au porte-à-porte. Ces personnes sont nettement moins susceptibles d’entraîner ou d’arbitrer dans le cadre sportif et légèrement moins susceptibles d’effectuer des travaux d’entretien ou de réparations.
                        """),
                # Volunteer rate by activity
                dcc.Graph(id='HealthVolActivity', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4("Motivations du bénévolat"),
                        html.P("""
                        On a demandé aux répondant.e.s si douze facteurs potentiels jouaient un rôle important dans leur décision de faire don de leur temps. Contrairement à de nombreux autres domaines de l’Enquête, ces motivations sont liées précisément au bénévolat au bénéfice de causes particulières. À l’échelle nationale, les bénévoles des organismes de santé se distinguent le plus par leur tendance supérieure à faire du bénévolat parce que la cause les touche personnellement ou touche une personne de leur connaissance. Ces personnes sont légèrement moins enclines à faire du bénévolat pour réseauter ou pour rencontrer des personnes. Les autres motivations semblent avoir une influence à peu près égale sur les bénévoles des organismes de la santé et des autres types d’organismes. 
                        """),
                # Motivations for volunteering
                dcc.Graph(id='HealthVolMotivations', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4("Freins au bénévolat"),
                        html.P("""
                        On a demandé aux bénévoles si douze freins potentiels les avaient empêchés de faire don de plus de temps pendant l’année précédente. Bien que les freins ne soient pas liés directement aux causes soutenues, la comparaison des bénévoles des organismes de santé et de ceux des autres organismes apporte une information importante. Au total, ces bénévoles réagissent aux freins potentiels d’une manière très semblable aux autres bénévoles. À l’échelle nationale, les bénévoles des organismes de santé se démarquent le plus nettement en ayant légèrement moins tendance à souhaiter faire plus de bénévolat et à avoir légèrement plus tendance à faire des dons d’argent de préférence à faire don de leur temps.
                        """),
                # Barriers to volunteering more
                dcc.Graph(id='HealthVolBarriers', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
   ]),
   footer
])

################ Callbacks ################

@app.callback(
    dash.dependencies.Output('DonRateAvgDon', 'figure'),
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

    # name2 = "Average donation"
    name2 = "Dons annuels moyens"

    title = '{}, {}'.format("Taux de donateur.trice.s et montant moyen des dons selon la cause", region)

    return rate_avg_cause(dff1, dff2, name1, name2, title)


@app.callback(
    dash.dependencies.Output('HealthDonsCauses', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = HealthDonorsDonRates_2018[HealthDonorsDonRates_2018['Region'] == region]
    name1 = "Health donors"
    name2 = "Non-health donor"

    array = ["Health", "Hospitals", "Social services", "Religion",
             "Sports &<br>recreation", "Education &<br>research", "Grant-making,<br>fundraising",
             "International", "Environment", "Law, advocacy &<br>politics", "Arts & culture",
             "Development &<br>housing", "Other", "Universities &<br>colleges", "Business &<br>professional"]
    title = '{}, {}'.format("Rates of donating to other causes", region)
    return vertical_percentage_graph(dff, title, name1, name2, sort=True, array=array)


@app.callback(
    dash.dependencies.Output('HealthDonsMeth', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = HealthDonorsDonMeth_2018[HealthDonorsDonMeth_2018['Region'] == region]
    dff = dff.replace('Health donors', 'Donateur.trice.s de la santé')
    dff = dff.replace("Non-health donors", 'Autres donateur.trice.s')
    # name1 = "Health donors"
    # name2 = "Non-health donors"
    name1 = 'Donateur.trice.s de la santé'
    name2 = 'Autres donateur.trice.s'

    title = '{}, {}'.format("Taux de donateur.trice.s par méthode", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('HealthMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = HealthDonorsMotivations_2018[HealthDonorsMotivations_2018['Region'] == region]
    dff = dff.replace('Health donors', 'Donateur.trice.s de la santé')
    dff = dff.replace("Non-health donors", 'Autres donateur.trice.s')
    # name1 = "Health donors"
    # name2 = "Non-health donors"
    name1 = 'Donateur.trice.s de la santé'
    name2 = 'Autres donateur.trice.s'

    title = '{}, {}'.format("Motivations des dons", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('HealthBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = HealthDonorsBarriers_2018[HealthDonorsBarriers_2018['Region'] == region]

    dff = dff.replace('Health donors', 'Donateur.trice.s de la santé')
    dff = dff.replace("Non-health donors", 'Autres donateur.trice.s')
    # name1 = "Health donors"
    # name2 = "Non-health donors"
    name1 = 'Donateur.trice.s de la santé'
    name2 = 'Autres donateur.trice.s'

    title = '{}, {}'.format("Freins à donner plus", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('VolRateAvgHrs', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = SubSecVolRates_2018[SubSecVolRates_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "All"]
    dff1 = dff1.replace('Volunteer rate', 'Taux de bénévolat')
    # name1 = "Volunteer rate"
    name1 = 'Taux de bénévolat'

    dff2 = SubSecAvgHrs_2018[SubSecAvgHrs_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "All"]
    dff2 = dff2.replace('Average hours', "Nombre d'heures moyen")
    # name2 = "Average hours"
    name2 = "Nombre d'heures moyen"

    title = '{}, {}'.format("Taux de bénévoles et nombre moyen d’heures de bénévolat selon la cause", region)

    return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)


@app.callback(
    dash.dependencies.Output('HealthHrsCauses', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = HealthVolsVolRates_2018[HealthVolsVolRates_2018['Region'] == region]
    name1 = "Health volunteer"
    name2 = "Non-health volunteer"

    title = '{}, {}'.format("Rates of volunteering for other causes", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('HealthVolActivity', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = HealthVolsActivities_2018[HealthVolsActivities_2018['Region'] == region]
    
    dff = dff.replace("Health volunteer", "Bénévoles de la santé")
    dff = dff.replace("Non-health volunteer", "Autres bénévoles")
    name1 = "Bénévoles de la santé"
    name2 = "Autres bénévoles"
    # name1 = "Health volunteer"
    # name2 = "Non-health volunteer"
    
    title = '{}, {}'.format("Taux de bénévoles par activité", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('HealthVolMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = HealthVolsMotivations_2018[HealthVolsMotivations_2018['Region'] == region]
    
    dff = dff.replace("Health volunteer", "Bénévoles de la santé")
    dff = dff.replace("Non-health volunteer", "Autres bénévoles")
    name1 = "Bénévoles de la santé"
    name2 = "Autres bénévoles"
    # name1 = "Health volunteer"
    # name2 = "Non-health volunteer"

    title = '{}, {}'.format("Motivations du bénévolat", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('HealthVolBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = HealthVolsBarriers_2018[HealthVolsBarriers_2018['Region'] == region]
    
    dff = dff.replace("Health volunteer", "Bénévoles de la santé")
    dff = dff.replace("Non-health volunteer", "Autres bénévoles")
    name1 = "Bénévoles de la santé"
    name2 = "Autres bénévoles"
    # name1 = "Health volunteer"
    # name2 = "Non-health volunteer"

    title = '{}, {}'.format("Freins à faire plus de bénévolat", region)
    return vertical_percentage_graph(dff, title, name1, name2)
