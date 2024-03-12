from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app
from ..layout_utils import gen_home_button, gen_navbar, footer
from .callbacks import register_callbacks
from .data_processing import region_values, bus_groups, text_items_1, text_items_2

register_callbacks(app)

marginTop = 20
home_button = gen_home_button()
navbar = gen_navbar("donation_trends_2023")

layout = html.Div([
    navbar,
        html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1("Histoire relative aux tendances en matière de don"),
                    ],
                        className='post-heading'
                    ),
                    className='col-md-10 col-lg-8 mx-auto position-relative'
                )
            )
        ),
        ],
        className="sub-header bg-secondary text-white text-center py-5",
    ),
    dbc.Container([
        home_button,
        dbc.Row(
            dbc.Col(
                html.Div([
                    "Sélectionnez une région :",
                    dcc.Dropdown(
                      id='geo-selection',
                      options=[{'label': region_values[i], 'value': region_values[i]}
                               for i in range(len(region_values))],
                      value='CA',
                      style={'verticalAlign': 'middle'}
                  ),
                  html.Br(),
                ], className="m-2 p-2"),
            ), id="sticky-dropdown"),
    ], className='sticky-top select-region mb-2', fluid=True),
    dbc.Container(
        dbc.Row([
            html.Div(
                [
                    html.Br(),
                    html.H2('Tendances en matière de don'),
                    html.Span([
                        '''Au quatrième trimestre de 2023, l’''',
                        html.Span('Enquête canadienne sur la situation des entreprises', style={'font-style': 'italic'}),
                        ''' a demandé aux organismes à but non lucratif '''
                    ]),
                    html.Sup(html.A('1', href='#footnote1', id="ref1")),
                    html.Span('''
                     de décrire les défis qu’ils devaient relever en ce qui a trait aux dons du public. Les organismes qui reçoivent généralement des dons du public (64 % des organismes communautaires à but non lucratif et 13 % des institutions commerciales à but non lucratif) devaient préciser s’ils étaient confrontés à des défis liés aux dons et aux donateurs. Les organismes étaient plus susceptibles de mentionner la recherche de nouveaux donateurs, le déclin des sommes versées par les donateurs, la difficulté à conserver les donateurs, et le manque de temps ou de ressources pour la collecte de fonds. Seuls 14 % des organismes communautaires à but non lucratif et 11 % des institutions commerciales à but non lucratif ont déclaré ne pas avoir de défis liés aux dons.
                    ''', className='mt-4'),
                    dcc.Graph(
                        id="donationChallenges", style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.Span('''
                    Certains types d’organismes étaient plus susceptibles que d’autres de déclarer avoir des défis liés aux dons. Les organismes comptant 100 employés ou plus étaient plus susceptibles de déclarer qu’ils faisaient face à de tels défis, tout comme les organismes situés dans les centres urbains. Quant aux organismes plus âgés, ils étaient moins susceptibles de signaler avoir de la difficulté à trouver de nouveaux donateurs, probablement en raison de leurs réseaux établis. Ils étaient toutefois plus susceptibles de constater que les sommes versées étaient moins élevées qu’avant.
                    ''', className='mt-4'),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            dcc.Dropdown(
                                id='donationChallengesDetailed_filter_1',
                                options=[{'label': bus_groups[i], 'value': bus_groups[i]}
                                        for i in range(len(bus_groups))],
                                value='Emploi',
                                style={'verticalAlign': 'middle'})]),
                        dbc.Col([
                            dcc.Dropdown(
                                id='donationChallengesDetailed_filter_2',
                                  options=[{'label': text_items_1[i], 'value': text_items_1[i]}
                                        for i in range(len(text_items_1))],
                                value='Recherche de nouveaux donateurs',
                                style={'verticalAlign': 'middle'})]),
                            ]),
                    dcc.Graph(id="donationChallengesDetailed", style={
                        'marginTop': marginTop})
                        ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.Span('''
                    Les organismes qui ont déclaré éprouver des difficultés avec les dons ont été interrogés sur les impacts vécus ou prévus. Dans le cas des organismes communautaires à but non lucratif, un tiers ou plus des organismes a vécu les répercussions suivantes : dépendance accrue aux bénévoles; besoin de trouver de nouvelles sources de revenus; réduction des dépenses non liées au personnel; et diminution du nombre de programmes offerts. Les organismes étaient moins susceptibles de réduire le nombre d’employés rémunérés ou les niveaux de service, ou encore d’annuler des programmes, mais ces solutions constituaient des possibilités voire des réalités pour une minorité appréciable d’organismes. Un peu plus d’un organisme sur vingt a déclaré courir un risque de fermeture.
                    '''),
                    html.Br(),
                    html.Br(),
                    html.Span('''
                    Les institutions commerciales à but non lucratif devaient relever des défis similaires, même s’ils étaient légèrement moins susceptibles de déclarer dépendre de bénévoles, de devoir réduire les dépenses non liées au personnel, d’avoir recours à des réductions de personnel ou de courir un risque de fermeture. Un peu plus du quart des institutions commerciales à but non lucratif n’ont signalé aucun impact lié aux dons contre un peu plus du sixième des organismes communautaires à but non lucratif.
                    ''', className='mt-4'),
                    dcc.Graph(id="donationImpact", style={
                            'marginTop': marginTop})
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.Span('''
                    Les organismes de plus grande taille étaient plus susceptibles de déclarer avoir eu à prendre la plupart des mesures d’intervention mentionnées ci-dessus, sauf la dépendance accrue aux bénévoles et le risque accru de fermeture. Même si les plus petits organismes étaient les plus susceptibles de déclarer ne pas devoir relever de défis liés aux dons, ils étaient considérablement plus susceptibles de courir un risque de fermeture, ce qui laisse supposer qu’ils avaient moins d’occasions de s’adapter. Quant aux organismes des centres urbains, ils étaient considérablement plus susceptibles d’avoir vécu ou contemplé des réductions de personnel ou de programmes, tout comme les organismes plus établis. Enfin, les organismes de deux ans ou moins couraient moins de risque de fermeture, alors que ceux qui existaient depuis 3 à 10 ans étaient plus susceptibles d’être incapables d’accepter de nouveaux clients.
                    ''', className='mt-4'),
                    html.Br(),
                    html.Br(),
                    dbc.Row([
                        dbc.Col([
                            dcc.Dropdown(
                                id='donationImpactDetailed_filter_1',
                                options=[{'label': bus_groups[i], 'value': bus_groups[i]}
                                         for i in range(len(bus_groups))],
                                value='Emploi',
                                style={'verticalAlign': 'middle'})
                                ]),
                        dbc.Col([
                            dcc.Dropdown(
                                id='donationImpactDetailed_filter_2',
                                options=[{'label': text_items_2[i], 'value': text_items_2[i]}
                                         for i in range(len(text_items_2))],
                                value='Dépendance accrue aux bénévoles',
                                style={'verticalAlign': 'middle'})
                                ]),
                    ]),
                  dcc.Graph(id="donationImpactDetailed", style={
                            'marginTop': marginTop})
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H2(
                        "Note de bas de page",
                        className="anchored quarto-appendix-heading"),
                        html.Ol([
                        html.Li([
                            html.P([
                                "Les organismes à but non lucratif se divisent en deux catégories : ",
                                html.Em("organismes communautaires à but non lucratif"),
                                ", qui desservent les ménages ou les particuliers (p. ex., banques alimentaires, refuges, congrégations religieuses, et groupes de sports et loisirs); et ",
                                html.Em("institutions commerciales à but non lucratif"),
                                ", qui desservent les entreprises (p. ex., associations commerciales, chambres de commerce et associations de copropriétaires). Les ",
                                html.Em("institutions gouvernementales à but non lucratif"),
                                " et les ",
                                html.Em("entreprises"),
                                " à but lucratif n’ont pas été interrogées à propos de leurs dons.",
                                html.A(
                                    "↩︎",
                                    href="#ref1",
                                    className="footnote-back",
                                    role="doc-backlink")
                            ], id="fn1")
                        ], id="footnote1")
                    ])
                ]
            )
        ])
    )
])
