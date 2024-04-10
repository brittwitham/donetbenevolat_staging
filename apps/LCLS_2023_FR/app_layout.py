from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app
from ..layout_utils import gen_home_button, gen_navbar, footer
from .callbacks import register_callbacks
from .data_processing import region_values, list_factors

register_callbacks(app)

marginTop = 20
home_button = gen_home_button(bc_link="https://donetbenevolat.ca/apercu-des-donnees-sur-la-situation-des-entreprises")
navbar = gen_navbar("liquidity_and_ceba_loans_2023")

layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1("Histoire relative à la liquidité et aux prêts du CUEC"),
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
                    html.H2('Accès à la liquidité et aux prêts du CUEC'),
                    html.Span([
                        '''Chaque trimestre, l’''',
                        html.Span('Enquête canadienne sur la situation des entreprises', style={'font-style': 'italic'}),
                        ''' demande aux organismes'''
                    ]),
                    html.Sup(html.A('1', href='#footnote1', id="ref1")),
                    html.Span(''' dans quelle mesure ils peuvent accéder aux sommes dont ils ont besoin pour poursuivre leurs opérations pendant les trois prochains mois. Le sondage le plus récent a révélé que les organismes sans but lucratif et les organismes gouvernementaux sont plus susceptibles que les entreprises de savoir qu’ils peuvent accéder à la liquidité dont ils ont besoin, alors que les entreprises sont plus susceptibles d’éprouver de l’incertitude face aux sommes dont elles ont besoin.
                    ''', className='mt-4'),
                    dcc.Graph(
                        id="accessLiquidity", style={
                            'marginTop': marginTop,
                            'height': "90vh"}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    dcc.Markdown(
                        '''
                        L’accès prévu à la liquidité est resté remarquablement constant au cours des deux dernières années. Le seul changement d’importance a été constaté au niveau des institutions gouvernementales, qui sont de plus en plus certaines d’avoir accès à la liquidité dont elles ont besoin, surtout en raison d’une diminution de l’incertitude.
                        '''
                        , className='mt-4'),
                    dcc.Dropdown(
                      id='item2-selection',
                      options=[{'label': list_factors[i], 'value': list_factors[i]}
                               for i in range(len(list_factors))],
                      value=list_factors[0],
                      style={'verticalAlign': 'middle'}
                  ),
                    dcc.Graph(
                        id="accessLiquidityChange", style={
                            'marginTop': marginTop,
                            'height': "115vh"}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H3('Statut des prêts du CUEC'),
                    html.Span(
                        '''Au cours du quatrième trimestre de 2023, les organismes ont été interrogés sur le statut de tout prêt reçu du Compte d’urgence pour les entreprises canadiennes (CUEC). En général, les organismes à but non lucratif et les institutions gouvernementales avaient la moitié moins de chances que les entreprises de recevoir un prêt du CUEC. Parmi les organismes à but non lucratif, les institutions commerciales à but non lucratif étaient légèrement plus susceptibles que les organismes communautaires à but non lucratif de recevoir un prêt.'''
                        , className='mt-4'),
                    dcc.Graph(
                        id="receiveCEBA", style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.Span(
                        '''
                        Les organismes qui ont indiqué avoir reçu un prêt du CUEC ont été interrogés sur le statut du remboursement de leur prêt. Même si les organismes à but non lucratif étaient moins susceptibles que les entreprises de recevoir un prêt, ils étaient légèrement plus susceptibles de l’avoir remboursé.'''
                        ,  className='mt-4'),
                        html.Sup(html.A('2', href='#footnote2', id="ref2")
                        ),
                    dcc.Graph(
                        id="statusCEBA", style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.Span(
                        '''
                        Le sondage demandait ensuite aux organismes qui n’avaient pas encore remboursé leur prêt s’ils prévoyaient être en mesure de le faire d’ici la fin de 2026. Les organismes à but non lucratif étaient considérablement plus susceptibles que les entreprises à croire qu’ils pourraient rembourser leur prêt d’ici l’échéance.'''
                        ,  className='mt-4'),
                    dcc.Graph(
                        id="willPayCEBA", style={
                            'marginTop': marginTop}),
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
                                "Les organismes se divisent en quatre catégories : ",
                                html.Em("organismes communautaires à but non lucratif"),
                                ", qui desservent les ménages ou les particuliers (p. ex., banques alimentaires, refuges, congrégations religieuses, et groupes de sports et loisirs); ",
                                html.Em("institutions commerciales à but non lucratif"),
                                ", qui desservent les entreprises (p. ex., associations commerciales, chambres de commerce et associations de copropriétaires); ",
                                html.Em("institutions gouvernementales à but non lucratif"),
                                "; et ",
                                html.Em("entreprises"),
                                " à but lucratif.",
                                html.A(
                                    "↩︎",
                                    href="#ref1",
                                    className="footnote-back",
                                    role="doc-backlink")
                            ], id="fn1")
                        ], id="footnote1"),
                        html.Li(
                            [
                                html.P(
                                    [
                                        "En raison de la taille réduite de l’échantillon, les données relatives aux institutions gouvernementales n’ont pu être publiées.",
                                        html.A(
                                            "↩︎",
                                            href="#ref2",
                                            className="footnote-back",
                                            role="doc-backlink")
                                    ]
                                )
                            ], id="footnote2"),
                    ])
                ],
            )
        ])
    ),
])
