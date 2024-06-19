# Callbacks file for GV_NC_2018_FR converted from GAV0306_fr.py

import dash
from .data_processing import *
from .graphs import *


def register_callbacks(app):

    @app.callback(
        dash.dependencies.Output('NewCanadiansDonRateAmt_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff1 = NewCanadiansDonRates_2018[NewCanadiansDonRates_2018['Region'] == region]

        dff2 = NewCanadiansAvgDonAmt_2018[NewCanadiansAvgDonAmt_2018['Region'] == region]

        dff1 = dff1.replace("Giving Overall", "Le don en général")
        # dff1 = dff1.replace("Naturalized", "Naturalisé.e")
        # dff1 = dff1.replace("Non-Canadian", "Non canadien.ne")

        dff2 = dff2.replace("Giving Overall", "Le don en général")
        # dff2 = dff2.replace("Naturalized", "Naturalisé.e")
        # dff2 = dff2.replace("Non-Canadian", "Non canadien.ne")

        # name1 = "Native-born"
        # name2 = "Naturalized"
        # name3 = "Non-Canadian"
        name1 = "Né.e au Canada"
        name2 = "Naturalisé.e"
        name3 = "Non canadien.ne"

        title = '{}, {}'.format(
            "Taux des dons laïcs et religieux totaux et montant moyen des dons", region)
        return triple_horizontal_rate_avg(
            dff1, dff2, name1, name2, name3, title, giving=True)

    @app.callback(
        dash.dependencies.Output('NewCanadiansDonRateByCause_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = NewCanadiansDonRateByCause_2018[NewCanadiansDonRateByCause_2018['Region'] == region]

        dff = dff.replace("Native-born", "Né.e au Canada")
        dff = dff.replace("Naturalized", "Naturalisé.e")
        dff = dff.replace("Non-Canadian", "Non canadien.ne")

        # name1 = "Native-born"
        # name2 = "Naturalized"
        # name3 = "Non-Canadian"
        name1 = "Né.e au Canada"
        name2 = "Naturalisé.e"
        name3 = "Non canadien.ne"

        title = '{}, {}'.format("Taux de dons par cause", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "percent")

    @app.callback(
        dash.dependencies.Output('NewCanadiansAvgAmtByCause_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = NewCanadiansAvgDonByCause_2018[NewCanadiansAvgDonByCause_2018['Region'] == region]

        dff = dff.replace("Native-born", "Né.e au Canada")
        dff = dff.replace("Naturalized", "Naturalisé.e")
        dff = dff.replace("Non-Canadian", "Non canadien.ne")

        # name1 = "Native-born"
        # name2 = "Naturalized"
        # name3 = "Non-Canadian"
        name1 = "Né.e au Canada"
        name2 = "Naturalisé.e"
        name3 = "Non canadien.ne"
        title = '{}, {}'.format(
            "Montant moyen des dons selon la cause", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "dollar")

    @app.callback(
        dash.dependencies.Output('NewCanadiansDonRateByMeth_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = NewCanadiansDonRateByMeth_2018[NewCanadiansDonRateByMeth_2018['Region'] == region]

        dff = dff.replace("Native-born", "Né.e au Canada")
        dff = dff.replace("Naturalized", "Naturalisé.e")
        dff = dff.replace("Non-Canadian", "Non canadien.ne")

        # name1 = "Native-born"
        # name2 = "Naturalized"
        # name3 = "Non-Canadian"
        name1 = "Né.e au Canada"
        name2 = "Naturalisé.e"
        name3 = "Non canadien.ne"
        title = '{}, {}'.format("Taux de dons par méthode", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "percent")

    @app.callback(
        dash.dependencies.Output('NewCanadiansAvgAmtByMeth_13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = NewCanadiansAvgDonByMeth_2018[NewCanadiansAvgDonByMeth_2018['Region'] == region]

        dff = dff.replace("Native-born", "Né.e au Canada")
        dff = dff.replace("Naturalized", "Naturalisé.e")
        dff = dff.replace("Non-Canadian", "Non canadien.ne")

        # name1 = "Native-born"
        # name2 = "Naturalized"
        # name3 = "Non-Canadian"
        name1 = "Né.e au Canada"
        name2 = "Naturalisé.e"
        name3 = "Non canadien.ne"
        title = '{}, {}'.format("Montant moyen des dons par méthode", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "dollar")

    @app.callback(
        dash.dependencies.Output('NewCanadiansMotivations_13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = NewCanadiansReasonsGiving_2018[NewCanadiansReasonsGiving_2018['Region'] == region]

        dff = dff.replace("Native-born", "Né.e au Canada")
        dff = dff.replace("Naturalized", "Naturalisé.e")
        dff = dff.replace("Non-Canadian", "Non canadien.ne")

        # name1 = "Native-born"
        # name2 = "Naturalized"
        # name3 = "Non-Canadian"
        name1 = "Né.e au Canada"
        name2 = "Naturalisé.e"
        name3 = "Non canadien.ne"
        title = '{}, {}'.format("Motivations des dons", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "percent")

    @app.callback(
        dash.dependencies.Output('NewCanadiansBarriers_13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = NewCanadiansBarriers_2018[NewCanadiansBarriers_2018['Region'] == region]

        dff = dff.replace("Native-born", "Né.e au Canada")
        dff = dff.replace("Naturalized", "Naturalisé.e")
        dff = dff.replace("Non-Canadian", "Non canadien.ne")

        # name1 = "Native-born"
        # name2 = "Naturalized"
        # name3 = "Non-Canadian"
        name1 = "Né.e au Canada"
        name2 = "Naturalisé.e"
        name3 = "Non canadien.ne"
        title = '{}, {}'.format("Freins à donner davantage", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "percent")

    @app.callback(
        dash.dependencies.Output('NewCanadiansEfficiency_13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = NewCanadiansEfficiencyConcerns_2018[NewCanadiansEfficiencyConcerns_2018['Region'] == region]

        dff = dff.replace("Native-born", "Né.e au Canada")
        dff = dff.replace("Naturalized", "Naturalisé.e")
        dff = dff.replace("Non-Canadian", "Non canadien.ne")

        # name1 = "Native-born"
        # name2 = "Naturalized"
        # name3 = "Non-Canadian"
        name1 = "Né.e au Canada"
        name2 = "Naturalisé.e"
        name3 = "Non canadien.ne"
        title = '{}, {}'.format(
            "Raisons des préoccupations relatives à l'efficience", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "percent")

    @app.callback(
        dash.dependencies.Output('NewCanadiansSolicitations_13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = NewCanadiansSolicitationConcerns_2018[NewCanadiansSolicitationConcerns_2018['Region'] == region]

        dff = dff.replace("Native-born", "Né.e au Canada")
        dff = dff.replace("Naturalized", "Naturalisé.e")
        dff = dff.replace("Non-Canadian", "Non canadien.ne")

        # name1 = "Native-born"
        # name2 = "Naturalized"
        # name3 = "Non-Canadian"
        name1 = "Né.e au Canada"
        name2 = "Naturalisé.e"
        name3 = "Non canadien.ne"
        title = '{}, {}'.format(
            "Raisons de l'aversion pour les sollicitations", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "percent")

    @app.callback(
        dash.dependencies.Output('NewCanadiansVolRateVolAmt_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff1 = NewCanadiansVolRate_2018[NewCanadiansVolRate_2018['Region'] == region]

        dff2 = NewCanadiansAvgHrs_2018[NewCanadiansAvgHrs_2018['Region'] == region]

        # name1 = "Native-born"
        # name2 = "Naturalized"
        # name3 = "Non-Canadian"
        name1 = "Né.e au Canada"
        name2 = "Naturalisé.e"
        name3 = "Non canadien.ne"
        title = '{}, {}'.format(
            "Taux et nombre moyen d'heures consacrées au bénévolat, à l'aide d'autrui<br>et à l'engagement communautaire",
            region)
        return triple_horizontal_rate_avg(
            dff1, dff2, name1, name2, name3, title, giving=False)

    @app.callback(
        dash.dependencies.Output('NewCanadiansVolRateByCause_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = NewCanadiansVolRateByCause_2018[NewCanadiansVolRateByCause_2018['Region'] == region]

        # name1 = "Native-born"
        # name2 = "Naturalized"
        # name3 = "Non-Canadian"
        name1 = "Né.e au Canada"
        name2 = "Naturalisé.e"
        name3 = "Non canadien.ne"
        title = '{}, {}'.format("Taux de bénévoles selon la cause", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "percent")

    @app.callback(
        dash.dependencies.Output('NewCanadiansAvgHrsByCause_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = NewCanadiansAvgHrsByCause_2018[NewCanadiansAvgHrsByCause_2018['Region'] == region]

        # name1 = "Native-born"
        # name2 = "Naturalized"
        # name3 = "Non-Canadian"
        name1 = "Né.e au Canada"
        name2 = "Naturalisé.e"
        name3 = "Non canadien.ne"
        title = '{}, {}'.format(
            "Nombre moyen d'heures de bénévolat selon la cause", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "hours")

    @app.callback(
        dash.dependencies.Output('NewCanadiansVolRateByActivity_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = NewCanadiansVolRateByActivity_2018[NewCanadiansVolRateByActivity_2018['Region'] == region]

        # name1 = "Native-born"
        # name2 = "Naturalized"
        # name3 = "Non-Canadian"
        name1 = "Né.e au Canada"
        name2 = "Naturalisé.e"
        name3 = "Non canadien.ne"
        title = '{}, {}'.format("Taux de bénévoles par activité", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "percent")

    @app.callback(
        dash.dependencies.Output('NewCanadiansAvgHrsByActivity_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = NewCanadiansAvgHrsByActivity_2018[NewCanadiansAvgHrsByActivity_2018['Region'] == region]

        # name1 = "Native-born"
        # name2 = "Naturalized"
        # name3 = "Non-Canadian"
        name1 = "Né.e au Canada"
        name2 = "Naturalisé.e"
        name3 = "Non canadien.ne"
        title = '{}, {}'.format(
            "Nombre moyen d'heures de bénévolat par activité", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "hours")

    @app.callback(
        dash.dependencies.Output('NewCanadiansVolMotivations_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = NewCanadiansReasonsVol_2018[NewCanadiansReasonsVol_2018['Region'] == region]

        # name1 = "Native-born"
        # name2 = "Naturalized"
        # name3 = "Non-Canadian"
        name1 = "Né.e au Canada"
        name2 = "Naturalisé.e"
        name3 = "Non canadien.ne"
        title = '{}, {}'.format("Motivations du bénévolat", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "percent")

    @app.callback(
        dash.dependencies.Output('NewCanadiansVolBarriers_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = NewCanadiansBarriersVol_2018[NewCanadiansBarriersVol_2018['Region'] == region]

        # name1 = "Native-born"
        # name2 = "Naturalized"
        # name3 = "Non-Canadian"
        name1 = "Né.e au Canada"
        name2 = "Naturalisé.e"
        name3 = "Non canadien.ne"
        title = '{}, {}'.format("Freins à faire plus de bénévolat", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "percent")

    @app.callback(
        dash.dependencies.Output('NewCanadiansRateHelpDirect_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = NewCanadiansHelpDirectlyRate_2018[NewCanadiansHelpDirectlyRate_2018['Region'] == region]

        # name1 = "Native-born"
        # name2 = "Naturalized"
        # name3 = "Non-Canadian"
        name1 = "Né.e au Canada"
        name2 = "Naturalisé.e"
        name3 = "Non canadien.ne"
        title = '{}, {}'.format("Méthodes d'aide directe d'autrui", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "percent")

    @app.callback(
        dash.dependencies.Output('NewCanadiansHrsHelpDirect_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = NewCanadiansAvgHrsHelpDirectly_2018[NewCanadiansAvgHrsHelpDirectly_2018['Region'] == region]

        # name1 = "Native-born"
        # name2 = "Naturalized"
        # name3 = "Non-Canadian"
        name1 = "Né.e au Canada"
        name2 = "Naturalisé.e"
        name3 = "Non canadien.ne"
        title = '{}, {}'.format(
            "Nombre moyen d'heures consacrées à l'aide directe d'autrui", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "hours")

    @app.callback(
        dash.dependencies.Output('NewCanadiansRateCommInvolve_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = NewCanadiansCommInvolveRate_2018[NewCanadiansCommInvolveRate_2018['Region'] == region]

        # name1 = "Native-born"
        # name2 = "Naturalized"
        # name3 = "Non-Canadian"
        name1 = "Né.e au Canada"
        name2 = "Naturalisé.e"
        name3 = "Non canadien.ne"
        title = '{}, {}'.format("Types d'engagement communautaire", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "percent")

    @app.callback(
        dash.dependencies.Output('NewCanadiansHrsCommInvolve_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = NewCanadiansAvgHrsCommInvolve_2018[NewCanadiansAvgHrsCommInvolve_2018['Region'] == region]

        # name1 = "Native-born"
        # name2 = "Naturalized"
        # name3 = "Non-Canadian"
        name1 = "Né.e au Canada"
        name2 = "Naturalisé.e"
        name3 = "Non canadien.ne"
        title = '{}, {}'.format(
            "Nombre moyen d'heures consacrées aux formes d'engagement communautaire",
            region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "hours")


# def triple_horizontal_rate_avg(dff_1, dff_2, name1, name2, name3, title, giving=True):
#     dff_1['Text'] = np.select([dff_1["Marker"] == "*", dff_1["Marker"] == "...", pd.isnull(dff_1["Marker"])],
#                               [dff_1.Estimate.map(str) + "%*", "...", dff_1.Estimate.map(str) + " %"])
#     dff_1['HoverText'] = np.select([dff_1["Marker"] == "*",
#                                     dff_1["Marker"] == "...",
#                                     pd.isnull(dff_1["Marker"])],
#                                    ["Estimate: " + dff_1.Estimate.map(str) + "% ± " + (dff_1["CI Upper"] - dff_1["Estimate"]).map(str) + "%<br><b>Use with caution</b>",
#                                     "Estimate Suppressed",
#                                     "Estimate: " + dff_1.Estimate.map(str) + "% ± " + (dff_1["CI Upper"] - dff_1["Estimate"]).map(str) + " %"])
#
#     if giving:
#         dff_2['Text'] = np.select([dff_2["Marker"] == "*", dff_2["Marker"] == "...", pd.isnull(dff_2["Marker"])],
#                                   ["$" + dff_2.Estimate.map(str) + "*", "...", "$" + dff_2.Estimate.map(str)])
#         dff_2['HoverText'] = np.select([dff_2["Marker"] == "*",
#                                         dff_2["Marker"] == "...",
#                                         pd.isnull(dff_2["Marker"])],
#                                        ["Estimate: $" + dff_2.Estimate.map(str) + " ± $" + (dff_2["CI Upper"] - dff_2["Estimate"]).map(str) + "<br><b>Use with caution</b>",
#                                         "Estimate Suppressed",
#                                         "Estimate: $" + dff_2.Estimate.map(str) + " ± $" + (dff_2["CI Upper"] - dff_2["Estimate"]).map(str)])
#         dff_1['QuestionText'] = np.select([dff_1["QuestionText"] == 'Donor flag', dff_1["QuestionText"] == 'Secular donor flag', dff_1["QuestionText"] == 'Religious donor flag'],
#                                           ["Le don en général", "Dons séculaires", "Dons religieux"])
#         dff_2['QuestionText'] = np.select([dff_2["QuestionText"] == 'Total donation<br>amount', dff_2["QuestionText"] == 'Secular donation<br>amount', dff_2["QuestionText"] == 'Religious donation<br>amount'],
#                                           ["Le don en général", "Dons séculaires", "Dons religieux"])
#     else:
#         dff_2['Text'] = np.select([dff_2["Marker"] == "*", dff_2["Marker"] == "...", pd.isnull(dff_2["Marker"])],
#                                   [dff_2.Estimate.map(str) + "*", "...", dff_2.Estimate.map(str)])
#         dff_2['HoverText'] = np.select([dff_2["Marker"] == "*",
#                                         dff_2["Marker"] == "...",
#                                         pd.isnull(dff_2["Marker"])],
#                                        ["Estimate: " + dff_2.Estimate.map(str) + " ± " + (dff_2["CI Upper"] - dff_2["Estimate"]).map(str) + "<br><b>Use with caution</b>",
#                                         "Estimate Suppressed",
#                                         "Estimate: " + dff_2.Estimate.map(str) + " ± " + (dff_2["CI Upper"] - dff_2["Estimate"]).map(str)])
#         dff_1['QuestionText'] = np.select([dff_1["QuestionText"] == 'Volunteer flag', dff_1["QuestionText"] == 'Direct help flag', dff_1["QuestionText"] == 'Community<br>involvement flag'],
#                                           ["Volontariat", "Aider les autres", "CEngagement communautaire"])
#         dff_2['QuestionText'] = np.select([dff_2["QuestionText"] == 'Total formal<br>volunteer hours', dff_2["QuestionText"] == 'Total hours spent<br>helping directly', dff_2["QuestionText"] == 'Total hours spent on<br>community<br>involvement'],
#                                           ["Volontariat", "Aider les autres", "CEngagement communautaire"])
#
#     dff1 = dff_1[dff_1['Attribute'] == name1]
#
#     dff2 = dff_1[dff_1['Attribute'] == name2]
#
#     dff3 = dff_1[dff_1['Attribute'] == name3]
#
#     dff4 = dff_2[dff_2['Attribute'] == name1]
#
#     dff5 = dff_2[dff_2['Attribute'] == name2]
#
#     dff6 = dff_2[dff_2['Attribute'] == name3]
#
#     fig = go.Figure()
#
#     fig.add_trace(go.Bar(y=dff1['CI Upper'],
#                          x=dff1['QuestionText'],
#                          error_y=None,
#                          marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
#                          showlegend=False,
#                          hoverinfo="skip",
#                          text=None,
#                          textposition="outside",
#                          cliponaxis=False,
#                          offsetgroup=2,
#                          yaxis='y2'
#                          ),
#                   )
#
#     fig.add_trace(go.Bar(y=dff2['CI Upper'],
#                          x=dff2['QuestionText'],
#                          error_y=None,
#                          marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
#                          showlegend=False,
#                          hoverinfo="skip",
#                          text=None,
#                          textposition="outside",
#                          cliponaxis=False,
#                          offsetgroup=1,
#                          yaxis='y2'
#                          ),
#                   )
#
#     fig.add_trace(go.Bar(y=dff3['CI Upper'],
#                          x=dff3['QuestionText'],
#                          error_y=None,
#                          marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
#                          showlegend=False,
#                          hoverinfo="skip",
#                          text=None,
#                          textposition="outside",
#                          cliponaxis=False,
#                          offsetgroup=3,
#                          yaxis='y2'
#                          ),
#                   )
#
#     fig.add_trace(go.Bar(y=[0, 0, 0],
#                          x=dff6['QuestionText'],
#                          width=[0.5, 0.5, 0.5],
#                          cliponaxis=False,
#                          showlegend=False,
#                          offsetgroup=4,
#                          yaxis='y1'
#                          ),
#                   )
#
#     fig.add_trace(go.Bar(y=dff4['CI Upper'],
#                          x=dff4['QuestionText'],
#                          error_y=None,
#                          marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
#                          showlegend=False,
#                          hoverinfo="skip",
#                          text=None,
#                          textposition="outside",
#                          cliponaxis=False,
#                          offsetgroup=5,
#                          yaxis='y1'
#                          ),
#                   )
#
#     fig.add_trace(go.Bar(y=dff5['CI Upper'],
#                          x=dff5['QuestionText'],
#                          error_y=None,
#                          marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
#                          showlegend=False,
#                          hoverinfo="skip",
#                          text=None,
#                          textposition="outside",
#                          cliponaxis=False,
#                          offsetgroup=6,
#                          yaxis='y1'
#                          ),
#                   )
#
#     fig.add_trace(go.Bar(y=dff6['CI Upper'],
#                          x=dff6['QuestionText'],
#                          error_y=None,
#                          marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
#                          showlegend=False,
#                          hoverinfo="skip",
#                          text=None,
#                          textposition="outside",
#                          cliponaxis=False,
#                          offsetgroup=7,
#                          yaxis='y1'
#                          ),
#                   )
#
#     fig.add_trace(go.Bar(y=dff1['Estimate'],
#                          x=dff1['QuestionText'],
#                          error_y=None,
#                          hovertext=dff1['HoverText'],
#                          hovertemplate="%{hovertext}",
#                          hoverlabel=dict(font=dict(color="white")),
#                          hoverinfo="text",
#                          marker=dict(color="#FD7B5F"),
#                          text=dff1['Text'],
#                          textposition='outside',
#                          cliponaxis=False,
#                          name=name1,
#                          offsetgroup=2,
#                          yaxis='y2'
#                          ),
#                   )
#
#     fig.add_trace(go.Bar(y=dff2['Estimate'],
#                          x=dff2['QuestionText'],
#                          error_y=None,
#                          hovertext=dff2['HoverText'],
#                          hovertemplate="%{hovertext}",
#                          hoverlabel=dict(font=dict(color="white")),
#                          hoverinfo="text",
#                          marker=dict(color="#234C66"),
#                          text=dff2['Text'],
#                          textposition='outside',
#                          cliponaxis=False,
#                          name=name2,
#                          offsetgroup=1, yaxis='y2'
#                          ),
#                   )
#
#     fig.add_trace(go.Bar(y=dff3['Estimate'],
#                          x=dff3['QuestionText'],
#                          error_y=None,
#                          hovertext=dff3['HoverText'],
#                          hovertemplate="%{hovertext}",
#                          hoverlabel=dict(font=dict(color="white")),
#                          hoverinfo="text",
#                          marker=dict(color="#0B6623"),
#                          text=dff3['Text'],
#                          textposition='outside',
#                          cliponaxis=False,
#                          name=name3,
#                          offsetgroup=3, yaxis='y2'
#                          ),
#                   )
#
#     fig.add_trace(go.Bar(y=dff4['Estimate'],
#                          x=dff4['QuestionText'],
#                          error_y=None,
#                          hovertext=dff4['HoverText'],
#                          hovertemplate="%{hovertext}",
#                          hoverlabel=dict(font=dict(color="white")),
#                          hoverinfo="text",
#                          marker=dict(color="#FD7B5F"),
#                          text=dff4['Text'],
#                          textposition='outside',
#                          cliponaxis=False,
#                          showlegend=False,
#                          offsetgroup=5,
#                          yaxis='y1'
#                          ),
#                   )
#
#     fig.add_trace(go.Bar(y=dff5['Estimate'],
#                          x=dff5['QuestionText'],
#                          error_y=None,
#                          hovertext=dff5['HoverText'],
#                          hovertemplate="%{hovertext}",
#                          hoverlabel=dict(font=dict(color="white")),
#                          hoverinfo="text",
#                          marker=dict(color="#234C66"),
#                          text=dff5['Text'],
#                          textposition='outside',
#                          cliponaxis=False,
#                          showlegend=False,
#                          offsetgroup=6,
#                          yaxis='y1'
#                          ),
#                   )
#
#     fig.add_trace(go.Bar(y=dff6['Estimate'],
#                          x=dff6['QuestionText'],
#                          error_y=None,
#                          hovertext=dff6['HoverText'],
#                          hovertemplate="%{hovertext}",
#                          hoverlabel=dict(font=dict(color="white")),
#                          hoverinfo="text",
#                          marker=dict(color="#0B6623"),
#                          text=dff6['Text'],
#                          textposition='outside',
#                          cliponaxis=False,
#                          showlegend=False,
#                          offsetgroup=7,
#                          yaxis='y1'
#                          ),
#                   )
#
#     y2 = go.layout.YAxis(overlaying='y',
#                          side='left',
#                          autorange=False,
#                          range=[0, 1.25 * max(np.concatenate([dff1["CI Upper"], dff2["CI Upper"], dff3["CI Upper"]]))])
#     y1 = go.layout.YAxis(overlaying='y',
#                          side='right',
#                          autorange=False,
#                          range=[0, 1.25 * max(np.concatenate([dff4["CI Upper"], dff5["CI Upper"], dff6["CI Upper"]]))])
#
#     fig.update_layout(title={'text': title,
#                              'y': 0.99},
#                       margin={'l': 30, 'b': 30, 'r': 10, 't': 10},
#                       height=600,
#                       plot_bgcolor='rgba(0, 0, 0, 0)',
#                       bargroupgap=0.05,
#                       yaxis2=y2,
#                       yaxis1=y1,
#                       barmode="group",
#                       legend={'orientation': 'h', 'yanchor': "bottom", "xanchor": "center", "x": 0.5},
#                       updatemenus=[
#                           dict(
#                               type="buttons",
#                               xanchor='right',
#                               x=1.2,
#                               y=0.5,
#                               buttons=list([
#                                   dict(
#                                       args=[{"error_y": [None, None, None, None, None, None, None, None, None, None, None, None, None],
#                                              "text": [None, None, None, None, None, None, None, dff1['Text'], dff2['Text'], dff3['Text'], dff4['Text'], dff5['Text'], dff6['Text']]}],
#                                       label="Reset",
#                                       method="restyle"
#                                   ),
#                                   dict(
#                                       args=[{"error_y": [None, None, None, None, None, None, None,
#                                                          dict(
#                                                              type="data", array=dff1["CI Upper"] - dff1["Estimate"], color="#424242", thickness=1.5),
#                                                          dict(
#                                                              type="data", array=dff2["CI Upper"] - dff2["Estimate"], color="#424242", thickness=1.5),
#                                                          dict(
#                                                              type="data", array=dff3["CI Upper"] - dff3["Estimate"], color="#424242", thickness=1.5),
#                                                          dict(
#                                                              type="data", array=dff4["CI Upper"] - dff4["Estimate"], color="#424242", thickness=1.5),
#                                                          dict(
#                                                              type="data", array=dff5["CI Upper"] - dff5["Estimate"], color="#424242", thickness=1.5),
#                                                          dict(type="data", array=dff6["CI Upper"] - dff6["Estimate"], color="#424242", thickness=1.5)],
#                                              "text": [dff1['Text'], dff2['Text'], dff3['Text'], None, dff4['Text'], dff5['Text'], dff6['Text'], None, None, None, None, None, None]}],
#                                       label="Confidence Intervals",
#                                       method="restyle"
#                                   )
#                               ]),
#                           ),
#     ]
#     )
#
#     fig.update_yaxes(showgrid=False,
#                      showticklabels=False)
#     fig.update_xaxes(ticklabelposition="outside top",
#                      tickfont=dict(size=12))
#
#     markers = pd.concat([dff1["Marker"], dff2["Marker"], dff3["Marker"],
#                         dff4["Marker"], dff5["Marker"], dff6["Marker"]])
#     if markers.isin(["*"]).any() and markers.isin(["..."]).any():
#         fig.update_layout(margin={'l': 40, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="*<i>Use with caution<br>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     elif markers.isin(["*"]).any():
#         fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="*<i>Use with caution</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     elif markers.isin(["..."]).any():
#         fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="<i>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     else:
#         fig.update_layout(margin={'l': 30, 'b': 30, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.32, x=1.2, align="left", showarrow=False)])
#
#     return fig
#
#
# def triple_vertical_graphs_pops(dff, title, name1, name2, name3, type):
#     if type == "percent":
#         dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
#                                 [dff.Estimate.map(str) + " %" + "*", "...", dff.Estimate.map(str) + " %"])
#         dff['HoverText'] = np.select([dff["Marker"] == "*",
#                                       dff["Marker"] == "...",
#                                       pd.isnull(dff["Marker"])],
#                                      ["Estimate: " + dff.Estimate.map(str) + "% ± " + (dff["CI Upper"] - dff["Estimate"]).map(str) + "%<br><b>Use with caution</b>",
#                                       "Estimate Suppressed",
#                                       "Estimate: " + dff.Estimate.map(str) + "% ± " + (dff["CI Upper"] - dff["Estimate"]).map(str) + " %"])
#     elif type == "hours":
#         dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
#                                 [dff.Estimate.map(str) + "*", "...", dff.Estimate.map(str)])
#         dff['HoverText'] = np.select([dff["Marker"] == "*",
#                                       dff["Marker"] == "...",
#                                       pd.isnull(dff["Marker"])],
#                                      ["Estimate: " + dff.Estimate.map(str) + " ± " + (dff["CI Upper"] - dff["Estimate"]).map(str) + "<br><b>Use with caution</b>",
#                                       "Estimate Suppressed",
#                                       "Estimate: " + dff.Estimate.map(str) + " ± " + (dff["CI Upper"] - dff["Estimate"]).map(str)])
#     elif type == "dollar":
#         dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
#                                 ["$" + dff.Estimate.map(str) + "*", "...", "$" + dff.Estimate.map(str)])
#         dff['HoverText'] = np.select([dff["Marker"] == "*",
#                                       dff["Marker"] == "...",
#                                       pd.isnull(dff["Marker"])],
#                                      ["Estimate: $" + dff.Estimate.map(str) + " ± $" + (dff["CI Upper"] - dff["Estimate"]).map(str) + "<br><b>Use with caution</b>",
#                                       "Estimate Suppressed",
#                                       "Estimate: $" + dff.Estimate.map(str) + " ± $" + (dff["CI Upper"] - dff["Estimate"]).map(str)])
#
#     dff1 = dff[dff['Attribute'] == name1]
#
#     dff2 = dff[dff['Attribute'] == name2]
#
#     dff3 = dff[dff['Attribute'] == name3]
#
#     fig = go.Figure()
#
#     fig.add_trace(go.Bar(x=dff1['CI Upper'],
#                          y=dff1['QuestionText'],
#                          orientation="h",
#                          error_x=None,
#                          marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
#                          showlegend=False,
#                          hoverinfo="skip",
#                          text=None,
#                          textposition="outside",
#                          cliponaxis=False,
#                          offsetgroup=2
#                          ),
#                   )
#
#     fig.add_trace(go.Bar(x=dff2['CI Upper'],
#                          y=dff2['QuestionText'],
#                          orientation="h",
#                          error_x=None,
#                          marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
#                          showlegend=False,
#                          hoverinfo="skip",
#                          text=None,
#                          textposition="outside",
#                          cliponaxis=False,
#                          offsetgroup=1
#                          ),
#                   )
#
#     fig.add_trace(go.Bar(x=dff3['CI Upper'],
#                          y=dff3['QuestionText'],
#                          orientation="h",
#                          error_x=None,
#                          marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
#                          showlegend=False,
#                          hoverinfo="skip",
#                          text=None,
#                          textposition="outside",
#                          cliponaxis=False,
#                          offsetgroup=3
#                          ),
#                   )
#
#     fig.add_trace(go.Bar(x=dff1['Estimate'],
#                          y=dff1['QuestionText'],
#                          orientation="h",
#                          error_x=None,
#                          hovertext=dff1['HoverText'],
#                          hovertemplate="%{hovertext}",
#                          hoverlabel=dict(font=dict(color="white")),
#                          hoverinfo="text",
#                          marker=dict(color="#FD7B5F"),
#                          text=dff1['Text'],
#                          textposition='outside',
#                          cliponaxis=False,
#                          name=name1,
#                          offsetgroup=2
#                          ),
#                   )
#
#     fig.add_trace(go.Bar(x=dff2['Estimate'],
#                          y=dff2['QuestionText'],
#                          orientation="h",
#                          error_x=None,
#                          hovertext=dff2['HoverText'],
#                          hovertemplate="%{hovertext}",
#                          hoverlabel=dict(font=dict(color="white")),
#                          hoverinfo="text",
#                          marker=dict(color="#234C66"),
#                          text=dff2['Text'],
#                          textposition='outside',
#                          cliponaxis=False,
#                          name=name2,
#                          offsetgroup=1
#                          ),
#                   )
#
#     fig.add_trace(go.Bar(x=dff3['Estimate'],
#                          y=dff3['QuestionText'],
#                          orientation="h",
#                          error_x=None,
#                          hovertext=dff3['HoverText'],
#                          hovertemplate="%{hovertext}",
#                          hoverlabel=dict(font=dict(color="white")),
#                          hoverinfo="text",
#                          marker=dict(color="#0B6623"),
#                          text=dff3['Text'],
#                          textposition='outside',
#                          cliponaxis=False,
#                          name=name3,
#                          offsetgroup=3
#                          ),
#                   )
#
#     fig.update_layout(title={'text': title,
#                              'y': 0.99},
#                       margin={'l': 30, 'b': 30, 'r': 10, 't': 10},
#                       height=600,
#                       plot_bgcolor='rgba(0, 0, 0, 0)',
#                       bargroupgap=0.05,
#                       barmode="group",
#                       legend={'orientation': 'h', 'yanchor': "bottom"},
#                       updatemenus=[
#                           dict(
#                               type="buttons",
#                               xanchor='right',
#                               x=1.2,
#                               y=0.5,
#                               buttons=list([
#                                   dict(
#                                       args=[{"error_x": [None, None, None, None, None, None],
#                                              "text": [None, None, None, dff1['Text'], dff2['Text'], dff3['Text']]}],
#                                       label="Reset",
#                                       method="restyle"
#                                   ),
#                                   dict(
#                                       args=[{"error_x": [None, None, None, dict(type="data", array=dff1["CI Upper"] - dff1["Estimate"], color="#424242", thickness=1.5),
#                                                          dict(
#                                                              type="data", array=dff2["CI Upper"] - dff2["Estimate"], color="#424242", thickness=1.5),
#                                                          dict(type="data", array=dff3["CI Upper"] - dff3["Estimate"], color="#424242", thickness=1.5)],
#                                              "text": [dff1['Text'], dff2['Text'], dff3['Text'], None, None, None]}],
#                                       label="Confidence Intervals",
#                                       method="restyle"
#                                   )
#                               ]),
#                           ),
#     ]
#     )
#
#     fig.update_xaxes(showgrid=False,
#                      showticklabels=False,
#                      autorange=False,
#                      range=[0, 1.25 * max(np.concatenate([dff1["CI Upper"], dff2["CI Upper"], dff3["CI Upper"]]))])
#     fig.update_yaxes(autorange="reversed",
#                      ticklabelposition="outside top",
#                      tickfont=dict(size=11),
#                      categoryorder='array',
#                      categoryarray=dff2.sort_values(by="Estimate", ascending=False)["QuestionText"])
#
#     markers = pd.concat([dff1["Marker"], dff2["Marker"], dff3["Marker"]])
#     if markers.isin(["*"]).any() and markers.isin(["..."]).any():
#         fig.update_layout(margin={'l': 40, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="*<i>Use with caution<br>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     elif markers.isin(["*"]).any():
#         fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="*<i>Use with caution</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     elif markers.isin(["..."]).any():
#         fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
#                                        dict(text="<i>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
#     else:
#         fig.update_layout(margin={'l': 30, 'b': 30, 'r': 10, 't': 40},
#                           annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.32, x=1.2, align="left", showarrow=False)])
#
#     return fig
