import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc

from utils.graphs.WTO0107_graph_utils import rate_avg_cause, single_vertical_percentage_graph
from utils.data.WTO0107_data_utils import get_data, process_data, get_region_names, get_region_values

from app import app
from homepage import footer #navbar, footer

####################### Data processing ######################
SubSecDonRates_2018, SubSecAvgDon_2018, Allocation_2018 = get_data()
data = [SubSecDonRates_2018, SubSecAvgDon_2018, Allocation_2018]
process_data(data)

region_values = get_region_values()
region_names = get_region_names()

###################### App layout ######################
navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                # dcc.Link("Home", href="/")
                dbc.NavLink("À propos", href="https://www.donetbenevolat.ca/",external_link=True)
            ),
            dbc.NavItem(
                dbc.NavLink("EN", href="http://app.givingandvolunteering.ca/What_types_of_organizations_do_Canadians_support_2018",external_link=True)
            ),
        ],
        brand="Don et Benevolat",
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
                        html.H1("Quels types d'organismes soutient-on au Canada?"),
                        # html.Span(
                        #     'David Lasby',
                        #     className='meta')
                        ], className='post-heading'
                    ), className='col-md-10 col-lg-8 mx-auto position-relative'
                )
            )
        )], className="bg-secondary text-white text-center py-4",
    ),
    # Note: filters put in separate container to make floating element later
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
                    dcc.Markdown('''
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, un peu plus de deux tiers des personnes (68 %) au Canada ont donné à un organisme de bienfaisance ou à but non lucratif pendant l’année qui l’a précédée et leur contribution individuelle moyenne s’est chiffrée à 569 $. Ces personnes ont fait, en moyenne, 3,7 dons au bénéfice de 2,5 causes (c.-à-d. elles ont été nombreuses à faire plusieurs dons à la même cause). La majorité d’entre elles ont soutenu plusieurs causes. À l’échelle nationale, environ un tiers des donateur.trice.s (31 %) a soutenu une seule cause, un peu plus d’un quart (27 %) en a soutenu deux, environ un cinquième (19 %) trois et le reste (23 %) en a soutenu quatre ou plus.
                    ''',className='mt-4'),
                    dcc.Markdown('''
                    Nous décrivons ci-dessous les tendances de leur soutien au niveau national et, pour obtenir des précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer des résultats au niveau national décrits dans le texte, les tendances générales sont très similaires.
                    '''),
                    # dcc.Markdown('''
                    # Canadians are most likely to volunteer for social services and sports & recreation organizations and for religious congregations. In terms of the hours typically contributed, volunteers for these three causes tend to be towards the most committed; these causes rank in the top five in terms of average hours volunteered (at the national level). In contrast, volunteers for the next three most commonly supported causes (education & research, development & housing, and health) tend to contribute somewhat fewer hours, with these causes ranking in the bottom four in terms of average hours volunteered in spite of having comparatively broad bases of support. The bases of support for the remaining eight causes are somewhat narrower, ranging between one in 30 and one in 100 Canadians, depending on the specific cause. Overall, volunteers for these causes tend to be more towards the middle of the range in terms of the hours they volunteer. Only hospitals and grantmaking & fundraising organizations stand out as being particularly highly or lowly ranked in terms of average volunteer hours, at least at the national level.
                    #  '''),
                    dcc.Markdown('''
                    L’examen des pourcentages de personnes qui soutiennent chaque cause au Canada et des montants qu’elles ont tendance à donner semble indiquer trois grands niveaux de soutien. Le premier est celui des causes à la base de soutien la plus large (entre une sur trois et une sur six personnes au Canada). Ces causes sont les organismes des secteurs de la santé, des services sociaux, les organismes religieux, ainsi que les hôpitaux. À l’exception notable des organismes religieux, le montant des dons au bénéfice de ces causes a tendance à être relativement modeste. Le deuxième niveau de soutien est celui des causes soutenues par une sur dix à une sur quinze personnes au Canada. À ce niveau, les organismes des secteurs du sport et des loisirs et de l’éducation et de la recherche ont tendance à recevoir des dons moins importants que les autres causes, leurs dons étant notamment inférieurs à ceux au bénéfice du développement international, de l’aide internationale, de l’octroi de subventions et de la collecte de fonds. Le troisième niveau de soutien est celui des organismes des secteurs du droit, du plaidoyer, de la politique, des arts et de la culture, de l’aménagement et du logement, ainsi que des universités et des collèges et des associations professionnelles et des syndicats. Ces causes sont soutenues par moins d’une personne sur vingt au Canada, bien que les montants de leurs dons aient tendance à être supérieurs à ceux au bénéfice de la majorité des autres causes.
                    '''),
                    # Levels of support by cause
                    dcc.Graph(id='DonRateAvgDonAmt-Cause', style={'marginTop': marginTop}),
                    dcc.Markdown('''
                    Au total, les contributions financières aux organismes de bienfaisance et à but non lucratif se chiffrent approximativement à 11,9 milliards $. La proportion la plus importante de ces dons, et de loin, est au bénéfice des organismes religieux, en raison de leur large base de soutien, par comparaison avec les autres organismes, et des montants habituellement très élevés des dons à leur bénéfice. Les organismes des secteurs de la santé et des services sociaux sont associés aux proportions suivantes du total des dons par ordre d’importance décroissante, principalement en raison de leurs larges bases de soutien. À l’échelle nationale, les hôpitaux sont à la traîne des organismes à vocation internationale, en raison des montants habituellement très élevés des dons au bénéfice des causes du développement international et de l’aide internationale. Dans le même ordre d’idées, les organismes à vocation environnementale et les universités et les collèges se situent à un niveau relativement supérieur à celui auquel on aurait pu s’attendre, en raison des montants importants qu’ils ont tendance à recevoir.
                    '''),
                    # Allocation of support by cause
                    dcc.Graph(id='AllocationSupport-Cause', style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
   ),
   footer
])

################### CALLBACKS ###################

@app.callback(

    dash.dependencies.Output('DonRateAvgDonAmt-Cause', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):

    dff1 = SubSecDonRates_2018[SubSecDonRates_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "All"]
    dff1 = dff1.replace('Donation rate', 'Taux de donateur.trice.s')
    # name1 = "Donation rate"
    name1 = "Taux de donateur.trice.s"

    dff2 = SubSecAvgDon_2018[SubSecAvgDon_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "All"]
    dff2 = dff2.replace('Average donation', 'Dons annuels moyens')
    # name2 = "Average donation"
    name2 = 'Dons annuels moyens'

    title = '{}, {}'.format("Niveaux de soutien par cause", region)

    return rate_avg_cause(dff1, dff2, name1, name2, title)

@app.callback(

    dash.dependencies.Output('AllocationSupport-Cause', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):

    dff = Allocation_2018[Allocation_2018['Region'] == region]
    title = '{}, {}'.format("Répartition du soutien par cause", region)

    return single_vertical_percentage_graph(dff, title, by="QuestionText", sort=True)
