# App layout file for GV_AR_2018_FR converted from GAV0305_fr.py

from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app
from ..layout_utils import gen_home_button, gen_navbar, footer
from .callbacks import register_callbacks
from .data_processing import *

register_callbacks(app)


marginTop = 20
home_button = gen_home_button()
navbar = gen_navbar(
    "giving_and_volunteering_for_arts_and_recreation_organizations_2018")

layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1(
                            'Dons et bénévolat pour les organismes des arts et des loisirs (2018)'),
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
    dbc.Container([
        dbc.Row([
            html.Div([
                # html.H3('Giving'),
                dcc.Markdown("""
                    En plus de mesurer l’importance générale des dons et du bénévolat à divers niveaux, l’Enquête sociale générale sur les dons, le bénévolat et la participation mesure l’importance des niveaux de soutien pour 15 types de causes (appelées communément « domaines d’activité »), dont les arts et les loisirs. Selon la définition de l’Enquête, la catégorie des arts et loisirs se compose de deux sous-catégories. Les organismes des arts et de la culture se consacrent aux arts visuels, aux arts plastiques et aux arts de la scène et comprennent les sociétés historiques et humanistes, les musées, les zoos et les aquariums et les organisations du secteur des médias et des communications. Les organismes des sports et des loisirs sont axés sur le sport amateur et le conditionnement physique et comprennent les clubs d’activités de loisirs et sociaux, les organismes spécialisés dans les installations de sport et loisirs et leur entretien et les clubs de service.
                    """),
                dcc.Markdown("""
                    Nous analysons ci-dessous les tendances des dons et du bénévolat au bénéfice de ces organismes. Nous décrivons dans le texte ci-dessous les résultats au niveau national et, pour obtenir des précisions, vous pourrez utiliser le menu déroulant lié aux visualisations de données interactives pour afficher les résultats au niveau régional. Bien que les caractéristiques régionales puissent différer des résultats au niveau national décrits dans le texte, les tendances générales étaient très similaires.
                    """),
                html.H4('Montants des dons'),
                dcc.Markdown("""
                    À l’échelle nationale, un peu plus d’une personne sur sept (14 %) au Canada a fait au moins un don à un organisme des arts, de la culture et des loisirs pendant la période d’une année qui a précédé l’Enquête, ce qui place les arts, la culture et les loisirs au quatrième rang des causes les plus soutenues au Canada. Sur le plan des deux sous-causes, environ une personne sur dix au Canada a donné de l’argent aux organismes des sports et des loisirs et un peu moins d’une sur trente aux organismes des arts et de la culture (moins de 1 % d’entre elles ont donné aux deux sous-causes). Malgré leur base de donateur.trice.s relativement large, les organismes des arts et des loisirs ont reçu seulement environ 4 % de la valeur totale des dons, répartis à raison d’environ 60 % pour les organismes des sports et des loisirs et de 40 % pour les organismes des arts et de la culture. Bien que les organismes des arts et de la culture représentaient une proportion inférieure de la valeur totale des dons, leurs donateur.trice.s étaient très engagé.e.s, le montant moyen de leurs dons étant près de deux fois et demie supérieur à celui des dons au bénéfice des organismes des sports et des loisirs. Par comparaison avec les niveaux de soutien caractéristiques des autres causes, les donateur.trice.s des arts et de la culture se classaient parmi les partisan.e.s les plus engagé.es, tandis que les donateur.trice.s des sports et des loisirs faisaient partie des partisan.e.s les moins engagé.e.s.
                    """),
                # Donation rate and average donation amount by cause
                dcc.Graph(
                    id='ArtRecDonRateAvgDon', style={
                        'marginTop': marginTop}),
            ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Qui donne de l’argent'),
                dcc.Markdown("""
                    Certaines personnes sont plus enclines que d’autres à donner aux organismes des arts et des loisirs. À l’échelle nationale, la probabilité de donner augmente avec le niveau d’éducation formelle et avec l’âge, jusqu’à 55 à 64 ans, puis baisse légèrement. Les personnes nées au Canada et celles au revenu du ménage égal ou supérieur à 100 000 $ se distinguent en ayant légèrement plus tendance à donner, tandis que les personnes célibataires ou ne s’étant jamais mariées ont moins tendance à donner à ces organismes.
                    """
                             ),
                html.Div([
                    html.Div(['Sélectionnez un catégorie démographique:',
                             dcc.Dropdown(
                                 id='demo-selection-don',
                                 options=[{'label': demo_names[i], 'value': demo_names[i]}
                                          for i in range(len(demo_names))],
                                 value='Groupe d\'âge',
                                 style={'verticalAlign': 'middle'}
                             ), ],
                             style={'width': '33%', 'display': 'inline-block'})
                ]),
                # Donation rate by key demographic characteristics
                dcc.Graph(
                    id="ArtRecDonRateDemo_fr", style={
                        'marginTop': marginTop})
            ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # html.Div([
            #     html.H4('Support for Other Organization Types'),
            #     # Rates of donating to other causes
            #     dcc.Graph(id='ArtRecDonsCauses', style={'marginTop': marginTop}),
            #     ], className='col-md-10 col-lg-8 mx-auto'
            # ),
            html.Div([
                html.H4('Méthodes de dons'),
                dcc.Markdown("""
                    On a demandé aux répondant.e.s à l’Enquête si l’un ou plusieurs de 13 types de sollicitations différents les conduisaient à donner. Bien que l’Enquête ne lie pas directement ces méthodes aux causes soutenues, la comparaison entre les donateur.trice.s au bénéfice des arts et des loisirs et les autres (c.-à-d. les personnes qui ne soutenaient que d’autres causes) permet de comprendre comment les personnes ont tendance à soutenir financièrement cette catégorie d’organismes. À l’échelle nationale, ces dernières sont particulièrement enclines à donner à la suite de leur sollicitation dans un lieu public (par exemple, dans la rue ou dans un centre commercial), en achetant un billet à un événement de bienfaisance, en parrainant quelqu’un ou à la suite de leur sollicitation à leur lieu de travail. Ces personnes ne sont pas particulièrement plus susceptibles de donner dans un lieu de culte ou par d’autres méthodes non mentionnées expressément dans le questionnaire de l’Enquête.
                    """),
                # Donation rate by method
                dcc.Graph(id='ArtRecDonsMeth', style={'marginTop': marginTop}),
            ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Motivations des dons'),
                dcc.Markdown("""
                    On a demandé aux répondant.e.s à l’Enquête si huit facteurs potentiels jouaient un rôle important dans leurs décisions de donner. Là encore, bien qu’il n’existe aucun lien direct entre les motivations et les causes soutenues, la comparaison des personnes qui donnent aux organismes des arts et des loisirs et de celles qui donnent aux autres organismes permet de comprendre les raisons de leur soutien de cette catégorie d’organismes. À l’échelle nationale, ces personnes ont nettement plus tendance à donner après avoir été sollicitées par une personne de leur connaissance, pour contribuer à la collectivité et parce que la cause les touche personnellement. Les croyances spirituelles et religieuses et les crédits d’impôt éventuels ne semblent pas constituer des facteurs de motivation particulièrement importants.
                    """),
                # Motivations for donating
                dcc.Graph(
                    id='ArtRecMotivations', style={
                        'marginTop': marginTop}),
            ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Freins aux dons'),
                html.P("""
                    Afin de mieux comprendre les facteurs qui peuvent dissuader de donner, on a demandé aux donateur.trice.s si dix freins potentiels les empêchent de donner plus. À l’échelle nationale, les différences plus importantes qui caractérisent les donateur.trice.s des arts et des loisirs sont leur tendance supérieure à donner directement aux personnes dans le besoin au lieu de passer par un organisme, à ne pas aimer les méthodes de sollicitation et à penser avoir déjà donné assez. Ces personnes sont légèrement moins susceptibles de ne pas savoir où s’adresser pour faire des dons supplémentaires.
                    """
                       ),
                # Barriers to donating more
                dcc.Graph(id='ArtRecBarriers', style={'marginTop': marginTop}),
            ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
        dbc.Row([
            html.Div([
                html.H4("Niveaux de bénévolat"),
                html.P("""
                        À l’échelle nationale, environ une personne sur huit (12 %) au Canada a fait du bénévolat pour un organisme des arts et des loisirs, ce place les arts et les loisirs en tête des causes les plus soutenues au Canada, devant les services sociaux, l’éducation et la recherche (9 %), la santé (9 %) et la religion. Sur le plan des deux sous-causes, les personnes sont environ trois fois plus susceptibles de faire du bénévolat pour les organismes des sports et des loisirs que pour les organismes des arts et de la culture, bien qu’elles aient tendance à faire quasiment don du même nombre d’heures de bénévolat aux deux sous-causes. À l’échelle nationale, les organismes des arts et des loisirs représentent la proportion la plus importante du total des heures de bénévolat (23 %), devant les organismes de services sociaux (18 %), les organismes religieux (16 %), les organismes d’éducation et de recherche (9 %) et les organismes de santé (9 %).
                        """),
                # Volunteer rate and average hours volunteered by cause
                dcc.Graph(
                    id='ArtReVolRateAvgHrs', style={
                        'marginTop': marginTop}),
            ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4("Qui fait du bénévolat"),
                html.P("""
                        Dans l’ensemble, la probabilité de faire du bénévolat pour les organismes des arts et des loisirs ne varie pas beaucoup selon les caractéristiques personnelles et économiques. À l’échelle nationale, les personnes au niveau d’éducation formelle supérieur ont relativement plus tendance à faire du bénévolat pour ces organismes, de même que les membres des ménages au revenu supérieur et les personnes nées au Canada.
                        """),
                html.Div([
                    html.Div(['Sélectionnez un catégorie démographique:',
                             dcc.Dropdown(
                                 id='demo-selection-vol',
                                 options=[{'label': demo_names[i], 'value': demo_names[i]}
                                          for i in range(len(demo_names))],
                                 value='Groupe d\'âge',
                                 style={'verticalAlign': 'middle'}
                             ), ],
                             style={'width': '33%', 'display': 'inline-block'})
                ]),
                # Volunteer rate by key demographic characteristics
                dcc.Graph(
                    id="ArtRecVolRateDemo_fr", style={
                        'marginTop': marginTop})
            ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # html.Div([
            #     html.H4('Support for other organization types'),
            #     # Rates of volunteering for other causes
            #     dcc.Graph(id='ArtRecHrsCauses', style={'marginTop': marginTop}),
            #     ], className='col-md-10 col-lg-8 mx-auto'
            # ),
            html.Div([
                html.H4("Activités des bénévoles"),
                html.P("""
                        On a demandé aux personnes si, parmi 14 types d’activité différents, elles participaient à 1 ou plusieurs d’entre elles pour un organisme. Bien que l’Enquête ne lie pas précisément les activités aux types d’organismes soutenus, la comparaison des bénévoles des organismes des arts et des loisirs et des bénévoles des autres organismes permet de comprendre des activité des bénévoles pour cette catégorie d’organismes. À l’échelle nationale, les bénévoles des arts et des loisirs ont relativement tendance à participer à plusieurs activités, plus particulièrement à l’entraînement et à l’arbitrage dans le cadre sportif, à l’organisation d’activités ou d’événements, aux collectes de fonds et à être membres d’un comité ou d’un conseil d’administration. Leur participation à la plupart des autres activités est plus ou moins analogue à celle des autres bénévoles.
                        """),
                # Volunteer rate by activity
                dcc.Graph(
                    id='ArtRecVolActivity', style={
                        'marginTop': marginTop}),
            ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4("Motivations du bénévolat"),
                html.P("""
                        On a demandé aux répondant.e.s si douze facteurs potentiels jouaient un rôle important dans leur décision de faire don de leur temps. Contrairement à de nombreux autres domaines de l’Enquête, ces motivations sont liées précisément au bénévolat au bénéfice de causes particulières. À l’échelle nationale, les bénévoles des arts et des loisirs sont légèrement plus enclins à faire du bénévolat pour mettre en application leurs compétences et parce que leurs amis sont des bénévoles. Ces personnes sont nettement moins enclines à faire du bénévolat en raison de croyances religieuses ou spirituelles et légèrement moins enclines à chercher à soutenir une cause politique ou sociale ou à améliorer leurs possibilités d’emploi.
                        """),
                # Motivations for volunteering
                dcc.Graph(
                    id='ArtRecVolMotivations', style={
                        'marginTop': marginTop}),
            ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4("Freins au bénévolat"),
                html.P("""
                        On a demandé aux bénévoles si douze freins potentiels les avaient empêchés de faire don de plus de temps pendant l’année précédente. Bien que les freins ne soient pas liés directement aux causes soutenues, la comparaison des bénévoles des organismes des arts et des loisirs et de ceux des autres organismes apporte une information importante sur les facteurs qui peuvent importer particulièrement à ces bénévoles. À l’échelle nationale, les bénévoles des arts et des loisirs ont plus tendance à limiter leur bénévolat en pensant avoir déjà fait don d’assez de temps et ont légèrement plus tendance à n’avoir aucun intérêt pour faire plus de bénévolat. Ces personnes sont moins enclines à donner de l’argent de préférence à faire plus de bénévolat.
                        """),
                # Barriers to volunteering more
                dcc.Graph(
                    id='ArtRecVolBarriers', style={
                        'marginTop': marginTop}),
            ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
    ]),
    footer
])
