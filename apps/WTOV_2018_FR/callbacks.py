# CALLBACKS file for WTOV_2018_FR converted from
# A_quels_types_organismes_fait_on_don_de_son_temps_au_Canada_2018.py

import dash
from .data_processing import *
from .graphs import *


def register_callbacks(app):
    @app.callback(

        dash.dependencies.Output('DonRateAvgDonAmt-Cause-2', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):

        dff1 = SubSecVolRates_2018[SubSecVolRates_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "All"]
        dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")
        # name1 = "Volunteer rate"
        name1 = "Taux de bénévolat"

        dff2 = SubSecAvgHrs_2018[SubSecAvgHrs_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "All"]
        dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
        # name2 = "Average hours"
        name2 = "Nombre d'heures moyen"

        title = '{}, {}'.format("Niveaux de soutien par cause", region)

        return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)

    @app.callback(

        dash.dependencies.Output('AllocationSupport-Cause-2', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):

        dff = AllocationVol_2018[AllocationVol_2018['Region'] == region]
        title = '{}, {}'.format("Répartition du soutien par cause", region)

        return single_vertical_percentage_graph(
            dff, title, by="QuestionText", sort=True)
