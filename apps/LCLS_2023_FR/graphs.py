import pandas as pd
import plotly.graph_objects as go
import numpy as np
import textwrap

# Example code
# def ExampleGraph(dff1, dff2, name1, name2, title, vol=False):
#     # Graph code here
#     return Graph

def ImpactRates(df, title, var, accessLiquidity = False):

    title = "<br>".join(textwrap.wrap(title, width=70))
    # Special case: accessLiquidity graph has its own sorting
    if not accessLiquidity:
        df = df.sort_values("CommNPO")

    fig_ImpactRates = go.Figure()

    fig_ImpactRates.add_trace(go.Bar(y=["<br>".join(textwrap.wrap(label, width=35)) for label in df[var]],
                                     x=round(df['Business'] * 100, 0),
                                     marker=dict(color="#50a684"),
                                     name="Entreprises",
                                     text=df['Business']*100,
                                     texttemplate="%{text:.0f} %",
                                     textposition="outside",
                                     meta=df['BusinessStat'],
                                     hovertemplate="%{y} : "+"%{text:.1f} %"+"<br>Qualité de données : "+"%{meta}",
                                     orientation='h'))

    fig_ImpactRates.add_trace(go.Bar(y=["<br>".join(textwrap.wrap(label, width=35)) for label in df[var]],
                                     x=round(df['GovAgency'] * 100, 0),
                                     marker=dict(color="#ffc72c"),
                                     name="Institutions gouvernementales",
                                     text=df['GovAgency']*100,
                                     texttemplate="%{text:.0f} %",
                                     textposition="outside",
                                     meta=df['GovAgencyStat'],
                                     hovertemplate="%{y} : "+"%{text:.1f} %"+"<br>Qualité de données : "+"%{meta}",
                                     orientation='h'))

    fig_ImpactRates.add_trace(go.Bar(y=["<br>".join(textwrap.wrap(label, width=35)) for label in df[var]],
                                     x=round(df['BusNPO'] * 100, 0),
                                     marker=dict(color="#7bafd4"),
                                     name="Institutions commerciales à but non lucratif",
                                     text=df['BusNPO']*100,
                                     texttemplate="%{text:.0f} %",
                                     textposition="outside",
                                     meta=df['BusNPOStat'],
                                     hovertemplate="%{y} : " + "%{text:.1f} %" + "<br>Qualité de données : " + "%{meta}",
                                     orientation='h'))

    fig_ImpactRates.add_trace(go.Bar(y=["<br>".join(textwrap.wrap(label, width=35)) for label in df[var]],
                                     x=round(df['CommNPO'] * 100, 0),
                                     marker=dict(color="#c8102e"),
                                     name="Organismes communautaires à but non lucratif",
                                     text=df['CommNPO']*100,
                                     texttemplate="%{text:.0f} %",
                                     textposition="outside",
                                     meta=df['CommNPOStat'],
                                     hovertemplate="%{y} : " + "%{text:.1f} %" + "<br>Qualité de données : " + "%{meta}",
                                     orientation='h'))

    fig_ImpactRates.update_layout(title = title,
                                  yaxis=dict(title=""),
                                  xaxis=dict(title="",
                                             showticklabels=False,
                                             showgrid=False),
                                  margin=dict(pad=15),
                                  legend=dict(orientation='h',
                                              xanchor='center',
                                              x=0.5,
                                              traceorder='reversed'),
                                 paper_bgcolor='rgba(0,0,0,0)',
                                 plot_bgcolor='rgba(0,0,0,0)')

    fig_ImpactRates.update_yaxes(showline=True, linewidth=1, linecolor='black', position=0)

    return fig_ImpactRates

