import pandas as pd
import plotly.graph_objects as go
import numpy as np
import os
import os.path as op


def static_graph(VolRate_2018, AvgTotHours_2018):

    fig1df1 = VolRate_2018[VolRate_2018['Group'] == "All"]
    fig1df1 = fig1df1[fig1df1.Province.notnull()]

    fig1df2 = AvgTotHours_2018[AvgTotHours_2018['Group'] == "All"]
    fig1df2 = fig1df2[fig1df2.Province.notnull()]

    fig1df1['Text'] = np.select([fig1df1["Marker"] == "*",
                                 fig1df1["Marker"] == "...",
                                 pd.isnull(fig1df1["Marker"])],
                                [fig1df1.Estimate.map(str) + "%" + "*",
                                 "...",
                                 fig1df1.Estimate.map(str) + "%"])
    fig1df1['HoverText'] = np.select(
        [
            fig1df1["Marker"] == "*",
            fig1df1["Marker"] == "...",
            pd.isnull(
                fig1df1["Marker"])],
        [
            "Estimate: " +
            fig1df1.Estimate.map(str) +
            "% ± " +
            (
                fig1df1["CI Upper"] -
                fig1df1["Estimate"]).map(str) +
            "%<br><b>À utiliser avec précaution</b>",
            "Estimate Suppressed",
            "Estimate: " +
            fig1df1.Estimate.map(str) +
            "% ± " +
            (
                fig1df1["CI Upper"] -
                fig1df1["Estimate"]).map(str) +
            "%"])

    fig1df2['Text'] = np.select([fig1df2["Marker"] == "*",
                                 fig1df2["Marker"] == "...",
                                 pd.isnull(fig1df2["Marker"])],
                                ["$" + fig1df2.Estimate.map(str) + "*",
                                 "...",
                                 "$" + fig1df2.Estimate.map(str)])

    fig1df2text_list = []
    for i in list(fig1df2['Text']):
        x = i[1:]
        fig1df2text_list.append(x)

    fig1df2['HoverText'] = np.select(
        [
            fig1df2["Marker"] == "*",
            fig1df2["Marker"] == "...",
            pd.isnull(
                fig1df2["Marker"])],
        [
            "Estimate: $" +
            fig1df2.Estimate.map(str) +
            " ± $" +
            (
                fig1df2["CI Upper"] -
                fig1df2["Estimate"]).map(str) +
            "<br><b>À utiliser avec précaution</b>",
            "Estimate Suppressed",
            "Estimate: $" +
            fig1df2.Estimate.map(str) +
            " ± $" +
            (
                fig1df2["CI Upper"] -
                fig1df2["Estimate"]).map(str)])

    fig1 = go.Figure()

    fig1.add_trace(
        go.Bar(
            x=fig1df2['Province'],
            y=fig1df2['CI Upper'],
            marker=dict(
                color="#FFFFFF",
                line=dict(
                    color="#FFFFFF")),
            text=None,
            textposition='outside',
            showlegend=False,
            hoverinfo="skip",
            cliponaxis=False,
            offsetgroup=1,
        ),
    )

    fig1.add_trace(
        go.Bar(
            x=fig1df1['Province'],
            y=fig1df1['CI Upper'],
            marker=dict(
                color="#FFFFFF",
                line=dict(
                    color="#FFFFFF")),
            text=None,
            textposition='outside',
            hoverinfo="skip",
            showlegend=False,
            name="Taux de bénévolat",
            yaxis='y2',
            offsetgroup=2,
        ),
    )

    fig1.add_trace(go.Bar(x=fig1df2['Province'],
                          y=fig1df2['Estimate'],
                          error_y=None,  # need to vectorize subtraction
                          hovertext=fig1df2['HoverText'],
                          hovertemplate="%{hovertext}",
                          hoverlabel=dict(font=dict(color="white")),
                          hoverinfo="text",
                          marker=dict(color="#234C66"),
                          text=fig1df2text_list,  # fig1df2_text,
                          textposition='outside',
                          cliponaxis=False,
                          name="Nombre d'heures moyen",
                          offsetgroup=1
                          ),
                   )

    fig1.add_trace(go.Bar(x=fig1df1['Province'],
                          y=fig1df1['Estimate'],
                          error_y=None,
                          hovertext=fig1df1['HoverText'],
                          hovertemplate="%{hovertext}",
                          hoverlabel=dict(font=dict(color="white")),
                          hoverinfo="text",
                          marker=dict(color="#FD7B5F"),
                          text=fig1df1['Text'],
                          textposition='outside',
                          cliponaxis=False,
                          name="Taux de bénévolat",
                          yaxis='y2',
                          offsetgroup=2
                          ),
                   )

    y1 = go.layout.YAxis(overlaying='y', side='left', range=[
                         0, 1.25 * max(fig1df2["CI Upper"])])
    y2 = go.layout.YAxis(overlaying='y', side='right', range=[
                         0, 1.25 * max(fig1df1["CI Upper"])])

    fig1.update_layout(
        title={
            'text': "Taux de bénévolat et nombre moyen d’heures de bénévolat par province",
            'y': 0.99},
        margin={
            'l': 30,
            'b': 30,
            'r': 10,
            't': 10},
        plot_bgcolor='rgba(0, 0, 0, 0)',
        barmode="group",
        yaxis1=y1,
        yaxis2=y2,
        legend={
                'orientation': 'h',
                'yanchor': "bottom",
                'xanchor': 'center',
                'x': 0.5,
                'y': -0.15,
                'traceorder': 'reversed'},
        height=400,
        updatemenus=[
            dict(
                type="buttons",
                xanchor='right',
                x=1.4,
                y=0.5,
                buttons=list(
                    [
                        dict(
                            args=[
                                {
                                    "error_y": [
                                        None,
                                        None,
                                        None,
                                        None],
                                    "text": [
                                        None,
                                        None,
                                        fig1df2['Text'],
                                        fig1df1['Text']],
                                }],
                            label="Sans intervalles de confiance",
                            method="restyle"),
                        dict(
                            args=[
                                {
                                    "error_y": [
                                        None,
                                        None,
                                        dict(
                                            type="data",
                                            array=fig1df2["CI Upper"] - fig1df2["Estimate"],
                                            color="#424242",
                                            thickness=1.5),
                                        dict(
                                            type="data",
                                            array=fig1df1["CI Upper"] - fig1df1["Estimate"],
                                            color="#424242",
                                            thickness=1.5)],
                                    "text": [
                                        fig1df2['Text'],
                                        fig1df1['Text'],
                                        None,
                                        None],
                                }],
                            label="Intervalles de confiance",
                            method="restyle")]),
            ),
        ])

    # Aesthetics for fig
    fig1.update_xaxes(autorange="reversed", tickfont=dict(size=12))
    fig1.update_yaxes(showgrid=False,
                      showticklabels=False,
                      autorange=False)

    markers = pd.concat([fig1df1["Marker"], fig1df2["Marker"]])
    if markers.isin(["*"]).any() and markers.isin(["..."]).any():
        fig1.update_layout(
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
                    x=1.4,
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
        fig1.update_layout(
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
                    x=1.4,
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
        fig1.update_layout(
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
                    x=1.4,
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
        fig1.update_layout(
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
                    y=0.21,
                    x=1.4,
                    align="left",
                    showarrow=False)])

    return fig1


def forms_of_giving(dff, title):
    dff['Text'] = np.select([dff["Marker"] == "*",
                             dff["Marker"] == "...",
                             pd.isnull(dff["Marker"])],
                            [dff.Estimate.map(str) + "%" + "*",
                             "...",
                             dff.Estimate.map(str) + "%"])
    dff['HoverText'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])], ["Estimate: " +
                                                                                                            dff.Estimate.map(str) +
                                                                                                            "% ± " +
                                                                                                            (dff["CI Upper"] -
                                                                                                             dff["Estimate"]).map(str) +
                                                                                                            "%<br><b>À utiliser avec précaution</b>", "Estimate Suppressed", "Estimate: " +
                                                                                                            dff.Estimate.map(str) +
                                                                                                            "% ± " +
                                                                                                            (dff["CI Upper"] -
                                                                                                                dff["Estimate"]).map(str) +
                                                                                                            "%"])

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            y=dff['CI Upper'],
            x=dff['QuestionText'],
            marker=dict(
                color="#FFFFFF",
                line=dict(
                    color="#FFFFFF")),
            text=None,
            textposition='outside',
            hoverinfo="skip",
            showlegend=False,
            offsetgroup=1))

    fig.add_trace(go.Bar(y=dff['Estimate'],
                         x=dff['QuestionText'],
                         error_y=None,  # need to vectorize subtraction
                         marker=dict(color="#FD7B5F"),
                         name="Forms of giving",
                         hovertext=dff['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         text=dff['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         showlegend=False,
                         offsetgroup=1
                         )
                  )

    fig.update_layout(
        title={
            'text': title,
            'y': 0.99},
        margin={
            'l': 30,
            'b': 30,
            'r': 10,
            't': 10},
        height=400,
        plot_bgcolor='rgba(0, 0, 0, 0)',
        updatemenus=[
            dict(
                type="buttons",
                xanchor='right',
                x=1.4,
                y=0.5,
                buttons=list(
                        [
                            dict(
                                args=[
                                    {
                                        "error_y": [
                                            None,
                                            None],
                                        "text": [
                                            None,
                                            dff['Text']]}],
                                label="Sans intervalles de confiance",
                                method="restyle"),
                            dict(
                                args=[
                                    {
                                        "error_y": [
                                            None,
                                            dict(
                                                type="data",
                                                array=dff["CI Upper"] - dff["Estimate"],
                                                color="#424242",
                                                thickness=1.5)],
                                        "text": [
                                            dff['Text'],
                                            None]}],
                                label="Intervalles de confiance",
                                method="restyle")]),
            ),
        ])

    # Aesthetics for fig
    fig.update_yaxes(showticklabels=False,
                     autorange=False,
                     range=[0, 1.1 * max(dff["CI Upper"])])
    fig.update_xaxes(showgrid=False, tickfont=dict(size=12))

    markers = dff["Marker"]
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
                    x=1.4,
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
                    x=1.4,
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
                    x=1.4,
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
                    y=0.23,
                    x=1.4,
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
    dff2['Text'] = np.select([dff2["Marker"] == "*", dff2["Marker"] == "...", pd.isnull(
        dff2["Marker"])], [+dff2.Estimate.map(str) + "*", "...", +dff2.Estimate.map(str)])
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
            'y': 0.966},
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


