import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd

from utils.data.WDA0101_data_utils import get_region_values
from utils.data.WDC0105_data_utils import get_region_names
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc
import os
import os.path as op

from utils.graphs.WKC0106_graph_utils import single_vertical_percentage_graph, vertical_dollar_graph, vertical_percentage_graph
from utils.data.WKC0106_data_utils import get_data, process_data, get_region_names, get_region_values

from app import app
from homepage import navbar, footer

####################### Data processing ######################
Barriers_2018, AvgAmtBarriers_2018, GivingConcerns_2018, SolicitationConcerns_2018, BarriersByCause_2018 = get_data()

data = [Barriers_2018, AvgAmtBarriers_2018, GivingConcerns_2018, SolicitationConcerns_2018, BarriersByCause_2018]

cause_names = BarriersByCause_2018["Group"].unique()
barriers_names = Barriers_2018["QuestionText"].unique()
status_names = ['Marital status', 'Labour force status', 'Immigration status']

process_data(data)

region_values = get_region_values()
region_names = get_region_names()

###################### App layout ######################

marginTop = 20

layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1('Why do Canadians give?'),
                        html.Span(
                            'David Lasby',
                            className='meta'
                        )
                        ],
                        className='post-heading'
                    ),
                    className='col-md-10 col-lg-8 mx-auto position-relative'
                )
            )
        ),
    ],
        # className='masthead'
        className="bg-secondary text-white text-center py-4",
    ),
    # Note: filters put in separate container to make floating element later
