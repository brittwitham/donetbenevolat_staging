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
                                     x=round(df['Business'] * 100, 0),
                                     marker=dict(color="#50a684"),
                                     name="Businesses",
                                     text=df['Business'],
                                     texttemplate="%{text:.0%}",
                                     textposition="outside",
                                     meta=df['BusinessStat'],
                                     hovertemplate="%{y}: "+"%{text:.1%}"+"<br>Data quality: "+"%{meta}",
                                     orientation='h'))

    fig_ImpactRates.add_trace(go.Bar(y=["<br>".join(textwrap.wrap(label, width=35)) for label in df[var]],
                                     x=round(df['GovAgency'] * 100, 0),
                                     marker=dict(color="#ffc72c"),
                                     name="Government agencies",
                                     text=df['GovAgency'],
                                     texttemplate="%{text:.0%}",
                                     textposition="outside",
                                     meta=df['GovAgencyStat'],
                                     hovertemplate="%{y}: "+"%{text:.1%}"+"<br>Data quality: "+"%{meta}",
                                     orientation='h'))

    fig_ImpactRates.add_trace(go.Bar(y=["<br>".join(textwrap.wrap(label, width=35)) for label in df[var]],
                                     x=round(df['BusNPO'] * 100, 0),
                                     marker=dict(color="#7bafd4"),
                                     name="Business NPOs",
                                     text=df['BusNPO'],
                                     texttemplate="%{text:.0%}",
                                     textposition="outside",
                                     meta=df['BusNPOStat'],
                                     hovertemplate="%{y}: " + "%{text:.1%}" + "<br>Data quality: " + "%{meta}",
                                     orientation='h'))

    fig_ImpactRates.add_trace(go.Bar(y=["<br>".join(textwrap.wrap(label, width=35)) for label in df[var]],
                                     x=round(df['CommNPO'] * 100, 0),
                                     marker=dict(color="#c8102e"),
                                     name="Community NPOs",
                                     text=df['CommNPO'],
                                     texttemplate="%{text:.0%}",
                                     textposition="outside",
                                     meta=df['CommNPOStat'],
                                     hovertemplate="%{y}: " + "%{text:.1%}" + "<br>Data quality: " + "%{meta}",
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
                                       name="Businesses",
                                       text=df['Business'],
                                       texttemplate="%{text:.0%}",
                                       textposition='outside',
                                       meta=df['BusinessStat'],
                                       hovertemplate="%{y}: %{text:.1%}<br>Data quality: %{meta}",
                                       orientation='h'
    ))

    fig_ImpactOrgType.add_trace(go.Bar(y=df['dateLabel'],
                                       x=round(df['GovAgency'] * 100, 0),
                                       marker=dict(color="#ffc72c"),
                                       name="Government agencies",
                                       text=df['GovAgency'],
                                       texttemplate="%{text:.0%}",
                                       textposition='outside',
                                       meta=df['GovAgencyStat'],
                                       hovertemplate="%{y}: %{text:.1%}<br>Data quality: %{meta}",
                                       orientation='h'
                                       ))

    fig_ImpactOrgType.add_trace(go.Bar(y=df['dateLabel'],
                                       x=round(df['BusNPO'] * 100, 0),
                                       marker=dict(color="#7bafd4"),
                                       name="Business NPOs",
                                       text=df['BusNPO'],
                                       texttemplate="%{text:.0%}",
                                       textposition='outside',
                                       meta=df['BusNPOStat'],
                                       hovertemplate="%{y}: %{text:.1%}<br>Data quality: %{meta}",
                                       orientation='h'
                                       ))

    fig_ImpactOrgType.add_trace(go.Bar(y=df['dateLabel'],
                                       x=round(df['CommNPO'] * 100, 0),
                                       marker=dict(color="#c8102e"),
                                       name="Community NPOs",
                                       text=df['CommNPO'],
                                       texttemplate="%{text:.0%}",
                                       textposition='outside',
                                       meta=df['CommNPOStat'],
                                       hovertemplate="%{y}: %{text:.1%}<br>Data quality: %{meta}",
                                       orientation='h'
                                       ))

    fig_ImpactOrgType.update_layout(title=title,
                                    yaxis=dict(title=""),
                                    xaxis=dict(title="",
                                               ticksuffix='%',
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
                                           name="Community NPOs",
                                           text=df['CommNPO'],
                                           texttemplate="%{text:.0%}",
                                           textposition='outside',
                                           meta=df['CommNPOStat'],
                                           hovertemplate="%{x}: %{text:.1%}<br>Data quality: %{meta}"))

    fig_ImpactOrgVertical.add_trace(go.Bar(x=df['item2'],
                                           y=round(df['BusNPO'] * 100, 0),
                                           marker=dict(color="#7bafd4"),
                                           name="Business NPOs",
                                           text=df['BusNPO'],
                                           texttemplate="%{text:.0%}",
                                           textposition='outside',
                                           meta=df['BusNPOStat'],
                                           hovertemplate="%{x}: %{text:.1%}<br>Data quality: %{meta}"))

    fig_ImpactOrgVertical.add_trace(go.Bar(x=df['item2'],
                                           y=round(df['GovAgency'] * 100, 0),
                                           marker=dict(color="#ffc72c"),
                                           name="Government agencies",
                                           text=df['GovAgency'],
                                           texttemplate="%{text:.0%}",
                                           textposition='outside',
                                           meta=df['GovAgencyStat'],
                                           hovertemplate="%{y}: %{text:.1%}<br>Data quality: %{meta}"))

    fig_ImpactOrgVertical.add_trace(go.Bar(x=df['item2'],
                                           y=round(df['Business'] * 100, 0),
                                           marker=dict(color="#50a684"),
                                           name="Businesses",
                                           text=df['Business'],
                                           texttemplate="%{text:.0%}",
                                           textposition='outside',
                                           meta=df['BusinessStat'],
                                           hovertemplate="%{y}: %{text:.1%}<br>Data quality: %{meta}"))

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
