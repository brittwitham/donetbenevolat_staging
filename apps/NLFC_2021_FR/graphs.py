import pandas as pd
import plotly.graph_objects as go
import numpy as np
import os
import os.path as op
import re
import textwrap


def jobsType_fig(df, title):
    fig_jobsType = go.Figure()

    df['subSector'] = [textwrap.fill(title, width=16) for title in df['subSector']]

    fig_jobsType.add_trace(go.Bar(x=["<br>".join(textwrap.wrap(label, width=16)) for label in df['subSector']],
                                  y=df['valNorm_FT'],
                                  name="Emplois à plein temps",
                                  marker=dict(color="#c8102e"),
                                  text=(df['valNormP_FT']*100).astype(str),
                                  texttemplate='%{text:.0f} %',
                                  textposition='inside',
                                  insidetextanchor='middle',
                                  textfont=dict(size=15, color="white"),
                                  hovertemplate='%{y:,}'))

    fig_jobsType.add_trace(go.Bar(x=["<br>".join(textwrap.wrap(label, width=16)) for label in df['subSector']],
                                  y=df['valNorm_PT'],
                                  name="Emplois à temps partiel",
                                  marker=dict(color="#7bafd4"),
                                  text=(df['valNormP_PT']*100).astype(str),
                                  texttemplate='%{text:.0f} %',
                                  textposition='inside',
                                  insidetextanchor='middle',
                                  textfont=dict(size=15, color="white"),
                                  hovertemplate='%{y:,}'))

    for i in df.index:
        fig_jobsType.add_annotation(x="<br>".join(textwrap.wrap(df.loc[i]['subSector'], width=16)),
                                    y=df.loc[i]['valNorm_Tot'],
                                    # marker = dict(opacity = 0),
                                    text=f'{int(df.loc[i]["valNorm_Tot"]):,}',
                                    # texttemplate = '%{text:,}',
                                    yanchor='bottom',
                                    # showlegend = False,
                                    font=dict(size=15, color="black"),
                                    showarrow=False, )

    fig_jobsType.update_layout(barmode='stack',
                               title=dict(text=title,
                                          xanchor='left', x=0.02),
                               margin=dict(t=50),
                               yaxis=dict(title="",
                                          showgrid=False,
                                          showticklabels=False),
                               xaxis=dict(title="",
                                          showgrid=False,
                                          dtick=1,
                                          tickfont=dict(size=15)),
                               legend=dict(orientation='h',
                                           xanchor='center',
                                           x=0.5,
                                           y=-0.4,
                                           font=dict(size=15)),
                               paper_bgcolor='rgba(0,0,0,0)',
                               plot_bgcolor='rgba(0,0,0,0)')

    fig_jobsType.update_xaxes(showline=True, linewidth=1, linecolor='black')
    fig_jobsType.update_yaxes(range=[0, max(pd.concat([df['valNorm_PT'], df['valNorm_FT'], df['valNorm_Tot']], axis=0)) * 1.1])

    return fig_jobsType


def wagesType_fig(df, title):
    fig_wagesType = go.Figure()

    df['subSector'] = [textwrap.fill(title, width=16) for title in df['subSector']]

    fig_wagesType.add_trace(go.Bar(x=["<br>".join(textwrap.wrap(label, width=16)) for label in df['subSector']],
                                   y=df['FT'],
                                   name="Emplois à plein temps",
                                   marker=dict(color="#c8102e"),
                                   text=df['FT'],
                                   texttemplate='%{text:,} $',
                                   textposition='outside',
                                   textfont=dict(size=15, color="black"),
                                   hoverinfo="skip"))

    fig_wagesType.add_trace(go.Bar(x=["<br>".join(textwrap.wrap(label, width=16)) for label in df['subSector']],
                                   y=df['PT'],
                                   name="Emplois à temps partiel",
                                   marker=dict(color="#7bafd4"),
                                   text=df['PT'],
                                   texttemplate='%{text:,} $',
                                   textposition='outside',
                                   textfont=dict(size=15, color="black"),
                                   hoverinfo="skip"))

    fig_wagesType.add_trace(go.Bar(x=["<br>".join(textwrap.wrap(label, width=16)) for label in df['subSector']],
                                   y=df['Tot'],
                                   name="Tous les emplois",
                                   marker=dict(color="#7A4A89"),
                                   text=df['Tot'],
                                   texttemplate='%{text:,} $',
                                   textposition='outside',
                                   textfont=dict(size=15, color="black"),
                                   hoverinfo="skip"))

    fig_wagesType.update_layout(title=dict(text=title,
                                           xanchor='left',
                                           x=0.02),
                                margin=dict(t=50),
                                yaxis=dict(title="",
                                           showgrid=False,
                                           showticklabels=False),
                                xaxis=dict(title="",
                                           showgrid=False,
                                           dtick=1,
                                           tickfont=dict(size=15)),
                                legend=dict(orientation='h',
                                            xanchor='center',
                                            x=0.5,
                                            y=-0.4,
                                            font=dict(size=15)),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)')

    fig_wagesType.update_xaxes(showline=True, linewidth=1, linecolor='black')
    fig_wagesType.update_yaxes(range=[0, max(pd.concat([df['PT'], df['FT'], df['Tot']], axis=0)) * 1.1])

    return fig_wagesType


