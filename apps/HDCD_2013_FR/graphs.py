import pandas as pd
import plotly.graph_objects as go
import numpy as np


def don_rate_avg_don_by_meth(dff1, dff2, name1, name2, title):
    dff1['Text'] = np.select([dff1["Marker"] == "*",
                              dff1["Marker"] == "...",
                              pd.isnull(dff1["Marker"])],
                             [dff1.Estimate.map(str) + "%" + "*",
                              "...",
                              dff1.Estimate.map(str) + "%"])
    dff1['HoverText'] = np.select(
        [
            dff1["Marker"] == "*",
            dff1["Marker"] == "...",
            pd.isnull(
                dff1["Marker"])],
        [
            "Estimate: " +
            dff1.Estimate.map(str) +
            "% ± " +
            (
                dff1["CI Upper"] -
                dff1["Estimate"]).map(str) +
            "%<br><b>À utiliser avec précaution</b>",
            "Estimate Suppressed",
            "Estimate: " +
            dff1.Estimate.map(str) +
            "% ± " +
            (
                dff1["CI Upper"] -
                dff1["Estimate"]).map(str) +
            "%"])
    dff2['Text'] = np.select([dff2["Marker"] == "*",
                              dff2["Marker"] == "...",
                              pd.isnull(dff2["Marker"])],
                             ["$" + dff2.Estimate.map(str) + "*",
                              "...",
                              "$" + dff2.Estimate.map(str)])
    dff2['HoverText'] = np.select(
        [
            dff2["Marker"] == "*",
            dff2["Marker"] == "...",
            pd.isnull(
                dff2["Marker"])],
        [
            "Estimate: $" +
            dff2.Estimate.map(str) +
            " ± $" +
            (
                dff2["CI Upper"] -
                dff2["Estimate"]).map(str) +
            "<br><b>À utiliser avec précaution</b>",
            "Estimate Suppressed",
            "Estimate: $" +
            dff2.Estimate.map(str) +
            " ± $" +
            (
                dff2["CI Upper"] -
                dff2["Estimate"]).map(str)])
    dff1 = dff1[(dff1.Attribute != "Unknown")]
    dff1 = dff1[(dff1.Attribute != "Unable to<br>determine")]
    dff2 = dff2[(dff2.Attribute != "Unknown")]
    dff2 = dff2[(dff2.Attribute != "Unable to<br>determine")]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=dff1['CI Upper'],
            y=dff1['QuestionText'],
            orientation="h",
            error_x=None,
            marker=dict(
                color="#FFFFFF",
                line=dict(
                    color="#FFFFFF")),
            text=None,
            hoverinfo="skip",
            textposition='outside',
            showlegend=False,
            cliponaxis=False,
            xaxis='x2',
            offsetgroup=2),
    )
    fig.add_trace(go.Bar(x=dff2['CI Upper'],
                         y=dff2['QuestionText'],
                         orientation="h",
                         error_x=None,  # need to vectorize subtraction
                         marker=dict(
        color="#FFFFFF", line=dict(
            color="#FFFFFF")),
        text=None,
        hoverinfo="skip",
        textposition='outside',
        showlegend=False,
        cliponaxis=False,
        xaxis='x1',
        offsetgroup=1
    ),
    )

    fig.add_trace(go.Bar(x=dff1['Estimate'],
                         y=dff1['QuestionText'],
                         orientation="h",
                         error_x=None,
                         hovertext=dff1['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#FD7B5F"),
                         text=dff1['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         insidetextanchor=None,
                         name=name1,
                         xaxis='x2',
                         offsetgroup=2
                         ),
                  )
    fig.add_trace(go.Bar(x=dff2['Estimate'],
                         y=dff2['QuestionText'],
                         orientation="h",
                         error_x=None,  # need to vectorize subtraction
                         hovertext=dff2['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         marker=dict(color="#234C66"),
                         text=dff2['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         insidetextanchor=None,
                         name=name2,
                         xaxis='x1',
                         offsetgroup=1
                         ),
                  )

    x2 = go.layout.XAxis(overlaying='x',
                         side='bottom',
                         autorange=False,
                         range=[0, 1.25 * max(dff1["CI Upper"])])
    x1 = go.layout.XAxis(overlaying='x',
                         side='top',
                         autorange=False,
                         range=[0, 1.25 * max(dff2["CI Upper"])])

    fig.update_layout(
        title={
            'text': title,
            'y': 0.95},
        margin={
            'l': 30,
            'b': 30,
            'r': 10,
            't': 30},
        height=600,
        bargroupgap=0.05,
        plot_bgcolor='rgba(0, 0, 0, 0)',
        barmode="group",
        xaxis1=x1,
        xaxis2=x2,
        legend={
                'orientation': 'h',
                'yanchor': "bottom"},
        updatemenus=[
            dict(
                type="buttons",
                xanchor='right',
                x=1.2,
                y=0.5,
                buttons=list(
                    [
                        dict(
                            args=[
                                {
                                    "error_x": [
                                        None,
                                        None,
                                        None,
                                        None],
                                    "text": [
                                        None,
                                        None,
                                        dff1['Text'],
                                        dff2['Text']]}],
                            label="Sans intervalles de confiance",
                            method="restyle"),
                        dict(
                            args=[
                                {
                                    "error_x": [
                                        None,
                                        None,
                                        dict(
                                            type="data",
                                            array=dff1["CI Upper"] - dff1["Estimate"],
                                            color="#424242",
                                            thickness=1.5),
                                        dict(
                                            type="data",
                                            array=dff2["CI Upper"] - dff2["Estimate"],
                                            color="#424242",
                                            thickness=1.5)],
                                    "text": [
                                        dff1['Text'],
                                        dff2['Text'],
                                        None,
                                        None]}],
                            label="Intervalles de confiance",
                            method="restyle")]),
            ),
        ])
    fig.update_xaxes(showgrid=False,
                     showticklabels=False,
                     autorange=False,
                     )
    fig.update_yaxes(
        autorange="reversed", ticklabelposition="outside", tickfont=dict(
            size=12), categoryorder='array', categoryarray=dff1.sort_values(
            by="Estimate", ascending=False)["QuestionText"])

    markers = pd.concat([dff1["Marker"], dff2["Marker"]])
    if markers.isin(["*"]).any() and markers.isin(["..."]).any():
        fig.update_layout(
            margin={
                'l': 30,
                'b': 75,
                'r': 10,
                't': 40},
            annotations=[
                dict(
                    text="<a href='/popup'>De quoi s'agit-il?</a>",
                    xref="paper",
                    yref="paper",
                    xanchor='right',
                    y=0.31,
                    x=1.2,
                    align="left",
                    showarrow=False),
                dict(
                    text="*<i>À utiliser avec précaution<br>Certains résultats sont pas assez fiables pour être affichés</i>",
                    xref="paper",
                    yref="paper",
                    xanchor='right',
                    yanchor="top",
                    y=-0.08,
                    x=1.2,
                    align="right",
                    showarrow=False,
                    font=dict(
                        size=13))])
    elif markers.isin(["*"]).any():
        fig.update_layout(
            margin={
                'l': 30,
                'b': 75,
                'r': 10,
                't': 40},
            annotations=[
                dict(
                    text="<a href='/popup'>De quoi s'agit-il?</a>",
                    xref="paper",
                    yref="paper",
                    xanchor='right',
                    y=0.31,
                    x=1.2,
                    align="left",
                    showarrow=False),
                dict(
                    text="*<i>À utiliser avec précaution</i>",
                    xref="paper",
                    yref="paper",
                    xanchor='right',
                    yanchor="top",
                    y=-0.08,
                    x=1.2,
                    align="right",
                    showarrow=False,
                    font=dict(
                        size=13))])
    elif markers.isin(["..."]).any():
        fig.update_layout(
            margin={
                'l': 30,
                'b': 75,
                'r': 10,
                't': 40},
            annotations=[
                dict(
                    text="<a href='/popup'>De quoi s'agit-il?</a>",
                    xref="paper",
                    yref="paper",
                    xanchor='right',
                    y=0.31,
                    x=1.2,
                    align="left",
                    showarrow=False),
                dict(
                    text="<i>Certains résultats sont pas assez fiables pour être affichés</i>",
                    xref="paper",
                    yref="paper",
                    xanchor='right',
                    yanchor="top",
                    y=-0.08,
                    x=1.2,
                    align="right",
                    showarrow=False,
                    font=dict(
                        size=13))])
    else:
        fig.update_layout(
            margin={
                'l': 30,
                'b': 30,
                'r': 10,
                't': 40},
            annotations=[
                dict(
                    text="<a href='/popup'>De quoi s'agit-il?</a>",
                    xref="paper",
                    yref="paper",
                    xanchor='right',
                    y=0.32,
                    x=1.2,
                    align="left",
                    showarrow=False)])

    return fig


def don_rate_avg_don(dff1, dff2, name1, name2, title):
    dff1['Text'] = np.select([dff1["Marker"] == "*",
                              dff1["Marker"] == "...",
                              pd.isnull(dff1["Marker"])],
                             [dff1.Estimate.map(str) + "%" + "*",
                              "...",
                              dff1.Estimate.map(str) + "%"])
    dff1['HoverText'] = np.select(
        [
            dff1["Marker"] == "*",
            dff1["Marker"] == "...",
            pd.isnull(
                dff1["Marker"])],
        [
            "Estimate: " +
            dff1.Estimate.map(str) +
            "% ± " +
            (
                dff1["CI Upper"] -
                dff1["Estimate"]).map(str) +
            "%<br><b>À utiliser avec précaution</b>",
            "Estimate Suppressed",
            "Estimate: " +
            dff1.Estimate.map(str) +
            "% ± " +
            (
                dff1["CI Upper"] -
                dff1["Estimate"]).map(str) +
            "%"])
    dff2['Text'] = np.select([dff2["Marker"] == "*",
                              dff2["Marker"] == "...",
                              pd.isnull(dff2["Marker"])],
                             ["$" + dff2.Estimate.map(str) + "*",
                              "...",
                              "$" + dff2.Estimate.map(str)])
    dff2['HoverText'] = np.select(
        [
            dff2["Marker"] == "*",
            dff2["Marker"] == "...",
            pd.isnull(
                dff2["Marker"])],
        [
            "Estimate: $" +
            dff2.Estimate.map(str) +
            " ± $" +
            (
                dff2["CI Upper"] -
                dff2["Estimate"]).map(str) +
            "<br><b>À utiliser avec précaution</b>",
            "Estimate Suppressed",
            "Estimate: $" +
            dff2.Estimate.map(str) +
            " ± $" +
            (
                dff2["CI Upper"] -
                dff2["Estimate"]).map(str)])
    dff1 = dff1[(dff1.Attribute != "Unknown") & (
        dff1.Attribute != "Unable to determine")]
    dff2 = dff2[(dff2.Attribute != "Unknown") & (
        dff2.Attribute != "Unable to determine")]

    # Scatter plot - data frame, x label, y label
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=dff1['CI Upper'],
            y=dff1['Attribute'],
            orientation="h",
            error_x=None,
            marker=dict(
                color="#FFFFFF",
                line=dict(
                    color="#FFFFFF")),
            text=None,
            hoverinfo="skip",
            textposition='outside',
            showlegend=False,
            cliponaxis=False,
            xaxis='x2',
            offsetgroup=2),
    )
    fig.add_trace(go.Bar(x=dff2['CI Upper'],
                         y=dff2['Attribute'],
                         orientation="h",
                         error_x=None,  # need to vectorize subtraction
                         marker=dict(
        color="#FFFFFF", line=dict(
            color="#FFFFFF")),
        text=None,
        hoverinfo="skip",
        textposition='outside',
        showlegend=False,
        cliponaxis=False,
        xaxis='x1',
        offsetgroup=1
    ),
    )

    fig.add_trace(go.Bar(x=dff1['Estimate'],
                         y=dff1['Attribute'],
                         orientation="h",
                         error_x=None,
                         hovertext=dff1['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#FD7B5F"),
                         text=dff1['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         insidetextanchor=None,
                         name=name1,
                         xaxis='x2',
                         offsetgroup=2
                         ),
                  )
    fig.add_trace(go.Bar(x=dff2['Estimate'],
                         y=dff2['Attribute'],
                         orientation="h",
                         error_x=None,  # need to vectorize subtraction
                         hovertext=dff2['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         marker=dict(color="#234C66"),
                         text=dff2['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         insidetextanchor=None,
                         name=name2,
                         xaxis='x1',
                         offsetgroup=1
                         ),
                  )

    x2 = go.layout.XAxis(overlaying='x',
                         side='bottom',
                         autorange=False,
                         range=[0, 1.25 * max(dff1["CI Upper"])])
    x1 = go.layout.XAxis(overlaying='x',
                         side='top',
                         autorange=False,
                         range=[0, 1.25 * max(dff2["CI Upper"])])

    fig.update_layout(
        title={
            'text': title,
            'y': 0.95},
        margin={
            'l': 30,
            'b': 30,
            'r': 10,
            't': 30},
        height=400,
        bargroupgap=0.05,
        plot_bgcolor='rgba(0, 0, 0, 0)',
        barmode="group",
        xaxis1=x1,
        xaxis2=x2,
        legend={
                'orientation': 'h',
                'yanchor': "bottom"},
        updatemenus=[
            dict(
                type="buttons",
                xanchor='right',
                x=1.2,
                y=0.5,
                buttons=list(
                    [
                        dict(
                            args=[
                                {
                                    "error_x": [
                                        None,
                                        None,
                                        None,
                                        None],
                                    "text": [
                                        None,
                                        None,
                                        dff1['Text'],
                                        dff2['Text']]}],
                            label="Sans intervalles de confiance",
                            method="restyle"),
                        dict(
                            args=[
                                {
                                    "error_x": [
                                        None,
                                        None,
                                        dict(
                                            type="data",
                                            array=dff1["CI Upper"] - dff1["Estimate"],
                                            color="#424242",
                                            thickness=1.5),
                                        dict(
                                            type="data",
                                            array=dff2["CI Upper"] - dff2["Estimate"],
                                            color="#424242",
                                            thickness=1.5)],
                                    "text": [
                                        dff1['Text'],
                                        dff2['Text'],
                                        None,
                                        None]}],
                            label="Intervalles de confiance",
                            method="restyle")]),
            ),
        ])
    fig.update_xaxes(showgrid=False,
                     showticklabels=False,
                     autorange=False,
                     )
    fig.update_yaxes(autorange="reversed",
                     ticklabelposition="outside",
                     tickfont=dict(size=12))

    markers = pd.concat([dff1["Marker"], dff2["Marker"]])
    if markers.isin(["*"]).any() and markers.isin(["..."]).any():
        fig.update_layout(
            margin={
                'l': 30,
                'b': 75,
                'r': 10,
                't': 40},
            annotations=[
                dict(
                    text="<a href='/popup'>De quoi s'agit-il?</a>",
                    xref="paper",
                    yref="paper",
                    xanchor='right',
                    y=0.19,
                    x=1.2,
                    align="left",
                    showarrow=False),
                dict(
                    text="*<i>À utiliser avec précaution<br>Certains résultats sont pas assez fiables pour être affichés</i>",
                    xref="paper",
                    yref="paper",
                    xanchor='right',
                    yanchor="top",
                    y=-0.11,
                    x=1.2,
                    align="right",
                    showarrow=False,
                    font=dict(
                        size=13))])
    elif markers.isin(["*"]).any():
        fig.update_layout(
            margin={
                'l': 30,
                'b': 75,
                'r': 10,
                't': 40},
            annotations=[
                dict(
                    text="<a href='/popup'>De quoi s'agit-il?</a>",
                    xref="paper",
                    yref="paper",
                    xanchor='right',
                    y=0.19,
                    x=1.2,
                    align="left",
                    showarrow=False),
                dict(
                    text="*<i>À utiliser avec précaution</i>",
                    xref="paper",
                    yref="paper",
                    xanchor='right',
                    yanchor="top",
                    y=-0.11,
                    x=1.2,
                    align="right",
                    showarrow=False,
                    font=dict(
                        size=13))])
    elif markers.isin(["..."]).any():
        fig.update_layout(
            margin={
                'l': 30,
                'b': 75,
                'r': 10,
                't': 40},
            annotations=[
                dict(
                    text="<a href='/popup'>De quoi s'agit-il?</a>",
                    xref="paper",
                    yref="paper",
                    xanchor='right',
                    y=0.19,
                    x=1.2,
                    align="left",
                    showarrow=False),
                dict(
                    text="<i>Certains résultats sont pas assez fiables pour être affichés</i>",
                    xref="paper",
                    yref="paper",
                    xanchor='right',
                    yanchor="top",
                    y=-0.11,
                    x=1.2,
                    align="right",
                    showarrow=False,
                    font=dict(
                        size=13))])
    else:
        fig.update_layout(
            margin={
                'l': 30,
                'b': 30,
                'r': 10,
                't': 40},
            annotations=[
                dict(
                    text="<a href='/popup'>De quoi s'agit-il?</a>",
                    xref="paper",
                    yref="paper",
                    xanchor='right',
                    y=0.22,
                    x=1.2,
                    align="left",
                    showarrow=False)])

    return fig
