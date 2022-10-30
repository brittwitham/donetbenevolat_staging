import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc
import os
import os.path as op
import re

from utils.graphs.WVA0201_graph_utils import static_graph, forms_of_giving, don_rate_avg_don, perc_don_perc_amt
from utils.data.WVA0201_data_utils_13 import get_data, process_data, get_region_values, get_region_names, translate

from app import app
from homepage import footer #navbar, footer

####################### Data processing ######################
VolRate_2018, AvgTotHours_2018, FormsVolunteering_2018, PercTotVols_2018, PercTotHours_2018 = get_data()

data = [VolRate_2018, AvgTotHours_2018, PercTotVols_2018, PercTotHours_2018, FormsVolunteering_2018]

process_data(data)

PercTotVols_2018 = translate(PercTotVols_2018)
PercTotHours_2018 = translate(PercTotHours_2018)

region_values = get_region_values()
region_names = get_region_names()

status_names = ["Situation d'activité", "Statut d'immigration"]

###################### App layout ######################
navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                # dcc.Link("Home", href="/")
                dbc.NavLink("À propos", href="https://www.donetbenevolat.ca/",external_link=True)
            ),
            dbc.NavItem(
                dbc.NavLink("EN", href="http://app.givingandvolunteering.ca/who_volunteers_and_how_much_time_do_they_contribute_2013",external_link=True)
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
                        html.H1("Qui sont les bénévoles et combien d'heures donnent-ils? (2013)"),
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
                       options=[{'label': region_values[i], 'value': region_values[i]} for i in range(len(region_values))],
                       value='CA',
                       ),
                    html.Br(),
                ],className="m-2 p-2"),
            ), id='sticky-dropdown'),
    ], className='sticky-top bg-light mb-2', fluid=True),
   dbc.Container(
       dbc.Row([
            html.Div(
                [
                    dcc.Markdown("""
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2013, près de neuf personnes sur dix (85 %) au Canada ont fait don de leur temps pour une forme ou une autre d’activité prosociale pendant la période d’un an qui l’a précédée. Plus de deux cinquièmes des personnes au Canada (44 %) étaient des bénévoles encadrés, qui faisaient don de leur temps à des organismes de bienfaisance ou à but non lucratif, et environ quatre cinquièmes des personnes (82 %) étaient des bénévoles non encadrés, qui faisaient directement don de leur temps à des personnes dans le besoin non membre de leur ménage, et ce, en dehors d’un organisme. À l’échelle nationale, les bénévoles encadrés ont fait chacun don de 154 heures en moyenne, soit, au total, 2,0 milliards d’heures de bénévolat au bénéfice des organismes de bienfaisance et sans but lucratif équivalant à environ 1,0 million d’emplois à temps plein.
                    """),
                    # Forms of volunteering
                    dcc.Graph(id='FormsVolunteering_13', style={'marginTop': marginTop}),
                    dcc.Markdown("""
                    La probabilité de faire du bénévolat pour un organisme de bienfaisance ou à but non lucratif variait selon le lieu de résidence des bénévoles. Pour la majorité des provinces, la proportion de bénévoles se situait à la norme nationale ou légèrement au-dessus de celle-ci. Elle était nettement supérieure à la norme dans la Saskatchewan et au Manitoba et nettement inférieure à la norme au Québec. Pour la majorité des provinces, le nombre moyen d’heures de bénévolat ne s’écartait pas de manière significative de la norme nationale, à l’exception notable du Québec.
                    """),
                    # Volunteer rate & average hours volunteered by province
                    dcc.Graph(id='VolRateAvgHours-prv',figure=static_graph(VolRate_2018, AvgTotHours_2018), style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Personal & economic characteristics
            html.Div(
                [
                    html.H3('Caractéristiques personnelles et économiques'),
                    html.P("""
                        En plus des variations selon le lieu de résidence, le bénévolat encadré avait également tendance à varier selon les caractéristiques personnelles et économiques des bénévoles. Nous examinons ci-dessous l’association entre certaines de ces caractéristiques et les mesures clés du bénévolat:
                    """),
                    html.Ul([
                        html.Li('la probabilité de faire du bénévolat et le nombre moyen d’heures de bénévolat par personne; '),
                        html.Li('les pourcentages de la population canadienne et le nombre total d’heures de bénévolat pour chaque sous-groupe. '),
                    ]),
                    
                    html.P("""
                        À elles toutes, ces mesures brossent un tableau détaillé du bassin de bénévoles et fournissent un aperçu de la concentration générale du soutien bénévole des organismes de bienfaisance et à but non lucratif. Dans le texte, nous décrivons les résultats au niveau national et, pour obtenir des précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer des résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.
                    """),
                    html.Div([
                        html.H4("Genre"),
                        html.P("""
                        Au niveau national, les femmes étaient légèrement plus enclines à faire du bénévolat que les hommes (respectivement 45 % et 42 %), bien que les hommes aient légèrement plus tendance à faire don de plus d’heures quand ils faisaient du bénévolat.
                        """),
                        # Barriers to giving more by gender
                        html.Div([
                            dcc.Graph(id='VolRateAvgHours-Gndr_13', style={'marginTop': marginTop}),
                        ]),
                        dcc.Markdown("""
                    Dans l’ensemble, les pourcentages du nombre total d’heures de bénévolat des hommes et des femmes étaient très comparables à leur représentation au sein de la population (c.-à-d. que le nombre d’heures de bénévolat de l’un ou l’autre genre n’était pas nettement plus ou moins élevé par rapport à son nombre).
                    """),
                        # Percentage of Canadians & total hours volunteered by gender
                        html.Div([
                            dcc.Graph(id='PercVolHours-Gndr_13', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("""
                        Les personnes plus jeunes et d’âge moyen étaient les plus susceptibles de faire du bénévolat, surtout celles âgées de 15 à 24 ans. Après l’âge de 65 ans, la probabilité de faire du bénévolat chutait fortement. Quant aux heures de bénévolat caractéristiques, les personnes de moins de 55 ans avaient tendance à faire don de moins d’heures.
                        """),
                        # Volunteer rate & average hours volunteered by age
                        html.Div([
                            dcc.Graph(id='VolRateAvgHours-Age_13', style={'marginTop': marginTop}),
                        ]),
                        dcc.Markdown("""
                    Étant donné leur tendance à faire don de moins d’heures, les bénévoles âgés de 24 à 44 ans représentaient moins d’heures que leur représentation au sein de la population ne le donnait à penser. En revanche, les bénévoles âgés de 55 à 74 ans représentaient des pourcentages du nombre total d’heures excessivement élevés compte tenu de leur nombre..
                    """),
                        # Percentage of Canadians & total hours volunteered by age
                        html.Div([
                            dcc.Graph(id='PercVolHours-Age_13', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Formal Education
                    html.Div([
                         html.H5("Éducation formelle"),
                        html.P("""
                        La probabilité de faire du bénévolat avait tendance à augmenter en allant de pair avec les niveaux d’études supérieurs au diplôme d’études secondaires, les titulaires d’un diplôme universitaire étant enclins à faire don d’un nombre d’heures relativement plus élevé que les autres.
                        """),
                        # Volunteer rate & average hours volunteered by formal education
                        html.Div([
                            dcc.Graph(id='VolRateAvgHours-Educ_13', style={'marginTop': marginTop}),
                        ]),
                        dcc.Markdown("""
                    À l’échelle nationale, les bénévoles titulaires d’un diplôme d’études secondaires faisaient don d’un nombre d’heures légèrement inférieur à leur représentation au sein de la population, tandis que les bénévoles titulaires d’un diplôme universitaire faisaient don d’un nombre d’heures relativement supérieur à celui auquel on pourrait s’attendre.
                    """),
                        # Percentage of Canadians & total hours volunteered by formal education
                        html.Div([
                            dcc.Graph(id='PercVolHours-Educ_13', style={'marginTop': marginTop}),
                        ]),             
                    ]),
                    # Marital status
                    html.Div([
                        html.H5("Situation matrimoniale"),
                        html.P("""
                        Les personnes célibataires et mariées étaient les plus enclines à faire du bénévolat, contrairement aux personnes veuves. Ces dernières avaient tendance à faire don d’un plus grand nombre d’heures quand elles faisaient du bénévolat, tandis que les célibataires en faisaient souvent relativement moins.
                        """),
                        # Volunteer rate & average hours volunteered by marital status
                        html.Div([
                            dcc.Graph(id='VolRateAvgHours-MarStat_13', style={'marginTop': marginTop}),
                        ]),
                        dcc.Markdown("""
                    Les variations de la probabilité de faire du bénévolat et des heures de bénévolat caractéristiques se compensaient presque totalement, ce qui veut dire que chaque groupe représentait presque exactement la proportion des heures de bénévolat à laquelle on pourrait s’attendre, étant donné leur nombre respectif au sein de la population canadienne.
                    """),
                        # Percentage of  Canadians & total hours volunteered by marital status
                        html.Div([
                            dcc.Graph(id='PercVolHours-MarStat_13', style={'marginTop': marginTop}),
                        ]),             
                    ]),
                    # household income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("""
                        D’une façon très générale, la probabilité de faire du bénévolat avait tendance à augmenter avec le revenu du ménage, tandis que le nombre d’heures de bénévolat des ménages au revenu égal ou supérieur à 120 000 $ avait tendance à être inférieur.
                        """),
                        # Volunteer rate & average hours volunteered by household income
                        html.Div([
                            dcc.Graph(id='VolRateAvgHours-Inc_13', style={'marginTop': marginTop}),
                        ]),
                        dcc.Markdown("""
                    Dans l’ensemble, chaque groupe de revenu représentait à peu près la même proportion du nombre total d’heures de bénévolat que sa proportion au sein de la population canadienne (c.-à-d. aucun groupe ne se distingue en faisant don de nettement plus ou moins d’heures par rapport à son nombre).
                    """),
                        # Percentage of Canadians & total hours volunteered by household income
                        html.Div([
                            dcc.Graph(id='PercVolHours-Inc_fr', style={'marginTop': marginTop}),
                        ]),       
                    ]),
                    # Religious attendance
                    html.Div([
                        html.H5("Pratique religieuse"),
                        html.P("""
                        La probabilité de faire du bénévolat avait tendance à augmenter avec l’assiduité aux offices religieux. À l’exception des personnes qui assistaient aux services une fois par semaine (enclines à faire don de beaucoup plus de temps), les bénévoles avaient tendance à faire don d’un nombre d’heures relativement uniforme.
                        """),
                        # Volunteer rate & average hours volunteered by religious attendance
                        html.Div([
                           dcc.Graph(id='VolRateAvgHours-Relig_13', style={'marginTop': marginTop}),
                        ]),
                        dcc.Markdown("""
                    Étant donné leur taux de bénévolat supérieur et le nombre d’heures de bénévolat significativement plus important dont elles avaient tendance à faire don, les personnes présentes chaque semaine aux offices religieux représentaient une proportion des heures de bénévolat très supérieure à leur représentation au sein de la population. Les personnes qui n’assistaient pas aux services religieux représentaient une proportion des heures de bénévolat significativement inférieure à celle que leur nombre permettait de présager.
                    """),
                        # Percentage of Canadians & total hours volunteered by religious attendance
                        html.Div([
                            dcc.Graph(id='PercVolHours-Relig_13', style={'marginTop': marginTop}),
                        ]),       
                    ]),
                    # Other personal & economic characteristics
                    html.Div([
                        html.H5("Autres facteurs"),
                        dcc.Markdown("""
                    Étant donné leur taux de bénévolat supérieur et le nombre d’heures de bénévolat significativement plus important dont elles avaient tendance à faire don, les personnes présentes chaque semaine aux offices religieux représentaient une proportion des heures de bénévolat très supérieure à leur représentation au sein de la population. Les personnes qui n’assistaient pas aux services religieux représentaient une proportion des heures de bénévolat significativement inférieure à celle que leur nombre permettait de présager.
                    """),
                        # Volunteer rate & average hours volunteered by employment status
                        
                        html.Div([
                            html.Div(['Select status:',
                                      dcc.Dropdown(
                                          id='status-selection2',
                                          options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                                          value="Situation d'activité",
                                          style={'verticalAlign': 'middle'}
                                      ),],
                                     style={'width': '33%', 'display': 'inline-block'})
                        ]),
                        dcc.Graph(id='status-hours_13', style={'marginTop': marginTop}),
                        
                        # html.Div([
                        #     dcc.Graph(id='VolRateAvgHours-Labour', style={'marginTop': marginTop}),
                        # ]),
                        # # Volunteer rate & average hours volunteered by immigration status
                        # html.Div([
                        #     dcc.Graph(id='VolRateAvgHours-ImmStat', style={'marginTop': marginTop}),
                        # ]),
                        # html.P("Dans l’ensemble, les personnes qui ne font pas partie de la population active et les personnes nées au Canada ont tendance à représenter un nombre d’heures proportionnellement supérieur, tandis que les personnes naturalisées et employées ont tendance à représenter un nombre d’heures proportionnellement inférieur."),
                        # Percentage of Canadians & total hours volunteered by employment status
                        # html.Div([
                        #     dcc.Graph(id='PercVolHours-Labour', style={'marginTop': marginTop})
                        # ]),
                        # # Percentage of Canadians & total hours volunteered by immigration status
                        # html.Div([
                        #     dcc.Graph(id='PercVolHours-ImmStat', style={'marginTop': marginTop})
                        # ]),
                        html.Div([
                            html.Div(['Sélectionner le statut:',
                                      dcc.Dropdown(
                                          id='status-selection',
                                          options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                                          value="Situation d'activité",
                                          style={'verticalAlign': 'middle'}
                                      ),],
                                     style={'width': '33%', 'display': 'inline-block'})
                        ]),
                        dcc.Graph(id='status-perc_13', style={'marginTop': marginTop})
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
   ),
   footer
])


################## Callbacks #################
@app.callback(
    dash.dependencies.Output('FormsVolunteering_13', 'figure'),
    [

        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):

    dff1 = FormsVolunteering_2018[FormsVolunteering_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "All"]
    dff1 = dff1.replace("Formal volunteer", "Bénévolat <br> encadré")
    dff1 = dff1.replace("Informal volunteer", "Bénévolat <br> non encadré")
    dff1 = dff1.replace("Help people directly", "Aider les gens <br> directement")
    dff1 = dff1.replace("Improve community", "Améliorer <br> la communauté")

    title = '{}, {}'.format("Formes de bénévolat", region)

    return forms_of_giving(dff1, title)

@app.callback(
    dash.dependencies.Output('VolRateAvgHours-Gndr_13', 'figure'),
    [

        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):

    dff1 = VolRate_2018[VolRate_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Genre"]
    dff1 = dff1.replace("Male", "Hommes")
    dff1 = dff1.replace("Female", "Femmes")
    dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")

    # name1 = "Volunteer rate"
    name1 = 'Taux de bénévolat'


    dff2 = AvgTotHours_2018[AvgTotHours_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Genre"]
    dff2 = dff2.replace("Male", "Hommes")
    dff2 = dff2.replace("Female", "Femmes")
    dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
    
    # name2 = "Average hours"
    name2 = "Nombre d'heures moyen"

    title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures de bénévolat selon le genre", region)

    return don_rate_avg_don(dff1, dff2, name1, name2, title)

@app.callback(
    dash.dependencies.Output('PercVolHours-Gndr_13', 'figure'),
    [

        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = PercTotVols_2018[PercTotVols_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Genre"]
    # dff1 = dff1[dff1['Group'] == "Gender"]
    # dff1 = dff1.replace("Male gender", "Hommes")
    # dff1 = dff1.replace("Female gender", "Femmes")
    dff1 = dff1.replace("% volunteers", "% population")
    # name1 = "% volunteers"
    name1 = "% population"


    dff2 = PercTotHours_2018[PercTotHours_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Genre"]
    # dff2 = dff2.replace("Male gender", "Hommes")
    # dff2 = dff2.replace("Female gender", "Femmes")
    dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
    name2 = "% heures de bénévolat"

    title = '{}, {}'.format("Pourcentage de la population et nombre total d’heures de bénévolat selon le genre", region)

    return perc_don_perc_amt(dff1, dff2, name1, name2, title)

@app.callback(
    dash.dependencies.Output('PercVolHours-Age_13', 'figure'),
    [

        dash.dependencies.Input('region-selection', 'value')
    ])

def update_graph(region):
    dff1 = PercTotVols_2018[PercTotVols_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Groupe d'âge"]
    # dff1 = dff1.replace('15 to 24 years', '15 à 24 ans')
    # dff1 = dff1.replace('25 to 34 years', '25 à 34 ans')
    # dff1 = dff1.replace('35 to 44 years', '35 à 44 ans')
    # dff1 = dff1.replace('45 to 54 years', '45 à 54 ans')
    # dff1 = dff1.replace('55 to 64 years', '55 à 64 ans')
    # dff1 = dff1.replace('65 to 74 years', '65 à 74 ans')
    # dff1 = dff1.replace('75 years and over', '75 ans et plus')
    dff1 = dff1.replace("% volunteers", "% population")
    # name1 = "% volunteers"
    name1 = "% population"


    dff2 = PercTotHours_2018[PercTotHours_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Groupe d'âge"]
    # dff2 = dff2.replace('15 to 24 years', '15 à 24 ans')
    # dff2 = dff2.replace('25 to 34 years', '25 à 34 ans')
    # dff2 = dff2.replace('35 to 44 years', '35 à 44 ans')
    # dff2 = dff2.replace('45 to 54 years', '45 à 54 ans')
    # dff2 = dff2.replace('55 to 64 years', '55 à 64 ans')
    # dff2 = dff2.replace('65 to 74 years', '65 à 74 ans')
    # dff2 = dff2.replace('75 years and over', '75 ans et plus')
    dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
    name2 = "% heures de bénévolat"
    # name2 = "% volunteer hours"

    title = '{}, {}'.format("Pourcentage de la population et du <br> nombre total d’heures de bénévolat selon l’âge", region)

    return perc_don_perc_amt(dff1, dff2, name1, name2, title)

@app.callback(
    dash.dependencies.Output('VolRateAvgHours-Age_13', 'figure'),
    [

        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):

    dff1 = VolRate_2018[VolRate_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Groupe d'âge"]
    # dff1 = dff1.replace('15 to 24 years', '15 à 24 ans')
    # dff1 = dff1.replace('25 to 34 years', '25 à 34 ans')
    # dff1 = dff1.replace('35 to 44 years', '35 à 44 ans')
    # dff1 = dff1.replace('45 to 54 years', '45 à 54 ans')
    # dff1 = dff1.replace('55 to 64 years', '55 à 64 ans')
    # dff1 = dff1.replace('65 to 74 years', '65 à 74 ans')
    # dff1 = dff1.replace('75 years and over', '75 ans et plus')
    dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")

    # name1 = "Volunteer rate"
    name1 = 'Taux de bénévolat'

    dff2 = AvgTotHours_2018[AvgTotHours_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Groupe d'âge"]
    # dff2 = dff2.replace('15 to 24 years', '15 à 24 ans')
    # dff2 = dff2.replace('25 to 34 years', '25 à 34 ans')
    # dff2 = dff2.replace('35 to 44 years', '35 à 44 ans')
    # dff2 = dff2.replace('45 to 54 years', '45 à 54 ans')
    # dff2 = dff2.replace('55 to 64 years', '55 à 64 ans')
    # dff2 = dff2.replace('65 to 74 years', '65 à 74 ans')
    # dff2 = dff2.replace('75 years and over', '75 ans et plus')
    # dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
    dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
    
    # name2 = "Average hours"
    name2 = "Nombre d'heures moyen"

    title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures <br> de bénévolat selon le groupe d'âge", region)

    return don_rate_avg_don(dff1, dff2, name1, name2, title)


@app.callback(
    dash.dependencies.Output('VolRateAvgHours-Educ_13', 'figure'),
    [

        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):

    dff1 = VolRate_2018[VolRate_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Éducation"]
    # dff1 = dff1.replace('Less than High School', "Sans diplôme d'études secondaires")
    # dff1 = dff1.replace('Graduated from High school', "Diplôme d'études secondaires")
    # dff1 = dff1.replace('Post-secondary diploma', 'Diplôme post-secondaire')
    # dff1 = dff1.replace('University Diploma', "Diplôme universtaire")
    dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")

    # name1 = "Volunteer rate"
    name1 = 'Taux de bénévolat'


    dff2 = AvgTotHours_2018[AvgTotHours_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Éducation"]
    # dff2 = dff2.replace('Less than High School', "Sans diplôme d'études secondaires")
    # dff2 = dff2.replace('Graduated from High school', "Diplôme d'études secondaires")
    # dff2 = dff2.replace('Post-secondary diploma', 'Diplôme post-secondaire')
    # dff2 = dff2.replace('University Diploma', "Diplôme universtaire")
    # dff2 = dff2.replace("Volunteer rate", "Taux de bénévolat")
    dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
    
    # name2 = "Average hours"
    name2 = "Nombre d'heures moyen"

    title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures <br> de bénévolat selon l’éducation ", region)

    return don_rate_avg_don(dff1, dff2, name1, name2, title)


@app.callback(
    dash.dependencies.Output('PercVolHours-Educ_13', 'figure'),
    [

        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):



    dff1 = PercTotVols_2018[PercTotVols_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Éducation"]
    # dff1 = dff1.replace('Less than High School', "Sans diplôme d'études secondaires")
    # dff1 = dff1.replace('Graduated from High school', "Diplôme d'études secondaires")
    # dff1 = dff1.replace('Post-secondary diploma', 'Diplôme post-secondaire')
    # dff1 = dff1.replace('University Diploma', "Diplôme universtaire")
    # dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")
    dff1 = dff1.replace("% volunteers", "% population")
    # name1 = "% volunteers"
    name1 = "% population"


    dff2 = PercTotHours_2018[PercTotHours_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Éducation"]
    # dff2 = dff2.replace('Less than High School', "Sans diplôme d'études secondaires")
    # dff2 = dff2.replace('Graduated from High school', "Diplôme d'études secondaires")
    # dff2 = dff2.replace('Post-secondary diploma', 'Diplôme post-secondaire')
    # dff2 = dff2.replace('University Diploma', "Diplôme universtaire")
    # dff2 = dff2.replace("Volunteer rate", "Taux de bénévolat")
    dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
    name2 = "% heures de bénévolat"
    # name2 = "% volunteer hours"

    title = '{}, {}'.format("Pourcentage de la population et du nombre total <br> d’heures de bénévolat selon l’éducation", region)

    return perc_don_perc_amt(dff1, dff2, name1, name2, title)

@app.callback(
    dash.dependencies.Output('VolRateAvgHours-MarStat_13', 'figure'),
    [

        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):

    dff1 = VolRate_2018[VolRate_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "État civil"]
    # dff1 = dff1.replace('Married/common-law', 'Marié.e/union de fait')
    # dff1 = dff1.replace('Separated/divorced', 'Séparé.e/divorcé.e')
    # dff1 = dff1.replace('Married', 'Marié.e')
    # dff1 = dff1.replace('Living common-law', 'Union de fait')
    # dff1 = dff1.replace('Separated', 'Séparé.e')
    # dff1 = dff1.replace('Divorced', 'divorcé.e')
    # dff1 = dff1.replace('Widowed', 'Veuf.ve')
    # dff1 = dff1.replace('Single, never married', 'Célibataire, jamais marié.e')
    dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")

    # name1 = "Volunteer rate"
    name1 = 'Taux de bénévolat'


    dff2 = AvgTotHours_2018[AvgTotHours_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "État civil"]
    # dff2 = dff2.replace('Married/common-law', 'Marié.e/union de fait')
    # dff2 = dff2.replace('Separated/divorced', 'Séparé.e/divorcé.e')
    # dff2 = dff2.replace('Married', 'Marié.e')
    # dff2 = dff2.replace('Living common-law', 'Union de fait')
    # dff2 = dff2.replace('Separated', 'Séparé.e')
    # dff2 = dff2.replace('Divorced', 'divorcé.e')
    # dff2 = dff2.replace('Widowed', 'Veuf.ve')
    # dff2 = dff2.replace('Single, never married', 'Célibataire, jamais marié.e')
    
    dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
    
    # name2 = "Average hours"
    name2 = "Nombre d'heures moyen"

    title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures <br> de bénévolat selon la situation matrimoniale", region)

    return don_rate_avg_don(dff1, dff2, name1, name2, title)


@app.callback(
    dash.dependencies.Output('PercVolHours-MarStat_13', 'figure'),
    [

        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = PercTotVols_2018[PercTotVols_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "État civil"]
    # dff1 = dff1.replace('Married/common-law', 'Marié.e/union de fait')
    # dff1 = dff1.replace('Separated/divorced', 'Séparé.e/divorcé.e')
    # dff1 = dff1.replace('Married', 'Marié.e')
    # dff1 = dff1.replace('Living common-law', 'Union de fait')
    # dff1 = dff1.replace('Separated', 'Séparé.e')
    # dff1 = dff1.replace('Divorced', 'divorcé.e')
    # dff1 = dff1.replace('Widowed', 'Veuf.ve')
    # dff1 = dff1.replace('Single, never married', 'Célibataire, jamais marié.e')
    dff1 = dff1.replace("% volunteers", "% population")
    # name1 = "% volunteers"
    name1 = "% population"


    dff2 = PercTotHours_2018[PercTotHours_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "État civil"]
    # dff2 = dff2.replace('Married/common-law', 'Marié.e/union de fait')
    # dff2 = dff2.replace('Separated/divorced', 'Séparé.e/divorcé.e')
    # dff2 = dff2.replace('Married', 'Marié.e')
    # dff2 = dff2.replace('Living common-law', 'Union de fait')
    # dff2 = dff2.replace('Separated', 'Séparé.e')
    # dff2 = dff2.replace('Divorced', 'divorcé.e')
    # dff2 = dff2.replace('Widowed', 'Veuf.ve')
    # dff2 = dff2.replace('Single, never married', 'Célibataire, jamais marié.e')
    # dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
    dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
    name2 = "% heures de bénévolat"
    # name2 = "% volunteer hours"

    title = '{}, {}'.format("Pourcentage de la population et du nombre total <br> d’heures de bénévolat selon la situation matrimoniale", region)

    return perc_don_perc_amt(dff1, dff2, name1, name2, title)

@app.callback(
    dash.dependencies.Output('VolRateAvgHours-Inc_13', 'figure'),
    [

        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = VolRate_2018[VolRate_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Catégorie de revenu familial"]
    # dff1 = dff1.replace('Less than $25,000', 'Moins de 25,000 $')
    # dff1 = dff1.replace('$25,000 to $49,999', '25,000 $ à 49,999 $')
    # dff1 = dff1.replace('$50,000 to $74,999', '50,000 $ a 74,999 $')
    # dff1 = dff1.replace('$75,000 to $99,999', '75,000 $ à 99,999 $')
    # dff1 = dff1.replace('$100,000 to $124,999', '100,000 $ à 124,999 $')
    # dff1 = dff1.replace('$125,000 and more', '125,000 $ et plus')
    dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")

    # name1 = "Volunteer rate"
    name1 = 'Taux de bénévolat'


    dff2 = AvgTotHours_2018[AvgTotHours_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Catégorie de revenu familial"]
    # dff2 = dff2.replace('Less than $25,000', 'Moins de 25,000 $')
    # dff2 = dff2.replace('$25,000 to $49,999', '25,000 $ à 49,999 $')
    # dff2 = dff2.replace('$50,000 to $74,999', '50,000 $ a 74,999 $')
    # dff2 = dff2.replace('$75,000 to $99,999', '75,000 $ à 99,999 $')
    # dff2 = dff2.replace('$100,000 to $124,999', '100,000 $ à 124,999 $')
    # dff2 = dff2.replace('$125,000 and more', '125,000 $ et plus')
    # dff2 = dff2.replace("Volunteer rate", "Taux de bénévolat")
    dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
    
    # name2 = "Average hours"
    name2 = "Nombre d'heures moyen"

    title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures <br> de bénévolat selon le revenu", region)

    return don_rate_avg_don(dff1, dff2, name1, name2, title)

@app.callback(
    dash.dependencies.Output('PercVolHours-Inc_fr', 'figure'),
    [

        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = PercTotVols_2018[PercTotVols_2018['Region'] == region]
    # dff1 = dff1.replace('$120,000 and more', '120 000 $ et plus')
    dff1 = dff1[dff1['Group'] == "Catégorie de revenu personnel"]
    # dff1 = dff1.replace('Less than $25,000', 'Moins de 25,000 $')
    # dff1 = dff1.replace('$25,000 to $49,999', '25,000 $ à 49,999 $')
    # dff1 = dff1.replace('$50,000 to $74,999', '50,000 $ a 74,999 $')
    # dff1 = dff1.replace('$75,000 to $99,999', '75,000 $ à 99,999 $')
    # dff1 = dff1.replace('$100,000 to $124,999', '100,000 $ à 124,999 $')
    dff1 = dff1.replace('$120,000 and more', '120 000 $ et plus')
    dff1 = dff1.replace("% volunteers", "% population")
    # name1 = "% volunteers"
    name1 = "% population"


    dff2 = PercTotHours_2018[PercTotHours_2018['Region'] == region]
    # dff2 = dff2.replace('$120 000 and more', '120 000 $ et plus')
    dff2 = dff2[dff2['Group'] == "Catégorie de revenu personnel"]
    dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
    # dff2 = dff2.replace('Less than $25,000', 'Moins de 25,000 $')
    # dff2 = dff2.replace('$25,000 to $49,999', '25,000 $ à 49,999 $')
    # dff2 = dff2.replace('$50,000 to $74,999', '50,000 $ a 74,999 $')
    # dff2 = dff2.replace('$75,000 to $99,999', '75,000 $ à 99,999 $')
    # dff2 = dff2.replace('$100,000 to $124,999', '100,000 $ à 124,999 $')
    
    # dff2 = dff2.replace("Volunteer rate", "Taux de bénévolat")
    # dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
    name2 = "% heures de bénévolat"
    # name2 = "% volunteer hours"

    title = '{}, {}'.format("Pourcentage de la population et du nombre total <br> d’heures de bénévolat selon le revenu", region)

    return perc_don_perc_amt(dff1, dff2, name1, name2, title)

@app.callback(
    dash.dependencies.Output('VolRateAvgHours-Relig_13', 'figure'),
    [

        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):

    dff1 = VolRate_2018[VolRate_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Fréquence de la fréquentation religieuse"]
    # dff1 = dff1.replace('At least once a week', 'Au moins 1 fois par semaine')
    # dff1 = dff1.replace('At least once a month', 'Au moins 1 fois par mois')
    # dff1 = dff1.replace('At least 3 times a year', 'Au moins 3 fois par mois')
    # dff1 = dff1.replace('Once or twice a year', '1 ou 2 fois par an')
    # dff1 = dff1.replace('Not at all', 'Pas du tout')
    dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")

    # name1 = "Volunteer rate"
    name1 = 'Taux de bénévolat'


    dff2 = AvgTotHours_2018[AvgTotHours_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Fréquence de la fréquentation religieuse"]
    # dff2 = dff2.replace('At least once a week', 'Au moins 1 fois par semaine')
    # dff2 = dff2.replace('At least once a month', 'Au moins 1 fois par mois')
    # dff2 = dff2.replace('At least 3 times a year', 'Au moins 3 fois par mois')
    # dff2 = dff2.replace('Once or twice a year', '1 ou 2 fois par an')
    # dff2 = dff2.replace('Not at all', 'Pas du tout')
    dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
    
    # name2 = "Average hours"
    name2 = "Nombre d'heures moyen"

    title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures de <br> bénévolat selon la pratique religieuse", region)

    return don_rate_avg_don(dff1, dff2, name1, name2, title)

@app.callback(
    dash.dependencies.Output('PercVolHours-Relig_13', 'figure'),
    [

        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = PercTotVols_2018[PercTotVols_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "Fréquence de la fréquentation religieuse"]
    # dff1 = dff1.replace('At least once a week', 'Au moins 1 fois par semaine')
    # dff1 = dff1.replace('At least once a month', 'Au moins 1 fois par mois')
    # dff1 = dff1.replace('At least 3 times a year', 'Au moins 3 fois par mois')
    # dff1 = dff1.replace('Once or twice a year', '1 ou 2 fois par an')
    # dff1 = dff1.replace('Not at all', 'Pas du tout')
    dff1 = dff1.replace("% volunteers", "% population")
    # name1 = "% volunteers"
    name1 = "% population"


    dff2 = PercTotHours_2018[PercTotHours_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "Fréquence de la fréquentation religieuse"]
    # dff2 = dff2.replace('At least once a week', 'Au moins 1 fois par semaine')
    # dff2 = dff2.replace('At least once a month', 'Au moins 1 fois par mois')
    # dff2 = dff2.replace('At least 3 times a year', 'Au moins 3 fois par mois')
    # dff2 = dff2.replace('Once or twice a year', '1 ou 2 fois par an')
    # dff2 = dff2.replace('Not at all', 'Pas du tout')
    # dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
    dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
    name2 = "% heures de bénévolat"
    # name2 = "% volunteer hours"

    title = '{}, {}'.format("Pourcentage de la population et du nombre total <br> d’heures de bénévolat selon la pratique religieuse", region)

    return perc_don_perc_amt(dff1, dff2, name1, name2, title)

# @app.callback(
#     dash.dependencies.Output('VolRateAvgHours-Labour', 'figure'),
#     [

#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):

#     dff1 = VolRate_2018[VolRate_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == "Situation d'activité"]
#     # dff1 = dff1.replace('Employed', 'Employé.e')
#     # dff1 = dff1.replace('Unemployed', 'Au chômage')
#     # dff1 = dff1.replace('Not in labour force', 'Pas dans la population active')
#     dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")

#     # name1 = "Volunteer rate"
#     name1 = 'Taux de bénévolat'


#     dff2 = AvgTotHours_2018[AvgTotHours_2018['Region'] == region]
#     dff2 = dff2[dff2['Group'] == "Situation d'activité"]
#     # dff2 = dff2.replace('Employed', 'Employé.e')
#     # dff2 = dff2.replace('Unemployed', 'Au chômage')
#     # dff2 = dff2.replace('Not in labour force', 'Pas dans la population active')
#     dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
    
#     # name2 = "Average hours"
#     name2 = "Nombre d'heures moyen"

#     title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures de <br> bénévolat selon la situation d’emploi", region)

#     return don_rate_avg_don(dff1, dff2, name1, name2, title)


# @app.callback(
#     dash.dependencies.Output('PercVolHours-Labour', 'figure'),
#     [

#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):

#     dff1 = PercTotVols_2018[PercTotVols_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == "Situation d'activité"]
#     # dff1 = dff1.replace('Employed', 'Employé.e')
#     # dff1 = dff1.replace('Unemployed', 'Au chômage')
#     # dff1 = dff1.replace('Not in labour force', 'Pas dans la population active')
#     # dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")
#     dff1 = dff1.replace("% volunteers", "% population")
#     # name1 = "% volunteers"
#     name1 = "% population"


#     dff2 = PercTotHours_2018[PercTotHours_2018['Region'] == region]
#     dff2 = dff2[dff2['Group'] == "Situation d'activité"]
#     # dff2 = dff2.replace('Employed', 'Employé.e')
#     # dff2 = dff2.replace('Unemployed', 'Au chômage')
#     # dff2 = dff2.replace('Not in labour force', 'Pas dans la population active')
#     # dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
#     dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
#     name2 = "% heures de bénévolat"
#     # name2 = "% volunteer hours"

#     title = '{}, {}'.format("Pourcentage de la population et du nombre total <br> d’heures de bénévolat selon la situation d’emploi", region)

#     return perc_don_perc_amt(dff1, dff2, name1, name2, title)

# @app.callback(
#     dash.dependencies.Output('VolRateAvgHours-ImmStat', 'figure'),
#     [

#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):

#     dff1 = VolRate_2018[VolRate_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == "Statut d'immigration"]
#     # dff1 = dff1.replace('Native-born', 'Né.e au Canada')
#     # dff1 = dff1.replace('Naturalized', 'Naturalisé.e')
#     # dff1 = dff1.replace('Non-Canadian', 'Non canadien.ne')
#     dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")

#     # name1 = "Volunteer rate"
#     name1 = 'Taux de bénévolat'


#     dff2 = AvgTotHours_2018[AvgTotHours_2018['Region'] == region]
#     dff2 = dff2[dff2['Group'] == "Statut d'immigration"]
#     # dff2 = dff2.replace('Native-born', 'Né.e au Canada')
#     # dff2 = dff2.replace('Naturalized', 'Naturalisé.e')
#     # dff2 = dff2.replace('Non-Canadian', 'Non canadien.ne')
#     dff2 = dff2.replace("Volunteer rate", "Taux de bénévolat")
#     dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
    
#     # name2 = "Average hours"
#     name2 = "Nombre d'heures moyen"

#     title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures de <br> bénévolat selon le statut d’immigration", region)

#     return don_rate_avg_don(dff1, dff2, name1, name2, title)

# @app.callback(
#     dash.dependencies.Output('PercVolHours-ImmStat', 'figure'),
#     [

#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     dff1 = PercTotVols_2018[PercTotVols_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == "Statut d'immigration"]
#     # dff1 = dff1.replace('Native-born', 'Né.e au Canada')
#     # dff1 = dff1.replace('Naturalized', 'Naturalisé.e')
#     # dff1 = dff1.replace('Non-Canadian', 'Non canadien.ne')
#     dff1 = dff1.replace("% volunteers", "% population")
#     # name1 = "% volunteers"
#     name1 = "% population"


#     dff2 = PercTotHours_2018[PercTotHours_2018['Region'] == region]
#     dff2 = dff2[dff2['Group'] == "Statut d'immigration"]
#     # dff2 = dff2.replace('Native-born', 'Né.e au Canada')
#     # dff2 = dff2.replace('Naturalized', 'Naturalisé.e')
#     # dff2 = dff2.replace('Non-Canadian', 'Non canadien.ne')
#     # dff2 = dff2.replace("Volunteer rate", "Taux de bénévolat")
#     dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
#     name2 = "% heures de bénévolat"
#     # name2 = "% volunteer hours"

#     title = '{}, {}'.format("Pourcentage de la population et du nombre total <br> d’heures de bénévolat selon le statut d’immigration", region)

#     return perc_don_perc_amt(dff1, dff2, name1, name2, title)


@app.callback(
    dash.dependencies.Output('status-hours_13', 'figure'),
    [

        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('status-selection2', 'value')

    ])
def update_graph(region, status):

    dff1 = VolRate_2018[VolRate_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == status]
    dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")
    # name1 = "Volunteer rate"
    name1 = "Taux de bénévolat"


    dff2 = AvgTotHours_2018[AvgTotHours_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == status]
    
    dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
    
    # name2 = "Average hours"
    name2 = "Nombre d'heures moyen"

    title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures de <br> bénévolat selon " + str(status).lower(), region)

    return don_rate_avg_don(dff1, dff2, name1, name2, title)


@app.callback(
    dash.dependencies.Output('status-perc_13', 'figure'),
    [

        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('status-selection', 'value')

    ])
def update_graph(region, status):
    dff1 = PercTotVols_2018[PercTotVols_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == status]
    dff1 = dff1.replace("% volunteers", "% population")
    # name1 = "% Canadians"
    name1 = "% population"


    dff2 = PercTotHours_2018[PercTotHours_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == status]
    dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
    name2 = "% heures de bénévolat"
    # name2 = "% volunteer hours"

    title = '{}, {}'.format("Pourcentage de la population et du nombre total <br> d’heures de bénévolat selon " + str(status).lower(), region)

    return perc_don_perc_amt(dff1, dff2, name1, name2, title)