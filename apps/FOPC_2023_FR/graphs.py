import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import textwrap

# Example code
# def ExampleGraph(dff1, dff2, name1, name2, title, vol=False):
#     # Graph code here
#     return Graph

def FutureOptimism(df, title, var):

    title = "<br>".join(textwrap.wrap(title, width=70))

    df = df.loc[df['busChar'].map({"Community nonprofits": 3, "Business nonprofits": 2, "Government agencies": 1, "Businesses": 0}).sort_values().index]


    fig_FutureOptimism = go.Figure()

    fig_FutureOptimism.add_trace(go.Scatter(x=[0] * len(df[var]),
                                            y=["<br>".join(textwrap.wrap(col, width=25)) for col in df[var]],
                                            showlegend=False,
                                            mode="lines",
                                            line=dict(color="#000000",
                                                      width=0.5),
                                            hoverinfo="skip"),
                                 )

    fig_FutureOptimism.add_trace(go.Bar(y=["<br>".join(textwrap.wrap(col, width=25)) for col in df[var]],
                                        x=df['S_pessimistic'],
                                        name="Somewhat pessimistic",
                                        marker=dict(color="#50a684"),
                                        legendrank=2,
                                        text=df['S_pessimistic']*-100,
                                        texttemplate="%{text:.0f} %",
                                        textposition='inside',
                                        insidetextanchor='middle',
                                        meta=df['S_pessimisticStat'],
                                        hovertemplate="%{text:.1f} %"+"<br>Qualité de données : "+"%{meta}",
                                        orientation='h'))

    fig_FutureOptimism.add_trace(go.Bar(y=["<br>".join(textwrap.wrap(col, width=25)) for col in df[var]],
                                        x=df['V_pessimistic'],
                                        name="Very pessimistic",
                                        marker=dict(color="#75787b"),
                                        legendrank=1,
                                        text=df['V_pessimistic']*-100,
                                        texttemplate="%{text:.0f} %",
                                        textposition='inside',
                                        insidetextanchor='middle',
                                        meta=df['V_pessimisticStat'],
                                        hovertemplate="%{text:.1f} %"+"<br>Qualité de données : "+"%{meta}",
                                        orientation='h'))

    fig_FutureOptimism.add_trace(go.Bar(y=["<br>".join(textwrap.wrap(col, width=25)) for col in df[var]],
                                        x=df['S_optimistic'],
                                        name="Somewhat optimistic",
                                        marker=dict(color="#7bafd4"),
                                        legendrank=3,
                                        text=df['S_optimistic']*100,
                                        texttemplate="%{text:.0f} %",
                                        textposition='inside',
                                        insidetextanchor='middle',
                                        meta=df['S_optimisticStat'],
                                        hovertemplate="%{text:.1f} %"+"<br>Qualité de données : "+"%{meta}",
                                        orientation='h'))

    fig_FutureOptimism.add_trace(go.Bar(y=["<br>".join(textwrap.wrap(col, width=25)) for col in df[var]],
                                        x=df['V_optimistic'],
                                        name="Very optimistic",
                                        marker=dict(color="#c8102e"),
                                        legendrank=4,
                                        text=df['V_optimistic']*100,
                                        texttemplate="%{text:.0f} %",
                                        textposition='inside',
                                        insidetextanchor='middle',
                                        meta=df['V_optimisticStat'],
                                        hovertemplate="%{text:.1f} %"+"<br>Qualité de données : "+"%{meta}",
                                        orientation='h'))

    fig_FutureOptimism.add_trace(go.Scatter(y=["<br>".join(textwrap.wrap(col, width=25)) for col in df[var]],
                                            x=df['pessimistic'],
                                            mode='markers+text',
                                            showlegend=False,
                                            name="Pessimistic",
                                            # marker=dict(color="#75787b00", size=0),
                                            marker=dict(color="#75787b", size=0, opacity=0),
                                            text=df['pessimistic'] * -100,
                                            texttemplate="%{text:.0f} %",
                                            textposition='middle left',
                                            hovertemplate='',
                                            hoverinfo="skip",
                                            orientation='h'))

    fig_FutureOptimism.add_trace(go.Scatter(y=["<br>".join(textwrap.wrap(col, width=25)) for col in df[var]],
                                            x=df['optimistic'],
                                            mode='markers+text',
                                            showlegend=False,
                                            name="Optimistic",
                                            # marker=dict(color="#75787b00", size=0),
                                            marker=dict(color="#75787b", size=0, opacity=0),
                                            text=df['optimistic']*100,
                                            texttemplate="%{text:.0f} %",
                                            textposition='middle right',
                                            hovertemplate='',
                                            hoverinfo="skip",
                                            orientation='h'))


    fig_FutureOptimism.update_layout(title = title,
                                     barmode="relative",
                                     xaxis=dict(title="",
                                                showticklabels=False,
                                                showgrid=False),
                                     yaxis=dict(title=""),
                                     legend=dict(orientation='h',
                                                 traceorder='normal',
                                                 x=.5,
                                                 y=-0.05,
                                                 xanchor='center',
                                                 font=dict(size=12)),
                                     margin=dict(pad=5),
                                     paper_bgcolor='rgba(0,0,0,0)',
                                     plot_bgcolor='rgba(0,0,0,0)')

    # fig_FutureOptimism.update_yaxes(showline=True,
    #                                 linewidth=1,
    #                                 linecolor='black',
    #                                 position=max(df['V_pessimistic']*-1+df['S_pessimistic']*-1))

    return fig_FutureOptimism

