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
                        html.H1('Qui sont les bénévoles et combien d’heures donnent-ils? (2013)'),
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
   dbc.Container(
       dbc.Row([
            # Starting text
            html.Div([
                    dcc.Markdown("""
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2013, près de neuf personnes sur dix (85 %) au Canada ont fait don de leur temps pour une forme ou une autre d’activité prosociale pendant la période d’un an qui l’a précédée. Plus de deux cinquièmes des personnes au Canada (44 %) étaient des bénévoles encadrés, qui faisaient don de leur temps à des organismes de bienfaisance ou à but non lucratif, et environ quatre cinquièmes des personnes (82 %) étaient des bénévoles non encadrés, qui faisaient directement don de leur temps à des personnes dans le besoin non membre de leur ménage, et ce, en dehors d’un organisme. À l’échelle nationale, les bénévoles encadrés ont fait chacun don de 154 heures en moyenne, soit, au total, 2,0 milliards d’heures de bénévolat au bénéfice des organismes de bienfaisance et sans but lucratif équivalant à environ 1,0 million d’emplois à temps plein.
                    """),
                    # Forms of volunteering graph
                    #dcc.Graph(id='ActivitiesVolRateAvgHrs', style={'marginTop': 20}),
                 ], className='col-md-10 col-lg-8 mx-auto'
            ),
                
            html.Div([
                    dcc.Markdown("""
                    La probabilité de faire du bénévolat pour un organisme de bienfaisance ou à but non lucratif variait selon le lieu de résidence des bénévoles. Pour la majorité des provinces, la proportion de bénévoles se situait à la norme nationale ou légèrement au-dessus de celle-ci. Elle était nettement supérieure à la norme dans la Saskatchewan et au Manitoba et nettement inférieure à la norme au Québec. Pour la majorité des provinces, le nombre moyen d’heures de bénévolat ne s’écartait pas de manière significative de la norme nationale, à l’exception notable du Québec.
                    """),
           
                    # Volunteer rate & average hours volunteered by province graph
                    #dcc.Graph(id='ActivitiesVolRateAvgHrs', style={'marginTop': 20}),
                 ], className='col-md-10 col-lg-8 mx-auto'
            ),
            
        
            # Personal & Economic Characteristics
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

                    
                    # Gender
                    html.Div([
                        html.H4("Genre"),
                        html.P("""
                        Au niveau national, les femmes étaient légèrement plus enclines à faire du bénévolat que les hommes (respectivement 45 % et 42 %), bien que les hommes aient légèrement plus tendance à faire don de plus d’heures quand ils faisaient du bénévolat.
                        """),
                        # Volunteer rate & average volunteer hours by gender graph
                        #dcc.Graph(id='ActivityVolRate-Gndr', style={'marginTop': marginTop}),
                    ]),
                    html.Div([
                    dcc.Markdown("""
                    Dans l’ensemble, les pourcentages du nombre total d’heures de bénévolat des hommes et des femmes étaient très comparables à leur représentation au sein de la population (c.-à-d. que le nombre d’heures de bénévolat de l’un ou l’autre genre n’était pas nettement plus ou moins élevé par rapport à son nombre).
                    """),
                        # Percentage of population & total volunteer hours by gender graph
                        #dcc.Graph(id='ActivityVolRate-Gndr', style={'marginTop': marginTop}),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("""
                        Les personnes plus jeunes et d’âge moyen étaient les plus susceptibles de faire du bénévolat, surtout celles âgées de 15 à 24 ans. Après l’âge de 65 ans, la probabilité de faire du bénévolat chutait fortement. Quant aux heures de bénévolat caractéristiques, les personnes de moins de 55 ans avaient tendance à faire don de moins d’heures.
                        """),
                        # Volunteer rate & average volunteer hours by age graph
                        #dcc.Graph(id='ActivityVolRate-Age', style={'marginTop': marginTop}),
                    ]),
                    html.Div([
                    dcc.Markdown("""
                    Étant donné leur tendance à faire don de moins d’heures, les bénévoles âgés de 24 à 44 ans représentaient moins d’heures que leur représentation au sein de la population ne le donnait à penser. En revanche, les bénévoles âgés de 55 à 74 ans représentaient des pourcentages du nombre total d’heures excessivement élevés compte tenu de leur nombre..
                    """),
                        # Percentage of population & total volunteer hours by age graph
                        #dcc.Graph(id='ActivityVolRate-Age', style={'marginTop': marginTop}),
                    ]),
                    
                    # Formal Education
                    html.Div([
                        html.H5("Éducation formelle"),
                        html.P("""
                        La probabilité de faire du bénévolat avait tendance à augmenter en allant de pair avec les niveaux d’études supérieurs au diplôme d’études secondaires, les titulaires d’un diplôme universitaire étant enclins à faire don d’un nombre d’heures relativement plus élevé que les autres.
                        """),
                        # Volunteer rate & average volunteer hours by formal education graph
                        #dcc.Graph(id='ActivityVolRate-Educ', style={'marginTop': marginTop}),
                    ]),
                        
                    html.Div([
                    dcc.Markdown("""
                    À l’échelle nationale, les bénévoles titulaires d’un diplôme d’études secondaires faisaient don d’un nombre d’heures légèrement inférieur à leur représentation au sein de la population, tandis que les bénévoles titulaires d’un diplôme universitaire faisaient don d’un nombre d’heures relativement supérieur à celui auquel on pourrait s’attendre.
                    """),
                        # Percentage of population & total volunteer hours by formal education graph
                        #dcc.Graph(id='ActivityVolRate-Educ', style={'marginTop': marginTop}),
                    ]),
                    # Marital Status
                    html.Div([
                        html.H5("Situation matrimoniale"),
                        html.P("""
                        Les personnes célibataires et mariées étaient les plus enclines à faire du bénévolat, contrairement aux personnes veuves. Ces dernières avaient tendance à faire don d’un plus grand nombre d’heures quand elles faisaient du bénévolat, tandis que les célibataires en faisaient souvent relativement moins.
                        """),
                        # Volunteer rate & average volunteer hours by marital status graph
                        #dcc.Graph(id='ActivityVolRate-MarStat', style={'marginTop': marginTop}),
                    ]),
                    html.Div([
                    dcc.Markdown("""
                    Les variations de la probabilité de faire du bénévolat et des heures de bénévolat caractéristiques se compensaient presque totalement, ce qui veut dire que chaque groupe représentait presque exactement la proportion des heures de bénévolat à laquelle on pourrait s’attendre, étant donné leur nombre respectif au sein de la population canadienne.
                    """),
                        # Percentage of population & total volunteer hours by marital status graph
                        #dcc.Graph(id='ActivityVolRate-Educ', style={'marginTop': marginTop}),
                    ]),
                        
                    # Income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("""
                        D’une façon très générale, la probabilité de faire du bénévolat avait tendance à augmenter avec le revenu du ménage, tandis que le nombre d’heures de bénévolat des ménages au revenu égal ou supérieur à 120 000 $ avait tendance à être inférieur.
                        """),
                        # Volunteer rate & average volunteer hours by household income graph
                        #dcc.Graph(id='ActivityVolRate-Inc', style={'marginTop': marginTop}),
                    ]),
                    html.Div([
                    dcc.Markdown("""
                    Dans l’ensemble, chaque groupe de revenu représentait à peu près la même proportion du nombre total d’heures de bénévolat que sa proportion au sein de la population canadienne (c.-à-d. aucun groupe ne se distingue en faisant don de nettement plus ou moins d’heures par rapport à son nombre).
                    """),
                        # Percentage of population & total volunteer hours by household income graph
                        #dcc.Graph(id='ActivityVolRate-Educ', style={'marginTop': marginTop}),
                    ]),
                        
                        
                    # Religious Attendance
                    html.Div([
                        html.H5("Pratique religieuse"),
                        html.P("""
                        La probabilité de faire du bénévolat avait tendance à augmenter avec l’assiduité aux offices religieux. À l’exception des personnes qui assistaient aux services une fois par semaine (enclines à faire don de beaucoup plus de temps), les bénévoles avaient tendance à faire don d’un nombre d’heures relativement uniforme.
                        """),
                        # Volunteer rate & average volunteer hours by religious attendance graph
                        #dcc.Graph(id='ActivityVolRate-Relig', style={'marginTop': marginTop}),
                    ]),
                        
                    html.Div([
                    dcc.Markdown("""
                    Étant donné leur taux de bénévolat supérieur et le nombre d’heures de bénévolat significativement plus important dont elles avaient tendance à faire don, les personnes présentes chaque semaine aux offices religieux représentaient une proportion des heures de bénévolat très supérieure à leur représentation au sein de la population. Les personnes qui n’assistaient pas aux services religieux représentaient une proportion des heures de bénévolat significativement inférieure à celle que leur nombre permettait de présager.
                    """),
                        # Percentage of population & total volunteer hours by religious attendance graph
                        #dcc.Graph(id='ActivityVolRate-Educ', style={'marginTop': marginTop}),
                    ]),
                        
                    # Other Factors
                    html.Div([
                        html.H5("Autres facteurs"),
                        html.P("""
                        Au chapitre de la situation d’emploi, les personnes employées étaient plus susceptibles de faire du bénévolat que les personnes non membres de la population active, bien que ces dernières avaient tendance à faire don de plus d’heures quand elles faisaient effectivement du bénévolat. Ces deux tendances s’annulaient largement, la répartition des heures de bénévolat suivant d’assez près la population dans son ensemble. Quant au statut d’immigration, les personnes nées au Canada avaient légèrement plus tendance à faire du bénévolat que les personnes nouvellement arrivées au Canada, mais pas suffisamment pour créer une différence significative dans la répartition du nombre total d’heures de bénévolat.
                        """),
                        # Volunteer rate & average volunteer hours by labour force status graph
                        # dcc.Graph(id='ActivityVolRate-Labour', style={'marginTop': marginTop}),
                        # Volunteer rate & average volunteer hours by immigration status
                        # dcc.Graph(id='ActivityVolRate-ImmStat', style={'marginTop': marginTop}),
                        # Percentage of population & total volunteer hours by labour force status
                        # dcc.Graph(id='ActivityVolRate-ImmStat', style={'marginTop': marginTop}),
                        # Percentage of population & total volunteer hours by immigration status
                        # dcc.Graph(id='ActivityVolRate-ImmStat', style={'marginTop': marginTop}),
                        # html.Div([
                        #     html.Div(['Select status:',
                        #               dcc.Dropdown(
                        #                   id='status-selection',
                        #                   options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                        #                   value='Labour force status',
                        #                   style={'verticalAlign': 'middle'}
                        #               ),],
                        #              style={'width': '33%', 'display': 'inline-block'})
                        # ]),
                        # dcc.Graph(id='status-fig', style={'marginTop': marginTop})
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'

            ),
        ]),
   ),
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
