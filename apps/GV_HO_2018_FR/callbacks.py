# Callbacks file for GV_HO_2018_FR converted from GAV0301_fr.py

import dash
from .data_processing import *
from .graphs import *


def register_callbacks(app):
    @app.callback(
        dash.dependencies.Output('DonRateAvgDon', 'figure'),
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

        # name2 = "Average donation"
        name2 = "Dons annuels moyens"

        title = '{}, {}'.format(
            "Taux de donateur.trice.s et montant moyen des dons selon la cause", region)

        return rate_avg_cause(dff1, dff2, name1, name2, title)

    @app.callback(
        dash.dependencies.Output('HealthDonRateDemo_fr', 'figure'),
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
        dash.dependencies.Output('HealthDonsCauses', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = HealthDonorsDonRates_2018[HealthDonorsDonRates_2018['Region'] == region]
        name1 = "Health donors"
        name2 = "Non-health donor"

        array = [
            "Health",
            "Hospitals",
            "Social services",
            "Religion",
            "Sports &<br>recreation",
            "Education &<br>research",
            "Grant-making,<br>fundraising",
            "International",
            "Environment",
            "Law, advocacy &<br>politics",
            "Arts & culture",
            "Development &<br>housing",
            "Other",
            "Universities &<br>colleges",
            "Business &<br>professional"]
        title = '{}, {}'.format("Rates of donating to other causes", region)
        return vertical_percentage_graph(
            dff, title, name1, name2, sort=True, array=array)

    @app.callback(
        dash.dependencies.Output('HealthDonsMeth', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = HealthDonorsDonMeth_2018[HealthDonorsDonMeth_2018['Region'] == region]
        dff = dff.replace('Health donors', 'Donateur.trice.s de la santé')
        dff = dff.replace("Non-health donors", 'Autres donateur.trice.s')
        # name1 = "Health donors"
        # name2 = "Non-health donors"
        name1 = 'Donateur.trice.s de la santé'
        name2 = 'Autres donateur.trice.s'

        title = '{}, {}'.format("Taux de donateur.trice.s par méthode", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('HealthMotivations', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = HealthDonorsMotivations_2018[HealthDonorsMotivations_2018['Region'] == region]
        dff = dff.replace('Health donors', 'Donateur.trice.s de la santé')
        dff = dff.replace("Non-health donors", 'Autres donateur.trice.s')
        # name1 = "Health donors"
        # name2 = "Non-health donors"
        name1 = 'Donateur.trice.s de la santé'
        name2 = 'Autres donateur.trice.s'

        title = '{}, {}'.format("Motivations des dons", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('HealthBarriers', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = HealthDonorsBarriers_2018[HealthDonorsBarriers_2018['Region'] == region]

        dff = dff.replace('Health donors', 'Donateur.trice.s de la santé')
        dff = dff.replace("Non-health donors", 'Autres donateur.trice.s')
        # name1 = "Health donors"
        # name2 = "Non-health donors"
        name1 = 'Donateur.trice.s de la santé'
        name2 = 'Autres donateur.trice.s'

        title = '{}, {}'.format("Freins à donner plus", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('VolRateAvgHrs', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff1 = SubSecVolRates_2018[SubSecVolRates_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "All"]
        dff1 = dff1.replace('Volunteer rate', 'Taux de bénévolat')
        # name1 = "Volunteer rate"
        name1 = 'Taux de bénévolat'

        dff2 = SubSecAvgHrs_2018[SubSecAvgHrs_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "All"]
        dff2 = dff2.replace('Average hours', "Nombre d'heures moyen")
        # name2 = "Average hours"
        name2 = "Nombre d'heures moyen"

        title = '{}, {}'.format(
            "Taux de bénévoles et nombre moyen d’heures de bénévolat selon la cause",
            region)

        return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)

    @app.callback(
        dash.dependencies.Output('HealthVolRateDemo_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('demo-selection-vol', 'value'),
        ])
    def update_graph(region, demo):
        dff = SubSecVolRatesFoc_2018[SubSecVolRatesFoc_2018['Region'] == region]
        dff = dff[dff['Group'] == demo]

        title = 'Taux de bénévoles par {}, {}'.format(demo.lower(), region)

        return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('HealthHrsCauses', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = HealthVolsVolRates_2018[HealthVolsVolRates_2018['Region'] == region]
        name1 = "Health volunteer"
        name2 = "Non-health volunteer"

        title = '{}, {}'.format(
            "Rates of volunteering for other causes", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('HealthVolActivity', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = HealthVolsActivities_2018[HealthVolsActivities_2018['Region'] == region]

        dff = dff.replace("Health volunteer", "Bénévoles de la santé")
        dff = dff.replace("Non-health volunteer", "Autres bénévoles")
        name1 = "Bénévoles de la santé"
        name2 = "Autres bénévoles"
        # name1 = "Health volunteer"
        # name2 = "Non-health volunteer"

        title = '{}, {}'.format("Taux de bénévoles par activité", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('HealthVolMotivations', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = HealthVolsMotivations_2018[HealthVolsMotivations_2018['Region'] == region]

        dff = dff.replace("Health volunteer", "Bénévoles de la santé")
        dff = dff.replace("Non-health volunteer", "Autres bénévoles")
        name1 = "Bénévoles de la santé"
        name2 = "Autres bénévoles"
        # name1 = "Health volunteer"
        # name2 = "Non-health volunteer"

        title = '{}, {}'.format("Motivations du bénévolat", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('HealthVolBarriers', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = HealthVolsBarriers_2018[HealthVolsBarriers_2018['Region'] == region]

        dff = dff.replace("Health volunteer", "Bénévoles de la santé")
        dff = dff.replace("Non-health volunteer", "Autres bénévoles")
        name1 = "Bénévoles de la santé"
        name2 = "Autres bénévoles"
        # name1 = "Health volunteer"
        # name2 = "Non-health volunteer"

        title = '{}, {}'.format("Freins à faire plus de bénévolat", region)
        return vertical_percentage_graph(dff, title, name1, name2)
