# App layout file for WKCG_2013_FR converted from WKC010613_fr.py

from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app
from ..layout_utils import gen_home_button, gen_navbar, footer
from .callbacks import register_callbacks
from .data_processing import *

register_callbacks(app)

navbar = gen_navbar("what_keeps_canadians_from_giving_more_2013")
home_button = gen_home_button(is_2013=True, sat_link=False, bc_link=False)
marginTop = 20

layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1("Qu'est-ce qui empeche de donner plus? (2013)"),
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

    dbc.Container([
        home_button,
        dbc.Row([
            dbc.Col(
                html.Div([
                    "Sélectionnez une région:",
                    dcc.Dropdown(
                        id='region-selection-fr',
                        options=[{'label': region_values[i], 'value': region_values[i]}
                                 for i in range(len(region_values))],
                        value='CA',
                    ), html.Br(),
                ], className='m-2 p-2')
            )
        ], id='sticky-dropdown')
    ], className='sticky-top select-region mb-2', fluid=True),
    dbc.Container(
        dbc.Row([
            html.Div(
                [
                    dcc.Markdown("""
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2013, un peu plus de quatre cinquièmes des personnes au Canada (82 %) ont fait un don à un organisme de bienfaisance ou à but non lucratif pendant l’année qui l’a précédée.
                    """),
                    dcc.Markdown("""
                    Afin de mieux comprendre les facteurs susceptibles de limiter le soutien des donateur.trice.s, on leur a demandé si, parmi dix facteurs différents, un ou plusieurs de ceux-ci les empêchaient de donner plus. Nous analysons ci-dessous l’incidence de ces freins sur le don. Dans le texte, nous décrivons les résultats au niveau national; pour obtenir plus de précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer légèrement par rapport aux résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.
                    """),
                    dcc.Markdown("""
                    Dans l’ensemble, les sentiments d’avoir assez donné et de ne pas avoir les moyens financiers de donner plus étaient de loin les freins signalés le plus souvent. Les autres facteurs limitant les dons étaient la préférence pour d’autres méthodes de soutien (donner directement aux personnes dans le besoin, sans faire appel à un organisme de bienfaisance ou à but non lucratif, ou faire du bénévolat au lieu d’un don) et la conviction que des dons supplémentaires ne seraient pas utilisés efficacement. La sollicitation constituait effectivement un défi, comme le montrent les proportions relativement significatives de personnes qui déclaraient qu’on ne leur avait pas demandé de donner plus ou qu’elles n’aimaient pas la méthode employée à cette fin. Un nombre relativement inférieur de personnes ont limité leurs dons parce que les reçus d’impôt qu’elles recevraient étaient insuffisants pour les motiver, parce qu’elles ne savaient pas où donner plus ou parce qu’elles avaient de la difficulté à trouver une cause digne de leur soutien.
                    """
                                 ),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Barriers reported by donors.
            html.Div(
                [
                    dcc.Graph(
                        id='BarriersOverall_13', style={
                            'marginTop': marginTop}),
                    dcc.Markdown("""
                    Parmi ces freins potentiels ayant une incidence sur les montants des dons des personnes au Canada, l’efficacité de la sollicitation semble constituer un défi clé. Les personnes qui ne savaient pas où donner ou qui trouvaient difficilement une cause digne de leur soutien donnaient beaucoup moins, en moyenne, que celles qui ne faisaient pas état de ces problèmes. Ne pas avoir les moyens financiers de donner plus et l’absence de sollicitation pour donner plus constituaient également des freins significatifs.
                    """),
                    dcc.Markdown("""
                    Il est important de comprendre que, bien que ces freins aient effectivement réduit les montants des dons, les freins n’étaient pas tous associés à des dons inférieurs en valeur absolue. Certains d’eux étaient plus courants pour les personnes aux dons importants. Les personnes satisfaites des montants déjà donnés ou qui n’aimaient pas la façon dont on leur demandait de donner plus octroyaient toutes des montants relativement plus importants que celles qui ne faisaient pas état de ces freins.
                    """),
                    dcc.Markdown("""
                    Enfin, certains freins ne semblaient entraîner aucune différence dans les montants des dons en valeur absolue. Les montants moyens des dons des personnes qui faisaient du bénévolat au lieu de donner plus, qui croyaient que des dons supplémentaires ne seraient pas employés efficacement, qui estimaient insuffisant le crédit d’impôt reçu pour leurs dons ou qui donnaient directement à des personnes, sans faire appel à un organisme, étaient tous très similaires aux montants moyens octroyés par les personnes qui n’étaient pas de leur avis.
                    """
                                 ),
                    # Average amounts contributed by donors reporting and not
                    # reporting specific barriers.
                    dcc.Graph(
                        id='BarriersAvgAmts_13', style={
                            'marginTop': marginTop}),

                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Concerns about efficiency and effectiveness
            html.Div(
                [
                    html.H3(
                        'Préoccupations concernant l’efficience et l’efficacité'),
                    html.P("""
                    Les personnes qui s’abstenaient de donner plus parce qu’elles craignaient que leurs contributions financières ne soient pas utilisées avec efficience ou efficacité ont été priées d’indiquer si un ou plusieurs de trois facteurs précis expliquaient leur préoccupation. Les personnes préoccupées par l’utilisation de leurs dons avaient plus tendance à s’inquiéter parce qu’elles n’avaient reçu aucune explication sur l’utilisation des dons supplémentaires. À l’échelle nationale, un peu moins de la moitié d’entre elles pensaient que les organismes consacraient trop de ressources financières aux collectes de fonds et environ deux sur cinq ne croyaient pas que les organismes qui les sollicitaient pouvaient démontrer leur incidence sur la cause ou la communauté. Environ une de ces personnes sur cinq se disait préoccupée par l’efficience pour une autre raison.
                    """),
                    # Reasons for efficiency / effectiveness concerns.
                    dcc.Graph(
                        id='EfficiencyConcerns_13', style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H5("Aversion à l’égard des méthodes de sollicitation"),
                    html.P("Les personnes qui s’abstenaient de donner plus par aversion à l’égard des méthodes de sollicitation ont été priées d’indiquer précisément ce qui leur déplaisait dans les sollicitations reçues. Le ton des sollicitations était de loin l’aspect qui leur déplaisait. Environ la moitié des d’entre elles n’aimaient pas recevoir plusieurs demandes de dons du même organisme et étaient tout aussi nombreuses à ne pas aimer le nombre de demandes qu’elles recevaient de différents organismes. Les personnes avaient relativement moins tendance à ne pas aimer les autres aspects des sollicitations, comme les méthodes employées pour prendre contact avec elles où l’heure à laquelle on les sollicitait, mais ces raisons étaient quand même citées par une personne sur vingt. Fait intéressant, environ un tiers des personnes qui éprouvaient de l’aversion pour leurs sollicitations l’expliquaient pour d’autres raisons que celles mentionnées expressément par le questionnaire de l’enquête."),
                    # Reasons for disliking solicitations.
                    dcc.Graph(
                        id='DislikeSolicitations_13', style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Personal & economic characteristics
            html.Div(
                [
                    html.Div([
                        html.H4('Caractéristiques personnelles et économiques'),
                        html.P("Toutes les personnes au Canada ne font pas face aux mêmes freins et n’y réagissent pas de la même façon. L’incidence de nombreux freins variait selon leurs caractéristiques personnelles et économiques. Nous analysons ci-dessous les variations des freins aux dons selon certains des facteurs démographiques les plus importants. Là encore, nous présentons dans le texte les résultats au niveau national, mais vous pourrez utiliser le menu déroulant pour passer en revue les résultats au niveau national."),
                        html.H3("Genre"),
                        html.P("""
                        À l’échelle nationale, les hommes faisaient état des principaux freins légèrement plus souvent que les femmes. Les différences ne variaient normalement pas beaucoup, mais cette tendance était très uniforme. Les hommes avaient plus particulièrement tendance à croire que des dons supplémentaires ne seraient pas utilisés efficacement, à ne pas aimer la méthode employée pour solliciter leurs dons et à avoir de la difficulté à trouver des causes dignes de leur soutien. Ne pas avoir les moyens financiers de donner plus était le seul frein dont les hommes avaient significativement moins tendance à faire état.
                        """),
                        # Barriers to giving more by gender
                        # html.Div([
                        #     "Select a barrier:",
                        #     dcc.Dropdown(
                        #       id='barrier-selection',
                        #       options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(len(barriers_names))],
                        #       value='Happy with what already given',
                        #       style={'verticalAlgin': 'middle'}
                        #     ),
                        #   ],
                        #  className='col-md-10 col-lg-8 mx-auto mt-4'),
                        # className='sticky-top select-region mb-2',
                        # fluid=True),
                        dbc.Container([
                            html.Div([
                                "Sélectionnez une barrière:",
                                dcc.Dropdown(
                                    id='barrier-selection',
                                    options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(
                                        len(barriers_names))],
                                    value='Montant déjà donné suffisant',
                                    style={'vertical-align': 'right'}
                                ),
                            ],
                                className='col-md-10 col-lg-8 mx-auto mt-4'),
                        ], style={'backgroundColor': 'F4F5F6'},),
                        # className='sticky-top select-region mb-2',
                        # fluid=True),
                        html.Div([
                            dcc.Graph(
                                id='Barriers-Gndr_13',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("""
                        L’incidence de la majorité des freins variait selon l’âge. Étant donné les montants souvent plus importants de leurs dons, les personnes plus âgées étaient plus enclines à être satisfaites des montants déjà donnés et à estimer les crédits d’impôt insuffisants pour motiver des dons supplémentaires. Les personnes plus âgées avaient également tendance à donner directement aux personnes dans le besoin plutôt qu’à un organisme, à croire que des dons supplémentaires ne seraient pas utilisés efficacement et à ne pas aimer la méthode employée pour solliciter leurs dons. Les autres freins diminuaient avec l’âge, en particulier l’absence de sollicitation pour donner plus et ne pas savoir où donner. Fait intéressant, les donateur.trice.s les plus jeunes, comme les donateur.trice.s les plus âgés, avaient plus souvent de la difficulté à trouver une cause digne de leur soutien.
                        """),
                        # Barriers to giving more by age
                        html.Div([
                            "Sélectionnez une barrière:",
                            dcc.Dropdown(
                                id='barrier-selection-age',
                                options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(
                                    len(barriers_names))],
                                value='Montant déjà donné suffisant',
                                style={'verticalAlgin': 'middle'}
                            ),
                        ],
                            className='col-md-10 col-lg-8 mx-auto mt-4'),
                        html.Div([
                            dcc.Graph(
                                id='Barriers-Age_13',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # Formal Education
                    html.Div([
                        html.H5("Éducation formelle"),
                        html.P("""
                        La majorité des freins variaient relativement peu selon le niveau d’éducation formelle. Ne pas savoir où donner et avoir de la difficulté à trouver une cause digne d’être soutenue constituaient la tendance la plus nette, l’une et l’autre baissant de manière significative en fonction de l’augmentation du niveau d’éducation formelle. Les personnes au niveau d’éducation supérieur étaient également moins susceptibles de donner directement aux personnes dans le besoin au lieu de donner à un organisme, mais cette tendance était relativement moins prononcée. Vraisemblablement en raison du nombre de sollicitations qu’elles reçoivent, les personnes au niveau d’éducation supérieur avaient tendance à ne pas aimer la méthode employée pour solliciter leurs dons. Enfin, les personnes non titulaires d’un diplôme du palier secondaire et celles titulaires d’un diplôme universitaire étaient plus enclines, les unes comme les autres, à faire don de leur temps plutôt qu’à donner de l’argent.
                        """),
                        # Barriers to giving more by formal education
                        html.Div([
                            "Sélectionnez une barrière:",
                            dcc.Dropdown(
                                id='barrier-selection-educ',
                                options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(
                                    len(barriers_names))],
                                value='Montant déjà donné suffisant',
                                style={'verticalAlgin': 'middle'}
                            ),
                        ],
                            className='col-md-10 col-lg-8 mx-auto mt-4'),
                        html.Div([
                            dcc.Graph(
                                id='Barriers-Educ_13',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # household income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("""
                        Les tendances nettes, liées au revenu du ménage étaient relativement peu nombreuses. Comme il fallait peut-être s’y attendre, ne pas avoir les moyens de donner plus était la tendance la plus nette qui diminuait quand le revenu du ménage augmentait. L’absence de sollicitation pour donner plus constituait la barrière la plus nette suivante, qui avait tendance à augmenter avec le revenu du ménage. À quelques petites exceptions près (p. ex. les membres des ménages au revenu supérieur ou égal à 100 000 $ étaient moins enclins à donner directement aux personnes dans le besoin), les autres freins ne variaient pas systématiquement selon le revenu du ménage.
                        """),
                        # Barriers to giving more by household income
                        html.Div([
                            "Sélectionnez une barrière:",
                            dcc.Dropdown(
                                id='barrier-selection-income',
                                options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(
                                    len(barriers_names))],
                                value='Montant déjà donné suffisant',
                                style={'verticalAlgin': 'middle'}
                            ),
                        ],
                            className='col-md-10 col-lg-8 mx-auto mt-4'),
                        html.Div([
                            dcc.Graph(
                                id='Barriers-Inc_13',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # Religious attendance
                    html.Div([
                        html.H5("Statut d’immigration"),
                        html.P("""
                        Joindre efficacement les personnes naturalisées représentait clairement un défi pour les organismes. Ces personnes avaient plus tendance à limiter leurs dons parce qu’elles ne savaient pas où donner et parce qu’elles avaient de la difficulté à trouver une cause digne de leur soutien. Elles étaient également plus enclines à ne pas croire que les dons seraient utilisés efficacement et à ne pas aimer la méthode employée pour solliciter leurs dons.
                        """),
                        # Barriers to giving more by religious attendance
                        html.Div([
                            "Sélectionnez une barrière:",
                            dcc.Dropdown(
                                id='barrier-selection-immstat',
                                options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(
                                    len(barriers_names))],
                                value='Montant déjà donné suffisant',
                                style={'verticalAlgin': 'middle'}
                            ),
                        ],
                            className='col-md-10 col-lg-8 mx-auto mt-4'),
                        html.Div([
                            dcc.Graph(
                                id='Barriers-Immstat_fr',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # Other personal & economic characteristics
                    html.Div([
                        html.H5("Autres facteurs"),
                        html.P("La variation selon la situation matrimoniale et la situation d’emploi semblent principalement liées à l’âge. Par exemple, les célibataires (qui avaient tendance à être plus jeunes) étaient plus susceptibles de ne pas savoir où donner et d’avoir de la difficulté à trouver une cause digne de leur soutien, tandis que les personnes non membres de la population active (qui avaient tendance à être plus âgées) étaient plus enclines à être satisfaites des montants qu’elles avaient déjà donnés. Au chapitre de la pratique religieuse, les liens les plus nets avaient trait aux autres formes de soutien. Les personnes plus assidues avaient plus tendance à faire du bénévolat, de préférence à des dons d’argent, et à donner directement aux personnes dans le besoin, sans faire appel à un organisme. Les autres freins ne variaient pas systématiquement en fonction de la pratique religieuse."),
                        # Barriers to giving more by marital status
                        # html.Div([
                        # dcc.Graph(id='Barriers-Marstat', style={'marginTop': marginTop}),
                        # ]),
                        # Barriers to giving more by labour force status
                        # html.Div([
                        # dcc.Graph(id='Barriers-Labour', style={'marginTop': marginTop}),
                        # ]),
                        # Barriers to giving more by immigration status
                        # html.Div([
                        # dcc.Graph(id='Barriers-Immstat', style={'marginTop': marginTop})
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
                            html.Div(["Sélectionnez une barrière:",
                                      dcc.Dropdown(
                                          id='barrier-selection-other',
                                          options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(
                                              len(barriers_names))],
                                          value='Montant déjà donné suffisant',
                                          style={'verticalAlign': 'middle'}
                                      ),],
                                     style={'width': '66%', 'display': 'inline-block'}),
                        ]),
                        dcc.Graph(
                            id='status-sel-barrier_13',
                            style={
                                'marginTop': marginTop})
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'

            ),
            html.Div(
                [
                    html.Div([
                        html.H4('Causes soutenues', className='mt-3'),
                        html.P("Bien que l’ESG DBP ne recueille pas directement de l’information sur les freins qui empêchent les personnes d’augmenter le montant de leurs dons à chaque cause, la comparaison des freins auxquels les personnes qui soutiennent une cause donnée font face et des freins rencontrés par celles qui ne la soutiennent pas peut nous éclairer. Le graphique ci-dessous montre les pourcentages de donateur.trice.s qui ont fait état de chaque frein, subdivisés en fonction de leur don ou de leur absence de don à chaque cause. Plusieurs associations se constatent à l’échelle nationale. Par exemple, les donateur.trice.s aux organismes du secteur des arts et de la culture et à celui de l’éducation et de la recherche ont plus tendance à se préoccuper de l’utilisation efficiente de dons supplémentaires et à ne pas aimer la façon dont on les sollicite. En revanche, les donateur.trice.s aux organismes religieux sont plus enclins à soutenir directement les personnes dans le besoin et à faire du bénévolat au lieu de donner plus. Enfin, les donateur.trice.s aux organismes de services sociaux ont plus tendance à ne pas aimer la façon dont on sollicite des dons supplémentaires de leur part et à donner directement aux personnes dans le besoin au lieu d’augmenter leur soutien en faisant appel à un organisme. Il existe d’autres associations, mais elles sont plus faibles."),
                        html.Div([
                            "Sélectionnez une cause:",
                            dcc.Dropdown(
                                id='cause-selection',
                                options=[{'label': cause_names[i], 'value': cause_names[i]} for i in range(
                                    len(cause_names))],
                                value='Arts et culture',
                                style={'verticalAlgin': 'middle'}
                            ),
                        ], className='col-md-10 col-lg-8 mx-auto mt-4'),
                        # Percentages of cause supporters and non-supporters
                        # reporting each barrier, by cause
                        dcc.Graph(
                            id='BarriersCauses_13', style={
                                'marginTop': marginTop}),
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
    ),
    footer
])


#
