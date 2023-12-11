# App layout file for WVHT_2018_EN converted from
# Who_volunteers_and_how_much_time_do_they_contribute_2018.py

from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app
from ..layout_utils import gen_home_button, gen_navbar, footer
from .callbacks import register_callbacks
# from .data_processing import region_values, status_names, VolRate_2018, AvgTotHours_2018
from .graphs import fig_perNatGDP

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
    "economic_role_of_the_nonprofit_sector_2021")

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
                            'Rôle économique du secteur sans but lucratif'),
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
                    "Select a region:",
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
Le secteur sans but lucratif et de bienfaisance joue un rôle de premier plan dans l’économie canadienne. En 2021, il représentait plus de huit pour cent du produit intérieur brut (PIB).
'''),
                    html.Sup(html.A('1', href='#footnote1', id="ref1")),
                    html.Span('''
                               De façon générale, les organismes à but non lucratif ont tendance à jouer un rôle économique plus important au Québec et dans les provinces de l’Atlantique que dans le centre et l’ouest du Canada (à l’exception du Manitoba). Dans les territoires, le poids économique du secteur sans but lucratif varie considérablement. Il représente environ trois pour cent de l’économie totale du Nunavut et environ un dixième de l’économie des Territoires du Nord-Ouest. 
                           '''),
                    # Nonprofit GDP as % of total GDP
                    dcc.Graph(
                        figure=fig_perNatGDP, id="perNatGDP", style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H2('PIB par type d’organisme à but non lucratif et par sous-secteur'),
                    html.Span('''
À l’échelle nationale, les institutions gouvernementales à but non lucratif (hôpitaux, certains établissements de soins pour bénéficiaires internes, universités et collèges) produisent environ trois quarts du PIB total du secteur sans but lucratif. Le quart restant revient aux organismes du sous-secteur de base. Le ratio est d’environ 3:2 entre les organismes communautaires et les institutions communautaires à but non lucratif. 
                              '''),
                    html.Sup(html.A('2', href='#footnote2', id="ref2")),
                    html.Span('''
Ces dernières jouent un rôle économique dominant dans presque toutes les provinces et les territoires (la seule exception étant le Nunavut). De même, les organismes communautaires représentent une proportion plus élevée du PIB que les institutions communautaires à but non lucratif dans tout le pays, sauf au Nouveau-Brunswick et à Terre-Neuve-et-Labrador. 
                    ''', className='mt-4'),
                    # % and $ nonprofit GP by subsec
                    dcc.Graph(
                        id='gdpSubSec', style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H3('Tendances relatives au PIB par type d’organisme à but non lucratif et par sous-secteur'),
                    html.Span('''
Depuis 2007, le secteur sans but lucratif a enregistré une croissance supérieure à celle de l’économie dans son ensemble. Cette différence est en grande partie attribuable au ralentissement économique de 2008-2009, ainsi qu’à une période de croissance économique plus lente entre 2014 et 2016. Pendant ces périodes, le PIB du secteur sans but lucratif a continué d’augmenter au même rythme, alors que le reste de l’économie s’est contracté ou a considérablement ralenti. La croissance des institutions communautaires à but non lucratif était un peu plus rapide que celle des organismes communautaires et des institutions gouvernementales à but non lucratif, mais elle était également un peu plus volatile. À l’échelle nationale, le PIB des institutions communautaires à but non lucratif a presque doublé en termes nominaux'''),
                    html.Sup(html.A('3', href='#footnote3', id="ref3")),
                    html.Span('''
depuis 2007, alors que celui des institutions gouvernementales à but non lucratif a augmenté d’environ 85 % et celui des organismes communautaires à but non lucratif a augmenté d’environ 75 %. Le PIB des institutions et des organismes communautaires à but non lucratif s’est contracté avec la pandémie, alors que celui des institutions gouvernementales à but non lucratif a continué de croître, probablement en raison du rôle majeur qu’ont joué les hôpitaux en réaction à cette crise.

                    ''', className='mt-4'),
                    # TODO: Add footnote
                    # Relative growth nominal GDP subsec
                    dcc.Graph(
                        id='gdpGrowth', style={
                            'marginTop': marginTop}
                    ),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H2('PIB par secteur d’activités'),
                    dcc.Markdown('''
