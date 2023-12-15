import pandas as pd
import plotly.graph_objects as go
import numpy as np
import os
import os.path as op
import re
from plotly.subplots import make_subplots
from .data_processing import get_data
import textwrap

_, _, _, _, revSource, revGrowthSource = get_data()


def SubSec(df, title):

    df = df.loc[df['subSector'].map({"Organismes communautaires à but non lucratif": 0,
                                     "Institutions communautaires à but non lucratif": 1,
                                     "Institutions gouvernementales à but non lucratif": 2}).sort_values().index]

    fig_SubSec = go.Figure()

    # Sous-secteur de base (red)
    fig_SubSec.add_trace(
        go.Bar(
            x=["<br>".join(textwrap.wrap(label, width=16)) for label in df['subSector']],
            y=np.where(
                df["coreStatus"] == "Sous-secteur de base",
                df['valNormP'],
                np.nan),
            text=[
                str(
                    int(
                        round(
                            df['valNormP'].loc[i] *
                            100,
                            0))) +
                " %" if df.loc[i]["coreStatus"] == "Sous-secteur de base" else '' for i in df.index],
            textposition='outside',
            textfont=dict(
                size=15,
                color="black"),
            marker=dict(
                color='#c8102e'),
            showlegend=True,
            name="Sous-secteur de base",
            hoverinfo='skip'))

    # Gouvernement sub-sector (blue)
    fig_SubSec.add_trace(
        go.Bar(
            x=["<br>".join(textwrap.wrap(label, width=16)) for label in df['subSector']],
            y=np.where(
                df["coreStatus"] == "Gouvernement sub-sector",
                df['valNormP'],
                np.nan),
            text=[
                str(
                    int(
                        round(
                            df['valNormP'].loc[i] *
                            100,
                            0))) +
                " %" if df.loc[i]["coreStatus"] == "Gouvernement sub-sector" else '' for i in df.index],
            textposition='outside',
            textfont=dict(
                size=15,
                color="black"),
            marker=dict(
                color='#7bafd4'),
            showlegend=True,
            name="Gouvernement sub-sector",
            hoverinfo='skip'))

    # Mid-bar text
    for i in df.index:
        fig_SubSec.add_annotation(x="<br>".join(textwrap.wrap(df.loc[i]['subSector'], width=16)),
                                  y=df.loc[i]['valNormP'] / 2,
                                  text=df.loc[i]['label'],
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
                                         y=-0.4,
                                         font=dict(size=15)),
                             paper_bgcolor='rgba(0,0,0,0)',
                             plot_bgcolor='rgba(0,0,0,0)')

    fig_SubSec.update_xaxes(showline=True, linewidth=1, linecolor='black')
    fig_SubSec.update_yaxes(range=[0, max(df['valNormP']) * 1.1])

    return fig_SubSec


def Growth(df, title, trace_settings):
    # TODO: Chck if hovertext needs to be added
    fig_Growth = go.Figure()

    df['refDate'] = pd.to_datetime(df['refDate'])

    for var in trace_settings.keys():
        text_var = "label" + var[8:]
        fig_Growth.add_trace(go.Scatter(x=df['refDate'].dt.year,
                                        y=df[var],
                                        name=trace_settings[var]['name'],
                                        mode='lines',
                                        line=trace_settings[var]['line_dict'],
                                        hovertext = df[text_var],
                                        hovertemplate='%{y:0.2f}'+" / "+'%{hovertext}'))

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
                             hovermode='x unified',
                             paper_bgcolor='rgba(0,0,0,0)',
                             plot_bgcolor='rgba(0,0,0,0)')

    fig_Growth.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#cccccc')

    return fig_Growth


