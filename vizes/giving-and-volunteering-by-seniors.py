import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import textwrap

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

SeniorsAvgDonAmt_2018 = pd.read_csv("../tables/2018-SeniorsAvgDonAmt.csv")
SeniorsAvgDonByCause_2018 = pd.read_csv("../tables/2018-SeniorsAvgDonByCause.csv")
SeniorsAvgDonByMeth_2018 = pd.read_csv("../tables/2018-SeniorsAvgDonByMeth.csv")
SeniorsAvgHrs_2018 = pd.read_csv("../tables/2018-SeniorsAvgHrs.csv")
SeniorsAvgHrsByActivity_2018 = pd.read_csv("../tables/2018-SeniorsAvgHrsByActivity.csv")
SeniorsAvgHrsByCause_2018 = pd.read_csv("../tables/2018-SeniorsAvgHrsByCause.csv")
SeniorsAvgHrsCommInvolve_2018 = pd.read_csv("../tables/2018-SeniorsAvgHrsCommInvolve.csv")
SeniorsAvgHrsHelpDirectly_2018 = pd.read_csv("../tables/2018-SeniorsAvgHrsHelpDirectly.csv")
SeniorsBarriers_2018 = pd.read_csv("../tables/2018-SeniorsBarriersGiving.csv")
SeniorsBarriersVol_2018 = pd.read_csv("../tables/2018-SeniorsBarriersVol.csv")
SeniorsCommInvolveRate_2018 = pd.read_csv("../tables/2018-SeniorsCommInvolveRate.csv")
SeniorsDonRateByCause_2018 = pd.read_csv("../tables/2018-SeniorsDonRateByCause.csv")
SeniorsDonRateByMeth_2018 = pd.read_csv("../tables/2018-SeniorsDonRateByMeth.csv")
SeniorsDonRates_2018 = pd.read_csv("../tables/2018-SeniorsDonRates.csv")
SeniorsEfficiencyConcerns_2018 = pd.read_csv("../tables/2018-SeniorsEfficiencyConcerns.csv")
SeniorsHelpDirectlyRate_2018 = pd.read_csv("../tables/2018-SeniorsHelpDirectlyRate.csv")
SeniorsReasonsGiving_2018 = pd.read_csv("../tables/2018-SeniorsReasonsGiving.csv")
SeniorsReasonsVol_2018 = pd.read_csv("../tables/2018-SeniorsReasonsVol.csv")
SeniorsSolicitationConcerns_2018 = pd.read_csv("../tables/2018-SeniorsSolicitationConcerns.csv")
SeniorsVolRateByActivity_2018 = pd.read_csv("../tables/2018-SeniorsVolRateByActivity.csv")
SeniorsVolRateByCause_2018 = pd.read_csv("../tables/2018-SeniorsVolRateByCause.csv")
SeniorsVolRate_2018 = pd.read_csv("../tables/2018-SeniorsVolRates.csv")

rates = [SeniorsBarriers_2018,
         SeniorsBarriersVol_2018,
         SeniorsCommInvolveRate_2018,
         SeniorsDonRateByCause_2018,
         SeniorsDonRateByMeth_2018,
         SeniorsDonRates_2018,
         SeniorsEfficiencyConcerns_2018,
         SeniorsHelpDirectlyRate_2018,
         SeniorsReasonsGiving_2018,
         SeniorsReasonsVol_2018,
         SeniorsSolicitationConcerns_2018,
         SeniorsVolRateByActivity_2018,
         SeniorsVolRateByCause_2018,
         SeniorsVolRate_2018]

data = [SeniorsAvgDonAmt_2018,
        SeniorsAvgDonByCause_2018,
        SeniorsAvgDonByMeth_2018,
        SeniorsAvgHrs_2018,
        SeniorsAvgHrsByActivity_2018,
        SeniorsAvgHrsByCause_2018,
        SeniorsAvgHrsCommInvolve_2018,
        SeniorsAvgHrsHelpDirectly_2018,
        SeniorsBarriers_2018,
        SeniorsBarriersVol_2018,
        SeniorsCommInvolveRate_2018,
        SeniorsDonRateByCause_2018,
        SeniorsDonRateByMeth_2018,
        SeniorsDonRates_2018,
        SeniorsEfficiencyConcerns_2018,
        SeniorsHelpDirectlyRate_2018,
        SeniorsReasonsGiving_2018,
        SeniorsReasonsVol_2018,
        SeniorsSolicitationConcerns_2018,
        SeniorsVolRateByActivity_2018,
        SeniorsVolRateByCause_2018,
        SeniorsVolRate_2018]

