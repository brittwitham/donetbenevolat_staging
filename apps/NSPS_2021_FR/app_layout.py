# App layout file for WVHT_2018_EN converted from
# Who_volunteers_and_how_much_time_do_they_contribute_2018.py

from dash import dcc, html
import dash_bootstrap_components as dbc
from app import app
from ..layout_utils import gen_home_button, gen_navbar, footer
from .callbacks import register_callbacks
# from .data_processing import region_values, status_names, VolRate_2018, AvgTotHours_2018
# from .graphs import static_graph

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
    "nonprofit_paid_staff_2021")

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
                            'Personnel rémunéré du secteur sans but lucratif'),
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
                    CLe secteur sans but lucratif emploie quelque 2,5 millions de Canadiens, ce qui correspond à environ 13 % de la population active du Canada. Deux tiers des employés de ce secteur travaillent pour des institutions gouvernementales à but non lucratif (hôpitaux, établissements de soins pour bénéficiaires internes, universités et collèges) qui dépendent grandement de la population active rémunérée pour assurer la prestation de leurs services. Le tiers restant travaille dans les institutions du sous-secteur de base
                           '''),
                    html.Sup(html.A('1', href='#footnote1', id="ref1")),
                    html.Span('''
                    dont le ratio est d’environ 3:1 entre les organismes communautaires et les institutions communautaires à but non lucratif. Comparativement aux institutions gouvernementales à but non lucratif, les organismes du sous-secteur de base ont tendance à dépendre davantage des bénévoles pour réaliser leur mission.
                    ''', className='mt-4'),
                    html.Span('''
                    Bien que la distribution relative au personnel rémunéré par type d’organisme à but non lucratif et par sous-secteur soit plutôt constante entre les provinces, il existe certaines variations. De façon générale, le pourcentage du nombre total d’employés des organismes à but non lucratif de base est supérieur en Ontario et en Colombie-Britannique, mais il est moins élevé dans les provinces de l’Atlantique, en Saskatchewan et en Alberta. La situation dans les territoires est plus difficile à évaluer en raison de l’arrondissement des données publiées par Statistique Canada.
                    '''),
                    html.Sup(html.A('2', href='#footnote2', id="ref2")),
                    # Nonrpofit employemnt by sub-sector, 2021

                    dcc.Graph(
                        id='empSubSec', style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H3('Tendances relatives au personnel rémunéré par type d’organisme à but non lucratif et par sous-secteur'),
                    dcc.Markdown('''
                    De 2007 à 2009, l’emploi dans les organismes communautaires, les institutions communautaires à but non lucratif et les institutions gouvernementales à but non lucratif a augmenté à peu près au même rythme. Depuis 2009, l’emploi dans le sous-secteur de base (surtout dans les institutions communautaires à but non lucratif) a augmenté plus rapidement que dans les institutions gouvernementales à but non lucratif. En 2021, l’emploi dans les institutions communautaires à but non lucratif avait augmenté d’environ un tiers. Dans les organismes communautaires, il avait augmenté d’environ un quart depuis 2007, alors que l’emploi dans les institutions gouvernementales à but non lucratif avait augmenté d’un peu moins d’un cinquième.
                    ''', className='mt-4'),
                    html.Span('''
                    Les différences de croissance entre les institutions de base et gouvernementales auraient probablement été plus importantes, mais la pandémie a fait chuter l’emploi au sein des organismes communautaires et des institutions communautaires à but non lucratif, davantage que dans les institutions gouvernementales à but non lucratif. En général, l’emploi dans les organismes communautaires et les institutions communautaires à but non lucratif a reculé d’environ 12 % en 2020, alors que l’emploi au sein des institutions gouvernementales à but non lucratif n’a chuté que légèrement.[^3] Bien que l’emploi au sein du sous-secteur de base se soit considérablement rétabli en 2021, il demeurait inférieur aux niveaux prépandémiques.'''),
                    html.Sup(html.A('3', href='#footnote3', id="ref3")),
                    html.Span('''
                                 Il est à noter qu’il s’agit là de données annuelles. Les niveaux d’emploi ont chuté beaucoup plus immédiatement après la pandémie, mais ils étaient partiellement rétablis avant la fin de l’année.
                    '''),
                    # TODO: Add footnote
                    # Nonrpofit employemnt by sub-sector, 2021
                    dcc.Graph(
                        id='empGrowth', style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H3('Personnel rémunéré par secteur d’activités'),
                    html.Sup(html.A('4', href='#footnote4', id="ref4")),
                    html.Span('''
                    À l’échelle nationale, les organismes des domaines de la santé, de l’éducation, de la recherche et des services sociaux représentent les plus grandes proportions d’emploi.[^4] Deux tiers de l’emploi du sous-secteur gouvernemental reviennent aux organismes de santé, un peu plus d’un quart appartient aux organismes d’éducation et de recherche, et le reste revient aux organismes de services sociaux. La majeure partie des employés du secteur sans but lucratif qui travaillent pour des organismes de santé, d’éducation et de recherche le font au sein d’institutions gouvernementales à but non lucratif, alors que la majorité des employés qui travaillent pour des organismes de services sociaux le font au sein d’organismes du sous-secteur de base (surtout les organismes communautaires à but non lucratif). 
                    ''', className='mt-4'),
                    dcc.Markdown('''
                    En ce qui concerne le sous-secteur de base, la plus grande proportion d’employés revient aux organismes de services sociaux, suivis des institutions commerciales et professionnelles, des syndicats et des organismes des secteurs qui ne font pas partie d’un des onze autres secteurs d’activités. Les organismes environnementaux sont ceux qui comptent le moins d’employés (moins d’un demi pour cent de l’emploi total), suivis des organismes de développement international et d’aide internationale, puis des organismes des secteurs du droit, de la défense des intérêts et de la politique.
                    '''),
                    dcc.Markdown('''
                    Lorsque des données provinciales complètes existent, elles correspondent habituellement aux tendances nationales. Malheureusement, en raison de leur arrondissement (voir note de bas de page 2 ci-dessous), notre compréhension de l’emploi par secteur d’activités dans les provinces de l’Atlantique et les territoires est assez limitée.
                    '''),
                    # TODO: Add footnote
                    # Nonrpofit employemnt by sub-sector, 2021
                    dcc.Graph(
                        id='empSubSecActivity', style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H3(' Tendances relatives au personnel rémunéré par secteur d’activités'),
                    dcc.Markdown('''
                    En ce qui a trait à la croissance de l’emploi rémunéré par secteur d’activités, le taux de croissance le plus élevé depuis 2007 a été enregistré pour les organismes du sous-secteur de base qui offrent des services sociaux ou travaillent dans des domaines qui n’appartiennent pas à un autre secteur d’activités défini. Les compléments de personnel rémunéré de ces organismes ont augmenté d’environ deux tiers au cours de la période. Quant au taux de croissance relatif au personnel rémunéré, il a légèrement diminué dans les intermédiaires philanthropiques et les organismes religieux. Il est demeuré inchangé ou a légèrement augmenté dans le cas des organismes environnementaux, de sports, de loisirs et de culture.
                    ''', className='mt-4'),
                    dcc.Markdown('''
                    Quant au sous-secteur des institutions gouvernementales à but non lucratif, l’emploi associé aux services de santé et sociaux a augmenté de près d’un quart, ce qui est supérieur à celui des universités et des collèges dont l’emploi a augmenté de moins d’un dixième. Le rythme de croissance de ces organismes s’est montré relativement constant, sauf depuis le début de la pandémie lorsque l’emploi est resté relativement stable avant d’augmenter rapidement. Dans le sous-secteur de base, les changements liés à la pandémie sont clairs dans le cas des organismes axés sur les services sociaux, les sports, les loisirs, la culture, l’éducation et divers autres secteurs moins bien définis.
                    '''),
                    dcc.Graph(
                        id='empGrowthActivity_core', style={
                            'marginTop': marginTop}),
                    # TODO: Add footnote
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H2(
                        "Footnotes",
                        className="anchored quarto-appendix-heading"),
                    html.Ol([
                        html.Li(
                            [
                                html.P(
                                    "Le Compte satellite des institutions sans but lucratif et du bénévolat de Statistique Canada (source de données utilisée pour cette histoire) divise le secteur sans but lucratif en trois catégories :"),
                                html.P([html.B("Organismes communautaires à but non lucratif."), " Ces organismes sont indépendants du gouvernement et produisent des biens et des services sans frais, ou à des prix économiquement non significatifs (c’est-à-dire que les prix demandés influencent peu les quantités de biens ou de services produites ou achetées par les consommateurs). Les biens et les services qu’ils produisent peuvent être consommés par des foyers (y compris des particuliers) ou par la société dans son ensemble. Ils comprennent, par exemple, les organismes de services à la personne, tels que les banques alimentaires, les refuges, les groupes jeunesse, les lieux de culte, les organismes de défense et les clubs de service."]),
                                html.P([html.B("Institutions communautaires à but non lucratif."), "À l’instar des organismes communautaires à but non lucratif, ces institutions sont indépendantes du gouvernement. Toutefois, elles produisent des biens et des services destinés aux foyers ou à la société à des prix économiquement significatifs (c’est-à-dire qu’ils ont pour activité la production marchande), ou encore elles produisent des biens et des services destinés aux entreprises ou à d’autres organismes à but non lucratif. Elles comprennent, par exemple, les associations d’affaires, les chambres de commerce et les associations de copropriétaires (condominiums)."]),
                                html.P([html.B("Institutions gouvernementales à but non lucratif."), " Ces institutions sont semblables aux organismes communautaires à but non lucratif en ce sens qu’elles produisent des biens et des services à des prix économiquement non significatifs. La principale différence réside dans le fait qu’elles sont grandement influencées par le gouvernement, même si elles sont distinctes de celui-ci. Elles comprennent, par exemple, les hôpitaux, certains établissements de soins pour bénéficiaires internes, les universités et les collèges."]),
                                html.P(
                                    [
                                        "Les organismes et les institutions communautaires à but non lucratif sont regroupés dans le",
                                        html.Em("sous-secteur sans but lucratif de base"),
                                        "  qui contraste avec le ",
                                        html.Em("sous-secteur des institutions gouvernementales à but non lucratif."), html.A(
                                            "↩︎", href="#fnref1", className="footnote-back", role="doc-backlink")
                                    ]
                                )
                            ], id="fn1"),
                        html.Li([
                            html.P([
                                "Lorsque l’emploi dans un sous-secteur et un secteur d’activités est arrondi à moins de mille employés, Statistique Canada déclare que le nombre d’employés est de zéro.",
                                html.A(
                                    "↩︎",
                                    href="#fnref2",
                                    className="footnote-back",
                                    role="doc-backlink")
                            ], id="fn2")
                        ], id="fn2"),
                        html.Li([
                            html.P([
                                "Note that these are annual figures. Employment levels dropped much more in the immediate aftermath of the pandemic but partially recovered before the end of the year.", html.A("↩︎", href="#fnref3", className="footnote-back", role="doc-backlink")])
                        ], id="fn3"),
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
                                    "Autre",
                                    " -  organismes qui ne font pas partie de ces secteurs d’activités.",
                                    html.A(
                                        "↩︎",
                                        href="#fnref4",
                                        className="footnote-back",
                                        role="doc-backlink")])
                        ], id="fn4")
                    ])
                ],
            )
        ]
        ),
    ),
    footer
])
