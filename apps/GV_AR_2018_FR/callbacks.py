# Callbacks file for GV_AR_2018_FR converted from GAV0305_fr.py

import dash
from .data_processing import *
from .graphs import *


def register_callbacks(app):


    @app.callback(
        dash.dependencies.Output('ArtRecDonRateAvgDon', 'figure'),
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


    @app.callback(
        dash.dependencies.Output('ArtRecDonsCauses', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = ArtRecDonorsDonRates_2018[ArtRecDonorsDonRates_2018['Region'] == region]
        name1 = "Arts and recreation donors"
        name2 = "Non-arts and recreation donors"

        array = [
            "Sports &<br>Recreation",
            "Arts & culture",
            "Health",
            "Social services",
            "Religion",
            "Hospitals",
            "Education &<br>research",
            "Grant-making,<br>fundraising",
            "Environment",
            "International",
            "Law, advocacy &<br>politics",
            "Development &<br>housing",
            "Other",
            "Universities &<br>colleges",
            "Business &<br>professional"]
        title = '{}, {}'.format("Rates of donating to other causes", region)
        return vertical_percentage_graph(
            dff, title, name1, name2, sort=True, array=array)


    @app.callback(
        dash.dependencies.Output('ArtRecDonsMeth', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = ArtRecDonorsDonMeth_2018[ArtRecDonorsDonMeth_2018['Region'] == region]

        dff = dff.replace(
            'Arts and recreation donors',
            "Donateur.trice.s des arts et des loisirs")
        dff = dff.replace(
            "Non-arts and recreation donors",
            "Autres donateur.trice.s")
        # name1 = "Arts and recreation donors"
        # name2 = "Non-arts and recreation donors"
        name1 = "Donateur.trice.s des arts et des loisirs"
        name2 = "Autres donateur.trice.s"

        title = '{}, {}'.format("Taux de donateur.trice.s par méthode", region)
        return vertical_percentage_graph(dff, title, name1, name2)


    @app.callback(
        dash.dependencies.Output('ArtRecMotivations', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = ArtRecDonorsMotivations_2018[ArtRecDonorsMotivations_2018['Region'] == region]
        dff = dff.replace(
            'Arts and recreation donors',
            "Donateur.trice.s des arts et des loisirs")
        dff = dff.replace(
            "Non-arts and recreation donors",
            "Autres donateur.trice.s")
        # name1 = "Arts and recreation donors"
        # name2 = "Non-arts and recreation donors"
        name1 = "Donateur.trice.s des arts et des loisirs"
        name2 = "Autres donateur.trice.s"

        title = '{}, {}'.format("Motivations des dons", region)
        return vertical_percentage_graph(dff, title, name1, name2)


    @app.callback(
        dash.dependencies.Output('ArtRecBarriers', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = ArtRecDonorsBarriers_2018[ArtRecDonorsBarriers_2018['Region'] == region]
        dff = dff.replace(
            'Arts and recreation donors',
            "Donateur.trice.s des arts et des loisirs")
        dff = dff.replace(
            "Non-arts and recreation donors",
            "Autres donateur.trice.s")
        # name1 = "Arts and recreation donors"
        # name2 = "Non-arts and recreation donors"
        name1 = "Donateur.trice.s des arts et des loisirs"
        name2 = "Autres donateur.trice.s"

        title = '{}, {}'.format("Freins à donner plus", region)
        return vertical_percentage_graph(dff, title, name1, name2)


    @app.callback(
        dash.dependencies.Output('ArtReVolRateAvgHrs', 'figure'),
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
        dash.dependencies.Output('ArtRecHrsCauses', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = ArtRecVolsVolRates_2018[ArtRecVolsVolRates_2018['Region'] == region]
        dff = dff.replace(
            'Arts and recreation volunteer',
            'Arts and recreation volunteers')
        dff = dff.replace(
            'Non-arts and recreation volunteer',
            'Non-arts and recreation volunteers')
        name1 = "Arts and recreation volunteers"
        name2 = "Non-arts and recreation volunteers"

        title = '{}, {}'.format("Rates of volunteering for other causes", region)
        return vertical_percentage_graph(dff, title, name1, name2)


    @app.callback(
        dash.dependencies.Output('ArtRecVolActivity', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = ArtRecVolsActivities_2018[ArtRecVolsActivities_2018['Region'] == region]

        dff = dff.replace(
            "Arts and recreation volunteer",
            "Bénévoles des arts et loisirs")
        dff = dff.replace("Non-arts and recreation volunteer", "Autres bénévoles")
        # name1 = "Arts and recreation volunteer"
        # name2 = "Non-arts and recreation volunteer"
        name1 = "Bénévoles des arts et loisirs"
        name2 = "Autres bénévoles"

        title = '{}, {}'.format("Taux de bénévolat par activité", region)
        return vertical_percentage_graph(dff, title, name1, name2)


    @app.callback(
        dash.dependencies.Output('ArtRecVolMotivations', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = ArtRecVolsMotivations_2018[ArtRecVolsMotivations_2018['Region'] == region]
        dff = dff.replace(
            "Arts and recreation volunteer",
            "Bénévoles des arts et loisirs")
        dff = dff.replace("Non-arts and recreation volunteer", "Autres bénévoles")
        # name1 = "Arts and recreation volunteer"
        # name2 = "Non-arts and recreation volunteer"
        name1 = "Bénévoles des arts et loisirs"
        name2 = "Autres bénévoles"

        title = '{}, {}'.format("Motivations des bénévoles", region)
        return vertical_percentage_graph(dff, title, name1, name2)


    @app.callback(
        dash.dependencies.Output('ArtRecVolBarriers', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = ArtRecVolsBarriers_2018[ArtRecVolsBarriers_2018['Region'] == region]
        dff = dff.replace(
            "Arts and recreation volunteer",
            "Bénévoles des arts et loisirs")
        dff = dff.replace("Non-arts and recreation volunteer", "Autres bénévoles")
        # name1 = "Arts and recreation volunteer"
        # name2 = "Non-arts and recreation volunteer"
        name1 = "Bénévoles des arts et loisirs"
        name2 = "Autres bénévoles"
        # name1 = "Arts and recreation volunteer"
        # name2 = "Non-arts and recreation volunteer"

        title = '{}, {}'.format("Freins à faire plus de bénévolat", region)
        return vertical_percentage_graph(dff, title, name1, name2)


    @app.callback(
        dash.dependencies.Output('ArtRecDonRateDemo_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('demo-selection-don', 'value'),
        ])
    def update_graph(region, demo):
        dff = SubSecDonRatesFoc_2018[SubSecDonRatesFoc_2018['Region'] == region]
        dff = dff[dff['Group'] == demo]

        title = 'Taux de donateur.trice.s par {}, {}'.format(demo.lower(), region)

        return single_vertical_percentage_graph(dff, title)


    @app.callback(
        dash.dependencies.Output('ArtRecVolRateDemo_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('demo-selection-vol', 'value'),
        ])
    def update_graph(region, demo):
        dff = SubSecVolRatesFoc_2018[SubSecVolRatesFoc_2018['Region'] == region]
        dff = dff[dff['Group'] == demo]

        title = 'Taux de bénévoles par {}, {}'.format(demo.lower(), region)

        return single_vertical_percentage_graph(dff, title)