def FutureFacet(df, title):

    title = "<br>".join(textwrap.wrap(title, width=65))

    fig_FutureFacet = make_subplots(rows=5,
                                    cols=3,
                                    shared_xaxes=True,
                                    shared_yaxes=True,
                                    vertical_spacing = 0,
                                    horizontal_spacing = 0.04)

    df = df.loc[df['busChar'].map({"Community nonprofits": 3, "Business nonprofits": 2, "Government agencies": 1, "Businesses": 0}).sort_values().index]

    items = df.sort_values("valIncrease", ascending=False)['item2'].unique()

    for j in range(5): # col num
        for i in range(3): # row nums
            if i+j == 0:
                legend = True
            else:
                legend=False
            this_item = items[i+(3*j)]

            this_df = df[df['item2']==this_item]

            fig_FutureFacet.add_trace(go.Bar(x=this_df['valNA'],
                                            y=this_df['busChar'],
                                            name="Not applicable",
                                            marker=dict(color="#ffc72c"),
                                            legendrank=1,
                                             showlegend=legend,
                                            text=this_df['valNA']*100,
                                            texttemplate="%{text:.0f} %",
                                            textposition='none',
                                            meta=this_df['statusNA'],
                                            hovertemplate="%{text:.0f} %" + "<br>Data quality: " + "%{meta}",
                                            orientation="h"), row=j+1, col=i+1)

            fig_FutureFacet.add_trace(go.Bar(y=this_df['busChar'],
                                            x=this_df['valDecrease'],
                                            name="Decrease",
                                            marker=dict(color="#50a684"),
                                            legendrank=2,
                                             showlegend=legend,
                                             text=this_df['valDecrease']*100,
                                            texttemplate="%{text:.0f} %",
                                            textposition='none',
                                            meta=this_df['statusDecrease'],
                                            hovertemplate="%{text:.0f} %" + "<br>Data quality: " + "%{meta}",
                                            orientation="h"), row=j+1, col=i+1)

            fig_FutureFacet.add_trace(go.Bar(y=this_df['busChar'],
                                            x=this_df['valSame'],
                                            name="About the same",
                                            marker=dict(color="#7BAFD4"),
                                            legendrank=3,
                                             showlegend=legend,
                                             text=this_df['valSame']*100,
                                            texttemplate="%{text:.0f} %",
                                            textposition='none',
                                            meta=this_df['statusSame'],
                                            hovertemplate="%{text:.0f} %" + "<br>Data quality: " + "%{meta}",
                                            orientation="h"), row=j+1, col=i+1)

            fig_FutureFacet.add_trace(go.Bar(y=this_df['busChar'],
                                            x=this_df['valIncrease'],
                                            name="Increase",
                                            marker=dict(color="#c8102e"),
                                            legendrank=4,
                                             showlegend=legend,
                                             text=this_df['valIncrease']*100,
                                            texttemplate="%{text:.0f} %",
                                            textposition='none',
                                            meta=this_df['statusIncrease'],
                                            hovertemplate="%{text:.0f} %" + "<br>Data quality: " + "%{meta}",
                                            orientation="h"), row=j+1, col=i+1)
            fig_FutureFacet.add_annotation(text=this_item,
                                                  showarrow=False,
                                                  xanchor='center',
                                                  # yanchor='top',
                                                  x=0.5,
                                                  y=3.75,
                                                  row=j+1, col=i+1)
            fig_FutureFacet.update_yaxes(#tickfont=dict(size=10),
                                         tickprefix="<span style='font-size:0.6vw'>",
                                         ticksuffix="</span>",
                                         row=j+1, col=i+1)

    for i in range(1,4):
        fig_FutureFacet.update_xaxes(title="",
                                    showticklabels=True,
                                    showgrid=False,
                                    tickformat=',.0%', row=5, col=i)

    fig_FutureFacet.update_layout(title=title,
                                 barmode='relative',
                                 showlegend=True,
                                 legend=dict(orientation = 'h',
                                               x = 0.5,
                                               y = -0.05,
                                               xanchor = 'center',
                                               font = dict(size = 12),
                                               # traceorder = 'reversed'
                                             ),
                                 yaxis=dict(title=""),
                                 paper_bgcolor='rgba(0,0,0,0)',
                                 plot_bgcolor='rgba(0,0,0,0)')

    return fig_FutureFacet

