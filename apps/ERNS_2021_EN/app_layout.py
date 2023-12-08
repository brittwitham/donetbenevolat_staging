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
                            'The economic role of the nonprofit sector'),
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
                    html.Span('''
The nonprofit and charitable sector plays a significant role in the Canadian economy, accounting for over eight percent of national Gross Domestic Product (GDP) in 2021.'''),
                    html.Sup(html.A('1', href='#footnote1', id="ref1")),
                    html.Span('''
                               Broadly speaking, nonprofits tend to play a larger economic role in Quebec and the Atlantic provinces than in Central and Western Canada, with Manitoba marking the major exception. The economic size of the nonprofit sector in the territories is quite variable, ranging from about three percent of the total economy in Nunavut economy to about a tenth in the Northwest Territories.
                           '''),
                    # Nonprofit GDP as % of total GDP
                    dcc.Graph(
                        figure=fig_perNatGDP, id="perNatGDP", style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H2('GDP by nonprofit type and sub-sector'),
                    html.Span('''
Nationally, government nonprofits (hospitals, residential care facilities, universities and colleges) produce about three quarters of total nonprofit GDP. The remaining quarter comes from core sub-sector organizations divided about 3:2 between community and business nonprofits.'''),
                    html.Sup(html.A('2', href='#footnote2', id="ref2")),
                    html.Span('''
                                  Government nonprofits play the dominant economic role in virtually every province and territory, with Nunavut being the only exception. Similarly, community nonprofits account for a higher proportion of GDP than business nonprofits everywhere except for New Brunswick and Newfoundland and Labrador.
                    ''', className='mt-4'),
                    # % and $ nonprofit GP by subsec
                    dcc.Graph(
                        id='gdpSubSec', style={
                            'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H3('GDP trends by nonprofit type and sub-sector'),
                    html.Span('''
Since 2007, the nonprofit sector has grown more than the economy as a whole. Most of this difference is due to the 2008-09 economic downturn and a period of slower economic growth between 2014 and 2016. During these periods, nonprofit GDP continued to increase at pace while the rest of the economy contracted or slowed significantly. Business nonprofits have tended to grow somewhat faster than community and government nonprofits, though this growth has been somewhat more volatile. Nationally, business nonprofit GDP has almost doubled in nominal terms'''),
                    html.Sup(html.A('3', href='#footnote3', id="ref3")),
                    html.Span('''
                                 since 2007 while government nonprofit GDP has increased by about 85% and community nonprofit GDP by about 75%. Both business and community nonprofit GDP contracted with the onset of the pandemic while government nonprofit GDP continued to grow, likely driven by the central role of hospitals in pandemic response.
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
                    html.H2('GDP by activity area'),
                    dcc.Markdown('''
Organizations working in the areas of health, education and research and social services account for the bulk of GDP produced by the nonprofit sector. Nationally, about three fifths of government sub-sector GDP is produced by health organizations, just over a third by education and research organizations and the balance by social services organizations. Most health and education and research related GDP is produced by government nonprofits while most social services GDP is produced by community nonprofits.
                    ''', className='mt-4'),
                    dcc.Markdown('''
Within the community nonprofit sub-sector, nearly two thirds of GDP is produced by organizations working in four activity areas (business and professional associations and unions, social services, culture, sports and recreation and education and research). Quite small percentages of GDP are produced by organizations working in the areas of international development and relief, the environment and law, advocacy and politics.
                    '''),
                    dcc.Markdown('''
Broadly speaking, provincial and territorial data are quite consistent with the national pattern.                    '''),
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
                                "Gross Domestic Product is a measure of the total value of goods and services produced in country within a given period",
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
                                            "↩︎", href="#fnref2", className="footnote-back", role="doc-backlink")
                                    ]
                                )
                            ], id="fn2"),
                        html.Li([
                            html.P([
                                "i.e., not accounting for the effects of inflation.", html.A("↩︎", href="#fnref3", className="footnote-back", role="doc-backlink")])
                        ], id="fn3"),
                    ])
                ],
            )
        ]
        ),
    ),
    footer
])
