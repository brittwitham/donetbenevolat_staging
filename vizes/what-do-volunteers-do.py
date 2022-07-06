import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

ActivityVolRate_2018 = pd.read_csv("../tables/2018-ActivityVolRate.csv")
AvgHoursVol_2018 = pd.read_csv("../tables/2018-AvgHoursVol.csv")

ActivityVolRate_2018['Estimate'] = ActivityVolRate_2018['Estimate']*100
ActivityVolRate_2018['CI Upper'] = ActivityVolRate_2018['CI Upper']*100

data = [ActivityVolRate_2018, AvgHoursVol_2018]

for i in range(len(data)):
    data[i]["Estimate"] = np.where(data[i]["Marker"] == "...", 0, data[i]["Estimate"])
    data[i]["CI Upper"] = np.where(data[i]["Marker"] == "...", 0, data[i]["CI Upper"])

    data[i]["Group"] = np.where(data[i]["Attribute"] == "Unable to determine", "", data[i]["Group"])
    data[i]["Group"] = np.where(data[i]["Attribute"] == "Unknown", "", data[i]["Group"])

    data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15)
    data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)
    data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Regular<br>volunteer", "Regular volunteer", data[i]["Attribute"])

    data[i]["QuestionText"] = data[i]["QuestionText"].str.wrap(20)
    data[i]["QuestionText"] = data[i]["QuestionText"].replace({'\n': '<br>'}, regex=True)

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
activity_names = ActivityVolRate_2018.QuestionText.unique()

app.layout = html.Div([
    html.Div([
        html.H1('What do volunteers do?')]),
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
        dcc.Graph(id='ActivitiesVolRateAvgHrs', style={'marginTop': 50}),
        html.Div([
            "Choose activity of focus: ",
            dcc.Dropdown(id='activity-selection',
                         options=[{'label': i, 'value': i} for i in activity_names],
                         value="Canvassing")
        ], style={'marginTop': 50, 'width': '100%', 'verticalAlign': 'middle'}),
        dcc.Graph(id='ActivityVolRate-Gndr', style={'marginTop': 50}),
        dcc.Graph(id='ActivityVolRate-Age', style={'marginTop': 50}),
        dcc.Graph(id='ActivityVolRate-Educ', style={'marginTop': 50}),
        dcc.Graph(id='ActivityVolRate-MarStat', style={'marginTop': 50}),
        dcc.Graph(id='ActivityVolRate-Inc', style={'marginTop': 50}),
        dcc.Graph(id='ActivityVolRate-Relig', style={'marginTop': 50}),
        dcc.Graph(id='ActivityVolRate-Labour', style={'marginTop': 50}),
        dcc.Graph(id='ActivityVolRate-ImmStat', style={'marginTop': 50})
    ],
        style={'width': '50%', 'display': 'inline-block', "marginTop": 20}),
])