def EmpDemog(df, title, jobs=True):
    if jobs:
        var1 = 'valNormP_Comm'
        var2 = 'valNormP_Bus'
        var3 = 'valNormP_Govt'
        template = '%{text:.0f} %'
        # template = '%{text:.0%}'
        hovertemplate = '%{hovertext:,}'

        fig_jobsDemog = go.Figure()

        fig_jobsDemog.add_trace(
            go.Bar(
                x=["<br>".join(textwrap.wrap(label, width=15)) for label in df['characteristics']],
                y=df[var1],
                name="Organismes communautaires à but non lucratif",
                marker=dict(
                    color='#7bafd4'),
                text=df[var1]*100,
                texttemplate=template,
                textposition='outside',
                textfont=dict(
                    size=15,
                    color="black"),
               hovertext=df['valNorm_Comm'],
               hovertemplate='%{hovertext:,}'))

        fig_jobsDemog.add_trace(
            go.Bar(
                x=["<br>".join(textwrap.wrap(label, width=15)) for label in df['characteristics']],
                y=df[var2],
                name="institutions commerciales à but non lucratif",
                marker=dict(
                    color='#9ac1dd'),
                text=df[var2]*100,
                texttemplate=template,
                textposition='outside',
                textfont=dict(
                    size=15,
                    color="black"),
               hovertext=df["valNorm_Bus"],
               hovertemplate='%{hovertext:,}'))

        fig_jobsDemog.add_trace(
            go.Bar(
                x=["<br>".join(textwrap.wrap(label, width=15)) for label in df['characteristics']],
                y=df[var3],
                name="Institutions gouvernementales à but non lucratif",
                marker=dict(
                    color='#c8102e'),
                text=df[var3]*100,
                texttemplate=template,
                textposition='outside',
                textfont=dict(
                    size=15,
                    color="black"),
               hovertext=df["valNorm_Govt"],
               hovertemplate='%{hovertext:,}'))

    else:
        var1 = 'Comm'
        var2 = 'Bus'
        var3 = 'Govt'
        template = '%{text:,} $'
        hovertemplate = None

        fig_jobsDemog = go.Figure()

        fig_jobsDemog.add_trace(
            go.Bar(
                x=["<br>".join(textwrap.wrap(label, width=15)) for label in df['characteristics']],
                y=df[var1],
                name="Organismes communautaires à but non lucratif",
                marker=dict(
                    color='#7bafd4'),
                text=df[var1],
                texttemplate=template,
                textposition='outside',
                textfont=dict(
                    size=15,
                    color="black"),
                   hoverinfo="skip"))

        fig_jobsDemog.add_trace(
            go.Bar(
                x=["<br>".join(textwrap.wrap(label, width=15)) for label in df['characteristics']],
                y=df[var2],
                name="institutions commerciales à but non lucratif",
                marker=dict(
                    color='#9ac1dd'),
                text=df[var2],
                texttemplate=template,
                textposition='outside',
                textfont=dict(
                    size=15,
                    color="black"),
                                       hoverinfo="skip"))

        fig_jobsDemog.add_trace(
            go.Bar(
                x=["<br>".join(textwrap.wrap(label, width=15)) for label in df['characteristics']],
                y=df[var3],
                name="Institutions gouvernementales à but non lucratif",
                marker=dict(
                    color='#c8102e'),
                text=df[var3],
                texttemplate=template,
                textposition='outside',
                textfont=dict(
                    size=15,
                    color="black"),
                                       hoverinfo="skip"))

    fig_jobsDemog.update_layout(title=dict(text=title,
                                           xanchor='left',
                                           x=0.02),
                                margin=dict(t=50),
                                yaxis=dict(title="",
                                           showgrid=False,
                                           showticklabels=False),
                                xaxis=dict(title="",
                                           tickfont=dict(size=15)),
                                legend=dict(orientation='h',
                                            xanchor='center',
                                            x=0.5,
                                            y=-0.2,
                                            font=dict(size=15)),
                                paper_bgcolor='rgba(0,0,0,0)',
                                plot_bgcolor='rgba(0,0,0,0)')

    fig_jobsDemog.update_xaxes(showline=True, linewidth=1, linecolor='black')
    fig_jobsDemog.update_yaxes(range=[0, max(pd.concat([df[var1], df[var2], df[var3]], axis=0)) * 1.1])

    return fig_jobsDemog