Les organismes des domaines de la santé, de l’éducation, de la recherche et des services sociaux représentent les plus grandes proportions du PIB du secteur sans but lucratif. À l’échelle nationale, environ trois cinquièmes du PIB du sous-secteur gouvernemental reviennent aux organismes de santé, un peu plus d’un tiers appartient aux organismes d’éducation et de recherche, et le reste revient aux organismes de services sociaux. La majeure partie du PIB des organismes de santé, d’éducation et de recherche revient aux institutions communautaires à but non lucratif, alors que la majorité du PIB des organismes de services sociaux appartient aux organismes communautaires à but non lucratif.
                    ''', className='mt-4'),
                    dcc.Markdown('''
En ce qui a trait aux revenus du sous-secteur communautaire sans but lucratif, près de deux tiers du PIB revient aux organismes de quatre secteurs d’activités particuliers (associations commerciales, associations professionnelles et syndicats; services sociaux; culture, sports et loisirs; et éducation et recherche). Des pourcentages plutôt faibles du PIB se rapportent aux organismes des secteurs du développement international et de l’aide internationale, de l’environnement, du droit, de la défense des intérêts et de la politique.
                    '''),
                    dcc.Markdown('''
De façon générale, les données provinciales et territoriales concordent avec les tendances nationales.                 
                    '''),
                    # TODO: Add footnote
                    # % nonrpfot GDP subsec and activity
                    dcc.Graph(
                        id='gdpSubSecActivity', style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H2(
                        "Footnotes",
                        className="anchored quarto-appendix-heading"),
                    html.Ol([
                        html.Li([
                            html.P([
                                "Le PIB est une mesure de la valeur totale des biens et services produits au pays pendant une période donnée.",
                                html.A(
                                    "↩︎",
                                    href="#fnref1",
                                    className="footnote-back",
                                    role="doc-backlink")
                            ], id="fn1")
                        ], id="fn1"),
                        html.Li(
                            [
                                html.P(
                                    "Le Compte satellite des institutions sans but lucratif et du bénévolat de Statistique Canada (source de données utilisée pour cette histoire) divise le secteur sans but lucratif en trois catégories :"),
                                html.P([html.B("Organismes communautaires à but non lucratif."), "  Ces organismes sont indépendants du gouvernement et produisent des biens et des services sans frais, ou à des prix économiquement non significatifs (c’est-à-dire que les prix demandés influencent peu les quantités de biens ou de services produites ou achetées par les consommateurs). Les biens et les services qu’ils produisent peuvent être consommés par des foyers (y compris des particuliers) ou par la société dans son ensemble. Ils comprennent, par exemple, les organismes de services à la personne, tels que les banques alimentaires, les refuges, les groupes jeunesse, les lieux de culte, les organismes de défense et les clubs de service"]),
                                html.P([html.B("Institutions communautaires à but non lucratif."), " À l’instar des organismes communautaires à but non lucratif, ces institutions sont indépendantes du gouvernement. Toutefois, elles produisent des biens et des services destinés aux foyers ou à la société à des prix économiquement significatifs (c’est-à-dire qu’ils ont pour activité la production marchande), ou encore elles produisent des biens et des services destinés aux entreprises ou à d’autres organismes à but non lucratif. Elles comprennent, par exemple, les associations d’affaires, les chambres de commerce et les associations de copropriétaires (condominiums)."]),
                                html.P([html.B("Institutions gouvernementales à but non lucratif."), " Ces institutions sont semblables aux organismes communautaires à but non lucratif en ce sens qu’elles produisent des biens et des services à des prix économiquement non significatifs. La principale différence réside dans le fait qu’elles sont grandement influencées par le gouvernement, même si elles sont distinctes de celui-ci. Elles comprennent, par exemple, les hôpitaux, certains établissements de soins pour bénéficiaires internes, les universités et les collèges."]),
                                html.P(
                                    [
                                        "Les organismes communautaires et les institutions communautaires à but non lucratif  sont regroupés dans le ",
                                        html.Em("sous-secteur sans but lucratif de base"),
                                        " qui contraste avec le ",
                                        html.Em("sous-secteur des institutions gouvernementales à but non lucratif"), " composé d’institutions gouvernementales à but non lucratif.", html.A(
                                            "↩︎", href="#fnref2", className="footnote-back", role="doc-backlink")
                                    ]
                                )
                            ], id="fn2"),
                        html.Li([
                            html.P([
                                "C’est-à-dire, sans tenir compte des effets de l’inflation.", html.A("↩︎", href="#fnref3", className="footnote-back", role="doc-backlink")])
                        ], id="fn3"),
                    ])
                ],
            )
        ]
        ),
    ),
    footer
])
