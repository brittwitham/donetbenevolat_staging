from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app
from ..layout_utils import gen_home_button, gen_navbar, footer
from .callbacks import register_callbacks
from .data_processing import region_values, list_factors

register_callbacks(app)

marginTop = 20
home_button = gen_home_button(bc_link="https://donetbenevolat.ca/apercu-des-donnees-sur-la-situation-des-entreprises")
navbar = gen_navbar("impact_of_interest_rates_2023")

layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1("Histoire relative à l’incidence des taux d’intérêt"),
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
                    html.H2('Incidence des taux d’intérêt'),
                    html.Span([
                        '''Au quatrième trimestre de 2023, l’''',
                        html.Span('Enquête canadienne sur la situation des entreprises', style={'font-style': 'italic'}),
                        ''' a demandé aux organismes'''
                    ]),
                    html.Sup(html.A('1', href='#footnote1', id="ref1")),
                    html.Span(''' de préciser l’incidence des taux d’intérêt sur eux, car ils sont à leur niveau le plus élevé depuis plus de dix ans. Parallèlement, les organismes doivent composer avec un taux d’inflation supérieur à la normale, même si celui-ci a considérablement baissé après avoir atteint un sommet au milieu de 2022.
                    ''', className='mt-4'),
                    dcc.Markdown('''
                    Les organismes devaient indiquer s’ils s’attendaient à ce que les taux d’intérêt et l’inflation constituent des obstacles pour eux au cours des trois prochains mois. Même si l’inflation était à la baisse, elle préoccupait beaucoup plus les organismes à but non lucratif que les taux d’intérêt. En ce qui a trait aux différences entre les types d’organismes, les organismes communautaires à but non lucratif étaient plus susceptibles que les institutions commerciales à but non lucratif – mais moins susceptibles que les entreprises à but lucratif – d’anticiper des défis liés à ces facteurs.
                    ''', className='mt-4'),
                    dcc.Graph(
                        id="org3MonthObstaclesImpact", style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
        [
            html.Span('''
            Dans une question de suivi, les répondants devaient indiquer les obstacles qui allaient constituer leurs plus grands défis. Les réponses reflétaient à nouveau les préoccupations liées à l’inflation. Les organismes à but non lucratif étaient considérablement moins susceptibles que les entreprises d’indiquer que les taux d’intérêt représentaient leur plus grand défi.
            ''', className='mt-4'),
            dcc.Graph(id="orgGreatestObstacleImpact", style={
                            'marginTop': marginTop}),
        ], className='col-md-10 col-lg-8 mx-auto'
    ),
    html.Div(
        [
            html.Span('''
            Bien que les taux d’intérêt soient devenus un plus grand obstacle pour les entreprises à but lucratif au fil des ans, il n’est pas dit qu’il en est de même pour les organismes à but non lucratif. Même si les organismes communautaires à but non lucratif sont devenus quelque peu plus susceptibles d’anticiper des défis liés aux taux d’intérêt depuis le troisième trimestre de 2023, les résultats des institutions commerciales à but non lucratif varient beaucoup plus. Les préoccupations des organismes à but non lucratif relatives à l’inflation semblent moins prononcées qu’au quatrième trimestre de 2022, alors que celles des entreprises à but lucratif sont demeurées plus ou moins stables.
            ''', className='mt-4'),
            html.Sup(html.A('2', href='#footnote2', id="ref2")),
        ], className='col-md-10 col-lg-8 mx-auto'
    ),
    html.Br(),
    html.Div(
        [
        dcc.Dropdown(
                      id='item2-selection',
                      options=[{'label': list_factors[i], 'value': list_factors[i]}
                               for i in range(len(list_factors))],
                      value='Inflation',
                      style={'verticalAlign': 'middle'}
                  ),
        dcc.Graph(id="orgExpectedObstaclesChange",
                  style={'marginTop': marginTop,
                         "height": "90vh"})
        ], className='col-md-10 col-lg-8 mx-auto'
    ),
    html.Div(
        [
            html.Span('''
            Au quatrième trimestre de 2023, les organismes devaient préciser l’incidence des taux d’intérêt sur eux. De façon générale, les organismes à but non lucratif étaient d’avis que les taux d’intérêt avaient moins d’incidence sur eux que sur les entreprises à but lucratif.
            ''', className='mt-4'),
            html.Sup(html.A('3', href='#footnote3', id="ref3")),
            dcc.Graph(id="impactLevelInterestRates", style={
                            'marginTop': marginTop}),
        ], className='col-md-10 col-lg-8 mx-auto'
    ),
    html.Div(
        [
            html.Span('''
            Les organismes qui ont indiqué que les taux d’intérêt avaient une incidence sur eux devaient ensuite préciser comment ils étaient touchés. Les organismes à but non lucratif étaient les plus susceptibles de signaler que les investissements, les dépenses en capital et les coûts associés à leur dette existante avaient été touchés par les taux d’intérêt.
            ''', className='mt-4'),
            dcc.Markdown('''
            Comparativement aux entreprises à but lucratif, les organismes à but non lucratif étaient plus susceptibles de mentionner l’incidence des taux d’intérêt sur leurs investissements et moins susceptibles de signaler leur incidence sur leur dette existante. Quant aux organismes communautaires à but non lucratif, ils étaient plus susceptibles de déclarer que leurs dépenses en capital avaient été touchées par les taux d’intérêt.
            ''', className='mt-4'),
            dcc.Graph(id="greatestImpactInterestRates", style={
                            'marginTop': marginTop,
                "height": "90vh"}),
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
                                        "En raison du nombre limité de l’échantillonnage, il est difficile de tirer des conclusions fermes relatives aux institutions gouvernementales. Les résultats présentés doivent donc être utilisés avec prudence.",
                                        html.A(
                                            "↩︎",
                                            href="#ref2",
                                            className="footnote-back",
                                            role="doc-backlink")
                                    ]
                                )
                            ], id="footnote2"),
                            html.Li(
                            [
                                html.P(
                                    [
                                        "Même si les institutions gouvernementales étaient plus susceptibles de déclarer que les taux d’intérêt avaient une forte incidence sur elles, elles étaient moins certaines de leur impact, ce qui complique les comparaisons avec les organismes à but non lucratif.",
                                        html.A(
                                            "↩︎",
                                            href="#ref3",
                                            className="footnote-back",
                                            role="doc-backlink")
                                    ]
                                )
                            ], id="footnote3"),
                    ])
                ],
            )
        ])
    ),
])

