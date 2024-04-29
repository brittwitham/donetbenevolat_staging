import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc

# from utils.graphs.WDA0101_graph_utils import *
# from utils.data.HDC0102_data_utils import get_data, process_data, process_data_num

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

SubSecAvgDon_2018 = pd.read_csv("../tables/2018-SubSecAvgDon.csv")
SubSecDonRates_2018 = pd.read_csv("../tables/2018-SubSecDonRates.csv")
SubSecAvgHrs_2018 = pd.read_csv("../tables/2018-SubSecAvgHrs.csv")
SubSecVolRates_2018 = pd.read_csv("../tables/2018-SubSecVolRates.csv")
ArtRecDonorsBarriers_2018 = pd.read_csv("../tables/2018-ArtRecDonorsBarriers.csv")
ArtRecDonorsDonMeth_2018 = pd.read_csv("../tables/2018-ArtRecDonorsDonMeth.csv")
ArtRecDonorsDonRates_2018 = pd.read_csv("../tables/2018-ArtRecDonorsDonRates.csv")
ArtRecDonorsMotivations_2018 = pd.read_csv("../tables/2018-ArtRecDonorsMotivations.csv")
ArtRecVolsActivities_2018 = pd.read_csv("../tables/2018-ArtRecVolsActivities.csv")
ArtRecVolsBarriers_2018 = pd.read_csv("../tables/2018-ArtRecVolsBarriers.csv")
ArtRecVolsMotivations_2018 = pd.read_csv("../tables/2018-ArtRecVolsReasons.csv")
ArtRecVolsVolRates_2018 = pd.read_csv("../tables/2018-ArtRecVolsVolRates.csv")

SubSecDonRates_2018['Estimate'] = SubSecDonRates_2018['Estimate']*100
SubSecDonRates_2018['CI Upper'] = SubSecDonRates_2018['CI Upper']*100
SubSecVolRates_2018['Estimate'] = SubSecVolRates_2018['Estimate']*100
SubSecVolRates_2018['CI Upper'] = SubSecVolRates_2018['CI Upper']*100
ArtRecDonorsBarriers_2018['Estimate'] = ArtRecDonorsBarriers_2018['Estimate']*100
ArtRecDonorsBarriers_2018['CI Upper'] = ArtRecDonorsBarriers_2018['CI Upper']*100
ArtRecDonorsDonMeth_2018['Estimate'] = ArtRecDonorsDonMeth_2018['Estimate']*100
ArtRecDonorsDonMeth_2018['CI Upper'] = ArtRecDonorsDonMeth_2018['CI Upper']*100
ArtRecDonorsDonRates_2018['Estimate'] = ArtRecDonorsDonRates_2018['Estimate']*100
ArtRecDonorsDonRates_2018['CI Upper'] = ArtRecDonorsDonRates_2018['CI Upper']*100
ArtRecDonorsMotivations_2018['Estimate'] = ArtRecDonorsMotivations_2018['Estimate']*100
ArtRecDonorsMotivations_2018['CI Upper'] = ArtRecDonorsMotivations_2018['CI Upper']*100
ArtRecVolsActivities_2018['Estimate'] = ArtRecVolsActivities_2018['Estimate']*100
ArtRecVolsActivities_2018['CI Upper'] = ArtRecVolsActivities_2018['CI Upper']*100
ArtRecVolsBarriers_2018['Estimate'] = ArtRecVolsBarriers_2018['Estimate']*100
ArtRecVolsBarriers_2018['CI Upper'] = ArtRecVolsBarriers_2018['CI Upper']*100
ArtRecVolsMotivations_2018['Estimate'] = ArtRecVolsMotivations_2018['Estimate']*100
ArtRecVolsMotivations_2018['CI Upper'] = ArtRecVolsMotivations_2018['CI Upper']*100
ArtRecVolsVolRates_2018['Estimate'] = ArtRecVolsVolRates_2018['Estimate']*100
ArtRecVolsVolRates_2018['CI Upper'] = ArtRecVolsVolRates_2018['CI Upper']*100

