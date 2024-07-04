# Callbacks file for GV_SS_2018_FR converted from GAV0304_fr.py

import dash
from .data_processing import *
from .graphs import *


def register_callbacks(app):

    @app.callback(
        dash.dependencies.Output('SocSerDonRateAvgDon', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff1 = SubSecDonRates_2018[SubSecDonRates_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "All"]

        dff1 = dff1.replace("Donation rate", "Taux de donateur.trice.s")
        # name1 = "Donation rate"
        name1 = "Taux de donateur.trice.s"

        dff2 = SubSecAvgDon_2018[SubSecAvgDon_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "All"]

        dff2 = dff2.replace("Average donation", "Dons annuels moyens")
    #     name2 = "Average donation"
        name2 = "Dons annuels moyens"

        title = '{}, {}'.format(
            "Taux et montant moyen des dons selon la cause", region)

        return rate_avg_cause(dff1, dff2, name1, name2, title)

    # @app.callback(
    #     dash.dependencies.Output('SocSerDonRateAvgDon', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     dff1 = SubSecDonRates_2018[SubSecDonRates_2018['Region'] == region]
    #     # dff1 = dff1.replace("Donation rate", "Taux de donateur.trice.s")
    #     name1 = "Donation rate"
    #     # name1 = "Taux de donateur.trice.s"

    #     dff2 = SubSecAvgDon_2018[SubSecAvgDon_2018['Region'] == region]
    #     # dff2 = dff2.replace("Average donation", "Dons annuels moyens")
    #     name2 = "Average donation"
    #     # name2 = "Dons annuels moyens"

    #     title = '{}, {}'.format("Taux et montant moyen des dons selon la cause", region)

    #     return rate_avg_cause(dff1, dff2, name1, name2, title)

    @app.callback(
        dash.dependencies.Output('SocSerDonsCauses', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = SocSerDonorsDonRates_2018[SocSerDonorsDonRates_2018['Region'] == region]
        dff = dff.replace(
            "Social services donor",
            "Donateur.trice.s des services sociaux")
        dff = dff.replace(
            "Non-social services donor",
            "Autres donateur.trice.s")

        # name1 = "Social services donor"
        # name2 = "Non-social services donor"
        name1 = "Donateur.trice.s des services sociaux"
        name2 = "Autres donateur.trice.s"

        title = '{}, {}'.format("Rates of donating to other causes", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('SocSerDonsMeth', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = SocSerDonorsDonMeth_2018[SocSerDonorsDonMeth_2018['Region'] == region]
        dff = dff.replace(
            "Social services donors",
            "Donateur.trice.s des services sociaux")
        dff = dff.replace(
            "Non-social services donors",
            "Autres donateur.trice.s")

        # name1 = "Social services donor"
        # name2 = "Non-social services donor"
        name1 = "Donateur.trice.s des services sociaux"
        name2 = "Autres donateur.trice.s"

        title = '{}, {}'.format("Taux de donateur.trice.s par méthode", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('SocSerMotivations', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = SocSerDonorsMotivations_2018[SocSerDonorsMotivations_2018['Region'] == region]
        dff = dff.replace(
            "Social services donors",
            "Donateur.trice.s des services sociaux")
        dff = dff.replace(
            "Non-social services donors",
            "Autres donateur.trice.s")

        # name1 = "Social services donor"
        # name2 = "Non-social services donor"
        name1 = "Donateur.trice.s des services sociaux"
        name2 = "Autres donateur.trice.s"

        title = '{}, {}'.format("Motivations des dons", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('SocSerBarriers', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = SocSerDonorsBarriers_2018[SocSerDonorsBarriers_2018['Region'] == region]
        dff = dff.replace(
            "Social services donors",
            "Donateur.trice.s des services sociaux")
        dff = dff.replace(
            "Non-social services donors",
            "Autres donateur.trice.s")

        # name1 = "Social services donor"
        # name2 = "Non-social services donor"
        name1 = "Donateur.trice.s des services sociaux"
        name2 = "Autres donateur.trice.s"

        title = '{}, {}'.format("Freins à donner plus", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    # @app.callback(
    #     dash.dependencies.Output('SocSerVolRateAvgHrs', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     dff1 = SubSecVolRates_2018[SubSecVolRates_2018['Region'] == region]
    #     dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")
    #     # name1 = "Volunteer rate"
    #     name1 = "Taux de bénévolat"

    #     dff2 = SubSecAvgHrs_2018[SubSecAvgHrs_2018['Region'] == region]
    #     dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
    #     # name2 = "Average hours"
    #     name2 = "Nombre d'heures moyen"

    #     title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures de bénévolat selon la cause", region)

    #     return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)

    @app.callback(
        dash.dependencies.Output('SocSerVolRateAvgHrs', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff1 = SubSecVolRates_2018[SubSecVolRates_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "All"]
        dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")
    #     # name1 = "Volunteer rate"
        name1 = "Taux de bénévolat"

        dff2 = SubSecAvgHrs_2018[SubSecAvgHrs_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "All"]
        dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
    #     # name2 = "Average hours"
        name2 = "Nombre d'heures moyen"

        title = '{}, {}'.format(
            "Taux de bénévolat et nombre moyen d’heures de bénévolat selon la cause",
            region)

        return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)

    @app.callback(
        dash.dependencies.Output('SocSerHrsCauses', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = SocSerVolsVolRates_2018[SocSerVolsVolRates_2018['Region'] == region]
        name1 = "Donateur.trice.s des services sociaux"
        name2 = "Autres donateur.trice.s"

        title = '{}, {}'.format(
            "Rates of volunteering for other causes", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('SocSerVolActivity', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = SocSerVolsActivities_2018[SocSerVolsActivities_2018['Region'] == region]
        dff = dff.replace(
            "Social services volunteer",
            "Bénévoles des services sociaux")
        dff = dff.replace("Non-social services volunteer", "Autres bénévoles")
        name1 = "Bénévoles des services sociaux"
        name2 = "Autres bénévoles"

        title = '{}, {}'.format("Taux de bénévolat par activité", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('SocSerVolMotivations', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = SocSerVolsMotivations_2018[SocSerVolsMotivations_2018['Region'] == region]
        dff = dff.replace(
            "Social services volunteer",
            "Bénévoles des services sociaux")
        dff = dff.replace("Non-social services volunteer", "Autres bénévoles")
        name1 = "Bénévoles des services sociaux"
        name2 = "Autres bénévoles"

        title = '{}, {}'.format("Motivations des bénévoles", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('SocSerVolBarriers', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = SocSerVolsBarriers_2018[SocSerVolsBarriers_2018['Region'] == region]
        dff = dff.replace(
            "Social services volunteer",
            "Bénévoles des services sociaux")
        dff = dff.replace("Non-social services volunteer", "Autres bénévoles")
        name1 = "Bénévoles des services sociaux"
        name2 = "Autres bénévoles"

        title = '{}, {}'.format("Freins à faire plus de bénévolat", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('SocSerDonRateDemo_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('demo-selection-don', 'value'),
        ])
    def update_graph(region, demo):
        dff = SubSecDonRatesFoc_2018[SubSecDonRatesFoc_2018['Region'] == region]
        dff = dff[dff['Group'] == demo]

        title = 'Taux de donateur.trice.s par {}, {}'.format(
            demo.lower(), region)

        return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('SocSerVolRateDemo_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('demo-selection-vol', 'value'),
        ])
    def update_graph(region, demo):
        dff = SubSecVolRatesFoc_2018[SubSecVolRatesFoc_2018['Region'] == region]
        dff = dff[dff['Group'] == demo]

        title = 'Taux de bénévoles par {}, {}'.format(demo.lower(), region)

        return single_vertical_percentage_graph(dff, title)