def SubSecActivity(df, title, vars):
    var_1 = vars[0]
    var_2 = vars[1]
    # Set limits based on max/min values
    limitRight = max(pd.concat([df[var_2], df[var_1]])) * 1.15 * 100
    limitLeft = max(max(df[var_2]) * 100 * 0.7, max(df[var_1]) * 100 * 1.15)

    # Sort data in correct order, anchoring "Autre" at the bottom
    df = pd.concat([df[df['activity'] == "Autre"],
                   df[df['activity'] != "Autre"].sort_values(var_1)], axis=0)

    fig_SubSecActivity = make_subplots(rows=1, cols=2, horizontal_spacing=0.01)

    fig_SubSecActivity.add_trace(go.Bar(  # y = ~str_wrap_factor(fct_rev(activity), 28),
        y=df['activity'],
        x=df[var_1] * 100,
        name="Organismes à but non lucratif de base",
        orientation='h',
        marker=dict(color="#c8102e"),
        text=round(df[var_1] * 100, 0).astype(int).map(str) + " %",
        textposition='outside',
        textfont=dict(size=12, color="black"),
        hovertext=df['labelCoreRev'],
        hovertemplate='%{hovertext}'+'<extra>'+'</extra>'), row=1, col=1)

    fig_SubSecActivity.add_trace(go.Bar(  # y = ~str_wrap_factor(fct_rev(activity), 25),
        y=df['activity'],
        x=df[var_2] * 100,
        name="Institutions gouvernementales à but non lucratif",
        orientation='h',
        marker=dict(color="#7BAFD4"),
        text=np.where(
            df[var_2] > 0,
            round(
                df[var_2] *
                100,
                0).astype(int).map(str) +
            " %",
            ""),
        textposition='outside',
        textfont=dict(size=12, color="black"),
        hovertext=df['labelGovtRev'],
        hovertemplate='%{hovertext}' + '<extra>' + '</extra>'), row=1, col=2)

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
                                                 font=dict(size=15)),
                                     paper_bgcolor='rgba(0,0,0,0)',
                                     plot_bgcolor='rgba(0,0,0,0)')

    return fig_SubSecActivity


