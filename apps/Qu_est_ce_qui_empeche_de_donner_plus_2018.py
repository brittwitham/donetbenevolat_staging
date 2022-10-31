import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd

from utils.data.WDA0101_data_utils import get_region_values
from utils.data.WDC0105_data_utils import get_region_names
from utils.home_button import gen_home_button
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc
import os
import os.path as op

from utils.graphs.WKC0106_graph_utils import single_vertical_percentage_graph, vertical_dollar_graph, vertical_percentage_graph
from utils.data.WKC0106_data_utils import get_data, process_data, get_region_names, get_region_values

from app import app
from homepage import footer #navbar, footer

####################### Data processing ######################
Barriers_2018, AvgAmtBarriers_2018, GivingConcerns_2018, SolicitationConcerns_2018, BarriersByCause_2018 = get_data()

data = [Barriers_2018, AvgAmtBarriers_2018, GivingConcerns_2018, SolicitationConcerns_2018, BarriersByCause_2018]

cause_names = BarriersByCause_2018["Group"].unique()
barriers_names = Barriers_2018["QuestionText"].unique()
status_names = ["État civil", "Situation d'activité", "Statut d'immigration"]

process_data(data)

region_values = get_region_values()
region_names = get_region_names()

###################### App layout ######################
navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                # dcc.Link("Home", href="/")
                dbc.NavLink("À propos", href="https://www.donetbenevolat.ca/",external_link=True)
            ),
            dbc.NavItem(
                dbc.NavLink("EN", href="http://app.givingandvolunteering.ca/What_keeps_Canadians_from_giving_more_2018",external_link=True)
            ),
        ],
        brand="Centre Canadien de Connaissances sur les Dons et le Bénévolat",
        brand_href="/",
        color="#4B161D",
        dark=True,
        sticky='top'
    )
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
        className="bg-secondary text-white text-center pt-4",
    ),
    # Note: filters put in separate container to make floating element later
