import pandas as pd
import plotly.graph_objects as go
import numpy as np
import textwrap

# Example code
def OrgQuad1(df, title):

    title = "<br>".join(textwrap.wrap(title, width=70)) + "<br><sup>Remarque : veuillez passer le curseur sur les barres pour connaître les valeurs exactes</sup>"

    df = df.sort_values('Business')
    df = df.loc[df['item2'].map({"Other obstacle": -1, "None": -2}).sort_values().index]

    fig_OrgQuad1 = go.Figure()

    fig_OrgQuad1.add_trace(go.Bar(x = df['Business'] * 100,
                                  y=df['item2'],
                                  marker = dict(color = "#0B6623"),
                                  name = "Entreprises",
                                  text = [str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['Business']],
                                  # texttemplate = "%{text:.0f} %",
                                  textposition = "none",
                                  meta = df['BusinessStat'],
                                  hovertemplate = "%{y} : " + "%{x:.1f} %" + "<br>Qualité de données : " + "%{meta}",
                                  orientation='h'))

    fig_OrgQuad1.add_trace(go.Bar(x = df['GovAgency'] * 100,
                                  y=df['item2'],
                                  marker = dict(color = "#FCD12A"),
                                  name = "Institutions gouvernementales",
                                  text = [str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['GovAgency']],
                                  # texttemplate="%{text:.0f} %",
                                  textposition="none",
                                  meta = df['GovAgencyStat'],
                                  hovertemplate="%{y} : " + "%{x:.1f} %" + "<br>Qualité de données : " + "%{meta}",
                                  orientation='h'))

    fig_OrgQuad1.add_trace(go.Bar(x = df['BusNPO'] * 100,
                                  y=df['item2'],
                                  marker = dict(color = "#234C66"),
                                  name = "Institutions commerciales à but non lucratif",
                                  text = [str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['BusNPO']],
                                  # texttemplate="%{text:.0f} %",
                                  textposition="none",
                                  meta = df['BusNPOStat'],
                                  hovertemplate="%{y} : " + "%{x:.1f} %" + "<br>Qualité de données : " + "%{meta}",
                                  orientation='h'))

    fig_OrgQuad1.add_trace(go.Bar(x = df['CommNPO'] * 100,
                                  y=df['item2'],
                                  marker = dict(color = "#FD7B5F"),
                                  name = "Organismes communautaires à but non lucratif",
                                  text = [str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['CommNPO']],
                                  # texttemplate="%{text:.0f} %",
                                  textposition="none",
                                  meta = df['CommNPOStat'],
                                  hovertemplate="%{y} : " + "%{x:.1f} %" + "<br>Qualité de données : " + "%{meta}",
                                  orientation='h'))

    fig_OrgQuad1.update_layout(title = dict(text=title,
                                            y=0.971,
                                            yanchor="bottom"),
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

    title = "<br>".join(textwrap.wrap(title, width=70)) + "<br><sup>Remarque : aucune donnée n’est disponible pour certains trimestres et pour certaines années</sup>"

    df = df.sort_values("seriesDate")

    fig_OrgQuad2 = go.Figure()

    fig_OrgQuad2.add_trace(go.Bar(y = df['dateLabel'],
                                  x = df['Business'] * 100,
                                  marker = dict(color = "#0B6623"),
                                  name = "Entreprises",
                                  text = [str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['Business']],
                                  # texttemplate = "%{text:.0f} %",
                                  textposition = 'outside',
                                  meta = df['BusinessStat'],
                                  hovertemplate = "%{y} : %{x:.1f} %<br>Qualité de données : %{meta}",
                                  orientation="h",
                                  ))

    fig_OrgQuad2.add_trace(go.Bar(y = df['dateLabel'],
                                  x = df['GovAgency'] * 100,
                                  marker = dict(color = "#FCD12A"),
                                  name = "Institutions gouvernementales",
                                  text = [str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['GovAgency']],
                                  # texttemplate="%{text:.0f} %",
                                  textposition='outside',
                                  meta = df['GovAgencyStat'],
                                  hovertemplate="%{y} : %{x:.1f} %<br>Qualité de données : %{meta}",
                                  orientation="h",
                                  ))

    fig_OrgQuad2.add_trace(go.Bar(y = df['dateLabel'],
                                  x = df['BusNPO'] * 100,
                                  marker = dict(color = "#234C66"),
                                  name = "Institutions commerciales à but non lucratif",
                                  text = [str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['BusNPO']],
                                  # texttemplate="%{text:.0f} %",
                                  textposition='outside',
                                  meta=df['BusNPOStat'],
                                  hovertemplate="%{y} : %{x:.1f} %<br>Qualité de données : %{meta}",
                                  orientation="h",
                                  ))

    fig_OrgQuad2.add_trace(go.Bar(y = df['dateLabel'],
                                  x = df['CommNPO'] * 100,
                                  marker = dict(color = "#FD7B5F"),
                                  name = "Organismes communautaires à but non lucratif",
                                  text = [str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['CommNPO']],
                                  # texttemplate="%{text:.0f} %",
                                  textposition='outside',
                                  meta = df['CommNPOStat'],
                                  hovertemplate="%{y} : %{x:.1f} %<br>Qualité de données : %{meta}",
                                  orientation="h",
                                  ))

    fig_OrgQuad2.update_layout(title = dict(text=title,
                                            y=0.971,
                                            yanchor="bottom"),
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
