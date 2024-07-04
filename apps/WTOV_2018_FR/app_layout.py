# App layout file for WTOV_2018_FR converted from
# A_quels_types_organismes_fait_on_don_de_son_temps_au_Canada_2018.py

from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app
from ..layout_utils import gen_home_button, gen_navbar, footer
from .callbacks import register_callbacks
from .data_processing import *

register_callbacks(app)
marginTop = 20
navbar = gen_navbar(
    "What_types_of_organizations_do_Canadians_volunteer_for_2018")

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
                        html.H1(
                            'À quels types d’organismes fait-on don de son temps au Canada?'),
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
                        options=[{'label': region_names[i], 'value': region_names[i]}
                                 for i in range(len(region_names))],
                        value='CA',
                    ),
                    html.Br(),
                ], className="m-2 p-2"),
            ), id='sticky-dropdown'),
    ], className='sticky-top select-region mb-2', fluid=True),
    dbc.Container(
        dbc.Row([
            html.Div(
                [
                    dcc.Markdown('''
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, un peu plus de deux cinquièmes des personnes (41 %) au Canada ont fait du bénévolat pour un organisme de bienfaisance ou à but non lucratif pendant l’année qui l’a précédée, en leur faisant don de 131 heures en moyenne par personne. En moyenne, les bénévoles ont fait don de leur temps à 1,4 cause. La majorité des bénévoles (62 %) ont fait don de leur temps à une seule cause, un peu plus d’un quart d’entre eux (28 %) à deux causes et les autres (10 %) à trois causes.
                    ''', className='mt-4'),
                    dcc.Markdown('''
                    Nous décrivons ci-dessous les tendances de leur soutien au niveau national et, pour obtenir des précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer des résultats au niveau national décrits dans le texte, les tendances générales sont très similaires dans l’ensemble.
                    '''),
                    dcc.Markdown('''
                    Les personnes au Canada sont les plus enclines à faire du bénévolat pour les organismes du secteur des services sociaux et de celui du sport et des loisirs, ainsi que pour les congrégations religieuses. S’agissant du nombre d’heures de bénévolat habituel, les bénévoles qui font don de leur temps à ces trois causes ont tendance à se rapprocher de ceux qui s’engagent le plus. En effet, ces causes se situent parmi les cinq causes au bénéfice desquelles le nombre moyen d’heures de bénévolat est le plus élevé (au niveau national). En revanche, les bénévoles des trois causes les plus soutenues suivantes (éducation et recherche, aménagement et logement, et santé) ont tendance à faire don de relativement moins d’heures, ces causes faisant partie des quatre dernières du point de vue des heures de bénévolat qui leur sont consacrées, malgré leurs bases de soutien relativement larges. Les bases de soutien des huit causes restantes sont un peu plus étroites, en s’échelonnant de 30 à une personne sur 100 au Canada, selon le cas. Dans l’ensemble, les bénévoles au service de ces causes ont tendance à se rapprocher davantage du milieu de la fourchette des heures de bénévolat. Les hôpitaux et les organismes d’octroi de subventions et de collecte de fonds sont les seuls à se distinguer dans le classement selon leur nombre moyen d’heures de bénévolat particulièrement élevé ou bas, du moins au niveau national.
                    '''),
                    # Levels of support by cause
                    dcc.Graph(
                        id='DonRateAvgDonAmt-Cause-2',
                        style={
                            'marginTop': marginTop}),
                    html.Br(),
                    dcc.Markdown('''
                    Au total, les personnes au Canada font don d’un peu moins d’1,7 milliard d’heures de bénévolat par année aux organismes de bienfaisance et à but non lucratif, ce qui équivaut à environ 863 000 emplois à plein temps. La plus grande partie de ce soutien, et de loin, est offerte aux organismes du secteur des services sociaux et à celui du sport et des loisirs, ainsi qu’aux organismes religieux qui reçoivent collectivement plus de la moitié du total des heures de bénévolat. Les cinq causes suivantes (éducation et recherche, aménagement et logement, arts et culture, santé et environnement) reçoivent chacune au moins une heure de bénévolat sur vingt. À l’échelle nationale, ces causes représentent collectivement plus du quart des heures de bénévolat. Les sept causes restantes représentent à elles toutes environ 16 % du total des heures, le niveau de leur soutien s’échelonnant de quatre pour cent du total des heures, pour les hôpitaux, à un pour cent du total des heures pour les organismes du développement international et de l’aide internationale.
                    '''),
                    # Allocation of support by cause
                    dcc.Graph(id='AllocationSupport-Cause-2',
                              style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
    ),
    footer
])