#    dbc.Container(
#        [
#         html.Div(["Select a region:",
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
#     className='sticky-top bg-light mb-2', fluid=True),
    dbc.Container([
        home_button,
        dbc.Row([
            dbc.Col(
                html.Div([
                    "Sélectionnez une région:",
                    dcc.Dropdown(
                        id='region-selection',
                        options=[{'label': region_values[i], 'value': region_values[i]} for i in range(len(region_values))],
                        value='CA',
                        style={'vertical-align': 'left'}
                    ), html.Br(),
                ], className='m-2 p-2')
            )
        ])
    ],className='sticky-top bg-light mb-2', fluid=True), 
   dbc.Container(
       dbc.Row([
            html.Div(
                [
                    dcc.Markdown('''
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, à peine plus de deux tiers des personnes (68 %) au Canada ont déclaré avoir fait un don à un organisme de bienfaisance ou à but non lucratif pendant l’année qui l’a précédée. 
                    ''',className='mt-4'),
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
                    dcc.Graph(id='BarriersOverall', style={'marginTop': marginTop}),
                    html.P("Quant à l’incidence de ces freins potentiels sur le montant des dons, l’efficacité de la sollicitation des donateur.trice.s constitue manifestement un facteur important. Les personnes à qui on n’a pas demandé de donner plus, qui trouvaient difficilement une cause digne de leur soutien ou qui ne savaient pas où donner plus avaient toutes tendance à faire des dons légèrement inférieurs à ceux des personnes qui ne faisaient pas état de ces freins. Les personnes qui n’avaient pas les moyens financiers de donner plus tendaient également à faire des dons légèrement inférieurs."),
                    html.P("Il est important de comprendre que bien que ces freins aient effectivement réduit les montants des dons, ils ne sont pas tous associés à des dons inférieurs en valeur absolue. Certains d’entre eux semblent jouer un rôle plus déterminant pour les personnes aux dons plus importants. Les personnes satisfaites des montants déjà donnés ou que la méthode de sollicitation des dons préoccupe ou ayant donné directement aux personnes dans le besoin, sans passer par un organisme, ont toutes tendance à donner des montants relativement plus importants que celles qui ne font pas état de ces freins."),
                    html.P("Enfin, certains freins ne semblent entraîner aucune différence dans les montants des dons en valeur absolue. Les montants habituels des dons des personnes qui se demandent avec inquiétude si leurs dons seront utilisés avec efficience et efficacité, qui estiment les crédits d’impôt insuffisants pour les motiver ou qui préfèrent faire du bénévolat plutôt que des dons ne semblent pas statistiquement différents des montants des dons des personnes qui ne mentionnent pas ces freins."),
                    # Average amounts contributed by donors reporting and not reporting specific barriers.
                    dcc.Graph(id='BarriersAvgAmts', style={'marginTop': marginTop}),

                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Concerns about efficiency and effectiveness
            html.Div(
                [
                    html.H5("Préoccupations concernant l’efficience et l’efficacité"),
                    html.P("Les personnes qui s’abstenaient de donner plus par crainte que leurs contributions financières ne soient pas utilisées avec efficience ou efficacité ont été priées d’indiquer si un ou plusieurs de trois facteurs précis expliquaient leur préoccupation. En bref, cette opinion semble liée à la crainte que des dons supplémentaires ne soient pas utilisés à bon escient. À l’échelle nationale, selon trois personnes sur cinq étant de cet avis, les organismes n’expliquent pas suffisamment bien comment ils utiliseraient des dons supplémentaires, environ la moitié d’entre elles croient que les organismes consacrent des ressources financières excessives aux collectes de fonds et elles sont environ quatre sur dix à se dire incapables de constater l’incidence de leurs dons sur la cause ou la communauté à laquelle ils sont destinés. Environ une de ces personnes sur huit est préoccupée par l’utilisation de ses dons pour une autre raison."),
                    # Reasons for efficiency / effectiveness concerns.
                    dcc.Graph(id='EfficiencyConcerns', style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H5("Aversion à l’égard des méthodes de sollicitation"),
                    html.P("On a demandé aux personnes qui s’abstenaient de donner plus par aversion à l’égard des méthodes de sollicitation d’indiquer ce qui leur déplaisait dans les sollicitations qu’elles avaient reçues. Dans l’ensemble, le nombre de demandes de dons reçues est clairement une préoccupation importante. À l’échelle nationale, environ la moitié des personnes qui limitent leurs dons parce qu’elles n’aiment pas les sollicitations qu’elles reçoivent ont cité les multiples demandes émanant du même organisme et le nombre total de demandes reçues pour expliquer leur manque de soutien. Quant aux autres facteurs, environ la moitié de ces personnes n’aimaient pas les méthodes employées par les organismes pour solliciter des dons; environ deux cinquièmes des personnes dans ce cas n’aimaient pas le ton employé à cette fin et un peu moins d’un tiers d’entre elles n’aimaient pas l’heure de la journée à laquelle elles recevaient habituellement ces sollicitations."),
                    # Reasons for disliking solicitations.
                    dcc.Graph(id='DislikeSolicitations', style={'marginTop': marginTop}),
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
                    #  className='sticky-top bg-light mb-2', fluid=True),
                    dbc.Container([
                        html.Div([
                            "Sélectionnez une barrière:",
                            dcc.Dropdown(
                            id='barrier-selection',
                            options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(len(barriers_names))],
                            value='Montant déjà donné suffisant',
                            style={'vertical-align': 'right'}
                            ),
                        ],
                            className='col-md-10 col-lg-8 mx-auto mt-4'),
                    ], style={'backgroundColor':'F4F5F6'},),
                    # className='sticky-top bg-light mb-2', fluid=True),
                        html.Div([
                            dcc.Graph(id='Barriers-Gndr', style={'marginTop': marginTop}),
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
                          options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(len(barriers_names))],
                          value='Montant déjà donné suffisant',
                          style={'verticalAlgin': 'middle'}
                        ),
                      ],
                     className='col-md-10 col-lg-8 mx-auto mt-4'),
                        html.Div([
                            dcc.Graph(id='Barriers-Age', style={'marginTop': marginTop}),
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
                          options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(len(barriers_names))],
                          value='Montant déjà donné suffisant',
                          style={'verticalAlgin': 'middle'}
                        ),
                      ],
                     className='col-md-10 col-lg-8 mx-auto mt-4'),
                        html.Div([
                            dcc.Graph(id='Barriers-Educ', style={'marginTop': marginTop}),
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
                          options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(len(barriers_names))],
                          value='Montant déjà donné suffisant',
                          style={'verticalAlgin': 'middle'}
                        ),
                      ],
                     className='col-md-10 col-lg-8 mx-auto mt-4'),
                        html.Div([
                            dcc.Graph(id='Barriers-Inc', style={'marginTop': marginTop}),
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
                          options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(len(barriers_names))],
                          value='Montant déjà donné suffisant',
                          style={'verticalAlgin': 'middle'}
                        ),
                      ],
                     className='col-md-10 col-lg-8 mx-auto mt-4'),
                        html.Div([
                           dcc.Graph(id='Barriers-Relig', style={'marginTop': marginTop}),
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
                                          options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                                          value='État civil',
                                          style={'verticalAlign': 'middle'}
                                      ),],
                                     style={'width': '33%', 'display': 'inline-block'}),
                            html.Div(["Sélectionnez une barrière:",
                                            dcc.Dropdown(
                                            id='barrier-selection-other',
                                            options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(len(barriers_names))],
                                            value='Montant déjà donné suffisant',
                                            style={'verticalAlign': 'middle'}
                                      ),],                                     
                                     style={'width': '66%', 'display': 'inline-block'}),
                        ]),
                        dcc.Graph(id='status-sel-barrier', style={'marginTop': marginTop})
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'

            ),
            html.Div(
                [
                    html.Div([
                        html.H4('Causes soutenues',className='mt-3'),
                        html.P("Bien que l’ESG DBP ne recueille pas directement de l’information sur les freins qui empêchent les personnes d’augmenter le montant de leurs dons à chaque cause, la comparaison des freins auxquels les personnes qui soutiennent une cause donnée font face et des freins rencontrés par celles qui ne la soutiennent pas peut nous éclairer. Le graphique ci-dessous montre les pourcentages de donateur.trice.s qui ont fait état de chaque frein, subdivisés en fonction de leur don ou de leur absence de don à chaque cause. Plusieurs associations se constatent à l’échelle nationale. Par exemple, les donateur.trice.s aux organismes du secteur des arts et de la culture et à celui de l’éducation et de la recherche ont plus tendance à se préoccuper de l’utilisation efficiente de dons supplémentaires et à ne pas aimer la façon dont on les sollicite. En revanche, les donateur.trice.s aux organismes religieux sont plus enclins à soutenir directement les personnes dans le besoin et à faire du bénévolat au lieu de donner plus. Enfin, les donateur.trice.s aux organismes de services sociaux ont plus tendance à ne pas aimer la façon dont on sollicite des dons supplémentaires de leur part et à donner directement aux personnes dans le besoin au lieu d’augmenter leur soutien en faisant appel à un organisme. Il existe d’autres associations, mais elles sont plus faibles."),
                        html.Div([
                            "Sélectionnez une cause:",
                            dcc.Dropdown(
                                id='cause-selection',
                                options=[{'label': cause_names[i], 'value': cause_names[i]} for i in range(len(cause_names))],
                                value='Arts et culture',
                                style={'verticalAlgin': 'middle'}
                                ),
                            ], className='col-md-10 col-lg-8 mx-auto mt-4'),
                        # Percentages of cause supporters and non-supporters reporting each barrier, by cause
                        dcc.Graph(id='BarriersCauses', style={'marginTop': marginTop}),
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
   ),
   footer
])

################## Graphs #################
# def single_vertical_percentage_graph(dff, title, by="Attribute", sort=False):

#     dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
#                             [dff.Estimate.map(str) + "%" + "*", "...", dff.Estimate.map(str) + "%"])
#     dff['HoverText'] = np.select([dff["Marker"] == "*",
#                                   dff["Marker"] == "...",
#                                   pd.isnull(dff["Marker"])],
#                                  ["Estimate: " + dff.Estimate.map(str) + "% ± " + (dff["CI Upper"] - dff["Estimate"]).map(str) + "%<br><b>Use with caution</b>",
#                                   "Estimate Suppressed",
#                                   "Estimate: " + dff.Estimate.map(str) + "% ± " + (dff["CI Upper"] - dff["Estimate"]).map(str) + "%"])

#     fig = go.Figure()

#     fig.add_trace(go.Bar(x=dff['CI Upper'],
#                          y=dff[by],
#                          orientation="h",
#                          error_x=None,
#                          marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
#                          showlegend=False,
#                          hoverinfo="skip",
#                          text=None,
#                          name="",
#                          textposition="outside",
#                          cliponaxis=False,
#                          offsetgroup=1
#                          ),
#                   )

#     fig.add_trace(go.Bar(x=dff['Estimate'],
#                          y=dff[by],
#                          orientation="h",
#                          error_x=None,
#                          hovertext=dff['HoverText'],
#                          hovertemplate="%{hovertext}",
#                          hoverlabel=dict(font=dict(color="white")),
#                          hoverinfo="text",
#                          marker=dict(color="#c8102e"),
#                          text=dff['Text'],
#                          name="",
#                          textposition='outside',
#                          cliponaxis=False,
#                          offsetgroup=1
#                          ),
#                   )

#     fig.update_layout(title={'text': title,
#                              'y': 0.99},
#                       margin={'l': 30, 'b': 30, 'r': 10, 't': 10},
#                       height=600,
#                       plot_bgcolor='rgba(0, 0, 0, 0)',
#                       showlegend=False,
#                       updatemenus=[
#                           dict(
#                               type="buttons",
#                               xanchor='right',
#                               x=1.2,
#                               y=0.5,
#                               buttons=list([
#                                   dict(
#                                       args=[{"error_x": [None, None],
#                                              "text": [None, dff['Text']]}],
#                                       label="Réinitialiser",
#                                       method="restyle"
#                                   ),
#                                   dict(
#                                       args=[{"error_x": [None, dict(type="data", array=dff["CI Upper"] - dff["Estimate"], color="#424242", thickness=1.5)],
#                                              "text": [dff['Text'], None]}],
#                                       label="Intervalles de confiance",
#                                       method="restyle"
#                                   )
#                               ]),
#                           ),
#                       ]
#                       )

#     fig.update_xaxes(showgrid=False,
#                      showticklabels=False,
#                      autorange=False,
#                      range=[0, 1.25 * max(dff["CI Upper"])])
#     fig.update_yaxes(autorange="reversed",
#                      ticklabelposition="outside top",
#                      tickfont=dict(size=9))

#     if sort:
#         fig.update_yaxes(categoryorder="total descending")

#     markers = dff["Marker"]
#     if markers.isin(["*"]).any() and markers.isin(["..."]).any():
#         fig.update_layout(margin={'l': 40, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href='/popup'>Ce quoi ça?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="*<i>Use with caution<br>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     elif markers.isin(["*"]).any():
#         fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href='/popup'>Ce quoi ça?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="*<i>Use with caution</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     elif markers.isin(["..."]).any():
#         fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href='/popup'>Ce quoi ça?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="<i>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     else:
#         fig.update_layout(margin={'l': 30, 'b': 30, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href='/popup'>Ce quoi ça?</a>", xref="paper", yref="paper", xanchor='right', y=0.32, x=1.2, align="left", showarrow=False)])

#     return fig

# def vertical_dollar_graph(dff, name1, name2, title):
#     dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
#                             ["$" + dff.Estimate.map(str) + "*", "...", "$" + dff.Estimate.map(str)])
#     dff['HoverText'] = np.select([dff["Marker"] == "*",
#                                   dff["Marker"] == "...",
#                                   pd.isnull(dff["Marker"])],
#                                  ["Estimate: $" + dff.Estimate.map(str) + " ± $" + (dff["CI Upper"] - dff["Estimate"]).map(str) + "<br><b>Use with caution</b>",
#                                   "Estimate Suppressed",
#                                   "Estimate: $" + dff.Estimate.map(str) + " ± $" + (dff["CI Upper"] - dff["Estimate"]).map(str)])

#     dff1 = dff[dff['Attribute'] == name1]

#     dff2 = dff[dff['Attribute'] == name2]

#     fig = go.Figure()

#     fig.add_trace(go.Bar(x=dff1['CI Upper'],
#                          y=dff1['Group'],
#                          orientation="h",
#                          error_x=None,
#                          marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
#                          showlegend=False,
#                          hoverinfo="skip",
#                          text=None,
#                          textposition="outside",
#                          cliponaxis=False,
#                          offsetgroup=2
#                          ),
#                   )

#     fig.add_trace(go.Bar(x=dff2['CI Upper'],
#                          y=dff2['Group'],
#                          orientation="h",
#                          error_x=None,
#                          marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
#                          showlegend=False,
#                          hoverinfo="skip",
#                          text=None,
#                          textposition="outside",
#                          cliponaxis=False,
#                          offsetgroup=1
#                          ),
#                   )

#     fig.add_trace(go.Bar(x=dff1['Estimate'],
#                          y=dff1['Group'],
#                          orientation="h",
#                          error_x=None,
#                          hovertext=dff1['HoverText'],
#                          hovertemplate="%{hovertext}",
#                          hoverlabel=dict(font=dict(color="white")),
#                          hoverinfo="text",
#                          marker=dict(color="#c8102e"),
#                          text=dff1['Text'],
#                          textposition='outside',
#                          cliponaxis=False,
#                          name=name1,
#                          offsetgroup=2
#                          ),
#                   )

#     fig.add_trace(go.Bar(x=dff2['Estimate'],
#                          y=dff2['Group'],
#                          orientation="h",
#                          error_x=None,
#                          hovertext=dff2['HoverText'],
#                          hovertemplate="%{hovertext}",
#                          hoverlabel=dict(font=dict(color="white")),
#                          hoverinfo="text",
#                          marker=dict(color="#7BAFD4"),
#                          text=dff2['Text'],
#                          textposition='outside',
#                          cliponaxis=False,
#                          name=name2,
#                          offsetgroup=1
#                          ),
#                   )

#     fig.update_layout(title={'text': title,
#                              'y': 0.99},
#                       margin={'l': 30, 'b': 30, 'r': 10, 't': 10},
#                       height=600,
#                       plot_bgcolor='rgba(0, 0, 0, 0)',
#                       bargroupgap=0.05,
#                       barmode="group",
#                       legend={'orientation': 'h', 'yanchor': "bottom"},
#                       updatemenus=[
#                           dict(
#                               type="buttons",
#                               xanchor='right',
#                               x=1.2,
#                               y=0.5,
#                               buttons=list([
#                                   dict(
#                                       args=[{"error_x": [None, None, None, None],
#                                              "text": [None, None, dff1['Text'], dff2['Text']]}],
#                                       label="Réinitialiser",
#                                       method="restyle"
#                                   ),
#                                   dict(
#                                       args=[{"error_x": [None, None, dict(type="data", array=dff1["CI Upper"] - dff1["Estimate"], color="#424242", thickness=1.5), dict(type="data", array=dff2["CI Upper"] - dff2["Estimate"], color="#424242", thickness=1.5)],
#                                              "text": [dff1['Text'], dff2['Text'], None, None]}],
#                                       label="Intervalles de confiance",
#                                       method="restyle"
#                                   )
#                               ]),
#                           ),
#                       ]
#                       )

#     fig.update_xaxes(showgrid=False,
#                      showticklabels=False,
#                      autorange=False,
#                      range=[0, 1.25 * max(np.concatenate([dff1["CI Upper"], dff2["CI Upper"]]))])
#     fig.update_yaxes(autorange="reversed",
#                      ticklabelposition="outside top",
#                      tickfont=dict(size=9),
#                      categoryorder='array',
#                      categoryarray=dff1.sort_values(by="Estimate", ascending=False)["Group"])

#     markers = pd.concat([dff1["Marker"], dff2["Marker"]])
#     if markers.isin(["*"]).any() and markers.isin(["..."]).any():
#         fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href='/popup'>Ce quoi ça?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="*<i>Use with caution<br>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     elif markers.isin(["*"]).any():
#         fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href='/popup'>Ce quoi ça?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="*<i>Use with caution</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     elif markers.isin(["..."]).any():
#         fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href='/popup'>Ce quoi ça?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="<i>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     else:
#         fig.update_layout(margin={'l': 30, 'b': 30, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href='/popup'>Ce quoi ça?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False)])

#     return fig

# def vertical_percentage_graph(dff, title, name1, name2):
#     dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
#                             [dff.Estimate.map(str) + "%" + "*", "...", dff.Estimate.map(str) + "%"])
#     dff['HoverText'] = np.select([dff["Marker"] == "*",
#                                   dff["Marker"] == "...",
#                                   pd.isnull(dff["Marker"])],
#                                  ["Estimate: " + dff.Estimate.map(str) + "% ± " + (dff["CI Upper"] - dff["Estimate"]).map(str) + "%<br><b>Use with caution</b>",
#                                   "Estimate Suppressed",
#                                   "Estimate: " + dff.Estimate.map(str) + "% ± " + (dff["CI Upper"] - dff["Estimate"]).map(str) + "%"])

#     dff1 = dff[dff['Attribute'] == name1]

#     dff2 = dff[dff['Attribute'] == name2]

#     fig = go.Figure()

#     fig.add_trace(go.Bar(x=dff1['CI Upper'],
#                          y=dff1['QuestionText'],
#                          orientation="h",
#                          error_x=None,
#                          marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
#                          showlegend=False,
#                          hoverinfo="skip",
#                          text=None,
#                          textposition="outside",
#                          cliponaxis=False,
#                          offsetgroup=2
#                          ),
#                   )

#     fig.add_trace(go.Bar(x=dff2['CI Upper'],
#                          y=dff2['QuestionText'],
#                          orientation="h",
#                          error_x=None,
#                          marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
#                          showlegend=False,
#                          hoverinfo="skip",
#                          text=None,
#                          textposition="outside",
#                          cliponaxis=False,
#                          offsetgroup=1
#                          ),
#                   )

#     fig.add_trace(go.Bar(x=dff1['Estimate'],
#                          y=dff1['QuestionText'],
#                          orientation="h",
#                          error_x=None,
#                          hovertext=dff1['HoverText'],
#                          hovertemplate="%{hovertext}",
#                          hoverlabel=dict(font=dict(color="white")),
#                          hoverinfo="text",
#                          marker=dict(color="#c8102e"),
#                          text=dff1['Text'],
#                          textposition='outside',
#                          cliponaxis=False,
#                          name=name1,
#                          offsetgroup=2
#                          ),
#                   )

#     fig.add_trace(go.Bar(x=dff2['Estimate'],
#                          y=dff2['QuestionText'],
#                          orientation="h",
#                          error_x=None,
#                          hovertext=dff2['HoverText'],
#                          hovertemplate="%{hovertext}",
#                          hoverlabel=dict(font=dict(color="white")),
#                          hoverinfo="text",
#                          marker=dict(color="#7BAFD4"),
#                          text=dff2['Text'],
#                          textposition='outside',
#                          cliponaxis=False,
#                          name=name2,
#                          offsetgroup=1
#                          ),
#                   )

#     fig.update_layout(title={'text': title,
#                              'y': 0.99},
#                       margin={'l': 30, 'b': 30, 'r': 10, 't': 10},
#                       height=600,
#                       plot_bgcolor='rgba(0, 0, 0, 0)',
#                       bargroupgap=0.05,
#                       barmode="group",
#                       legend={'orientation': 'h', 'yanchor': "bottom"},
#                       updatemenus=[
#                           dict(
#                               type="buttons",
#                               xanchor='right',
#                               x=1.2,
#                               y=0.5,
#                               buttons=list([
#                                   dict(
#                                       args=[{"error_x": [None, None, None, None],
#                                              "text": [None, None, dff1['Text'], dff2['Text']]}],
#                                       label="Réinitialiser",
#                                       method="restyle"
#                                   ),
#                                   dict(
#                                       args=[{"error_x": [None, None, dict(type="data", array=dff1["CI Upper"] - dff1["Estimate"], color="#424242", thickness=1.5), dict(type="data", array=dff2["CI Upper"] - dff2["Estimate"], color="#424242", thickness=1.5)],
#                                              "text": [dff1['Text'], dff2['Text'], None, None]}],
#                                       label="Intervalles de confiance",
#                                       method="restyle"
#                                   )
#                               ]),
#                           ),
#                       ]
#                       )

#     fig.update_xaxes(showgrid=False,
#                      showticklabels=False,
#                      autorange=False,
#                      range=[0, 1.25 * max(np.concatenate([dff1["CI Upper"], dff2["CI Upper"]]))])
#     fig.update_yaxes(autorange="reversed",
#                      ticklabelposition="outside top",
#                      tickfont=dict(size=9),
#                      categoryorder='array',
#                      categoryarray=dff1.sort_values(by="Estimate", ascending=False)["QuestionText"])

#     markers = pd.concat([dff1["Marker"], dff2["Marker"]])
#     if markers.isin(["*"]).any() and markers.isin(["..."]).any():
#         fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href='/popup'>Ce quoi ça?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="*<i>Use with caution<br>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     elif markers.isin(["*"]).any():
#         fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href='/popup'>Ce quoi ça?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                      dict(text="*<i>Use with caution</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     elif markers.isin(["..."]).any():
#         fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href='/popup'>Ce quoi ça?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="<i>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     else:
#         fig.update_layout(margin={'l': 30, 'b': 30, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href='/popup'>Ce quoi ça?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False)])

#     return fig



################## Callbacks #################
@app.callback(
    dash.dependencies.Output('BarriersOverall', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = Barriers_2018[Barriers_2018['Region'] == region]
    dff = dff[dff["Group"] == "All"]
    title = '{}, {}'.format("Freins signalés par les donateur.trice.s", region)
    return single_vertical_percentage_graph(dff, title, by="QuestionText", sort=True)

@app.callback(
    dash.dependencies.Output('BarriersAvgAmts', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = AvgAmtBarriers_2018[AvgAmtBarriers_2018['Region'] == region]
    dff = dff.replace("Report barrier", "Signalent un frein")
    dff = dff.replace("Do not report barrier", "Ne signalent aucun frein")
    # name1 = "Report barrier"
    name1 = "Signalent un frein"
    # name2 = "Do not report barrier"
    name2 = 'Ne signalent aucun frein'
    title = '{}, {}'.format("Montants moyens des contributions des donateur.trice.s <br> faisant état ou non de freins précis", region)
    return vertical_dollar_graph(dff, name1, name2, title)


@app.callback(
    dash.dependencies.Output('EfficiencyConcerns', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = GivingConcerns_2018[GivingConcerns_2018['Region'] == region]
    dff = dff[dff["Group"] == "All"]
    title = '{}, {}'.format("Préoccupations concernant l’efficience et l’efficacité", region)
    return single_vertical_percentage_graph(dff, title, by="QuestionText", sort=True)

@app.callback(
    dash.dependencies.Output('DislikeSolicitations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SolicitationConcerns_2018[SolicitationConcerns_2018['Region'] == region]
    dff = dff[dff["Group"] == "All"]
    title = '{}, {}'.format("Raisons de l’aversion à l’égard des sollicitations", region)
    return single_vertical_percentage_graph(dff, title, by="QuestionText", sort=True)

@app.callback(
    dash.dependencies.Output('Barriers-Gndr', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection', 'value')

    ])
def update_graph(region, barrier):
    dff = Barriers_2018[Barriers_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == "Genre"]
    dff = dff[dff["QuestionText"] == barrier]
    title = '{}, {}'.format("Barrière de donateurs: " + str(barrier) + " selon le genre", region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('Barriers-Age', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection-age', 'value')

    ])
def update_graph(region, barrier):
    dff = Barriers_2018[Barriers_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == "Groupe d'âge"]
    dff = dff[dff["QuestionText"] == barrier]
    title = '{}, {}'.format("Barrière de donateurs: " + str(barrier) + " selon l’âge", region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('Barriers-Educ', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection-educ', 'value')

    ])
def update_graph(region, barrier):
    dff = Barriers_2018[Barriers_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == "Éducation"]
    dff = dff[dff["QuestionText"] == barrier]
    title = '{}, {}'.format("Barrière de donateurs: " + str(barrier) + " selon l’éducation formelle", region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('Barriers-Inc', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection-income', 'value')

    ])
def update_graph(region, barrier):
    dff = Barriers_2018[Barriers_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == "Catégorie de revenu familial"]
    dff = dff[dff["QuestionText"] == barrier]
    title = '{}, {}'.format("Barrière de donateurs: " + str(barrier) + " selon le revenu du ménage", region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('Barriers-Relig', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection-religion', 'value')

    ])
def update_graph(region, barrier):
    dff = Barriers_2018[Barriers_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == "Fréquence de la fréquentation religieuse"]
    dff = dff[dff["QuestionText"] == barrier]
    title = '{}, {}'.format("Barrière de donateurs: " + str(barrier) + " selon la pratique religiouse", region)
    return single_vertical_percentage_graph(dff, title)

# @app.callback(
#     dash.dependencies.Output('Barriers-Marstat', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value'),
#         dash.dependencies.Input('barrier-selection', 'value')

#     ])
# def update_graph(region, barrier):
#     dff = Barriers_2018[Barriers_2018['Region'] == region]
#     dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
#     dff = dff[dff["Group"] == "Marital status"]
#     dff = dff[dff["QuestionText"] == barrier]
#     title = '{}, {}'.format("Barriers reported by marital status", region)
#     return single_vertical_percentage_graph(dff, title)

# @app.callback(
#     dash.dependencies.Output('Barriers-Labour', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value'),
#         dash.dependencies.Input('barrier-selection', 'value')

#     ])
# def update_graph(region, barrier):
#     dff = Barriers_2018[Barriers_2018['Region'] == region]
#     dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
#     dff = dff[dff["Group"] == "Labour force status"]
#     dff = dff[dff["QuestionText"] == barrier]
#     title = '{}, {}'.format("Barriers reported by labour force status", region)
#     return single_vertical_percentage_graph(dff, title)


# @app.callback(
#     dash.dependencies.Output('Barriers-Immstat', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value'),
#         dash.dependencies.Input('barrier-selection', 'value')
#     ])
# def update_graph(region, barrier):
#     dff = Barriers_2018[Barriers_2018['Region'] == region]
#     dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
#     dff = dff[dff["Group"] == "Immigration status"]
#     dff = dff[dff["QuestionText"] == barrier]
#     title = '{}, {}'.format("Barriers reported by immigration status", region)
#     return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('status-sel-barrier', 'figure'),
    [ 
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection-other', 'value'),
        dash.dependencies.Input('status-selection', 'value')
    ])

def update_graph(region, barrier, status):
    dff = Barriers_2018[Barriers_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == status]
    dff = dff[dff["QuestionText"] == barrier]
    title = '{}, {}'.format("Barrière de donateurs: " + str(barrier).lower() + " selon " + str(status).lower(), region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('BarriersCauses', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('cause-selection', 'value')
    ])
def update_graph(region, cause):
    dff = BarriersByCause_2018[BarriersByCause_2018['Region'] == region]
    dff = dff[dff["Group"] == cause]
    dff = dff.replace('Support cause', 'Soutenir la cause')
    dff = dff.replace('Do not support cause', "Ne pas soutenir la cause")
    # name1 = "Support cause"
    name1 = "Soutenir la cause"
    # name2 = "Do not support cause"
    name2 = "Ne pas soutenir la cause"
    title = '{}, {}'.format("Pourcentages de partisan.e.s et de non-partisan.e.s <br> d’une cause faisant état de chaque frein, selon la cause", region)
    return vertical_percentage_graph(dff, title, name1, name2)