def Source(df, title):

    fig_revSource = go.Figure()

    fig_revSource.add_trace(
        go.Bar(
            x=["<br>".join(textwrap.wrap(label, width=16)) for label in df['subSector']],
            y=df['perTot_Government'],
            name="Gouvernement",
            text=[
                str(
                    int(
                        round(
                            df['perTot_Government'].loc[i] *
                            100,
                            0))) +
                " %" for i in df.index],
            textposition='inside',
            insidetextanchor='middle',
            textfont=dict(
                size=15,
                color="white"),
            marker=dict(
                color="#50a684"),
            hovertext=df['label_Government'],
            hovertemplate="Gouvernement: %{y:.0%}<br>Valeur: %{hovertext}<extra></extra>"))
    fig_revSource.add_trace(go.Bar(x=["<br>".join(textwrap.wrap(label, width=16)) for label in df['subSector']],
                                   y=df['perTot_CorpDons'],
                                   name="Dons d'entreprises",
                                   text=[str(int(round(df['perTot_CorpDons'].loc[i] * 100, 0))) + " %" if not np.isnan(
                                       df['perTot_CorpDons'].loc[i]) else '' for i in df.index],
                                   textposition='inside',
                                   insidetextanchor='middle',
                                   textfont=dict(color="black"),
                                   # TODO: What is this color?
                                   marker=dict(color="#a8cae3"),
                                   hovertext=df['label_CorpDons'],
                                   hovertemplate="Dons d'entreprises: %{y:.0%}<br>Valeur: %{hovertext}<extra></extra>"
                                   ))
    fig_revSource.add_trace(
        go.Bar(
            x=["<br>".join(textwrap.wrap(label, width=16)) for label in df['subSector']],
            y=df['perTot_HouseDons'],
            name="Dons de ménages",
            text=[
                str(
                    int(
                        round(
                            df['perTot_HouseDons'].loc[i] *
                            100,
                            0))) +
                " %" if not np.isnan(
                    df['perTot_HouseDons'].loc[i]) else '' for i in df.index],
            textposition='inside',
            insidetextanchor='middle',
            textfont=dict(
                color="white"),
            marker=dict(
                color="#7BAFD4"),
            hovertext=df['label_HouseDons'],
            hovertemplate="Dons de ménages & memberships: %{y:.0%}<br>Valeur: %{hovertext}<extra></extra>"))
    fig_revSource.add_trace(go.Bar(x=["<br>".join(textwrap.wrap(label, width=16)) for label in df['subSector']],
                                   y=df['perTot_Investments'],
                                   name="Investissements",
                                   text=[str(int(round(df['perTot_Investments'].loc[i] * 100, 0))) + " %" if not np.isnan(
                                       df['perTot_Investments'].loc[i]) else '' for i in df.index],
                                   textposition='inside',
                                   insidetextanchor='middle',
                                   textfont=dict(color="black"),
                                   # TODO: What is this color?
                                   marker=dict(color="#eca7ad"),
                                   hovertext=df['label_Investments'],
                                   hovertemplate="Investissements: %{y:.0%}<br>Valeur: %{hovertext}<extra></extra>"
                                   ))
    fig_revSource.add_trace(go.Bar(x=["<br>".join(textwrap.wrap(label, width=16)) for label in df['subSector']],
                                   y=df['perTot_Membership'],
                                   name="Frais d'adhésion commerciaux",
                                   text=[str(int(round(df['perTot_Membership'].loc[i] * 100, 0))) + " %" if not np.isnan(
                                       df['perTot_Membership'].loc[i]) else '' for i in df.index],
                                   textposition='inside',
                                   insidetextanchor='middle',
                                   textfont=dict(color="white"),
                                   # TODO: What is this color?
                                   marker=dict(color="#e06d78"),
                                   hovertext=df['label_Membership'],
                                   hovertemplate="Frais d'adhésion commerciaux: %{y:.0%}<br>Valeur: %{hovertext}<extra></extra>"
                                   ))
    fig_revSource.add_trace(
        go.Bar(
            x=["<br>".join(textwrap.wrap(label, width=16)) for label in df['subSector']],
            y=df['perTot_Goods'],
            name="Biens et services",
            text=[
                str(
                    int(
                        round(
                            df['perTot_Goods'].loc[i] *
                            100,
                            0))) +
                " %" if not np.isnan(
                    df['perTot_Goods'].loc[i]) else '' for i in df.index],
            textposition='inside',
            insidetextanchor='middle',
            textfont=dict(
                color="white"),
            marker=dict(
                color="#c8102e"),
            hovertext=df['label_Goods'],
            hovertemplate="Biens et services: %{y:.0%}<br>Valeur: %{hovertext}<extra></extra>"))
    fig_revSource.update_layout(barmode='stack',
                                title=dict(text=title,
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
                                            y=-0.4,
                                            font=dict(size=15)),
                                hoverlabel=dict(align='right'),
                                 paper_bgcolor='rgba(0,0,0,0)',
                                 plot_bgcolor='rgba(0,0,0,0)')

    fig_revSource.update_xaxes(showline=True, linewidth=1, linecolor='black')

    return fig_revSource


