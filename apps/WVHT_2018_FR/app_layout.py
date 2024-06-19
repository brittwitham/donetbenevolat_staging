# App layout file for WVHT_2018_FR converted from
# Qui_sont_les_benevoles_et_combien_heures_donnent_ils_2018.py

from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app
from ..layout_utils import gen_home_button, gen_navbar, footer
from .callbacks import register_callbacks
from .data_processing import *
from .graphs import static_graph

register_callbacks(app)

navbar = gen_navbar("Who_volunteers_and_how_much_time_do_they_contribute_2018")
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
                        html.H1(
                            "Qui sont les bénévoles et combien d'heures donnent-ils?"),
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
                        options=[{'label': region_values[i], 'value': region_values[i]}
                                 for i in range(len(region_values))],
                        value='CA',
                    ),
                    html.Br()
                ], className="m-2 p-2"),
            ), id='sticky-dropdown'),
    ], className='sticky-top select-region mb-2', fluid=True),
    dbc.Container(
        dbc.Row([
            html.Div(
                [
                    dcc.Markdown('''
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, près de huit personnes sur dix (79 %) au Canada ont fait don de leur temps au service d’une forme ou d’une autre d’activité prosociale pendant la période d’un an qui l’a précédée. Un peu plus de deux cinquièmes de ces personnes étaient des bénévoles encadrés, qui faisaient don de leur temps à des organismes de bienfaisance ou à but non lucratif, et environ trois quarts d’entre elles étaient des bénévoles non encadrés, qui faisaient directement don de leur temps à des personnes dans le besoin non membre de leur ménage, et ce, en dehors d’un organisme. À l’échelle nationale, les bénévoles encadrés ont fait don de 131 heures en moyenne par personne, soit, au total, un peu moins de 1,7 milliard d’heures de bénévolat par an, au bénéfice des organismes de bienfaisance et sans but lucratif.
                    ''', className='mt-4'),
                    # Forms of volunteering
                    dcc.Graph(
                        id='FormsVolunteering', style={
                            'marginTop': marginTop}),
                    dcc.Markdown('''
                    La probabilité de faire du bénévolat pour un organisme de bienfaisance ou à but non lucratif varie selon le lieu de résidence des bénévoles. Pour la majorité des provinces, la proportion de bénévoles se situe à la norme nationale ou légèrement au-dessus de celle-ci. Elle est nettement supérieure à la norme nationale dans la Saskatchewan et nettement inférieure à celle-ci au Québec. Bien que le nombre d’heures de bénévolat habituel varie selon les provinces, ces variations ne généralement pas suffisantes pour être statistiquement significatives.
                    '''),
                    # Volunteer rate & average hours volunteered by province
                    dcc.Graph(
                        id='VolRateAvgHours-prv',
                        figure=static_graph(
                            VolRate_2018,
                            AvgTotHours_2018),
                        style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Personal & economic characteristics
            html.Div(
                [
                    html.H3('Caractéristiques personnelles et économiques'),
                    html.P("En plus des variations selon le lieu de résidence, les tendances du bénévolat encadré varient aussi généralement selon les caractéristiques personnelles et économiques des bénévoles. Nous examinons ci-dessous l’association entre certaines de ces caractéristiques et les mesures clés du bénévolat:"),
                    html.Ul([
                        html.Li(
                            'la probabilité de faire du bénévolat et le nombre moyen d’heures de bénévolat par personne;'),
                        html.Li(
                            'les pourcentages de la population canadienne et le nombre total d’heures de bénévolat pour chaque sous-groupe.'),

                    ]),
                    html.Div([
                        html.P("À elles toutes, ces mesures brossent un tableau détaillé du bassin de bénévoles et fournissent un aperçu de la concentration générale du soutien bénévole des organismes de bienfaisance et à but non lucratif. Nous décrivons dans le texte les résultats au niveau national et, pour obtenir des précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer des résultats au niveau national décrits dans le texte, les tendances générales sont très similaires."),
                    ]),
                    html.Div([
                        html.H5("Genre"),
                        html.P(
                            "Au niveau national, les femmes sont plus enclines que les hommes à faire du bénévolat et ont tendance à faire don de légèrement plus d’heures."),
                        # Barriers to giving more by gender
                        html.Div([
                            dcc.Graph(
                                id='VolRateAvgHours-Gndr',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                        html.P("En raison de leur plus grande probabilité de faire du bénévolat et de leur tendance à faire don d’un plus grand nombre d’heures de bénévolat, le pourcentage des heures de bénévolat des femmes est nettement supérieur à celui que leur nombre donne à penser (57 % des heures de bénévolat par rapport à 51 % de la population au niveau national)."),
                        # Percentage of Canadians & total hours volunteered by
                        # gender
                        html.Div([
                            dcc.Graph(
                                id='PercVolHours-Gndr',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("La probabilité de faire du bénévolat varie selon l’âge et le stade de la vie. Bien que les personnes âgées de 15 à 24 ans soient les plus susceptibles de faire du bénévolat, la probabilité de faire du bénévolat chute fortement chez les personnes à la fin de la vingtaine et au début de la trentaine. Cette probabilité culmine à nouveau à la mi-trentaine avant de décliner plus tard dans la vie. Cette baisse de la probabilité de faire du bénévolat est compensée par la tendance des bénévoles plus âgés à faire don de plus d’heures."),
                        # Volunteer rate & average hours volunteered by age
                        html.Div([
                            dcc.Graph(
                                id='VolRateAvgHours-Age',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                        html.P("Les personnes de moins de 45 ans représentent une proportion du total des heures de bénévolat inférieure à celle que leurs nombres donnent à penser. Étant donné leur tendance à faire don d’un grand nombre d’heures quand elles font du bénévolat, les personnes âgées de 65 ans et plus représentent des pourcentages du total des heures de bénévolat significativement supérieurs à ceux auxquels on pourrait s’attendre étant donné leurs nombres."),
                        # Percentage of Canadians & total hours volunteered by
                        # age
                        html.Div([
                            dcc.Graph(
                                id='PercVolHours-Age',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # Formal Education
                    html.Div([
                        html.H5("Éducation formelle"),
                        html.P("En général, à la fois la probabilité de faire du bénévolat et les heures dont les bénévoles font habituellement don augmentent avec le niveau d’études."),
                        # Volunteer rate & average hours volunteered by formal
                        # education
                        html.Div([
                            dcc.Graph(
                                id='VolRateAvgHours-Educ',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                        html.P("À l’échelle nationale, les bénévoles titulaires du diplôme d’études secondaires ou au niveau d’études inférieur font don d’un nombre d’heures légèrement inférieur à celui auquel on pourrait s’attendre étant donné leur représentation au sein de la population, tandis que les personnes titulaires d’un diplôme universitaire font don d’un nombre d’heures nettement."),
                        # Percentage of Canadians & total hours volunteered by
                        # formal education
                        html.Div([
                            dcc.Graph(
                                id='PercVolHours-Educ',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # Marital status
                    html.Div([
                        html.H5("Situation matrimoniale"),
                        html.P("Dans l’ensemble, les personnes mariées, séparées, divorcées ou célibataires sont grosso modo tout aussi susceptibles les unes que les autres de faire du bénévolat, tandis que les personnes mariées ou célibataires ont tendance à faire don de légèrement moins d’heures quand elles font du bénévolat. Les personnes veuves sont nettement moins enclines à faire du bénévolat, mais ont tendance à faire don de beaucoup plus d’heures."),
                        # Volunteer rate & average hours volunteered by marital
                        # status
                        html.Div([
                            dcc.Graph(
                                id='VolRateAvgHours-MarStat',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                        html.P("Les personnes célibataires et qui ne sont jamais mariées représentent une proportion du total des heures de bénévolat légèrement inférieure à celle à laquelle on pourrait s’attendre, étant donné leur représentation au sein de la population. Les contributions des autres sous-groupes matrimoniaux correspondent largement à leurs nombres au sein de la population."),
                        # Percentage of  Canadians & total hours volunteered by
                        # marital status
                        html.Div([
                            dcc.Graph(
                                id='PercVolHours-MarStat',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # household income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("Bien que la probabilité de faire du bénévolat ait tendance à augmenter avec le revenu du ménage, le nombre d’heures de bénévolat habituel des ménages au revenu plus élevé est, en général, légèrement inférieur."),
                        # Volunteer rate & average hours volunteered by
                        # household income
                        html.Div([
                            dcc.Graph(
                                id='VolRateAvgHours-Inc',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                        html.P("Les deux tendances de l’augmentation de la probabilité de faire du bénévolat et de la diminution des heures de bénévolat qui vont de pair avec l’augmentation du revenu s’annulent l’une et l’autre presque totalement. Au niveau national du moins, chaque groupe de revenu représente une proportion du total des heures de bénévolat presque identique à sa représentation au sein de la population."),
                        # Percentage of Canadians & total hours volunteered by
                        # household income
                        html.Div([
                            dcc.Graph(
                                id='PercVolHours-Inc',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # Religious attendance
                    html.Div([
                        html.H5("Pratique religieuse"),
                        html.P("Dans l’ensemble, la probabilité de faire du bénévolat va de pair avec l’assiduité aux offices religieux. Les heures de bénévolat ont tendance à être relativement uniformes pour la majorité des catégories d’assiduité. Au niveau national du moins, l’exception majeure concerne les personnes qui assistent aux services au moins une fois par semaine : ces bénévoles ont tendance à faire don d’un nombre d’heures significativement supérieur à celui des personnes moins assidues ou qui n’assistent jamais aux offices religieux."),
                        # Volunteer rate & average hours volunteered by
                        # religious attendance
                        html.Div([
                            dcc.Graph(
                                id='VolRateAvgHours-Relig',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                        html.P("Les personnes qui assistent chaque semaine aux offices religieux représentent une proportion du total des heures de bénévolat très supérieure à celle à laquelle on pourrait s’attendre, étant donné leur représentation au sein de la population (29 % du total des heures par rapport à 14 % de la population nationale). Les personnes qui n’assistent jamais aux services religieux, en revanche, représentent une proportion des heures inférieure à leur représentation au sein de la population."),
                        # Percentage of Canadians & total hours volunteered by
                        # religious attendance
                        html.Div([
                            dcc.Graph(
                                id='PercVolHours-Relig',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # Other personal & economic characteristics
                    html.Div([
                        html.H5("Autres facteurs"),
                        html.P("La situation d’emploi et le statut d’immigration sont également des prédicteurs significatifs des tendances du bénévolat. En général, la probabilité de faire du bénévolat varie peu selon le statut d’emploi, mais les bénévoles qui ne font pas partie de la population active ont tendance à faire don de beaucoup plus d’heures. Quant au statut d’immigration, les personnes naturalisées (qui ont tendance à être plus âgées) sont légèrement moins susceptibles de faire du bénévolat que les personnes nées au Canada."),
                        # Volunteer rate & average hours volunteered by
                        # employment status

                        html.Div([
                            html.Div(['Select status:',
                                     dcc.Dropdown(
                                         id='status-selection2',
                                         options=[{'label': status_names[i], 'value': status_names[i]} for i in range(
                                             len(status_names))],
                                         value="Situation d'activité",
                                         style={'verticalAlign': 'middle'}
                                     ),],
                                     style={'width': '33%', 'display': 'inline-block'})
                        ]),
                        dcc.Graph(
                            id='status-hours',
                            style={
                                'marginTop': marginTop}),

                        # html.Div([
                        #     dcc.Graph(id='VolRateAvgHours-Labour', style={'marginTop': marginTop}),
                        # ]),
                        # # Volunteer rate & average hours volunteered by immigration status
                        # html.Div([
                        #     dcc.Graph(id='VolRateAvgHours-ImmStat', style={'marginTop': marginTop}),
                        # ]),
                        html.P("Dans l’ensemble, les personnes qui ne font pas partie de la population active et les personnes nées au Canada ont tendance à représenter un nombre d’heures proportionnellement supérieur, tandis que les personnes naturalisées et employées ont tendance à représenter un nombre d’heures proportionnellement inférieur."),
                        # Percentage of Canadians & total hours volunteered by employment status
                        # html.Div([
                        #     dcc.Graph(id='PercVolHours-Labour', style={'marginTop': marginTop})
                        # ]),
                        # # Percentage of Canadians & total hours volunteered by immigration status
                        # html.Div([
                        #     dcc.Graph(id='PercVolHours-ImmStat', style={'marginTop': marginTop})
                        # ]),
                        html.Div([
                            html.Div(['Sélectionner le statut:',
                                      dcc.Dropdown(
                                          id='status-selection',
                                          options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                                          value="Situation d'activité",
                                          style={'verticalAlign': 'middle'}
                                      ),],
                                     style={'width': '33%', 'display': 'inline-block'})
                        ]),
                        dcc.Graph(id='status-perc', style={'marginTop': marginTop})
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
    ),
    footer
])


#
