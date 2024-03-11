from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app
from ..layout_utils import gen_home_button, gen_navbar, footer
from .callbacks import register_callbacks
from .data_processing import region_values, list_factors, bus_char

register_callbacks(app)


marginTop = 20
home_button = gen_home_button()
navbar = gen_navbar("future_outlook_and_predicted_changes_2023")

layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1("Histoire relative aux perspectives d’avenir et aux changements prévus"),
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
                    html.H2('Perspectives d’avenir et changements prévus'),
                    html.Span([
                        '''Chaque trimestre, l’''',
                        html.Span('Enquête canadienne sur la situation des entreprises', style={'font-style': 'italic'}),
                        ''' demande aux organismes '''
                    ]),
                    html.Sup(html.A('1', href='#footnote1', id="ref1")),
                    html.Span(''' de préciser leurs attentes relatives à la prochaine année d’existence de leur organisme, ainsi que tous les changements prévus pour le prochain trimestre.
                    ''', className='mt-4'),
                    html.Br(),
                    html.Br(),
                    html.H3('Perspectives d’avenir'),
                    html.Span(
                        '''
                       Au cours du dernier sondage réalisé au quatrième trimestre de 2023, les organismes communautaires à but non lucratif et les institutions gouvernementales étaient plutôt optimistes. Même si la plupart des institutions commerciales à but non lucratif et des entreprises se disaient également optimistes pour l’année à venir, environ un cinquième de ces organismes était pessimiste face à l’avenir.
                        '''
                    , className='mt-4'),
                    dcc.Graph(id="FutureOutlook", style={
                            'marginTop': marginTop}),
                    html.Span(
                        '''
                        Au cours des deux dernières années, le degré d’optimisme des organismes à but non lucratif est demeuré supérieur à celui des entreprises, dont l’optimisme est de moins en moins évident.'''
                    ),
                    html.Sup(html.A('2', href='#footnote2', id="ref2")),
                    html.Span(
                        ''' Dernièrement, l’optimisme des institutions commerciales à but non lucratif a fortement chuté, probablement en raison de préoccupations relatives au climat économique. Quant au degré d’optimisme des institutions gouvernementales, il était quelque peu plus variable que celui des autres types d’organismes, probablement en raison du nombre limité d’organismes de ce type qui a répondu au sondage.
                        '''
                    ),
                    html.Br(),
                    html.Br(),
                    dcc.Dropdown(
                      id='busChar-selection',
                      options=[{'label': bus_char[i], 'value': bus_char[i]}
                               for i in range(len(bus_char))],
                      value='Organismes communautaires à but non lucratif',
                      style={'verticalAlign': 'middle'}
                  ),
                    dcc.Graph(id="futureOutlookByQuarter", style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H3('Changements prévus'),
                    html.Span(
                        '''
                        Les organismes devaient décrire à quel point ils prévoyaient que 15 facteurs donnés allaient changer au cours des trois prochains mois (excluant les variations saisonnières). En général, un nombre plus élevé d’organismes à but non lucratif et d’institutions gouvernementales prévoyaient une augmentation de leurs dépenses d’exploitation et de la demande pour leurs services plutôt qu’une augmentation de leur revenu opérationnel et du nombre d’employés embauchés. Les entreprises étaient légèrement plus susceptibles que les autres organismes de prévoir une diminution de la demande et de leur revenu opérationnel, ce qui pourrait expliquer leur plus grand pessimisme face à l’avenir.
                        '''
                    ),
                    html.Br(),
                    html.Br(),
                    dcc.Dropdown(
                      id='item2-selection',
                      options=[{'label': list_factors[i], 'value': list_factors[i]}
                               for i in range(len(list_factors))],
                      value='Réserves de trésorerie',
                      style={'verticalAlign': 'middle'}
                  ),
                    dcc.Graph(id="org3MonthExpectations_facet", style={
                        'marginTop': marginTop,
                        'height': '120vh'})
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.Span(
                        '''
                        Au cours des deux dernières années, les organismes se sont montrés remarquablement constants dans leurs prévisions. La seule tendance à se manifester clairement au cours de cette période était une légère diminution du pourcentage d’organismes qui prédisaient une augmentation du nombre de postes à combler.
                        '''
                    ),
                    dcc.Graph(id="org3MonthExpectations",
                            style={'marginTop': marginTop,
                                   'height': '150vh'})
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H2(
                        "Footnotes",
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
                                        'Les données des organismes qui ont répondu « Ne sais pas » sont exclues des données présentées.',
                                        html.A(
                                            "↩︎",
                                            href="#ref2",
                                            className="footnote-back",
                                            role="doc-backlink")
                                    ]
                                )
                            ], id="footnote2"),
                    ])
                ]
            )
        ])
    )
])





