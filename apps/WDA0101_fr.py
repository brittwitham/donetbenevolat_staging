import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
# from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State, ClientsideFunction

from utils.graphs.WDA0101_graph_utils import don_rate_avg_don_amt_prv, don_rate_avg_don, perc_don_perc_amt, prim_cause_num_cause, forms_of_giving, fr_don_rate_avg_don_amt_prv
from utils.data.WDA0101_data_utils import get_data, get_region_values, process_data, process_data_num, get_region_names, get_region_values

from app import app
from homepage import navbar, footer

####################### Data processing ######################

[DonRates_2018, AvgTotDon_2018, AvgNumCauses_2018, FormsGiving_2018, TopCauseFocus_2018, PropTotDon_2018, PropTotDonAmt_2018] = get_data()
data = [DonRates_2018, AvgTotDon_2018, FormsGiving_2018, TopCauseFocus_2018, PropTotDon_2018, PropTotDonAmt_2018]
data_num = [AvgNumCauses_2018]
# values = ["Use with caution", "Estimate suppressed", ""]
values = ["Utiliser avec précaution", 'Estimation supprimée', '']
status_names = ["État civil", "Situation d'activité", "Statut d'immigration"]

process_data(data)
process_data_num(data_num)
#
# Extract info from data for selection menus
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
                        html.H1('Qui Donne Aux Organismes Caritatifs et Combien?'),
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
        dbc.Row(
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
            ),id='sticky-dropdown'),
    ],className='sticky-top bg-light mb-2', fluid=True),
   dbc.Container(
       dbc.Row([
            # Starting text
            html.Div(
                [
                    html.H4('Formes de don'),
                    html.P("D'après l'Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, presque neuf personnes sur dix au Canada ont contribué financièrement ou en nature, sous une forme ou une autre, aux organismes de bienfaisance ou à but non lucratif pendant l'année qui l'a précédée. Plus des deux tiers de ces personnes ont donné de l'argent ou des articles ménagers, des jouets et des vêtements et environ la moitié d'entre elles ont donné des aliments. Environ un tiers d'entre elles ont déclaré avoir fait un legs dans leur testament ou par le biais d'un autre instrument de planification financière à un organisme caritatif. Le montant moyen de ces dons aux organismes de bienfaisance et à but non lucratif était de 569 $ et leur total général s'est élevé à approximativement 11,9 milliards $."),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Forms of Giving
            html.Div(
                [
                    
                    dcc.Graph(id='FormsGiving_fr', style={'marginTop': 20}),
                    html.P("La probabilité de faire un don financier et le montant habituel des dons variaient selon le lieu de résidence. En général, la proportion de donateur.trice.s avait tendance à être plus élevée dans l’Est, tandis que le montant habituel des dons avait tendance à être supérieur dans l’Ouest. Plus précisément, les personnes habitant à Terre-Neuve-et-Labrador et à l’Île-du-Prince-Édouard étaient les plus enclines à donner, alors que celles de la Colombie-Britannique étaient les moins enclines à le faire. Les personnes habitant dans l’Ouest du Canada, en Alberta plus particulièrement, avaient tendance à faire des dons supérieurs à la moyenne, tandis que celles habitant au Québec avaient tendance à faire des dons nettement inférieurs."),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Donation rate & average donation amount by province
            html.Div(
                [
                    # html.H4('Donation rate & average donation amount by province'),
                    dcc.Graph(id='DonRateAvgDonAmt-prv_fr', figure=fr_don_rate_avg_don_amt_prv(DonRates_2018, AvgTotDon_2018)),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Key personal & economic characteristics
            html.Div(
                [
                    html.H3('Caractéristiques personnelles et économiques '),
                    html.P("En plus des variations selon les lieux de résidence, les tendances des dons avaient également tendance à fluctuer selon les caractéristiques personnelles et économiques des donateur.trices. Nous examinons ci-dessous les tendances de plusieurs mesures clés des dons:"),
                    html.Ul([
                        html.Li('la probabilité de donner et le montant moyen des contributions,'),
                        html.Li('les pourcentages de donateur.trice.s et la valeur totale des dons pour chaque sous-groupe,'),
                        html.Li('la concentration moyenne des dons sur la cause principale et le nombre moyen de causes soutenues.'),
                    ]),
                    html.P("À elles toutes, ces mesures brossent un tableau détaillé du bassin de donateur.trices.s au Canada, ainsi que de l’ampleur et de la portée de leur soutien des organismes de bienfaisance et à but non lucratif. Nous décrivons dans le texte ci-dessous les tendances nationales et, pour obtenir des précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer des résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires."),
                    # Gender
                    html.Div([
                        html.H4("Genre"),
                        html.P("Au niveau national, les femmes sont relativement plus enclines à donner que les hommes. Les hommes et les femmes ont tendance à donner des montants très similaires, le montant moyen des dons étant pratiquement impossible à différencier statistiquement. Cette tendance est uniforme dans toutes les régions."),
                        # Donation rate & average donation amount by gender
                        html.Div([
                            # html.H6("Donation rate & average donation amount by gender"),
                            dcc.Graph(id='DonRateAvgDonAmt-Gndr_fr', style={'marginTop': marginTop}),
                            html.P("La probabilité de donner des femmes, supérieure à celle des hommes, est partiellement compensée par les montants inférieurs de leurs dons. Les femmes représentent un pourcentage de la valeur totale des dons légèrement supérieur à celui auquel on pourrait s'attendre, compte tenu de leur nombre."),
                        ]),
                        # Percentage of donors & total donation value by gender
                        html.Div([
                            # html.H6("Percentage of donors & total donation value by gender"),
                            dcc.Graph(id='PercDon-Gndr_fr', style={'marginTop': marginTop}),
                            html.P("Sur le plan de la tendance des donateur.trice.s à répartir leur soutien entre différentes causes, la concentration des dons des femmes et des hommes sur leur cause principale est très similaire. À l’échelle nationale, les deux genres attribuent un peu plus des trois quarts de leur soutien financier à leur cause principale. Bien que leur degré de concentration de leurs dons sur leur cause principale soit très similaire, les femmes sont un peu plus susceptibles de soutenir des causes secondaires, comme le montre le nombre légèrement supérieur, en moyenne, des causes qu’elles soutiennent."),
                        ]),
                        # Focus on primary cause & average number of causes supported by gender
                        html.Div([
                            # html.H6("Focus on primary cause & average number of causes supported by gender"),
                            dcc.Graph(id='PrimCauseNumCause-Gndr_fr', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("De façon générale, à la fois la probabilité de donner et les montants habituels ont tendance à augmenter avec l’âge. Par rapport aux tendances générales des dons, les personnes âgées de 15 à 24 ans sont moins susceptibles, celles âgées de 25 à 54 ans à peu près aussi susceptibles et celles âgées de 55 ans et plus légèrement plus susceptibles de donner, du moins au niveau national. Les montants habituels des dons des personnes de ces groupes d’âge suivent une tendance largement similaire."),
                        # Donation rate & average donation amount by age
                        html.Div([
                            # html.H6("Donation rate & average donation amount by age"),
                            dcc.Graph(id='DonRateAvgDonAmt-Age_fr', style={'marginTop': marginTop}),
                            html.P("En raison de leur plus forte probabilité de donner et du montant généralement plus important de leurs dons, la place des personnes âgées de 55 ans ou plus dans les dons est disproportionnée au Canada :  elles représentent des pourcentages de la valeur totale des dons supérieurs à leur représentation au sein de la population."),
                            # html.Br(),
                        ]),
                        # Percentage of donors & total donation value by age
                        html.Div([
                            # html.H6("Percentage of donors & total donation value by age"),
                            dcc.Graph(id='PercDon-Age_fr', style={'marginTop': marginTop}),
                            html.P("Étant donné leur plus forte probabilité de donner et les montants habituellement supérieurs de leurs dons, les personnes diplômées de l’université occupent une place disproportionnée dans les dons. Au niveau national, elles représentent  un peu moins d'un tiers des personnes au Canada, mais presque la moitié de la valeur totale des dons. Par contre, les personnes non titulaires d’un diplôme d’études secondaires représentent environ un dixième des personnes au Canada et six pour cent de la valeur totale des dons."),
                            # html.Br(),
                        ]),
                        # Focus on primary cause & average number of causes supported by age
                        html.Div([
                            # html.H6("Focus on primary cause & average number of causes supported by age"),
                            dcc.Graph(id='PrimCauseNumCause-Age_fr', style={'marginTop': marginTop}),
                            html.Br(),
                        ]),
                    ]),
                    # Formal Education
                    html.Div([
                        html.H5("Éducation formelle"),
                        html.P("À la fois la probabilité de donner et les montants habituels des dons vont de pair avec le niveau d’éducation formelle. Au niveau national, les personnes titulaires d’un diplôme universitaire étaient environ 1,4 fois plus susceptibles de donner que les personnes non titulaires d’un diplôme d’études secondaires. Vraisemblablement en raison de leurs rémunérations supérieures, les donateur.trice.s au niveau d’étude supérieur ont également tendance à donner des montants plus importants. À l’échelle nationale, les dons moyens des personnes ayant étudié à l’université étaient environ deux fois et demie plus élevés que ceux des personnes n’ayant pas achevé leurs études secondaires."),
                        # Donation rate & average donation amount by Formal Education
                        html.Div([
                            # html.H6("Donation rate & average donation amount by formal education"),
                            dcc.Graph(id='DonRateAvgDonAmt-Educ_fr', style={'marginTop': marginTop}),
                            html.P("Étant donné leur plus forte probabilité de donner et les montants habituellement supérieurs de leurs dons, les personnes diplômées de l’université occupent une place disproportionnée dans les dons. Au niveau national, elles représentent  un peu moins d'un tiers des personnes au Canada, mais presque la moitié de la valeur totale des dons. Par contre, les personnes non titulaires d’un diplôme d’études secondaires représentent environ un dixième des personnes au Canada et six pour cent de la valeur totale des dons."),
                            # html.Br(),
                        ]),
                        # Percentage of donors & total donation value by formal education
                        html.Div([
                            # html.H6("Percentage of donors & total donation value by formal education"),
                            dcc.Graph(id='PercDon-Educ_fr', style={'marginTop': marginTop}),
                            html.P("Bien que les donateur.trice.s non titulaires d’un diplôme d’études secondaires concentrent légèrement plus leurs dons sur leur cause principale, l’écart entre les niveaux d’éducation formelle est faible à cet égard. Le niveau d’études se répercute cependant de manière sensible sur le nombre de causes soutenues, presque certainement en raison du montant habituel des dons allant de pair avec les niveaux d’éducation formelle supérieurs."),
                            # html.Br(),
                        ]),
                        # Focus on primary cause & average number of causes supported by formal education
                        html.Div([
                            # html.H6("Focus on primary cause & average number of causes supported by formal education"),
                            dcc.Graph(id='PrimCauseNumCause-Educ_fr', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # household income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("La relation entre les dons et le revenu du ménage est quelque peu complexe, en raison des autres caractéristiques personnelles des membres des ménages aux différents niveaux de revenu. En général, la probabilité de donner et les montants moyens des dons ont tendance à augmenter en fonction du revenu du ménage, malgré certaines fluctuations et la manifestation plus claire de cette tendance aux extrémités de l’échelle des revenus."),
                        # Donation rate & average donation amount by household income
                        html.Div([
                            # html.H6("Donation rate & average donation amount by household income"),
                            dcc.Graph(id='DonRateAvgDonAmt-Inc_fr', style={'marginTop': marginTop}),
                            html.P("En raison des variations du montant des dons habituels, au niveau national, les membres des ménages au revenu annuel inférieur à 75 000 $ ont tendance à occuper une place excessivement faible dans les dons. En revanche, les membres des ménages de la catégorie supérieure de revenu ont tendance à occuper une place beaucoup plus importante, en représentant moins d’un tiers des personnes au Canada, mais deux cinquièmes de la valeur totale des dons."),
                            # html.Br(),
                        ]),
                        # Percentage of donors & total donation value by household income
                        html.Div([
                            # html.H6("Percentage of donors & total donation value by household income"),
                            dcc.Graph(id='PercDon-Inc_fr', style={'marginTop': marginTop}),
                            # html.Br(),
                        ]),
                        # Focus on primary cause & average number of causes supported by household income
                        html.Div([
                            html.P("Dans l’ensemble, la concentration des dons sur la cause principale a tendance à être inversement proportionnelle au revenu du ménage, tandis que le nombre de causes soutenues a tendance à augmenter avec le revenu du ménage."),
                            # html.H6("Focus on primary cause & average number of causes supported by household income"),
                            dcc.Graph(id='PrimCauseNumCause-Inc_fr', style={'marginTop': marginTop}),
                            html.Br(),
                        ]),
                    ]),
                    # Religious attendance
                    html.Div([
                        html.H5("Pratique religieuse"),
                        html.P("La participation aux traditions religieuses a une incidence importante à la fois sur la probabilité de donner et sur les montants habituels des dons. La probabilité de donner et les montants moyens des dons augmentent l’une et l’autre avec la fréquence de la pratique religieuse. Au niveau national, la probabilité de donner était, pour les personnes qui assistaient au moins une fois par semaine aux offices religieux, supérieure d’environ un tiers à celle des personnes qui n’assistent jamais aux services. De plus, leurs dons étaient près de cinq fois supérieurs, en moyenne, à ceux des personnes qui n’assistent jamais aux services. Bien qu’un grand nombre des dons des personnes plus assidues aux services sont au bénéfice des organisations religieuses, ce n’est pas exclusivement le cas. Pour obtenir des précisions à ce sujet, veuillez vous reporter à Les dons et le bénévolat pour les organisations religieuses, également sur le présent site."),
                        # Donation rate & average donation amount by religious attendance
                        html.Div([
                            # html.H6("Donation rate & average donation amount by religious attendance"),
                            dcc.Graph(id='DonRateAvgDonAmt-Relig_fr', style={'marginTop': marginTop}),
                            html.P("Étant donné leur probabilité plus forte de donner et, plus particulièrement, les montants importants qu’elles ont tendance à donner, les personnes qui assistent chaque semaine aux offices religieux représentent à peine moins de la moitié de la valeur totale des dons au niveau national, mais seulement 18 % des personnes au Canada. Au contraire, celles qui n’assistent jamais aux offices religieux représentent la moitié des personnes au Canada, mais à peu près un quart de la valeur totale des dons."),
                            # html.Br(),
                        ]),
                        # Percentage of donors & total donation value by religious attendance
                        html.Div([
                            # html.H6("Percentage of donors & total donation value by religious attendance"),
                            dcc.Graph(id='PercDon-Relig_fr', style={'marginTop': marginTop}),
                            html.P("Bien que les personnes qui assistent chaque semaine aux offices religieux affectent une proportion plutôt supérieure de leurs dons à leur cause principale (presque toujours celle d’une organisation religieuse), elles ont également tendance à soutenir un plus grand nombre de causes que celles qui n’assistent que très épisodiquement ou jamais aux offices religieux. Fait intéressant, ce sont les personnes qui assistent une fois par mois aux offices religieux qui concentrent le moins leurs dons sur leur cause principale et qui soutiennent habituellement le plus grand nombre de causes. Comme il fallait peut-être s’y attendre, étant donné leur faible probabilité de donner et leurs dons habituellement plus petits, ce sont les personnes qui n’assistent pas aux offices religieux qui ont tendance à soutenir le plus petit nombre de causes et à concentrer plutôt leurs dons sur leur cause principale."),
                            # html.Br(),
                        ]),
                        # Focus on primary cause & average number of causes supported by religious attendance
                        html.Div([
                            #html.H6("Focus on primary cause & average number of causes supported by religious attendance"),
                            dcc.Graph(id='PrimCauseNumCause-Relig_fr', style={'marginTop': marginTop}),
                            html.Br(),
                        ]),
                    ]),
                    # Other personal & economic characteristics
                    html.Div([
                        html.H5("Autres facteurs"),
                        html.P("Les autres caractéristiques personnelles et économiques significatives sont la situation matrimoniale, la situation d’emploi et le statut d’immigration. Grosso modo, les personnes mariées ou veuves sont généralement plus susceptibles de donner, et ce, en montants supérieurs, de même que les personnes occupant un emploi ou non membres de la population active (dont un grand nombre ont pris leur retraite). Au chapitre du statut d’immigration, les personnes nées au Canada donnent relativement plus souvent que celles ayant immigré au Canada, mais les personnes nouvellement arrivées au Canada ont tendance à donner des montants supérieurs. Pour obtenir plus de précisions sur les dons et le bénévolat des personnes nouvellement arrivées au Canada, reportez-vous à Les dons et le bénévolat des personnes nouvellement arrivées au Canada, également sur ce site Web."),
                        # Donation rate & average donation amount by religious attendance
                        # html.Div([
                        #     # html.H6("Donation rate & average donation amount by marital status"),
                        #     dcc.Graph(id='DonRateAvgDonAmt-MarStat', style={'marginTop': marginTop}),
                        #     # html.Br(),
                        # ]),
                        # Donation rate & average donation amount by labour force status
                        # html.Div([
                        #     # html.H6("Donation rate & average donation amount by labour force status"),
                        #     dcc.Graph(id='DonRateAvgDonAmt-Labour', style={'marginTop': marginTop}),
                        #     # html.Br(),
                        # ]),
                        # Donation rate & average donation amount by immigration status
                        # html.Div([
                        #     # html.H6("Donation rate & average donation amount by immigration status"),
                        #     dcc.Graph(id='DonRateAvgDonAmt-ImmStat', style={'marginTop': marginTop}),
                        #     html.P("Looking at the relative donation roles of the various sub-groups, those who are married or widowed tend to contribute disproportionately large proportions of total donations, while the smaller average donations made by single donors mean they account for a disproportionately small fraction of total donations. The relative role of donors does not vary significantly by labour force status, but New Canadians tend to play a slightly larger financial role in donations than their numbers would indicate."),
                        #     html.Br(),
                        # ]),
                        html.Div(['Sélectionner le statut:',
                                      dcc.Dropdown(
                                          id='status-selection1',
                                          options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                                          value='État civil',
                                          style={'verticalAlign': 'middle'}
                                      ),],
                                     style={'width': '50%', 'display': 'inline-block'}),
                        html.Div([
                            # html.H6("Donation rate & average donation amount by immigration status"),
                            dcc.Graph(id='DonRateAvgDonAmt-other_fr', style={'marginTop': marginTop}),
                            html.P("Quant à l’importance relative des divers sous-groupes dans les dons, les personnes mariées ou veuves ont tendance à représenter des proportions disproportionnellement élevées du total des dons, tandis que, en raison des montants moyens inférieurs de leurs dons, les célibataires représentent une fraction excessivement petite du total des dons. L’importance relative des donateur.trice.s ne varie pas de manière significative selon la situation d’emploi, mais l’importance financière des dons des personnes nouvellement arrivées au Canada a tendance à être légèrement supérieure à celle que leur nombre donnerait à penser."),
                            html.Br(),
                        ]),
                        # Percentage of donors & total donation value by marital status
                        # html.Div([
                        #     # html.H6("Percentage of donors & total donation value by marital status"),
                        #     dcc.Graph(id='PercDon-MarStat', style={'marginTop': marginTop}),
                        #     html.Br(),
                        # ]),
                        # # Percentage of donors & total donation value by labour force status
                        # html.Div([
                        #     # html.H6("Percentage of donors & total donation value by labour force status"),
                        #     dcc.Graph(id='PercDon-Labour', style={'marginTop': marginTop}),
                        #     html.Br(),
                        # ]),
                        # Percentage of donors & total donation value by immigration status
                        html.Div(['Sélectionner le statut:',
                                      dcc.Dropdown(
                                          id='status-selection2',
                                          options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                                          value='État civil',
                                          style={'verticalAlign': 'middle'}
                                      ),],
                                     style={'width': '50%', 'display': 'inline-block'}),
                        html.Div([
                            # html.H6("Percentage of donors & total donation value by immigration status"),
                            dcc.Graph(id='PercDon-other_fr', style={'marginTop': marginTop}),
                            html.Br(),
                            html.P("La mesure dans laquelle les personnes au Canada concentrent leur soutien sur leur cause principale ne semble pas varier de manière significative en fonction de leur situation matrimoniale ou de leur situation d’emploi. Les personnes mariées, veuves et, dans une moindre mesure, divorcées ont tendance à soutenir des causes relativement plus nombreuses, de même que les personnes qui ne font pas partie de la population active. Au chapitre du statut d’immigration, les personnes nouvellement arrivées au Canada et n’ayant pas encore obtenu leur résidence permanente ont tendance à concentrer davantage leur soutien sur leur cause principale et à soutenir moins de causes que les personnes nées au Canada."),
                        ]),
                        # Focus on primary cause & average number of causes supported by marital status
                        # html.Div([
                        #     # html.H6("Focus on primary cause & average number of causes supported by marital status"),
                        #     dcc.Graph(id='PrimCauseNumCause-MarStat', style={'marginTop': marginTop}),
                        #     html.Br(),
                        # ]),
                        # # Focus on primary cause & average number of causes supported by labour force status
                        # html.Div([
                        #     # html.H6("Focus on primary cause & average number of causes supported by labour force status"),
                        #     dcc.Graph(id='PrimCauseNumCause-Labour', style={'marginTop': marginTop}),
                        #     html.Br(),
                        # ]),
                        # # Focus on primary cause & average number of causes supported by immigration status
                        # html.Div([
                        #     # html.H6("Focus on primary cause & average number of causes supported by immigration status"),
                        #     dcc.Graph(id='PrimCauseNumCause-ImmStat', style={'marginTop': marginTop}),
                        #     html.Br(),
                        # ]),
                        html.Div(['Sélectionner le statut:',
                                      dcc.Dropdown(
                                          id='status-selection3',
                                          options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                                          value='État civil',
                                          style={'verticalAlign': 'middle'}
                                      ),],
                                     style={'width': '50%', 'display': 'inline-block'}),
                        html.Div([
                            # html.H6("Focus on primary cause & average number of causes supported by immigration status"),
                            dcc.Graph(id='PrimCauseNumCause-other3_fr', style={'marginTop': marginTop}),
                            html.Br(),
                        ]),
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'

            ),
        ]),
   ),
#    footer
])

# ###################### Graph functions ######################



# ###################### Callbacks ######################
app.clientside_callback(
    ClientsideFunction("clientside", "stickyHeader"),
    Output("sticky", "data-loaded_fr"),  # Just put some dummy output here
    [Input("sticky", "id")],  # This will trigger the callback when the object is injected in the DOM
)


@app.callback(
    # Output: change to graph-1
    dash.dependencies.Output('FormsGiving_fr', 'figure'),
    [
        # Input: selected region from region-selection (dropdown menu)
        # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    """
    Construct or update graph according to input from 'region-selection' dropdown menu.

    :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
    :return: Plot.ly graph object, produced by don_rate_avg_don().
    """
    # Donation rate data, filtered for selected region and demographic group (age group)
    # Corresponding name assigned
    dff1 = FormsGiving_2018[FormsGiving_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "All"]
    
    dff1['QuestionText'] = dff1['QuestionText'].replace('Financial donation', 'Don financier')
    dff1['QuestionText'] = dff1['QuestionText'].replace('Food bank', 'Banque alimentaire')
    dff1['QuestionText'] = dff1['QuestionText'].replace('In-kind', 'En nature')
    dff1['QuestionText'] = dff1['QuestionText'].replace('Bequest, planned gift', 'Leg, don planifié')

    # Format title according to dropdown input
    title = '{}, {}'.format("Formes de don", region)

    # Uses external function with dataframes, names, and title set up above
    return forms_of_giving(dff1, title)

# @app.callback(
#     dash.dependencies.Output('DonRateAvgDonAmt-prv_fr', 'figure'),
# #     )
# def update_graph():
    
#     name1 = "Taux de donateur.trice.s"

#     name2 = "Montant moyen des dons"

#     # title = 'Region selected: {}'.format(region)
#     title = '{}, {}'.format("Donation rate and average annual donation by province")

#     return don_rate_avg_don_amt_prv(DonRates_2018, AvgTotDon_2018, name1, name2, title)

@app.callback(
    dash.dependencies.Output('DonRateAvgDonAmt-Age_fr', 'figure'),
    [dash.dependencies.Input('region-selection', 'value')])
def update_graph(region):
    dff1 = DonRates_2018[DonRates_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Groupe d'âge"]
    name1 = "Taux de donateur.trice.s"

    dff2 = AvgTotDon_2018[AvgTotDon_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Groupe d'âge"]
    name2 = "Dons annuels moyens"
    
    # title = 'Region selected: {}'.format(region)
    title = '{}, {}'.format("Taux de donateur.trice.s et montant moyen des dons selon le groupe d'âge", region)

    return don_rate_avg_don(dff1, dff2, name1, name2, title)

@app.callback(
    # Output: change to graph-1
    dash.dependencies.Output('DonRateAvgDonAmt-Gndr_fr', 'figure'),
    [
        # Input: selected region from region-selection (dropdown menu)
        # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    """
    Construct or update graph according to input from 'region-selection' dropdown menu.

    :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
    :return: Plot.ly graph object, produced by don_rate_avg_don().
    """
    # Donation rate data, filtered for selected region and demographic group (age group)
    # Corresponding name assigned
    dff1 = DonRates_2018[DonRates_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Genre"]
    name1 = "Taux de donateur.trice.s"

    # Average annual donation data, filtered for selected region and demographic group (age group)
    # Corresponding name assigned
    dff2 = AvgTotDon_2018[AvgTotDon_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Genre"]
    name2 = "Dons annuels moyens"
    
    # Format title according to dropdown input
    title = '{}, {}'.format("Taux de donateur.trice.s et montant moyen des dons selon le genre", region)

    # Uses external function with dataframes, names, and title set up above
    return don_rate_avg_don(dff1, dff2, name1, name2, title)


@app.callback(
    # Output: change to graph-2
    dash.dependencies.Output('PercDon-Gndr_fr', 'figure'),
    [
        # Input: selected region from region-selection (dropdown menu)
        # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    """
        Construct or update graph according to input from 'region-selection' dropdown menu.

        :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
        :return: Plot.ly graph object, produced by don_rate_avg_don().
    """

    # Donation rate data, filtered for selected region and demographic group (education)
    # Corresponding name assigned
    dff1 = PropTotDon_2018[PropTotDon_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Genre"]
    name1 = "Pourcentage de la population"

    # Average annual donation data, filtered for selected region and demographic group (education)
    # Corresponding name assigned
    dff2 = PropTotDonAmt_2018[PropTotDonAmt_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Genre"]
    name2 = "Pourcentage de la valeur des dons"
   

    # Format title according to dropdown input
    title = '{}, {}'.format("Pourcentage de la population et de la valeur totale des dons selon le genre", region)

    # Uses external function with dataframes, names, and title set up above
    return perc_don_perc_amt(dff1, dff2, name1, name2, title)

@app.callback(
    # Output: change to graph-4
    dash.dependencies.Output('PrimCauseNumCause-Gndr_fr', 'figure'),
    [
        # Inputs: selected region from region-selection and selected demographic group from graph-4-demos (dropdown menu)
        dash.dependencies.Input('region-selection', 'value'),
    ])
def update_graph(region):
    """
        Construct or update graph according to input from 'region-selection' dropdown menu.

        :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
        :param demo: Demographic group name (str). Automatically inherited from 'graph-4-demos' dcc.Dropdown() input via dash.dependencies.Input('graph-4-demos', 'value') above.
        :return: Plot.ly graph object, produced by don_rate_avg_don().
    """

    # Average number of annual donations data, filtered for selected region and demographic group
    # Corresponding name assigned
    dff1 = AvgNumCauses_2018[AvgNumCauses_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Genre"]
    name1 = "Nombre moyen de causes"

    # Average number of causes supported data, filtered for selected region and demographic group
    # Corresponding name assigned
    dff2 = TopCauseFocus_2018[TopCauseFocus_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Genre"]
    name2 = "Concentration moyenne sur la 1ère cause"
    
    

    # Format title according to dropdown input
    title = '{}, {}'.format("Concentration sur la cause principale et nombre moyen de causes soutenues selon le genre", region)

    # Uses external function with dataframes, names, and title set up above
    return prim_cause_num_cause(dff2, dff1, name2, name1, title)

@app.callback(
    # Output: change to graph-2
    dash.dependencies.Output('PercDon-Age_fr', 'figure'),
    [
        # Input: selected region from region-selection (dropdown menu)
        # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
        dash.dependencies.Input('region-selection', 'value')
    ])

def update_graph(region):
    """
        Construct or update graph according to input from 'region-selection' dropdown menu.

        :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
        :return: Plot.ly graph object, produced by don_rate_avg_don().
    """

    # Donation rate data, filtered for selected region and demographic group (education)
    # Corresponding name assigned
    dff1 = PropTotDon_2018[PropTotDon_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Groupe d'âge"]
    name1 = "Pourcentage de la population"

    # Average annual donation data, filtered for selected region and demographic group (education)
    # Corresponding name assigned
    dff2 = PropTotDonAmt_2018[PropTotDonAmt_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Groupe d'âge"]
    name2 = "Pourcentage de la valeur des dons"
    
    

    # Format title according to dropdown input
    title = '{}, {}'.format("Pourcentage de la population et de la valeur totale des dons selon l’âge", region)

    # Uses external function with dataframes, names, and title set up above
    return perc_don_perc_amt(dff1, dff2, name1, name2, title)

@app.callback(
    # Output: change to graph-4
    dash.dependencies.Output('PrimCauseNumCause-Age_fr', 'figure'),
    [
        # Inputs: selected region from region-selection and selected demographic group from graph-4-demos (dropdown menu)
        dash.dependencies.Input('region-selection', 'value'),
    ])
def update_graph(region):
    """
        Construct or update graph according to input from 'region-selection' dropdown menu.

        :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
        :param demo: Demographic group name (str). Automatically inherited from 'graph-4-demos' dcc.Dropdown() input via dash.dependencies.Input('graph-4-demos', 'value') above.
        :return: Plot.ly graph object, produced by don_rate_avg_don().
    """

    # Average number of annual donations data, filtered for selected region and demographic group
    # Corresponding name assigned
    dff1 = AvgNumCauses_2018[AvgNumCauses_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Groupe d'âge"]
    name1 = "Nombre moyen de causes"

    # Average number of causes supported data, filtered for selected region and demographic group
    # Corresponding name assigned
    dff2 = TopCauseFocus_2018[TopCauseFocus_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Groupe d'âge"]
    name2 = "Concentration moyenne sur la 1ère cause"

   
    # Format title according to dropdown input
    title = '{}, {}'.format("Concentration sur la cause principale et nombre moyen de causes soutenues selon l’âge", region)

    # Uses external function with dataframes, names, and title set up above
    return prim_cause_num_cause(dff2, dff1, name2, name1, title)


@app.callback(
    # Output: change to graph-1
    dash.dependencies.Output('DonRateAvgDonAmt-Educ_fr', 'figure'),
    [
        # Input: selected region from region-selection (dropdown menu)
        # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    """
    Construct or update graph according to input from 'region-selection' dropdown menu.

    :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
    :return: Plot.ly graph object, produced by don_rate_avg_don().
    """
    # Donation rate data, filtered for selected region and demographic group (age group)
    # Corresponding name assigned
    dff1 = DonRates_2018[DonRates_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Éducation"]
    name1 = "Taux de donateur.trice.s"

    # Average annual donation data, filtered for selected region and demographic group (age group)
    # Corresponding name assigned
    dff2 = AvgTotDon_2018[AvgTotDon_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Éducation"]
    name2 = "Dons annuels moyens"

    # Format title according to dropdown input
    title = '{}, {}'.format("Taux de donateur.trice.s et montant moyen des dons selon l’éducation", region)

    # Uses external function with dataframes, names, and title set up above
    return don_rate_avg_don(dff1, dff2, name1, name2, title)



@app.callback(
    # Output: change to graph-2
    dash.dependencies.Output('PercDon-Educ_fr', 'figure'),
    [
        # Input: selected region from region-selection (dropdown menu)
        # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    """
        Construct or update graph according to input from 'region-selection' dropdown menu.

        :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
        :return: Plot.ly graph object, produced by don_rate_avg_don().
    """

    # Donation rate data, filtered for selected region and demographic group (education)
    # Corresponding name assigned
    dff1 = PropTotDon_2018[PropTotDon_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Éducation"]
    name1 = "Pourcentage de la population"

    # Average annual donation data, filtered for selected region and demographic group (education)
    # Corresponding name assigned
    dff2 = PropTotDonAmt_2018[PropTotDonAmt_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Éducation"]
    name2 = "Pourcentage de la valeur des dons"

    # Format title according to dropdown input
    title = '{}, {}'.format("Pourcentage de la population et de la valeur totale des dons selon l’éducation", region)

    # Uses external function with dataframes, names, and title set up above
    return perc_don_perc_amt(dff1, dff2, name1, name2, title)


@app.callback(
    # Output: change to graph-4
    dash.dependencies.Output('PrimCauseNumCause-Educ_fr', 'figure'),
    [
        # Inputs: selected region from region-selection and selected demographic group from graph-4-demos (dropdown menu)
        dash.dependencies.Input('region-selection', 'value'),
    ])
def update_graph(region):
    """
        Construct or update graph according to input from 'region-selection' dropdown menu.

        :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
        :param demo: Demographic group name (str). Automatically inherited from 'graph-4-demos' dcc.Dropdown() input via dash.dependencies.Input('graph-4-demos', 'value') above.
        :return: Plot.ly graph object, produced by don_rate_avg_don().
    """

    # Average number of annual donations data, filtered for selected region and demographic group
    # Corresponding name assigned
    AvgNumCauses_2018.Attribute = AvgNumCauses_2018.Attribute.replace("Less than High School", "Sans diplôme d'études secondaires")
    TopCauseFocus_2018.Attribute = TopCauseFocus_2018.Attribute.replace("Less than High School", "Sans diplôme d'études secondaires")
    
    dff1 = AvgNumCauses_2018[AvgNumCauses_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Éducation"]
    name1 = "Nombre moyen de causes"

    # Average number of causes supported data, filtered for selected region and demographic group
    # Corresponding name assigned
    dff2 = TopCauseFocus_2018[TopCauseFocus_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Éducation"]
    name2 = "Concentration moyenne sur la 1ère cause"
    
    

    # Format title according to dropdown input
    title = '{}, {}'.format("Concentration sur la cause principale et nombre moyen de causes soutenues selon l’éducation ", region)

    # Uses external function with dataframes, names, and title set up above
    return prim_cause_num_cause(dff2, dff1, name2, name1, title)


@app.callback(
    # Output: change to graph-1
    dash.dependencies.Output('DonRateAvgDonAmt-Inc_fr', 'figure'),
    [
        # Input: selected region from region-selection (dropdown menu)
        # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    """
    Construct or update graph according to input from 'region-selection' dropdown menu.

    :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
    :return: Plot.ly graph object, produced by don_rate_avg_don().
    """
    # Donation rate data, filtered for selected region and demographic group (age group)
    # Corresponding name assigned
    dff1 = DonRates_2018[DonRates_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Catégorie de revenu familial"]
    name1 = "Taux de donateur.trice.s"

    # Average annual donation data, filtered for selected region and demographic group (age group)
    # Corresponding name assigned
    dff2 = AvgTotDon_2018[AvgTotDon_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Catégorie de revenu familial"]
    name2 = "Dons annuels moyens"
    
  
    # Format title according to dropdown input
    title = '{}, {}'.format("Taux de donateur.trice.s et montant moyen des dons selon le revenu", region)

    # Uses external function with dataframes, names, and title set up above
    return don_rate_avg_don(dff1, dff2, name1, name2, title)


@app.callback(
    # Output: change to graph-2
    dash.dependencies.Output('PercDon-Inc_fr', 'figure'),
    [
        # Input: selected region from region-selection (dropdown menu)
        # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    """
        Construct or update graph according to input from 'region-selection' dropdown menu.

        :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
        :return: Plot.ly graph object, produced by don_rate_avg_don().
    """

    # Donation rate data, filtered for selected region and demographic group (education)
    # Corresponding name assigned
    dff1 = PropTotDon_2018[PropTotDon_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Catégorie de revenu familial"]
    name1 = "Pourcentage de la population"

    # Average annual donation data, filtered for selected region and demographic group (education)
    # Corresponding name assigned
    dff2 = PropTotDonAmt_2018[PropTotDonAmt_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Catégorie de revenu familial"]
    name2 = "Pourcentage de la valeur des dons"

    # Format title according to dropdown input
    title = '{}, {}'.format("Pourcentage de la population et de la valeur totale des dons selon le revenu", region)

    # Uses external function with dataframes, names, and title set up above
    return perc_don_perc_amt(dff1, dff2, name1, name2, title)


@app.callback(
    # Output: change to graph-4
    dash.dependencies.Output('PrimCauseNumCause-Inc_fr', 'figure'),
    [
        # Inputs: selected region from region-selection and selected demographic group from graph-4-demos (dropdown menu)
        dash.dependencies.Input('region-selection', 'value'),
    ])
def update_graph(region):
    """
        Construct or update graph according to input from 'region-selection' dropdown menu.

        :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
        :param demo: Demographic group name (str). Automatically inherited from 'graph-4-demos' dcc.Dropdown() input via dash.dependencies.Input('graph-4-demos', 'value') above.
        :return: Plot.ly graph object, produced by don_rate_avg_don().
    """

    # Average number of annual donations data, filtered for selected region and demographic group
    # Corresponding name assigned
    dff1 = AvgNumCauses_2018[AvgNumCauses_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Catégorie de revenu familial"]
    name1 = "Nombre moyen de causes"

    # Average number of causes supported data, filtered for selected region and demographic group
    # Corresponding name assigned
    dff2 = TopCauseFocus_2018[TopCauseFocus_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Catégorie de revenu familial"]
    name2 = "Concentration moyenne sur la 1ère cause"

    # Format title according to dropdown input
    title = '{}, {}'.format("Concentration sur la cause principale et nombre moyen de causes soutenues selon le revenu", region)

    # Uses external function with dataframes, names, and title set up above
    return prim_cause_num_cause(dff2, dff1, name2, name1, title)


@app.callback(
    # Output: change to graph-1
    dash.dependencies.Output('DonRateAvgDonAmt-Relig_fr', 'figure'),
    [
        # Input: selected region from region-selection (dropdown menu)
        # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    """
    Construct or update graph according to input from 'region-selection' dropdown menu.

    :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
    :return: Plot.ly graph object, produced by don_rate_avg_don().
    """
    # Donation rate data, filtered for selected region and demographic group (age group)
    # Corresponding name assigned
    dff1 = DonRates_2018[DonRates_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Fréquence de la fréquentation religieuse"]
    name1 = "Taux de donateur.trice.s"

    # Average annual donation data, filtered for selected region and demographic group (age group)
    # Corresponding name assigned
    dff2 = AvgTotDon_2018[AvgTotDon_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Fréquence de la fréquentation religieuse"]
    name2 = "Dons annuels moyens"

       # Format title according to dropdown input
    title = '{}, {}'.format("Taux de donateur.trice.s et montant moyen des dons selon la pratique religieuse", region)

    # Uses external function with dataframes, names, and title set up above
    return don_rate_avg_don(dff1, dff2, name1, name2, title)

@app.callback(
    # Output: change to graph-2
    dash.dependencies.Output('PercDon-Relig_fr', 'figure'),
    [
        # Input: selected region from region-selection (dropdown menu)
        # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    """
        Construct or update graph according to input from 'region-selection' dropdown menu.

        :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
        :return: Plot.ly graph object, produced by don_rate_avg_don().
    """

    # Donation rate data, filtered for selected region and demographic group (education)
    # Corresponding name assigned
    dff1 = PropTotDon_2018[PropTotDon_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Fréquence de la fréquentation religieuse"]
    name1 = "Pourcentage de la population"

    # Average annual donation data, filtered for selected region and demographic group (education)
    # Corresponding name assigned
    dff2 = PropTotDonAmt_2018[PropTotDonAmt_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Fréquence de la fréquentation religieuse"]
    name2 = "Pourcentage de la valeur des dons"

    # Format title according to dropdown input
    title = '{}, {}'.format("Pourcentage de la population et de la valeur totale des dons selon la pratique religieuse", region)

    # Uses external function with dataframes, names, and title set up above
    return perc_don_perc_amt(dff1, dff2, name1, name2, title)


@app.callback(
    # Output: change to graph-4
    dash.dependencies.Output('PrimCauseNumCause-Relig_fr', 'figure'),
    [
        # Inputs: selected region from region-selection and selected demographic group from graph-4-demos (dropdown menu)
        dash.dependencies.Input('region-selection', 'value'),
    ])
def update_graph(region):
    """
        Construct or update graph according to input from 'region-selection' dropdown menu.

        :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
        :param demo: Demographic group name (str). Automatically inherited from 'graph-4-demos' dcc.Dropdown() input via dash.dependencies.Input('graph-4-demos', 'value') above.
        :return: Plot.ly graph object, produced by don_rate_avg_don().
    """

    # Average number of annual donations data, filtered for selected region and demographic group
    # Corresponding name assigned
    dff1 = AvgNumCauses_2018[AvgNumCauses_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Fréquence de la fréquentation religieuse"]
    name1 = "Nombre moyen de causes"

    # Average number of causes supported data, filtered for selected region and demographic group
    # Corresponding name assigned
    dff2 = TopCauseFocus_2018[TopCauseFocus_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Fréquence de la fréquentation religieuse"]
    name2 = "Concentration moyenne sur la 1ère cause"

    # Format title according to dropdown input
    title = '{}, {}'.format("Concentration sur la cause principale et nombre moyen de causes soutenues selon la pratique religieuse ", region)

    # Uses external function with dataframes, names, and title set up above
    return prim_cause_num_cause(dff2, dff1, name2, name1, title)


# @app.callback(
#     # Output: change to graph-1
#     dash.dependencies.Output('DonRateAvgDonAmt-MarStat', 'figure'),
#     [
#         # Input: selected region from region-selection (dropdown menu)
#         # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     """
#     Construct or update graph according to input from 'region-selection' dropdown menu.

#     :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
#     :return: Plot.ly graph object, produced by don_rate_avg_don().
#     """
#     # Donation rate data, filtered for selected region and demographic group (age group)
#     # Corresponding name assigned
#     dff1 = DonRates_2018[DonRates_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == "Marital status"]
#     name1 = "Donation rate"

#     # Average annual donation data, filtered for selected region and demographic group (age group)
#     # Corresponding name assigned
#     dff2 = AvgTotDon_2018[AvgTotDon_2018['Region'] == region]
#     dff2 = dff2[dff2['Group'] == "Marital status"]
#     name2 = "Average annual donations"

#     # Format title according to dropdown input
#     title = '{}, {}'.format("Donation rate and average annual donation by marital status", region)

#     # Uses external function with dataframes, names, and title set up above
#     return don_rate_avg_don(dff1, dff2, name1, name2, title)

# @app.callback(
#     # Output: change to graph-1
#     dash.dependencies.Output('DonRateAvgDonAmt-Labour', 'figure'),
#     [
#         # Input: selected region from region-selection (dropdown menu)
#         # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     """
#     Construct or update graph according to input from 'region-selection' dropdown menu.

#     :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
#     :return: Plot.ly graph object, produced by don_rate_avg_don().
#     """
#     # Donation rate data, filtered for selected region and demographic group (age group)
#     # Corresponding name assigned
#     dff1 = DonRates_2018[DonRates_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == "Labour force status"]
#     name1 = "Donation rate"

#     # Average annual donation data, filtered for selected region and demographic group (age group)
#     # Corresponding name assigned
#     dff2 = AvgTotDon_2018[AvgTotDon_2018['Region'] == region]
#     dff2 = dff2[dff2['Group'] == "Labour force status"]
#     name2 = "Average annual donations"

#     # Format title according to dropdown input
#     title = '{}, {}'.format("Donation rate and average annual donation by employment status", region)

#     # Uses external function with dataframes, names, and title set up above
#     return don_rate_avg_don(dff1, dff2, name1, name2, title)

# @app.callback(
#     # Output: change to graph-1
#     dash.dependencies.Output('DonRateAvgDonAmt-ImmStat', 'figure'),
#     [
#         # Input: selected region from region-selection (dropdown menu)
#         # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     """
#     Construct or update graph according to input from 'region-selection' dropdown menu.

#     :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
#     :return: Plot.ly graph object, produced by don_rate_avg_don().
#     """
#     # Donation rate data, filtered for selected region and demographic group (age group)
#     # Corresponding name assigned
#     dff1 = DonRates_2018[DonRates_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == "Immigration status"]
#     name1 = "Donation rate"

#     # Average annual donation data, filtered for selected region and demographic group (age group)
#     # Corresponding name assigned
#     dff2 = AvgTotDon_2018[AvgTotDon_2018['Region'] == region]
#     dff2 = dff2[dff2['Group'] == "Immigration status"]
#     name2 = "Average annual donations"

#     # Format title according to dropdown input
#     title = '{}, {}'.format("Donation rate and average annual donation by immigration status", region)

#     # Uses external function with dataframes, names, and title set up above
#     return don_rate_avg_don(dff1, dff2, name1, name2, title)

@app.callback(
    # Output: change to graph-1
    dash.dependencies.Output('DonRateAvgDonAmt-other_fr', 'figure'),
    [
        # Input: selected region from region-selection (dropdown menu)
        # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('status-selection1', 'value')
    ])
def update_graph(region, status):
    """
    Construct or update graph according to input from 'region-selection' dropdown menu.

    :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
    :return: Plot.ly graph object, produced by don_rate_avg_don().
    """
    # Donation rate data, filtered for selected region and demographic group (age group)
    # Corresponding name assigned
    dff1 = DonRates_2018[DonRates_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == status]
    name1 = "Taux de donateur.trice.s"

    # Average annual donation data, filtered for selected region and demographic group (age group)
    # Corresponding name assigned
    dff2 = AvgTotDon_2018[AvgTotDon_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == status]
    name2 = "Dons annuels moyens"

    # Format title according to dropdown input
    title = '{}, {}'.format("Taux de donateur.trice.s et montant moyen des dons selon " + str(status).lower(), region)

    # Uses external function with dataframes, names, and title set up above
    return don_rate_avg_don(dff1, dff2, name1, name2, title)


# @app.callback(
#     # Output: change to graph-2
#     dash.dependencies.Output('PercDon-MarStat', 'figure'),
#     [
#         # Input: selected region from region-selection (dropdown menu)
#         # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     """
#         Construct or update graph according to input from 'region-selection' dropdown menu.

#         :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
#         :return: Plot.ly graph object, produced by don_rate_avg_don().
#     """

#     # Donation rate data, filtered for selected region and demographic group (education)
#     # Corresponding name assigned
#     dff1 = PropTotDon_2018[PropTotDon_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == "Marital status (original)"]
#     name1 = "Proportion of donors"

#     # Average annual donation data, filtered for selected region and demographic group (education)
#     # Corresponding name assigned
#     dff2 = PropTotDonAmt_2018[PropTotDonAmt_2018['Region'] == region]
#     dff2 = dff2[dff2['Group'] == "Marital status"]
#     name2 = "Percentage of donation value"

#     # Format title according to dropdown input
#     title = '{}, {}'.format("Percentage of Canadians & total donation value by marital status", region)

#     # Uses external function with dataframes, names, and title set up above
#     return perc_don_perc_amt(dff1, dff2, name1, name2, title)


# @app.callback(
#     # Output: change to graph-2
#     dash.dependencies.Output('PercDon-Labour', 'figure'),
#     [
#         # Input: selected region from region-selection (dropdown menu)
#         # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     """
#         Construct or update graph according to input from 'region-selection' dropdown menu.

#         :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
#         :return: Plot.ly graph object, produced by don_rate_avg_don().
#     """

#     # Donation rate data, filtered for selected region and demographic group (education)
#     # Corresponding name assigned
#     dff1 = PropTotDon_2018[PropTotDon_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == "Labour force status"]
#     name1 = "Proportion of donors"

#     # Average annual donation data, filtered for selected region and demographic group (education)
#     # Corresponding name assigned
#     dff2 = PropTotDonAmt_2018[PropTotDonAmt_2018['Region'] == region]
#     dff2 = dff2[dff2['Group'] == "Labour force status"]
#     name2 = "Percentage of donation value"

#     # Format title according to dropdown input
#     title = '{}, {}'.format("Percentage of Canadians & total donation value by employment", region)

#     # Uses external function with dataframes, names, and title set up above
#     return perc_don_perc_amt(dff1, dff2, name1, name2, title)

# @app.callback(
#     # Output: change to graph-2
#     dash.dependencies.Output('PercDon-ImmStat', 'figure'),
#     [
#         # Input: selected region from region-selection (dropdown menu)
#         # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     """
#         Construct or update graph according to input from 'region-selection' dropdown menu.

#         :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
#         :return: Plot.ly graph object, produced by don_rate_avg_don().
#     """

#     # Donation rate data, filtered for selected region and demographic group (education)
#     # Corresponding name assigned
#     dff1 = PropTotDon_2018[PropTotDon_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == "Immigration status"]
#     name1 = "Proportion of donors"

#     # Average annual donation data, filtered for selected region and demographic group (education)
#     # Corresponding name assigned
#     dff2 = PropTotDonAmt_2018[PropTotDonAmt_2018['Region'] == region]
#     dff2 = dff2[dff2['Group'] == "Immigration status"]
#     name2 = "Percentage of donation value"

#     # Format title according to dropdown input
#     title = '{}, {}'.format("Percentage of Canadians & total donation value by immigration status", region)

#     # Uses external function with dataframes, names, and title set up above
#     return perc_don_perc_amt(dff1, dff2, name1, name2, title)

@app.callback(
    # Output: change to graph-2
    dash.dependencies.Output('PercDon-other_fr', 'figure'),
    [
        # Input: selected region from region-selection (dropdown menu)
        # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('status-selection2', 'value')
    ])
def update_graph(region, status):
    """
        Construct or update graph according to input from 'region-selection' dropdown menu.

        :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
        :return: Plot.ly graph object, produced by don_rate_avg_don().
    """

    # Donation rate data, filtered for selected region and demographic group (education)
    # Corresponding name assigned
    dff1 = PropTotDon_2018[PropTotDon_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == status]
    name1 = "Pourcentage de la population"

    # Average annual donation data, filtered for selected region and demographic group (education)
    # Corresponding name assigned
    dff2 = PropTotDonAmt_2018[PropTotDonAmt_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == status]
    name2 = "Pourcentage de la valeur des dons"

    # Format title according to dropdown input
    title = '{}, {}'.format("Pourcentage de la population et de la valeur totale des dons selon "  + str(status).lower(), region)

    # Uses external function with dataframes, names, and title set up above
    return perc_don_perc_amt(dff1, dff2, name1, name2, title)

# @app.callback(
#     # Output: change to graph-4
#     dash.dependencies.Output('PrimCauseNumCause-MarStat', 'figure'),
#     [
#         # Inputs: selected region from region-selection and selected demographic group from graph-4-demos (dropdown menu)
#         dash.dependencies.Input('region-selection', 'value'),
#     ])
# def update_graph(region):
#     """
#         Construct or update graph according to input from 'region-selection' dropdown menu.

#         :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
#         :param demo: Demographic group name (str). Automatically inherited from 'graph-4-demos' dcc.Dropdown() input via dash.dependencies.Input('graph-4-demos', 'value') above.
#         :return: Plot.ly graph object, produced by don_rate_avg_don().
#     """

#     # Average number of annual donations data, filtered for selected region and demographic group
#     # Corresponding name assigned
#     dff1 = AvgNumCauses_2018[AvgNumCauses_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == "Marital status"]
#     name1 = "Average number of causes"

#     # Average number of causes supported data, filtered for selected region and demographic group
#     # Corresponding name assigned
#     dff2 = TopCauseFocus_2018[TopCauseFocus_2018['Region'] == region]
#     dff2 = dff2[dff2['Group'] == "Marital status"]
#     name2 = "Average concentration on first cause"

#     # Format title according to dropdown input
#     title = '{}, {}'.format("Focus on primary cause & average number of causes supported by marital status", region)

#     # Uses external function with dataframes, names, and title set up above
#     return prim_cause_num_cause(dff2, dff1, name2, name1, title)


# @app.callback(
#     # Output: change to graph-4
#     dash.dependencies.Output('PrimCauseNumCause-Labour', 'figure'),
#     [
#         # Inputs: selected region from region-selection and selected demographic group from graph-4-demos (dropdown menu)
#         dash.dependencies.Input('region-selection', 'value'),
#     ])
# def update_graph(region):
#     """
#         Construct or update graph according to input from 'region-selection' dropdown menu.

#         :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
#         :param demo: Demographic group name (str). Automatically inherited from 'graph-4-demos' dcc.Dropdown() input via dash.dependencies.Input('graph-4-demos', 'value') above.
#         :return: Plot.ly graph object, produced by don_rate_avg_don().
#     """

#     # Average number of annual donations data, filtered for selected region and demographic group
#     # Corresponding name assigned
#     dff1 = AvgNumCauses_2018[AvgNumCauses_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == "Labour force status"]
#     name1 = "Average number of causes"

#     # Average number of causes supported data, filtered for selected region and demographic group
#     # Corresponding name assigned
#     dff2 = TopCauseFocus_2018[TopCauseFocus_2018['Region'] == region]
#     dff2 = dff2[dff2['Group'] == "Labour force status"]
#     name2 = "Average concentration on first cause"

#     # Format title according to dropdown input
#     title = '{}, {}'.format("Focus on primary cause & average number of causes supported by employment status", region)

#     # Uses external function with dataframes, names, and title set up above
#     return prim_cause_num_cause(dff2, dff1, name2, name1, title)


# @app.callback(
#     # Output: change to graph-4
#     dash.dependencies.Output('PrimCauseNumCause-ImmStat', 'figure'),
#     [
#         # Inputs: selected region from region-selection and selected demographic group from graph-4-demos (dropdown menu)
#         dash.dependencies.Input('region-selection', 'value'),
#     ])
# def update_graph(region):
#     """
#         Construct or update graph according to input from 'region-selection' dropdown menu.

#         :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
#         :param demo: Demographic group name (str). Automatically inherited from 'graph-4-demos' dcc.Dropdown() input via dash.dependencies.Input('graph-4-demos', 'value') above.
#         :return: Plot.ly graph object, produced by don_rate_avg_don().
#     """

#     # Average number of annual donations data, filtered for selected region and demographic group
#     # Corresponding name assigned
#     dff1 = AvgNumCauses_2018[AvgNumCauses_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == "Immigration status"]
#     name1 = "Average number of causes"

#     # Average number of causes supported data, filtered for selected region and demographic group
#     # Corresponding name assigned
#     dff2 = TopCauseFocus_2018[TopCauseFocus_2018['Region'] == region]
#     dff2 = dff2[dff2['Group'] == "Immigration status"]
#     name2 = "Average concentration on first cause"

#     # Format title according to dropdown input
#     title = '{}, {}'.format("Focus on primary cause & average number of causes supported by immigration status", region)

#     # Uses external function with dataframes, names, and title set up above
#     return prim_cause_num_cause(dff2, dff1, name2, name1, title)


@app.callback(
    # Output: change to graph-4
    dash.dependencies.Output('PrimCauseNumCause-other3_fr', 'figure'),
    [
        # Inputs: selected region from region-selection and selected demographic group from graph-4-demos (dropdown menu)
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('status-selection3', 'value')
    ])
def update_graph(region, status):
    """
        Construct or update graph according to input from 'region-selection' dropdown menu.

        :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
        :param demo: Demographic group name (str). Automatically inherited from 'graph-4-demos' dcc.Dropdown() input via dash.dependencies.Input('graph-4-demos', 'value') above.
        :return: Plot.ly graph object, produced by don_rate_avg_don().
    """

    # Average number of annual donations data, filtered for selected region and demographic group
    # Corresponding name assigned
    dff1 = AvgNumCauses_2018[AvgNumCauses_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == status]
    name1 = "Nombre moyen de causes"

    # Average number of causes supported data, filtered for selected region and demographic group
    # Corresponding name assigned
    dff2 = TopCauseFocus_2018[TopCauseFocus_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == status]
    name2 = "Concentration moyenne sur la 1ère cause"

    # Format title according to dropdown input
    title = '{}, {}'.format("Concentration sur la cause principale et nombre <br> moyen de causes soutenues selon " + str(status).lower(), region)

    # Uses external function with dataframes, names, and title set up above
    return prim_cause_num_cause(dff2, dff1, name2, name1, title)






# if __name__ == "__main__":
#     app.run_server(debug=True)