for i in range(len(rates)):
    rates[i]['Estimate'] = rates[i]['Estimate'] * 100
    rates[i]['CI Upper'] = rates[i]['CI Upper'] * 100


for i in range(len(data)):
    data[i]["Estimate"] = np.where(data[i]["Marker"] == "...", 0, data[i]["Estimate"])
    data[i]["CI Upper"] = np.where(data[i]["Marker"] == "...", 0, data[i]["CI Upper"])
    data[i]["Group"] = np.where(data[i]["Attribute"] == "Unable to determine", "", data[i]["Group"])
    data[i]["Group"] = np.where(data[i]["Attribute"] == "Unknown", "", data[i]["Group"])

    data[i]['Estimate'] = data[i]['Estimate'].round(0).astype(int)
    data[i]["CI Upper"] = data[i]["CI Upper"].round(0).astype(int)
    data[i]['cv'] = data[i]['cv'].round(2)

    # if not data[i]["Attribute"].isna().all():
    #     data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15)
    #     data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)
    #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Do not support<br>cause", "Do not support cause", data[i]["Attribute"])
    #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Do not report<br>barrier", "Do not report barrier", data[i]["Attribute"])
    #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Report<br>barrier", "Report barrier", data[i]["Attribute"])

    data[i]["QuestionText"] = data[i]["QuestionText"].str.wrap(20)
    data[i]["QuestionText"] = data[i]["QuestionText"].replace({'\n': '<br>'}, regex=True)

region_values = np.array(['CA', 'BC', 'AB', 'PR', 'ON', 'QC', 'AT'], dtype=object)
region_names = np.array(['Canada',
                         'British Columbia',
                         'Alberta',
                         'Prairie Provinces (SK, MB)',
                         'Ontario',
                         'Quebec',
                         'Atlantic Provinces (NB, NS, PE, NL)'], dtype=str)

app.layout = html.Div([
    html.Div([
        html.H1('Giving and Volunteering by Seniors')]),
    html.Div([
        html.Div(["Select a region of focus:",
                  dcc.Dropdown(
                      id='region-selection',
                      options=[{'label': region_names[i], 'value': region_values[i]} for i in range(len(region_values))],
                      value='CA',
                      style={'verticalAlgin': 'middle'}
                  ),
                  ],
                 style={'width': '33%', 'display': 'inline-block'})
    ]),
    html.Div([
        dcc.Graph(id='SeniorsDonRateAmt', style={'marginTop': 50}),
        dcc.Graph(id='SeniorsDonRateByCause', style={'marginTop': 50}),
        dcc.Graph(id='SeniorsAvgAmtByCause', style={'marginTop': 50}),
        dcc.Graph(id='SeniorsDonRateByMeth', style={'marginTop': 50}),
        dcc.Graph(id='SeniorsAvgAmtByMeth', style={'marginTop': 50}),
        dcc.Graph(id='SeniorsMotivations', style={'marginTop': 50}),
        dcc.Graph(id='SeniorsBarriers', style={'marginTop': 50}),
        dcc.Graph(id='SeniorsEfficiency', style={'marginTop': 50}),
        dcc.Graph(id='SeniorsSolicitations', style={'marginTop': 50}),
        dcc.Graph(id='SeniorsVolRateVolAmt', style={'marginTop': 50}),
        dcc.Graph(id='SeniorsVolRateByCause', style={'marginTop': 50}),
        dcc.Graph(id='SeniorsAvgHrsByCause', style={'marginTop': 50}),
        dcc.Graph(id='SeniorsVolRateByActivity', style={'marginTop': 50}),
        dcc.Graph(id='SeniorsAvgHrsByActivity', style={'marginTop': 50}),
        dcc.Graph(id='SeniorsVolMotivations', style={'marginTop': 50}),
        dcc.Graph(id='SeniorsVolBarriers', style={'marginTop': 50}),
        dcc.Graph(id='SeniorsRateHelpDirect', style={'marginTop': 50}),
        dcc.Graph(id='SeniorsHrsHelpDirect', style={'marginTop': 50}),
        dcc.Graph(id='SeniorsRateCommInvolve', style={'marginTop': 50}),
        dcc.Graph(id='SeniorsHrsCommInvolve', style={'marginTop': 50})
    ],
        style={'width': '50%', 'display': 'inline-block', "marginTop": 20}),
])


