import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd

from utils.home_button import gen_home_button
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc
import os

from utils.data.UTD0103_data_utils import get_data, process_data, get_region_values, get_region_names
from utils.graphs.UTD0103_graph_utils import *

from app import app
from homepage import footer #navbar, footer

####################### Data processing ######################
TopDonorsMotivations_2018, TopDonorsBarriers_2018, TopDonorsPercTotDonations_2018, TopDonorsPercTotDonors_2018, TopDonorsDonRates_2018, TopDonorsDemoLikelihoods = get_data()

data = [TopDonorsMotivations_2018, TopDonorsBarriers_2018, TopDonorsPercTotDonations_2018, TopDonorsPercTotDonors_2018, TopDonorsDonRates_2018, TopDonorsDemoLikelihoods]
process_data(data)

region_values = get_region_values()
region_names = get_region_names()
demo_names = TopDonorsDemoLikelihoods["Group"].unique()

###################### App layout ######################
navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                # dcc.Link("Home", href="/")
                dbc.NavLink("À propos", href="https://www.donetbenevolat.ca/",external_link=True)
            ),
            dbc.NavItem(
                dbc.NavLink("EN", href="http://app.givingandvolunteering.ca/Understanding_top_donors_2018",external_link=True)
            ),
        ],
        brand="Centre Canadien de Connaissances sur les Dons et le Bénévolat",
        brand_href="/",
        color="#4B161D",
        dark=True,
        sticky='top'
    )
home_button = gen_home_button()
marginTop = 20

layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1('Comprendre les grand.e.s. donateur.trice.s'),
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
        dbc.Row([
           dbc.Col(
               html.Div([
                   "Sélectionnez une région:",
                   dcc.Dropdown(
                      id='region-selection',
                      options=[{'label': region_values[i], 'value': region_values[i]} for i in range(len(region_values))],
                      value='CA',
                    #   style={'verticalAlign': 'middle'},
                     # style={'width': '100%', 'display': 'inline-block', 'align-items': 'center', 'justify-content': 'center'},
                      style = {'width': '96%','padding-left':'3%', 'padding-right':'1%'}
              ),
                ],className="m-2 p-2"),
            # html.Div(["Select a region:",
            #       dcc.Dropdown(
            #           id='region-selection',
            #           options=[{'label': region_names[i], 'value': region_values[i]} for i in range(len(region_values))],
            #           value='CA',
            #           style={'verticalAlign': 'middle'}
            #       ),
            #       ],className="m-2 p-2"),
            ),
           
            #    html.Div([
            #        "Select a demographic characteristic:",
            #        dcc.Dropdown(id='demo-selection',
            #             options=[{'label': i, 'value': i} for i in demo_names],
            #             value="Personal income category")
            #     ],className="m-2 p-2"),
            ]),
    ],className='sticky-top bg-light mb-2', fluid=True),
   dbc.Container(
       dbc.Row([
            html.Div(
                [
                    dcc.Markdown('''
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, un peu plus de deux tiers des personnes (68 %) au Canada ont donné à un organisme de bienfaisance ou à but non lucratif pendant l’année qui l’a précédée. Le montant moyen de ces dons était de 569 $ par personne et leur total national s’est élevé à approximativement 11,9 milliards $.
                    ''',className='mt-4'),
                    dcc.Markdown('''
                    Bien que la majorité des personnes fassent des dons d’argent au Canada, la vaste majorité de ceux-ci proviennent d’une petite minorité de donateur.trice.s. Nous analysons ci-dessous leurs caractéristiques personnelles et économiques, les causes qu’elles soutiennent, leurs motivations et les freins qui les empêchent de donner encore plus. Nous décrivons dans le texte ci-dessous les tendances nationales et, pour obtenir des précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer légèrement des résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires. 
                    '''),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Donation rate & average donation amount by method graph
            html.Div(
                [
                    html.H4('Définition des grand.e.s donateur.trice.s',className='mt-3'),
                    dcc.Markdown('''
                    Le graphique ci-dessous regroupe les donateur.trice.s en quatre catégories, selon le montant de leurs dons, le montant total des dons et les dons aux organismes laïcs et religieux. À l’échelle nationale, les personnes appartenant à ce groupe, soit 25 % des personnes qui contribuent le plus financièrement, représentaient collectivement 84 % du montant total des dons. Par contre, la moitié des personnes qui ont contribué le moins ne représentaient à elles toutes que 5 % du montant total des dons et le quart suivant, selon le montant de leurs dons en ordre d’importance croissante, en représentaient 11 %. S’agissant plus particulièrement des dons aux organismes religieux et laïcs, les tendances générales sont très similaires et les principales différences sont doubles : les personnes qui soutiennent les organismes religieux ont tendance à donner des montants plus importants et les dons des grand.e.s donateur.trice.s aux organismes laïcs représentent une proportion du montant total des dons inférieure à celle des grand.e.s donateur.trice.s aux organismes religieux.
                    '''),
                    #html.P("Focussing more specifically on donations to religious and secular organizations, the overall trends are very similar with the major differences being that religious donors tend to give larger amounts and top secular donors account for a smaller proportion of total donations than top religious donors."),
                    # Distribution of total donations by amount donated
                    dcc.Graph(id='TopDonorsTotalDonations', style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Key personal & economic characteristics
            html.Div(
                [
                    html.Div([
                        html.H4('Qui sont les grand.e.s donateur.trice.s',className='mt-3'),
                        html.P("La probabilité de faire partie des grand.e.s donateur.trice.s au Canada varie selon les caractéristiques personnelles et économiques. En effet, les personnes qui donnent le plus ont tendance à se concentrer dans des groupes particulièrement enclins à donner et à donner d’importantes sommes. Par exemple, cette probabilité a tendance à augmenter avec l’âge et le niveau d’études. De même, les personnes veuves sont particulièrement enclines à donner le plus d’argent, tandis que les personnes qui ne se sont jamais mariées sont moins susceptibles de le faire. Les personnes qui assistent chaque semaine aux offices religieux sont particulièrement enclines à contribuer le plus largement, ce qui semble lié en grande partie aux montants importants qu’elles ont tendance à donner aux causes religieuses, mais elles sont également enclines à en faire de même au bénéfice des causes laïques. À l’échelle nationale, bien que la probabilité de contribuer financièrement le plus augmente généralement avec le revenu du ménage, les personnes aux revenus compris entre 100 000 $ et 124 999 $ ont nettement moins tendance à faire partie du groupe des grand.e.s donateur.trice.s, contrairement à cette tendance générale."),
                        # Likelihood of being a top donor by demographic characteristic
                        html.Div([
                            "Sélectionnez une caractéristique démographique:",
                            dcc.Dropdown(id='demo-selection',
                                         options=[{'label': i, 'value': i} for i in demo_names],
                                         value="Catégorie de revenu personnel")
                            ],className="m-2 p-2"),
                        dcc.Graph(id='TopDonorsDemographics', style={'marginTop': marginTop}),
                    ]),
                    #The causes supported by top donors
                    html.Div([
                        html.H4("Causes soutenues par les grand.e.s donateur.trice.s",className='mt-3'),
                        html.P("Les grand.e.s donateur.trice.s soutiennent toutes les causes plus fréquemment, lorsque l’on compare avec les autres donateur.trice.s. À l’échelle nationale, ces personnes sont environ quatre fois plus enclines à donner aux organismes du secteur du développement international et de l’aide internationale, trois fois plus enclines à donner aux universités et aux collèges, ainsi qu’aux organismes des secteurs du droit, du plaidoyer et de la politique, et environ deux fois plus enclines à donner aux organismes du secteur des arts et de la culture et aux organismes religieux.  En ce qui a trait plus particulièrement aux causes religieuses et laïques, la probabilité plus élevée de donner à des organismes religieux est principalement attribuable aux grand.e.s donateur.trice.s soutenant les causes religieuses, tandis que la probabilité plus élevée de donner à des organismes laïques est principalement due aux grand.e.s donateur.trice.s soutenant des causes laïques. Seuls les organismes du secteur du développement international et de l’aide internationale sont nettement plus susceptibles d’être soutenus par ces deux groupes de personnes."),
                        # Levels of support by cause, top donors vs. regular donors
                        html.Div([
                            # html.H6("Donation rate & average donation amount by gender"),
                            dcc.Graph(id='TopDonorsSubSecSupport', style={'marginTop': marginTop}),

                        ]),
                    ]),
                    # Top donor motivations
                    html.Div([
                        html.H4("Motivations des grand.e.s donateur.trice.s",className='mt-3'),
                        html.P("Donors were asked whether any of eight factors were important to their decisions to donate. Top donors were more likely than regular donors to report each given motivation for giving. Nationally, the largest motivational differences were with religious and spiritual factors and the tax credits donors receive in return for donating. Looking specifically at religious and secular top donors, religious and spiritual factors were more important among religious top donors, while most other factors were somewhat more important among secular top donors. Tax credits played a very similar role among both religious and secular top donors."),
                        # Motivations for giving, top donors vs. regular donors
                        html.Div([
                            # html.H6("Donation rate & average donation amount by age"),
                            dcc.Graph(id='TopDonorsMotivations', style={'marginTop': marginTop}),

                        ]),
                    ]),
                    # Top donor barriers
                    html.Div([
                        html.H4("Top donor barriers",className='mt-3'),
                        html.P("On a demandé aux donateur.trice.s si un ou plusieurs de huit facteurs jouaient un rôle important dans leurs décisions de donner. Les personnes aux dons les plus importants signalaient chacun de ces facteurs de motivation plus fréquemment que les personnes aux dons ordinaires. À l’échelle nationale, les facteurs religieux et spirituels et les crédits d’impôt reçus en échange des dons constituaient les différences les plus importantes dans les facteurs de motivation. En ce qui concerne les grand.e.s donateur.trice.s qui soutiennent des causes laïques et religieuses, les facteurs religieux et spirituels importaient plus aux personnes qui contribuaient le plus aux causes religieuses, tandis que la majorité des autres facteurs importaient légèrement plus à celles qui contribuaient le plus aux causes laïques. Les crédits d’impôt jouaient un rôle très comparable dans les motivations de ces deux groupes de personnes."),
                        # Barriers to giving more, top donors vs. regular donors
                        html.Div([
                            # html.H6("Donation rate & average donation amount by formal education"),
                            dcc.Graph(id='TopDonorsBarriers', style={'marginTop': marginTop})

                        ]),
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'

            ),
        ]),
   ),
   footer
])

################## Graphs #################


################## Callbacks #################

@app.callback(
    dash.dependencies.Output('TopDonorsTotalDonations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff2 = TopDonorsPercTotDonors_2018[TopDonorsPercTotDonors_2018['Region'] == region]
    dff1 = TopDonorsPercTotDonations_2018[TopDonorsPercTotDonations_2018['Region'] == region]

    name2 = "% donateur.trice.s"
    name1 = "% valeur des dons"

    title = '{}, {}'.format("Répartition de la totalité des dons selon leur montant", region)
    return dist_total_donations(dff1, dff2, name1, name2, title)

@app.callback(
    dash.dependencies.Output('TopDonorsDemographics', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('demo-selection', 'value')
    ])
def update_graph(region, demo):
    dff = TopDonorsDemoLikelihoods[TopDonorsDemoLikelihoods['Region'] == region]
    dff = dff[dff['Group'] == demo]

    title = '{}, {}'.format("Probabilité d’être un.e grand.e donateur.trice selon le profil démographique ", region)
    return triple_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('TopDonorsSubSecSupport', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = TopDonorsDonRates_2018[TopDonorsDonRates_2018['Region'] == region]

    title = '{}, {}'.format("Niveaux de soutien selon la cause, <br> grand.e.s donateur.trice.s et donateur.trice.s ordinaires", region)
    return vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('TopDonorsMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = TopDonorsMotivations_2018[TopDonorsMotivations_2018['Region'] == region]

    title = '{}, {}'.format("Motivations des dons, grand.e.s donateur.trice.s <br> et donateur.trice.s ordinaires", region)
    return vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('TopDonorsBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = TopDonorsBarriers_2018[TopDonorsBarriers_2018['Region'] == region]

    title = '{}, {}'.format("Freins empêchant de donner plus, grand.e.s <br> donateur.trice.s et donateur.trice.s ordinaires", region)
    return vertical_percentage_graph(dff, title)
