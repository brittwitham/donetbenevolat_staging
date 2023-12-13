import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd

from utils.home_button import gen_home_button
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc
import os
import os.path as op

from utils.graphs.WTO0207_graph_utils import rate_avg_cause, single_vertical_percentage_graph
from utils.data.WTO0207_data_utils import get_data, process_data, get_region_names, get_region_values

from app import app
from homepage import footer #navbar, footer
from utils.gen_navbar import gen_navbar

####################### Data processing ######################
BarriersVol_2018, SubSecAvgHrs_2018, SubSecVolRates_2018, AllocationVol_2018 = get_data()

data = [SubSecVolRates_2018, SubSecAvgHrs_2018, AllocationVol_2018]
process_data(data)

# region_values = get_region_values()
# region_names = get_region_names()
region_names = ['CA', 'BC', 'AB', 'PR', 'ON', 'QC', 'AT']
###################### App layout ######################
navbar = gen_navbar("What_types_of_organizations_do_Canadians_volunteer_for_2018")

marginTop = 20
home_button = gen_home_button()

layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1('À quels types d’organismes fait-on don de son temps au Canada?'),
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
        className="sub-header bg-secondary text-white text-center pt-5",
    ),
    # Dropdown menu
    dbc.Container([
        home_button,
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
    ],className='sticky-top select-region mb-2', fluid=True),
   dbc.Container(
       dbc.Row([
            html.Div(
                [
                    dcc.Markdown('''
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, un peu plus de deux cinquièmes des personnes (41 %) au Canada ont fait du bénévolat pour un organisme de bienfaisance ou à but non lucratif pendant l’année qui l’a précédée, en leur faisant don de 131 heures en moyenne par personne. En moyenne, les bénévoles ont fait don de leur temps à 1,4 cause. La majorité des bénévoles (62 %) ont fait don de leur temps à une seule cause, un peu plus d’un quart d’entre eux (28 %) à deux causes et les autres (10 %) à trois causes.
                    ''',className='mt-4'),
                    dcc.Markdown('''
                    Nous décrivons ci-dessous les tendances de leur soutien au niveau national et, pour obtenir des précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer des résultats au niveau national décrits dans le texte, les tendances générales sont très similaires dans l’ensemble.
                    '''),
                    dcc.Markdown('''
                    Les personnes au Canada sont les plus enclines à faire du bénévolat pour les organismes du secteur des services sociaux et de celui du sport et des loisirs, ainsi que pour les congrégations religieuses. S’agissant du nombre d’heures de bénévolat habituel, les bénévoles qui font don de leur temps à ces trois causes ont tendance à se rapprocher de ceux qui s’engagent le plus. En effet, ces causes se situent parmi les cinq causes au bénéfice desquelles le nombre moyen d’heures de bénévolat est le plus élevé (au niveau national). En revanche, les bénévoles des trois causes les plus soutenues suivantes (éducation et recherche, aménagement et logement, et santé) ont tendance à faire don de relativement moins d’heures, ces causes faisant partie des quatre dernières du point de vue des heures de bénévolat qui leur sont consacrées, malgré leurs bases de soutien relativement larges. Les bases de soutien des huit causes restantes sont un peu plus étroites, en s’échelonnant de 30 à une personne sur 100 au Canada, selon le cas. Dans l’ensemble, les bénévoles au service de ces causes ont tendance à se rapprocher davantage du milieu de la fourchette des heures de bénévolat. Les hôpitaux et les organismes d’octroi de subventions et de collecte de fonds sont les seuls à se distinguer dans le classement selon leur nombre moyen d’heures de bénévolat particulièrement élevé ou bas, du moins au niveau national.
                    '''),
                    # Levels of support by cause
                    dcc.Graph(id='DonRateAvgDonAmt-Cause-2', style={'marginTop': marginTop}),
                    html.Br(),
                    dcc.Markdown('''
                    Au total, les personnes au Canada font don d’un peu moins d’1,7 milliard d’heures de bénévolat par année aux organismes de bienfaisance et à but non lucratif, ce qui équivaut à environ 863 000 emplois à plein temps. La plus grande partie de ce soutien, et de loin, est offerte aux organismes du secteur des services sociaux et à celui du sport et des loisirs, ainsi qu’aux organismes religieux qui reçoivent collectivement plus de la moitié du total des heures de bénévolat. Les cinq causes suivantes (éducation et recherche, aménagement et logement, arts et culture, santé et environnement) reçoivent chacune au moins une heure de bénévolat sur vingt. À l’échelle nationale, ces causes représentent collectivement plus du quart des heures de bénévolat. Les sept causes restantes représentent à elles toutes environ 16 % du total des heures, le niveau de leur soutien s’échelonnant de quatre pour cent du total des heures, pour les hôpitaux, à un pour cent du total des heures pour les organismes du développement international et de l’aide internationale.
                    '''),
                    # Allocation of support by cause
                    dcc.Graph(id='AllocationSupport-Cause-2', style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
   ),
   footer
])

################## CALLBACKS ##################

@app.callback(

    dash.dependencies.Output('DonRateAvgDonAmt-Cause-2', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):

    dff1 = SubSecVolRates_2018[SubSecVolRates_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "All"]
    dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")
    # name1 = "Volunteer rate"
    name1 = "Taux de bénévolat"

    dff2 = SubSecAvgHrs_2018[SubSecAvgHrs_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "All"]
    dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
    # name2 = "Average hours"
    name2 = "Nombre d'heures moyen"

    title = '{}, {}'.format("Niveaux de soutien par cause", region)

    return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)


@app.callback(

    dash.dependencies.Output('AllocationSupport-Cause-2', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):

    dff = AllocationVol_2018[AllocationVol_2018['Region'] == region]
    title = '{}, {}'.format("Répartition du soutien par cause", region)

    return single_vertical_percentage_graph(dff, title, by="QuestionText", sort=True)


# import dash
# from dash import dcc, html
# import plotly.graph_objects as go
# import numpy as np
# import pandas as pd
# pd.options.mode.chained_assignment = None  # default='warn'
# import dash_bootstrap_components as dbc
# import os
# import os.path as op

# from utils.graphs.WTO0207_graph_utils import rate_avg_cause, single_vertical_percentage_graph
# from utils.data.WTO0207_data_utils import get_data, process_data, get_region_names, get_region_values

# from app import app
# from homepage import navbar, footer

# ####################### Data processing ######################
# BarriersVol_2018, SubSecAvgHrs_2018, SubSecVolRates_2018, AllocationVol_2018 = get_data()

# data = [SubSecVolRates_2018, SubSecAvgHrs_2018, AllocationVol_2018]
# process_data(data)

# # region_values = get_region_values()
# # region_names = get_region_names()
# region_names = ['CA', 'BC', 'AB', 'PR', 'ON', 'QC', 'AT']

# ###################### App layout ######################

# marginTop = 20

# layout = html.Div([
#     navbar,
#     html.Header([
#         html.Div(className='overlay'),
#         dbc.Container(
#             dbc.Row(
#                 html.Div(
#                     html.Div([
#                         html.H1('À Quels Types D’Organismes Fait-On Don De Son Temps Au Canada?'),
#                         # html.Span(
#                         #     'David Lasby',
#                         #     className='meta'
#                         # )
#                         ],
#                         className='post-heading'
#                     ),
#                     className='col-md-10 col-lg-8 mx-auto position-relative'
#                 )
#             )
#         ),
#     ],
#         # className='masthead'
#         className="sub-header bg-secondary text-white text-center pt-5",
#     ),
#     # Dropdown menu
#     # dbc.Container([
#     #     dbc.Row(
#     #        dbc.Col(
#     #            html.Div([
#     #                "Sélectionnez une région:",
#     #                dcc.Dropdown(
#     #                    id='region-selection',
#     #                    options=[{'label': region_names[i], 'value': region_values[i]} for i in range(len(region_values))],
#     #                    value='CA',
#     #                    ),
#     #                 html.Br(),
#     #             ],className="m-2 p-2"),
#     #         ),id='sticky-dropdown'),
#     # ],className='sticky-top select-region mb-2', fluid=True),
#    dbc.Container(
#        dbc.Row([
#             html.Div(
#                 [
#                     dcc.Markdown('''
#                     According to the 2018 General Social Survey on Giving, Volunteering, and Participating, just over two fifths of Canadians (41%) volunteered for a charitable or nonprofit organization during the one year period prior to the survey, contributing an average of 131 hours each.  On average, volunteers contributed time to 1.4 causes. Most volunteers (62%) contributed time to one cause, just over a quarter (28%) to two, and the balance (10%) to three.
#                     ''',className='mt-4'),
#                     dcc.Markdown('''
#                     Below, we describe patterns of support by cause at the national level. In addition, readers can use the pull down menu linked to the interactive data visualizations to show regional level results. While the regional specifics may differ from the national level results described in the text, the overall trends are generally quite similar.
#                     '''),
#                     dcc.Markdown('''
#                     Canadians are most likely to volunteer for social services and sports & recreation organizations and for religious congregations. In terms of the hours typically contributed, volunteers for these three causes tend to be towards the most committed; these causes rank in the top five in terms of average hours volunteered (at the national level). In contrast, volunteers for the next three most commonly supported causes (education & research, development & housing, and health) tend to contribute somewhat fewer hours, with these causes ranking in the bottom four in terms of average hours volunteered in spite of their comparatively broad bases of support. The bases of support for the remaining eight causes are somewhat narrower, ranging between one in 30 and one in 100 Canadians, depending on the specific cause. Overall, volunteers for these causes tend to be more towards the middle of the range in terms of the hours they volunteer. Only hospitals and grantmaking & fundraising organizations stand out as being particularly highly or lowly ranked in terms of average volunteer hours, at least at the national level.
#                     '''),
#                     # Levels of support by cause
#                     html.Div([
#                    "Sélectionnez une région:",
#                    dcc.Dropdown(
#                        id='region-selection1',
#                        options=[{'label': region_names[i], 'value': region_names[i]} for i in range(len(region_names))],
#                        value='CA',
#                        ),
#                     # html.Br(),
#                         ],className="m-2 p-2"),
#                     dcc.Graph(id='DonRateAvgDonAmt-Cause-2', style={'marginTop': marginTop}),
#                     dcc.Markdown('''
#                     In total, Canadians contribute just under 1.7 billion volunteer hours to charitable and nonprofit organizations annually, equivalent to about 863 thousand full-time jobs.  By far the largest portion of this support goes to social services, sports & recreation and religious organizations which collectively receive over half of total hours volunteered. The next five causes (education & research, development & housing, arts & culture, health, and the environment) each receive at least one of every twenty hours volunteered. Nationally, they collectively account for over a quarter of volunteer hours. The remaining seven causes together account for about 16% of total hours, with the level of support ranging from four percent of total hours for hospitals to one percent for international development and relief organizations.
#                     '''),
#                     # Allocation of support by cause
#                     html.Div([
#                    "Sélectionnez une région:",
#                    dcc.Dropdown(
#                        id='region-selection2',
#                        options=[{'label': region_names[i], 'value': region_names[i]} for i in range(len(region_names))],
#                        value='CA',
#                        ),],className="m-2 p-2"),
#                     dcc.Graph(id='AllocationSupport-Cause-2', style={'marginTop': marginTop}),
#                 ], className='col-md-10 col-lg-8 mx-auto'
#             ),
#         ]),
#    ),
#    footer
# ])

# ################## CALLBACKS ##################

# @app.callback(

#     dash.dependencies.Output('DonRateAvgDonAmt-Cause-2', 'figure'),
#     [
#         dash.dependencies.Input('region-selection1', 'value')
#     ])
# def update_graph(region):

#     dff1 = SubSecVolRates_2018[SubSecVolRates_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == "All"]
#     name1 = "Volunteer rate"

#     dff2 = SubSecAvgHrs_2018[SubSecAvgHrs_2018['Region'] == region]
#     dff2 = dff2[dff2['Group'] == "All"]
#     name2 = "Average hours"

#     title = '{}, {}'.format("Levels of support by cause", region)

#     return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)


# @app.callback(

#     dash.dependencies.Output('AllocationSupport-Cause-2', 'figure'),
#     [
#         dash.dependencies.Input('region-selection2', 'value')
#     ])
# def update_graph(region):

#     dff = AllocationVol_2018[AllocationVol_2018['Region'] == region]
#     title = '{}, {}'.format("Allocation of support by cause", region)

#     return single_vertical_percentage_graph(dff, title, by="QuestionText", sort=True)