def GrowthSource(df, title):

    fig_revGrowthSource = make_subplots(rows=3, cols=1)

    filters = [
        'Organismes communautaires à but non lucratif',
        "Institutions communautaires à but non lucratif",
        "Institutions gouvernementales à but non lucratif"]
    text_y = [1.015, 0.575, 0.25]

    for i in range(len(filters)):
        this_df = df[df['subSector'] == filters[i]]
        if i > 0:
            legend_status = False
        else:
            legend_status = True
        fig_revGrowthSource.add_trace(
            go.Scatter(
                x=this_df['refDate'].dt.year,
                y=this_df['valNormP_Government'],
                name="Gouvernement",
                mode='lines',
                line=dict(
                    color="#50a684",
                    dash="solid"),
                text=this_df['label_Government'],
                hovertemplate='%{y:0.2f}' +
                " / %{text}",
                showlegend=legend_status),
            row=i +
            1,
            col=1)

        fig_revGrowthSource.add_trace(go.Scatter(x=this_df['refDate'].dt.year,
                                                 y=this_df['valNormP_CorpDons'],
                                                 name="Dons d'entreprises",
                                                 mode='lines',
                                                 line=dict(color="#a8cae3",  # TODO: What is this color?
                                                           dash="dot"),
                                                 text=this_df['label_CorpDons'],
                                                 hovertemplate='%{y:0.2f}' + \
                                                 " / %{text}",
                                                 showlegend=legend_status),
                                      row=i + 1, col=1)
        if i < 2:
            fig_revGrowthSource.add_trace(
                go.Scatter(
                    x=this_df['refDate'].dt.year,
                    y=this_df['valNormP_Households'],
                    name="Dons de ménages & fees",
                    mode='lines',
                    line=dict(
                        color="#7BAFD4",
                        dash="solid"),
                    text=this_df['label_Households'],
                    hovertemplate='%{y:0.2f}' + " / %{text}",
                    showlegend=legend_status),
                row=i + 1,
                col=1)
        else:
            fig_revGrowthSource.add_trace(
                go.Scatter(
                    x=this_df['refDate'].dt.year,
                    y=this_df['valNormP_HouseDons'],
                    name="Dons de ménages",
                    mode='lines',
                    line=dict(
                        color="#7BAFD4",
                        dash="solid"),
                    text=this_df['label_HouseDons'],
                    hovertemplate='%{y:0.2f}' +
                    " / %{text}",
                    showlegend=legend_status),
                row=i +
                1,
                col=1)
        fig_revGrowthSource.add_trace(go.Scatter(x=this_df['refDate'].dt.year,
                                                 y=this_df['valNormP_Investments'],
                                                 name="Investissements",
                                                 mode='lines',
                                                 line=dict(color="#eca7ad",  # TODO: What is this color?
                                                           dash="dot"),
                                                 text=this_df['label_Investments'],
                                                 hovertemplate='%{y:0.2f}' + \
                                                 " / %{text}",
                                                 showlegend=legend_status),
                                      row=i + 1, col=1)

        fig_revGrowthSource.add_trace(go.Scatter(x=this_df['refDate'].dt.year,
                                                 y=this_df['valNormP_Membership'],
                                                 name="Frais d'adhésion",
                                                 mode='lines',
                                                 line=dict(color="#e06d78",  # TODO: What is this color?
                                                           dash="dash"),
                                                 text=this_df['label_Membership'],
                                                 hovertemplate='%{y:0.2f}' + \
                                                 " / %{text}",
                                                 showlegend=legend_status),
                                      row=i + 1, col=1)

        fig_revGrowthSource.add_trace(
            go.Scatter(
                x=this_df['refDate'].dt.year,
                y=this_df['valNormP_Goods'],
                name="Biens et services",
                mode='lines',
                line=dict(
                    color="#c8102e",
                    dash="solid"),
                text=this_df['label_Goods'],
                hovertemplate='%{y:0.2f}' +
                " / %{text}",
                showlegend=legend_status),
            row=i +
            1,
            col=1)

        fig_revGrowthSource.add_annotation(x=0,
                                           y=text_y[i],
                                           text=filters[i],
                                           xref='paper',
                                           yref='paper',
                                           xanchor='left',
                                           showarrow=False)

        fig_revGrowthSource.update_xaxes(
            title="", showgrid=False, dtick=1, tickfont=dict(
                size=12), row=i + 1, col=1)

        fig_revGrowthSource.update_yaxes(title="",
                                         tickformat='.2f',
                                         nticks=4, showgrid=True, gridwidth=1, gridcolor='#cccccc',
                                         # griddash = 'dot',
                                         row=i + 1, col=1)

    fig_revGrowthSource.update_layout(title=dict(text=title,
                                                 xanchor='left',
                                                 x=0.02),
                                      margin=dict(t=50),
                                      legend=dict(orientation='h',
                                                  xanchor='center',
                                                  x=0.5,
                                                  y=-0.05,
                                                  font=dict(size=15),
                                                  traceorder='reversed'),
                                      hoverlabel=dict(align='right'),
                                      hovermode='x',
                                     paper_bgcolor='rgba(0,0,0,0)',
                                     plot_bgcolor='rgba(0,0,0,0)'
                                      )
    return fig_revGrowthSource