def vol_rate_avg_hrs_qt(dff1, dff2, name1, name2, title):

    dff1['Text'] = np.select([dff1["Marker"] == "*", dff1["Marker"] == "...", pd.isnull(dff1["Marker"])],
                             [dff1.Estimate.map(str)+"%"+"*", "...", dff1.Estimate.map(str)+"%"])
    dff1['HoverText'] = np.select([dff1["Marker"] == "*",
                                   dff1["Marker"] == "...",
                                   pd.isnull(dff1["Marker"])],
                                  ["Estimate: "+dff1.Estimate.map(str)+"% ± "+(dff1["CI Upper"] - dff1["Estimate"]).map(str)+"%<br><b>Use with caution</b>",
                                   "Estimate Suppressed",
                                   "Estimate: "+dff1.Estimate.map(str)+"% ± "+(dff1["CI Upper"] - dff1["Estimate"]).map(str)+"%"])
    dff2['Text'] = np.select([dff2["Marker"] == "*", dff2["Marker"] == "...", pd.isnull(dff2["Marker"])],
                             [dff2.Estimate.map(str)+"*", "...", dff2.Estimate.map(str)])
    dff2['HoverText'] = np.select([dff2["Marker"] == "*",
                                   dff2["Marker"] == "...",
                                   pd.isnull(dff2["Marker"])],
                                  ["Estimate: "+dff2.Estimate.map(str)+" ± "+(dff2["CI Upper"] - dff2["Estimate"]).map(str)+"<br><b>Use with caution</b>",
                                   "Estimate Suppressed",
                                   "Estimate: "+dff2.Estimate.map(str)+" ± "+(dff2["CI Upper"] - dff2["Estimate"]).map(str)])
    dff1 = dff1[(dff1.Attribute != "Unknown") & (dff1.Attribute != "Unable to determine")]
    dff2 = dff2[(dff2.Attribute != "Unknown") & (dff2.Attribute != "Unable to determine")]

    # Scatter plot - data frame, x label, y label
    fig = go.Figure()

    fig.add_trace(go.Bar(x=dff1['CI Upper'],
                         y=dff1["QuestionText"],
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
                         y=dff2["QuestionText"],
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
                         y=dff1["QuestionText"],
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
                         insidetextanchor=None,
                         name=name1,
                         xaxis='x2',
                         offsetgroup=2
                         ),
                  )
    fig.add_trace(go.Bar(x=dff2['Estimate'],
                         y=dff2["QuestionText"],
                         orientation="h",
                         error_x=None, # need to vectorize subtraction
                         hovertext =dff2['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         marker=dict(color="#7BAFD4"),
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
                             'y': 0.98},
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
                                      label="Reset",
                                      method="restyle"
                                  ),
                                  dict(
                                      args=[{"error_x": [None, None, dict(type="data", array=dff1["CI Upper"]-dff1["Estimate"], color="#424242", thickness=1.5), dict(type="data", array=dff2["CI Upper"]-dff2["Estimate"], color="#424242", thickness=1.5)],
                                             "text": [dff1['Text'], dff2['Text'], None, None]}],
                                      label="Confidence Intervals",
                                      method="restyle"
                                  )
                              ]),
                          ),
                      ]
                      )
    fig.update_xaxes(showgrid=False,
                     showticklabels=False,
                     autorange = False,
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


def single_vertical_percentage_graph(dff, title, by="Attribute", sort=False):

    dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
                            [dff.Estimate.map(str) + "%" + "*", "...", dff.Estimate.map(str) + "%"])
    dff['HoverText'] = np.select([dff["Marker"] == "*",
                                  dff["Marker"] == "...",
                                  pd.isnull(dff["Marker"])],
                                 ["Estimate: " + dff.Estimate.map(str) + "% ± " + (dff["CI Upper"] - dff["Estimate"]).map(str) + "%<br><b>Use with caution</b>",
                                  "Estimate Suppressed",
                                  "Estimate: " + dff.Estimate.map(str) + "% ± " + (dff["CI Upper"] - dff["Estimate"]).map(str) + "%"])

    fig = go.Figure()

    fig.add_trace(go.Bar(x=dff['CI Upper'],
                         y=dff[by],
                         orientation="h",
                         error_x=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         name="",
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=1
                         ),
                  )

    fig.add_trace(go.Bar(x=dff['Estimate'],
                         y=dff[by],
                         orientation="h",
                         error_x=None,
                         hovertext=dff['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#c8102e"),
                         text=dff['Text'],
                         name="",
                         textposition='outside',
                         cliponaxis=False,
                         offsetgroup=1
                         ),
                  )

    fig.update_layout(title={'text': title,
                             'y': 0.99},
                      margin={'l': 30, 'b': 30, 'r': 10, 't': 10},
                      height=600,
                      plot_bgcolor='rgba(0, 0, 0, 0)',
                      showlegend=False,
                      updatemenus=[
                          dict(
                              type="buttons",
                              xanchor='right',
                              x=1.2,
                              y=0.5,
                              buttons=list([
                                  dict(
                                      args=[{"error_x": [None, None],
                                             "text": [None, dff['Text']]}],
                                      label="Reset",
                                      method="restyle"
                                  ),
                                  dict(
                                      args=[{"error_x": [None, dict(type="data", array=dff["CI Upper"] - dff["Estimate"], color="#424242", thickness=1.5)],
                                             "text": [dff['Text'], None]}],
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
                     range=[0, 1.25 * max(dff["CI Upper"])])
    fig.update_yaxes(autorange="reversed",
                     ticklabelposition="outside top",
                     tickfont=dict(size=11))

    if sort:
        fig.update_yaxes(categoryorder='array',
                         categoryarray=dff.sort_values(by="Estimate", ascending=False)["QuestionText"])

    markers = dff["Marker"]
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
    dash.dependencies.Output('ActivitiesVolRateAvgHrs', 'figure'),
    [

        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):

    dff1 = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "All"]
    name1 = "% volunteering"

    dff2 = AvgHoursVol_2018[AvgHoursVol_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "All"]
    name2 = "Average hours"

    title = '{}, {}'.format("Volunteer rate & average hours contributed by activity", region)

    return vol_rate_avg_hrs_qt(dff1, dff2, name1, name2, title)

@app.callback(
    dash.dependencies.Output('ActivityVolRate-Gndr', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('activity-selection', 'value')
    ])
def update_graph(region, activity):
    dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
    dff = dff[dff['QuestionText'] == activity]
    dff = dff[dff['Group'] == "Gender"]

    title = '{}, {}'.format("Volunteer rate by activity by gender", region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('ActivityVolRate-Age', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('activity-selection', 'value')
    ])
def update_graph(region, activity):
    dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
    dff = dff[dff['QuestionText'] == activity]
    dff = dff[dff['Group'] == "Age group"]

    title = '{}, {}'.format("Volunteer rate by activity by age", region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('ActivityVolRate-Educ', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('activity-selection', 'value')
    ])
def update_graph(region, activity):
    dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
    dff = dff[dff['QuestionText'] == activity]
    dff = dff[dff['Group'] == "Education"]

    title = '{}, {}'.format("Volunteer rate by activity by formal education", region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('ActivityVolRate-MarStat', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('activity-selection', 'value')
    ])
def update_graph(region, activity):
    dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
    dff = dff[dff['QuestionText'] == activity]
    dff = dff[dff['Group'] == "Marital status"]

    title = '{}, {}'.format("Volunteer rate by activity by marital status", region)
    return single_vertical_percentage_graph(dff, title)

@app.callback(
    dash.dependencies.Output('ActivityVolRate-Inc', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('activity-selection', 'value')
    ])
def update_graph(region, activity):
    dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
    dff = dff[dff['QuestionText'] == activity]
    dff = dff[dff['Group'] == "Family income category"]

    title = '{}, {}'.format("Volunteer rate by activity by household income", region)
    return single_vertical_percentage_graph(dff, title)


@app.callback(
    dash.dependencies.Output('ActivityVolRate-Relig', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('activity-selection', 'value')
    ])
def update_graph(region, activity):
    dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
    dff = dff[dff['QuestionText'] == activity]
    dff = dff[dff['Group'] == "Frequency of religious attendance"]

    title = '{}, {}'.format("Volunteer rate by activity by religious attendance", region)
    return single_vertical_percentage_graph(dff, title)


@app.callback(
    dash.dependencies.Output('ActivityVolRate-Labour', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('activity-selection', 'value')
    ])
def update_graph(region, activity):
    dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
    dff = dff[dff['QuestionText'] == activity]
    dff = dff[dff['Group'] == "Labour force status"]

    title = '{}, {}'.format("Volunteer rate by activity by labour force status", region)
    return single_vertical_percentage_graph(dff, title)


@app.callback(
    dash.dependencies.Output('ActivityVolRate-ImmStat', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value'),
        dash.dependencies.Input('activity-selection', 'value')
    ])
def update_graph(region, activity):
    dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
    dff = dff[dff['QuestionText'] == activity]
    dff = dff[dff['Group'] == "Immigration status"]

    title = '{}, {}'.format("Volunteer rate by activity by immigration status", region)
    return single_vertical_percentage_graph(dff, title)

if __name__ == '__main__':
    app.run_server(debug=True)
