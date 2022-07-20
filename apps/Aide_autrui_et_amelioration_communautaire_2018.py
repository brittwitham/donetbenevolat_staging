import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc

from utils.graphs.HOA0204_graph_utils import forms_of_giving, rate_avg_cause, triple_vertical_graphs_rates
from utils.data.HOA0204_data_utils import get_data, process_data, get_region_names, get_region_values

from app import app
from homepage import footer #navbar, footer

####################### Data processing ######################
VolRate_2018, CommInvolveHrs_2018, CommInvolveRate_2018, HelpDirectHrs_2018, HelpDirectRate_2018, FormsVolunteering_2018 = get_data()
data = [VolRate_2018, CommInvolveHrs_2018, CommInvolveRate_2018, HelpDirectHrs_2018, HelpDirectRate_2018, FormsVolunteering_2018]

process_data(data)
region_values = get_region_values()
region_names = get_region_names()

# demo_names = ['Age group', 'Gender', 'Education',
#             'Marital status', 'Labour force status', 'Catégorie de revenu personnel',
#             'Frequency of religious attendance', 'Immigration status']
demo_names = ["Groupe d'âge", 'Genre', 'Éducation',
            'État civil', "Situation d'activité", 'Catégorie de revenu personnel',
            'Fréquence de la fréquentation religieuse', "Statut d'immigration"]


###################### App layout ######################
navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                # dcc.Link("Home", href="/")
                dbc.NavLink("Home", href="/",external_link=True)
            ),
            dbc.NavItem(
                dbc.NavLink("EN", href="http://app.givingandvolunteering.ca/Helping_others_and_community_improvement_2018",external_link=True)
            ),
        ],
        brand="Don et Benevolat",
        brand_href="/",
        color="#c7102e",
        dark=True,
        sticky='top'
    )

marginTop = 20

heading = 'Aide d’autrui et amélioration communautaire'

layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1(heading),
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
    # Dropdown menu
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
            html.Div(
                [
                    dcc.Markdown('''
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, un peu plus de deux personnes sur cinq (41 %) âgées de 15 ans ou plus au Canada ont fait du bénévolat pour un organisme de bienfaisance ou à but non lucratif pendant la période d’un an qui l’a précédée. En plus du bénévolat pour les organismes (qu’on appelle le bénévolat encadré), presque trois quarts des personnes au Canada étaient des bénévoles non encadrés, en dehors d’un organisme. Ils ont pratiqué cette forme de bénévolat de deux façons; un peu plus de deux tiers de ces personnes ont aidé directement des personnes non membres de leur ménage et environ un quart d’entre elles ont participé à des activités d’amélioration communautaire.
                    ''',className='mt-4'),
                    dcc.Markdown('''
                    Nous décrivons ci-dessous les tendances du bénévolat encadré et du bénévolat non encadré au niveau national. Nous décrivons dans le texte les résultats au niveau national, mais, pour obtenir des précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer des résultats au niveau national décrits dans le texte, les tendances générales sont très similaires.
                    ''',className='mt-4'),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Forms of volunteering
            html.Div(
                [
                    # html.H4('Formes de bénévolat ',className='mt-3'),
                    # Forms of volunteering graph
                    dcc.Graph(id='FormsVolunteering', style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    #How much time do Canadians contribute?
                    html.Div([
                        html.H4('Combien d’heures de son temps donne-t-on au Canada?',className='mt-3'),
                        html.P("""
                        En moyenne, les bénévoles encadrés font don de 131 heures par année aux organismes de bienfaisance et à but non lucratif, ce qui représente collectivement un peu moins de 1,7 milliard d’heures (soit l’équivalent de 863 000 emplois à temps plein). Les personnes qui en aident directement d’autres leur font don de 135 heures chacune en moyenne, pour un total de presque 2,9 milliards d’heures. À peine plus de trois cinquièmes des heures d’aide directe (1,8 milliard d’heures) sont consacrées au soutien de membres de leurs familles. Par comparaison avec les autres formes de bénévolat, les bénévoles qui œuvrent à l’amélioration de leur collectivité font plutôt habituellement don de moins d’heures (45 en moyenne), soit 387 millions d’heures au total.
                        """),              
                    ]),
                    # THelping others
                    html.Div([
                        html.H4("Aide d’autrui",className='mt-3'),
                        html.P("""
                        Un peu moins de la moitié des personnes au Canada aident les autres en cuisinant, en nettoyant, en jardinant, en effectuant des travaux d’entretien ou d’autres tâches domestiques et environ deux cinquièmes d’entre elles apportent leur aide pour des tâches liées à la santé ou aux soins personnels ou en magasinant, en conduisant ou en accompagnant quelqu’un à un magasin ou à un rendez-vous. Les tâches liées à la santé ou aux soins personnels prennent normalement plus de temps que les tâches domestiques ou que conduire ou accompagner quelqu’un. Environ un cinquième des personnes au Canada apportent leur aide pour des tâches administratives, comme les formulaires à remplir, les impôts, les opérations bancaires ou la recherche d’information et environ un dixième d’entre elles apportent leur aide sous forme d’enseignement, de tutorat, d’accompagnement ou d’aide à la lecture. D’autres formes d’aide sont relativement peu courantes, mais ont tendance à prendre beaucoup de temps.
                        """),
                        # Forms of helping others
                        html.Div([
                            dcc.Graph(id='VolRateAvgHrs-Helping', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Community improvement
                    html.Div([
                        html.H4("Amélioration communautaire",className='mt-3'),
                        html.P("""
                        Environ une personne sur sept au Canada produit ou diffuse de l’information pour améliorer la sensibilisation aux affaires municipales et une sur dix participe à des réunions publiques où elles sont débattues. Elles sont un peu moins nombreuses à organiser ou à coordonner des groupes ou des événements et environ une personne sur vingt participe directement à l’entretien ou à la réparation d’installations ou de lieux publics. Seulement une personne sur trente contribue à l’élaboration de projets économiques ou sociaux pour sa collectivité. Comme pour l’aide d’autrui, d’autres formes d’amélioration communautaire sont relativement peu courantes, mais ont tendance à prendre beaucoup de temps. Au niveau national du moins, des activités comme l’élaboration d’un projet ou l’organisation d’un groupe ou d’une réunion sont celles qui ont tendance à prendre le plus de temps, suivies par l’entretien des lieux publics et la production ou la diffusion d’information aux fins de sensibilisation. Fait intéressant, bien que les réunions publiques jouent traditionnellement un rôle central dans la sensibilisation et l’amélioration communautaires, elles prennent relativement peu de temps. Cela s’explique peut-être par l’essor des communications en ligne et des médias sociaux.
                        """),
                        # Forms of community improvement
                        html.Div([
                            dcc.Graph(id='VolRateAvgHrs-Community', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Linkages between forms of support
                    #html.Div([
                        #html.H4("Linkages between forms of support",className='mt-3'),
                        #html.P("""
                        #Formal and informal forms of volunteering do appear to be related, in the sense that those who volunteer in any given way are more likely to volunteer in each of the other ways. For instance, at the national level, those who help others directly are nearly twice as likely to volunteer for an organization (48% vs. 26%) and over three times as likely to contribute time to improving their community (35% vs. 11%). Similarly, those who improve their communities are almost twice as likely to volunteer for an organization (63% vs. 33%) and about forty percent more likely to help others directly (81% vs. 62%). Finally, those who volunteer for an organization are about half again as likely likely to engage in community improvement activities (43% vs. 28%) and about a third more likely to help others without going through an organization (81% vs. 62%). The net effect is that most people volunteer in some way, with just over a third (35%) engaging in one type of volunteer activity, 28% in two, and 16% in three. Only about a fifth of Canadians (21%) do not engage in some form of formal or informal volunteering.
                        #"""),
                        # Linkages between forms of support
                        #html.Div([
                        #    dcc.Graph(id='SupportLinkages', style={'marginTop': marginTop})
                        #]),
                    #]),
                    # Who helps others and improves the community?
                    html.Div([
                        html.H4("Qui aide autrui et améliore la collectivité?",className='mt-3'),
                        html.P("""
                        La probabilité d’aider autrui et d’améliorer la collectivité a tendance à varier selon les caractéristiques personnelles et économiques d’une manière très semblable à la probabilité de pratiquer le bénévolat encadré. D’une façon très générale, au niveau national, la probabilité d’aider et d’améliorer la collectivité diminue avec l’âge, mais augmente avec le niveau d’éducation formelle et l’assiduité aux offices religieux. En raison de la diminution liée à l’âge, les personnes veuves ou qui ne sont pas membres de la population active ont également tendance à moins offrir ces formes de soutien. La fréquence de l’aide d’autrui augmente directement avec le revenu du ménage et est plus répandue parmi les personnes nées au Canada, tandis que la probabilité de contribuer à l’amélioration de la collectivité ne varie pas de manière significative selon ces caractéristiques.
                        """),
                        # Likelihood of providing support by key personal and economic characteristics
                        html.Div([
                            html.Div(["Catégorie démographique:",
                                dcc.Dropdown(
                                    id='demo-selection',
                                    options=[{'label': name, 'value': name} for name in demo_names],
                                    value="Groupe d'âge",
                                    # value='Age group',
                                    style={'verticalAlgin': 'middle'}
                                ),
                                ],
                                className='bg-light m-2 p-2'),
                            dcc.Graph(id='VolRates-All', style={'marginTop': marginTop})
                        ]),
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'

            ),
        ]),
   ),
   footer
])

################## Callbacks #################

# @app.callback(
#     dash.dependencies.Output('FormsVolunteering', 'figure'),
#     [

#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):

#     dff1 = FormsVolunteering_2018[FormsVolunteering_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == "All"]

#     title = '{}, {}'.format("Forms of giving", region)

#     return forms_of_giving(dff1, title)

@app.callback(
    dash.dependencies.Output('VolRateAvgHrs-Helping', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = HelpDirectRate_2018[HelpDirectRate_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "All"]
    dff1 = dff1.replace("Helping others rate", "Taux d'aide aux autres")
    name1 = "Taux d'aide aux autres"
    # name1 = "Helping others rate"

    dff2 = HelpDirectHrs_2018[HelpDirectHrs_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "All"]
    dff2 = dff2.replace('Average hours', "Nbre d'h moyen")
    name2 = "Nbre d'h moyen"

    title = '{}, {}'.format("Formes d’aide", region)

    return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)

@app.callback(
    dash.dependencies.Output('VolRateAvgHrs-Community', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = CommInvolveRate_2018[CommInvolveRate_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "All"]
    dff1 = dff1.replace('Community improvement rate', "")
    name1 = "Community improvement rate"

    dff2 = CommInvolveHrs_2018[CommInvolveHrs_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "All"]
    dff2 = dff2.replace('Average hours', "Nbre d'h moyen")
    name2 = "Nbre d'h moyen"
    # name2 = "Average hours"

    title = '{}, {}'.format("Formes d’amélioration communautaire", region)

    return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)

@app.callback(
    dash.dependencies.Output('VolRates-All', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('demo-selection', 'value')
    ])

def update_graph(region, demo):
    dff1 = VolRate_2018[VolRate_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == demo]
    # name1 = "Volunteering"
    name1 = 'Volontariat'

    dff2 = FormsVolunteering_2018[FormsVolunteering_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == demo]
    dff2 = dff2[dff2['QuestionText'] == 'Help people<br>directly']
    name2 = "Aider les autres"

    dff3 = FormsVolunteering_2018[FormsVolunteering_2018['Region'] == region]
    dff3 = dff3[dff3['Group'] == demo]
    dff3 = dff3[dff3['QuestionText'] == 'Improve<br>community']
    name3 = "Participation de la communauté"


    title = '{}, {}'.format("Probabilité de soutenir selon les caractéristiques personnelles et économiques clés", region)

    return triple_vertical_graphs_rates(dff1, dff2, dff3, title, name1, name2, name3, type="percent")

# def update_graph(region, demo):
#     dff1 = VolRate_2018[VolRate_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == demo]
#     dff1 = dff1.replace('Volunteering', 'Volontariat')
#     name1 = "Volontariat"

#     dff2 = FormsVolunteering_2018[FormsVolunteering_2018['Region'] == region]
#     dff2 = dff2[dff2['Group'] == demo]
#     dff2 = dff2[dff2['QuestionText'] == 'Aider les gens directement']
#     dff2 = dff2.replace("Helping others", "Aider les autres")
#     # name2 = "Helping others"
#     name2 = "Aider les autres"

#     dff3 = FormsVolunteering_2018[FormsVolunteering_2018['Region'] == region]
#     dff3 = dff3[dff3['Group'] == demo]
#     dff3 = dff3[dff3['QuestionText'] == 'Améliorer la communauté']
#     dff3 = dff3.replace("Community involvement", "Participation de la communauté")
#     # name3 = "Community involvement"
#     name3 = "Participation de la communauté"

#     title = '{}, {}'.format("Probabilité de soutenir selon les caractéristiques personnelles et économiques clés", region)

#     return triple_vertical_graphs_rates(dff1, dff2, dff3, title, name1, name2, name3, type="percent")