def build_fig_revsouce_CA(df):
    fig_revSource_CA = go.Figure()

    fig_revSource_CA.add_trace(
        go.Bar(
            x=df['subSector'],
            y=df['perTot_Government'],
            name="Gouvernement",
            text=[
                str(
                    int(
                        round(
                            df['perTot_Government'].loc[i] *
                            100,
                            0))) +
                " %" for i in df.index],
            textposition='inside',
            insidetextanchor='middle',
            textfont=dict(
                size=15,
                color="white"),
            marker=dict(
                color="#50a684"),
            hovertext=df['label_Government'],
            hovertemplate="Gouvernement: %{y:.0%}<br>Valeur: %{hovertext}<extra></extra>"))
    fig_revSource_CA.add_trace(go.Bar(x=df['subSector'],
                                      y=df['perTot_CorpDons'],
                                      name="Dons d'entreprises",
                                      text=[str(int(round(df['perTot_CorpDons'].loc[i] * 100, 0))) + " %" if not np.isnan(
                                          df['perTot_CorpDons'].loc[i]) else '' for i in df.index],
                                      textposition='inside',
                                      insidetextanchor='middle',
                                      textfont=dict(color="black"),
                                      marker=dict(
        color="#a8cae3"),  # TODO: What is this color?
        hovertext=df['label_CorpDons'],
        hovertemplate="Dons d'entreprises: %{y:.0%}<br>Valeur: %{hovertext}<extra></extra>"
    ))
    fig_revSource_CA.add_trace(
        go.Bar(
            x=df['subSector'],
            y=df['perTot_HouseDons'],
            name="Dons de ménages",
            text=[
                str(
                    int(
                        round(
                            df['perTot_HouseDons'].loc[i] *
                            100,
                            0))) +
                " %" if not np.isnan(
                    df['perTot_HouseDons'].loc[i]) else '' for i in df.index],
            textposition='inside',
            insidetextanchor='middle',
            textfont=dict(
                color="white"),
            marker=dict(
                color="#7BAFD4"),
            hovertext=df['label_HouseDons'],
            hovertemplate="Dons de ménages: %{y:.0%}<br>Valeur: %{hovertext}<extra></extra>"))
    fig_revSource_CA.add_trace(go.Bar(x=df['subSector'],
                                      y=df['perTot_Investments'],
                                      name="Investissements",
                                      text=[str(int(round(df['perTot_Investments'].loc[i] * 100, 0))) + " %" if not np.isnan(
                                          df['perTot_Investments'].loc[i]) else '' for i in df.index],
                                      textposition='inside',
                                      insidetextanchor='middle',
                                      textfont=dict(color="black"),
                                      marker=dict(
        color="#eca7ad"),  # TODO: What is this color?
        hovertext=df['label_Investments'],
        hovertemplate="Investissements: %{y:.0%}<br>Valeur: %{hovertext}<extra></extra>"
    ))
    fig_revSource_CA.add_trace(go.Bar(x=df['subSector'],
                                      y=df['perTot_Membership'],
                                      name="Frais d'adhésion",
                                      text=[str(int(round(df['perTot_Membership'].loc[i] * 100, 0))) + " %" if not np.isnan(
                                          df['perTot_Membership'].loc[i]) else '' for i in df.index],
                                      textposition='inside',
                                      insidetextanchor='middle',
                                      textfont=dict(color="white"),
                                      marker=dict(
        color="#e06d78"),  # TODO: What is this color?
        hovertext=df['label_Membership'],
        hovertemplate="Frais d'adhésion: %{y:.0%}<br>Valeur: %{hovertext}<extra></extra>"
    ))
    fig_revSource_CA.add_trace(
        go.Bar(
            x=df['subSector'],
            y=df['perTot_Goods'],
            name="Biens et services",
            text=[
                str(
                    int(
                        round(
                            df['perTot_Goods'].loc[i] *
                            100,
                            0))) +
                " %" if not np.isnan(
                    df['perTot_Goods'].loc[i]) else '' for i in df.index],
            textposition='inside',
            insidetextanchor='middle',
            textfont=dict(
                color="white"),
            marker=dict(
                color="#c8102e"),
            hovertext=df['label_Goods'],
            hovertemplate="Biens et services: %{y:.0%}<br>Valeur: %{hovertext}<extra></extra>"))
    fig_revSource_CA.update_layout(
        barmode='stack',
        title=dict(
            text="Revenues by source and sub-sector, 2021 - CA<br>" +
            '<sup>' +
            " Remarque : placer le curseur sur la barre pour connaître le nombre absolu d'employés." +
            '</sup>',
            xanchor='left',
            x=0.02),
        margin=dict(
            t=50),
        yaxis=dict(
            title="",
            showgrid=False,
            showticklabels=False),
        xaxis=dict(
            title="",
            tickfont=dict(
                size=15)),
        legend=dict(
            orientation='h',
            xanchor='center',
            x=0.5,
            y=-
            0.1,
            font=dict(
                size=15)),
        hoverlabel=dict(
            align='right'),
             paper_bgcolor='rgba(0,0,0,0)',
             plot_bgcolor='rgba(0,0,0,0)')

    return fig_revSource_CA


