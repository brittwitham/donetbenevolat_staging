# App layout file for WDHG_2013_FR converted from WDA010113_fr.py

from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app
from ..layout_utils import gen_home_button, gen_navbar, footer
from .callbacks import register_callbacks
from .data_processing import *
from .graphs import fr_don_rate_avg_don_amt_prv


register_callbacks(app)

navbar = gen_navbar("who_donates_and_how_much_do_they_give_2013")
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
                        # dcc.Link(html.P('Click here for French', className = "ml-auto col-auto"), href='/WDA0101_fr'),
                        html.H1(
                            'Qui donne aux organismes caritatifs et combien? (2013)'),
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
        dbc.Row(
            dbc.Col(
                html.Div([
                    "Sélectionnez une région:",
                    dcc.Dropdown(
                        id='region-selection',
                        #    options=[{'label': region_names[i], 'value': region_values[i]} for i in range(len(region_values))],
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
            # Starting text
            html.Div(
                [
                    dcc.Markdown("""
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2013, un peu plus de neuf personnes sur dix (92 %) au Canada ont contribué financièrement ou en nature, sous une forme ou une autre, aux organismes de bienfaisance ou à but non lucratif pendant l’année qui l’a précédée. À peine plus de quatre cinquièmes de ces personnes ont fait un don en argent, dont environ trois quarts ont fait un don en nature sous forme d’articles ménagers, de jouets ou de vêtements. Trois cinquièmes d’entre elles ont donné des aliments et environ une sur trente a fait un legs ou pris une forme d’engagement dans son testament. Le montant moyen des dons est de 532 $ et leur total général s’élève approximativement à 12,8 milliards $.
                    """
                                 ),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Forms of Giving
            html.Div(
                [

                    dcc.Graph(id='FormsGiving_13', style={'marginTop': 20}),
                    dcc.Markdown("""
                    La probabilité de faire un don financier et le montant habituel des dons variaient légèrement selon les lieux de résidence. Dans l’ensemble, la probabilité de donner ne variait pas de manière statistiquement significative, les personnes vivant en Colombie-Britannique étant les seules relativement moins enclines à faire des dons. Quant au montant moyen des dons, les personnes du Québec et du Canada atlantique avaient tendance à donner moins que celles des Prairies et de l’Ouest canadien.
                    """
                                 ),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Donation rate & average donation amount by province
            html.Div(
                [
                    # html.H4('Donation rate & average donation amount by province'),
                    dcc.Graph(
                        id='DonRateAvgDonAmt-prv',
                        figure=fr_don_rate_avg_don_amt_prv(
                            DonRates_2018,
                            AvgTotDon_2018))
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Key personal & economic characteristics
            html.Div(
                [
                    html.H3('Caractéristiques personnelles et économiques clés'),
                    html.P("""
                    En plus des variations provinciales, les tendances des dons fluctuaient également selon les caractéristiques personnelles et économiques. Nous examinons ci-dessous les deux mesures clés des dons:
                    """),
                    html.Ul([
                        html.Li(
                            'la probabilité de donner et le montant moyen des contributions, '),
                        html.Li(
                            'les pourcentages de donateur.trice.s et le total des dons pour chaque sous-groupe.'),
                    ]),
                    html.P("""
                    Ces mesures brossent un tableau détaillé du bassin de donateur.trice.s et fournissent un aperçu de la concentration du soutien financier des organismes de bienfaisance et à but non lucratif. Dans le texte, nous décrivons les résultats au niveau national et, pour obtenir des précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer des résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.
                    """
                           ),
                    # Gender
                    html.Div([
                        html.H5("Genre"),
                        html.P("""
                        Au niveau national, les femmes étaient relativement plus enclines à donner que les hommes, mais avaient tendance à donner des montants plutôt inférieurs.
                        """),
                        # Donation rate & average donation amount by gender
                        html.Div([
                            # html.H6("Donation rate & average donation amount by gender"),
                            dcc.Graph(id='DonRateAvgDonAmt-Gndr_13',
                                      style={'marginTop': marginTop}),
                            html.P("""
                        En raison de leurs dons plus importants en moyenne, les hommes représentaient une proportion du total des dons supérieure à celle que leur nombre portait à croire. Bien qu’ils étaient légèrement minoritaires parmi les Canadiens, la valeur totale de leurs dons était légèrement majoritaire.
                        """),
                        ]),
                        # Percentage of donors & total donation value by gender
                        html.Div([
                            # html.H6("Percentage of donors & total donation value by gender"),
                            dcc.Graph(
                                id='PercDon-Gndr_13',
                                style={
                                    'marginTop': marginTop}),
                            # html.P("Looking at how donors tend to allocate their support across different causes, women and men have very similar degrees of focus on their primary cause. Nationally, both allocate just over three quarters of their financial support to their primary cause. While their degree of focus on the primary cause is quite similar, women are somewhat more likely to support secondary causes, as shown by the slightly higher average number of causes supported."),
                        ]),
                        # Focus on primary cause & average number of causes supported by gender
                        # html.Div([
                        #     # html.H6("Focus on primary cause & average number of causes supported by gender"),
                        #     dcc.Graph(id='PrimCauseNumCause-Gndr', style={'marginTop': marginTop}),
                        # ]),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("""
                        La probabilité de donner était la plus faible chez les personnes de 15 à 24 ans, puis augmentait à un niveau relativement constant chez celles âgées de 35 ans et plus. La légère baisse apparente après l’âge de 65 ans n’était pas assez importante pour être statistiquement significative. Les montants moyens des contributions augmentaient jusqu’à l’âge d’environ 45 ans en étant plus ou moins uniformes chez les personnes plus âgées. Là encore, les différences entre ces groupes n’étaient pas statistiquement significatives, du moins au niveau national.
                        """),
                        # Donation rate & average donation amount by age
                        dcc.Graph(id='DonRateAvgDonAmt-Age_13', style={'marginTop': marginTop})
                    ]),
                    html.Div([
                        # html.H6("Donation rate & average donation amount by age"),
                        html.P("""
                        Étant donné leur plus forte tendance à donner et les montants habituellement supérieurs de leurs dons, les personnes âgées de 45 ans et plus représentaient une proportion de la valeur totale des dons supérieure à celle que leur représentation au sein de la population laissait présager. Au contraire, les personnes âgées de moins de 45 ans (et surtout celles de moins de 25 ans) représentaient des proportions de la valeur totale des dons très inférieures à leur représentation au sein de la population.
                        """),
                        # Percentage of donors & total donation value by age
                        html.Div([
                            # html.H6("Percentage of donors & total donation value by age"),
                            dcc.Graph(id='PercDon-Age_13', style={'marginTop': marginTop}),
                            # html.P("Reflecting their smaller typical gift, those aged 15 to 24 tend to allocate more of their contributions on their primary cause and to support a smaller number of causes, on average. While donors aged 25 and older are quite consistent in their level of focus on their primary cause, they are somewhat more likely to support a broader range of causes, as indicated by increases in the average number of causes supported."),
                            # html.Br(),
                        ]),
                        # Focus on primary cause & average number of causes supported by age
                        # html.Div([
                        #     # html.H6("Focus on primary cause & average number of causes supported by age"),
                        #     dcc.Graph(id='PrimCauseNumCause-Age', style={'marginTop': marginTop}),
                        #     html.Br(),
                        # ]),
                    ]),
                    # Formal Education
                    html.Div([
                        html.H5("Éducation formelle"),
                        html.P("""
                        L’augmentation de la probabilité de donner allait de pair avec le niveau d’éducation formelle pour culminer chez les titulaires d’un diplôme postsecondaire. Les montants moyens des dons augmentaient également avec le niveau d’éducation formelle, les titulaires d’un diplôme universitaire donnant nettement plus que les personnes à l’éducation formelle moindre.
                        """),
                        # Donation rate & average donation amount by Formal Education
                        html.Div([
                            # html.H6("Donation rate & average donation amount by formal education"),
                            dcc.Graph(id='DonRateAvgDonAmt-Educ_13', style={'marginTop': marginTop}),
                            html.P("""
                        Principalement du fait de leur tendance à donner des montants supérieurs, les titulaires d’un diplôme universitaire représentaient une proportion de la totalité des dons très supérieure à celle que leur représentation au sein de la population donnait à penser. Les personnes à l’éducation formelle moindre représentaient une proportion très inférieure du total des dons, notamment celles non diplômées du palier secondaire.
                        """),
                            # html.Br(),
                        ]),
                        # Percentage of donors & total donation value by formal education
                        html.Div([
                            # html.H6("Percentage of donors & total donation value by formal education"),
                            dcc.Graph(id='PercDon-Educ_13', style={'marginTop': marginTop}),
                            # html.P("While donors without a high school diploma focus slightly more of their donations on the primary cause, the degree of variation by level of formal eduction is low. Educational attainment does have an appreciable impact on the number causes of supported, almost certainly related to the increase in typical donation amounts with higher levels of formal education."),
                            # html.Br(),
                        ]),
                        # Focus on primary cause & average number of causes supported by formal education
                        # html.Div([
                        #     # html.H6("Focus on primary cause & average number of causes supported by formal education"),
                        #     dcc.Graph(id='PrimCauseNumCause-Educ', style={'marginTop': marginTop}),
                        # ]),
                    ]),
                    # household income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("""
                        À seulement quelques divergences près, la probabilité de donner et les montants moyens augmentaient avec le revenu du ménage. Les ménages au revenu annuel égal ou supérieur à 140 000 $ donnaient souvent beaucoup plus que les ménages au revenu inférieur.
                        """),
                        # Donation rate & average donation amount by household income
                        html.Div([
                            # html.H6("Donation rate & average donation amount by household income"),
                            dcc.Graph(id='DonRateAvgDonAmt-Inc_13', style={'marginTop': marginTop}),
                            html.P("""
                        En raison de leurs dons souvent supérieurs, les ménages au revenu annuel égal ou supérieur à 140 000 $ représentaient un pourcentage de la totalité des dons très supérieur à celui que leur représentation au sein de la population pouvait laisser penser.
                        """),
                            # html.Br(),
                        ]),
                        # Percentage of donors & total donation value by household income
                        html.Div([
                            # html.H6("Percentage of donors & total donation value by household income"),
                            dcc.Graph(id='PercDon-Inc_13', style={'marginTop': marginTop}),
                            # html.Br(),
                        ]),
                        # Focus on primary cause & average number of causes supported by household income
                        # html.Div([
                        #     # html.P("Overall, the degree of focus on the primary cause supported tends to decrease as household income increases while the breadth of causes supported tends to increase."),
                        #     # html.H6("Focus on primary cause & average number of causes supported by household income"),
                        #     dcc.Graph(id='PrimCauseNumCause-Inc', style={'marginTop': marginTop}),
                        #     html.Br(),
                        # ]),
                    ]),
                    # Religious attendance
                    html.Div([
                        html.H5("Pratique religieuse"),
                        html.P("""
                        La probabilité de donner et les montants moyens des dons augmentaient avec la fréquence de la pratique religieuse. Bien que la valeur des dons des personnes assidues aux offices religieux bénéficiait majoritairement aux organisations religieuses, ce n’était pas exclusivement le cas. En effet, elles avaient aussi davantage tendance à donner à des organisations laïques et à leur donner des montants plus importants.
                        """),
                        # Donation rate & average donation amount by religious attendance
                        html.Div([
                            # html.H6("Donation rate & average donation amount by religious attendance"),
                            dcc.Graph(id='DonRateAvgDonAmt-Relig_13', style={'marginTop': marginTop}),
                            html.P("""
                        Étant donné leur tendance plus forte à donner et, plus particulièrement, le montant moyen supérieur de leurs dons, les personnes assidues aux offices religieux, surtout celles qui y assistaient chaque semaine, représentaient des pourcentages disproportionnés du total des dons, compte tenu de leur représentation au sein de la population. Au contraire, celles qui n’assistaient pas ou qu’épisodiquement aux offices représentaient des pourcentages beaucoup plus petits du total des dons.
                        """),
                            # html.Br(),
                        ]),
                        # Percentage of donors & total donation value by religious attendance
                        html.Div([
                            # html.H6("Percentage of donors & total donation value by religious attendance"),
                            dcc.Graph(id='PercDon-Relig_13', style={'marginTop': marginTop}),
                            # html.P("While weekly attenders allocate a somewhat higher proportion of their donations towards their primary cause (almost always religious organizations), they also tend to support a broader range of causes than do those who attend religious services very infrequently or not at all. Interestingly, monthly attenders have the lowest degree of focus on the primary cause and typically support the greatest number of causes. Perhaps unsurprisingly, given their low likelihood of donating and typically smaller donations, non-attenders tend to support the smallest number of causes and tend to be fairly focused on their primary cause."),
                            # html.Br(),
                        ]),
                        # Focus on primary cause & average number of causes supported by religious attendance
                        # html.Div([
                        #     #html.H6("Focus on primary cause & average number of causes supported by religious attendance"),
                        #     dcc.Graph(id='PrimCauseNumCause-Relig', style={'marginTop': marginTop}),
                        #     html.Br(),
                        # ]),
                    ]),
                    # Other personal & economic characteristics
                    html.Div([
                        html.H5("Autres caractéristiques personnelles et économiques"),
                        html.P("""
                        Les autres caractéristiques personnelles et économiques significatives sont la situation matrimoniale, la situation d’emploi et le statut d’immigration. D’une façon générale, les personnes mariées ou en union de fait ou veuves étaient plus susceptibles de donner, et ce, en montants supérieurs, de même que les salariés. Les personnes non membres de la population active avaient légèrement moins tendance à donner, mais étaient enclines à se montrer très généreuses quand elles le faisaient. Au chapitre du statut d’immigration, les personnes nouvellement arrivées au Canada donnaient tout aussi souvent que celles nées au Canada, mais le montant de leurs dons était souvent légèrement supérieur.
                        """),
                        # Donation rate & average donation amount by religious attendance
                        # html.Div([
                        #     # html.H6("Donation rate & average donation amount by marital status"),
                        #     dcc.Graph(id='DonRateAvgDonAmt-MarStat', style={'marginTop': marginTop}),
                        #     # html.Br(),
                        # ]),
                        # Donation rate & average donation amount by labour force status
                        # html.Div([
                        #     # html.H6("Donation rate & average donation amount by labour force status"),
                        #     dcc.Graph(id='DonRateAvgDonAmt-Labour', style={'marginTop': marginTop}),
                        #     # html.Br(),
                        # ]),
                        # Donation rate & average donation amount by immigration status
                        # html.Div([
                        #     # html.H6("Donation rate & average donation amount by immigration status"),
                        #     dcc.Graph(id='DonRateAvgDonAmt-ImmStat', style={'marginTop': marginTop}),
                        #     html.P("Looking at the relative donation roles of the various sub-groups, those who are married or widowed tend to contribute disproportionately large proportions of total donations, while the smaller average donations made by single donors mean they account for a disproportionately small fraction of total donations. The relative role of donors does not vary significantly by labour force status, but New Canadians tend to play a slightly larger financial role in donations than their numbers would indicate."),
                        #     html.Br(),
                        # ]),
                        html.Div(['Sélectionner le statut:',
                                  dcc.Dropdown(
                                      id='status-selection1',
                                      options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                                      value='État civil',
                                      style={'verticalAlign': 'middle'}
                                  ),],
                                 style={'width': '50%', 'display': 'inline-block'}),
                        html.Div([
                            # html.H6("Donation rate & average donation amount by immigration status"),
                            dcc.Graph(id='DonRateAvgDonAmt-other_13', style={'marginTop': marginTop}),
                            html.P("""
                        En général, les personnes mariées ou en union de fait représentaient une proportion du total des dons significativement supérieure à celle que leur nombre laissait présager, de même que les personnes nouvellement arrivées au Canada et, dans une moindre mesure, les salarié.e.s.
                        """),
                            html.Br(),
                        ]),
                        # Percentage of donors & total donation value by marital status
                        # html.Div([
                        #     # html.H6("Percentage of donors & total donation value by marital status"),
                        #     dcc.Graph(id='PercDon-MarStat', style={'marginTop': marginTop}),
                        #     html.Br(),
                        # ]),
                        # # Percentage of donors & total donation value by labour force status
                        # html.Div([
                        #     # html.H6("Percentage of donors & total donation value by labour force status"),
                        #     dcc.Graph(id='PercDon-Labour', style={'marginTop': marginTop}),
                        #     html.Br(),
                        # ]),
                        # Percentage of donors & total donation value by immigration status
                        html.Div(['Select status:',
                                  dcc.Dropdown(
                                      id='status-selection2',
                                      options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                                      value='État civil',
                                      style={'verticalAlign': 'middle'}
                                  ),],
                                 style={'width': '50%', 'display': 'inline-block'}),
                        html.Div([
                            # html.H6("Percentage of donors & total donation value by immigration status"),
                            dcc.Graph(id='PercDon-other_13', style={'marginTop': marginTop}),
                            html.Br(),
                            #html.P("The degree to which Canadians focus on the primary cause they support does not seem to vary significantly according to their marital or labour force status. Married, widowed, and to a certain extent divorced Canadians tend to support a somewhat wider range of causes, as do those who are not in the labour force. Turning to immigration status, New Canadians and those residing in Canada who have not yet obtained landed immigrant status tend to focus more of their support on the primary cause and to support fewer causes than do native-born Canadians."),
                        ]),
                        # Focus on primary cause & average number of causes supported by marital status
                        # html.Div([
                        #     # html.H6("Focus on primary cause & average number of causes supported by marital status"),
                        #     dcc.Graph(id='PrimCauseNumCause-MarStat', style={'marginTop': marginTop}),
                        #     html.Br(),
                        # ]),
                        # # Focus on primary cause & average number of causes supported by labour force status
                        # html.Div([
                        #     # html.H6("Focus on primary cause & average number of causes supported by labour force status"),
                        #     dcc.Graph(id='PrimCauseNumCause-Labour', style={'marginTop': marginTop}),
                        #     html.Br(),
                        # ]),
                        # # Focus on primary cause & average number of causes supported by immigration status
                        # html.Div([
                        #     # html.H6("Focus on primary cause & average number of causes supported by immigration status"),
                        #     dcc.Graph(id='PrimCauseNumCause-ImmStat', style={'marginTop': marginTop}),
                        #     html.Br(),
                        # ]),
                        # html.Div(['Select status:',
                        #               dcc.Dropdown(
                        #                   id='status-selection3',
                        #                   options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                        #                   value='Marital status',
                        #                   style={'verticalAlign': 'middle'}
                        #               ),],
                        #              style={'width': '50%', 'display': 'inline-block'}),
                        html.Div([
                            # html.H6("Focus on primary cause & average number of causes supported by immigration status"),
                            # dcc.Graph(id='PrimCauseNumCause-other3', style={'marginTop': marginTop}),
                            html.Br(),
                        ]),
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'

            ),
        ]),
    ),
    footer
])


#