def perc_don_perc_amt(dff1, dff2, name1, name2, title):
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
                             [dff2.Estimate.map(str) + "%" + "*",
                              "...",
                              dff2.Estimate.map(str) + "%"])
    dff2['HoverText'] = np.select(
        [
            dff2["Marker"] == "*",
            dff2["Marker"] == "...",
            pd.isnull(
                dff2["Marker"])],
        [
            "Estimate: " +
            dff2.Estimate.map(str) +
            "% ± " +
            (
                dff2["CI Upper"] -
                dff2["Estimate"]).map(str) +
            "%<br><b>À utiliser avec précaution</b>",
            "Estimate Suppressed",
            "Estimate: " +
            dff2.Estimate.map(str) +
            "% ± " +
            (
                dff2["CI Upper"] -
                dff2["Estimate"]).map(str) +
            "%"])
    dff1 = dff1[(dff1.Attribute != "Not in labour force")]
    # & (dff1.Attribute != "Unknown")]
    dff2 = dff2[(dff2.Attribute != "Not in labour force")]
    # & (dff2.Attribute != "Unknown")]

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
            showlegend=False,
            hoverinfo="skip",
            text=None,
            textposition="outside",
            cliponaxis=False,
            offsetgroup=2),
    )

    fig.add_trace(go.Bar(x=dff2['CI Upper'],
                         y=dff2['Attribute'],
                         orientation="h",
                         error_x=None,  # need to vectorize subtraction
                         marker=dict(
        color="#FFFFFF", line=dict(
            color="#FFFFFF")),
        showlegend=False,
        hoverinfo="skip",
        text=None,
        textposition="outside",
        cliponaxis=False,
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
                         name=name1,
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
                         hoverinfo="text",
                         marker=dict(color="#234C66"),
                         text=dff2['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         name=name2,
                         offsetgroup=1
                         ),
                  )

    fig.update_layout(
        title={
            'text': title,
            'y': 0.967},
        margin={
            'l': 30,
            'b': 30,
            'r': 10,
            't': 10},
        height=400,
        plot_bgcolor='rgba(0, 0, 0, 0)',
        bargroupgap=0.05,
        barmode="group",
        legend={
                'orientation': 'h',
                'yanchor': "middle"},
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

    # Aesthetics for fig
    fig.update_xaxes(showgrid=False, showticklabels=False, autorange=False, range=[
                     0, 1.25 * max(np.concatenate([dff1["CI Upper"], dff2["CI Upper"]]))])
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
                    y=0.21,
                    x=1.2,
                    align="left",
                    showarrow=False)])

    return fig
