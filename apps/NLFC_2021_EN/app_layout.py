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
Collectively, the nonprofit sector employs just over 2.5 million Canadians, equivalent to roughly 13% of the labour force. Two thirds of these workers are employed in government nonprofits and the remaining third in core nonprofits, divided about 3:1 between community and business nonprofits.
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
                    ])
                ],
            )
        ]
        ),
    ),
    footer
])
