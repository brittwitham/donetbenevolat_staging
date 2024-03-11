import pandas as pd
import plotly.graph_objects as go
import numpy as np
import textwrap

# Example code
def OrgQuad1(df, title):

    title = "<br>".join(textwrap.wrap(title, width=70))

    df = df.sort_values('Business')
    df = df.loc[df['item2'].map({"Other obstacle": -1, "None": -2}).sort_values().index]

    fig_OrgQuad1 = go.Figure()

    fig_OrgQuad1.add_trace(go.Bar(x = round(df['Business'] * 100),
                                  y=df['item2'],
                                  marker = dict(color = "#50a684"),
                                  name = "Entreprises",
                                  text = df['Business']*100,
                                  texttemplate = "%{text:.0f} %",
                                  textposition = "none",
                                  meta = df['BusinessStat'],
                                  hovertemplate = "%{y} : " + "%{text:.1f} %" + "<br>Qualité de données : " + "%{meta}",
                                  orientation='h'))

    fig_OrgQuad1.add_trace(go.Bar(x = round(df['GovAgency'] * 100,0),
                                  y=df['item2'],
                                  marker = dict(color = "#ffc72c"),
                                  name = "Institutions gouvernementales",
                                  text = df['GovAgency']*100,
                                  texttemplate="%{text:.0f} %",
                                  textposition="none",
                                  meta = df['GovAgencyStat'],
                                  hovertemplate="%{y} : " + "%{text:.1f} %" + "<br>Qualité de données : " + "%{meta}",
                                  orientation='h'))

    fig_OrgQuad1.add_trace(go.Bar(x = round(df['BusNPO'] * 100,0),
                                  y=df['item2'],
                                  marker = dict(color = "#7bafd4"),
                                  name = "Institutions commerciales à but non lucratif",
                                  text = df['BusNPO']*100,
                                  texttemplate="%{text:.0f} %",
                                  textposition="none",
                                  meta = df['BusNPOStat'],
                                  hovertemplate="%{y} : " + "%{text:.1f} %" + "<br>Qualité de données : " + "%{meta}",
                                  orientation='h'))

    fig_OrgQuad1.add_trace(go.Bar(x = round(df['CommNPO'] * 100,0),
                                  y=df['item2'],
                                  marker = dict(color = "#c8102e"),
                                  name = "Organismes communautaires à but non lucratif",
                                  text = df['CommNPO']*100,
                                  texttemplate="%{text:.0f} %",
                                  textposition="none",
                                  meta = df['CommNPOStat'],
                                  hovertemplate="%{y} : " + "%{text:.1f} %" + "<br>Qualité de données : " + "%{meta}",
                                  orientation='h'))

    fig_OrgQuad1.update_layout(title = title,
                               yaxis = dict(title = "",
                                            showticklabels = True,
                                            showgrid = False),
                               xaxis = dict(title = "",
                                            showticklabels = False,
                                            showgrid = False),
                               margin = dict(pad = 15),
                               legend = dict(orientation = 'h',
                                             xanchor = 'center',
                                             x=0.5,
                                             y=0,
                                             traceorder = 'reversed'),
                               paper_bgcolor='rgba(0,0,0,0)',
                               plot_bgcolor='rgba(0,0,0,0)'
                               )

    fig_OrgQuad1.update_yaxes(showline=True, linewidth=1, linecolor='black', position=0)

    return fig_OrgQuad1


def OrgQuad2(df, title):

    title = "<br>".join(textwrap.wrap(title, width=70))

    df = df.sort_values("seriesDate")

    fig_OrgQuad2 = go.Figure()

    fig_OrgQuad2.add_trace(go.Bar(y = df['dateLabel'],
                                  x = round(df['Business'] * 100,0),
                                  marker = dict(color = "#50a684"),
                                  name = "Entreprises",
                                  text = df['Business']*100,
                                  texttemplate = "%{text:.0f} %",
                                  textposition = 'outside',
                                  meta = df['BusinessStat'],
                                  hovertemplate = "%{y} : %{text:.1f} %<br>Qualité de données : %{meta}",
                                  orientation="h",
                                  ))

    fig_OrgQuad2.add_trace(go.Bar(y = df['dateLabel'],
                                  x = round(df['GovAgency'] * 100,0),
                                  marker = dict(color = "#ffc72c"),
                                  name = "Institutions gouvernementales",
                                  text = df['GovAgency']*100,
                                  texttemplate="%{text:.0f} %",
                                  textposition='outside',
                                  meta = df['GovAgencyStat'],
                                  hovertemplate="%{y} : %{text:.1f} %<br>Qualité de données : %{meta}",
                                  orientation="h",
                                  ))

    fig_OrgQuad2.add_trace(go.Bar(y = df['dateLabel'],
                                  x = round(df['BusNPO'] * 100,0),
                                  marker = dict(color = "#7bafd4"),
                                  name = "Institutions commerciales à but non lucratif",
                                  text = df['BusNPO']*100,
                                  texttemplate="%{text:.0f} %",
                                  textposition='outside',
                                  meta=df['BusNPOStat'],
                                  hovertemplate="%{y} : %{text:.1f} %<br>Qualité de données : %{meta}",
                                  orientation="h",
                                  ))

    fig_OrgQuad2.add_trace(go.Bar(y = df['dateLabel'],
                                  x = round(df['CommNPO'] * 100,0),
                                  marker = dict(color = "#c8102e"),
                                  name = "Organismes communautaires à but non lucratif",
                                  text = df['CommNPO']*100,
                                  texttemplate="%{text:.0f} %",
                                  textposition='outside',
                                  meta = df['CommNPOStat'],
                                  hovertemplate="%{y} : %{text:.1f} %<br>Qualité de données : %{meta}",
                                  orientation="h",
                                  ))

    fig_OrgQuad2.update_layout(title = title,
                               yaxis = dict(title = ""),
                               xaxis = dict(title = "",
                                            ticksuffix = ' %'),
                               margin = dict(pad = 15),
                               legend = dict(orientation = 'h',
                                             xanchor = 'center',
                                             x = 0.5,
                                             traceorder = 'reversed'),
                               paper_bgcolor='rgba(0,0,0,0)',
                               plot_bgcolor='rgba(0,0,0,0)')

    fig_OrgQuad2.update_yaxes(showline=True, linewidth=1, linecolor='black', position=0)

    return fig_OrgQuad2
