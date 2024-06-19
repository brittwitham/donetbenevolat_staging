import dash
from .data_processing import *
from .graphs import *


def register_callbacks(app):
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
    
    @app.callback(
        dash.dependencies.Output('EducDonRateAvgDon', 'figure'),
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
            "Taux et montant moyen des dons selon la cause", region)

        return rate_avg_cause(dff1, dff2, name1, name2, title)


    @app.callback(
        dash.dependencies.Output('EducDonsCauses', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = EducDonorsDonRates_2018[EducDonorsDonRates_2018['Region'] == region]
        name1 = "Education and research donor"
        name2 = "Non-education and research donor"

        array = [
            "Education &<br>research",
            "Universities &<br>colleges",
            "Health",
            "Social services",
            "Religion",
            "Hospitals",
            "Sports &<br>recreation",
            "Grant-making,<br>fundraising",
            "Environment",
            "International",
            "Arts & culture",
            "Law, advocacy &<br>politics",
            "Development &<br>housing",
            "Other",
            "Business &<br>professional"]
        title = '{}, {}'.format("Rates of donating to other causes", region)
        return vertical_percentage_graph(
            dff, title, name1, name2, sort=True, array=array)


    @app.callback(
        dash.dependencies.Output('EducDonsMeth', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = EducDonorsDonMeth_2018[EducDonorsDonMeth_2018['Region'] == region]
        dff = dff.replace(
            "Education and research donors",
            "Donateur.trice.s de l'éducation")
        dff = dff.replace(
            "Non-education and research donors",
            "Autres donateur.trice.s")

        # name1 = "Education and research donors"
        # name2 = "Non-education and research donors"
        name1 = "Donateur.trice.s de l'éducation"
        name2 = "Autres donateur.trice.s"

        title = '{}, {}'.format("Taux de donateur.trice.s par méthode", region)
        return vertical_percentage_graph(dff, title, name1, name2)


    @app.callback(
        dash.dependencies.Output('EducMotivations', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = EducDonorsMotivations_2018[EducDonorsMotivations_2018['Region'] == region]
        dff = dff.replace(
            "Education and research donors",
            "Donateur.trice.s de l'éducation")
        dff = dff.replace(
            "Non-education and research donors",
            "Autres donateur.trice.s")

        # name1 = "Education and research donors"
        # name2 = "Non-education and research donors"
        name1 = "Donateur.trice.s de l'éducation"
        name2 = "Autres donateur.trice.s"

        title = '{}, {}'.format("Motivations des dons", region)
        return vertical_percentage_graph(dff, title, name1, name2)


    @app.callback(
        dash.dependencies.Output('EducBarriers', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = EducDonorsBarriers_2018[EducDonorsBarriers_2018['Region'] == region]
        dff = dff.replace(
            "Education and research donors",
            "Donateur.trice.s de l'éducation")
        dff = dff.replace(
            "Non-education and research donors",
            "Autres donateur.trice.s")

        # name1 = "Education and research donors"
        # name2 = "Non-education and research donors"
        name1 = "Donateur.trice.s de l'éducation"
        name2 = "Autres donateur.trice.s"

        title = '{}, {}'.format("Freins à donner plus", region)
        return vertical_percentage_graph(dff, title, name1, name2)


    # @app.callback(
    #     dash.dependencies.Output('EducVolRateAvgHrs', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     dff1 = SubSecVolRates_2018[SubSecVolRates_2018['Region'] == region]
    #     dff1 = dff1[dff1['Group'] == "All"]
    #     # dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")
    #     name1 = "Volunteer rate"
    #     # name1 = "Taux de bénévolat"

    #     dff2 = SubSecAvgHrs_2018[SubSecAvgHrs_2018['Region'] == region]
    #     # dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
    #     name2 = "Average hours"
    #     # name2 = "Nombre d'heures moyen"

    #     title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures de bénévolat selon la cause", region)

    #     return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)

    @app.callback(
        dash.dependencies.Output('EducVolRateAvgHrs', 'figure'),
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
        dash.dependencies.Output('EducHrsCauses', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = EducVolsVolRates_2018[EducVolsVolRates_2018['Region'] == region]
        dff = dff.replace(
            "Education and research volunteer",
            "Bénévoles de l'éducation")
        dff = dff.replace(
            "Non-education and research volunteer",
            "Autres bénévoles")

        # name1 = "Education and research volunteer"
        # name2 = "Non-education and research volunteer"
        name1 = "Bénévoles de l'éducation"
        name2 = "Autres bénévoles"

        title = '{}, {}'.format("Rates of volunteering for other causes", region)
        return vertical_percentage_graph(dff, title, name1, name2)


    @app.callback(
        dash.dependencies.Output('EducVolActivity', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = EducVolsActivities_2018[EducVolsActivities_2018['Region'] == region]
        dff = dff.replace(
            "Education and research volunteer",
            "Bénévoles de l'éducation")
        dff = dff.replace(
            "Non-education and research volunteer",
            "Autres bénévoles")

        # name1 = "Education and research volunteer"
        # name2 = "Non-education and research volunteer"
        name1 = "Bénévoles de l'éducation"
        name2 = "Autres bénévoles"

        title = '{}, {}'.format("Taux de bénévolat par activité", region)
        return vertical_percentage_graph(dff, title, name1, name2)


    @app.callback(
        dash.dependencies.Output('EducVolMotivations', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = EducVolsMotivations_2018[EducVolsMotivations_2018['Region'] == region]
        dff = dff.replace(
            "Education and research volunteer",
            "Bénévoles de l'éducation")
        dff = dff.replace(
            "Non-education and research volunteer",
            "Autres bénévoles")

        # name1 = "Education and research volunteer"
        # name2 = "Non-education and research volunteer"
        name1 = "Bénévoles de l'éducation"
        name2 = "Autres bénévoles"

        title = '{}, {}'.format("Motivations des bénévoles", region)
        return vertical_percentage_graph(dff, title, name1, name2)


    @app.callback(
        dash.dependencies.Output('EducVolBarriers', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = EducVolsBarriers_2018[EducVolsBarriers_2018['Region'] == region]
        dff = dff.replace(
            "Education and research volunteer",
            "Bénévoles de l'éducation")
        dff = dff.replace(
            "Non-education and research volunteer",
            "Autres bénévoles")

        # name1 = "Education and research volunteer"
        # name2 = "Non-education and research volunteer"
        name1 = "Bénévoles de l'éducation"
        name2 = "Autres bénévoles"

        title = '{}, {}'.format("Freins à faire plus de bénévolat", region)
        return vertical_percentage_graph(dff, title, name1, name2)


    @app.callback(
        dash.dependencies.Output('EducDonRateDemo_fr', 'figure'),
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
        dash.dependencies.Output('EducVolRateDemo_fr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('demo-selection-vol', 'value'),
        ])
    def update_graph(region, demo):
        dff = SubSecVolRatesFoc_2018[SubSecVolRatesFoc_2018['Region'] == region]
        dff = dff[dff['Group'] == demo]

        title = 'Taux de bénévoles par {}, {}'.format(demo.lower(), region)

        return single_vertical_percentage_graph(dff, title)