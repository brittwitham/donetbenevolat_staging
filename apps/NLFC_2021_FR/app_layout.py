# App layout file for WVHT_2018_EN converted from
# Who_volunteers_and_how_much_time_do_they_contribute_2018.py

from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app
from ..layout_utils import gen_home_button, gen_navbar, footer
from .callbacks import register_callbacks
# from .data_processing import region_values, status_names, VolRate_2018, AvgTotHours_2018
# from .graphs import static_graph

register_callbacks(app)

provOrder = [
    "CA",
    "BC",
    "AB",
    "SK",
    "MB",
    "ON",
    "QC",
    "NB",
    "NS",
    "PE",
    "NL",
    "YT",
    "NT",
    "NU"]
demos = [
    'Genre',
    'Immigration',
    'Autochtones',
    'Minorités visibles',
    'Éducation formelle',
    "Groupe d'âge"]


# TODO!
navbar = gen_navbar(
    "nonprofit_labour_force_composition_2021")

marginTop = 20
home_button = gen_home_button(sat_link=True)

layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1(
                            'Composition de la population active du secteur sans but lucratif'),
                    ],
                        className='post-heading'
                    ),
                    className='col-md-10 col-lg-8 mx-auto position-relative'
                )
            )
        ),
    ],
        # className='masthead'
        className="sub-header bg-secondary text-white text-center py-5",
    ),
    dbc.Container([
        home_button,
        dbc.Row(
            dbc.Col(
                html.Div([
                    "Sélectionnez une région:",
                    dcc.Dropdown(
                        id='geo-selection',
                        options=[{'label': provOrder[i], 'value': provOrder[i]}
                                 for i in range(len(provOrder))],
                        value='CA',
                        style={'verticalAlign': 'middle'}
                    ),
                    html.Br(),
                ], className="m-2 p-2"),
            ), id='sticky-dropdown'),
    ], className='sticky-top select-region mb-2', fluid=True),
    dbc.Container(
        dbc.Row([
            html.Div(
                [
                    html.H3('Introduction'),
                    html.Span('''
Le secteur sans but lucratif emploie quelque 2,5 millions de Canadiens, ce qui correspond à environ 13 % de la population active du Canada. Deux tiers des employés de ce secteur travaillent pour des institutions gouvernementales à but non lucratif. Le tiers restant travaille dans les institutions du sous-secteur de base, dont le ratio est d’environ 3:1 entre les organismes communautaires et les institutions commerciales à but non lucratif.
                              '''),
                    html.Sup(html.A('1', href='#footnote1', id="ref1")),
                    html.Span('''
                               Pour obtenir plus de détails sur la répartition du personnel rémunéré par type d’organisme à but non lucratif et par secteur d’activités, consulter la section Personnel rémunéré du secteur sans but lucratif ailleurs sur ce site Web.
                           '''),
                    html.Br(),
                    html.Br(),
                    html.H3('Type d’emploi'),
                    html.Span('''
De façon générale, près de quatre cinquièmes des employés du secteur sans but lucratif travaillent à temps plein et un cinquième travaille à temps partiel. Les employés à temps partiel représentent une plus grande partie de la main-d’œuvre des organismes communautaires à but non lucratif que celle des institutions communautaires et gouvernementales à but non lucratif.
                    ''', className='mt-4'),
                    html.Br(),
                    html.Br(),
                    html.Span('''
Ces tendances sont raisonnablement les mêmes entre les provinces, bien qu’il existe certaines fluctuations. La situation dans les territoires est plus difficile à évaluer en raison de l’arrondissement des données publiées par Statistique Canada.
                    ''', className='mt-4'),
                    html.Sup(html.A('2', href='#footnote2', id="ref2")),
                    # TODO: Add footnote
                    # NNo and % of full time ...
                    dcc.Graph(
                        id='jobsType', style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H4('Salaires moyens par type d’organisme'),
                    dcc.Markdown('''
En ce qui a trait aux salaires moyens par type d’organisme, la rémunération au sein des organismes communautaires à but non lucratif est souvent inférieure à celle des autres types d’organismes à but non lucratif. À l’échelle nationale, la rémunération moyenne des postes à temps plein au sein des organismes communautaires à but non lucratif est inférieure d’environ un cinquième à celle des postes à temps plein au sein des institutions communautaires et gouvernementales à but non lucratif. Bien que la rémunération des postes à temps partiel au sein des organismes communautaires à but non lucratif soit à peu près équivalente à celle des postes à temps partiel au sein des institutions commerciales à but non lucratif, les deux demeurent inférieures de près d’un tiers à celle des postes à temps partiel au sein des institutions gouvernementales à but non lucratif. La combinaison de salaires inférieurs et d’un nombre plus élevé d’emplois à temps partiel signifie que le salaire typique au sein des organismes communautaires à but non lucratif est environ 26 % moins élevé que le salaire typique au sein des institutions gouvernementales à but non lucratif, et 22 % moins élevé que le salaire typique au sein des institutions commerciales à but non lucratif.
                    ''', className='mt-4'),
                    dcc.Markdown('''
Selon la province, les salaires moyens des postes à temps plein au sein des organismes communautaires à but non lucratif sont souvent vingt à trente pour cent moins élevés que ceux des postes à temps plein au sein des institutions gouvernementales à but non lucratif. L’écart est moins prononcé en Alberta, en Colombie-Britannique et en Ontario, et plus Georg important en Saskatchewan et dans les provinces de l’Atlantique. Par ailleurs, les salaires des postes à temps plein au sein des institutions communautaires à but non lucratif sont inférieurs aux salaires des postes à temps plein au sein des institutions gouvernementales à but non lucratif, mais les écarts sont moins prononcés, voire inexistants, en Alberta et en Ontario. Quant aux salaires des postes à temps partiel au sein des organismes et des institutions communautaires à but non lucratif, ils se ressemblent davantage entre les provinces que les salaires des postes à temps plein, mais ils demeurent inférieurs à ceux des postes à temps partiel au sein des institutions gouvernementales à but non lucratif. Les fluctuations entre les salaires moyens semblent surtout attribuables aux variations entre les pourcentages de travailleurs à temps plein et à temps partiel.
                    ''', className='mt-4'),
                    # Average wages and salaries by employment type
                    dcc.Graph(
                        id='wagesType', style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H3(
                        'Caractéristiques de la population active du secteur sans but lucratif'),
                    dcc.Markdown('''
À l’échelle nationale, sept employés du secteur sans but lucratif sur dix sont des femmes. Le nombre de femmes est plus élevé dans les organismes et les institutions commerciales à but non lucratif, et moins élevé dans les institutions commerciales à but non lucratif. Comme c’est généralement le cas avec les autres effectifs, la majorité des employés du secteur sans but lucratif est âgée de 25 à 64 ans. Dans ce secteur, comparativement aux organismes et institutions commerciales à but non lucratif, une proportion considérablement plus élevée des employés des institutions gouvernementales à but non lucratif font partie de ce groupe d’âge. Les employés des organismes communautaires à but non lucratif sont disproportionnellement susceptibles d’avoir 65 ans, alors que les employés des institutions commerciales à but non lucratif sont disproportionnellement susceptibles d’avoir moins de 25 ans. Par ailleurs, les employés du secteur sans but lucratif sont plutôt instruits. En fait, un peu moins de la moitié d’entre eux ont un diplôme universitaire. Comparativement aux autres employés, ceux des institutions gouvernementales à but non lucratif sont un peu plus susceptibles d’avoir un diplôme universitaire, alors que ceux des organismes communautaires à but non lucratif et surtout des institutions commerciales à but non lucratif sont beaucoup plus susceptibles d’avoir un diplôme d’études secondaires ou moins. Au niveau provincial, ces tendances relatives à l’âge et à l’instruction sont plutôt semblables, mais elles sont souvent plus prononcées qu’au niveau national.
                    ''', className='mt-4'),
                    dcc.Markdown('''
En ce qui a trait aux autres caractéristiques, plus d’un quart des employés du secteur sans but lucratif ont immigré au Canada à un certain moment de leur vie ou sont membres d’une minorité visible. Ces données varient peu selon le type d’organisme à but non lucratif. Environ un employé sur 25 s’auto-identifie comme étant Autochtone. Même si la différence entre les organismes communautaires à but non lucratif et les autres types d’organismes à but non lucratif n’est que de deux points de pourcentage, ce groupe relativement modeste signifie que les employés des organismes communautaires à but non lucratif sont beaucoup plus susceptibles d’être des Autochtones que les employés des autres types d’organismes à but non lucratif. À l’échelle provinciale, la proportion d’employés du secteur sans but lucratif qui ont immigré au Canada à un certain moment de leur vie ou qui sont membres d’une minorité visible a tendance à être plus élevée en Ontario et en Colombie-Britannique. Elle est plus faible dans les provinces de l’Atlantique. Enfin, les employés des organismes du secteur sans but lucratif en Saskatchewan et au Manitoba sont beaucoup plus susceptibles d’être des Autochtones.
                    '''),
                    # TODO: Add footnote
                    # Dist of nonprofit employees
                    dcc.Dropdown(
                        id='demo-selection-jobs',
                        options=[{'label': demos[i], 'value': demos[i]}
                                 for i in range(len(demos))],
                        value='Éducation formelle',
                        style={'verticalAlign': 'middle'}
                    ),
                    dcc.Graph(
                        id='jobsDemog', style={
                            'marginTop': marginTop}
                    ),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H4('Salaires moyens par caractéristique de travailleur'),
                    dcc.Markdown('''
Bien que la plupart des employés du secteur sans but lucratif soient des femmes, celles-ci gagnent considérablement moins que les hommes employés dans ce même secteur. Cet écart salarial est plus important dans les institutions commerciales à but non lucratif et moins élevé dans les institutions gouvernementales à but non lucratif. En ce qui a trait au salaire selon le groupe d’âge, le salaire moyen a tendance à augmenter jusqu’à la tranche d’âge de 45 ans à 54 ans, puis il diminue. À l’échelle nationale, dans le cas des employés de 25 à 64 ans, les salaires offerts au sein des organismes communautaires à but non lucratif ont tendance à être un quart moins élevés que les salaires offerts au sein des institutions gouvernementales à but non lucratif. De plus, les écarts sont plus importants entre les jeunes employés et les employés plus âgés. Quant aux salaires offerts au sein des institutions commerciales à but non lucratif, ils sont environ un quart moins élevés que les salaires offerts au sein des institutions gouvernementales à but non lucratif dans le cas des employés de moins de 25 ans. Toutefois, cet écart disparaît et se renverse même avec l’âge avant de refaire surface chez les employés de 65 ans et plus. Par ailleurs, les salaires moyens ont tendance à augmenter avec les niveaux d’éducation formelle. Les salaires offerts au sein des organismes communautaires à but non lucratif sont toujours inférieurs à ceux qui sont offerts dans les institutions gouvernementales à but non lucratif. De plus, l’écart a tendance à augmenter avec le niveau d’éducation. Quant aux salaires moyens offerts au sein des institutions commerciales à but non lucratif, dans le cas des employés dont le niveau d’éducation formelle est moins élevé qu’un certificat de compétence ou inférieur, ils sont de 10 % à 15 % plus élevés que ceux qui sont offerts dans les institutions gouvernementales à but non lucratif, mais légèrement inférieurs dans le cas des employés qui détiennent un diplôme collégial ou plus.
                    ''', className='mt-4'),
                    dcc.Markdown('''
Au sein des institutions gouvernementales à but non lucratif, le salaire moyen des employés qui ont immigré au Canada à un certain moment de leur vie est légèrement supérieur à celui des non-immigrants, mais le contraire est tout aussi vrai au sein des organismes et des institutions commerciales à but non lucratif. Les écarts entre les salaires du sous-secteur de base et les salaires gouvernementaux sont légèrement plus élevés chez les employés immigrants que chez les employés nés au Canada, surtout au sein des institutions commerciales à but non lucratif. Quant aux employés des minorités visibles, ils ont tendance à toucher un salaire inférieur dans tous les types d’organismes à but non lucratif. Le plus grand écart revient aux institutions commerciales à but non lucratif et le plus faible appartient aux institutions gouvernementales à but non lucratif. La situation est très semblable dans le cas des employés autochtones. Toutefois, l’écart le plus faible entre les salaires moyens des employés autochtones et non autochtones revient aux organismes communautaires à but non lucratif, quoique les salaires des deux groupes sont inférieurs de plus d’un quart à ceux des institutions gouvernementales à but non lucratif.
                    '''),
                    # TODO: Add footnote
                    dcc.Dropdown(
                        id='demo-selection-wages',
                        options=[{'label': demos[i], 'value': demos[i]}
                                 for i in range(len(demos))],
                        value='Éducation formelle',
                        style={'verticalAlign': 'middle'}
                    ),
                    # Av nonprofit wages by dmeo
                    dcc.Graph(
                        id='wagesDemog', style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]
        ),
    ),
    dbc.Container([html.Div(
                [
                    html.H2(
                        " Note de bas de page",
                        className="anchored quarto-appendix-heading"),
                    html.Ol([
                        html.Li(
                            [
                                html.P(
                                    "Le Compte satellite des institutions sans but lucratif et du bénévolat de Statistique Canada (source de données utilisée pour cette histoire) divise le secteur sans but lucratif en trois catégories :"),
                                html.P([html.B("Organismes communautaires à but non lucratif."), " Ces organismes sont indépendants du gouvernement et produisent des biens et des services sans frais, ou à des prix économiquement non significatifs (c’est-à-dire que les prix demandés influencent peu les quantités de biens ou de services produites ou achetées par les consommateurs). Les biens et les services qu’ils produisent peuvent être consommés par des foyers (y compris des particuliers) ou par la société dans son ensemble. Ils comprennent, par exemple, les organismes de services à la personne, tels que les banques alimentaires, les refuges, les groupes jeunesse, les lieux de culte, les organismes de défense et les clubs de service."]),
                                html.P([html.B("institutions commerciales à but non lucratif."), "À l’instar des organismes communautaires à but non lucratif, ces institutions sont indépendantes du gouvernement. Toutefois, elles produisent des biens et des services destinés aux foyers ou à la société à des prix économiquement significatifs (c’est-à-dire qu’ils ont pour activité la production marchande), ou encore elles produisent des biens et des services destinés aux entreprises ou à d’autres organismes à but non lucratif. Elles comprennent, par exemple, les associations d’affaires, les chambres de commerce et les associations de copropriétaires (condominiums)."]),
                                html.P([html.B("Institutions gouvernementales à but non lucratif."), " Ces institutions sont semblables aux organismes communautaires à but non lucratif en ce sens qu’elles produisent des biens et des services à des prix économiquement non significatifs. La principale différence réside dans le fait qu’elles sont grandement influencées par le gouvernement, même si elles sont distinctes de celui-ci. Elles comprennent, par exemple, les hôpitaux, certains établissements de soins pour bénéficiaires internes, les universités et les collèges."]),
                                html.P(
                                    [
                                        "Les organismes et les institutions commerciales à but non lucratif sont regroupés dans le",
                                        html.Em(
                                            "sous-secteur sans but lucratif de base"),
                                        "  qui contraste avec le ",
                                        html.Em("sous-secteur des institutions gouvernementales à but non lucratif."), html.A(
                                            "↩︎", href="#ref1", className="footnote-back", role="doc-backlink")
                                    ]
                                )
                            ], id="footnote1"),
                        html.Li([
                            html.P([
                                "Lorsque l’emploi dans un sous-secteur et un secteur d’activités est arrondi à moins de mille employés, Statistique Canada déclare que le nombre d’employés est de zéro.",
                                html.A(
                                    "↩︎",
                                    href="#ref2",
                                    className="footnote-back",
                                    role="doc-backlink")
                            ], id="fn2")
                        ], id="footnote2"),
                    ])
                ],
            )], className="footnote"
        ),
    footer
])