def triple_horizontal_rate_avg(dff_1, dff_2, name1, name2, name3, title, giving=True):
    dff_1['Text'] = np.select([dff_1["Marker"] == "*", dff_1["Marker"] == "...", pd.isnull(dff_1["Marker"])],
                              [dff_1.Estimate.map(str) + "%*", "...", dff_1.Estimate.map(str)+"%"])
    dff_1['HoverText'] = np.select([dff_1["Marker"] == "*",
                                    dff_1["Marker"] == "...",
                                    pd.isnull(dff_1["Marker"])],
                                   ["Estimate: " + dff_1.Estimate.map(str) + "% ± " + (dff_1["CI Upper"] - dff_1["Estimate"]).map(str) + "%<br><b>Use with caution</b>",
                                    "Estimate Suppressed",
                                    "Estimate: " + dff_1.Estimate.map(str) + "% ± " + (dff_1["CI Upper"] - dff_1["Estimate"]).map(str)+"%"])

    if giving:
        dff_2['Text'] = np.select([dff_2["Marker"] == "*", dff_2["Marker"] == "...", pd.isnull(dff_2["Marker"])],
                                  ["$" + dff_2.Estimate.map(str) + "*", "...", "$" + dff_2.Estimate.map(str)])
        dff_2['HoverText'] = np.select([dff_2["Marker"] == "*",
                                        dff_2["Marker"] == "...",
                                        pd.isnull(dff_2["Marker"])],
                                       ["Estimate: $" + dff_2.Estimate.map(str) + " ± $" + (dff_2["CI Upper"] - dff_2["Estimate"]).map(str) + "<br><b>Use with caution</b>",
                                        "Estimate Suppressed",
                                        "Estimate: $" + dff_2.Estimate.map(str) + " ± $" + (dff_2["CI Upper"] - dff_2["Estimate"]).map(str)])
        dff_1['QuestionText'] = np.select([dff_1["QuestionText"] == 'Donor flag', dff_1["QuestionText"] == 'Secular donor flag', dff_1["QuestionText"] == 'Religious donor flag'],
                                          ["Giving overall", "Secular giving", "Religious giving"])
        dff_2['QuestionText'] = np.select([dff_2["QuestionText"] == 'Total donation<br>amount', dff_2["QuestionText"] == 'Secular donation<br>amount', dff_2["QuestionText"] == 'Religious donation<br>amount'],
                                          ["Giving overall", "Secular giving", "Religious giving"])
    else:
        dff_2['Text'] = np.select([dff_2["Marker"] == "*", dff_2["Marker"] == "...", pd.isnull(dff_2["Marker"])],
                                  [dff_2.Estimate.map(str) + "*", "...", dff_2.Estimate.map(str)])
        dff_2['HoverText'] = np.select([dff_2["Marker"] == "*",
                                        dff_2["Marker"] == "...",
                                        pd.isnull(dff_2["Marker"])],
                                       ["Estimate: " + dff_2.Estimate.map(str) + " ± " + (dff_2["CI Upper"] - dff_2["Estimate"]).map(str) + "<br><b>Use with caution</b>",
                                        "Estimate Suppressed",
                                        "Estimate: " + dff_2.Estimate.map(str) + " ± " + (dff_2["CI Upper"] - dff_2["Estimate"]).map(str)])
        dff_1['QuestionText'] = np.select([dff_1["QuestionText"] == 'Volunteer flag', dff_1["QuestionText"] == 'Direct help flag', dff_1["QuestionText"] == 'Community<br>involvement flag'],
                                          ["Volunteering", "Helping others", "Community engagement"])
        dff_2['QuestionText'] = np.select([dff_2["QuestionText"] == 'Total formal<br>volunteer hours', dff_2["QuestionText"] == 'Total hours spent<br>helping directly', dff_2["QuestionText"] == 'Total hours spent on<br>community<br>involvement'],
                                          ["Volunteering", "Helping others", "Community engagement"])

    dff1 = dff_1[dff_1['Attribute'] == name1]

    dff2 = dff_1[dff_1['Attribute'] == name2]

    dff3 = dff_1[dff_1['Attribute'] == name3]

    dff4 = dff_2[dff_2['Attribute'] == name1]

    dff5 = dff_2[dff_2['Attribute'] == name2]

    dff6 = dff_2[dff_2['Attribute'] == name3]

    fig = go.Figure()

    fig.add_trace(go.Bar(y=dff1['CI Upper'],
                         x=dff1['QuestionText'],
                         error_y=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=2,
                         yaxis='y2'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff2['CI Upper'],
                         x=dff2['QuestionText'],
                         error_y=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=1,
                         yaxis='y2'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff3['CI Upper'],
                         x=dff3['QuestionText'],
                         error_y=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=3,
                         yaxis='y2'
                         ),
                  )

    fig.add_trace(go.Bar(y=[0, 0, 0],
                         x=dff6['QuestionText'],
                         width=[0.5,0.5,0.5],
                         cliponaxis=False,
                         showlegend=False,
                         offsetgroup=4,
                         yaxis='y1'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff4['CI Upper'],
                         x=dff4['QuestionText'],
                         error_y=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=5,
                         yaxis='y1'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff5['CI Upper'],
                         x=dff5['QuestionText'],
                         error_y=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=6,
                         yaxis='y1'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff6['CI Upper'],
                         x=dff6['QuestionText'],
                         error_y=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=7,
                         yaxis='y1'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff1['Estimate'],
                         x=dff1['QuestionText'],
                         error_y=None,
                         hovertext=dff1['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#c8102e"),
                         text=dff1['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         name=name1,
                         offsetgroup=2,
                         yaxis='y2'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff2['Estimate'],
                         x=dff2['QuestionText'],
                         error_y=None,
                         hovertext=dff2['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#7BAFD4"),
                         text=dff2['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         name=name2,
                         offsetgroup=1, yaxis='y2'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff3['Estimate'],
                         x=dff3['QuestionText'],
                         error_y=None,
                         hovertext=dff3['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#50a684"),
                         text=dff3['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         name=name3,
                         offsetgroup=3, yaxis='y2'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff4['Estimate'],
                         x=dff4['QuestionText'],
                         error_y=None,
                         hovertext=dff4['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#c8102e"),
                         text=dff4['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         showlegend=False,
                         offsetgroup=5,
                         yaxis='y1'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff5['Estimate'],
                         x=dff5['QuestionText'],
                         error_y=None,
                         hovertext =dff5['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#7BAFD4"),
                         text=dff5['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         showlegend=False,
                         offsetgroup=6,
                         yaxis='y1'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff6['Estimate'],
                         x=dff6['QuestionText'],
                         error_y=None,
                         hovertext=dff6['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#50a684"),
                         text=dff6['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         showlegend=False,
                         offsetgroup=7,
                         yaxis='y1'
                         ),
                  )


    y2 = go.layout.YAxis(overlaying='y',
                         side='left',
                         autorange = False,
                         range = [0, 1.25*max(np.concatenate([dff1["CI Upper"], dff2["CI Upper"], dff3["CI Upper"]]))])
    y1 = go.layout.YAxis(overlaying='y',
                         side='right',
                         autorange = False,
                         range = [0, 1.25*max(np.concatenate([dff4["CI Upper"], dff5["CI Upper"], dff6["CI Upper"]]))])

    fig.update_layout(title={'text': title,
                             'y': 0.99},
                      margin={'l': 30, 'b': 30, 'r': 10, 't': 10},
                      height=600,
                      plot_bgcolor='rgba(0, 0, 0, 0)',
                      bargroupgap=0.05,
                      yaxis2=y2,
                      yaxis1=y1,
                      barmode="group",
                      legend={'orientation': 'h', 'yanchor': "bottom", "xanchor": "center", "x": 0.5},
                      updatemenus=[
                          dict(
                              type = "buttons",
                              xanchor='right',
                              x = 1.2,
                              y = 0.5,
                              buttons=list([
                                  dict(
                                      args=[{"error_y": [None, None, None, None, None, None, None, None, None, None, None, None, None],
                                             "text": [None, None, None, None, None, None, None, dff1['Text'], dff2['Text'], dff3['Text'], dff4['Text'], dff5['Text'], dff6['Text']]}],
                                      label="Reset",
                                      method="restyle"
                                  ),
                                  dict(
                                      args=[{"error_y": [None, None, None, None, None, None, None,
                                                         dict(type="data", array=dff1["CI Upper"]-dff1["Estimate"], color="#424242", thickness=1.5),
                                                         dict(type="data", array=dff2["CI Upper"]-dff2["Estimate"], color="#424242", thickness=1.5),
                                                         dict(type="data", array=dff3["CI Upper"]-dff3["Estimate"], color="#424242", thickness=1.5),
                                                         dict(type="data", array=dff4["CI Upper"]-dff4["Estimate"], color="#424242", thickness=1.5),
                                                         dict(type="data", array=dff5["CI Upper"]-dff5["Estimate"], color="#424242", thickness=1.5),
                                                         dict(type="data", array=dff6["CI Upper"]-dff6["Estimate"], color="#424242", thickness=1.5)],
                                             "text": [dff1['Text'], dff2['Text'], dff3['Text'], None, dff4['Text'], dff5['Text'], dff6['Text'], None, None, None, None, None, None]}],
                                      label="Confidence Intervals",
                                      method="restyle"
                                  )
                              ]),
                          ),
                      ]
                      )

    fig.update_yaxes(showgrid=False,
                     showticklabels=False)
    fig.update_xaxes(ticklabelposition="outside top",
                     tickfont=dict(size=12))

    markers = pd.concat([dff1["Marker"], dff2["Marker"], dff3["Marker"], dff4["Marker"], dff5["Marker"], dff6["Marker"]])
    if markers.isin(["*"]).any() and markers.isin(["..."]).any():
        fig.update_layout(margin={'l': 40, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="*<i>Use with caution<br>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    elif markers.isin(["*"]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="*<i>Use with caution</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    elif markers.isin(["..."]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="<i>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    else:
        fig.update_layout(margin={'l': 30, 'b': 30, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.32, x=1.2, align="left", showarrow=False)])

    return fig


def vertical_double_graph(dff, title, name1, name2, type, seniors=False):
    if type == "percent":
        dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
                                [dff.Estimate.map(str) + "%" + "*", "...", dff.Estimate.map(str) + "%"])
        dff['HoverText'] = np.select([dff["Marker"] == "*",
                                      dff["Marker"] == "...",
                                      pd.isnull(dff["Marker"])],
                                     ["Estimate: " + dff.Estimate.map(str) + "% ± " + (dff["CI Upper"] - dff["Estimate"]).map(str) + "%<br><b>Use with caution</b>",
                                      "Estimate Suppressed",
                                      "Estimate: " + dff.Estimate.map(str) + "% ± " + (dff["CI Upper"] - dff["Estimate"]).map(str) + "%"])
    elif type == "dollar":
        dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
                                ["$" + dff.Estimate.map(str) + "*", "...", "$" + dff.Estimate.map(str)])
        dff['HoverText'] = np.select([dff["Marker"] == "*",
                                      dff["Marker"] == "...",
                                      pd.isnull(dff["Marker"])],
                                     ["Estimate: $" + dff.Estimate.map(str) + " ± $" + (dff["CI Upper"] - dff["Estimate"]).map(str) + "<br><b>Use with caution</b>",
                                      "Estimate Suppressed",
                                      "Estimate: $" + dff.Estimate.map(str) + " ± $" + (dff["CI Upper"] - dff["Estimate"]).map(str)])

    elif type == "hours":
        dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
                                [dff.Estimate.map(str) + "*", "...", dff.Estimate.map(str)])
        dff['HoverText'] = np.select([dff["Marker"] == "*",
                                      dff["Marker"] == "...",
                                      pd.isnull(dff["Marker"])],
                                     ["Estimate: " + dff.Estimate.map(str) + " ± " + (dff["CI Upper"] - dff["Estimate"]).map(str) + "<br><b>Use with caution</b>",
                                      "Estimate Suppressed",
                                      "Estimate: " + dff.Estimate.map(str) + " ± " + (dff["CI Upper"] - dff["Estimate"]).map(str)])

    dff1 = dff[dff['Attribute'] == name1]

    dff2 = dff[dff['Attribute'] == name2]

    fig = go.Figure()

    fig.add_trace(go.Bar(x=dff1['CI Upper'],
                         y=dff1['QuestionText'],
                         orientation="h",
                         error_x=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=2
                         ),
                  )

    fig.add_trace(go.Bar(x=dff2['CI Upper'],
                         y=dff2['QuestionText'],
                         orientation="h",
                         error_x=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=1
                         ),
                  )

    fig.add_trace(go.Bar(x=dff1['Estimate'],
                         y=dff1['QuestionText'],
                         orientation="h",
                         error_x=None,
                         hovertext=dff1['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#c8102e"),
                         text=dff1['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         name=name1,
                         offsetgroup=2
                         ),
                  )

    fig.add_trace(go.Bar(x=dff2['Estimate'],
                         y=dff2['QuestionText'],
                         orientation="h",
                         error_x=None,
                         hovertext=dff2['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#7BAFD4"),
                         text=dff2['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         name=name2,
                         offsetgroup=1
                         ),
                  )

    fig.update_layout(title={'text': title,
                             'y': 0.99},
                      margin={'l': 30, 'b': 30, 'r': 10, 't': 10},
                      height=600,
                      plot_bgcolor='rgba(0, 0, 0, 0)',
                      bargroupgap=0.05,
                      barmode="group",
                      legend={'orientation': 'h', 'yanchor': "bottom"},
                      updatemenus=[
                          dict(
                              type="buttons",
                              xanchor='right',
                              x=1.2,
                              y=0.5,
                              buttons=list([
                                  dict(
                                      args=[{"error_x": [None, None, None, None],
                                             "text": [None, None, dff1['Text'], dff2['Text']]}],
                                      label="Reset",
                                      method="restyle"
                                  ),
                                  dict(
                                      args=[{"error_x": [None, None, dict(type="data", array=dff1["CI Upper"] - dff1["Estimate"], color="#424242", thickness=1.5), dict(type="data", array=dff2["CI Upper"] - dff2["Estimate"], color="#424242", thickness=1.5)],
                                             "text": [dff1['Text'], dff2['Text'], None, None]}],
                                      label="Confidence Intervals",
                                      method="restyle"
                                  )
                              ]),
                          ),
                      ]
                      )

    if seniors:
        array = dff2.sort_values(by="Estimate", ascending=False)["QuestionText"]
    else:
        array = dff1.sort_values(by="Estimate", ascending=False)["QuestionText"]
    fig.update_xaxes(showgrid=False,
                     showticklabels=False,
                     autorange=False,
                     range=[0, 1.25 * max(np.concatenate([dff1["CI Upper"], dff2["CI Upper"]]))])
    fig.update_yaxes(autorange="reversed",
                     ticklabelposition="outside top",
                     tickfont=dict(size=11),
                     categoryorder='array',
                     categoryarray=array)

    markers = pd.concat([dff1["Marker"], dff2["Marker"]])
    if markers.isin(["*"]).any() and markers.isin(["..."]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="*<i>Use with caution<br>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    elif markers.isin(["*"]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="*<i>Use with caution</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    elif markers.isin(["..."]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="<i>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    else:
        fig.update_layout(margin={'l': 30, 'b': 30, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False)])

    return fig


def triple_vertical_graphs_pops(dff, title, name1, name2, name3, type):
    if type == "percent":
        dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
                                [dff.Estimate.map(str)+"%"+"*", "...", dff.Estimate.map(str)+"%"])
        dff['HoverText'] = np.select([dff["Marker"] == "*",
                                      dff["Marker"] == "...",
                                      pd.isnull(dff["Marker"])],
                                     ["Estimate: "+dff.Estimate.map(str)+"% ± "+(dff["CI Upper"] - dff["Estimate"]).map(str)+"%<br><b>Use with caution</b>",
                                      "Estimate Suppressed",
                                      "Estimate: "+dff.Estimate.map(str)+"% ± "+(dff["CI Upper"] - dff["Estimate"]).map(str)+"%"])
    elif type == "hours":
        dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
                                [dff.Estimate.map(str)+"*", "...", dff.Estimate.map(str)])
        dff['HoverText'] = np.select([dff["Marker"] == "*",
                                      dff["Marker"] == "...",
                                      pd.isnull(dff["Marker"])],
                                     ["Estimate: "+dff.Estimate.map(str)+" ± "+(dff["CI Upper"] - dff["Estimate"]).map(str)+"<br><b>Use with caution</b>",
                                      "Estimate Suppressed",
                                      "Estimate: "+dff.Estimate.map(str)+" ± "+(dff["CI Upper"] - dff["Estimate"]).map(str)])
    elif type == "dollar":
        dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
                                ["$"+dff.Estimate.map(str)+"*", "...", "$"+dff.Estimate.map(str)])
        dff['HoverText'] = np.select([dff["Marker"] == "*",
                                      dff["Marker"] == "...",
                                      pd.isnull(dff["Marker"])],
                                     ["Estimate: $"+dff.Estimate.map(str)+" ± $"+(dff["CI Upper"] - dff["Estimate"]).map(str)+"<br><b>Use with caution</b>",
                                      "Estimate Suppressed",
                                      "Estimate: $"+dff.Estimate.map(str)+" ± $"+(dff["CI Upper"] - dff["Estimate"]).map(str)])

    dff1 = dff[dff['Attribute'] == name1]

    dff2 = dff[dff['Attribute'] == name2]

    dff3 = dff[dff['Attribute'] == name3]


    fig = go.Figure()

    fig.add_trace(go.Bar(x=dff1['CI Upper'],
                         y=dff1['QuestionText'],
                         orientation="h",
                         error_x=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=2
                         ),
                  )

    fig.add_trace(go.Bar(x=dff2['CI Upper'],
                         y=dff2['QuestionText'],
                         orientation="h",
                         error_x=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=1
                         ),
                  )

    fig.add_trace(go.Bar(x=dff3['CI Upper'],
                         y=dff3['QuestionText'],
                         orientation="h",
                         error_x=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=3
                         ),
                  )

    fig.add_trace(go.Bar(x=dff1['Estimate'],
                         y=dff1['QuestionText'],
                         orientation="h",
                         error_x=None,
                         hovertext=dff1['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#c8102e"),
                         text=dff1['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         name=name1,
                         offsetgroup=2
                         ),
                  )

    fig.add_trace(go.Bar(x=dff2['Estimate'],
                         y=dff2['QuestionText'],
                         orientation="h",
                         error_x=None,
                         hovertext =dff2['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#7BAFD4"),
                         text=dff2['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         name=name2,
                         offsetgroup=1
                         ),
                  )

    fig.add_trace(go.Bar(x=dff3['Estimate'],
                         y=dff3['QuestionText'],
                         orientation="h",
                         error_x=None,
                         hovertext=dff3['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#50a684"),
                         text=dff3['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         name=name3,
                         offsetgroup=3
                         ),
                  )

    fig.update_layout(title={'text': title,
                             'y': 0.99},
                      margin={'l': 30, 'b': 30, 'r': 10, 't': 10},
                      height=600,
                      plot_bgcolor='rgba(0, 0, 0, 0)',
                      bargroupgap=0.05,
                      barmode="group",
                      legend={'orientation': 'h', 'yanchor': "bottom"},
                      updatemenus=[
                          dict(
                              type = "buttons",
                              xanchor='right',
                              x = 1.2,
                              y = 0.5,
                              buttons=list([
                                  dict(
                                      args=[{"error_x": [None, None, None, None, None, None],
                                             "text": [None, None, None, dff1['Text'], dff2['Text'], dff3['Text']]}],
                                      label="Reset",
                                      method="restyle"
                                  ),
                                  dict(
                                      args=[{"error_x": [None, None, None, dict(type="data", array=dff1["CI Upper"]-dff1["Estimate"], color="#424242", thickness=1.5),
                                                         dict(type="data", array=dff2["CI Upper"]-dff2["Estimate"], color="#424242", thickness=1.5),
                                                         dict(type="data", array=dff3["CI Upper"]-dff3["Estimate"], color="#424242", thickness=1.5)],
                                             "text": [dff1['Text'], dff2['Text'], dff3['Text'], None, None, None]}],
                                      label="Confidence Intervals",
                                      method="restyle"
                                  )
                              ]),
                          ),
                      ]
                      )

    fig.update_xaxes(showgrid=False,
                     showticklabels=False,
                     autorange=False,
                     range=[0, 1.25*max(np.concatenate([dff1["CI Upper"], dff2["CI Upper"], dff3["CI Upper"]]))])
    fig.update_yaxes(autorange="reversed",
                     ticklabelposition="outside top",
                     tickfont=dict(size=11),
                     categoryorder='array',
                     categoryarray=dff2.sort_values(by="Estimate", ascending=False)["QuestionText"])

    markers = pd.concat([dff1["Marker"], dff2["Marker"], dff3["Marker"]])
    if markers.isin(["*"]).any() and markers.isin(["..."]).any():
        fig.update_layout(margin={'l': 40, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="*<i>Use with caution<br>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    elif markers.isin(["*"]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="*<i>Use with caution</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    elif markers.isin(["..."]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="<i>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    else:
        fig.update_layout(margin={'l': 30, 'b': 30, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.32, x=1.2, align="left", showarrow=False)])

    return fig

@app.callback(
    dash.dependencies.Output('SeniorsDonRateAmt', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = SeniorsDonRates_2018[SeniorsDonRates_2018['Region'] == region]
    dff1 = dff1[dff1["Group"] == "Senior"]

    dff2 = SeniorsAvgDonAmt_2018[SeniorsAvgDonAmt_2018['Region'] == region]
    dff2 = dff2[dff2["Group"] == "Senior"]

    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Donation rate and average donation amount", region)
    return triple_horizontal_rate_avg(dff1, dff2, name1, name2, name3, title, "dollar")


@app.callback(
    dash.dependencies.Output('SeniorsDonRateByCause', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsDonRateByCause_2018[SeniorsDonRateByCause_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Donation rate by cause", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('SeniorsAvgAmtByCause', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsAvgDonByCause_2018[SeniorsAvgDonByCause_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior2"]
    name1 = "15 to 64"
    name2 = "65 plus"
    title = '{}, {}'.format("Average amount donated by cause", region)
    return vertical_double_graph(dff, title, name1, name2, "dollar", seniors=True)


@app.callback(
    dash.dependencies.Output('SeniorsDonRateByMeth', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsDonRateByMeth_2018[SeniorsDonRateByMeth_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Donation rate by method", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('SeniorsAvgAmtByMeth', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsAvgDonByMeth_2018[SeniorsAvgDonByMeth_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior2"]
    name1 = "15 to 64"
    name2 = "65 plus"
    title = '{}, {}'.format("Donation rate by method", region)
    return vertical_double_graph(dff, title, name1, name2, "dollar", seniors=True)


@app.callback(
    dash.dependencies.Output('SeniorsMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsReasonsGiving_2018[SeniorsReasonsGiving_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Motivations for donating", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('SeniorsBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsBarriers_2018[SeniorsBarriers_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Barriers to donating more", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('SeniorsEfficiency', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsEfficiencyConcerns_2018[SeniorsEfficiencyConcerns_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Reasons for concern about efficiency", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('SeniorsSolicitations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsSolicitationConcerns_2018[SeniorsSolicitationConcerns_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Reasons for disliking solicitations", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")



@app.callback(
    dash.dependencies.Output('SeniorsVolRateVolAmt', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = SeniorsVolRate_2018[SeniorsVolRate_2018['Region'] == region]
    dff1 = dff1[dff1["Group"] == "Senior"]

    dff2 = SeniorsAvgHrs_2018[SeniorsAvgHrs_2018['Region'] == region]
    dff2 = dff2[dff2["Group"] == "Senior"]

    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Rates and average hours devoted to volunteering, helping others and community engagement", region)
    return triple_horizontal_rate_avg(dff1, dff2, name1, name2, name3, title, giving=False)


@app.callback(
    dash.dependencies.Output('SeniorsVolRateByCause', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsVolRateByCause_2018[SeniorsVolRateByCause_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior2"]
    name1 = "15 to 64"
    name2 = "65 plus"
    title = '{}, {}'.format("Volunteer rate by cause", region)
    return vertical_double_graph(dff, title, name1, name2, "percent", seniors=True)


@app.callback(
    dash.dependencies.Output('SeniorsAvgHrsByCause', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsAvgHrsByCause_2018[SeniorsAvgHrsByCause_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior2"]
    name1 = "15 to 64"
    name2 = "65 plus"
    title = '{}, {}'.format("Average hours volunteered by cause", region)
    return vertical_double_graph(dff, title, name1, name2, "hours", seniors=True)


@app.callback(
    dash.dependencies.Output('SeniorsVolRateByActivity', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsVolRateByActivity_2018[SeniorsVolRateByActivity_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Volunteer rate by activity", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('SeniorsAvgHrsByActivity', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsAvgHrsByActivity_2018[SeniorsAvgHrsByActivity_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior2"]
    dff = dff[dff["Group"] == "Senior2"]
    name1 = "15 to 64"
    name2 = "65 plus"
    title = '{}, {}'.format("Average hours volunteered by activity", region)
    return vertical_double_graph(dff, title, name1, name2, "hours", seniors=True)


@app.callback(
    dash.dependencies.Output('SeniorsVolMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsReasonsVol_2018[SeniorsReasonsVol_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Motivations for volunteering", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('SeniorsVolBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsBarriersVol_2018[SeniorsBarriersVol_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Barriers to volunteering more", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('SeniorsRateHelpDirect', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsHelpDirectlyRate_2018[SeniorsHelpDirectlyRate_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Methods of helping others directly", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('SeniorsHrsHelpDirect', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsAvgHrsHelpDirectly_2018[SeniorsAvgHrsHelpDirectly_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior2"]
    name1 = "15 to 64"
    name2 = "65 plus"
    title = '{}, {}'.format("Average hours devoted to means of helping others directly", region)
    return vertical_double_graph(dff, title, name1, name2, "hours", seniors=True)


@app.callback(
    dash.dependencies.Output('SeniorsRateCommInvolve', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsCommInvolveRate_2018[SeniorsCommInvolveRate_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Types of community engagement", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('SeniorsHrsCommInvolve', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsAvgHrsCommInvolve_2018[SeniorsAvgHrsCommInvolve_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior2"]
    name1 = "15 to 64"
    name2 = "65 plus"
    title = '{}, {}'.format("Average hours devoted to forms of community engagement", region)
    return vertical_double_graph(dff, title, name1, name2, "hours", seniors=True)


if __name__ == '__main__':
    app.run_server(debug=True)
