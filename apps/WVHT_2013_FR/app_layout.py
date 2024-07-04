# App layout file for WVHT_2013_FR converted from WVA020113_fr.py

from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app
from ..layout_utils import gen_home_button, gen_navbar, footer
from .callbacks import register_callbacks
from .data_processing import *
from .graphs import static_graph

register_callbacks(app)

navbar = gen_navbar("who_volunteers_and_how_much_time_do_they_contribute_2013")

marginTop = 20
home_button = gen_home_button(is_2013=True, sat_link=False, bc_link=False)
# home_button = gen_home_button()

layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1(
                            "Qui sont les bénévoles et combien d'heures donnent-ils? (2013)"),
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
                    html.Br(),
                ], className="m-2 p-2"),
            ), id='sticky-dropdown'),
    ], className='sticky-top select-region mb-2', fluid=True),
    dbc.Container(
        dbc.Row([
            html.Div(
                [
                    dcc.Markdown("""
                    D’après l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2013, près de neuf personnes sur dix (85 %) au Canada ont fait don de leur temps pour une forme ou une autre d’activité prosociale pendant la période d’un an qui l’a précédée. Plus de deux cinquièmes des personnes au Canada (44 %) étaient des bénévoles encadrés, qui faisaient don de leur temps à des organismes de bienfaisance ou à but non lucratif, et environ quatre cinquièmes des personnes (82 %) étaient des bénévoles non encadrés, qui faisaient directement don de leur temps à des personnes dans le besoin non membre de leur ménage, et ce, en dehors d’un organisme. À l’échelle nationale, les bénévoles encadrés ont fait chacun don de 154 heures en moyenne, soit, au total, 2,0 milliards d’heures de bénévolat au bénéfice des organismes de bienfaisance et sans but lucratif équivalant à environ 1,0 million d’emplois à temps plein.
                    """),
                    # Forms of volunteering
                    dcc.Graph(
                        id='FormsVolunteering_13', style={
                            'marginTop': marginTop}),
                    dcc.Markdown("""
                    La probabilité de faire du bénévolat pour un organisme de bienfaisance ou à but non lucratif variait selon le lieu de résidence des bénévoles. Pour la majorité des provinces, la proportion de bénévoles se situait à la norme nationale ou légèrement au-dessus de celle-ci. Elle était nettement supérieure à la norme dans la Saskatchewan et au Manitoba et nettement inférieure à la norme au Québec. Pour la majorité des provinces, le nombre moyen d’heures de bénévolat ne s’écartait pas de manière significative de la norme nationale, à l’exception notable du Québec.
                    """),
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
                    html.P("""
                        En plus des variations selon le lieu de résidence, le bénévolat encadré avait également tendance à varier selon les caractéristiques personnelles et économiques des bénévoles. Nous examinons ci-dessous l’association entre certaines de ces caractéristiques et les mesures clés du bénévolat:
                    """),
                    html.Ul([
                        html.Li(
                            'la probabilité de faire du bénévolat et le nombre moyen d’heures de bénévolat par personne; '),
                        html.Li(
                            'les pourcentages de la population canadienne et le nombre total d’heures de bénévolat pour chaque sous-groupe. '),
                    ]),

                    html.P("""
                        À elles toutes, ces mesures brossent un tableau détaillé du bassin de bénévoles et fournissent un aperçu de la concentration générale du soutien bénévole des organismes de bienfaisance et à but non lucratif. Dans le texte, nous décrivons les résultats au niveau national et, pour obtenir des précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer des résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.
                    """),
                    html.Div([
                        html.H4("Genre"),
                        html.P("""
                        Au niveau national, les femmes étaient légèrement plus enclines à faire du bénévolat que les hommes (respectivement 45 % et 42 %), bien que les hommes aient légèrement plus tendance à faire don de plus d’heures quand ils faisaient du bénévolat.
                        """),
                        # Barriers to giving more by gender
                        html.Div([
                            dcc.Graph(
                                id='VolRateAvgHours-Gndr_13',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                        dcc.Markdown("""
                    Dans l’ensemble, les pourcentages du nombre total d’heures de bénévolat des hommes et des femmes étaient très comparables à leur représentation au sein de la population (c.-à-d. que le nombre d’heures de bénévolat de l’un ou l’autre genre n’était pas nettement plus ou moins élevé par rapport à son nombre).
                    """),
                        # Percentage of Canadians & total hours volunteered by
                        # gender
                        html.Div([
                            dcc.Graph(
                                id='PercVolHours-Gndr_13',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Âge"),
                        html.P("""
                        Les personnes plus jeunes et d’âge moyen étaient les plus susceptibles de faire du bénévolat, surtout celles âgées de 15 à 24 ans. Après l’âge de 65 ans, la probabilité de faire du bénévolat chutait fortement. Quant aux heures de bénévolat caractéristiques, les personnes de moins de 55 ans avaient tendance à faire don de moins d’heures.
                        """),
                        # Volunteer rate & average hours volunteered by age
                        html.Div([
                            dcc.Graph(
                                id='VolRateAvgHours-Age_13',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                        dcc.Markdown("""
                    Étant donné leur tendance à faire don de moins d’heures, les bénévoles âgés de 24 à 44 ans représentaient moins d’heures que leur représentation au sein de la population ne le donnait à penser. En revanche, les bénévoles âgés de 55 à 74 ans représentaient des pourcentages du nombre total d’heures excessivement élevés compte tenu de leur nombre..
                    """),
                        # Percentage of Canadians & total hours volunteered by
                        # age
                        html.Div([
                            dcc.Graph(
                                id='PercVolHours-Age_13',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # Formal Education
                    html.Div([
                        html.H5("Éducation formelle"),
                        html.P("""
                        La probabilité de faire du bénévolat avait tendance à augmenter en allant de pair avec les niveaux d’études supérieurs au diplôme d’études secondaires, les titulaires d’un diplôme universitaire étant enclins à faire don d’un nombre d’heures relativement plus élevé que les autres.
                        """),
                        # Volunteer rate & average hours volunteered by formal
                        # education
                        html.Div([
                            dcc.Graph(
                                id='VolRateAvgHours-Educ_13',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                        dcc.Markdown("""
                    À l’échelle nationale, les bénévoles titulaires d’un diplôme d’études secondaires faisaient don d’un nombre d’heures légèrement inférieur à leur représentation au sein de la population, tandis que les bénévoles titulaires d’un diplôme universitaire faisaient don d’un nombre d’heures relativement supérieur à celui auquel on pourrait s’attendre.
                    """),
                        # Percentage of Canadians & total hours volunteered by
                        # formal education
                        html.Div([
                            dcc.Graph(
                                id='PercVolHours-Educ_13',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # Marital status
                    html.Div([
                        html.H5("Situation matrimoniale"),
                        html.P("""
                        Les personnes célibataires et mariées étaient les plus enclines à faire du bénévolat, contrairement aux personnes veuves. Ces dernières avaient tendance à faire don d’un plus grand nombre d’heures quand elles faisaient du bénévolat, tandis que les célibataires en faisaient souvent relativement moins.
                        """),
                        # Volunteer rate & average hours volunteered by marital
                        # status
                        html.Div([
                            dcc.Graph(
                                id='VolRateAvgHours-MarStat_13',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                        dcc.Markdown("""
                    Les variations de la probabilité de faire du bénévolat et des heures de bénévolat caractéristiques se compensaient presque totalement, ce qui veut dire que chaque groupe représentait presque exactement la proportion des heures de bénévolat à laquelle on pourrait s’attendre, étant donné leur nombre respectif au sein de la population canadienne.
                    """),
                        # Percentage of  Canadians & total hours volunteered by
                        # marital status
                        html.Div([
                            dcc.Graph(
                                id='PercVolHours-MarStat_13',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # household income
                    html.Div([
                        html.H5("Revenu"),
                        html.P("""
                        D’une façon très générale, la probabilité de faire du bénévolat avait tendance à augmenter avec le revenu du ménage, tandis que le nombre d’heures de bénévolat des ménages au revenu égal ou supérieur à 120 000 $ avait tendance à être inférieur.
                        """),
                        # Volunteer rate & average hours volunteered by
                        # household income
                        html.Div([
                            dcc.Graph(
                                id='VolRateAvgHours-Inc_13',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                        dcc.Markdown("""
                    Dans l’ensemble, chaque groupe de revenu représentait à peu près la même proportion du nombre total d’heures de bénévolat que sa proportion au sein de la population canadienne (c.-à-d. aucun groupe ne se distingue en faisant don de nettement plus ou moins d’heures par rapport à son nombre).
                    """),
                        # Percentage of Canadians & total hours volunteered by
                        # household income
                        html.Div([
                            dcc.Graph(
                                id='PercVolHours-Inc_fr',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # Religious attendance
                    html.Div([
                        html.H5("Pratique religieuse"),
                        html.P("""
                        La probabilité de faire du bénévolat avait tendance à augmenter avec l’assiduité aux offices religieux. À l’exception des personnes qui assistaient aux services une fois par semaine (enclines à faire don de beaucoup plus de temps), les bénévoles avaient tendance à faire don d’un nombre d’heures relativement uniforme.
                        """),
                        # Volunteer rate & average hours volunteered by
                        # religious attendance
                        html.Div([
                            dcc.Graph(id='VolRateAvgHours-Relig_13',
                                      style={'marginTop': marginTop}),
                        ]),
                        dcc.Markdown("""
                    Étant donné leur taux de bénévolat supérieur et le nombre d’heures de bénévolat significativement plus important dont elles avaient tendance à faire don, les personnes présentes chaque semaine aux offices religieux représentaient une proportion des heures de bénévolat très supérieure à leur représentation au sein de la population. Les personnes qui n’assistaient pas aux services religieux représentaient une proportion des heures de bénévolat significativement inférieure à celle que leur nombre permettait de présager.
                    """),
                        # Percentage of Canadians & total hours volunteered by
                        # religious attendance
                        html.Div([
                            dcc.Graph(
                                id='PercVolHours-Relig_13',
                                style={
                                    'marginTop': marginTop}),
                        ]),
                    ]),
                    # Other personal & economic characteristics
                    html.Div([
                        html.H5("Autres facteurs"),
                        dcc.Markdown("""
                    Étant donné leur taux de bénévolat supérieur et le nombre d’heures de bénévolat significativement plus important dont elles avaient tendance à faire don, les personnes présentes chaque semaine aux offices religieux représentaient une proportion des heures de bénévolat très supérieure à leur représentation au sein de la population. Les personnes qui n’assistaient pas aux services religieux représentaient une proportion des heures de bénévolat significativement inférieure à celle que leur nombre permettait de présager.
                    """),
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
                            id='status-hours_13',
                            style={
                                'marginTop': marginTop}),

                        # html.Div([
                        #     dcc.Graph(id='VolRateAvgHours-Labour', style={'marginTop': marginTop}),
                        # ]),
                        # # Volunteer rate & average hours volunteered by immigration status
                        # html.Div([
                        #     dcc.Graph(id='VolRateAvgHours-ImmStat', style={'marginTop': marginTop}),
                        # ]),
                        # html.P("Dans l’ensemble, les personnes qui ne font pas partie de la population active et les personnes nées au Canada ont tendance à représenter un nombre d’heures proportionnellement supérieur, tandis que les personnes naturalisées et employées ont tendance à représenter un nombre d’heures proportionnellement inférieur."),
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
                        dcc.Graph(id='status-perc_13', style={'marginTop': marginTop})
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
    ),
    footer
])


#
