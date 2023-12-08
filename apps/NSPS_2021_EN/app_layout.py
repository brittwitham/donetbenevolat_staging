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
    "Qui_sont_les_benevoles_et_combien_heures_donnent_ils_2018")

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
                            'Nonprofit sector paid staff'),
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
                    Collectively, the nonprofit sector employs approximately 2.5 million Canadians, equivalent to roughly 13% of the Canadian labour force. Two-thirds of nonprofit employees work for government nonprofits (hospitals, residential care facilities, universities and colleges) which are heavily dependent on paid labour to deliver their services. The remaining third are employed by core sub-sector
                           '''),
                    html.Sup(html.A('1', href='#footnote1', id="ref1")),
                    html.Span('''
                    organizations, divided about 3:1 between community and business nonprofits. Compared to government nonprofits, core sub-sector organizations tend to make much greater use of volunteers in carrying out their missions.
                    ''', className='mt-4'),
                    html.Span('''
                    The relative distributions of paid staff by nonprofit type and sub-sector are fairly consistent across provinces, though there are some fluctuations. Broadly speaking, core nonprofits account for larger percentages of total employees in Ontario and British Columbia and smaller percentages in the Atlantic provinces, Saskatchewan and Alberta. The situation in the Territories is more difficult to discern due to rounding of the data as released by Statistics Canada.
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
                    html.H3('Paid staff trends by nonprofit type and sub-sector'),
                    dcc.Markdown('''
                    From 2007 to 2009, employment in community, business and government nonprofits increased at roughly the same pace. Since 2009 core sub-sector employment, particularly among business nonprofits, increased much faster than employment in government nonprofits. As of 2021, business nonprofit employment was up by about a third and community nonprofit employment about a quarter from 2007 while government nonprofit employment was up by just under a fifth.
                    ''', className='mt-4'),
                    html.Span('''
                    The differences in growth between core and government organizations would likely have been larger, but community and business nonprofit employment dropped much more due to the pandemic than did government nonprofit employment. Overall, employment in community and business nonprofits contracted by about 12% in 2020 while government nonprofit employment dropped only marginally.'''),
                    html.Sup(html.A('3', href='#footnote3', id="ref3")),
                    html.Span('''
                                 While core sub-sector employment recovered significantly in 2021, employment remained below pre-pandemic levels.
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
                    html.H3('Paid staff by activity area'),
                    html.Span('''
                    Nationally, organizations working in the areas of health, education and research, and social services account for the largest proportions of total employment.'''),
                    html.Sup(html.A('4', href='#footnote4', id="ref4")),
                    html.Span('''
                    Health organizations account for two thirds of government sub-sector employment, education and research organizations just over a quarter and social services organizations the balance. The vast majority of nonprofit employees working in health and education and research organizations are employed in government nonprofits, while the majority of those working for social services organizations are employed in core sub-sector organizations, mainly community nonprofits.
                    ''', className='mt-4'),
                    dcc.Markdown('''
                    Focusing on the core sub-sector, social services organizations account for the largest proportion of employees, followed by business and professional associations and unions and organizations that do not clearly fall into one of the other 11 specific activity areas. Environmental organizations account for the fewest employees (less than one half of one percent of total employment), trailing international development and relief organizations and organizations devoted to law, advocacy and politics.
                    '''),
                    dcc.Markdown('''
                    Where complete provincial data exist, they are quite consistent with the national pattern. Unfortunately, due to data rounding (see footnote 2 below) our understanding of nonprofit employment by activity area in Atlantic Canada and the Territories is quite limited.
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
                    html.H3('Paid staff trends by activity area'),
                    dcc.Markdown('''
                    Looking at paid staff growth by activity area, the greatest growth from 2007 nationally has been among core sub-sector social services organizations or organizations that do not fall into one of the other 11 activity areas. The paid staff complements of these organizations have increased by about two thirds over the period. Paid staff numbers have decreased slightly in philanthropic intermediaries and religion organizations and held steady or increased slightly in environmental and sports, recreation and culture organizations.
                    ''', className='mt-4'),
                    dcc.Markdown('''
                    Focusing on the government nonprofit sub-sector, health and social services employment has increased by nearly a quarter, much more than among universities and colleges where employment has increased by less than a tenth. Health and social services employment has grown at a relatively constant pace, except with the onset of the pandemic when employment held steady before increasing sharply. In the core sub-sector, pandemic-related shifts are most clearly seen in organizations working in social services, sports, recreation and culture, education and other areas not clearly defined.
                    '''),
                    # TODO: Add footnote
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H3('Paid staff trends by activity area'),
                    dcc.Markdown('''
                    Looking at paid staff growth by activity area, the greatest growth from 2007 nationally has been among core sub-sector social services organizations or organizations that do not fall into one of the other 11 activity areas. The paid staff complements of these organizations have increased by about two thirds over the period. Paid staff numbers have decreased slightly in philanthropic intermediaries and religion organizations and held steady or increased slightly in environmental and sports, recreation and culture organizations.
                    ''', className='mt-4'),
                    dcc.Markdown('''
                    Focusing on the government nonprofit sub-sector, health and social services employment has increased by nearly a quarter, much more than among universities and colleges where employment has increased by less than a tenth. Health and social services employment has grown at a relatively constant pace, except with the onset of the pandemic when employment held steady before increasing sharply. In the core sub-sector, pandemic-related shifts are most clearly seen in organizations working in social services, sports, recreation and culture, education and other areas not clearly defined.
                    '''),
                    # TODO: Add footnote
                    # Nonrpofit employemnt by sub-sector, 2021
                    dcc.Graph(
                        id='empGrowthActivity_core', style={
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
                                    "Statistics Canada’s Satellite Account of Non-profit Organizations and Volunteering (the data source used in this story) divides the nonprofit sector into three parts:"),
                                html.P([html.B("Community nonprofits."), " These organizations are independent from government and produce goods and services for free or for prices that are not considered to be economically significant (i.e., the prices charged do not significantly influence the amounts of the good or service produced or the amounts purchased by consumers). The goods and services produced by community nonprofits may be consumed by households (including individuals) or collectively by society at large. Examples include human services organizations such as foodbanks, shelters, youth groups, places of worship, advocacy organizations and service clubs."]),
                                html.P([html.B("Business nonprofits."), " As with community nonprofits, these organizations are independent from government. They differ in that they produce goods and services for household or collective consumption at prices that are economically significant (i.e., they engage in market production) or produce goods and services for businesses or other nonprofit organizations. Examples include business associations, chambers of commerce and condominium associations."]),
                                html.P([html.B("Government nonprofits."), " These organizations are similar to community nonprofits in that they produce goods and services for prices that are not economically significant. The key difference is that they are heavily influenced by government, even though they are institutionally separate from it. Examples include hospitals, some residential care facilities, universities and colleges."]),
                                html.P(
                                    [
                                        "Community and business nonprofits are grouped together to form the ",
                                        html.Em("core nonprofit sub-sector"),
                                        " which is contrasted with the ",
                                        html.Em("government nonprofit sub-sector"), " made up of government nonprofits.", html.A(
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
                        html.Li([
                            html.P([
                                "Note that these are annual figures. Employment levels dropped much more in the immediate aftermath of the pandemic but partially recovered before the end of the year.", html.A("↩︎", href="#fnref3", className="footnote-back", role="doc-backlink")])
                        ], id="fn3"),
                        html.Li([
                            html.P("In addition to dividing organizations by type and sub-sector, the Satellite Account assigns organizations to one of 12 groups depending on their primary activity. These are:"),
                            html.P(
                                [
                                    html.Em("Arts, culture & recreation"),
                                    " - includes museums, visual, material and performing arts groups and facilities, media, historic and humanistic societies and sports and recreation groups."]),
                            html.P(
                                [
                                    html.Em("Education & research"),
                                    " - organizations dedicated to the provision and support of educational services and research. Universities and colleges are assigned to the government sub-sector."]),
                            html.P(
                                [
                                    html.Em("Health"),
                                    " - organizations providing and supporting in-patient and out-patient healthcare services. Hospitals and nursing homes are assigned to the government sub-sector."]),
                            html.P([html.Em("Social services"), " - organizations providing a diverse range of non-health related human services. A minority of organizations in this activity area are assigned to the government sub-sector, depending on the degree of influence government exerts on them."]),
                            html.P(
                                [
                                    html.Em("Environment"),
                                    " - organizations engaged in environmental protection and conservation, including animal welfare."]),
                            html.P(
                                [
                                    html.Em("Development & housing"),
                                    " - organizations engaged in social, community and economic development and the provision of housing."]),
                            html.P(
                                [
                                    html.Em("Law, advocacy & politics"),
                                    " - organizations engaged in advocacy or providing legal and related services, including offender rehabilitation."]),
                            html.P(
                                [
                                    html.Em(
                                        "Philanthropic intermediaries & voluntarism"),
                                    " - public and private foundations and organizations promoting voluntarism."]),
                            html.P(
                                [
                                    html.Em("International"),
                                    " - organizations engaged in international development and relief, including promotion of human rights and peace."]),
                            html.P(
                                [
                                    html.Em("Religion"),
                                    " - congregations and associations of congregations, including religious education and training."]),
                            html.P(
                                [
                                    html.Em(
                                        "Business and professional associations & unions"),
                                    " - organizations working to regulate and advance the interests of particular industries or groups of workers."]),
                            html.P(
                                [
                                    "Other",
                                    " - organizations not elsewhere assigned to an activity area.",
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