# DonMethAvgDon_2018, DonMethDonRates_2018 = get_data()

data = [SubSecAvgDon_2018, SubSecDonRates_2018, ArtRecDonorsBarriers_2018, ArtRecDonorsDonMeth_2018, ArtRecDonorsDonRates_2018, ArtRecDonorsMotivations_2018, ArtRecVolsActivities_2018, ArtRecVolsBarriers_2018, ArtRecVolsMotivations_2018, ArtRecVolsVolRates_2018, SubSecAvgHrs_2018, SubSecVolRates_2018]

for i in range(len(data)):
    # Suppress Estimate and CI Upper where necessary (for visualizations and error bars)
    data[i]["Estimate"] = np.where(data[i]["Marker"]=="...", 0, data[i]["Estimate"])
    data[i]["CI Upper"] = np.where(data[i]["Marker"]=="...", 0, data[i]["CI Upper"])

    data[i]["Group"] = np.where(data[i]["Attribute"]=="Unable to determine", "", data[i]["Group"])
    data[i]["Group"] = np.where(data[i]["Attribute"]=="Unknown", "", data[i]["Group"])

    data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15, break_long_words=False)
    data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)
    data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Arts and<br>recreation<br>volunteer", "Arts and recreation volunteer", data[i]["Attribute"])
    data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Arts and<br>recreation<br>donors", "Arts and recreation donors", data[i]["Attribute"])
    data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Arts and<br>recreation<br>donor", "Arts and recreation donor", data[i]["Attribute"])
    data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Non-arts and<br>recreation<br>volunteer", "Non-arts and recreation volunteer", data[i]["Attribute"])
    data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Non-arts and<br>recreation<br>donors", "Non-arts and recreation donors", data[i]["Attribute"])
    data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Non-arts and<br>recreation<br>donor", "Non-arts and recreation donor", data[i]["Attribute"])

    data[i]["QuestionText"] = data[i]["QuestionText"].str.wrap(15, break_long_words=False)
    data[i]["QuestionText"] = data[i]["QuestionText"].replace({'\n': '<br>'}, regex=True)

    # Round rates and dollar amounts to zero decimal places
    data[i]['Estimate'] = data[i]['Estimate'].round(0).astype(int)
    data[i]["CI Upper"] = data[i]["CI Upper"].round(0).astype(int)
    data[i]['cv'] = data[i]['cv'].round(2)

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
        html.H1('Giving and Volunteering for Arts, Culture & Recreation Organizations')]),
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
        dcc.Graph(id='ArtRecDonRateAvgDon', style={'marginTop': 50}),
        dcc.Graph(id='ArtRecDonsCauses', style={'marginTop': 50}),
        dcc.Graph(id='ArtRecDonsMeth', style={'marginTop': 50}),
        dcc.Graph(id='ArtRecMotivations', style={'marginTop': 50}),
        dcc.Graph(id='ArtRecBarriers', style={'marginTop': 50}),
        dcc.Graph(id='ArtReVolRateAvgHrs', style={'marginTop': 50}),
        dcc.Graph(id='ArtRecHrsCauses', style={'marginTop': 50}),
        dcc.Graph(id='ArtRecVolActivity', style={'marginTop': 50}),
        dcc.Graph(id='ArtRecVolMotivations', style={'marginTop': 50}),
        dcc.Graph(id='ArtRecVolBarriers', style={'marginTop': 50})
    ],
        style={'width': '50%', 'display': 'inline-block', "marginTop": 20}),
])


