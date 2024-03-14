from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app
from ..layout_utils import gen_home_button, gen_navbar, footer
from .callbacks import register_callbacks
from .data_processing import region_values, list_factors

register_callbacks(app)

marginTop = 20
home_button = gen_home_button(bc_link="https://donetbenevolat.ca/apercu-des-donnees-sur-la-situation-des-entreprises")
navbar = gen_navbar("current_obstacles_2023")

layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1("Histoire relative aux obstacles actuels"),
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
                    html.H2('Obstacles actuels'),
                    html.Span([
                        '''Chaque trimestre, l’''',
                        html.Span('Enquête canadienne sur la situation des entreprises', style={'font-style': 'italic'}),
                        ''' demande aux organismes '''
                    ]),
                    html.Sup(html.A('1', href='#footnote1', id="ref1")),
                    html.Span(''' de décrire les obstacles qu’ils prévoient d’affronter au cours du prochain trimestre. Le dernier sondage a révélé que les préoccupations relatives à l’inflation, aux ressources humaines et aux coûts prédominaient. De façon générale, les réponses des organismes à but non lucratif étaient plutôt semblables à celles des entreprises en ce qui avait trait aux obstacles les plus courants. Ils étaient toutefois moins nombreux à signaler certains obstacles moins courants, tels que la demande, l’augmentation de la concurrence et l’acquisition d’intrants. De plus, ils étaient moins susceptibles de déclarer éprouver des difficultés avec les taux d’intérêt. Les institutions gouvernementales semblaient notamment devoir relever des défis particuliers liés au recrutement et à la conservation du personnel rémunéré.
                    ''', className='mt-4'),
                    dcc.Graph(id="org3MonthObstacles", style={
                            'marginTop': marginTop,
                            'height': '150vh'}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.Span('''Après avoir décrit les différents obstacles auxquels ils prévoyaient de faire face au cours des trois prochains mois, les organismes devaient indiquer lequel poserait le plus grand défi. Dans l’ensemble, les résultats étaient très semblables à ceux de la version plus générale de la question. Dans le cas des organismes à but non lucratif, la seule grande différence résidait dans la difficulté à attirer des clients. En effet, bien que relativement peu d’organismes aient indiqué devoir affronter ce problème, il demeure important pour ceux qui doivent relever ce défi.
                    ''', className='mt-4'),
                    dcc.Graph(id="orgGreatestObstacle", style={
                            'marginTop': marginTop,
                            'height': "150vh"}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.Span('''De façon générale, les obstacles que doivent affronter les organismes sont demeurés relativement constants. Au degré où une tendance claire est ressortie, plusieurs obstacles semblent être devenus prévalents au cours de 2021, mais nombre d’entre eux sont demeurés plutôt constants depuis.
                    ''', className='mt-4'),
                    html.Br(),
                    html.Br(),
                    dcc.Dropdown(
                      id='expectedObstaclesChange_filter',
                      options=[{'label': list_factors[i], 'value': list_factors[i]}
                               for i in range(len(list_factors))],
                      value="Recrutement d'employés qualifiés",
                      style={'verticalAlign': 'middle'}
                  ),
                    dcc.Graph(id="expectedObstaclesChange", style={
                            'marginTop': marginTop,
                    'height': "115vh"}),
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
                    ])
                ],
            ),
        ])
    ),
])
