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

    df = df.loc[df['busChar'].map({"Organismes communautaires à but non lucratif": 3, "Institutions commerciales à but non lucratif": 2, "Institutions gouvernementales": 1, "Entreprises": 0}).sort_values().index]

    if var == "dateLabel":
        title += "<br><sup>Remarque : aucune donnée n’est disponible pour certains trimestres et pour certaines années</sup>"

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
                                        x=df['S_pessimistic']*100,
                                        name="Plutôt pessimiste",
                                        marker=dict(color="#0B6623"),
                                        legendrank=2,
                                        text=[str(round(val*-100))+" %" if not np.isnan(val) and abs(round(val*100)) >= 0.5 else None for val in df['S_pessimistic']],
                                        # texttemplate="%{text:.0f} %",
                                        textposition='inside',
                                        insidetextanchor='middle',
                                        meta=df['S_pessimisticStat'],
                                        hovertemplate="%{x:.1f} %"+"<br>Qualité de données : "+"%{meta}",
                                        orientation='h'))

    fig_FutureOptimism.add_trace(go.Bar(y=["<br>".join(textwrap.wrap(col, width=25)) for col in df[var]],
                                        x=df['V_pessimistic']*100,
                                        name="Très pessimiste",
                                        marker=dict(color="#75787b"),
                                        legendrank=1,
                                        text=[str(round(val*-100))+" %" if not np.isnan(val) and abs(round(val*100)) >= 0.5 else None for val in df['V_pessimistic']],
                                        # texttemplate="%{text:.0f} %",
                                        textposition='inside',
                                        insidetextanchor='middle',
                                        meta=df['V_pessimisticStat'],
                                        hovertemplate="%{x:.1f} %"+"<br>Qualité de données : "+"%{meta}",
                                        orientation='h'))

    fig_FutureOptimism.add_trace(go.Bar(y=["<br>".join(textwrap.wrap(col, width=25)) for col in df[var]],
                                        x=df['S_optimistic']*100,
                                        name="Plutôt optimiste",
                                        marker=dict(color="#234C66"),
                                        legendrank=3,
                                        text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['S_optimistic']],
                                        # texttemplate="%{text:.0f} %",
                                        textposition='inside',
                                        insidetextanchor='middle',
                                        meta=df['S_optimisticStat'],
                                        hovertemplate="%{x:.1f} %"+"<br>Qualité de données : "+"%{meta}",
                                        orientation='h'))

    fig_FutureOptimism.add_trace(go.Bar(y=["<br>".join(textwrap.wrap(col, width=25)) for col in df[var]],
                                        x=df['V_optimistic']*100,
                                        name="Très optimiste",
                                        marker=dict(color="#FD7B5F"),
                                        legendrank=4,
                                        text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['V_optimistic']],
                                        # texttemplate="%{text:.0f} %",
                                        textposition='inside',
                                        insidetextanchor='middle',
                                        meta=df['V_optimisticStat'],
                                        hovertemplate="%{x:.1f} %"+"<br>Qualité de données : "+"%{meta}",
                                        orientation='h'))

    fig_FutureOptimism.add_trace(go.Scatter(y=["<br>".join(textwrap.wrap(col, width=25)) for col in df[var]],
                                            x=df['pessimistic']*100,
                                            mode='markers+text',
                                            showlegend=False,
                                            name="Pessimiste",
                                            # marker=dict(color="#75787b00", size=0),
                                            marker=dict(color="#75787b", size=0, opacity=0),
                                            text=[str(round(val*-100))+" %" if not np.isnan(val) and abs(round(val*100)) >= 0.5 else None for val in df['pessimistic']],
                                            # texttemplate="%{text:.0f} %",
                                            textposition='middle left',
                                            hovertemplate='',
                                            hoverinfo="skip",
                                            orientation='h'))

    fig_FutureOptimism.add_trace(go.Scatter(y=["<br>".join(textwrap.wrap(col, width=25)) for col in df[var]],
                                            x=df['optimistic']*100,
                                            mode='markers+text',
                                            showlegend=False,
                                            name="Optimiste",
                                            # marker=dict(color="#75787b00", size=0),
                                            marker=dict(color="#75787b", size=0, opacity=0),
                                            text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in df['optimistic']],
                                            # texttemplate="%{text:.0f} %",
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

    items = df.sort_values("valIncrease", ascending=False)['item2'].unique()

    fig_FutureFacet = make_subplots(rows=5,
                                    cols=3,
                                    shared_xaxes=True,
                                    shared_yaxes=True,
                                    vertical_spacing = 0.04,
                                    horizontal_spacing = 0.075,
                                    # subplot_titles=["<br>".join(textwrap.wrap(this_item, 30)) for this_item in items]
                                    # column_widths=[1,1,1]
                                    )

    df = df.loc[df['busChar'].map({"Organismes communautaires à but non lucratif": 3, "Institutions commerciales à but non lucratif": 2, "Institutions gouvernementales": 1, "Entreprises": 0}).sort_values().index]


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
                                            name="Sans objet",
                                            marker=dict(color="#FCD12A"),
                                            legendrank=1,
                                            showlegend=legend,
                                            text=this_df['valNA']*100,
                                            texttemplate="%{text:.0f} %",
                                            textposition='none',
                                            meta=this_df['statusNA'],
                                            hovertemplate="%{text:.0f} %" + "<br>Qualité de données : " + "%{meta}",
                                            orientation="h"), row=j+1, col=i+1)

            fig_FutureFacet.add_trace(go.Bar(y=this_df['busChar'],
                                            x=this_df['valDecrease'],
                                            name="Diminution",
                                            marker=dict(color="#0B6623"),
                                            legendrank=2,
                                             showlegend=legend,
                                             text=this_df['valDecrease']*100,
                                            texttemplate="%{text:.0f} %",
                                            textposition='none',
                                            meta=this_df['statusDecrease'],
                                            hovertemplate="%{text:.0f} %" + "<br>Qualité de données : " + "%{meta}",
                                            orientation="h"), row=j+1, col=i+1)

            fig_FutureFacet.add_trace(go.Bar(y=this_df['busChar'],
                                            x=this_df['valSame'],
                                            name="À peu près identique",
                                            marker=dict(color="#234C66"),
                                            legendrank=3,
                                             showlegend=legend,
                                             text=this_df['valSame']*100,
                                            texttemplate="%{text:.0f} %",
                                            textposition='none',
                                            meta=this_df['statusSame'],
                                            hovertemplate="%{text:.0f} %" + "<br>Qualité de données : " + "%{meta}",
                                            orientation="h"), row=j+1, col=i+1)

            fig_FutureFacet.add_trace(go.Bar(y=this_df['busChar'],
                                            x=this_df['valIncrease'],
                                            name="Augmentation",
                                            marker=dict(color="#FD7B5F"),
                                            legendrank=4,
                                             showlegend=legend,
                                             text=this_df['valIncrease']*100,
                                            texttemplate="%{text:.0f} %",
                                            textposition='none',
                                            meta=this_df['statusIncrease'],
                                            hovertemplate="%{text:.0f} %" + "<br>Qualité de données : " + "%{meta}",
                                            orientation="h"), row=j+1, col=i+1)
            fig_FutureFacet.add_annotation(text="<br>".join(textwrap.wrap(this_item, 25)),
                                           font=dict(size=11),
                                                  showarrow=False,
                                                  xanchor='center',
                                                  yanchor='bottom',
                                                  x=0.5,
                                                  y=3.5,
                                                  row=j+1, col=i+1)
            fig_FutureFacet.update_yaxes(#tickfont=dict(size=10),
                                         tickprefix="<span style='font-size:0.6vw'>",
                                         ticksuffix="</span>",
                                         row=j+1, col=i+1)
            fig_FutureFacet.update_layout(title=dict(font=dict(size=12)))

    for i in range(1,4):
        fig_FutureFacet.update_xaxes(title="",
                                     showticklabels=True,
                                     showgrid=False,
                                     tickformat='.0%',
                                     # ticksuffix=" %",
                                     range=[0,1], row=5, col=i)

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

        fig_FutureExpectations.add_trace(go.Bar(x=this_df['valNA']*100,
                                                y=this_df['busChar'],
                                                name="Sans objet",
                                                marker=dict(color="#FCD12A"),
                                                legendrank=1,
                                                showlegend=legend,
                                                text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in this_df['valNA']],
                                                # texttemplate="%{text:.0f} %",
                                                textposition='none',
                                                meta=this_df['statusNA'],
                                                hovertemplate="%{x:.1f} %"+"<br>Qualité de données : "+"%{meta}",
                                                orientation="h"), row=i+1, col=1)

        fig_FutureExpectations.add_trace(go.Bar(y=this_df['busChar'],
                                                x=this_df['valDecrease']*100,
                                                name="Diminution",
                                                marker=dict(color="#0B6623"),
                                                legendrank=2,
                                                showlegend=legend,
                                                text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in this_df['valDecrease']],
                                                # texttemplate="%{text:.0f} %",
                                                textposition='none',
                                                meta=this_df['statusDecrease'],
                                                hovertemplate="%{x:.1f} %"+"<br>Qualité de données : "+"%{meta}",
                                                orientation="h"), row=i+1, col=1)

        fig_FutureExpectations.add_trace(go.Bar(y=this_df['busChar'],
                                                x=this_df['valSame']*100,
                                                name="À peu près identique",
                                                marker=dict(color="#234C66"),
                                                legendrank=3,
                                                showlegend=legend,
                                                text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in this_df['valSame']],
                                                # texttemplate="%{text:.0f} %",
                                                textposition='none',
                                                meta=this_df['statusSame'],
                                                hovertemplate="%{x:.1f} %"+"<br>Qualité de données : "+"%{meta}",
                                                orientation="h"), row=i+1, col=1)

        fig_FutureExpectations.add_trace(go.Bar(y=this_df['busChar'],
                                                x=this_df['valIncrease']*100,
                                                name="Augmentation",
                                                marker=dict(color="#FD7B5F"),
                                                legendrank=4,
                                                showlegend=legend,
                                                text=[str(round(val*100))+" %" if not np.isnan(val) and round(val*100) >= 0.5 else None for val in this_df['valIncrease']],
                                                # texttemplate="%{text:.0f} %",
                                                textposition='none',
                                                meta=this_df['statusIncrease'],
                                                hovertemplate="%{x:.1f} %"+"<br>Qualité de données : "+"%{meta}",
                                                orientation="h"), row=i+1, col=1)

        fig_FutureExpectations.add_annotation(text=dates[i],
                                               showarrow=False,
                                               xanchor='center',
                                               # yanchor='top',
                                               x=50,
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
