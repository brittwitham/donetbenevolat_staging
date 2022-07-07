from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                # dcc.Link("Home", href="/")
                dbc.NavLink("Home", href="/",external_link=True)
                ),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("More blogs", header=True),
                    # dbc.DropdownMenuItem("Blog 1", href="#"),
                    # dbc.DropdownMenuItem("Blog 2", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
        brand="Don et Benevolat",
        brand_href="/",
        color="#c7102e",
        dark=True,
        sticky='top'
    )
footer = html.Footer(
       dbc.Container(
           dbc.Row(
               html.Div(
                   html.P('Copyright © Imagine Canada 2021',className="text-center"),
                   className='col-md-10 col-lg-8 mx-auto mt-5'
               ),
           )
       )
   )

content = dbc.Container(
    [
        dcc.Location(id='url', refresh=False),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Qui Donne Aux Organismes Caritatifs et Combien?",className='card-title'), href='/WDA0101_fr'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("Almost nine in ten Canadians made some form of financial or in-kind contribution to charitable and nonprofit organizations during the one year period prior to the survey.",className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
                dcc.Location(id='url', refresh=False),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Comment Donne-T-On Au Canada?",className='card-title'), href='/HDC0102_fr'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("Nationally, they are most likely to donate in response to a public solicitation (such as on the street or in a shopping mall), while attending religious services, or by sponsoring someone in an event.",className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
                dcc.Location(id='url', refresh=False),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Comprendre Les Grand.E.S. Donateur.Trice.S",className='card-title'), href='/UTD0103_fr'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("On average, donors contributed $569 each, for a national total of approximately $11.9 billion.",className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Pourquoi Donne-T-On Au Canada?",className='card-title'), href='/WDC0105_fr'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("Nationally, roughly seven in every ten donors donate in order to make a contribution to theircommunity or because they are personally affected by the cause or know someone else who is.",className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("What Keeps Canadians From Giving More?",className='card-title'), href='/WKC0106'),
                                html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Nationally, one quarter of donors say they do not donate more because no one asks them to and roughly an eighth say they find it hard to find a cause worth supporting or do not know where to make additional donations.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Who Volunteers and How Much Time Do They Contribute?",className='card-title'), href='/WVA0201'),
                                html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Almost eight in ten Canadians (79%) volunteered time to some form of pro-social activity during the one year period prior to the survey.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Understanding Top Volunteers",className='card-title'), href='/UTV0203'),
                                html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                On average, volunteers contributed 131 hours each, contributing just under 1.7 billion volunteer hours annually.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Helping Others and Community Improvement",className='card-title'), href='/HOA0204'),
                                html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Just over two fifths of Canadians aged 15 and older volunteered for a charitable or nonprofit organization during the one year period prior to the survey.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Why Do Canadians Volunteer?",className='card-title'), href='/WDC0205'),
                                html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Overall, people are most likely to volunteer because they want to make a contribution to the community, to use their skills and experiences in support of a good cause, and because they or someone they know is personally affected by the cause of the organization.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("What Keeps Canadians From Giving More?",className='card-title'), href='/WKC0206'),
                                html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Lack of time was the most frequently reported barrier, followed by being unable to make a long-term commitment to volunteering.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("What Types of Organizations Do Canadians Support?",className='card-title'), href='/WTO0207'),
                                html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                On average, volunteers contributed time to 1.4 causes. Most volunteers contributed time to one cause, just over a quarter to two, and the balance to three.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        # html.Hr(),
        html.H2("Giving and Volunteering by Demographic"),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Giving and Volunteering for Health Organizations",className='card-title'), href='/GAV0301'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                # html.P("""
                                # On average, volunteers contributed time to 1.4 causes. Most volunteers contributed time to one cause, just over a quarter to two, and the balance to three.
                                # """,
                                # className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Giving and Volunteering for Religious Organizations",className='card-title'), href='/GAV0302'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                # html.P("""
                                # On average, volunteers contributed time to 1.4 causes. Most volunteers contributed time to one cause, just over a quarter to two, and the balance to three.
                                # """,
                                # className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Giving and Volunteering for Education and Research Organizations",className='card-title'), href='/GAV0303'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                # html.P("""
                                # On average, volunteers contributed time to 1.4 causes. Most volunteers contributed time to one cause, just over a quarter to two, and the balance to three.
                                # """,
                                # className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Giving and Volunteering for Social Services Organizations",className='card-title'), href='/GAV0304'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                # html.P("""
                                # On average, volunteers contributed time to 1.4 causes. Most volunteers contributed time to one cause, just over a quarter to two, and the balance to three.
                                # """,
                                # className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Giving and Volunteering for Arts, Culture and Rec Organizations",className='card-title'), href='/GAV0305'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                # html.P("""
                                # On average, volunteers contributed time to 1.4 causes. Most volunteers contributed time to one cause, just over a quarter to two, and the balance to three.
                                # """,
                                # className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Giving and Volunteering Among New Canadians",className='card-title'), href='/GAV0306'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                # html.P("""
                                # On average, volunteers contributed time to 1.4 causes. Most volunteers contributed time to one cause, just over a quarter to two, and the balance to three.
                                # """,
                                # className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Giving and Volunteering by Seniors",className='card-title'), href='/GAV0307'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                # html.P("""
                                # On average, volunteers contributed time to 1.4 causes. Most volunteers contributed time to one cause, just over a quarter to two, and the balance to three.
                                # """,
                                # className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Giving and Volunteering by Youth",className='card-title'), href='/GAV0308'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                # html.P("""
                                # On average, volunteers contributed time to 1.4 causes. Most volunteers contributed time to one cause, just over a quarter to two, and the balance to three.
                                # """,
                                # className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        # html.Hr(),
        html.H2("2013 Data"),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("How Do Canadians Donate? (2013)",className='card-title'), href='/HDC01002_13'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                # html.P("""
                                # On average, volunteers contributed time to 1.4 causes. Most volunteers contributed time to one cause, just over a quarter to two, and the balance to three.
                                # """,
                                # className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Why Do Canadians Give? (2013)",className='card-title'), href='/WDC0105_13'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                # html.P("""
                                # On average, volunteers contributed time to 1.4 causes. Most volunteers contributed time to one cause, just over a quarter to two, and the balance to three.
                                # """,
                                # className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
 
    ]
)


layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                [
                    html.Div(
                        html.Div(
                            html.H1('Don et Benevolat'),
                            className='site-heading'
                        ),
                        className="col-md-10 col-lg-8 mx-auto position-relative"
                    ),
                ]
            )
        ), 
    ],
        className='masthead',
        style={'backgroundImage':"url('./assets/home-bg.jpg')"}
    ),
    content,
    # footer
])

