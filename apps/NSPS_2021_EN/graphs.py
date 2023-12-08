import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import os
import os.path as op
import re


def SubSec(df, title):

    df = df.loc[df['subSector'].map({"Community nonprofits": 0,
                                     "Business nonprofits": 1,
                                     "Government nonprofits": 2}).sort_values().index]

    fig_SubSec = go.Figure()

    # Core sub-sector (red)
    fig_SubSec.add_trace(
        go.Bar(
            x=df['subSector'],
            y=np.where(
                df["coreStatus"] == "Core sub-sector",
                df['valNormP'],
                np.nan),
            text=[
                str(
                    int(
                        round(
                            df['valNormP'].loc[i] *
                            100,
                            0))) +
                "%" if df.loc[i]["coreStatus"] == "Core sub-sector" else '' for i in df.index],
            textposition='outside',
            textfont=dict(
                size=15,
                color="black"),
            marker=dict(
                color='#c8102e'),
            showlegend=True,
            name="Core sub-sector",
            hoverinfo='skip'))

    # Government sub-sector (blue)
    fig_SubSec.add_trace(
        go.Bar(
            x=df['subSector'],
            y=np.where(
                df["coreStatus"] == "Government sub-sector",
                df['valNormP'],
                np.nan),
            text=[
                str(
                    int(
                        round(
                            df['valNormP'].loc[i] *
                            100,
                            0))) +
                "%" if df.loc[i]["coreStatus"] == "Government sub-sector" else '' for i in df.index],
            textposition='outside',
            textfont=dict(
                size=15,
                color="black"),
            marker=dict(
                color='#7bafd4'),
            showlegend=True,
            name="Government sub-sector",
            hoverinfo='skip'))

    # Mid-bar text
    for i in df.index:
        fig_SubSec.add_annotation(x=df.loc[i]['subSector'],
                                  y=df.loc[i]['valNormP'] / 2,
                                  #  text = df.loc[i]['label'],
                                  font=dict(size=15, color="white"),
                                  showarrow=False)

    fig_SubSec.update_layout(title=dict(text=title,
                                        xanchor='left',
                                        x=0.02),
                             yaxis=dict(title="",
                                        showgrid=False,
                                        showticklabels=False),
                             xaxis=dict(title="",
                                        tickfont=dict(size=15)),
                             barmode="overlay",
                             legend=dict(orientation='h',
                                         xanchor='center',
                                         x=0.5,
                                         y=-0.1,
                                         font=dict(size=15)))

    return fig_SubSec


def Growth(df, title, trace_settings):
    # TODO: Chck if hovertext needs to be added
    fig_Growth = go.Figure()

    df['refDate'] = pd.to_datetime(df['refDate'])

    for var in trace_settings.keys():
        fig_Growth.add_trace(go.Scatter(x=df['refDate'].dt.year,
                                        y=df[var],
                                        name=trace_settings[var]['name'],
                                        mode='lines',
                                        line=trace_settings[var]['line_dict'],
                                        hovertemplate='%{y:0.2f}'))

    fig_Growth.update_layout(title=dict(text=title,
                                        xanchor='left',
                                        x=0.02),
                             yaxis=dict(title="",
                                        tickformat='.2f',
                                        nticks=4,
                                        # griddash = 'dot'
                                        ),
                             xaxis=dict(title="",
                                        showgrid=False,
                                        tick0=2009,
                                        dtick=1,
                                        tickfont=dict(size=12)),
                             legend=dict(orientation='h',
                                         xanchor='center',
                                         x=0.5,
                                         y=-0.1,
                                         font=dict(size=15)),
                             hoverlabel=dict(align='right'),
                             hovermode='x unified')

    return fig_Growth


def SubSecActivity(df, title, vars):
    var_1 = vars[0]
    var_2 = vars[1]
    # Set limits based on max/min values
    limitRight = max(pd.concat([df[var_2], df[var_1]])) * 1.15 * 100
    limitLeft = max(max(df[var_2]) * 100 * 0.7, max(df[var_1]) * 100 * 1.15)

    # Sort data in correct order, anchoring "Other" at the bottom
    df = pd.concat([df[df['activity'] == "Other"],
                   df[df['activity'] != "Other"].sort_values(var_1)], axis=0)

    fig_SubSecActivity = make_subplots(rows=1, cols=2)

    fig_SubSecActivity.add_trace(go.Bar(  # y = ~str_wrap_factor(fct_rev(activity), 28),
        y=df['activity'],
        x=df[var_1] * 100,
        name="Core nonprofits",
        orientation='h',
        marker=dict(color="#c8102e"),
        text=round(df[var_1] * 100, 0).astype(int).map(str) + "%",
        textposition='outside',
        textfont=dict(size=12, color="black"),
        hoverinfo='skip'), row=1, col=1)

    fig_SubSecActivity.add_trace(go.Bar(  # y = ~str_wrap_factor(fct_rev(activity), 25),
        y=df['activity'],
        x=df[var_2] * 100,
        name="Government nonprofits",
        orientation='h',
        marker=dict(color="#7BAFD4"),
        text=np.where(
            df[var_2] > 0,
            round(
                df[var_2] *
                100,
                0).astype(int).map(str) +
            "%",
            ""),
        textposition='outside',
        textfont=dict(size=12, color="black"),
        hoverinfo='skip'), row=1, col=2)

    # X-axes
    fig_SubSecActivity.update_xaxes(title="",
                                    showgrid=False,
                                    showticklabels=False,
                                    range=(limitLeft, 0),
                                    row=1, col=1)

    fig_SubSecActivity.update_xaxes(title="",
                                    showgrid=False,
                                    showticklabels=False,
                                    range=(0, limitRight),
                                    row=1, col=2)

    # Y-axes
    fig_SubSecActivity.update_yaxes(title="",
                                    showgrid=True,
                                    tickson='boundaries',
                                    tickfont=dict(size=14),
                                    row=1, col=1)
    fig_SubSecActivity.update_yaxes(title="",
                                    showgrid=True,
                                    showticklabels=False,
                                    tickson='boundaries',
                                    row=1, col=2)

    fig_SubSecActivity.update_layout(title=dict(text=title,
                                                xanchor='left',
                                                x=0.02),
                                     legend=dict(orientation='h',
                                                 xanchor='center',
                                                 x=0.5,
                                                 y=-0.05,
                                                 font=dict(size=15)))
    return fig_SubSecActivity