def ImpactOrgType(df, title):

    title = "<br>".join(textwrap.wrap(title, width=70))

    fig_ImpactOrgType = go.Figure()

    fig_ImpactOrgType.add_trace(go.Bar(y=df['dateLabel'],
                                       x=round(df['Business'] * 100, 0),
                                       marker=dict(color="#50a684"),
                                       name="Entreprises",
                                       text=df['Business']*100,
                                       texttemplate="%{text:.0f} %",
                                       textposition='outside',
                                       meta=df['BusinessStat'],
                                       hovertemplate="%{y} : %{text:.1f} %<br>Qualité de données : %{meta}",
                                       orientation='h'
    ))

    fig_ImpactOrgType.add_trace(go.Bar(y=df['dateLabel'],
                                       x=round(df['GovAgency'] * 100, 0),
                                       marker=dict(color="#ffc72c"),
                                       name="Institutions gouvernementales",
                                       text=df['GovAgency']*100,
                                       texttemplate="%{text:.0f} %",
                                       textposition='outside',
                                       meta=df['GovAgencyStat'],
                                       hovertemplate="%{y} : %{text:.1f} %<br>Qualité de données : %{meta}",
                                       orientation='h'
                                       ))

    fig_ImpactOrgType.add_trace(go.Bar(y=df['dateLabel'],
                                       x=round(df['BusNPO'] * 100, 0),
                                       marker=dict(color="#7bafd4"),
                                       name="Institutions commerciales à but non lucratif",
                                       text=df['BusNPO']*100,
                                       texttemplate="%{text:.0f} %",
                                       textposition='outside',
                                       meta=df['BusNPOStat'],
                                       hovertemplate="%{y} : %{text:.1f} %<br>Qualité de données : %{meta}",
                                       orientation='h'
                                       ))

    fig_ImpactOrgType.add_trace(go.Bar(y=df['dateLabel'],
                                       x=round(df['CommNPO'] * 100, 0),
                                       marker=dict(color="#c8102e"),
                                       name="Organismes communautaires à but non lucratif",
                                       text=df['CommNPO']*100,
                                       texttemplate="%{text:.0f} %",
                                       textposition='outside',
                                       meta=df['CommNPOStat'],
                                       hovertemplate="%{y} : %{text:.1f} %<br>Qualité de données : %{meta}",
                                       orientation='h'
                                       ))

    fig_ImpactOrgType.update_layout(title=title,
                                    yaxis=dict(title=""),
                                    xaxis=dict(title="",
                                               ticksuffix=' %',
                                               showgrid=True,
                                               gridcolor="whitesmoke"),
                                    margin=dict(pad=15),
                                    legend=dict(orientation='h',
                                                xanchor='center',
                                                x=0.5,
                                                traceorder='reversed'),
                                 paper_bgcolor='rgba(0,0,0,0)',
                                 plot_bgcolor='rgba(0,0,0,0)'
                                    )

    fig_ImpactOrgType.update_yaxes(showline=True, linewidth=1, linecolor='black', position=0)

    return fig_ImpactOrgType

def ImpactOrgVertical(df, title):

    title = "<br>".join(textwrap.wrap(title, width=70))

    y_lim = np.nanmax(pd.concat([df['CommNPO'], df['BusNPO'], df['GovAgency'], df['Business']])) * 1.15 * 100

    fig_ImpactOrgVertical = go.Figure()

    fig_ImpactOrgVertical.add_trace(go.Bar(x=df['item2'],
                                           y=round(df['CommNPO'] * 100, 0),
                                           marker=dict(color="#c8102e"),
                                           name="Organismes communautaires à but non lucratif",
                                           text=df['CommNPO']*100,
                                           texttemplate="%{text:.0f} %",
                                           textposition='outside',
                                           meta=df['CommNPOStat'],
                                           hovertemplate="%{x} : %{text:.1f} %<br>Qualité de données : %{meta}"))

    fig_ImpactOrgVertical.add_trace(go.Bar(x=df['item2'],
                                           y=round(df['BusNPO'] * 100, 0),
                                           marker=dict(color="#7bafd4"),
                                           name="Institutions commerciales à but non lucratif",
                                           text=df['BusNPO']*100,
                                           texttemplate="%{text:.0f} %",
                                           textposition='outside',
                                           meta=df['BusNPOStat'],
                                           hovertemplate="%{x} : %{text:.1f} %<br>Qualité de données : %{meta}"))

    fig_ImpactOrgVertical.add_trace(go.Bar(x=df['item2'],
                                           y=round(df['GovAgency'] * 100, 0),
                                           marker=dict(color="#ffc72c"),
                                           name="Institutions gouvernementales",
                                           text=df['GovAgency']*100,
                                           texttemplate="%{text:.0f} %",
                                           textposition='outside',
                                           meta=df['GovAgencyStat'],
                                           hovertemplate="%{x} : %{text:.1f} %<br>Qualité de données : %{meta}"))

    fig_ImpactOrgVertical.add_trace(go.Bar(x=df['item2'],
                                           y=round(df['Business'] * 100, 0),
                                           marker=dict(color="#50a684"),
                                           name="Entreprises",
                                           text=df['Business']*100,
                                           texttemplate="%{text:.0f} %",
                                           textposition='outside',
                                           meta=df['BusinessStat'],
                                           hovertemplate="%{x} : %{text:.1f} %<br>Qualité de données : %{meta}"))

    fig_ImpactOrgVertical.update_layout(title=title,
                                        yaxis=dict(title="",
                                                   showticklabels=False,
                                                   showgrid=False,
                                                   range = (0, y_lim)),
                                        xaxis=dict(title="",
                                                   showgrid=False),
                                        margin=dict(pad=15),
                                        legend=dict(orientation='h',
                                                    xanchor='center',
                                                    x=0.5),
                                        paper_bgcolor='rgba(0,0,0,0)',
                                        plot_bgcolor='rgba(0,0,0,0)'
                                        )

    fig_ImpactOrgVertical.update_xaxes(showline=True, linewidth=1, linecolor='black', position=0)

    return fig_ImpactOrgVertical


