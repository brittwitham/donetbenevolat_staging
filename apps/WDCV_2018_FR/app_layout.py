# App layout file for WDCV_2018_FR converted from
# Pourquoi_fait_on_du_benevolat_2018.py

from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app
from ..layout_utils import gen_home_button, gen_navbar, footer
from .callbacks import register_callbacks
from .data_processing import *

register_callbacks(app)

navbar = gen_navbar("Why_do_Canadians_volunteer_2018")
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
                        html.H1('Pourquoi fait-on du bénévolat?'),
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
                        options=[{'label': region_values[i], 'value': region_values[i]}
                                 for i in range(len(region_values))],
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
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, un peu plus de deux personnes sur cinq (41 %) au Canada ont fait du bénévolat pour un organisme de bienfaisance ou à but non lucratif pendant la période d’un an qui l’a précédée. Nous analysons ci-dessous leurs facteurs de motivation. Dans le texte, nous décrivons les résultats au niveau national, mais vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer légèrement par rapport aux résultats au niveau national décrits dans le texte, les tendances générales sont très similaires.
                    ''', className='mt-4'),
                    dcc.Markdown('''
                    Pour mieux comprendre les facteurs susceptibles d’inciter les bénévoles à augmenter leur soutien, on leur a demandé si l’un ou plusieurs de douze facteurs jouaient un rôle important dans leur décision de faire du bénévolat pour l’organisme auquel ils faisaient don du plus grand nombre d’heures. Dans l’ensemble, ces personnes étaient les plus enclines à faire du bénévolat pour apporter une contribution à leur communauté, pour mettre leurs compétences et leurs expériences au service d’une bonne cause et parce qu’elles étaient touchées personnellement par la cause de l’organisme qu’elles soutenaient ou parce qu’elles connaissaient une personne dans ce cas. À l’échelle nationale, environ la moitié des bénévoles sont motivés par le désir d’améliorer leur état de santé ou leur sentiment de bien-être ou de réseauter ou de rencontrer d’autres personnes. Environ deux cinquièmes des bénévoles souhaitent prendre conscience de leurs points forts ou faire du bénévolat comme leurs ami.e.s. Un peu moins d’un tiers des bénévoles veulent soutenir des causes politiques, environnementales ou sociales particulières et environ un quart de ces personnes sont motivées par le fait qu’un membre de leur famille fait du bénévolat, par leurs croyances spirituelles ou pour améliorer leurs possibilités d’emploi. Enfin, les obligations ou les croyances religieuses constituent un facteur de motivation pour environ un cinquième des bénévoles.
                    '''),
                    # Motivations Reported reported by donors.
                    dcc.Graph(
                        id='MotivationsOverall-2',
                        style={
                            'marginTop': marginTop}),
                    dcc.Markdown('''
                    Certaines motivations ont tendance à être associées à des dons de temps plus importants que d’autres, les bénévoles motivés par ces facteurs faisant don de plus de temps, en moyenne. Généralement parlant, certaines motivations parmi les plus répandues ont l’incidence la plus forte. À l’échelle nationale, le nombre d’heures de bénévolat des personnes qui souhaitent employer bénévolement leurs compétences et leur expérience personnelles est supérieur de 80 %, en moyenne, à celui des personnes motivées par d’autres facteurs. Dans le même ordre d’idées, le nombre d’heures de bénévolat des personnes qui souhaitent contribuer à la communauté est supérieur de 50 %, en moyenne, le nombre d’heures des personnes touchées personnellement par la cause est supérieur de 38 % et celui des personnes qui souhaitent améliorer leur état de santé ou leur bien-être de 37 %. Le bénévolat lié au fait que d’autres personnes sont bénévoles ou pour améliorer les possibilités d’emploi n’est pas habituellement associé à un grand nombre d’heures de bénévolat, mais d’autres motivations sont habituellement associées à un nombre d’heures supérieur.
                    '''),
                    # Average hours contributed by volunteers reporting and not
                    # reporting specific motivations
                    dcc.Graph(
                        id='MotivationsAvgHrs', style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Personal & economic characteristics

            html.Div(
                [
                    html.H3('Caractéristiques personnelles et économiques'),

                    html.P("""
                    Bien que les motivations du bénévolat soient fréquemment très personnelles, elles ont fortement tendance à varier en fonction des caractéristiques personnelles et économiques des bénévoles. Nous analysons ci-dessous les variations tendancielles des motivations des bénévoles en fonction de certains facteurs démographiques parmi les plus importants. Là encore, nous décrivons dans le texte les résultats au niveau national, mais vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les résultats régionaux puissent différer dans les détails par rapport aux résultats au niveau national décrits dans le texte, les tendances générales ont tendance à être très similaires.
                    """),
                    html.Div([
                        html.H5("Genre"),
                        html.P("""
                        À l’échelle nationale, les hommes et les femmes ont tendance à faire état à peu près également de la majorité des motivations. En ce qui concerne les exceptions, les femmes sont nettement plus enclines à faire du bénévolat pour prendre conscience de leurs points forts ou pour améliorer leur état de santé ou leur bien-être. Elles sont légèrement plus susceptibles de faire du bénévolat pour réseauter ou pour rencontrer d’autres personnes ou en raison de leurs croyances spirituelles ou autres que les hommes. Enfin, elles sont légèrement moins enclines que les hommes à faire du bénévolat parce que leurs ami.e.s sont des bénévoles.
                        """),
                        html.Div(["Sélectionnez une motivation:",
                                 dcc.Dropdown(
                                     id='motivation_selection',
                                     options=[{'label': motivations_names[i], 'value': motivations_names[i]} for i in range(
                                         len(motivations_names))],  # if isinstance(motivations_names[i], str)],
                                     value='Touché.e personnellement par la cause',
                                     style={'verticalAlign': 'middle'}
                                 ),
                        ],
                            className='bg-light m-2 p-2'),
                        # Volunteer motivations by gender
                        html.Div([
                            dcc.Graph(
                                id='Motivations-Gndr-2',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("""
                        La probabilité de faire du bénévolat pour améliorer ses possibilités d’emploi ou pour prendre conscience de ses points forts a tendance à diminuer avec l’âge dans un cas comme dans l’autre, tandis celle liée aux croyances religieuses ou spirituelles a tendance à augmenter avec l’âge. Le fait que des personnes amies sont des bénévoles, le désir de réseauter ou celui de rencontrer d’autres personnes ou d’employer ses compétences et son expérience personnelles ont l’un et l’autre tendance à être des facteurs de motivation supérieurs pour les bénévoles plus jeunes ou plus âgés. Enfin, la probabilité de faire du bénévolat quand on est touché personnellement par la cause culmine chez les bénévoles âgés de 35 à 44 ans pour diminuer ensuite.
                        """),
                        html.Div(["Sélectionnez une motivation:",
                                 dcc.Dropdown(
                                     id='motivation_selection-age',
                                     options=[{'label': motivations_names[i], 'value': motivations_names[i]} for i in range(
                                         len(motivations_names))],  # if isinstance(motivations_names[i], str)],
                                     value='Touché.e personnellement par la cause',
                                     style={'verticalAlign': 'middle'}
                                 ),
                        ],
                            className='bg-light m-2 p-2'),
                        # Volunteer motivations by age
                        html.Div([
                            dcc.Graph(
                                id='Motivations-Age-2',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # Formal Education
                    html.Div([
                        html.H5("Éducation formelle"),
                        html.P("""
                        L’importance d’employer ses compétences et ses expériences au service du bénévolat a tendance à augmenter avec le niveau d’éducation formelle, tandis que faire du bénévolat pour des raisons religieuses ou parce qu’un membre de sa famille est bénévole a tendance à diminuer. Les personnes n’ayant pas achevé leurs études secondaires (qui ont également tendance à être plus jeunes) sont relativement enclines à faire du bénévolat pour améliorer leurs possibilités d’emploi ou parce que leurs ami.e.s sont des bénévoles, mais sont rarement touchées personnellement par la cause ou animées par le désir de contribuer à la collectivité. Grosso modo, les personnes au niveau d’études inférieur sont légèrement plus enclines à faire du bénévolat pour prendre conscience de leurs points forts. Fait intéressant, à la fois les personnes non titulaires du diplôme de fin d’études secondaires et celles titulaires d’un diplôme universitaire sont plus susceptibles de faire du bénévolat pour améliorer leur état de santé ou leur bien-être.
                        """),
                        html.Div(["Sélectionnez une motivation:",
                                 dcc.Dropdown(
                                     id='motivation_selection-educ',
                                     options=[{'label': motivations_names[i], 'value': motivations_names[i]} for i in range(
                                         len(motivations_names)) if isinstance(motivations_names[i], str)],
                                     value='Touché.e personnellement par la cause',
                                     style={'verticalAlign': 'middle'}
                                 ),
                        ],
                            className='bg-light m-2 p-2'),
                        # Volunteer motivations by formal education
                        html.Div([
                            dcc.Graph(
                                id='Motivations-Educ-2',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # household income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("""
                        Dans l’ensemble, la probabilité de faire du bénévolat pour prendre conscience de ses points forts ou pour améliorer son état de santé et son bien-être a tendance à diminuer avec l’augmentation du revenu. Les personnes au revenu annuel inférieur à 25 000 $ sont nettement plus susceptibles de faire du bénévolat pour améliorer leurs possibilités d’emploi, tandis que celles au revenu du ménage inférieur à 75 000 $ sont plus susceptibles de faire du bénévolat pour réseauter ou pour rencontrer d’autres personnes. Enfin, celles au revenu du ménage supérieur à 100 000 $ sont plus susceptibles d’être motivées par leurs croyances religieuses ou spirituelles pour faire du bénévolat.
                        """),
                        html.Div(["Sélectionnez une motivation:",
                                 dcc.Dropdown(
                                     id='motivation_selection-income',
                                     options=[{'label': motivations_names[i], 'value': motivations_names[i]} for i in range(
                                         len(motivations_names)) if isinstance(motivations_names[i], str)],
                                     value='Touché.e personnellement par la cause',
                                     style={'verticalAlign': 'middle'}
                                 ),
                        ],
                            className='bg-light m-2 p-2'),
                        # Volunteer motivations by household income
                        html.Div([
                            dcc.Graph(
                                id='Motivations-Inc-2',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # Religious attendance
                    # html.Div([
                    #     html.H5("Religious Attendance"),
                    #     html.P("The clearest association between barriers to donating and the frequency of religious attendance is with giving time instead of donating more with more frequent attenders being more likely to report this barrier. Most other barriers do not vary by religious attendance in clear, predictable ways. The most notable exception is that non-attenders and very infrequent attenders are somewhat less likely to give directly to those in need instead of donating to an organization."),
                    #     html.Div(["Sélectionnez une motivation:",
                    #         dcc.Dropdown(
                    #             id='motivation_selection-relig',
                    #             options=[{'label': motivations_names[i], 'value': motivations_names[i]} for i in range(len(motivations_names)) if isinstance(motivations_names[i], str)],
                    #             value='Touché.e personnellement par la cause',
                    #             style={'verticalAlign': 'middle'}
                    #         ),
                    #         ],
                    #  className='bg-light m-2 p-2'),
                    #     # Barriers to giving more by religious attendance
                    #     html.Div([
                    #        dcc.Graph(id='Motivations-Relig-2', style={'marginTop': marginTop}),
                    #     ]),
                    # ]),
                    # Other factors
                    html.Div([
                        html.H5("Autres facteurs"),
                        html.P("""
                         Plusieurs tendances se constatent en association avec d’autres caractéristiques personnelles des bénévoles. Dans l’ensemble, l’augmentation de l’importance de la majorité des motivations va de pair avec celle de l’assiduité aux offices religieux. Faire du bénévolat pour améliorer ses possibilités d’emploi ou pour soutenir une cause politique, environnementale ou sociale constituent des exceptions à cette tendance générale. Sur le plan de la situation matrimoniale, les différences clés semblent principalement liées à l’âge. Par exemple, les célibataires (qui ont tendance à être plus jeunes) ont plus tendance à être motivés par l’amélioration de leurs possibilités d’emploi ou par la prise de conscience de leurs points forts, tandis que les personnes veuves (qui ont tendance à être plus âgées) sont moins susceptibles d’être motivées par ces facteurs. En revanche, ces dernières ont plus tendance à être motivées par les facteurs religieux ou spirituels que les célibataires. Quant à la situation d’emploi, les associations les plus claires sont avec les facteurs liés à l’emploi; les personnes au chômage sont plus enclines à faire du bénévolat pour améliorer leurs possibilités d’emploi et prendre conscience de leurs points forts, tandis que les personnes qui occupent un emploi ressentent moins la nécessité de faire du bénévolat pour réseauter ou pour rencontrer d’autres personnes. Enfin, au chapitre du statut d’immigration, les personnes naturalisées sont plus enclines à faire du bénévolat pour des raisons religieuses ou spirituelles, pour réseauter, pour prendre conscience de leurs points forts et pour soutenir des causes politiques, environnementales ou sociales.
                        """),
                        # # Volunteer motivations by religious attendance
                        # html.Div([
                        #     dcc.Graph(id='Motivations-Relig-2', style={'marginTop': marginTop}),
                        # ]),
                        # Volunteer motivations by marital status
                        # html.Div([
                        #     dcc.Graph(id='Motivations-Marstat-2', style={'marginTop': marginTop}),
                        # ]),
                        # # Volunteer motivations by labour force status
                        # html.Div([
                        #     dcc.Graph(id='Motivations-Labour-2', style={'marginTop': marginTop})
                        # ]),
                        # # Volunteer motivations by immigration status
                        # html.Div([
                        #     dcc.Graph(id='Motivations-Immstat-2', style={'marginTop': marginTop})
                        # ]),
                        html.Div([
                            html.Div(['Sélectionner le statut:',
                                      dcc.Dropdown(
                                          id='status-selection',
                                          options=[{'label': status_names[i], 'value': status_names[i]} for i in range(
                                              len(status_names))],
                                          value='État civil',
                                          style={'verticalAlign': 'middle'}
                                      ),],
                                     style={'width': '33%', 'display': 'inline-block'}),
                            html.Div(['Sélectionnez une motivation:',
                                      dcc.Dropdown(
                                          id='motivation_selection-other',
                                          options=[{'label': motivations_names[i], 'value': motivations_names[i]} for i in range(
                                              len(motivations_names)) if isinstance(motivations_names[i], str)],
                                          value='Touché.e personnellement par la cause',
                                          style={'verticalAlign': 'middle'}
                                      ),],
                                     style={'width': '66%', 'display': 'inline-block'}),

                        ]),
                        dcc.Graph(
                            id='status-sel2',
                            style={
                                'marginTop': marginTop})

                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'

            ),
            html.Div(
                [
                    html.Div([
                        html.H4('Causes soutenues', className='mt-3'),
                        html.P("""
                        Le graphique ci-dessous montre les pourcentages de bénévoles qui font état de chaque motivation, subdivisés en fonction de leur bénévolat ou de leur absence de bénévolat pour la cause particulière sélectionnée dans la visualisation. À l’échelle nationale, plusieurs associations se constatent. Par exemple, les motivations religieuses et spirituelles sont beaucoup plus importantes pour les bénévoles des organismes religieux pour qui le désir d’améliorer leurs possibilités d’emploi importe beaucoup moins. Le désir de soutenir une cause politique, environnementale ou sociale est plus important pour les bénévoles au service d’un éventail de causes, comme l’environnement, le plaidoyer et la politique, le développement et le logement. De même, le fait d’être personnellement touché par la cause ou de connaître une personne dans ce cas est plus important pour les bénévoles des services de santé, tandis que le désir d’améliorer leurs possibilités d’emploi importe aux bénévoles des organismes d’éducation et de recherche. Ce ne sont que quelques-unes des associations qui se constatent.
                        """),
                        html.Div(["Sélectionnez une cause:",
                                 dcc.Dropdown(
                                     id='cause-selection',
                                     options=[{'label': cause_names[i], 'value': cause_names[i]} for i in range(
                                         len(cause_names))],
                                     value='Arts et culture',
                                     style={'verticalAlgin': 'middle'}
                                 ),
                        ],
                            className='bg-light m-2 p-2'),
                        # Percentages of cause supporters and non-supporters
                        # reporting each motivation, by cause
                        dcc.Graph(
                            id='MotivationsCauses-2',
                            style={
                                'marginTop': marginTop}),
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
    ),
    footer
])
