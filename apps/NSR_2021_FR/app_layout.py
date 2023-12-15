# App layout file for WVHT_2018_EN converted from
# Who_volunteers_and_how_much_time_do_they_contribute_2018.py

from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app
from ..layout_utils import gen_home_button, gen_navbar, footer
from .callbacks import register_callbacks
# from .data_processing import region_values, status_names, VolRate_2018, AvgTotHours_2018
# from .graphs import static_graph
from .graphs import fig_revSource_CA, fig_revGrowthSource

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

# TODO!
navbar = gen_navbar(
    "nonprofit_sector_revenue_2021")

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
                        html.H1(
                            'Revenus du secteur sans but lucratif'),
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
Globalement, le secteur à but non lucratif canadien a accumulé un peu plus de 325 milliards de dollars en 2021, soit la dernière année pour laquelle des données sont disponibles. À l’échelle nationale, un peu plus des trois cinquièmes du total des revenus ont été attribuées aux institutions gouvernementales à but non lucratif (hôpitaux, certains établissements de soins pour bénéficiaires internes, universités et collèges) et deux cinquièmes reviennent aux organismes du sous-secteur de base. Le ratio est d’environ 3:2 entre les organismes communautaires et les institutions commerciales à but non lucratif.
                           '''),
                    html.Sup(html.A('1', href='#footnote1', id="ref1")),
                    html.Br(),
                    html.Br(),
                    html.Span('''
Bien que la distribution relative des revenus par type d’organisme à but non lucratif et par sous-secteur soit plutôt constante entre les provinces et les territoires, il existe certaines variations. Par exemple, les institutions gouvernementales à but non lucratif représentent un pourcentage supérieur des revenus totaux à l’Île-du-Prince-Édouard et à Terre-Neuve-et-Labrador, mais leur rôle est nettement moins important au Nunavut, seule région où elles représentent une minorité des revenus du secteur sans but lucratif. De même, les organismes communautaires à but non lucratif enregistrent constamment des revenus plus élevés que les institutions commerciales à but non lucratif, sauf au Nouveau-Brunswick et à Terre-Neuve-et-Labrador.
                    ''', className='mt-4'),
                    # TODO: Add footnote
                    # Nonprofit revenue by sub sector
                    dcc.Graph(
                        id='revSubSec', style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H3('Tendances des revenus par type d’organisme à but non lucratif et par sous-secteur'),
                    dcc.Markdown('''
Depuis 2007, les revenus du secteur sans but lucratif ont augmenté d’environ 80 % en termes nominaux (c’est-à-dire non ajustés selon les effets de l’inflation). Les revenus des institutions commerciales à but non lucratif sont ceux qui ont le plus augmenté (près de 95 %), suivis des revenus des organismes communautaires et des institutions gouvernementales à but non lucratif (environ 80 % dans les deux cas). Bien que les revenus des institutions commerciales à but non lucratif soient ceux qui ont le plus augmenté, ils étaient également les plus volatiles. Ils ont effectivement augmenté plus rapidement que ceux des autres sous-secteurs entre 2007 et 2009, mais ont considérablement diminué en 2014, et encore plus modestement en 2020 en raison de la pandémie. Quant aux revenus des organismes communautaires à but non lucratif, ils étaient inférieurs à ceux des institutions gouvernementales à but non lucratif entre 2010 et 2017, mais ont dépassé ceux-ci de 2017 à 2020.
                    ''', className='mt-4'),
                    # Relative growth of revenues by sub secotr
                    dcc.Graph(
                        id='revGrowth', style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H3('Revenus par secteur d’activités'),
                    html.Span('''
Les organismes des domaines de la santé, de l’éducation, de la recherche et des services sociaux représentent les plus grandes proportions des revenus du secteur sans but lucratif.'''),
                    html.Sup(html.A('2', href='#footnote2', id="ref2")),
                    html.Span('''
                                 Environ deux tiers des revenus du sous-secteur gouvernemental reviennent aux organismes de santé, un quart appartient aux organismes d’éducation et de recherche, et le reste revient aux services sociaux. La majeure partie des revenus des organismes de santé, d’éducation et de recherche revient aux organismes du sous-secteur gouvernemental, alors que la majorité des revenus des organismes de services sociaux appartiennent aux organismes du secteur sans but lucratif de base (surtout les organismes communautaires à but non lucratif).

                    ''', className='mt-4'),
                    dcc.Markdown('''
