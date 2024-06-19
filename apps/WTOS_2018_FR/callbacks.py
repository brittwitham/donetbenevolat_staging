# CALLBACKS file for WTOS_2018_FR converted from
# Quels_types_organismes_soutient_on_au_Canada_2018.py

import dash
from .data_processing import *
from .graphs import *


def register_callbacks(app):
    @app.callback(

        dash.dependencies.Output('DonRateAvgDonAmt-Cause', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):

        dff2 = SubSecDonRates_2018[SubSecDonRates_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "All"]
        dff2 = dff2.replace('Donation rate', 'Taux de donateur.trice.s')
        # name1 = "Donation rate"
        name1 = "Taux de donateur.trice.s"

        dff1 = SubSecAvgDon_2018[SubSecAvgDon_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "All"]
        dff1 = dff1.replace('Average donation', 'Dons annuels moyens')
        # name2 = "Average donation"
        name2 = 'Dons annuels moyens'

        title = '{}, {}'.format("Niveaux de soutien par cause", region)

        return rate_avg_cause(dff1, dff2, name1, name2, title)

    @app.callback(

        dash.dependencies.Output('AllocationSupport-Cause', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):

        dff = Allocation_2018[Allocation_2018['Region'] == region]
        title = '{}, {}'.format("Répartition du soutien par cause", region)

        return single_vertical_percentage_graph(
            dff, title, by="QuestionText", sort=True)
