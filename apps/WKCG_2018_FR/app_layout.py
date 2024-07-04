# App layout file for WKCG_2018_FR converted from
# Qu_est_ce_qui_empeche_de_donner_plus_2018.py

from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app
from ..layout_utils import gen_home_button, gen_navbar, footer
from .callbacks import register_callbacks
from .data_processing import *

register_callbacks(app)

navbar = gen_navbar("What_keeps_Canadians_from_giving_more_2018")
home_button = gen_home_button()
marginTop = 20

layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1("Qu'est-ce qui empeche de donner plus?"),
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
    # Note: filters put in separate container to make floating element later
    #    dbc.Container(
    #        [
    #         html.Div(["Sélectionnez une région:",
    #             dcc.Dropdown(
    #                       id='region-selection',
    #                       options=[{'label': region_names[i], 'value': region_values[i]} for i in range(len(region_values))],
    #                       value='CA',
    #                       style={'vertical-align': 'left'}
    #                   ),
    #             ],
    #             className='col-md-10 col-lg-8 mx-auto mt-4'
    #         ),
    #         ], style={'backgroundColor':'F4F5F6'},
    #     className='sticky-top select-region mb-2', fluid=True),
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
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, à peine plus de deux tiers des personnes (68 %) au Canada ont déclaré avoir fait un don à un organisme de bienfaisance ou à but non lucratif pendant l’année qui l’a précédée.
                    ''', className='mt-4'),
                    dcc.Markdown('''
                    Afin de mieux comprendre les facteurs susceptibles de limiter le soutien des donateur.trice.s, on a demandé aux personnes qui ont donné moins de 1 150 $ l’année précédente si, parmi dix facteurs différents, un ou plusieurs de ceux-ci les empêchaient de donner plus qu’ils l’auraient fait autrement. Nous analysons ci-dessous l’incidence de ces freins sur le don. Dans le texte, nous décrivons les résultats au niveau national et vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer légèrement par rapport aux résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.
                    '''),
                    dcc.Markdown('''Ne pas avoir les moyens financiers de donner plus et le sentiment d’avoir assez donné sont les freins cités les plus souvent par une marge considérable. Les autres facteurs limitant les dons étaient notamment la préférence pour d’autres méthodes de soutien (comme donner directement aux personnes dans le besoin ou faire du bénévolat) et la difficulté à solliciter les personnes de manière efficace. À l’échelle nationale, un quart des personnes ont déclaré ne pas donner plus parce qu’on ne les a pas sollicitées à cette fin et à peu près un huitième d’entre elles disent avoir de la difficulté à trouver une cause digne de leur soutien ou ne pas savoir où donner plus. De même, un peu plus d’un cinquième d’entre elles se demandent avec inquiétude si leurs dons seront utilisés avec efficience et efficacité et expriment des réserves à l’égard des méthodes de sollicitation. Enfin, selon un peu moins d’un sur six donateur.trice.s, les crédits d’impôt sont insuffisants pour les motiver à augmenter leurs dons.
                                 ''')
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Barriers reported by donors.
            html.Div(
                [
                    dcc.Graph(
                        id='BarriersOverall', style={
                            'marginTop': marginTop}),
                    html.P("Quant à l’incidence de ces freins potentiels sur le montant des dons, l’efficacité de la sollicitation des donateur.trice.s constitue manifestement un facteur important. Les personnes à qui on n’a pas demandé de donner plus, qui trouvaient difficilement une cause digne de leur soutien ou qui ne savaient pas où donner plus avaient toutes tendance à faire des dons légèrement inférieurs à ceux des personnes qui ne faisaient pas état de ces freins. Les personnes qui n’avaient pas les moyens financiers de donner plus tendaient également à faire des dons légèrement inférieurs."),
                    html.P("Il est important de comprendre que bien que ces freins aient effectivement réduit les montants des dons, ils ne sont pas tous associés à des dons inférieurs en valeur absolue. Certains d’entre eux semblent jouer un rôle plus déterminant pour les personnes aux dons plus importants. Les personnes satisfaites des montants déjà donnés ou que la méthode de sollicitation des dons préoccupe ou ayant donné directement aux personnes dans le besoin, sans passer par un organisme, ont toutes tendance à donner des montants relativement plus importants que celles qui ne font pas état de ces freins."),
                    html.P("Enfin, certains freins ne semblent entraîner aucune différence dans les montants des dons en valeur absolue. Les montants habituels des dons des personnes qui se demandent avec inquiétude si leurs dons seront utilisés avec efficience et efficacité, qui estiment les crédits d’impôt insuffisants pour les motiver ou qui préfèrent faire du bénévolat plutôt que des dons ne semblent pas statistiquement différents des montants des dons des personnes qui ne mentionnent pas ces freins."),
                    # Average amounts contributed by donors reporting and not
                    # reporting specific barriers.
                    dcc.Graph(
                        id='BarriersAvgAmts', style={
                            'marginTop': marginTop}),

                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Concerns about efficiency and effectiveness
            html.Div(
                [
                    html.H5(
                        "Préoccupations concernant l’efficience et l’efficacité"),
                    html.P("Les personnes qui s’abstenaient de donner plus par crainte que leurs contributions financières ne soient pas utilisées avec efficience ou efficacité ont été priées d’indiquer si un ou plusieurs de trois facteurs précis expliquaient leur préoccupation. En bref, cette opinion semble liée à la crainte que des dons supplémentaires ne soient pas utilisés à bon escient. À l’échelle nationale, selon trois personnes sur cinq étant de cet avis, les organismes n’expliquent pas suffisamment bien comment ils utiliseraient des dons supplémentaires, environ la moitié d’entre elles croient que les organismes consacrent des ressources financières excessives aux collectes de fonds et elles sont environ quatre sur dix à se dire incapables de constater l’incidence de leurs dons sur la cause ou la communauté à laquelle ils sont destinés. Environ une de ces personnes sur huit est préoccupée par l’utilisation de ses dons pour une autre raison."),
                    # Reasons for efficiency / effectiveness concerns.
                    dcc.Graph(
                        id='EfficiencyConcerns', style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H5("Aversion à l’égard des méthodes de sollicitation"),
                    html.P("On a demandé aux personnes qui s’abstenaient de donner plus par aversion à l’égard des méthodes de sollicitation d’indiquer ce qui leur déplaisait dans les sollicitations qu’elles avaient reçues. Dans l’ensemble, le nombre de demandes de dons reçues est clairement une préoccupation importante. À l’échelle nationale, environ la moitié des personnes qui limitent leurs dons parce qu’elles n’aiment pas les sollicitations qu’elles reçoivent ont cité les multiples demandes émanant du même organisme et le nombre total de demandes reçues pour expliquer leur manque de soutien. Quant aux autres facteurs, environ la moitié de ces personnes n’aimaient pas les méthodes employées par les organismes pour solliciter des dons; environ deux cinquièmes des personnes dans ce cas n’aimaient pas le ton employé à cette fin et un peu moins d’un tiers d’entre elles n’aimaient pas l’heure de la journée à laquelle elles recevaient habituellement ces sollicitations."),
                    # Reasons for disliking solicitations.
                    dcc.Graph(
                        id='DislikeSolicitations', style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Personal & economic characteristics
            html.Div(
                [
                    html.H3('Caractéristiques personnelles et économiques'),
                    html.P("Toutes les personnes au Canada ne font pas face aux mêmes freins et n’y réagissent pas de la même façon. L’incidence de nombreux freins varie selon leurs caractéristiques personnelles et économiques. Nous analysons ci-dessous les tendances des variations des freins aux dons selon certains des facteurs démographiques les plus importants. Là encore, nous présentons dans le texte les résultats au niveau national, mais vous pourrez utiliser le menu déroulant pour passer en revue les résultats au niveau régional."),

                    html.Div([
                        html.H5("Genre"),
                        html.P("À l’échelle nationale, les hommes et les femmes réagissent à peu près de la même façon aux freins, dans la mesure où les uns comme les autres sont tout aussi susceptibles de déclarer que ces freins limitent le montant de leurs dons. Les hommes et les femmes se distinguent cependant par plusieurs caractéristiques clés. Plus particulièrement, les hommes ont plus tendance à limiter leurs dons parce qu’ils ont de la difficulté à trouver une cause digne de leur soutien, parce qu’ils ne croient pas que des dons supplémentaires seront utilisés avec efficience et parce qu’ils n’aiment pas la façon dont on les sollicite. Les femmes limitent plus souvent que les hommes leurs dons parce que leurs moyens financiers ne leur permettent pas de donner plus."),
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
                                id='Barriers-Gndr',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P(" Les relations entre les freins et l’âge des donateur.trice.s sont très variables et plusieurs tendances différentes se constatent. Étant donné les montants souvent plus importants de leurs dons, les personnes plus âgées sont plus enclines à être satisfaites des montants déjà donnés et à estimer les crédits d’impôt insuffisants pour justifier des dons supplémentaires. Les personnes plus âgées ont également tendance à donner directement aux personnes dans le besoin au lieu de donner à un organisme. En revanche, elles ont moins tendance à limiter leurs dons parce que personne ne les a sollicitées ou parce qu’elles préfèrent faire don de leur temps. Fait intéressant, les personnes plus jeunes, comme plus âgées, ont plus tendance à limiter leurs dons parce qu’elles n’ont pas les moyens financiers de donner plus ou parce qu’elles ont de la difficulté à trouver une cause digne de leur soutien. La majorité des autres freins ont une incidence relativement uniforme sur les donateur.trice.s., à l’exception des personnes âgées de 15 à 24 ans. Les membres du groupe d’âge le plus jeune semblent moins pratiquer le don, en étant nettement moins susceptibles de savoir où donner et moins enclins à se préoccuper des méthodes de sollicitation et de l’utilisation efficiente des dons."),
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
                                id='Barriers-Age',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # Formal Education
                    html.Div([
                        html.H5("Éducation formelle"),
                        html.P("L’incidence de nombreux freins décroît avec l’augmentation du niveau d’éducation formelle. Les personnes au niveau d’éducation formelle supérieur sont moins susceptibles de ne pas savoir où faire des dons supplémentaires, d’avoir de la difficulté à trouver une cause digne de leur soutien ou de donner directement aux personnes dans le besoin au lieu de donner à un organisme. En raison de leur potentiel de revenu généralement supérieur, les personnes au niveau d’éducation formelle supérieur ont également moins tendance à limiter leurs dons parce que leurs moyens financiers ne leur permettent pas de donner plus. À titre de mise en garde, bien que les personnes au niveau d’éducation formelle supérieur donnent habituellement plus, elles sont plus enclines que les autres à ne pas aimer les méthodes de sollicitation. Enfin, les personnes qui n’ont pas achevé leurs études secondaires ont relativement plus tendance à faire du bénévolat que des dons."),
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
                                id='Barriers-Educ',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # household income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("L’importance de plusieurs freins décroît avec l’augmentation du revenu du ménage, plus particulièrement l’impossibilité de donner plus en raison de ses moyens financiers, faire don de son temps au lieu d’argent et donner directement aux personnes dans le besoin au lieu de donner à un organisme. Ne pas savoir où donner plus et la difficulté à trouver une cause digne d’être soutenue ont également tendance à diminuer avec l’augmentation du revenu, mais ces associations sont plus faibles. Les autres freins ne semblent guère varier selon le revenu, du moins au niveau national."),
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
                                id='Barriers-Inc',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # Religious attendance
                    html.Div([
                        html.H5("Pratique religieuse"),
                        html.P("La tendance à faire du bénévolat au lieu de donner plus constitue l’association la plus claire entre les freins à donner et la fréquence de la pratique religieuse, les personnes plus assidues ayant plus tendance à signaler ce frein. La majorité des autres freins ne varient pas d’une manière claire et prévisible selon l’assiduité aux offices religieux. L’exception la plus notable est celle des personnes qui n’assistent pas aux offices religieux ou qui y assistent très épisodiquement et qui sont légèrement moins susceptibles de donner directement aux personnes dans le besoin au lieu de donner à un organisme."),
                        # Barriers to giving more by religious attendance
                        html.Div([
                            "Sélectionnez une barrière:",
                            dcc.Dropdown(
                                id='barrier-selection-religion',
                                options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(
                                    len(barriers_names))],
                                value='Montant déjà donné suffisant',
                                style={'verticalAlgin': 'middle'}
                            ),
                        ],
                            className='col-md-10 col-lg-8 mx-auto mt-4'),
                        html.Div([
                            dcc.Graph(
                                id='Barriers-Relig',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # Other personal & economic characteristics
                    html.Div([
                        html.H5("Autres facteurs"),
                        html.P("Les tendances liées à la situation matrimoniale et à la situation d’emploi semblent principalement liées à l’âge des donateur.trice.s. Par exemple, les personnes qui n’appartiennent pas à la population active (qui ont tendance à être plus âgées) sont plus enclines à ne pas donner plus parce qu’elles sont satisfaites de ce qu’elles ont déjà donné. De même, les célibataires (qui ont tendance à être plus jeunes) sont plus susceptibles de ne pas savoir où donner et d’avoir de la difficulté à trouver une cause digne de leur soutien, tandis que les personnes veuves ont plus tendance à estimer les crédits d’impôt insuffisants pour motiver des dons supplémentaires. Au chapitre du statut d’immigration, pouvoir joindre les personnes naturalisées constitue clairement un défi, ces dernières ayant plus tendance à ne pas savoir où donner plus ou à avoir de la difficulté à trouver une cause digne de leur soutien."),
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
                            id='status-sel-barrier',
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
                            id='BarriersCauses', style={
                                'marginTop': marginTop}),
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
    ),
    footer
])
