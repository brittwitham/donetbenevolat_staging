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

    fig_DonationDouble = go.Figure()

    fig_DonationDouble.add_trace(go.Bar(y=df['item2'],
                                        x=round(df['BusNPO'] * 100, 0),
                                        marker=dict(color="#7bafd4"),
                                        name="Institutions commerciales à but non lucratif",
                                        text=df['BusNPO']*100,
                                        texttemplate="%{text:.0f} %",
                                        textposition='outside',
                                        meta=df['BusNPOStat'],
                                        hovertemplate="%{y} : %{text:.0f} %<br>Qualité de données : %{meta}",
                                        orientation="h"))

    fig_DonationDouble.add_trace(go.Bar(y=df['item2'],
                                        x=round(df['CommNPO'] * 100, 0),
                                        marker=dict(color="#c8102e"),
                                        name="Organismes communautaires à but non lucratif",
                                        text=df['CommNPO']*100,
                                        texttemplate="%{text:.0f} %",
                                        textposition='outside',
                                        meta=df['CommNPOStat'],
                                        hovertemplate="%{y} : %{text:.0f} %<br>Qualité de données : %{meta}",
                                        orientation="h"))

    fig_DonationDouble.update_layout(title = title,
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
                                     plot_bgcolor='rgba(0,0,0,0)'
                                     )

    fig_DonationDouble.update_yaxes(showline=True, linewidth=1, linecolor='black', position=0)

    return fig_DonationDouble

def DonationSingle(df, title):

    title = "<br>".join(textwrap.wrap(title, width=70))

    fig_DonationSingle = go.Figure()

    fig_DonationSingle.add_trace(go.Bar(y=df['busChar'],
                                        x=df['valNorm'],
                                        marker=dict(color="#c8102e"),
                                        name="",
                                        text=df['valNorm']*100,
                                        texttemplate="%{text:.0f} %",
                                        textposition='outside',
                                        meta=df['status'],
                                        hovertemplate="%{y} : %{text:.1f} %<br>Qualité de données : %{meta}",
                                        orientation = "h"))

    fig_DonationSingle.update_layout(title=title,
                                     yaxis=dict(title="",
                                                categoryorder="array",
                                                # categoryorder=df['busGroup']
                                                ),
                                     xaxis = dict(title="",
                                                  showticklabels=False,
                                                  showgrid=False),
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