revsource_df = revSource[revSource['geo'] == 'CA']
fig_revSource_CA = build_fig_revsouce_CA(revsource_df)


def build_fig_revGrowthSource(df):
    fig_revGrowthSource = make_subplots(rows=3, cols=1)

    filters = [
        'Organismes communautaires à but non lucratif',
        "Institutions communautaires à but non lucratif",
        "Institutions gouvernementales à but non lucratif"]
    text_y = [1.015, 0.575, 0.25]

    for i in range(len(filters)):
        this_df = df[df['subSector'] == filters[i]]
        if i > 0:
            legend_status = False
        else:
            legend_status = True

        this_df['refDate'] = pd.to_datetime(this_df['refDate'])
        fig_revGrowthSource.add_trace(
            go.Scatter(
                x=this_df['refDate'].dt.year,
                y=this_df['valNormP_Government'],
                name="Gouvernement",
                mode='lines',
                line=dict(
                    color="#50a684",
                    dash="solid"),
                text=this_df['label_Government'],
                hovertemplate='%{y:0.2f}' +
                " / %{text}",
                showlegend=legend_status),
            row=i +
            1,
            col=1)

        fig_revGrowthSource.add_trace(go.Scatter(x=this_df['refDate'].dt.year,
                                                 y=this_df['valNormP_CorpDons'],
                                                 name="Dons d'entreprises",
                                                 mode='lines',
                                                 line=dict(color="#a8cae3",  # TODO: What is this color?
                                                           dash="dot"),
                                                 text=this_df['label_CorpDons'],
                                                 hovertemplate='%{y:0.2f}' + \
                                                 " / %{text}",
                                                 showlegend=legend_status),
                                      row=i + 1, col=1)

        if i != 1:
            fig_revGrowthSource.add_trace(
                go.Scatter(
                    x=this_df['refDate'].dt.year,
                    y=this_df['valNormP_HouseDons'],
                    name="Dons de ménages",
                    mode='lines',
                    line=dict(
                        color="#7BAFD4",
                        dash="solid"),
                    text=this_df['label_HouseDons'],
                    hovertemplate='%{y:0.2f}' +
                    " / %{text}",
                    showlegend=legend_status),
                row=i +
                1,
                col=1)
        # TODO: This is translated directly from R code; should it be like this
        # though?
        else:
            fig_revGrowthSource.add_trace(
                go.Scatter(
                    x=this_df['refDate'].dt.year,
                    y=this_df['valNormP_Households'],
                    name="Dons de ménages & fees",
                    mode='lines',
                    line=dict(
                        color="#7BAFD4",
                        dash="solid"),
                    text=this_df['label_Households'],
                    hovertemplate='%{y:0.2f}' + " / %{text}",
                    showlegend=legend_status),
                row=i + 1,
                col=1)

        fig_revGrowthSource.add_trace(go.Scatter(x=this_df['refDate'].dt.year,
                                                 y=this_df['valNormP_Investments'],
                                                 name="Investissements",
                                                 mode='lines',
                                                 line=dict(color="#eca7ad",  # TODO: What is this color?
                                                           dash="dot"),
                                                 text=this_df['label_Investments'],
                                                 hovertemplate='%{y:0.2f}' + \
                                                 " / %{text}",
                                                 showlegend=legend_status),
                                      row=i + 1, col=1)

        fig_revGrowthSource.add_trace(go.Scatter(x=this_df['refDate'].dt.year,
                                                 y=this_df['valNormP_Membership'],
                                                 name="Frais d'adhésion",
                                                 mode='lines',
                                                 line=dict(color="#e06d78",  # TODO: What is this color?
                                                           dash="dash"),
                                                 text=this_df['label_Membership'],
                                                 hovertemplate='%{y:0.2f}' + \
                                                 " / %{text}",
                                                 showlegend=legend_status),
                                      row=i + 1, col=1)

        fig_revGrowthSource.add_trace(
            go.Scatter(
                x=this_df['refDate'].dt.year,
                y=this_df['valNormP_Goods'],
                name="Biens et services",
                mode='lines',
                line=dict(
                    color="#c8102e",
                    dash="solid"),
                text=this_df['label_Goods'],
                hovertemplate='%{y:0.2f}' +
                " / %{text}",
                showlegend=legend_status),
            row=i +
            1,
            col=1)

        fig_revGrowthSource.add_annotation(x=0,
                                           y=text_y[i],
                                           text=filters[i],
                                           xref='paper',
                                           yref='paper',
                                           xanchor='left',
                                           showarrow=False)

        fig_revGrowthSource.update_xaxes(
            title="", showgrid=False, dtick=1, tickfont=dict(
                size=12), row=i + 1, col=1)

        fig_revGrowthSource.update_yaxes(title="",
                                         tickformat='.2f',
                                         nticks=4, showgrid=True, gridwidth=1, gridcolor='#cccccc',
                                         # griddash = 'dot',
                                         row=i + 1, col=1)

    revGrowthSource['refDate'] = pd.to_datetime(revGrowthSource['refDate'])
    fig_revGrowthSource.update_layout(title=dict(text="Croissance relative des sources de revenu par sous-secteur, " +
                                                 str(min(revGrowthSource['refDate'].dt.year)) +
                                                 " to " +
                                                 str(max(revGrowthSource['refDate'].dt.year)) +
                                                 " - CA (" +
                                                 str(min(revGrowthSource['refDate'].dt.year)) +
                                                 " = 1.0)" +
                                                 '<br>' +
                                                 '<sup>' +
                                                 " Remarque : placer le curseur sur la ligne pour connaître les valeurs absolues." +
                                                 '</sup>', xanchor='left', x=0.02), margin=dict(t=50), legend=dict(orientation='h', xanchor='center', x=0.5, y=-
                                                                                                                   0.05, font=dict(size=15), traceorder='reversed'), hoverlabel=dict(align='right'), hovermode='x',
                                        paper_bgcolor='rgba(0,0,0,0)',
                                        plot_bgcolor='rgba(0,0,0,0)')

    return fig_revGrowthSource


revGrowthSource_df = revGrowthSource[revGrowthSource['geo'] == 'CA']
fig_revGrowthSource = build_fig_revGrowthSource(revGrowthSource_df)
