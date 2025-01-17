import pandas as pd
import plotly.graph_objects as go
import numpy as np
import textwrap

def ImpactRates(df, title, var, accessLiquidity = False):

    title = "<br>".join(textwrap.wrap(title, width=70))
    # Special case: accessLiquidity graph has its own sorting
    if not accessLiquidity:
        df = df.sort_values("CommNPO")

    fig_ImpactRates = go.Figure()

    fig_ImpactRates.add_trace(go.Bar(y=["<br>".join(textwrap.wrap(label, width=35)) for label in df[var]],
                                     x=df['Business'] * 100,
                                     marker=dict(color="#0B6623"),
                                     name="Entreprises",
                                     text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['Business']],
                                     # texttemplate="%{text:.0f} %",
                                     textposition="outside",
                                     meta=df['BusinessStat'],
                                     hovertemplate="%{y} : "+"%{x:.1f} %"+"<br>Qualité de données : "+"%{meta}",
                                     orientation='h'))

    fig_ImpactRates.add_trace(go.Bar(y=["<br>".join(textwrap.wrap(label, width=35)) for label in df[var]],
                                     x=df['GovAgency'] * 100,
                                     marker=dict(color="#FCD12A"),
                                     name="Institutions gouvernementales",
                                     text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['GovAgency']],
                                     # texttemplate="%{text:.0f} %",
                                     textposition="outside",
                                     meta=df['GovAgencyStat'],
                                     hovertemplate="%{y} : "+"%{x:.1f} %"+"<br>Qualité de données : "+"%{meta}",
                                     orientation='h'))

    fig_ImpactRates.add_trace(go.Bar(y=["<br>".join(textwrap.wrap(label, width=35)) for label in df[var]],
                                     x=df['BusNPO'] * 100,
                                     marker=dict(color="#234C66"),
                                     name="Institutions commerciales à but non lucratif",
                                     text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['BusNPO']],
                                     # texttemplate="%{text:.0f} %",
                                     textposition="outside",
                                     meta=df['BusNPOStat'],
                                     hovertemplate="%{y} : " + "%{x:.1f} %" + "<br>Qualité de données : " + "%{meta}",
                                     orientation='h'))

    fig_ImpactRates.add_trace(go.Bar(y=["<br>".join(textwrap.wrap(label, width=35)) for label in df[var]],
                                     x=df['CommNPO'] * 100,
                                     marker=dict(color="#FD7B5F"),
                                     name="Organismes communautaires à but non lucratif",
                                     text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['CommNPO']],
                                     # texttemplate="%{text:.0f} %",
                                     textposition="outside",
                                     meta=df['CommNPOStat'],
                                     hovertemplate="%{y} : " + "%{x:.1f} %" + "<br>Qualité de données : " + "%{meta}",
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
                                       x=df['Business'] * 100,
                                       marker=dict(color="#0B6623"),
                                       name="Entreprises",
                                       text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['Business']],
                                       # texttemplate="%{text:.0f} %",
                                       textposition='outside',
                                       meta=df['BusinessStat'],
                                       hovertemplate="%{y} : %{x:.1f} %<br>Qualité de données : %{meta}",
                                       orientation='h'
    ))

    fig_ImpactOrgType.add_trace(go.Bar(y=df['dateLabel'],
                                       x=df['GovAgency'] * 100,
                                       marker=dict(color="#FCD12A"),
                                       name="Institutions gouvernementales",
                                       text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['GovAgency']],
                                       # texttemplate="%{text:.0f} %",
                                       textposition='outside',
                                       meta=df['GovAgencyStat'],
                                       hovertemplate="%{y} : %{x:.1f} %<br>Qualité de données : %{meta}",
                                       orientation='h'
                                       ))

    fig_ImpactOrgType.add_trace(go.Bar(y=df['dateLabel'],
                                       x=df['BusNPO'] * 100,
                                       marker=dict(color="#234C66"),
                                       name="Institutions commerciales à but non lucratif",
                                       text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['BusNPO']],
                                       # texttemplate="%{text:.0f} %",
                                       textposition='outside',
                                       meta=df['BusNPOStat'],
                                       hovertemplate="%{y} : %{x:.1f} %<br>Qualité de données : %{meta}",
                                       orientation='h'
                                       ))

    fig_ImpactOrgType.add_trace(go.Bar(y=df['dateLabel'],
                                       x=df['CommNPO'] * 100,
                                       marker=dict(color="#FD7B5F"),
                                       name="Organismes communautaires à but non lucratif",
                                       text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['CommNPO']],
                                       # texttemplate="%{text:.0f} %",
                                       textposition='outside',
                                       meta=df['CommNPOStat'],
                                       hovertemplate="%{y} : %{x:.1f} %<br>Qualité de données : %{meta}",
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
                                           y=df['CommNPO'] * 100,
                                           marker=dict(color="#FD7B5F"),
                                           name="Organismes communautaires à but non lucratif",
                                           text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['CommNPO']],
                                           # texttemplate="%{text:.0f} %",
                                           textposition='outside',
                                           meta=df['CommNPOStat'],
                                           hovertemplate="%{x} : %{y:.1f} %<br>Qualité de données : %{meta}"))

    fig_ImpactOrgVertical.add_trace(go.Bar(x=df['item2'],
                                           y=df['BusNPO'] * 100,
                                           marker=dict(color="#234C66"),
                                           name="Institutions commerciales à but non lucratif",
                                           text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['BusNPO']],
                                           # texttemplate="%{text:.0f} %",
                                           textposition='outside',
                                           meta=df['BusNPOStat'],
                                           hovertemplate="%{x} : %{y:.1f} %<br>Qualité de données : %{meta}"))

    fig_ImpactOrgVertical.add_trace(go.Bar(x=df['item2'],
                                           y=df['GovAgency'] * 100,
                                           marker=dict(color="#FCD12A"),
                                           name="Institutions gouvernementales",
                                           text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['GovAgency']],
                                           # texttemplate="%{text:.0f} %",
                                           textposition='outside',
                                           meta=df['GovAgencyStat'],
                                           hovertemplate="%{x} : %{y:.1f} %<br>Qualité de données : %{meta}"))

    fig_ImpactOrgVertical.add_trace(go.Bar(x=df['item2'],
                                           y=df['Business'] * 100,
                                           marker=dict(color="#0B6623"),
                                           name="Entreprises",
                                           text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['Business']],
                                           # texttemplate="%{text:.0f} %",
                                           textposition='outside',
                                           meta=df['BusinessStat'],
                                           hovertemplate="%{x} : %{y:.1f} %<br>Qualité de données : %{meta}"))

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
