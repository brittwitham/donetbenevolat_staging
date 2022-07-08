import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc

from utils.graphs.UTV0203_graph_utils import dist_total_donations, vertical_percentage_graph, single_vertical_percentage_graph
from utils.data.UTV0203_data_utils import get_data, process_data, get_region_names, get_region_values

from app import app
from homepage import navbar, footer

####################### Data processing ######################
TopVolsMotivations_2018, TopVolsBarriers_2018, TopVolsPercTotHours_2018, TopVolsPercTotVols_2018, TopVolsVolRates_2018, TopVolsDemoLikelihoods = get_data()

data = [TopVolsMotivations_2018, TopVolsBarriers_2018, TopVolsPercTotHours_2018, TopVolsPercTotVols_2018, TopVolsVolRates_2018, TopVolsDemoLikelihoods]

process_data(data)

region_values = get_region_values()
region_names = get_region_names()

demo_names = list(set(TopVolsDemoLikelihoods["Group"]))
demo_names.remove('État civil (original)')
# demo_names.remove('')

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
                        html.H1('Comprendre Les Bénévoles Très Engagé.E.S'),
                        # html.Span(
                        #     'David Lasby',
                        #     className='meta'
                        #     )
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
    # Note: filters put in separate container to make floating element later
   dbc.Container(
       [
        html.Div(["Sélectionnez une région:",
            dcc.Dropdown(
                      id='region-selection',
                      options=[{'label': region_names[i], 'value': region_values[i]} for i in range(len(region_values))],
                      value='CA',
                      style={'verticalAlgin': 'middle'}
                  ),
            ],
            className='col-md-10 col-lg-8 mx-auto mt-4'
        ),
        ], style={'backgroundColor':'F4F5F6'},
    className='sticky-top bg-light mb-2', fluid=True), 
   dbc.Container(
       dbc.Row([
            html.Div(
                [
                    dcc.Markdown('''
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, un peu plus de deux personnes sur cinq (41 %) au Canada ont fait du bénévolat pour un organisme de bienfaisance ou à but non lucratif pendant l’année qui l’a précédée. Ces bénévoles ont fait don en moyenne de 131 heures par personne, soit une contribution de presque 1,7 milliard d’heures de bénévolat par année.
                    ''',className='mt-4'),
                    dcc.Markdown('Bien que de nombreuses personnes fassent du bénévolat au Canada, la majorité des heures de bénévolat est attribuable à une petite minorité de bénévoles. Nous analysons ci-dessous les caractéristiques personnelles et économiques de ces personnes, les causes qu’elles soutiennent, leurs motivations et les freins qui les empêchent de faire encore plus de bénévolat. Nous décrivons dans le texte les résultats au niveau national et, pour obtenir des précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer légèrement des résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.', className='mt-4')
                ], className='col-md-10 col-lg-8 mx-auto',
            ),
            # Donation rate & average donation amount by method graph
            html.Div(
                [
                    html.H4('Définition des bénévoles très engagé.e.s',className='mt-3'),
                    dcc.Markdown('''
                    Le graphique ci-dessous regroupe les bénévoles en quatre groupes, selon leur nombre d’heures de bénévolat. À l’échelle nationale, les bénévoles très engagé.e.s — 25 % des bénévoles qui ont fait don du plus grand nombre d’heures — ont représenté collectivement 78 % du total des heures de bénévolat. En revanche, la moitié des bénévoles qui faisaient don du moindre nombre d’heures de bénévolat représentaient ensemble 7 % du total des heures, et le quart suivant, par ordre d’importance croissante, en représentait 15 %.
                    '''),
                    # Distribution of total time by hours volunteered
                    dcc.Graph(id='TopVolsTotalHours', style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Key personal & economic characteristics
            html.Div(
                [
                    html.Div([
                        html.H4('Qui sont les bénévoles très engagé.e.s?',className='mt-3'),
                        html.P("La probabilité d’être une personne bénévole très engagé.e varie selon les caractéristiques personnelles et économiques. En effet, les bénévoles les plus engagé.e.s ont tendance à se concentrer dans des groupes particulièrement susceptibles de faire du bénévolat et à faire don de plus d’heures de leur temps. D’une façon générale, la probabilité de se classer dans le groupe des bénévoles très engagé.e.s a tendance à augmenter avec l’âge et avec le niveau d’éducation formelle et à décroître avec le revenu du ménage. Les bénévoles très engagé.e.s ont également tendance à être particulièrement bien représentés parmi les personnes qui ne font pas partie de la population active, les personnes veuves et celles qui assistent chaque semaine aux offices religieux."),              
                    ]),
                    html.Div([
                        "Caractéristiques démographiques: ",
                        dcc.Dropdown(
                            id='demo-selection',
                            options=[{'label': i, 'value': i} for i in demo_names],
                            value="Groupe d'âge")
                        ], 
                        style={'marginTop': 50, 'width': '100%', 'verticalAlign': 'middle'}),
                    # Likelihood of being a top volunteer by demographic characteristic
                    html.Div([
                        dcc.Graph(id='TopVolsDemographics', style={'marginTop': marginTop})
                    ]),
                    # The causes supported by top volunteers
                    html.Div([
                        html.H4("Causes soutenues par les bénévoles très engagé.e.s",className='mt-3'),
                        html.P("Les bénévoles très engagé.e.s ont plus tendance que les autres bénévoles à soutenir de nombreuses causes. À l’échelle nationale, par comparaison avec les autres bénévoles, presque deux fois plus de bénévoles très engagé.e.s ont plus tendance à faire don de leur temps aux hôpitaux et aux organismes du secteur des arts et de la culture, environ la moitié d’entre eux ont plus tendance à faire don de leur temps aux organismes religieux et à ceux du secteur du sport et des loisirs et environ le tiers d’entre eux aux organismes du secteur des services sociaux. Les bénévoles très engagé.e.s et les autres bénévoles ont à peu près tout aussi tendance à soutenir toutes les autres causes."),
                        # Levels of support by cause, top volunteers vs. regular volunteers
                        html.Div([
                            dcc.Graph(id='TopVolsSubSecSupport', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    #Top volunteer motivations
                    html.Div([
                        html.H4("Motivations des bénévoles très engagé.e.s",className='mt-3'),
                        html.P("On a demandé aux bénévoles lequel ou lesquels de douze facteurs jouaient un rôle important dans leurs décisions de faire du bénévolat. Les bénévoles très engagé.e.s étaient plus susceptibles de faire état de quasiment tous les facteurs de motivation. À l’échelle nationale, le bénévolat pour mettre en application leurs compétences et leurs expériences, pour améliorer leur santé et leur bien-être et pour prendre conscience de leurs points forts et de leurs aptitudes constituaient les différences les plus importantes dans les facteurs de motivation des bénévoles. Bien que les croyances religieuses et spirituelles soient des motivations relativement peu courantes, elles importent beaucoup plus aux bénévoles les plus engagé.e.s. Les bénévoles les plus engagé.e.s sont à peu près aussi susceptibles de faire don de leur temps parce que des amis ou des membres de leur famille sont bénévoles ou pour augmenter leurs possibilités d’emploi."),
                        # Motivations for volunteering, top volunteers vs. regular volunteers
                        html.Div([
                            dcc.Graph(id='TopVolsMotivations', style={'marginTop': marginTop}),

                        ]),
                    ]),
                    # Top donor barriers
                    html.Div([
                        html.H4("Freins rencontrés par les bénévoles très engagé.e.s",className='mt-3'),
                        html.P("Comme pour les facteurs de motivation, on a demandé aux bénévoles lequel ou lesquels de douze facteurs différents les avaient empêchés de faire don de plus de temps pendant les 12 mois précédant l’enquête. À l’échelle nationale, la raison la plus fréquente pour ne pas faire plus de bénévolat, et de loin, est la conviction d’avoir déjà fait don d’assez de temps, suivie par les coûts financiers du bénévolat et les problèmes de santé ou les handicaps physiques. Quant aux freins qui empêchent les bénévoles de devenir des bénévoles très engagé.e.s, les plus puissants (dans la mesure où ils sont signalés le plus souvent par les autres bénévoles) sont l’impossibilité de s’engager à long terme, l’absence de sollicitation, ne pas savoir comment s’engager davantage et les dons d’argent de préférence aux dons de temps."),
                        #Barriers to volunteering more, top volunteers vs. regular volunteers
                        html.Div([
                            dcc.Graph(id='TopVolsBarriers', style={'marginTop': marginTop})

                        ]),
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'

            ),
        ]),
   ),
   footer
])

################## Callbacks #################
@app.callback(
    dash.dependencies.Output('TopVolsTotalHours', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff2 = TopVolsPercTotVols_2018[TopVolsPercTotVols_2018['Region'] == region]
    dff1 = TopVolsPercTotHours_2018[TopVolsPercTotHours_2018['Region'] == region]
    # dff1 = dff1.replace("", "")
    # dff1 = dff1.replace("", "")
    # dff1 = dff1.replace("", "")
    # dff1 = dff1.replace("", "")
    
    dff1 = dff1.replace("% volunteers", "% bénévoles")
    # name1 = "% volunteers"
    name1 = "% bénévoles"
    
    dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
    name2 = "% heures de bénévolat"
    # name2 = "% volunteer hours"

    title = '{}, {}'.format("Répartition des heures de bénévolat totales", region)
    return dist_total_donations(dff1, dff2, name1, name2, title)

@app.callback(
    dash.dependencies.Output('TopVolsDemographics', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('demo-selection', 'value')
    ])
def update_graph(region, demo):
    dff = TopVolsDemoLikelihoods[TopVolsDemoLikelihoods['Region'] == region]
    dff = dff[dff['Group'] == demo]

    title = '{}, {}'.format("Probabilité d'être un.e bénévole très engagé.e selon " + str(demo).lower(), region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('TopVolsSubSecSupport', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = TopVolsVolRates_2018[TopVolsVolRates_2018['Region'] == region]
    dff = dff.replace('Health', 'Santé')
    dff = dff.replace('Social services', 'Services sociaux')
    dff = dff.replace('Hospitals', 'Hôpitaux')
    dff = dff.replace('Grant-making, fundraising', 'Subventions, collecte de fonds')
    dff = dff.replace('Grantmaking, fundraising', 'Subventions, collecte de fonds')
    dff = dff.replace('Sports & recreation', 'Sport et loisir')
    dff = dff.replace('Sports & Recreation', 'Sport et loisir')
    dff = dff.replace('Education & research', 'Éducation et recherche')
    dff = dff.replace('Environment', 'Environnement')
    dff = dff.replace('Law, advocacy & politics', 'Droit, plaidoyer et politique')
    dff = dff.replace('Law, advocacy', 'Droit, plaidoyer et politique')
    dff = dff.replace('Arts & culture', 'Arts et culture')
    dff = dff.replace('Universities & colleges', 'Universités et collèges')
    dff = dff.replace('Development & housing', 'Aménagement et logement')
    dff = dff.replace('Other', 'Autre')
    dff = dff.replace('Business & professional', 'Entreprises et professionnels')
    dff = dff.replace('Top volunteer', 'Bénévoles très engagé.e.s')
    dff = dff.replace('Regular volunteer', 'Autres bénévoles')
    
    name1 = "Bénévoles très engagé.e.s"
    name2 = "Autres bénévoles"

    title = '{}, {}'.format("Niveaux de soutien selon la cause, bénévoles très engagé.e.s et autres bénévoles ", region)
    return vertical_percentage_graph(dff, title, name1, name2)

@app.callback(
    dash.dependencies.Output('TopVolsMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = TopVolsMotivations_2018[TopVolsMotivations_2018['Region'] == region]
    
    dff = dff.replace('Top volunteer', 'Bénévoles très engagé.e.s')
    dff = dff.replace('Regular volunteer', 'Autres bénévoles')
    
    name1 = "Bénévoles très engagé.e.s"
    name2 = "Autres bénévoles"
    # name1 = "Top volunteer"
    # name2 = "Regular volunteer"

    title = '{}, {}'.format("Motivations du bénévolat, bénévoles très engagé.e.s et autres bénévoles", region)
    return vertical_percentage_graph(dff, title, name1, name2)

@app.callback(
    dash.dependencies.Output('TopVolsBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = TopVolsBarriers_2018[TopVolsBarriers_2018['Region'] == region]
    dff = dff.replace('Top volunteer', 'Bénévoles très engagé.e.s')
    dff = dff.replace('Regular volunteer', 'Autres bénévoles')
    
    name1 = "Bénévoles très engagé.e.s"
    name2 = "Autres bénévoles"
    # name1 = "Top volunteer"
    # name2 = "Regular volunteer"

    title = '{}, {}'.format("Barriers to volunteering more, top volunteers vs. regular volunteers", region)
    return vertical_percentage_graph(dff, title, name1, name2)