En ce qui a trait aux revenus du sous-secteur de base, quatre cinquièmes des revenus reviennent aux organismes de quatre secteurs d’activités particuliers (associations commerciales, associations professionnelles et syndicats; services sociaux; culture, sports et loisirs; et éducation et recherche), ainsi qu’aux organismes des secteurs qui ne font pas partie d’un des onze autres secteurs d’activités. Des pourcentages plutôt faibles des revenus du sous-secteur de base se rapportent aux organismes des secteurs du droit, de la défense des intérêts, de la politique, de l’environnement, du développement international et de l’aide internationale.
                    '''),
                    dcc.Markdown('''
De façon générale, les données provinciales et territoriales concordent avec les tendances nationales.
                    '''),
                    # TODO: Add footnote
                    # NPercentage of nonprofit ervenues by sub sector and
                    # activity
                    dcc.Graph(
                        id='revSubSecActivity', style={
                            'marginTop': marginTop}
                    ),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H3('Tendances relatives aux revenus par secteur d’activités'),
                    dcc.Markdown('''
En ce qui a trait à la croissance des revenus par secteur d’activités, le taux de croissance le plus élevé depuis 2007 a été enregistré pour les organismes du sous-secteur de base qui offrent des services sociaux ou travaillent dans des secteurs qui n’appartiennent pas à un autre secteur d’activités défini. Les revenus de ces organismes ont plus que doublé en termes nominaux. Le taux de croissance des revenus le moins élevé dans le sous-secteur de base revient aux organismes environnementaux, aux intermédiaires philanthropiques, aux organismes religieux, et aux organismes de sports et loisirs. Les revenus de ces organismes ont augmenté de cinquante pour cent ou d’un peu moins. 
                    ''', className='mt-4'),
                    dcc.Markdown('''
Quant au sous-secteur gouvernemental, les revenus associés aux services de santé et sociaux ont presque doublé, beaucoup plus que dans le cas des organismes d’éducation et de recherche dont les revenus ont seulement augmenté d’un peu plus de cinquante pour cent. En général, le rythme de croissance de ces organismes s’est montré relativement constant, sauf depuis 2020 en raison du financement accru accordé aux organismes de santé en réaction à la pandémie. Dans le sous-secteur de base, les changements liés à la pandémie sont clairs dans le cas des organismes axés sur le développement, le logement, les loisirs et la culture.
                    '''),
                    # TODO: Add footnote
                    # Relative growth of revenues by core acitivty area
                    dcc.Graph(
                        id='revGrowthActivity_core', style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H3('Sources de revenus'),
                    dcc.Markdown('''
Chaque sous-secteur dépend d’une combinaison de sources de revenus. Comme on peut s’y attendre étant donné la façon dont les sous-secteurs sont définis, les institutions commerciales à but non lucratif dépendent grandement des revenus gagnés. En effet, la vente de biens et de services représente environ trois cinquièmes des revenus totaux au niveau national. Quant aux frais d’adhésion et aux cotisations, ils représentent un tiers des revenus totaux. En ce qui a trait aux organismes gouvernementaux à but non lucratif, environ trois quarts de leurs revenus proviennent du financement gouvernemental, et environ un cinquième est associé à la vente de biens et de services. Enfin, les organismes communautaires à but non lucratif ont les sources de revenus les plus variées. La majorité provient des revenus gagnés, surtout de la vente de biens et de services. S’ensuivent les frais d’adhésion, les cotisations et les investissements. Un peu plus du tiers provient du financement gouvernemental et un peu moins du tiers provient de dons de particuliers ou d’entreprises.
                    ''', className='mt-4'),
                    # TODO: Add footnote
                    # Revenues by source and subsector
                    # dcc.Graph(
                    #     figure = fig_revSource_CA,
                    #     id='revSource_ca', style={
                    #         'marginTop': marginTop}),
                    dcc.Graph(id='revSource'),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H3('Tendances relatives aux revenus par source et par sous-secteur'),
                    dcc.Markdown('''
