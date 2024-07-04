# Callbacks file for GV_RO_2018_FR converted from GAV0302_fr.py

import dash
from .data_processing import *
from .graphs import *


def register_callbacks(app):
    # @app.callback(
    #     dash.dependencies.Output('DonRateAvgDon-2', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     dff1 = SubSecDonRates_2018[SubSecDonRates_2018['Region'] == region]
    #     dff1 = dff1[dff1['Group'] == "All"]
    #     name1 = "Donation rate"

    #     dff2 = SubSecAvgDon_2018[SubSecAvgDon_2018['Region'] == region]
    #     dff2 = dff2[dff2['Group'] == "All"]
    #     name2 = "Average donation"

    #     title = '{}, {}'.format("Donation rate and average donation amount by cause", region)

    #     return rate_avg_cause(dff1, dff2, name1, name2, title)

    # @app.callback(
    #     dash.dependencies.Output('HealthDonsCauses-2', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     dff = HealthDonorsDonRates_2018[HealthDonorsDonRates_2018['Region'] == region]
    #     name1 = "Health donors"
    #     name2 = "Non-health donor"

    #     array = ["Health", "Hospitals", "Social services", "Religion",
    #              "Sports &<br>recreation", "Education &<br>research", "Grant-making,<br>fundraising",
    #              "International", "Environment", "Law, advocacy &<br>politics", "Arts & culture",
    #              "Development &<br>housing", "Other", "Universities &<br>colleges", "Business &<br>professional"]
    #     title = '{}, {}'.format("Rates of donating to other causes", region)
    # return vertical_percentage_graph(dff, title, name1, name2, sort=True,
    # array=array)

    # @app.callback(
    #     dash.dependencies.Output('HealthDonsMeth-2', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     dff = HealthDonorsDonMeth_2018[HealthDonorsDonMeth_2018['Region'] == region]
    #     # dff = ReligionDonorsDonMeth_2018[ReligionDonorsDonMeth_2018['Region'] == region]
    #     # name1 = "Health donors"
    #     # name2 = "Non-health donors"
    #     # name1 = 'Religion donors'
    #     # name2 = 'Non-religion donors'
    #     name1 = dff.Attribute.unique()[1]
    #     name2 = dff.Attribute.unique()[0]

    #     title = '{}, {}'.format("Donation rate by method", region)
    #     return vertical_percentage_graph(dff, title, name1, name2)

    # @app.callback(
    #     dash.dependencies.Output('HealthMotivations-2', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     dff = HealthDonorsMotivations_2018[HealthDonorsMotivations_2018['Region'] == region]
    #     name1 = "Health donors"
    #     name2 = "Non-health donors"

    #     title = '{}, {}'.format("Motivations for donating", region)
    #     return vertical_percentage_graph(dff, title, name1, name2)

    # @app.callback(
    #     dash.dependencies.Output('HealthBarriers-2', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     dff = HealthDonorsBarriers_2018[HealthDonorsBarriers_2018['Region'] == region]
    #     name1 = "Health donors"
    #     name2 = "Non-health donors"

    #     title = '{}, {}'.format("Barriers to donating more", region)
    #     return vertical_percentage_graph(dff, title, name1, name2)

    # @app.callback(
    #     dash.dependencies.Output('VolRateAvgHrs-2', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     dff1 = SubSecVolRates_2018[SubSecVolRates_2018['Region'] == region]
    #     dff1 = dff1[dff1['Group'] == "All"]
    #     name1 = "Volunteer rate"

    #     dff2 = SubSecAvgHrs_2018[SubSecAvgHrs_2018['Region'] == region]
    #     dff2 = dff2[dff2['Group'] == "All"]
    #     name2 = "Average hours"

    #     title = '{}, {}'.format("Volunteer rate and average hours volunteered by cause", region)

    #     return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)

    # @app.callback(
    #     dash.dependencies.Output('HealthHrsCauses-2', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     dff = HealthVolsVolRates_2018[HealthVolsVolRates_2018['Region'] == region]
    #     name1 = "Health volunteer"
    #     name2 = "Non-health volunteer"

    #     title = '{}, {}'.format("Rates of volunteering for other causes", region)
    #     return vertical_percentage_graph(dff, title, name1, name2)

    # @app.callback(
    #     dash.dependencies.Output('HealthVolActivity-2', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     dff = HealthVolsActivities_2018[HealthVolsActivities_2018['Region'] == region]
    #     name1 = "Health volunteer"
    #     name2 = "Non-health volunteer"

    #     title = '{}, {}'.format("Volunteer rate by activity", region)
    #     return vertical_percentage_graph(dff, title, name1, name2)

    # @app.callback(
    #     dash.dependencies.Output('HealthVolMotivations-2', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     dff = HealthVolsMotivations_2018[HealthVolsMotivations_2018['Region'] == region]
    #     name1 = "Health volunteer"
    #     name2 = "Non-health volunteer"

    #     title = '{}, {}'.format("Motivations for volunteering", region)
    #     return vertical_percentage_graph(dff, title, name1, name2)

    # @app.callback(
    #     dash.dependencies.Output('HealthVolBarriers-2', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     dff = HealthVolsBarriers_2018[HealthVolsBarriers_2018['Region'] == region]
    #     name1 = "Health volunteer"
    #     name2 = "Non-health volunteer"

    #     title = '{}, {}'.format("Barriers to volunteering more", region)
    #     return vertical_percentage_graph(dff, title, name1, name2)

    # __________________________

    # @app.callback(
    #     dash.dependencies.Output('ReligionDonsMeth', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     dff = ReligionDonorsDonMeth_2018[ReligionDonorsDonMeth_2018['Region'] == region]
    #     name1 = "Religion donors"
    #     name2 = "Non-religion donors"

    #     title = '{}, {}'.format("Donation rate by method", region)
    #     return vertical_percentage_graph(dff, title, name1, name2)

    # @app.callback(
    #     dash.dependencies.Output('ReligionVolMotivations', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     dff = ReligionVolsMotivations_2018[ReligionVolsMotivations_2018['Region'] == region]
    #     # name1 = "Religion volunteer"
    #     # name2 = "Non-religion volunteer"
    #     name1 = dff.Attribute.unique()[1]
    #     name2 = dff.Attribute.unique()[0]

    #     title = '{}, {}'.format("Motivations for volunteering", region)
    #     return vertical_percentage_graph(dff, title, name1, name2)

    # @app.callback(
    #     dash.dependencies.Output('ReligionVolBarriers', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     dff = ReligionVolsBarriers_2018[ReligionVolsBarriers_2018['Region'] == region]
    #     name1 = "Religion volunteer"
    #     name2 = "Non-religion volunteer"

    #     title = '{}, {}'.format("Barriers to volunteering more", region)
    #     return vertical_percentage_graph(dff, title, name1, name2)

    # @app.callback(
    #     dash.dependencies.Output('ReligionBarriers', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     dff = ReligionDonorsBarriers_2018[ReligionDonorsBarriers_2018['Region'] == region]
    #     name1 = "Religion donors"
    #     name2 = "Non-religion donors"

    #     title = '{}, {}'.format("Barriers to donating more", region)
    #     return vertical_percentage_graph(dff, title, name1, name2)

    # @app.callback(
    #     dash.dependencies.Output('ReligionMotivations', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     dff = ReligionDonorsMotivations_2018[ReligionDonorsMotivations_2018['Region'] == region]
    #     name1 = "Religion donors"
    #     name2 = "Non-religion donors"

    #     title = '{}, {}'.format("Motivations for donating", region)
    #     return vertical_percentage_graph(dff, title, name1, name2)

    # @app.callback(
    #     dash.dependencies.Output('ReligionBarriers2', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     dff = ReligionDonorsBarriers_2018[ReligionDonorsBarriers_2018['Region'] == region]
    #     name1 = "Religion donors"
    #     name2 = "Non-religion donors"

    #     title = '{}, {}'.format("Barriers to donating more", region)
    #     return vertical_percentage_graph(dff, title, name1, name2)

    # @app.callback(
    #     dash.dependencies.Output('ReligionVolActivity', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     dff = ReligionVolsActivities_2018[ReligionVolsActivities_2018['Region'] == region]
    #     name1 = "Religion volunteer"
    #     name2 = "Non-religion volunteer"

    #     title = '{}, {}'.format("Volunteer rate by activity", region)
    #     return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('DonRateAvgDon2', 'figure'),
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
        dash.dependencies.Output('ReligionDonsCauses', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = ReligionDonorsDonRates_2018[ReligionDonorsDonRates_2018['Region'] == region]
        name1 = "Religion donor"
        name2 = "Non-religion donor"

        title = '{}, {}'.format("Rates of donating to other causes", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('ReligionDonsMeth', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = ReligionDonorsDonMeth_2018[ReligionDonorsDonMeth_2018['Region'] == region]
        dff = dff.replace("Religion donors", "Donateur.trice.s de la religion")
        dff = dff.replace("Non-religion donors", "Autres donateur.trice.s")
        # name1 = "Religion donors"
        # name2 = "Non-religion donors"
        name1 = "Donateur.trice.s de la religion"
        name2 = "Autres donateur.trice.s"

        title = '{}, {}'.format("Taux de donateur.trice.s par méthode", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('ReligionMotivations', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = ReligionDonorsMotivations_2018[ReligionDonorsMotivations_2018['Region'] == region]
        dff = dff.replace("Religion donors", "Donateur.trice.s de la religion")
        dff = dff.replace("Non-religion donors", "Autres donateur.trice.s")
        # name1 = "Religion donors"
        # name2 = "Non-religion donors"
        name1 = "Donateur.trice.s de la religion"
        name2 = "Autres donateur.trice.s"

        title = '{}, {}'.format("Motivations des dons", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('ReligionBarriers', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = ReligionDonorsBarriers_2018[ReligionDonorsBarriers_2018['Region'] == region]
        dff = dff.replace("Religion donors", "Donateur.trice.s de la religion")
        dff = dff.replace("Non-religion donors", "Autres donateur.trice.s")
        # name1 = "Religion donors"
        # name2 = "Non-religion donors"
        name1 = "Donateur.trice.s de la religion"
        name2 = "Autres donateur.trice.s"

        title = '{}, {}'.format("Freins à donner plus", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('VolRateAvgHrs2', 'figure'),
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

        title = '{}, {}'.format(
            "Taux de bénévolat et nombre moyen d’heures de bénévolat selon la cause",
            region)

        return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)

    @app.callback(
        dash.dependencies.Output('ReligionHrsCauses', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = ReligionVolsVolRates_2018[ReligionVolsVolRates_2018['Region'] == region]
        name1 = "Religion volunteer"
        name2 = "Non-religion volunteer"

        title = '{}, {}'.format(
            "Rates of volunteering for other causes", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('ReligionVolActivity', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = ReligionVolsActivities_2018[ReligionVolsActivities_2018['Region'] == region]
        dff = dff.replace("Religion volunteer", "Bénévoles de la religion")
        dff = dff.replace("Non-religion volunteer", "Autres bénévoles")

        # name1 = "Religion volunteer"
        # name2 = "Non-religion volunteer"
        name1 = "Bénévoles de la religion"
        name2 = "Autres bénévoles"

        title = '{}, {}'.format("Taux de bénévolat par activité", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('ReligionVolMotivations', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = ReligionVolsMotivations_2018[ReligionVolsMotivations_2018['Region'] == region]
        dff = dff.replace("Religion volunteer", "Bénévoles de la religion")
        dff = dff.replace("Non-religion volunteer", "Autres bénévoles")

        # name1 = "Religion volunteer"
        # name2 = "Non-religion volunteer"
        name1 = "Bénévoles de la religion"
        name2 = "Autres bénévoles"

        title = '{}, {}'.format("Motivations des bénévoles", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('ReligionVolBarriers', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = ReligionVolsBarriers_2018[ReligionVolsBarriers_2018['Region'] == region]
        dff = dff.replace("Religion volunteer", "Bénévoles de la religion")
        dff = dff.replace("Non-religion volunteer", "Autres bénévoles")

        # name1 = "Religion volunteer"
        # name2 = "Non-religion volunteer"
        name1 = "Bénévoles de la religion"
        name2 = "Autres bénévoles"

        title = '{}, {}'.format("Freins à faire plus de bénévolat", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('ReligionDonRateDemo_fr', 'figure'),
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
        dash.dependencies.Output('ReligionVolRateDemo_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('demo-selection-vol', 'value'),
        ])
    def update_graph(region, demo):
        dff = SubSecVolRatesFoc_2018[SubSecVolRatesFoc_2018['Region'] == region]
        dff = dff[dff['Group'] == demo]

        title = 'Taux de bénévoles par {}, {}'.format(demo.lower(), region)

        return single_vertical_percentage_graph(dff, title)