def rate_avg_cause(dff1, dff2, name1, name2, title, vol=False):
    dff1['Text'] = np.select([dff1["Marker"] == "*", dff1["Marker"] == "...", pd.isnull(dff1["Marker"])],
                             [dff1.Estimate.map(str)+"%"+"*", "...", dff1.Estimate.map(str)+"%"])
    dff1['HoverText'] = np.select([dff1["Marker"] == "*",
                                   dff1["Marker"] == "...",
                                   pd.isnull(dff1["Marker"])],
                                  ["Estimate: "+dff1.Estimate.map(str)+"% ± "+(dff1["CI Upper"] - dff1["Estimate"]).map(str)+"%<br><b>Use with caution</b>",
                                   "Estimate Suppressed",
                                   "Estimate: "+dff1.Estimate.map(str)+"% ± "+(dff1["CI Upper"] - dff1["Estimate"]).map(str)+"%"])
    if vol:
        dff2['Text'] = np.select([dff2["Marker"] == "*", dff2["Marker"] == "...", pd.isnull(dff2["Marker"])],
                                 [dff2.Estimate.map(str)+"*", "...", dff2.Estimate.map(str)])
        dff2['HoverText'] = np.select([dff2["Marker"] == "*",
                                       dff2["Marker"] == "...",
                                       pd.isnull(dff2["Marker"])],
                                      ["Estimate: "+dff2.Estimate.map(str)+" ± "+(dff2["CI Upper"] - dff2["Estimate"]).map(str)+"<br><b>Use with caution</b>",
                                       "Estimate Suppressed",
                                       "Estimate: "+dff2.Estimate.map(str)+" ± "+(dff2["CI Upper"] - dff2["Estimate"]).map(str)])
    if not vol:
        dff2['Text'] = np.select([dff2["Marker"] == "*", dff2["Marker"] == "...", pd.isnull(dff2["Marker"])],
                                 ["$"+dff2.Estimate.map(str)+"*", "...", "$"+dff2.Estimate.map(str)])
        dff2['HoverText'] = np.select([dff2["Marker"] == "*",
                                       dff2["Marker"] == "...",
                                       pd.isnull(dff2["Marker"])],
                                      ["Estimate: $"+dff2.Estimate.map(str)+" ± $"+(dff2["CI Upper"] - dff2["Estimate"]).map(str)+"<br><b>Use with caution</b>",
                                       "Estimate Suppressed",
                                       "Estimate: $"+dff2.Estimate.map(str)+" ± $"+(dff2["CI Upper"] - dff2["Estimate"]).map(str)])

    # Scatter plot - data frame, x label, y label
    fig = go.Figure()

    fig.add_trace(go.Bar(x=dff1['CI Upper'],
                         y=dff1['QuestionText'],
                         orientation="h",
                         error_x=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         text=None,
                         hoverinfo="skip",
                         textposition='outside',
                         showlegend=False,
                         cliponaxis=False,
                         xaxis='x2',
                         offsetgroup=2
                         ),
                  )
    fig.add_trace(go.Bar(x=dff2['CI Upper'],
                         y=dff2['QuestionText'],
                         orientation="h",
                         error_x=None, # need to vectorize subtraction
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         text=None,
                         hoverinfo="skip",
                         textposition='outside',
                         showlegend=False,
                         cliponaxis=False,
                         xaxis='x1',
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
                         marker=dict(color="#FD7B5F"),
                         text=dff1['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         insidetextanchor=None,
                         name=name1,
                         xaxis='x2',
                         offsetgroup=2
                         ),
                  )
    fig.add_trace(go.Bar(x=dff2['Estimate'],
                         y=dff2['QuestionText'],
                         orientation="h",
                         error_x=None, # need to vectorize subtraction
                         hovertext =dff2['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         marker=dict(color="#234C66"),
                         text=dff2['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         insidetextanchor= None,
                         name=name2,
                         xaxis='x1',
                         offsetgroup=1
                         ),
                  )

    x2 = go.layout.XAxis(overlaying='x',
                         side='bottom',
                         autorange = False,
                         range = [0, 1.25*max(dff1["CI Upper"])])
    x1 = go.layout.XAxis(overlaying='x',
                         side='top',
                         autorange = False,
                         range = [0, 1.25*max(dff2["CI Upper"])])

    fig.update_layout(title={'text': title,
                             'y': 0.99},
                      margin={'l': 30, 'b': 30, 'r': 10, 't': 30},
                      height=600,
                      bargroupgap=0.05,
                      plot_bgcolor='rgba(0, 0, 0, 0)',
                      barmode="group",
                      xaxis1=x1,
                      xaxis2=x2,
                      legend={'orientation': 'h', 'yanchor': "bottom"},
                      updatemenus=[
                          dict(
                              type = "buttons",
                              xanchor='right',
                              x = 1.2,
                              y = 0.5,
                              buttons=list([
                                  dict(
                                      args=[{"error_x": [None, None, None, None],
                                             "text": [None, None, dff1['Text'], dff2['Text']]}],
                                      label="Réinitialiser",
                                      method="restyle"
                                  ),
                                  dict(
                                      args=[{"error_x": [None, None, dict(type="data", array=dff1["CI Upper"]-dff1["Estimate"], color="#424242", thickness=1.5), dict(type="data", array=dff2["CI Upper"]-dff2["Estimate"], color="#424242", thickness=1.5)],
                                             "text": [dff1['Text'], dff2['Text'], None, None]}],
                                      label="Intervalles de confiance",
                                      method="restyle"
                                  )
                              ]),
                          ),
                      ]
                      )
    fig.update_xaxes(showgrid=False,
                     showticklabels=False,
                     autorange=False,
                     )
    fig.update_yaxes(autorange="reversed",
                     ticklabelposition="outside top",
                     tickfont=dict(size=12),
                     categoryorder='array',
                     categoryarray=dff1.sort_values(by="Estimate", ascending=False)["QuestionText"])

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


def vertical_percentage_graph(dff, title, name1, name2, sort=False, array=None):
    dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
                            [dff.Estimate.map(str) + "%" + "*", "...", dff.Estimate.map(str) + "%"])
    dff['HoverText'] = np.select([dff["Marker"] == "*",
                                  dff["Marker"] == "...",
                                  pd.isnull(dff["Marker"])],
                                 ["Estimate: " + dff.Estimate.map(str) + "% ± " + (dff["CI Upper"] - dff["Estimate"]).map(str) + "%<br><b>Use with caution</b>",
                                  "Estimate Suppressed",
                                  "Estimate: " + dff.Estimate.map(str) + "% ± " + (dff["CI Upper"] - dff["Estimate"]).map(str) + "%"])

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
                         marker=dict(color="#FD7B5F"),
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
                         marker=dict(color="#234C66"),
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
                                      label="Réinitialiser",
                                      method="restyle"
                                  ),
                                  dict(
                                      args=[{"error_x": [None, None, dict(type="data", array=dff1["CI Upper"] - dff1["Estimate"], color="#424242", thickness=1.5), dict(type="data", array=dff2["CI Upper"] - dff2["Estimate"], color="#424242", thickness=1.5)],
                                             "text": [dff1['Text'], dff2['Text'], None, None]}],
                                      label="Intervalles de confiance",
                                      method="restyle"
                                  )
                              ]),
                          ),
                      ]
                      )

    fig.update_xaxes(showgrid=False,
                     showticklabels=False,
                     autorange=False,
                     range=[0, 1.25 * max(np.concatenate([dff1["CI Upper"], dff2["CI Upper"]]))])
    if sort:
        fig.update_yaxes(autorange="reversed",
                         ticklabelposition="outside top",
                         tickfont=dict(size=11),
                         categoryorder='array',
                         categoryarray=array)
    else:
        fig.update_yaxes(autorange="reversed",
                         ticklabelposition="outside top",
                         tickfont=dict(size=11),
                         categoryorder='array',
                         categoryarray=dff1.sort_values(by="Estimate", ascending=False)["QuestionText"])

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