def ReceiveCEBA(df, title):

    title = "<br>".join(textwrap.wrap(title, width=70))

    fig_ReceiveCEBA = go.Figure()

    fig_ReceiveCEBA.add_trace(go.Bar(x=["<br>".join(textwrap.wrap(var, width=25)) for var in df['busChar']],
                                     y=df['valNorm'],
                                     name="",
                                     marker=dict(color="#c8102e"),
                                     text=df['valNorm']*100,
                                     texttemplate="%{text:.0f} %",
                                     textposition='outside',
                                     meta=df['status'],
                                     hovertemplate="%{x} : %{text:.0f} %<br>Qualité de données : %{meta}"))

    fig_ReceiveCEBA.update_layout(title=title,
                                  yaxis=dict(title="",
                                             showticklabels=False,
                                             showgrid=False,
                                             range=(0, np.nanmax(df['valNorm'] * 1.15))),
                                  xaxis=dict(title="",
                                             showgrid=False),
                                  margin=dict(pad=15),
                                  paper_bgcolor='rgba(0,0,0,0)',
                                  plot_bgcolor='rgba(0,0,0,0)')

    fig_ReceiveCEBA.update_xaxes(showline=True, linewidth=1, linecolor='black', position=0)
    fig_ReceiveCEBA.update_xaxes(categoryorder='array', categoryarray=['Organismes communautaires à but non lucratif',
                                                                       'Institutions commerciales à but non lucratif',
                                                                       'Institutions gouvernementales',
                                                                       'Entreprises'])

    return fig_ReceiveCEBA

def StatusCEBA(df, title):

    title = "<br>".join(textwrap.wrap(title, width=70))

    y_lim = np.nanmax(pd.concat([df['CommNPO'], df['BusNPO'], df['GovAgency'], df['Business']])) * 1.15 * 100

    fig_statusCEBA = go.Figure()

    fig_statusCEBA.add_trace(go.Bar(x=df['item2'],
                                    y=round(df['CommNPO'] * 100, 0),
                                    marker=dict(color="#c8102e"),
                                    name="Organismes communautaires à but non lucratif",
                                    text=df['CommNPO']*100,
                                    texttemplate="%{text:.0f} %",
                                    textposition='outside',
                                    meta=df['CommNPOStat'],
                                    hovertemplate="%{x} : %{text:.0f} %<br>Qualité de données : %{meta}"))

    fig_statusCEBA.add_trace(go.Bar(x=df['item2'],
                                    y=round(df['BusNPO'] * 100, 0),
                                    marker=dict(color="#7bafd4"),
                                    name="Institutions commerciales à but non lucratif",
                                    text=df['BusNPO']*100,
                                    texttemplate="%{text:.0f} %",
                                    textposition='outside',
                                    meta=df['BusNPOStat'],
                                    hovertemplate="%{x} : %{text:.0f} %<br>Qualité de données : %{meta}"))

    fig_statusCEBA.add_trace(go.Bar(x=df['item2'],
                                    y=round(df['Business'] * 100, 0),
                                    marker=dict(color="#50a684"),
                                    name="Entreprises",
                                    text=df['Business']*100,
                                    texttemplate="%{text:.0f} %",
                                    textposition='outside',
                                    meta=df['BusinessStat'],
                                    hovertemplate="%{x} : %{text:.0f} %<br>Qualité de données : %{meta}"))

    fig_statusCEBA.update_layout(title=title,
                                 yaxis=dict(title="",
                                            showticklabels=False,
                                            showgrid=False,
                                            range=(0, y_lim)),
                                 xaxis=dict(title="",
                                            showgrid=False),
                                 margin=dict(pad=15),
                                 legend=dict(orientation='h',
                                             xanchor='center',
                                             x=0.5),
                                  paper_bgcolor='rgba(0,0,0,0)',
                                  plot_bgcolor='rgba(0,0,0,0)')

    fig_statusCEBA.update_xaxes(showline=True, linewidth=1, linecolor='black', position=0)

    return fig_statusCEBA