def FutureExpectations(df, title):

    title = "<br>".join(textwrap.wrap(title, width=65))

    fig_FutureExpectations = make_subplots(rows=len(df['seriesDate'].unique()), vertical_spacing = 0)

    dates = df['dateLabel'].sort_values(ascending=False).unique()

    for i in range(len(dates)):
        if i == 0:
            legend = True
        else:
            legend = False

        this_df = df[df['dateLabel'] == dates[i]]

        fig_FutureExpectations.add_trace(go.Bar(x=this_df['valNA'],
                                                y=this_df['busChar'],
                                                name="Not applicable",
                                                marker=dict(color="#ffc72c"),
                                                legendrank=1,
                                                showlegend=legend,
                                                text=this_df['valNA']*100,
                                                texttemplate="%{text:.0f} %",
                                                textposition='none',
                                                meta=this_df['statusNA'],
                                                hovertemplate="%{text:.1f} %"+"<br>Qualité de données : "+"%{meta}",
                                                orientation="h"), row=i+1, col=1)

        fig_FutureExpectations.add_trace(go.Bar(y=this_df['busChar'],
                                                x=this_df['valDecrease'],
                                                name="Decrease",
                                                marker=dict(color="#50a684"),
                                                legendrank=2,
                                                showlegend=legend,
                                                text=this_df['valDecrease']*100,
                                                texttemplate="%{text:.0f} %",
                                                textposition='none',
                                                meta=this_df['statusDecrease'],
                                                hovertemplate="%{text:.1f} %"+"<br>Qualité de données : "+"%{meta}",
                                                orientation="h"), row=i+1, col=1)

        fig_FutureExpectations.add_trace(go.Bar(y=this_df['busChar'],
                                                x=this_df['valSame'],
                                                name="About the same",
                                                marker=dict(color="#7BAFD4"),
                                                legendrank=3,
                                                showlegend=legend,
                                                text=this_df['valSame']*100,
                                                texttemplate="%{text:.0f} %",
                                                textposition='none',
                                                meta=this_df['statusSame'],
                                                hovertemplate="%{text:.1f} %"+"<br>Qualité de données : "+"%{meta}",
                                                orientation="h"), row=i+1, col=1)

        fig_FutureExpectations.add_trace(go.Bar(y=this_df['busChar'],
                                                x=this_df['valIncrease'],
                                                name="Increase",
                                                marker=dict(color="#c8102e"),
                                                legendrank=4,
                                                showlegend=legend,
                                                text=this_df['valIncrease']*100,
                                                texttemplate="%{text:.0f} %",
                                                textposition='none',
                                                meta=this_df['statusIncrease'],
                                                hovertemplate="%{text:.1f} %"+"<br>Qualité de données : "+"%{meta}",
                                                orientation="h"), row=i+1, col=1)

        fig_FutureExpectations.add_annotation(text=dates[i],
                                               showarrow=False,
                                               xanchor='center',
                                               # yanchor='top',
                                               x=0.5,
                                               y=4,
                                              row=i+1, col=1)

        fig_FutureExpectations.update_xaxes(title="",
                                            showticklabels=False,
                                            showgrid=False, row=i+1, col=1)

        fig_FutureExpectations.update_yaxes(#tickfont=dict(size=10),
                                            tickprefix="<span style='font-size:0.6vw'>",
                                            ticksuffix="</span>",
                                            row=i + 1, col=1)

    fig_FutureExpectations.update_layout(title=title,
                                         barmode='relative',
                                         legend=dict(orientation='h',
                                                     x=0.5,
                                                     y=-0.03,
                                                     xanchor='center',
                                                     font=dict(size=12),
                                                     # traceorder = 'reversed'
                                                     ),
                                         # showlegend=True,
                                         xaxis=dict(title="",
                                                    showticklabels=False,
                                                    showgrid=False,
                                                    ),
                                         yaxis=dict(title=""),
                                     paper_bgcolor='rgba(0,0,0,0)',
                                     plot_bgcolor='rgba(0,0,0,0)')

    return fig_FutureExpectations
