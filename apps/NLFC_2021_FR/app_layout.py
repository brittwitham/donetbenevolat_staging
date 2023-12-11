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
demos = [
    'Gender',
    'Immigration',
    'Indigenous',
    'Visible minority',
    'Formal education',
    'Age group']


# TODO!
navbar = gen_navbar(
    "nonprofit_labour_force_composition_2021")

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
                            'Nonprofit labour force composition'),
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
Le secteur sans but lucratif emploie quelque 2,5 millions de Canadiens, ce qui correspond à environ 13 % de la population active du Canada. Deux tiers des employés de ce secteur travaillent pour des institutions gouvernementales à but non lucratif (hôpitaux, établissements de soins pour bénéficiaires internes, universités et collèges) qui dépendent grandement de la population active rémunérée pour assurer la prestation de leurs services. Le tiers restant travaille dans les institutions du sous-secteur de base[^1], dont le ratio est d’environ 3:1 entre les organismes communautaires et les institutions communautaires à but non lucratif. Comparativement aux institutions gouvernementales à but non lucratif, les organismes du sous-secteur de base ont tendance à dépendre davantage des bénévoles pour réaliser leur mission.
                              '''),
                    html.Sup(html.A('1', href='#footnote1', id="ref1")),
                    html.Span('''
                              For more details on how paid staff are distributed by nonprofit type and activity area, please refer to Nonprofit Sector Paid Staff elsewhere on this website.
                           '''),
                    html.H3('Job type'),
                    html.Span('''
Overall, nearly four fifths of nonprofit employees are employed on a full-time basis and one fifth on a part-time basis. Part-time employees make up a larger fraction of the community nonprofit workforce they do the business and government nonprofit labour forces.
                    ''', className='mt-4'),
                    html.Span('''
These patterns are reasonably consistent across provinces, though there are some fluctuations. The situation is less clear in the Territories due to rounding of the data as released by Statistics Canada.
                    ''', className='mt-4'),
                    html.Sup(html.A('2', href='#footnote2', id="ref2")),
                    # TODO: Add footnote
                    # NNo and % of full time ...
                    dcc.Graph(
                        id='jobsType', style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H4('Average wages by organization type'),
                    dcc.Markdown('''
Looking at average wages by organization type, compensation in community nonprofits tends to trail compensation in other types of nonprofits. Nationally, average compensation for full-time community nonprofit positions trails business and government full-time positions by roughly a fifth. While part-time community nonprofit compensation is roughly equivalent to part-time business nonprofit compensation, both are nearly a third less than part-time government compensation. The combination of lower wages and a higher fraction of part-time employment means that the typical community nonprofit wage is about 26% less than the typical government nonprofit wage and 22% less than the typical business nonprofit wage.
                    ''', className='mt-4'),
                    # Average wages and salaries by employment type
                    dcc.Graph(
                        id='wagesType', style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H3('Characteristics of the nonprofit labour force'),
                    dcc.Markdown('''
Nationally, seven in ten of those working in the nonprofit sector are women. The fraction of female employees is highest among government and community nonprofits, but lags somewhat among business nonprofits. As is typical of other workforces, the bulk of nonprofit employees are aged between 25 and 64. Within the nonprofit sector, a significantly higher fraction of government nonprofit employees fall into this age range, compared to community and business nonprofits. Community nonprofit employees are disproportionately likely to be 65 years of age while business nonprofit employees are disproportionately likely to be under the age of 25. Nonprofit employees also tend to be highly educated, with just under half having a university degree. Compared to other employees, government nonprofit employees are modestly more likely to have a university degree while community and particularly business nonprofit employees are markedly more likely to have a high school degree or less. These trends tend to hold constant at the provincial level with the age and education patterns frequently being even more pronounced than at the national level.
                    ''', className='mt-4'),
                    dcc.Markdown('''
Looking at other individual characteristics, over a quarter of nonprofit employees immigrated to Canada at some point in their life and/or are members of visible minorities. There is comparatively little variation in these figures by nonprofit type. Roughly one in every 25 employees identifies as Indigenous. While the difference between community and other nonprofits is just two percentage points, the comparatively small base means that community nonprofit employees are much more likely to be Indigenous than are employees in other types of nonprofits. Provincially, the fractions of nonprofit employees who have immigrated to Canada at some point or are members of a visible minority tend to be highest in Ontario and British Columbia and lowest in Atlantic Canada. Nonprofit employees in Saskatchewan and Manitoba are markedly more likely to be Indigenous.
                    '''),
                    dcc.Markdown('''
Broadly speaking, provincial and territorial data are quite consistent with the national pattern.
                    '''),
                    # TODO: Add footnote
                    # Dist of nonprofit employees
                    dcc.Dropdown(
                        id='demo-selection',
                        options=[{'label': demos[i], 'value': demos[i]}
                                 for i in range(len(demos))],
                        value='Formal education',
                        style={'verticalAlign': 'middle'}
                    ),
                    dcc.Graph(
                        id='jobsDemog', style={
                            'marginTop': marginTop}
                    ),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H4('Average wages by worker characteristic'),
                    dcc.Markdown('''
While most nonprofit employees are female, they tend to be paid significantly less than male employees. This pay gap is largest among business nonprofits and smallest among government nonprofits. Looking at pay by age, average wages tend to increase until the age of 45 to 54 before declining. Nationally, within the core age ranges of 25 to 64, community nonprofit wages tend to be about a quarter less than government nonprofit wages, with larger gaps among younger and older workers. Business nonprofit wages are about a quarter lower than government nonprofit wages for workers under 25, but this gap disappears and even reverses with age before re-emerging among workers 65 years of age and older. Average wages also tend to increase with levels of formal education. Community nonprofit wages are consistently lower than government nonprofit wages, with the size of the difference tending to increase with level of education. Average business nonprofit wages are 10% - 15% higher than government nonprofit wages for those with less than a trade certificate or less but slightly lower among those with a college diploma or more.
                    ''', className='mt-4'),
                    dcc.Markdown('''
Among government nonprofits, average wages for those who have been immigrants to Canada at some point in their lives are somewhat higher than non-immigrant wages, but the reverse is true for community and business nonprofits. The gaps between core sub-sector wages and government wages are somewhat larger among immigrant workers than they are among those born in Canada, particularly with business nonprofits. Visible minority employees tend to receive lower wages across all nonprofit types, with the largest gap among business nonprofits and the lowest among government nonprofits. The situation is very similar with Indigenous employees, though the gap in pay between average wages for Indigenous and non-Indigenous employees is lowest among community nonprofits, though wages for both groups trail government nonprofit wages by over a quarter.
                    '''),
                    # TODO: Add footnote
                    # Av nonprofit wages by dmeo
                    dcc.Graph(
                        id='wagesDemog', style={
                            'marginTop': marginTop}),
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
                                "When employment within a given sub-sector and activity area rounds to less than one thousand employees, Statistics Canada reports zero employees.",
                                html.A(
                                    "↩︎",
                                    href="#fnref2",
                                    className="footnote-back",
                                    role="doc-backlink")
                            ], id="fn2")
                        ], id="fn2"),
                    ])
                ],
            )
        ]
        ),
    ),
    footer
])
