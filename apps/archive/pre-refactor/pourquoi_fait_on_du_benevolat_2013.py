import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc
import os
import os.path as op

from utils.graphs.WTO0207_graph_utils import rate_avg_cause, single_vertical_percentage_graph
from utils.data.WTO0207_data_utils import get_data, process_data, get_region_names, get_region_values


from app import app
from homepage import footer #navbar, footer
from utils.gen_navbar import gen_navbar

####################### Data processing ######################
BarriersVol_2018, SubSecAvgHrs_2018, SubSecVolRates_2018, AllocationVol_2018 = get_data()

data = [SubSecVolRates_2018, SubSecAvgHrs_2018, AllocationVol_2018]
process_data(data)

region_values = get_region_values()
# region_names = get_region_names()
region_names = ['CA', 'BC', 'AB', 'PR', 'ON', 'QC', 'AT']
###################### App layout ######################
navbar = gen_navbar("why_do_canadians_volunteer_2013")

marginTop = 20

layout = html.Div([
    navbar,
    html.Header([
            html.Div(className='overlay'),
            dbc.Container(
                dbc.Row(
                    html.Div(
                        html.Div([
                            html.H1('Pourquoi fait-on du bénévolat? (2013)'),
                            ],
                            className='post-heading'
                        ),
                        className='col-md-10 col-lg-8 mx-auto position-relative'
                    )
                )
            ),
        ], className="sub-header bg-secondary text-white text-center pt-5",
    ),
    dbc.Container([
        dbc.Row([
            dbc.Col(
               html.Div([
                   "Select a region:",
                   dcc.Dropdown(
                       id='region-selection',
                       options=[{'label': region_values[i], 'value': region_values[i]} for i in range(len(region_values))],
                       value='CA',
                       ),
                    html.Br(),
                ],className="m-2 p-2"),
            ),
            # dbc.Col(
            #    html.Div([
            #     "Choose a volunteer activity: ",
            #     dcc.Dropdown(id='activity-selection',
            #         options=[{'label': i, 'value': i} for i in activity_names],
            #         value="Canvassing")
            #     ],className="m-2 p-2"),
            # )
            ],
            id='sticky-dropdown'),
    ], className='sticky-top select-region mb-2', fluid=True),

   dbc.Container([
       dbc.Row([
            # Starting text
            html.Div([
                    dcc.Markdown("""
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2013, plus de deux personnes sur cinq (44 %) au Canada ont fait du bénévolat pour un organisme de bienfaisance ou à but non lucratif pendant la période d’un an qui l’a précédée. Dans le texte, nous décrivons les résultats au niveau national, mais vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer légèrement par rapport aux résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.
                    """),
                    dcc.Markdown("""
                    Pour mieux comprendre les facteurs susceptibles d’inciter les bénévoles à augmenter leur soutien, on leur a demandé si l’un ou plusieurs de onze facteurs jouaient un rôle important dans leur décision de faire du bénévolat pour l’organisme qui en bénéficiait le plus. Dans l’ensemble, ces personnes étaient les plus enclines à faire du bénévolat pour apporter une contribution à leur communauté, pour mettre leurs compétences et leurs expériences au service d’une bonne cause et parce qu’elles étaient touchées personnellement par la cause de l’organisme ou des organismes qu’elles soutenaient ou parce qu’elles connaissaient une personne dans ce cas. À l’échelle nationale, environ la moitié des bénévoles étaient motivés par le désir d’améliorer leur état de santé ou leur sentiment de bien-être, de prendre conscience de leurs points forts ou de réseauter ou de rencontrer d’autres personnes. Entre un tiers et deux cinquièmes de ces personnes faisaient du bénévolat parce que leurs ami.e.s étaient des bénévoles ou pour soutenir des causes politiques, environnementales ou sociales particulières. Les personnes étaient relativement moins motivées par le fait qu’un membre de leur famille était bénévole ou par le désir d’augmenter leurs possibilités d’emploi ou par leurs obligations ou croyances religieuses.
                    """),
                    #  Motivations reported by volunteers graph
                    dcc.Graph(id='FormsGiving', style={'marginTop': 20}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                    dcc.Markdown("""
                    Certaines motivations avaient tendance à être associées à des dons de temps plus importants que d’autres, les bénévoles motivés par ces facteurs faisant don de plus de temps, en moyenne, que les bénévoles motivés par d’autres facteurs. D’après cette mesure, c’est le désir de mettre en application bénévolement leurs compétences qui avait la plus forte incidence, suivi par le désir de prendre conscience de leurs points forts. À l’inverse, le désir d’augmenter leurs possibilités d’emploi motivait relativement peu les bénévoles et le fait que des personnes amies ou des membres de leur famille étaient bénévoles avait peut-être même une incidence négative sur le nombre habituel d’heures de bénévolat. La comparaison de l’incidence caractéristique sur le nombre d’heures de bénévolat et de la fréquence des diverses motivations permet de conclure que l’incidence des facteurs liés principalement aux autres personnes et à l’avantage déterminant (p. ex. possibilités d’emploi) avait tendance à être inférieure et que celle des facteurs liés à la réalisation de soi et aux convictions personnelles avait tendance à être supérieure.
                    """
                    ),
                    # Average hours contributed by volunteers reporting and not reporting specific motivations graph
                    # dcc.Graph(id='DonRateAvgDonAmt-prv', figure=don_rate_avg_don_amt_prv(DonRates_2018, AvgTotDon_2018), style={'marginTop': 20}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Key personal & economic characteristics
            html.Div(
                [
                    html.H3('Caractéristiques personnelles et économiques'),
                    html.P("""
                    Bien que les raisons de faire du bénévolat aient tendance à être très personnelles, au niveau de la population, les motivations variaient fréquemment d’une manière relativement prévisible en fonction des caractéristiques personnelles et économiques des bénévoles. Nous analysons ci-dessous les variations tendancielles des motivations des bénévoles en fonction de certains facteurs démographiques parmi les plus importants. Là encore, nous décrivons dans le texte les résultats au niveau national, mais vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les résultats régionaux puissent différer légèrement dans les détails par rapport aux résultats au niveau national décrits dans le texte, les tendances générales étaient généralement très similaires. 
                    """
                    ),
                
                    # Gender
                    html.Div([
                        html.H5("Genre"),
                        html.P("""
                        Dans l’ensemble, les motivations du bénévolat variaient très peu selon le genre. Les hommes et les femmes avaient tendance à réagir d’une manière très similaire à la majorité des motivations. La plupart des différences entre les genres n’étaient pas statistiquement significatives. Pour autant que celles-ci l’étaient, les femmes étaient légèrement plus enclines à faire du bénévolat pour prendre conscience de leurs points forts, tandis que les hommes étaient légèrement plus enclins à être motivés par le fait que leurs ami.e.s faisaient du bénévolat.
                        """),
                        # Volunteer motivations by gender graph
                        dcc.Graph(id='DonRateAvgDonAmt-Gndrr', style={'marginTop': marginTop}),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("""
                        L’importance de la majorité des motivations (la probabilité selon laquelle les bénévoles en faisaient état) variait de manière significative avec l’âge. L’importance de l’amélioration des possibilités d’emploi diminuait fortement avec l’âge, contrairement à l’importance d’améliorer son état de santé ou son bien-être qui augmentait avec l’âge, de même que le rôle des obligations ou des croyances religieuses (bien que cette motivation était relativement plus importante chez les personnes de moins de 35 ans que chez celles âgées de 35 à 44 ans). Le fait que des personnes amies étaient des bénévoles ou le désir de réseauter ou de rencontrer d’autres personnes était la motivation la plus répandue chez les bénévoles plus jeunes ou plus âgés, tandis que l’incidence de la relation personnelle avec la cause d’un organisme suivait la tendance inverse, en culminant chez les bénévoles âgés de 35 à 54 ans, pour diminuer ensuite. Enfin, le désir de prendre conscience de leurs points forts ou celui de soutenir une cause politique, environnementale ou sociale était plus importants l’un et l’autre chez les bénévoles de moins de 35 ans.
                        """),
                        # Volunteer motivations by age graph
                        dcc.Graph(id='DonRateAvgDonAmt-Age_13', style={'marginTop': marginTop}),
                    ]),
                    # Formal Education
                    html.Div([
                        html.H5("Éducation formelle"),
                        html.P("""
                        Dans une large mesure, les variations des motivations selon le niveau d’éducation formelle semblent plus liées à l’âge des bénévoles qu’à leur niveau d’éducation formelle en soi. Par exemple, les personnes titulaires tout au plus d’un diplôme d’études secondaires (qui ont tendance à être plus jeunes) étaient plus enclines à faire du bénévolat pour améliorer leurs possibilités d’emploi et pour prendre conscience de leurs points forts. Elles avaient aussi plus tendance à faire du bénévolat parce que des personnes amies et des membres de leurs familles étaient des bénévoles et pour réseauter ou rencontrer d’autres personnes. Tous ces facteurs étaient plus fréquents à la fois chez les jeunes et les personnes plus âgées (moins susceptibles de détenir un diplôme universitaire). Quant aux autres tendances significatives, une relation personnelle avec la cause et le désir d’apporter une contribution à la communauté étaient des motivations qui augmentaient l’une et l’autre avec le niveau d’éducation formelle des bénévoles.
                        """),
                        # Volunteer motivations by formal education graph
                        dcc.Graph(id='DonRateAvgDonAmt-Educ_13', style={'marginTop': marginTop}),
                    ]),
                    # Income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("""
                        Dans l’ensemble, les motivations pour le bénévolat variaient relativement peu selon le revenu du ménage. Pour autant que des tendances étaient statistiquement significatives, la probabilité de faire du bénévolat pour réseauter ou pour rencontrer d’autres personnes diminuait avec l’augmentation des revenus du ménage, de même que le bénévolat en raison de croyances ou d’obligations religieuses. Fait intéressant, le bénévolat à l’appui d’une cause politique, environnementale ou sociale particulière était relativement plus fréquent chez les ménages au revenu annuel inférieur à 40 000 $.
                        """),
                        # Volunteer motivations by household income graph
                        dcc.Graph(id='DonRateAvgDonAmt-Inc_13', style={'marginTop': marginTop}),
                    ]),

                    # Other factors
                    html.Div([
                        html.H5("Autres facteurs "),
                        html.P("""
                        L’augmentation de l’importance de la majorité des motivations semble aller de pair avec celle de l’assiduité aux offices religieux. La corrélation la plus forte était avec les obligations et les croyances religieuses, nettement plus importantes chez les personnes plus assidues, mais cette tendance était également vraie pour plusieurs autres motivations, comme le désir de prendre conscience de leurs points forts ou le bénévolat de membres de leur famille. Bien que la force de cette tendance était parfois faible, seul le bénévolat à l’appui d’une cause politique, environnementale ou sociale ne variait pas en fonction de l’assiduité. Comme dans le cas de l’éducation, de nombreuses variations selon la situation matrimoniale et d’emploi semblent principalement liées à l’âge ou à l’étape de la vie, et sans lien direct avec la situation d’emploi ou matrimoniale. Par exemple, les personnes non membres de la population active (qui sont plus susceptibles d’être très jeunes ou très âgées) étaient plus enclines à faire du bénévolat parce que leurs ami.e.s en faisaient ou pour réseauter ou rencontrer d’autres personnes, de même que les célibataires (qui ont tendance à être très jeunes) ou les personnes veuves (qui ont tendance à être très âgées). Au chapitre du statut d’immigration, les personnes nouvellement arrivées au Canada avaient nettement plus tendance à faire du bénévolat en raison de leurs croyances ou obligations religieuses et étaient relativement plus enclines à soutenir une cause particulière, à prendre conscience de leurs points forts et à réseauter et à rencontrer d’autres personnes.
                        """),
                        # Volunteer motivations by religious attendance graph
                        # dcc.Graph(id='ActivityVolRate-Labour', style={'marginTop': marginTop}),
                        # Volunteer motivations by marital status graph
                        # dcc.Graph(id='ActivityVolRate-ImmStat', style={'marginTop': marginTop}),
                        # Volunteer motivations by labour force status graph
                        # dcc.Graph(id='ActivityVolRate-ImmStat', style={'marginTop': marginTop}),
                        # Volunteer motivations by immigration status graph
                        # dcc.Graph(id='ActivityVolRate-ImmStat', style={'marginTop': marginTop}),
                    ]),
                        
                    # Causes supported
                    html.Div([
                        html.H3("Causes soutenues "),
                        html.P("""
                        Le graphique ci-dessous montre les pourcentages de bénévoles qui ont fait état de chaque motivation, subdivisés en fonction de leur bénévolat ou de leur absence de bénévolat pour la cause particulière sélectionnée. À l’échelle nationale, plusieurs associations se constatent. Par exemple, les bénévoles des organismes du secteur de la santé et des hôpitaux étaient nettement plus susceptibles de déclarer être touchés personnellement par la cause de l’organisme ou de connaître une personne qui l’était. Les bénévoles des organismes religieux étaient particulièrement enclins à être motivés par leurs convictions religieuses, par le fait qu’un membre de leur famille faisait du bénévolat et par le désir de prendre conscience de leurs points forts et de mettre leurs compétences au service d’une cause digne de leur soutien. Les bénévoles des organismes de protection de l’environnement, des organismes du développement international et de l’aide internationale, ainsi que des organismes de plaidoyer étaient tous particulièrement susceptibles de déclarer faire du bénévolat pour soutenir une cause politique, environnementale ou sociale. 
                        """),
                        # Percentages of cause supporters and non-supporters reporting each motivation, by cause graph
                        # dcc.Graph(id='ActivityVolRate-Labour', style={'marginTop': marginTop}),
                            
                            
                        # html.Div(['Select status:',
                        #               dcc.Dropdown(
                        #                   id='status-selection1',
                        #                   options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                        #                   value='Marital status',
                        #                   style={'verticalAlign': 'middle'}
                        #               ),],
                        #              style={'width': '50%', 'display': 'inline-block'}),
                        html.Div([
                            # html.H6("Donation rate & average donation amount by immigration status"),
                            dcc.Graph(id='DonRateAvgDonAmt-other_13', style={'marginTop': marginTop}),
                            #html.P("Overall, those who were married or in a common-law relationship accounted to a significantly higher fraction of total donations than their numbers would suggest, as did New Canadians and, to a more modest extent, those who were employed."),
                            html.Br(),
                        ]),
                        # html.Div(['Select status:',
                        #               dcc.Dropdown(
                        #                   id='status-selection2',
                        #                   options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                        #                   value='Marital status',
                        #                   style={'verticalAlign': 'middle'}
                        #               ),],
                        #              style={'width': '50%', 'display': 'inline-block'}),
                        html.Div([
                            # html.H6("Percentage of donors & total donation value by immigration status"),
                            dcc.Graph(id='PercDon-other_13', style={'marginTop': marginTop}),
                            html.Br(),
                            # html.P("The degree to which Canadians focus on the primary cause they support does not seem to vary significantly according to their marital or labour force status. Married, widowed, and to a certain extent divorced Canadians tend to support a somewhat wider range of causes, as do those who are not in the labour force. Turning to immigration status, New Canadians and those residing in Canada who have not yet obtained landed immigrant status tend to focus more of their support on the primary cause and to support fewer causes than do native-born Canadians."),
                        ]),
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'

            ),
        ]),
]),
footer
]) 


################## CALLBACKS ##################

# @app.callback(

#     dash.dependencies.Output('DonRateAvgDonAmt-Cause-2', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):

#     dff1 = SubSecVolRates_2018[SubSecVolRates_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == "All"]
#     dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")
#     # name1 = "Volunteer rate"
#     name1 = "Taux de bénévolat"

#     dff2 = SubSecAvgHrs_2018[SubSecAvgHrs_2018['Region'] == region]
#     dff2 = dff2[dff2['Group'] == "All"]
#     dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
#     # name2 = "Average hours"
#     name2 = "Nombre d'heures moyen"

#     title = '{}, {}'.format("Niveaux de soutien par cause", region)

#     return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)


# @app.callback(

#     dash.dependencies.Output('AllocationSupport-Cause-2', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):

#     dff = AllocationVol_2018[AllocationVol_2018['Region'] == region]
#     title = '{}, {}'.format("Répartition du soutien par cause", region)

#     return single_vertical_percentage_graph(dff, title, by="QuestionText", sort=True)
