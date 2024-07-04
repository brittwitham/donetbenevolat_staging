# CALLBACKS file for GV_YO_2018_FR converted from
# les_dons_et_le_benevolat_des_jeunes_2018.py

import dash
from .data_processing import *
from .graphs import *


def register_callbacks(app):

    @app.callback(
        dash.dependencies.Output('YouthDonRateAmt', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff1 = YouthDonRates_2018[YouthDonRates_2018['Region'] == region]
        dff1 = dff1[dff1["Group"] == "Younger"]

        dff2 = YouthAvgDonAmt_2018[YouthAvgDonAmt_2018['Region'] == region]
        dff2 = dff2[dff2["Group"] == "Younger"]

        # name1 = "15 to 24"
        # name2 = "25 to 34"
        # name3 = ">=35"
        name1 = "15 à 24 ans"
        name2 = "25 à 34 ans"
        name3 = ">=35"

        title = '{}, {}'.format(
            "Taux des dons laïcs et religieux totaux et montant moyen des dons", region)
        return triple_horizontal_rate_avg(
            dff1, dff2, name1, name2, name3, title, "dollar")

    @app.callback(
        dash.dependencies.Output('YouthDonRateByCause', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = YouthDonRateByCause_2018[YouthDonRateByCause_2018['Region'] == region]
        dff = dff[dff["Group"] == "Younger2"]
        # name1 = "15 to 34"
        name1 = "15 à 34 ans"
        name2 = ">=35"
        title = '{}, {}'.format("Taux de dons par cause", region)
        return vertical_double_graph(dff, title, name1, name2, "percent")

    @app.callback(
        dash.dependencies.Output('YouthAvgAmtByCause', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = YouthAvgDonByCause_2018[YouthAvgDonByCause_2018['Region'] == region]
        dff = dff[dff["Group"] == "Younger2"]
        # name1 = "15 to 34"
        name1 = "15 à 34 ans"
        name2 = ">=35"
        title = '{}, {}'.format(
            "Montant moyen des dons selon la cause", region)
        return vertical_double_graph(dff, title, name1, name2, "dollar")

    @app.callback(
        dash.dependencies.Output('YouthDonRateByMeth', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = YouthDonRateByMeth_2018[YouthDonRateByMeth_2018['Region'] == region]
        dff = dff[dff["Group"] == "Younger2"]
        # name1 = "15 to 34"
        name1 = "15 à 34 ans"
        name2 = ">=35"
        title = '{}, {}'.format("Taux de dons par méthode", region)
        return vertical_double_graph(dff, title, name1, name2, "percent")

    @app.callback(
        dash.dependencies.Output('YouthAvgAmtByMeth', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = YouthAvgDonByMeth_2018[YouthAvgDonByMeth_2018['Region'] == region]
        dff = dff[dff["Group"] == "Younger2"]
        # name1 = "15 to 34"
        name1 = "15 à 34 ans"
        name2 = ">=35"
        title = '{}, {}'.format("Montant moyen des dons par méthode", region)
        return vertical_double_graph(dff, title, name1, name2, "dollar")

    @app.callback(
        dash.dependencies.Output('YouthMotivations', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = YouthReasonsGiving_2018[YouthReasonsGiving_2018['Region'] == region]
        dff = dff[dff["Group"] == "Younger"]
        # name1 = "15 to 24"
        # name2 = "25 to 34"
        # name3 = ">=35"
        name1 = "15 à 24 ans"
        name2 = "25 à 34 ans"
        name3 = ">=35"
        title = '{}, {}'.format("Motivations des dons", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "percent")

    @app.callback(
        dash.dependencies.Output('YouthBarriers', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = YouthBarriers_2018[YouthBarriers_2018['Region'] == region]
        dff = dff[dff["Group"] == "Younger"]
        # name1 = "15 to 24"
        # name2 = "25 to 34"
        # name3 = ">=35"
        name1 = "15 à 24 ans"
        name2 = "25 à 34 ans"
        name3 = ">=35"
        title = '{}, {}'.format("Freins à donner davantage", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "percent")

    @app.callback(
        dash.dependencies.Output('YouthEfficiency', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = YouthEfficiencyConcerns_2018[YouthEfficiencyConcerns_2018['Region'] == region]
        dff = dff[dff["Group"] == "Younger2"]
        # name1 = "15 to 34"
        name1 = "15 à 34 ans"
        name2 = ">=35"
        title = '{}, {}'.format(
            "Raisons des préoccupations relatives à l’efficience", region)
        return vertical_double_graph(dff, title, name1, name2, "percent")

    @app.callback(
        dash.dependencies.Output('YouthSolicitations', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = YouthSolicitationConcerns_2018[YouthSolicitationConcerns_2018['Region'] == region]
        dff = dff[dff["Group"] == "Younger2"]
        # name1 = "15 to 34"
        name1 = "15 à 34 ans"
        name2 = ">=35"
        title = '{}, {}'.format(
            "Raisons de l’aversion pour les sollicitations", region)
        return vertical_double_graph(dff, title, name1, name2, "percent")

    @app.callback(
        dash.dependencies.Output('YouthVolRateVolAmt', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff1 = YouthVolRate_2018[YouthVolRate_2018['Region'] == region]
        dff1 = dff1[dff1["Group"] == "Younger"]

        dff2 = YouthAvgHrs_2018[YouthAvgHrs_2018['Region'] == region]
        dff2 = dff2[dff2["Group"] == "Younger"]

        # name1 = "15 to 24"
        # name2 = "25 to 34"
        # name3 = ">=35"
        name1 = "15 à 24 ans"
        name2 = "25 à 34 ans"
        name3 = ">=35"
        title = '{}, {}'.format(
            "Taux et nombre moyen d’heures consacrées au bénévolat, à l’aide d’autrui<br>et à l’engagement communautaire",
            region)
        return triple_horizontal_rate_avg(
            dff1, dff2, name1, name2, name3, title, giving=False)

    @app.callback(
        dash.dependencies.Output('YouthVolRateByCause', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = YouthVolRateByCause_2018[YouthVolRateByCause_2018['Region'] == region]
        dff = dff[dff["Group"] == "Younger2"]
        # name1 = "15 to 34"
        name1 = "15 à 34 ans"
        name2 = ">=35"
        title = '{}, {}'.format("Taux de bénévoles selon la cause", region)
        return vertical_double_graph(dff, title, name1, name2, "percent")

    @app.callback(
        dash.dependencies.Output('YouthAvgHrsByCause', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = YouthAvgHrsByCause_2018[YouthAvgHrsByCause_2018['Region'] == region]
        dff = dff[dff["Group"] == "Younger2"]
        # name1 = "15 to 34"
        name1 = "15 à 34 ans"
        name2 = ">=35"
        title = '{}, {}'.format(
            "Nombre moyen d’heures de bénévolat selon la cause", region)
        return vertical_double_graph(dff, title, name1, name2, "hours")

    @app.callback(
        dash.dependencies.Output('YouthVolRateByActivity', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = YouthVolRateByActivity_2018[YouthVolRateByActivity_2018['Region'] == region]
        dff = dff[dff["Group"] == "Younger2"]
        # name1 = "15 to 34"
        name1 = "15 à 34 ans"
        name2 = ">=35"
        title = '{}, {}'.format("Taux de bénévoles par activité", region)
        return vertical_double_graph(dff, title, name1, name2, "percent")

    @app.callback(
        dash.dependencies.Output('YouthAvgHrsByActivity', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = YouthAvgHrsByActivity_2018[YouthAvgHrsByActivity_2018['Region'] == region]
        dff = dff[dff["Group"] == "Younger2"]
        dff = dff[dff["Group"] == "Younger2"]
        # name1 = "15 to 34"
        name1 = "15 à 34 ans"
        name2 = ">=35"
        title = '{}, {}'.format(
            "Nombre moyen d’heures de bénévolat par activité", region)
        return vertical_double_graph(dff, title, name1, name2, "hours")

    @app.callback(
        dash.dependencies.Output('YouthVolMotivations', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = YouthReasonsVol_2018[YouthReasonsVol_2018['Region'] == region]
        dff = dff[dff["Group"] == "Younger"]
        # name1 = "15 to 24"
        # name2 = "25 to 34"
        # name3 = ">=35"
        name1 = "15 à 24 ans"
        name2 = "25 à 34 ans"
        name3 = ">=35"
        title = '{}, {}'.format("Motivations du bénévolat", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "percent")

    @app.callback(
        dash.dependencies.Output('YouthVolBarriers', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = YouthBarriersVol_2018[YouthBarriersVol_2018['Region'] == region]
        dff = dff[dff["Group"] == "Younger"]
        # name1 = "15 to 24"
        # name2 = "25 to 34"
        # name3 = ">=35"
        name1 = "15 à 24 ans"
        name2 = "25 à 34 ans"
        name3 = ">=35"
        title = '{}, {}'.format("Freins à faire plus de bénévolat", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "percent")

    @app.callback(
        dash.dependencies.Output('YouthRateHelpDirect', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = YouthHelpDirectlyRate_2018[YouthHelpDirectlyRate_2018['Region'] == region]
        dff = dff[dff["Group"] == "Younger"]
        # name1 = "15 to 24"
        # name2 = "25 to 34"
        # name3 = ">=35"
        name1 = "15 à 24 ans"
        name2 = "25 à 34 ans"
        name3 = ">=35"
        title = '{}, {}'.format("Méthodes d’aide directe d’autrui", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "percent")

    @app.callback(
        dash.dependencies.Output('YouthHrsHelpDirect', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = YouthAvgHrsHelpDirectly_2018[YouthAvgHrsHelpDirectly_2018['Region'] == region]
        dff = dff[dff["Group"] == "Younger2"]
        # name1 = "15 to 34"
        name1 = "15 à 34 ans"
        name2 = ">=35"
        title = '{}, {}'.format(
            "Nombre moyen d’heures consacrées à l’aide directe d’autrui", region)
        return vertical_double_graph(dff, title, name1, name2, "hours")

    @app.callback(
        dash.dependencies.Output('YouthRateCommInvolve', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = YouthCommInvolveRate_2018[YouthCommInvolveRate_2018['Region'] == region]
        dff = dff[dff["Group"] == "Younger"]
        # name1 = "15 to 24"
        # name2 = "25 to 34"
        # name3 = ">=35"
        name1 = "15 à 24 ans"
        name2 = "25 à 34 ans"
        name3 = ">=35"
        title = '{}, {}'.format("Types d’engagement communautaire", region)
        return triple_vertical_graphs_pops(
            dff, title, name1, name2, name3, "percent")

    @app.callback(
        dash.dependencies.Output('YouthHrsCommInvolve', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = YouthAvgHrsCommInvolve_2018[YouthAvgHrsCommInvolve_2018['Region'] == region]
        dff = dff[dff["Group"] == "Younger2"]
        # name1 = "15 to 34"
        name1 = "15 à 34 ans"
        name2 = ">=35"
        title = '{}, {}'.format(
            "Nombre moyen d’heures consacrées aux formes d’engagement communautaire",
            region)
        return vertical_double_graph(dff, title, name1, name2, "hours")

    if __name__ == '__main__':
        app.run_server(debug=True)