Les moteurs de croissance associés aux revenus varient grandement entre les différents sous-secteurs. Comme on pouvait s’y attendre, le financement gouvernemental est le moteur de croissance le plus important dans le cas des institutions gouvernementales à but non lucratif (augmentation de 83 % en termes nominaux depuis 2007). Toutefois, il s’agit également d’un important moteur de croissance pour les organismes communautaires à but non lucratif (il a plus que doublé pendant la période donnée). Bien que ces deux sous-secteurs aient également enregistré des augmentations majeures en ce qui a trait à d’autres sources de revenus (revenus de placement des organismes communautaires à but non lucratif, et vente de biens et de services dans le cas des institutions gouvernementales à but non lucratif), ces sources ne représentent pas une importante proportion du financement, mais cela pourrait changer si la croissance se poursuit à ce rythme. 
                                 ''', className='mt-4'),
                    # TODO: Add footnote
                    # Relative grwoth of revenue sources by sub-sector
                    # dcc.Graph(
                    #     figure=fig_revGrowthSource,
                    #     id='revGrowthSource_ca', style={
                    #         'marginTop': marginTop}),
                    dcc.Graph(id='revGrowthSource')
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
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
                                        html.Em("sous-secteur sans but lucratif de base"),
                                        "  qui contraste avec le ",
                                        html.Em("sous-secteur des institutions gouvernementales à but non lucratif."), html.A(
                                            "↩︎", href="#fnref1", className="footnote-back", role="doc-backlink")
                                    ]
                                )
                            ], id="fn1"),
                        html.Li([
                            html.P("Outre le fait de diviser les organismes par type et par sous-secteur, le Compte satellite classe les organismes dans l’un des douze groupes suivants selon leur activité principale :"),
                            html.P(
                                [
                                    html.Em("Arts, culture et loisirs"),
                                    " - comprend les musées; les groupes et les institutions liés aux arts visuels, aux arts matériels et aux arts de la scène; les sociétés médiatiques, historiques et humanistes; et les groupes de sports et loisirs."]),
                            html.P(
                                [
                                    html.Em("Éducation et recherche"),
                                    " - organismes qui offrent et appuient des services d’éducation et de recherche. Les universités et les collèges font partie du sous-secteur gouvernemental."]),
                            html.P(
                                [
                                    html.Em("Santé"),
                                    " - organismes qui offrent et appuient des services de santé aux patients hospitalisés et externes. Les hôpitaux et les résidences pour personnes âgées font partie du sous-secteur gouvernemental."]),
                            html.P([html.Em("Services sociaux"), " - organismes qui proposent une grande variété de services à la personne non liés à la santé. Une minorité d’organismes de ce secteur d’activités font partie du sous-secteur gouvernemental selon l’influence que le gouvernement exerce sur eux."]),
                            html.P(
                                [
                                    html.Em("Environnement"),
                                    " -  organismes engagés dans la protection et la préservation de l’environnement, y compris le bien-être des animaux."]),
                            html.P(
                                [
                                    html.Em("Développement et logement"),
                                    " - organismes engagés dans le développement social, communautaire et économique, ainsi que l’offre de logement."]),
                            html.P(
                                [
                                    html.Em("Droit, défense des intérêts et politique"),
                                    " - organismes engagés dans la défense des intérêts ou la prestation de services juridiques et connexes, y compris la réadaptation des délinquants."]),
                            html.P(
                                [
                                    html.Em(
                                        "Intermédiaires philanthropiques et bénévolat"),
                                    " - fondations publiques et privées, et organismes qui promeuvent le bénévolat."]),
                            html.P(
                                [
                                    html.Em("International"),
                                    " - organismes engagés dans le développement international et l’aide internationale, y compris la promotion des droits de la personne et de la paix."]),
                            html.P(
                                [
                                    html.Em("Religion"),
                                    " - congrégations et associations de congrégations, y compris l’éducation religieuse."]),
                            html.P(
                                [
                                    html.Em(
                                        "Associations commerciales et professionnelles et syndicats"),
                                    "- organismes qui tentent de contrôler et de faire avancer les intérêts d’industries particulières ou de groupes particuliers de travailleurs."]),
                            html.P(
                                [
                                    html.Em("Autre"),
                                    " -  organismes qui ne font pas partie de ces secteurs d’activités.",
                                    html.A(
                                        "↩︎",
                                        href="#fnref2",
                                        className="footnote-back",
                                        role="doc-backlink")])
                        ], id="fn2")
                    ])
                ],
            )
        ]
        ),
    ),
    footer
])
