import pandas as pd
import plotly.graph_objects as go
import numpy as np

def dist_total_donations(dff1, dff2, name1, name2, title):
    dff1['Text'] = np.select([dff1["Marker"] == "*", dff1["Marker"] == "...", pd.isnull(dff1["Marker"])],
                                [dff1.Estimate.map(str)+"%"+"*", "...", dff1.Estimate.map(str)+"%"])
    dff1['HoverText'] = np.select([dff1["Marker"] == "*",
                                      dff1["Marker"] == "...",
                                      pd.isnull(dff1["Marker"])],
                                     ["Estimate: "+dff1.Estimate.map(str)+"% ± "+(dff1["CI Upper"] - dff1["Estimate"]).map(str)+"%<br><b>A utiliser avec précaution</b>",
                                      "Estimate Suppressed",
                                      "Estimate: "+dff1.Estimate.map(str)+"% ± "+(dff1["CI Upper"] - dff1["Estimate"]).map(str)+"%"])

    dff2['Text'] = np.select([dff2["Marker"] == "*", dff2["Marker"] == "...", pd.isnull(dff2["Marker"])],
                             [dff2.Estimate.map(str)+"%"+"*", "...", dff2.Estimate.map(str)+"%"])
    dff2['HoverText'] = np.select([dff2["Marker"] == "*",
                                   dff2["Marker"] == "...",
                               pd.isnull(dff2["Marker"])],
                              ["Estimate: "+dff2.Estimate.map(str)+"% ± "+(dff2["CI Upper"] - dff2["Estimate"]).map(str)+"%<br><b>A utiliser avec précaution</b>",
                               "Estimate Suppressed",
                               "Estimate: "+dff2.Estimate.map(str)+"% ± "+(dff2["CI Upper"] - dff2["Estimate"]).map(str)+"%"])
    fig = go.Figure()

    fig.add_trace(go.Bar(x=dff2['Attribute'],
                          y=dff2['CI Upper'],
                          marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                          text=None,
                          textposition='outside',
                          showlegend=False,
                          hoverinfo="skip",
                          cliponaxis=False,
                          offsetgroup=1,
                          ),
                   )

    fig.add_trace(go.Bar(x=dff1['Attribute'],
                          y=dff1['CI Upper'],
                          marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                          text=None,
                          textposition='outside',
                          hoverinfo="skip",
                          showlegend=False,
                          name=name1,
                          offsetgroup=2,
                          ),
                   )

    fig.add_trace(go.Bar(x=dff2['Attribute'],
                          y=dff2['Estimate'],
                          error_y=None,
                          hovertext =dff2['HoverText'],
                          hovertemplate="%{hovertext}",
                          hoverlabel=dict(font=dict(color="white")),
                          hoverinfo="text",
                          marker=dict(color="#c8102e"),
                         text=dff2['Text'],
                          textposition='outside',
                          cliponaxis=False,
                          name=name2,
                          offsetgroup=1
                          ),
                   )

    fig.add_trace(go.Bar(x=dff1['Attribute'],
                          y=dff1['Estimate'],
                          error_y=None,
                          hovertext=dff1['HoverText'],
                          hovertemplate="%{hovertext}",
                          hoverlabel=dict(font=dict(color="white")),
                          hoverinfo="text",
                          marker=dict(color="#7BAFD4"),
                          text=dff1['Text'],
                          textposition='outside',
                          cliponaxis=False,
                          name=name1,
                          offsetgroup=2
                          ),
                   )

    fig.update_layout(title={'text': title,
                              'y': 0.95},
                       margin={'l': 30, 'b': 30, 'r': 10, 't': 10},
                       plot_bgcolor='rgba(0, 0, 0, 0)',
                       barmode="group",
                       bargroupgap=0.05,
                       legend={'orientation': 'h', 'yanchor': "bottom", 'xanchor': 'center', 'x': 0.5, 'y': -0.2},
                       height=400,
                       updatemenus=[
                           dict(
                               type = "buttons",
                               xanchor='right',
                               x = 1.4,
                               y = 0.5,
                               buttons=list([
                                   dict(
                                       args=[{"error_y": [None, None, None, None],
                                              "text": [None, None, dff2['Text'], dff1['Text']],
                                              }],
                                       label="Réinitialiser",
                                       method="restyle"
                                   ),
                                   dict(
                                       args=[{"error_y": [None, None, dict(type="data", array=dff2["CI Upper"]-dff2["Estimate"], color="#424242", thickness=1.5), dict(type="data", array=dff1["CI Upper"]-dff1["Estimate"], color="#424242", thickness=1.5)],
                                              "text": [dff2['Text'], dff1['Text'], None, None],
                                              }],
                                       label="Intervalles de confiance",
                                       method="restyle"
                                   )
                               ]),
                           ),
                       ])

    fig.update_xaxes(tickfont=dict(size=12))
    fig.update_yaxes(showgrid=False,
                      showticklabels=False)

    markers = pd.concat([dff1["Marker"], dff2["Marker"]])
    if markers.isin(["*"]).any() and markers.isin(["..."]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                           annotations=[dict(text="<a href='/popup'>De quoi s'agit-il?</a>", xref="paper", yref="paper", xanchor='right', y=0.19, x=1.4, align="left", showarrow=False),
                                        dict(text="*<i>A utiliser avec précaution<br>Certains résultats sont pas assez fiables pour être affichés</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.11, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    elif markers.isin(["*"]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                           annotations=[dict(text="<a href='/popup'>De quoi s'agit-il?</a>", xref="paper", yref="paper", xanchor='right', y=0.19, x=1.4, align="left", showarrow=False),
                                        dict(text="*<i>A utiliser avec précaution</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.11, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    elif markers.isin(["..."]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                           annotations=[dict(text="<a href='/popup'>De quoi s'agit-il?</a>", xref="paper", yref="paper", xanchor='right', y=0.19, x=1.4, align="left", showarrow=False),
                                        dict(text="<i>Certains résultats sont pas assez fiables pour être affichés</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.11, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    else:
        fig.update_layout(margin={'l': 30, 'b': 30, 'r': 10, 't': 40},
                           annotations=[dict(text="<a href='/popup'>De quoi s'agit-il?</a>", xref="paper", yref="paper", xanchor='right', y=0.2, x=1.4, align="left", showarrow=False)])

    return fig

def triple_vertical_percentage_graph(dff, title):
    dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
                            [dff.Estimate.map(str)+"%"+"*", "...", dff.Estimate.map(str)+"%"])
    dff['HoverText'] = np.select([dff["Marker"] == "*",
                                  dff["Marker"] == "...",
                                  pd.isnull(dff["Marker"])],
                                 ["Estimate: "+dff.Estimate.map(str)+"% ± "+(dff["CI Upper"] - dff["Estimate"]).map(str)+"%<br><b>A utiliser avec précaution</b>",
                                  "Estimate Suppressed",
                                  "Estimate: "+dff.Estimate.map(str)+"% ± "+(dff["CI Upper"] - dff["Estimate"]).map(str)+"%"])

    # dff1 = dff[dff['QuestionText'] == "Grand.e.s donateur.trice.s"]
    # name1 = "Grand.e.s donateur.trice.s"

    # dff2 = dff[dff['QuestionText'] == "Grand.e.s donateur.trice.s religieux"]
    # name2 = "Grand.e.s donateur.trice.s religieux"

    # dff3 = dff[dff['QuestionText'] == "Grand.e.s donateur.trice.s laïcs"]
    # name3 = "Grand.e.s donateur.trice.s laïcs"
    
    dff1 = dff[dff['QuestionText'] == "Top donors"]
    # name1 = "Top donors"
    name1 = "Grand.e.s donateur.trice.s"

    dff2 = dff[dff['QuestionText'] == "Top religious donors"]
    # name2 = "Top religious donors"
    name2 = "Grand.e.s donateur.trice.s religieux"

    dff3 = dff[dff['QuestionText'] == "Top secular donors"]
    # name3 = "Top secular donors"
    name3 = "Grand.e.s donateur.trice.s laïcs"

    fig = go.Figure()

    fig.add_trace(go.Bar(x=dff1['CI Upper'],
                         y=dff1['Attribute'],
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
                         y=dff2['Attribute'],
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
                         y=dff3['Attribute'],
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
                         y=dff1['Attribute'],
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
                         y=dff2['Attribute'],
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
                         y=dff3['Attribute'],
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
                             'y': 0.977},
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
                                      label="Réinitialiser",
                                      method="restyle"
                                  ),
                                  dict(
                                      args=[{"error_x": [None, None, None, dict(type="data", array=dff1["CI Upper"]-dff1["Estimate"], color="#424242", thickness=1.5),
                                                         dict(type="data", array=dff2["CI Upper"]-dff2["Estimate"], color="#424242", thickness=1.5),
                                                         dict(type="data", array=dff3["CI Upper"]-dff3["Estimate"], color="#424242", thickness=1.5)],
                                             "text": [dff1['Text'], dff2['Text'], dff3['Text'], None, None, None]}],
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
                     range=[0, 1.25*max(np.concatenate([dff1["CI Upper"], dff2["CI Upper"], dff3["CI Upper"]]))])
    fig.update_yaxes(autorange="reversed",
                     ticklabelposition="outside top",
                     tickfont=dict(size=12))

    markers = pd.concat([dff1["Marker"], dff2["Marker"], dff3["Marker"]])
    if markers.isin(["*"]).any() and markers.isin(["..."]).any():
        fig.update_layout(margin={'l': 40, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href='/popup'>De quoi s'agit-il?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="*<i>A utiliser avec précaution<br>Certains résultats sont pas assez fiables pour être affichés</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    elif markers.isin(["*"]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href='/popup'>De quoi s'agit-il?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="*<i>A utiliser avec précaution</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    elif markers.isin(["..."]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href='/popup'>De quoi s'agit-il?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="<i>Certains résultats sont pas assez fiables pour être affichés</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    else:
        fig.update_layout(margin={'l': 30, 'b': 30, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href='/popup'>De quoi s'agit-il?</a>", xref="paper", yref="paper", xanchor='right', y=0.32, x=1.2, align="left", showarrow=False)])


    return fig

def vertical_percentage_graph(dff, title):
    dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
                             [dff.Estimate.map(str)+"%"+"*", "...", dff.Estimate.map(str)+"%"])
    dff['HoverText'] = np.select([dff["Marker"] == "*",
                                   dff["Marker"] == "...",
                                   pd.isnull(dff["Marker"])],
                                  ["Estimate: "+dff.Estimate.map(str)+"% ± "+(dff["CI Upper"] - dff["Estimate"]).map(str)+"%<br><b>A utiliser avec précaution</b>",
                                   "Estimate Suppressed",
                                   "Estimate: "+dff.Estimate.map(str)+"% ± "+(dff["CI Upper"] - dff["Estimate"]).map(str)+"%"])

    # dff1 = dff[dff['Attribute'] == "Grand.e.s donateur.trice.s"]
    # name1 = "Grand.e.s donateur.trice.s"

    # dff2 = dff[dff['Attribute'] == "Donateur.trice.s ordinaires"]
    # name2 = "Donateur.trice.s ordinaires"
    
    dff1 = dff[dff['Attribute'] == "Top donor"]
    # name1 = "Top donors"
    name1 = "Grand.e.s donateur.trice.s"

    dff2 = dff[dff['Attribute'] == "Regular donor"]
    # name2 = "Regular donors"
    name2 = "Donateur.trice.s ordinaires"

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

    fig.update_layout(title={'text': title,
                             'y': 0.977},
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
                     autorange = False,
                     range = [0, 1.25*max(np.concatenate([dff1["CI Upper"], dff2["CI Upper"]]))])
    fig.update_yaxes(autorange="reversed",
                     ticklabelposition="outside top",
                     tickfont=dict(size=12),
                     categoryorder='array',
                     categoryarray=dff1.sort_values(by="Estimate", ascending=False)["QuestionText"])

    markers = pd.concat([dff1["Marker"], dff2["Marker"]])
    if markers.isin(["*"]).any() and markers.isin(["..."]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href='/popup'>De quoi s'agit-il?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="*<i>A utiliser avec précaution<br>Certains résultats sont pas assez fiables pour être affichés</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    elif markers.isin(["*"]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href='/popup'>De quoi s'agit-il?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="*<i>A utiliser avec précaution</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    elif markers.isin(["..."]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href='/popup'>De quoi s'agit-il?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="<i>Certains résultats sont pas assez fiables pour être affichés</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    else:
        fig.update_layout(margin={'l': 30, 'b': 30, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href='/popup'>De quoi s'agit-il?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False)])


    return fig