#    dbc.Container(
#        [
#         html.Div(["Select a region:",
#             dcc.Dropdown(
#                       id='region-selection',
#                       options=[{'label': region_names[i], 'value': region_values[i]} for i in range(len(region_values))],
#                       value='CA',
#                       style={'vertical-align': 'left'}
#                   ),
#             ],
#             className='col-md-10 col-lg-8 mx-auto mt-4'
#         ),
#         ], style={'backgroundColor':'F4F5F6'},
#     className='sticky-top bg-light mb-2', fluid=True),
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.Div([
                    "Select a region:",
                    dcc.Dropdown(
                        id='region-selection',
                        options=[{'label': region_names[i], 'value': region_values[i]} for i in range(len(region_values))],
                        value='CA',
                        style={'vertical-align': 'left'}
                    ), html.Br(),
                ], className='m-2 p-2')
            )
        ])
    ],className='sticky-top bg-light mb-2', fluid=True), 
   dbc.Container(
       dbc.Row([
            html.Div(
                [
                    dcc.Markdown('''
                    According to the 2018 General Social Survey on Giving, Volunteering, and Participating, just over two-thirds of Canadians (68%) reported donating to a charitable or nonprofit organization during the one year period prior to the survey. 
                    ''',className='mt-4'),
                    dcc.Markdown('''
                    To gain greater insight into factors that might limit the support that Canadians provide, donors who gave less than $1,150 in the previous year were asked whether any of ten separate factors kept them from giving as much as they would otherwise. Below we explore the impacts these barriers had on giving. The text describes national level findings; for additional detail, readers can use the pull down menu linked to the interactive data visualizations to show regional level results. While the regional specifics may differ from the national level results described in the text, the overall trends were quite similar.
                    '''),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Barriers reported by donors.
            html.Div(
                [
                    dcc.Graph(id='BarriersOverall', style={'marginTop': marginTop}),
                    html.P("Turning to how these potential barriers affect the amounts Canadians donate, effectively reaching donors is clearly a significant factor. Donors who were not asked to give more, found it hard to find a cause worth supporting, or did not know where to donate more all tended to make somewhat smaller donations than donors who did not report these barriers. Those who were unable to afford further donations also tended to give somewhat smaller amounts."),
                    html.P("It is important to understand that while barriers reduce the amounts donors would otherwise have donated, not all of them are associated with smaller absolute donations. Some appear to play a more significant role among donors who make larger donations. Those who are happy with the amounts they have contributed, who have concerns about how requests for donations were made, or gave directly to people in need without going through an organization all tend to make somewhat larger donations than those not reporting these barriers. "),
                    html.P("Finally, some barriers do not appear to drive significant absolute differences in the amounts donated. The amounts typically donated by those concerned that additional donations would not be used efficiently or effectively, who believe that the tax credits received were insufficient as a motivator, or who prefer to volunteer rather than donate do not appear to be statistically different from those not reporting these barriers."),
                    # Average amounts contributed by donors reporting and not reporting specific barriers.
                    dcc.Graph(id='BarriersAvgAmts', style={'marginTop': marginTop}),

                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Concerns about efficiency and effectiveness
            html.Div(
                [
                    html.H5("Concerns about efficiency and effectiveness"),
                    html.P("Donors who did not contribute more because they had concerns about whether their donations would be used effectively or efficiently were asked whether any of three specific factors was a reason for their concern. Put simply, this view appears to be driven by concerns about whether additional donations will be put to good use. Nationally, three in five donors holding this view believe that organizations do not do an adequate job of explaining how additional donations would be used, about half believe organizations spend too much on fundraising and about four in ten say they are unable to see the impacts of their donations on the cause or community being served. About one in eight are concerned about how their donations will be used for some other reason."),
                    html.P("It is important to understand that while barriers reduce the amounts donors would otherwise have donated, not all of them are associated smaller absolute donations. Some appear to play a more significant role among donors who make larger donations. Those who are happy with the amounts they have contributed, who have concerns about how requests for donations were made, or gave directly to people in need without going through an organization all tend to make somewhat larger donations than those not reporting these barriers. "),
                    # Reasons for efficiency / effectiveness concerns.
                    dcc.Graph(id='EfficiencyConcerns', style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [
                    html.H5("Dislike of solicitation methods"),
                    html.P("Donors who did not donate more because they did not like how requests for donations were made were asked what they disliked about the solicitations they received. Overall, the number of requests donors receive is clearly a key concern. Nationally, about half of those limiting donations because they dislike the solicitations they received cited multiple requests from the same organization and the overall number of requests received as reasons for their lack of support. In terms of other drivers, about half disliked the methods organizations used to ask for donations, about two fifths disliked the tone of the ask, and just under a third disliked the typical time of day they received solicitations."),
                    # Reasons for disliking solicitations.
                    dcc.Graph(id='DislikeSolicitations', style={'marginTop': marginTop}),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            # Personal & economic characteristics
            html.Div(
                [
                    html.H3('Personal & economic characteristics'),
                    html.P("Not all Canadians face the same barriers to donating or respond to them in the same way. The incidence of many barriers varies according to the personal and economic characteristics of donors. Below we look at how barriers to donating tend to vary against some of the most important demographic factors. Again, the text describes findings at the national level but readers can use the pull down menu to explore regional level results."),
                    
                    html.Div([
                        html.H5("Gender"),
                        html.P("Nationally, most barriers affect men and women roughly equally, in the sense that they are equally likely to say they limit the amounts they donate. Men and women do differ in a number of key dimensions. Most notably, men are more likely to limit their donations because they find it difficult to find a cause worth supporting, because they do not believe additional donations will be used efficiently, and because they do not like how they were asked to donate. Women are more likely than men to limit their donations because they cannot afford to give more. "),
                        # Barriers to giving more by gender
                    # html.Div([
                    #     "Select a barrier:",
                    #     dcc.Dropdown(
                    #       id='barrier-selection',
                    #       options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(len(barriers_names))],
                    #       value='Happy with what already given',
                    #       style={'verticalAlgin': 'middle'}
                    #     ),
                    #   ],
                    #  className='col-md-10 col-lg-8 mx-auto mt-4'),
                    #  className='sticky-top bg-light mb-2', fluid=True),
                    dbc.Container([
                        html.Div([
                            "Select a barrier:",
                            dcc.Dropdown(
                            id='barrier-selection',
                            options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(len(barriers_names))],
                            value='Happy with what already given',
                            style={'vertical-align': 'right'}
                            ),
                        ],
                            className='col-md-10 col-lg-8 mx-auto mt-4'),
                    ], style={'backgroundColor':'F4F5F6'},),
                    # className='sticky-top bg-light mb-2', fluid=True),
                        html.Div([
                            dcc.Graph(id='Barriers-Gndr', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Age
                    html.Div([
                        html.H5("Age"),
                        html.P("The relationships between barriers and the age of donors are quite variable and a number of different patterns can be seen. Reflecting the larger amounts they typically give, older donors are more likely to limit their donations because they feel they have given enough and because the tax credits they will receive are not sufficient motivation to justify additional donations. Older donors are also more likely to give directly to those in need instead of donating to an organization. Conversely, older donors are less likely to limit their donations because no one asked them to donate or because they preferred to give time instead. Interestingly, both older and younger donors are more likely to limit their donations because they could not afford to give more or because they had difficulty finding a cause worth supporting. Most other barriers have roughly consistent effects on donors, with the exception of those aged 15 to 24. Donors in the youngest age group appear to have less involvement with donating in that they are markedly more likely to not know where to make a donation and less likely to have concerns related to solicitation methods and the efficient use of donations."),
                        # Barriers to giving more by age
                    html.Div([
                        "Select a barrier:",
                        dcc.Dropdown(
                          id='barrier-selection-age',
                          options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(len(barriers_names))],
                          value='Happy with what already given',
                          style={'verticalAlgin': 'middle'}
                        ),
                      ],
                     className='col-md-10 col-lg-8 mx-auto mt-4'),
                        html.Div([
                            dcc.Graph(id='Barriers-Age', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Formal Education
                    html.Div([
                        html.H5("Formal Education"),
                        html.P("The impact of many barriers decreases with level of formal education attained. Those with higher levels of formal education are less likely to not know where to make additional donations, to have difficulty finding a cause worth supporting or to give directly to those in need instead of giving to an organization. Reflecting their generally higher earning potential, those with more formal education are also less likely to limit their donations because they cannot afford to donate more. As a cautionary note, while those with higher levels of formal education typically give larger amounts, they are more likely than other donors to dislike how requests for donations are made. Finally, those who have less than a high school education are somewhat more likely to volunteer time instead of donating."),
                        # Barriers to giving more by formal education
                    html.Div([
                        "Select a barrier:",
                        dcc.Dropdown(
                          id='barrier-selection-educ',
                          options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(len(barriers_names))],
                          value='Happy with what already given',
                          style={'verticalAlgin': 'middle'}
                        ),
                      ],
                     className='col-md-10 col-lg-8 mx-auto mt-4'),
                        html.Div([
                            dcc.Graph(id='Barriers-Educ', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # household income
                    html.Div([
                        html.H5("Income"),
                        html.P("A number of barriers decrease in importance as household income increases, most notably not being able to afford to donate more, volunteering time instead, and giving directly to those in need instead of giving to an organization. Not knowing where to make additional donations and difficulty finding a cause worth supporting also tend to decline as income increases, but these associations are weaker. Other barriers do not seem to vary much with income, at least at the national level."),
                        # Barriers to giving more by household income
                        html.Div([
                        "Select a barrier:",
                        dcc.Dropdown(
                          id='barrier-selection-income',
                          options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(len(barriers_names))],
                          value='Happy with what already given',
                          style={'verticalAlgin': 'middle'}
                        ),
                      ],
                     className='col-md-10 col-lg-8 mx-auto mt-4'),
                        html.Div([
                            dcc.Graph(id='Barriers-Inc', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Religious attendance
                    html.Div([
                        html.H5("Religious Attendance"),
                        html.P("The clearest association between barriers to donating and the frequency of religious attendance is with giving time instead of donating more with more frequent attenders being more likely to report this barrier. Most other barriers do not vary by religious attendance in clear, predictable ways. The most notable exception is that non-attenders and very infrequent attenders are somewhat less likely to give directly to those in need instead of donating to an organization."),
                        # Barriers to giving more by religious attendance
                        html.Div([
                        "Select a barrier:",
                        dcc.Dropdown(
                          id='barrier-selection-religion',
                          options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(len(barriers_names))],
                          value='Happy with what already given',
                          style={'verticalAlgin': 'middle'}
                        ),
                      ],
                     className='col-md-10 col-lg-8 mx-auto mt-4'),
                        html.Div([
                           dcc.Graph(id='Barriers-Relig', style={'marginTop': marginTop}),
                        ]),
                    ]),
                    # Other personal & economic characteristics
                    html.Div([
                        html.H5("Other Factors"),
                        html.P("Much of the patterning by marital and labour force statuses seems primarily be driven by the age of donors. For example, those who are not in the labour force (who tend to be older) are more likely to not donate more because they are satisfied with what they have already given. Similarly, those who are single (and tend to be younger) are more likely to not know where to make a donation and to have difficulty finding a cause worth supporting while those who are widowed are more likely to believe the tax credits they will receive are not sufficient to drive additional donations. Turning to immigration status, being able to reach naturalized Canadians is clearly a challenge; they are more likely to not know where to make additional donations and to have difficulty finding a cause worth supporting."),
                        # Barriers to giving more by marital status
                        # html.Div([
                            # dcc.Graph(id='Barriers-Marstat', style={'marginTop': marginTop}),
                        # ]),
                        # Barriers to giving more by labour force status
                        # html.Div([
                            # dcc.Graph(id='Barriers-Labour', style={'marginTop': marginTop}),
                        # ]),
                        # Barriers to giving more by immigration status
                        # html.Div([
                            # dcc.Graph(id='Barriers-Immstat', style={'marginTop': marginTop})
                        # ]),
                        html.Div([
                            html.Div(['Select status:',
                                      dcc.Dropdown(
                                          id='status-selection',
                                          options=[{'label': status_names[i], 'value': status_names[i]} for i in range(len(status_names))],
                                          value='Marital status',
                                          style={'verticalAlign': 'middle'}
                                      ),],
                                     style={'width': '33%', 'display': 'inline-block'}),
                            html.Div(["Select a barrier:",
                                            dcc.Dropdown(
                                            id='barrier-selection-other',
                                            options=[{'label': barriers_names[i], 'value': barriers_names[i]} for i in range(len(barriers_names))],
                                            value='Happy with what already given',
                                            style={'verticalAlign': 'middle'}
                                      ),],                                     
                                     style={'width': '66%', 'display': 'inline-block'}),
                        ]),
                        dcc.Graph(id='status-sel-barrier', style={'marginTop': marginTop})
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'

            ),
            html.Div(
                [
                    html.Div([
                        html.H4('Causes supported',className='mt-3'),
                        html.P("While the GSS-GVP does not directly collect information about the barriers keeping donors from giving more to individual causes, comparing the barriers faced by those who support and do not support a given cause can provide some insight. The graph below shows the percentages of donors reporting each barrier, sub-divided according to whether they donated to each specific cause. Nationally, a number of associations can be seen. For example, donors to arts & culture and education & research organizations are more likely to have concerns about whether additional donations would be used efficiently and to dislike how they were asked to donate. Donors to religious organizations, on the other hand, are more likely to provide support directly to those in need and to volunteer instead of donating more. Finally, donors to social services organizations are more likely to dislike how they were asked for additional donations and to give directly to those in need instead of providing more support through an organization. Other associations exist, but are weaker."),
                        html.Div([
                            "Select a cause:",
                            dcc.Dropdown(
                                id='cause-selection',
                                options=[{'label': cause_names[i], 'value': cause_names[i]} for i in range(len(cause_names))],
                                value='Arts & culture',
                                style={'verticalAlgin': 'middle'}
                                ),
                            ], className='col-md-10 col-lg-8 mx-auto mt-4'),
                        # Percentages of cause supporters and non-supporters reporting each barrier, by cause
                        dcc.Graph(id='BarriersCauses', style={'marginTop': marginTop}),
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
   ),
   footer
])

################## Graphs #################
# def single_vertical_percentage_graph(dff, title, by="Attribute", sort=False):

#     dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
#                             [dff.Estimate.map(str) + "%" + "*", "...", dff.Estimate.map(str) + "%"])
#     dff['HoverText'] = np.select([dff["Marker"] == "*",
#                                   dff["Marker"] == "...",
#                                   pd.isnull(dff["Marker"])],
#                                  ["Estimate: " + dff.Estimate.map(str) + "% ± " + (dff["CI Upper"] - dff["Estimate"]).map(str) + "%<br><b>Use with caution</b>",
#                                   "Estimate Suppressed",
#                                   "Estimate: " + dff.Estimate.map(str) + "% ± " + (dff["CI Upper"] - dff["Estimate"]).map(str) + "%"])

#     fig = go.Figure()

#     fig.add_trace(go.Bar(x=dff['CI Upper'],
#                          y=dff[by],
#                          orientation="h",
#                          error_x=None,
#                          marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
#                          showlegend=False,
#                          hoverinfo="skip",
#                          text=None,
#                          name="",
#                          textposition="outside",
#                          cliponaxis=False,
#                          offsetgroup=1
#                          ),
#                   )

#     fig.add_trace(go.Bar(x=dff['Estimate'],
#                          y=dff[by],
#                          orientation="h",
#                          error_x=None,
#                          hovertext=dff['HoverText'],
#                          hovertemplate="%{hovertext}",
#                          hoverlabel=dict(font=dict(color="white")),
#                          hoverinfo="text",
#                          marker=dict(color="#c8102e"),
#                          text=dff['Text'],
#                          name="",
#                          textposition='outside',
#                          cliponaxis=False,
#                          offsetgroup=1
#                          ),
#                   )

#     fig.update_layout(title={'text': title,
#                              'y': 0.99},
#                       margin={'l': 30, 'b': 30, 'r': 10, 't': 10},
#                       height=600,
#                       plot_bgcolor='rgba(0, 0, 0, 0)',
#                       showlegend=False,
#                       updatemenus=[
#                           dict(
#                               type="buttons",
#                               xanchor='right',
#                               x=1.2,
#                               y=0.5,
#                               buttons=list([
#                                   dict(
#                                       args=[{"error_x": [None, None],
#                                              "text": [None, dff['Text']]}],
#                                       label="Reset",
#                                       method="restyle"
#                                   ),
#                                   dict(
#                                       args=[{"error_x": [None, dict(type="data", array=dff["CI Upper"] - dff["Estimate"], color="#424242", thickness=1.5)],
#                                              "text": [dff['Text'], None]}],
#                                       label="Confidence Intervals",
#                                       method="restyle"
#                                   )
#                               ]),
#                           ),
#                       ]
#                       )

#     fig.update_xaxes(showgrid=False,
#                      showticklabels=False,
#                      autorange=False,
#                      range=[0, 1.25 * max(dff["CI Upper"])])
#     fig.update_yaxes(autorange="reversed",
#                      ticklabelposition="outside top",
#                      tickfont=dict(size=9))

#     if sort:
#         fig.update_yaxes(categoryorder="total descending")

#     markers = dff["Marker"]
#     if markers.isin(["*"]).any() and markers.isin(["..."]).any():
#         fig.update_layout(margin={'l': 40, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="*<i>Use with caution<br>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     elif markers.isin(["*"]).any():
#         fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="*<i>Use with caution</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     elif markers.isin(["..."]).any():
#         fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="<i>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     else:
#         fig.update_layout(margin={'l': 30, 'b': 30, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.32, x=1.2, align="left", showarrow=False)])

#     return fig

# def vertical_dollar_graph(dff, name1, name2, title):
#     dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
#                             ["$" + dff.Estimate.map(str) + "*", "...", "$" + dff.Estimate.map(str)])
#     dff['HoverText'] = np.select([dff["Marker"] == "*",
#                                   dff["Marker"] == "...",
#                                   pd.isnull(dff["Marker"])],
#                                  ["Estimate: $" + dff.Estimate.map(str) + " ± $" + (dff["CI Upper"] - dff["Estimate"]).map(str) + "<br><b>Use with caution</b>",
#                                   "Estimate Suppressed",
#                                   "Estimate: $" + dff.Estimate.map(str) + " ± $" + (dff["CI Upper"] - dff["Estimate"]).map(str)])

#     dff1 = dff[dff['Attribute'] == name1]

#     dff2 = dff[dff['Attribute'] == name2]

#     fig = go.Figure()

#     fig.add_trace(go.Bar(x=dff1['CI Upper'],
#                          y=dff1['Group'],
#                          orientation="h",
#                          error_x=None,
#                          marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
#                          showlegend=False,
#                          hoverinfo="skip",
#                          text=None,
#                          textposition="outside",
#                          cliponaxis=False,
#                          offsetgroup=2
#                          ),
#                   )

#     fig.add_trace(go.Bar(x=dff2['CI Upper'],
#                          y=dff2['Group'],
#                          orientation="h",
#                          error_x=None,
#                          marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
#                          showlegend=False,
#                          hoverinfo="skip",
#                          text=None,
#                          textposition="outside",
#                          cliponaxis=False,
#                          offsetgroup=1
#                          ),
#                   )

#     fig.add_trace(go.Bar(x=dff1['Estimate'],
#                          y=dff1['Group'],
#                          orientation="h",
#                          error_x=None,
#                          hovertext=dff1['HoverText'],
#                          hovertemplate="%{hovertext}",
#                          hoverlabel=dict(font=dict(color="white")),
#                          hoverinfo="text",
#                          marker=dict(color="#c8102e"),
#                          text=dff1['Text'],
#                          textposition='outside',
#                          cliponaxis=False,
#                          name=name1,
#                          offsetgroup=2
#                          ),
#                   )

#     fig.add_trace(go.Bar(x=dff2['Estimate'],
#                          y=dff2['Group'],
#                          orientation="h",
#                          error_x=None,
#                          hovertext=dff2['HoverText'],
#                          hovertemplate="%{hovertext}",
#                          hoverlabel=dict(font=dict(color="white")),
#                          hoverinfo="text",
#                          marker=dict(color="#7BAFD4"),
#                          text=dff2['Text'],
#                          textposition='outside',
#                          cliponaxis=False,
#                          name=name2,
#                          offsetgroup=1
#                          ),
#                   )

#     fig.update_layout(title={'text': title,
#                              'y': 0.99},
#                       margin={'l': 30, 'b': 30, 'r': 10, 't': 10},
#                       height=600,
#                       plot_bgcolor='rgba(0, 0, 0, 0)',
#                       bargroupgap=0.05,
#                       barmode="group",
#                       legend={'orientation': 'h', 'yanchor': "bottom"},
#                       updatemenus=[
#                           dict(
#                               type="buttons",
#                               xanchor='right',
#                               x=1.2,
#                               y=0.5,
#                               buttons=list([
#                                   dict(
#                                       args=[{"error_x": [None, None, None, None],
#                                              "text": [None, None, dff1['Text'], dff2['Text']]}],
#                                       label="Reset",
#                                       method="restyle"
#                                   ),
#                                   dict(
#                                       args=[{"error_x": [None, None, dict(type="data", array=dff1["CI Upper"] - dff1["Estimate"], color="#424242", thickness=1.5), dict(type="data", array=dff2["CI Upper"] - dff2["Estimate"], color="#424242", thickness=1.5)],
#                                              "text": [dff1['Text'], dff2['Text'], None, None]}],
#                                       label="Confidence Intervals",
#                                       method="restyle"
#                                   )
#                               ]),
#                           ),
#                       ]
#                       )

#     fig.update_xaxes(showgrid=False,
#                      showticklabels=False,
#                      autorange=False,
#                      range=[0, 1.25 * max(np.concatenate([dff1["CI Upper"], dff2["CI Upper"]]))])
#     fig.update_yaxes(autorange="reversed",
#                      ticklabelposition="outside top",
#                      tickfont=dict(size=9),
#                      categoryorder='array',
#                      categoryarray=dff1.sort_values(by="Estimate", ascending=False)["Group"])

#     markers = pd.concat([dff1["Marker"], dff2["Marker"]])
#     if markers.isin(["*"]).any() and markers.isin(["..."]).any():
#         fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="*<i>Use with caution<br>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     elif markers.isin(["*"]).any():
#         fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="*<i>Use with caution</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     elif markers.isin(["..."]).any():
#         fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="<i>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     else:
#         fig.update_layout(margin={'l': 30, 'b': 30, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False)])

#     return fig

# def vertical_percentage_graph(dff, title, name1, name2):
#     dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
#                             [dff.Estimate.map(str) + "%" + "*", "...", dff.Estimate.map(str) + "%"])
#     dff['HoverText'] = np.select([dff["Marker"] == "*",
#                                   dff["Marker"] == "...",
#                                   pd.isnull(dff["Marker"])],
#                                  ["Estimate: " + dff.Estimate.map(str) + "% ± " + (dff["CI Upper"] - dff["Estimate"]).map(str) + "%<br><b>Use with caution</b>",
#                                   "Estimate Suppressed",
#                                   "Estimate: " + dff.Estimate.map(str) + "% ± " + (dff["CI Upper"] - dff["Estimate"]).map(str) + "%"])

#     dff1 = dff[dff['Attribute'] == name1]

#     dff2 = dff[dff['Attribute'] == name2]

#     fig = go.Figure()

#     fig.add_trace(go.Bar(x=dff1['CI Upper'],
#                          y=dff1['QuestionText'],
#                          orientation="h",
#                          error_x=None,
#                          marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
#                          showlegend=False,
#                          hoverinfo="skip",
#                          text=None,
#                          textposition="outside",
#                          cliponaxis=False,
#                          offsetgroup=2
#                          ),
#                   )

#     fig.add_trace(go.Bar(x=dff2['CI Upper'],
#                          y=dff2['QuestionText'],
#                          orientation="h",
#                          error_x=None,
#                          marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
#                          showlegend=False,
#                          hoverinfo="skip",
#                          text=None,
#                          textposition="outside",
#                          cliponaxis=False,
#                          offsetgroup=1
#                          ),
#                   )

#     fig.add_trace(go.Bar(x=dff1['Estimate'],
#                          y=dff1['QuestionText'],
#                          orientation="h",
#                          error_x=None,
#                          hovertext=dff1['HoverText'],
#                          hovertemplate="%{hovertext}",
#                          hoverlabel=dict(font=dict(color="white")),
#                          hoverinfo="text",
#                          marker=dict(color="#c8102e"),
#                          text=dff1['Text'],
#                          textposition='outside',
#                          cliponaxis=False,
#                          name=name1,
#                          offsetgroup=2
#                          ),
#                   )

#     fig.add_trace(go.Bar(x=dff2['Estimate'],
#                          y=dff2['QuestionText'],
#                          orientation="h",
#                          error_x=None,
#                          hovertext=dff2['HoverText'],
#                          hovertemplate="%{hovertext}",
#                          hoverlabel=dict(font=dict(color="white")),
#                          hoverinfo="text",
#                          marker=dict(color="#7BAFD4"),
#                          text=dff2['Text'],
#                          textposition='outside',
#                          cliponaxis=False,
#                          name=name2,
#                          offsetgroup=1
#                          ),
#                   )

#     fig.update_layout(title={'text': title,
#                              'y': 0.99},
#                       margin={'l': 30, 'b': 30, 'r': 10, 't': 10},
#                       height=600,
#                       plot_bgcolor='rgba(0, 0, 0, 0)',
#                       bargroupgap=0.05,
#                       barmode="group",
#                       legend={'orientation': 'h', 'yanchor': "bottom"},
#                       updatemenus=[
#                           dict(
#                               type="buttons",
#                               xanchor='right',
#                               x=1.2,
#                               y=0.5,
#                               buttons=list([
#                                   dict(
#                                       args=[{"error_x": [None, None, None, None],
#                                              "text": [None, None, dff1['Text'], dff2['Text']]}],
#                                       label="Reset",
#                                       method="restyle"
#                                   ),
#                                   dict(
#                                       args=[{"error_x": [None, None, dict(type="data", array=dff1["CI Upper"] - dff1["Estimate"], color="#424242", thickness=1.5), dict(type="data", array=dff2["CI Upper"] - dff2["Estimate"], color="#424242", thickness=1.5)],
#                                              "text": [dff1['Text'], dff2['Text'], None, None]}],
#                                       label="Confidence Intervals",
#                                       method="restyle"
#                                   )
#                               ]),
#                           ),
#                       ]
#                       )

#     fig.update_xaxes(showgrid=False,
#                      showticklabels=False,
#                      autorange=False,
#                      range=[0, 1.25 * max(np.concatenate([dff1["CI Upper"], dff2["CI Upper"]]))])
#     fig.update_yaxes(autorange="reversed",
#                      ticklabelposition="outside top",
#                      tickfont=dict(size=9),
#                      categoryorder='array',
#                      categoryarray=dff1.sort_values(by="Estimate", ascending=False)["QuestionText"])

#     markers = pd.concat([dff1["Marker"], dff2["Marker"]])
#     if markers.isin(["*"]).any() and markers.isin(["..."]).any():
#         fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="*<i>Use with caution<br>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     elif markers.isin(["*"]).any():
#         fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                      dict(text="*<i>Use with caution</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     elif markers.isin(["..."]).any():
#         fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="<i>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     else:
#         fig.update_layout(margin={'l': 30, 'b': 30, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False)])

#     return fig



################## Callbacks #################
@app.callback(
    dash.dependencies.Output('BarriersOverall', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = Barriers_2018[Barriers_2018['Region'] == region]
    dff = dff[dff["Group"] == "All"]
    title = '{}, {}'.format("Barriers reported by donors", region)
    return single_vertical_percentage_graph(dff, title, by="QuestionText", sort=True)

@app.callback(
    dash.dependencies.Output('BarriersAvgAmts', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = AvgAmtBarriers_2018[AvgAmtBarriers_2018['Region'] == region]
    name1 = "Report barrier"
    name2 = "Do not report barrier"
    title = '{}, {}'.format("Average amounts contributed by donors reporting and not reporting specific barriers", region)
    return vertical_dollar_graph(dff, name1, name2, title)


@app.callback(
    dash.dependencies.Output('EfficiencyConcerns', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = GivingConcerns_2018[GivingConcerns_2018['Region'] == region]
    dff = dff[dff["Group"] == "All"]
    title = '{}, {}'.format("Reasons for efficiency / effectiveness concerns", region)
    return single_vertical_percentage_graph(dff, title, by="QuestionText", sort=True)

@app.callback(
    dash.dependencies.Output('DislikeSolicitations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SolicitationConcerns_2018[SolicitationConcerns_2018['Region'] == region]
    dff = dff[dff["Group"] == "All"]
    title = '{}, {}'.format("Reasons for disliking solicitations", region)
    return single_vertical_percentage_graph(dff, title, by="QuestionText", sort=True)

@app.callback(
    dash.dependencies.Output('Barriers-Gndr', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection', 'value')

    ])
def update_graph(region, barrier):
    dff = Barriers_2018[Barriers_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == "Gender"]
    dff = dff[dff["QuestionText"] == barrier]
    title = '{}, {}'.format("Donor barrier: " + str(barrier) + " by gender", region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('Barriers-Age', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection-age', 'value')

    ])
def update_graph(region, barrier):
    dff = Barriers_2018[Barriers_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == "Age group"]
    dff = dff[dff["QuestionText"] == barrier]
    title = '{}, {}'.format("Donor barrier: " + str(barrier) + " by age", region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('Barriers-Educ', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection-educ', 'value')

    ])
def update_graph(region, barrier):
    dff = Barriers_2018[Barriers_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == "Education"]
    dff = dff[dff["QuestionText"] == barrier]
    title = '{}, {}'.format("Donor barrier: " + str(barrier) + " by formal education", region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('Barriers-Inc', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection-income', 'value')

    ])
def update_graph(region, barrier):
    dff = Barriers_2018[Barriers_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == "Family income category"]
    dff = dff[dff["QuestionText"] == barrier]
    title = '{}, {}'.format("Donor barrier: " + str(barrier) + " by household income", region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('Barriers-Relig', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection-religion', 'value')

    ])
def update_graph(region, barrier):
    dff = Barriers_2018[Barriers_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == "Frequency of religious attendance"]
    dff = dff[dff["QuestionText"] == barrier]
    title = '{}, {}'.format("Donor barrier: " + str(barrier) + " by religious attendance", region)
    return single_vertical_percentage_graph(dff, title)

# @app.callback(
#     dash.dependencies.Output('Barriers-Marstat', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value'),
#         dash.dependencies.Input('barrier-selection', 'value')

#     ])
# def update_graph(region, barrier):
#     dff = Barriers_2018[Barriers_2018['Region'] == region]
#     dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
#     dff = dff[dff["Group"] == "Marital status"]
#     dff = dff[dff["QuestionText"] == barrier]
#     title = '{}, {}'.format("Barriers reported by marital status", region)
#     return single_vertical_percentage_graph(dff, title)

# @app.callback(
#     dash.dependencies.Output('Barriers-Labour', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value'),
#         dash.dependencies.Input('barrier-selection', 'value')

#     ])
# def update_graph(region, barrier):
#     dff = Barriers_2018[Barriers_2018['Region'] == region]
#     dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
#     dff = dff[dff["Group"] == "Labour force status"]
#     dff = dff[dff["QuestionText"] == barrier]
#     title = '{}, {}'.format("Barriers reported by labour force status", region)
#     return single_vertical_percentage_graph(dff, title)


# @app.callback(
#     dash.dependencies.Output('Barriers-Immstat', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value'),
#         dash.dependencies.Input('barrier-selection', 'value')
#     ])
# def update_graph(region, barrier):
#     dff = Barriers_2018[Barriers_2018['Region'] == region]
#     dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
#     dff = dff[dff["Group"] == "Immigration status"]
#     dff = dff[dff["QuestionText"] == barrier]
#     title = '{}, {}'.format("Barriers reported by immigration status", region)
#     return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('status-sel-barrier', 'figure'),
    [ 
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('barrier-selection-other', 'value'),
        dash.dependencies.Input('status-selection', 'value')
    ])

def update_graph(region, barrier, status):
    dff = Barriers_2018[Barriers_2018['Region'] == region]
    dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    dff = dff[dff["Group"] == status]
    dff = dff[dff["QuestionText"] == barrier]
    title = '{}, {}'.format("Donor barrier: " + str(barrier).lower() + " by " + str(status).lower(), region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('BarriersCauses', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('cause-selection', 'value')
    ])
def update_graph(region, cause):
    dff = BarriersByCause_2018[BarriersByCause_2018['Region'] == region]
    dff = dff[dff["Group"] == cause]
    name1 = "Support cause"
    name2 = "Do not support cause"
    title = '{}, {}'.format("Percentages of cause supporters and non-supporters reporting each barrier, by cause", region)
    return vertical_percentage_graph(dff, title, name1, name2)