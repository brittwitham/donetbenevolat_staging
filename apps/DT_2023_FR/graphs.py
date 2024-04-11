import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import textwrap

def DonationDouble(df, title):

    title = "<br>".join(textwrap.wrap(title, width=70))

    df = df.sort_values('CommNPO')
    df = df.loc[df['item2'].map({"Other obstacle": -1, "None": -2}).sort_values().index]

    df['item2'] = [textwrap.fill(text, width = 25) for text in df['item2']]

    x_lim = max(pd.concat([df['BusNPO'], df['CommNPO']]))*115

    fig_DonationDouble = go.Figure()

    fig_DonationDouble.add_trace(go.Bar(y=df['item2'],
                                        x=df['BusNPO'] * 100,
                                        marker=dict(color="#7bafd4"),
                                        name="Institutions commerciales à but non lucratif",
                                        text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['BusNPO']],
                                        # texttemplate="%{text:.0f} %",
                                        textposition='outside',
                                        meta=df['BusNPOStat'],
                                        hovertemplate="%{y} : %{x:.0f} %<br>Qualité de données : %{meta}",
                                        orientation="h"))

    fig_DonationDouble.add_trace(go.Bar(y=df['item2'],
                                        x=df['CommNPO'] * 100,
                                        marker=dict(color="#c8102e"),
                                        name="Organismes communautaires à but non lucratif",
                                        text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['CommNPO']],
                                        # texttemplate="%{text:.0f} %",
                                        textposition='outside',
                                        meta=df['CommNPOStat'],
                                        hovertemplate="%{y} : %{x:.0f} %<br>Qualité de données : %{meta}",
                                        orientation="h"))

    fig_DonationDouble.update_layout(title = title,
                                     yaxis=dict(title=""),
                                     xaxis=dict(title="",
                                                showticklabels=False,
                                                showgrid=False,
                                                range=(0, x_lim)),
                                     margin=dict(pad=15),
                                     legend=dict(orientation='h',
                                                 xanchor='center',
                                                 x=0.5,
                                                 traceorder='reversed'),
                                     paper_bgcolor='rgba(0,0,0,0)',
                                     plot_bgcolor='rgba(0,0,0,0)'
                                     )

    fig_DonationDouble.update_yaxes(showline=True, linewidth=1, linecolor='black', position=0)

    return fig_DonationDouble

def DonationSingle(df, title):

    title = "<br>".join(textwrap.wrap(title, width=70))

    fig_DonationSingle = go.Figure()

    x_lim = max(df['valNorm'])*115

    fig_DonationSingle.add_trace(go.Bar(y=df['busChar'],
                                        x=df['valNorm']*100,
                                        marker=dict(color="#c8102e"),
                                        name="",
                                        text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['valNorm']],
                                        # texttemplate="%{text:.0f} %",
                                        textposition='outside',
                                        meta=df['status'],
                                        hovertemplate="%{y} : %{x:.1f} %<br>Qualité de données : %{meta}",
                                        orientation = "h"))

    fig_DonationSingle.update_layout(title=title,
                                     yaxis=dict(title="",
                                                categoryorder="array",
                                                # categoryorder=df['busGroup']
                                                ),
                                     xaxis = dict(title="",
                                                  showticklabels=False,
                                                  showgrid=False,
                                                  range=(0, x_lim)),
                                     margin = dict(pad=15),
                                     legend = dict(orientation='h',
                                                   xanchor='center',
                                                   x=0.5,
                                                   traceorder='reversed'),
                                     paper_bgcolor='rgba(0,0,0,0)',
                                     plot_bgcolor='rgba(0,0,0,0)'
                                     )

    fig_DonationSingle.update_yaxes(showline=True, linewidth=1, linecolor='black', position=0)

    return fig_DonationSingle