@app.callback(
    dash.dependencies.Output('ArtRecDonRateAvgDon', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = SubSecDonRates_2018[SubSecDonRates_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "All"]
    name1 = "Donation rate"

    dff2 = SubSecAvgDon_2018[SubSecAvgDon_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "All"]
    name2 = "Average donation"

    title = '{}, {}'.format("Donation rate and average donation amount by cause", region)

    return rate_avg_cause(dff1, dff2, name1, name2, title)


@app.callback(
    dash.dependencies.Output('ArtRecDonsCauses', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = ArtRecDonorsDonRates_2018[ArtRecDonorsDonRates_2018['Region'] == region]
    name1 = "Arts and recreation donor"
    name2 = "Non-arts and recreation donor"

    array = ["Sports &<br>Recreation", "Arts & culture", "Health", "Social services", "Religion", "Hospitals",
             "Education &<br>research", "Grant-making,<br>fundraising",
             "Environment", "International", "Law, advocacy &<br>politics",
             "Development &<br>housing", "Other", "Universities &<br>colleges", "Business &<br>professional"]
    title = '{}, {}'.format("Rates of donating to other causes", region)
    return vertical_percentage_graph(dff, title, name1, name2, sort=True, array=array)


@app.callback(
    dash.dependencies.Output('ArtRecDonsMeth', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = ArtRecDonorsDonMeth_2018[ArtRecDonorsDonMeth_2018['Region'] == region]
    name1 = "Arts and recreation donors"
    name2 = "Non-arts and recreation donors"

    title = '{}, {}'.format("Donation rate by method", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('ArtRecMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = ArtRecDonorsMotivations_2018[ArtRecDonorsMotivations_2018['Region'] == region]
    name1 = "Arts and recreation donors"
    name2 = "Non-arts and recreation donors"

    title = '{}, {}'.format("Motivations for donating", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('ArtRecBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = ArtRecDonorsBarriers_2018[ArtRecDonorsBarriers_2018['Region'] == region]
    name1 = "Arts and recreation donors"
    name2 = "Non-arts and recreation donors"

    title = '{}, {}'.format("Barriers to donating more", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('ArtReVolRateAvgHrs', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = SubSecVolRates_2018[SubSecVolRates_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "All"]
    name1 = "Volunteer rate"

    dff2 = SubSecAvgHrs_2018[SubSecAvgHrs_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "All"]
    name2 = "Average hours"

    title = '{}, {}'.format("Volunteer rate and average hours volunteered by cause", region)

    return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)


@app.callback(
    dash.dependencies.Output('ArtRecHrsCauses', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = ArtRecVolsVolRates_2018[ArtRecVolsVolRates_2018['Region'] == region]
    name1 = "Arts and recreation volunteer"
    name2 = "Non-arts and recreation volunteer"

    title = '{}, {}'.format("Rates of volunteering for other causes", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('ArtRecVolActivity', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = ArtRecVolsActivities_2018[ArtRecVolsActivities_2018['Region'] == region]
    name1 = "Arts and recreation volunteer"
    name2 = "Non-arts and recreation volunteer"

    title = '{}, {}'.format("Volunteer rate by activity", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('ArtRecVolMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = ArtRecVolsMotivations_2018[ArtRecVolsMotivations_2018['Region'] == region]
    name1 = "Arts and recreation volunteer"
    name2 = "Non-arts and recreation volunteer"

    title = '{}, {}'.format("Motivations for volunteering", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('ArtRecVolBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = ArtRecVolsBarriers_2018[ArtRecVolsBarriers_2018['Region'] == region]
    name1 = "Arts and recreation volunteer"
    name2 = "Non-arts and recreation volunteer"

    title = '{}, {}'.format("Barriers to volunteering more", region)
    return vertical_percentage_graph(dff, title, name1, name2)


if __name__ == '__main__':
    app.run_server(debug=True)



