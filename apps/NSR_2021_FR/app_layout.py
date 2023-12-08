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
                            'Nonprofit sector revenue'),
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
Overall, the Canadian nonprofit sector received just over $325 billion in revenue during 2021, the last complete year for which figures are available. Nationally, just over three fifths of total revenue went to government nonprofits (hospitals, residential care facilities, universities and colleges) and two fifths to core sub-sector organizations, divided about 3:2 between community and business nonprofits.
                           '''),
                    html.Sup(html.A('1', href='#footnote1', id="ref1")),
                    html.Br(),
                    html.Span('''
While the relative distributions of revenue by nonprofit type and sub-sector are fairly consistent across the provinces and territories, there are some variations. For example, government nonprofits account for larger percentages of total revenues in Prince Edward Island and Newfoundland and Labrador, but play a markedly smaller role in Nunavut, the only place where they accounted for a minority of nonprofit revenue. Similarly, community nonprofits consistently account for more revenue than business nonprofits, except in New Brunswick and Newfoundland and Labrador.
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
                    html.H3('Revenue trends by nonprofit type and sub-sector'),
                    dcc.Markdown('''
Since 2007, nonprofit revenue has grown by approximately 80% in nominal terms (i.e., not adjusting for the effects of inflation). Business nonprofit revenue has increased the most (nearly 95%), followed by community and government nonprofit revenue (each has increased by about 80%). While business nonprofit revenue increased the most, it was also the most volatile, increasing more rapidly than in other sub-sectors between 2007 and 2009 and decreasing significantly in 2014 and more modestly in 2020 with the onset of the pandemic. Community nonprofit revenues lagged government nonprofit revenues between 2010 and 2017 but outpaced them from 2017 to 2020.
                    ''', className='mt-4'),
                    # Relative growth of revenues by sub secotr
                    dcc.Graph(
                        id='revGrowth', style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H3('Revenue by activity area'),
                    html.Span('''
Organizations working in the areas of health, education and research and social services account for the largest portions of nonprofit revenue'''),
                    html.Sup(html.A('2', href='#footnote2', id="ref2")),
                    html.Span('''
                                 About two thirds of government sub-sector revenue goes to health organizations, a quarter to education and research organizations and the remainder to social services. The bulk of the revenue for health and education and research organizations goes to government sub-sector organizations while the bulk of social services organization revenue goes to organizations in the core nonprofit sector (mainly community nonprofits).
                    ''', className='mt-4'),
                    dcc.Markdown('''
Focusing on core sub-sector revenues, four fifths of revenues go to organizations working in four specific activity areas (business and professional associations and unions, social services, culture, sport and recreation, and education and research) and to organizations working in areas that do not clearly fall into one of the other 11 specific activity areas. Quite small percentages of core sub-sector revenues go to organizations working in the areas of law, advocacy and politics, the environment and international development and relief.
                    '''),
                    dcc.Markdown('''
Broadly speaking, provincial and territorial data are quite consistent with the national pattern.
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
                    html.H3('Revenue trends by activity area'),
                    dcc.Markdown('''
Looking at revenue growth by activity area, the largest growth since 2007 has been among core sub-sector organizations providing social services or working in areas that do not clearly fall into another defined activity area. Revenues for these organizations have more than doubled in nominal terms. Core sub-sector revenue has grown least among environmental organizations, philanthropic intermediaries, religious, and sports and recreation organizations. These organizations have seen their revenues increase by fifty percent or slightly less.
                    ''', className='mt-4'),
                    dcc.Markdown('''
Focusing on the government sub-sector, health and social services revenues have nearly doubled, much more than with education and research organizations where revenues have increased by just over fifty percent. Overall, the pace of growth among these organizations has been fairly consistent except since 2020, presumably due to increased pandemic-related funding for health organizations. In the core sub-sector, pandemic-related shifts are most clearly seen with organizations focusing on development and housing and sports, recreation and culture.
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
                    html.H3('Revenue sources'),
                    dcc.Markdown('''
Each sub-sector depends on a different mix of revenue sources. As one would expect given how the sub-sectors are defined, business nonprofits are heavily dependent on earned income, with sale of goods and services accounting for about three fifths of total revenue at the national level and membership fees and dues accounting for a third. Government nonprofits, on the other hand, receive about three quarters of revenue from government funding and about a fifth from the sale of goods and services. Community nonprofits have the most diverse range of revenue sources. The largest portion comes from earned income, chiefly the sale of goods and services, followed by membership fees and dues and investments. Just over a third comes from government funding and just under a third from personal and corporate donations.
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
                    html.H3('Revenue trends by source and sub-sector'),
                    dcc.Markdown('''
The drivers of revenue growth vary significantly from sub-sector to sub-sector. Unsurprisingly, government funding has been the largest driver in growth for government nonprofits (increasing by 83% in nominal terms since 2007), but it has also been a key driver for community nonprofits, more than doubling over the period. While both sub-sectors have also seen large increases in some other revenue sources - investment income for community nonprofits and sale of goods and services for government nonprofits - these sources do not account for such large portions of the funding pie, though that may change if growth continues at this pace.                    ''', className='mt-4'),
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
