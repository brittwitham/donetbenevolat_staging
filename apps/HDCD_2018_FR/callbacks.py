# Callbacks file for HDCD_2018_FR converted from
# Comment_donne_t_on_au_Canada_2018.py

import dash
from .data_processing import *
from .graphs import *


def register_callbacks(app):
    @app.callback(

        dash.dependencies.Output('DonMethDonRateAvgDonAmt-Method', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):

        dff1 = DonMethDonRates_2018[DonMethDonRates_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "All"]
        name1 = "Taux de donateur.trice.s"

        dff2 = DonMethAvgDon_2018[DonMethAvgDon_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "All"]
        name2 = "Dons annuels moyens"

        title = '{}, {}'.format(
            "Taux et montant moyen des dons par méthode", region)

        return don_rate_avg_don_by_meth(dff1, dff2, name1, name2, title)

    @app.callback(

        dash.dependencies.Output('DonMethDonRateAvgDonAmt-Gndr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('method-selection', 'value')
        ])
    def update_graph(region, method):
        dff1 = DonMethDonRates_2018[DonMethDonRates_2018['Region'] == region]
        dff1 = dff1[dff1['QuestionText'] == method]
        dff1 = dff1[dff1['Group'] == "Genre"]
        name1 = "Taux de donateur.trice.s"

        dff2 = DonMethAvgDon_2018[DonMethAvgDon_2018['Region'] == region]
        dff2 = dff2[dff2['QuestionText'] == method]
        dff2 = dff2[dff2['Group'] == "Genre"]
        name2 = "Dons annuels moyens"

        title = '{}, {}'.format(
            "Taux et montant moyen des dons " +
            str(method).lower() +
            " selon le genre",
            region)
        # a = ['At work', 'Online', 'On own', 'In memoriam', 'Door-to-door canvassing']
        # b = ['Mail request', 'Telephone request', 'TV or radio request', 'Sponsoring someone']
        # c = ['Charity event', 'Public place', 'Place of worship']

        # if str(method) in a:
        #     title = '{}, {}'.format("Donations made " + str(method).lower() + " by gender", region)
        # elif str(method) in b:
        #     title = '{}, {}'.format("Donations made by " + str(method).lower() + " by gender", region)
        # elif str(method) in c:
        #     title = '{}, {}'.format("Donations made at " + str(method).lower() + " by gender", region)
        # else:
        #     title = '{}, {}'.format(str(method) + " by gender", region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(

        dash.dependencies.Output('DonMethDonRateAvgDonAmt-Age', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('method-selection', 'value')
        ])
    def update_graph(region, method):

        dff1 = DonMethDonRates_2018[DonMethDonRates_2018['Region'] == region]
        dff1 = dff1[dff1['QuestionText'] == method]
        dff1 = dff1[dff1['Group'] == "Groupe d'âge"]
        name1 = "Taux de donateur.trice.s"

        dff2 = DonMethAvgDon_2018[DonMethAvgDon_2018['Region'] == region]
        dff2 = dff2[dff2['QuestionText'] == method]
        dff2 = dff2[dff2['Group'] == "Groupe d'âge"]
        name2 = "Dons annuels moyens"

        title = '{}, {}'.format(
            "Taux et montant moyen des dons " +
            str(method).lower() +
            " selon l’âge",
            region)
        # a = ['At work', 'Online', 'On own', 'In memoriam', 'Door-to-door canvassing']
        # b = ['Mail request', 'Telephone request', 'TV or radio request', 'Sponsoring someone']
        # c = ['Charity event', 'Public place', 'Place of worship']

        # if str(method) in a:
        #     title = '{}, {}'.format("Donations made " + str(method).lower() + " by age group", region)
        # elif str(method) in b:
        #     title = '{}, {}'.format("Donations made by " + str(method).lower() + " by age group", region)
        # elif str(method) in c:
        #     title = '{}, {}'.format("Donations made at " + str(method).lower() + " by age group", region)
        # else:
        #     title = '{}, {}'.format(str(method) + " by age group", region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(

        dash.dependencies.Output('DonMethDonRateAvgDonAmt-Educ', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('method-selection', 'value')
        ])
    def update_graph(region, method):
        dff1 = DonMethDonRates_2018[DonMethDonRates_2018['Region'] == region]
        dff1 = dff1[dff1['QuestionText'] == method]
        dff1 = dff1[dff1['Group'] == "Éducation"]
        name1 = "Taux de donateur.trice.s"

        dff2 = DonMethAvgDon_2018[DonMethAvgDon_2018['Region'] == region]
        dff2 = dff2[dff2['QuestionText'] == method]
        dff2 = dff2[dff2['Group'] == "Éducation"]
        name2 = "Dons annuels moyens"

        title = '{}, {}'.format(
            "Taux et montant moyen des dons " +
            str(method).lower() +
            " selon l’éducation",
            region)
        # a = ['At work', 'Online', 'On own', 'In memoriam', 'Door-to-door canvassing']
        # b = ['Mail request', 'Telephone request', 'TV or radio request', 'Sponsoring someone']
        # c = ['Charity event', 'Public place', 'Place of worship']

        # if str(method) in a:
        #     title = '{}, {}'.format("Donations made " + str(method).lower() + " by education", region)
        # elif str(method) in b:
        #     title = '{}, {}'.format("Donations made by " + str(method).lower() + " by education", region)
        # elif str(method) in c:
        #     title = '{}, {}'.format("Donations made at " + str(method).lower() + " by education", region)
        # else:
        #     title = '{}, {}'.format(str(method) + " by education", region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(

        dash.dependencies.Output('DonMethDonRateAvgDonAmt-Inc', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('method-selection', 'value')
        ])
    def update_graph(region, method):
        dff1 = DonMethDonRates_2018[DonMethDonRates_2018['Region'] == region]
        dff1 = dff1[dff1['QuestionText'] == method]
        dff1 = dff1[dff1['Group'] == "Catégorie de revenu personnel"]
        name1 = "Taux de donateur.trice.s"

        dff2 = DonMethAvgDon_2018[DonMethAvgDon_2018['Region'] == region]
        dff2 = dff2[dff2['QuestionText'] == method]
        dff2 = dff2[dff2['Group'] == "Catégorie de revenu personnel"]
        name2 = "Dons annuels moyens"

        title = '{}, {}'.format(
            "Taux et montant moyen des dons " +
            str(method).lower() +
            " selon le revenu",
            region)
        # a = ['At work', 'Online', 'On own', 'In memoriam', 'Door-to-door canvassing']
        # b = ['Mail request', 'Telephone request', 'TV or radio request', 'Sponsoring someone']
        # c = ['Charity event', 'Public place', 'Place of worship']

        # if str(method) in a:
        #     title = '{}, {}'.format("Donations made " + str(method).lower() + " by income", region)
        # elif str(method) in b:
        #     title = '{}, {}'.format("Donations made by " + str(method).lower() + " by income", region)
        # elif str(method) in c:
        #     title = '{}, {}'.format("Donations made at " + str(method).lower() + " by income", region)
        # else:
        #     title = '{}, {}'.format(str(method) + " by income", region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(

        dash.dependencies.Output('DonMethDonRateAvgDonAmt-Relig', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('method-selection', 'value')
        ])
    def update_graph(region, method):
        dff1 = DonMethDonRates_2018[DonMethDonRates_2018['Region'] == region]
        dff1 = dff1[dff1['QuestionText'] == method]
        dff1 = dff1[dff1['Group'] ==
                    "Fréquence de la fréquentation religieuse"]
        name1 = "Taux de donateur.trice.s"

        dff2 = DonMethAvgDon_2018[DonMethAvgDon_2018['Region'] == region]
        dff2 = dff2[dff2['QuestionText'] == method]
        dff2 = dff2[dff2['Group'] ==
                    "Fréquence de la fréquentation religieuse"]
        name2 = "Dons annuels moyens"

        title = '{}, {}'.format(
            "Taux et montant moyen des dons " +
            str(method).lower() +
            " selon la pratique religieuse",
            region)
        # a = ['At work', 'Online', 'On own', 'In memoriam', 'Door-to-door canvassing']
        # b = ['Mail request', 'Telephone request', 'TV or radio request', 'Sponsoring someone']
        # c = ['Charity event', 'Public place', 'Place of worship']

        # if str(method) in a:
        #     title = '{}, {}'.format("Donations made " + str(method).lower() + " by religious attendance", region)
        # elif str(method) in b:
        #     title = '{}, {}'.format("Donations made by " + str(method).lower() + " by religious attendance", region)
        # elif str(method) in c:
        #     title = '{}, {}'.format("Donations made at " + str(method).lower() + " by religious attendance", region)
        # else:
        #     title = '{}, {}'.format(str(method) + " by religious attendance", region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(
        dash.dependencies.Output('DonMethDonRateAvgDonAmt-MarStat', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('method-selection', 'value')
        ])
    def update_graph(region, method):
        dff1 = DonMethDonRates_2018[DonMethDonRates_2018['Region'] == region]
        dff1 = dff1[dff1['QuestionText'] == method]
        dff1 = dff1[dff1['Group'] == "Marital status"]
        name1 = "Taux de donateur.trice.s"

        dff2 = DonMethAvgDon_2018[DonMethAvgDon_2018['Region'] == region]
        dff2 = dff2[dff2['QuestionText'] == method]
        dff2 = dff2[dff2['Group'] == "Marital status"]
        name2 = "Dons annuels moyens"

        title = '{}, {}'.format(
            "Taux et montant moyen des dons " +
            str(method).lower() +
            " selon la situation matrimoniale",
            region)
        # a = ['At work', 'Online', 'On own', 'In memoriam', 'Door-to-door canvassing']
        # b = ['Mail request', 'Telephone request', 'TV or radio request', 'Sponsoring someone']
        # c = ['Charity event', 'Public place', 'Place of worship']

        # if str(method) in a:
        #     title = '{}, {}'.format("Donations made " + str(method).lower() + " by marital status", region)
        # elif str(method) in b:
        #     title = '{}, {}'.format("Donations made by " + str(method).lower() + " by marital status", region)
        # elif str(method) in c:
        #     title = '{}, {}'.format("Donations made at " + str(method).lower() + " by marital status", region)
        # else:
        #     title = '{}, {}'.format(str(method) + " by marital status", region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(

        dash.dependencies.Output('DonMethDonRateAvgDonAmt-Labour', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('method-selection', 'value')
        ])
    def update_graph(region, method):
        dff1 = DonMethDonRates_2018[DonMethDonRates_2018['Region'] == region]
        dff1 = dff1[dff1['QuestionText'] == method]
        dff1 = dff1[dff1['Group'] == "Labour force status"]
        name1 = "Taux de donateur.trice.s"

        dff2 = DonMethAvgDon_2018[DonMethAvgDon_2018['Region'] == region]
        dff2 = dff2[dff2['QuestionText'] == method]
        dff2 = dff2[dff2['Group'] == "Labour force status"]
        name2 = "Dons annuels moyens"

        title = '{}, {}'.format(
            "Taux et montant moyen des dons " +
            str(method).lower() +
            " selon la situation d’emploi",
            region)
        # a = ['At work', 'Online', 'On own', 'In memoriam', 'Door-to-door canvassing']
        # b = ['Mail request', 'Telephone request', 'TV or radio request', 'Sponsoring someone']
        # c = ['Charity event', 'Public place', 'Place of worship']

        # if str(method) in a:
        #     title = '{}, {}'.format("Donations made " + str(method).lower() + " by employment status", region)
        # elif str(method) in b:
        #     title = '{}, {}'.format("Donations made by " + str(method).lower() + " by employment status", region)
        # elif str(method) in c:
        #     title = '{}, {}'.format("Donations made at " + str(method).lower() + " by employment status", region)
        # else:
        #     title = '{}, {}'.format(str(method) + " by employment status", region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(

        dash.dependencies.Output('DonMethDonRateAvgDonAmt-ImmStat', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('method-selection', 'value')
        ])
    def update_graph(region, method):
        dff1 = DonMethDonRates_2018[DonMethDonRates_2018['Region'] == region]
        dff1 = dff1[dff1['QuestionText'] == method]
        dff1 = dff1[dff1['Group'] == "Immigration status"]
        name1 = "Taux de donateur.trice.s"

        dff2 = DonMethAvgDon_2018[DonMethAvgDon_2018['Region'] == region]
        dff2 = dff2[dff2['QuestionText'] == method]
        dff2 = dff2[dff2['Group'] == "Immigration status"]
        name2 = "Dons annuels moyens"

        title = '{}, {}'.format(
            "Taux et montant moyen des dons " +
            str(method).lower() +
            " selon le statut d’immigration",
            region)
        # a = ['At work', 'Online', 'On own', 'In memoriam', 'Door-to-door canvassing']
        # b = ['Mail request', 'Telephone request', 'TV or radio request', 'Sponsoring someone']
        # c = ['Charity event', 'Public place', 'Place of worship']

        # if str(method) in a:
        #     title = '{}, {}'.format("Donations made " + str(method).lower() + " by immigration status", region)
        # elif str(method) in b:
        #     title = '{}, {}'.format("Donations made by " + str(method).lower() + " by immigration status", region)
        # elif str(method) in c:
        #     title = '{}, {}'.format("Donations made at " + str(method).lower() + " by immigration status", region)
        # else:
        #     title = '{}, {}'.format(str(method) + " by immigration status", region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(

        dash.dependencies.Output('status-sel3', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('method-selection', 'value'),
            dash.dependencies.Input('status-selection', 'value')
        ])
    def update_graph(region, method, status):
        dff1 = DonMethDonRates_2018[DonMethDonRates_2018['Region'] == region]
        dff1 = dff1[dff1['QuestionText'] == method]
        dff1 = dff1[dff1['Group'] == status]
        # name1 = "Donation rate"
        name1 = "Taux de donateur.trice.s"

        dff2 = DonMethAvgDon_2018[DonMethAvgDon_2018['Region'] == region]
        dff2 = dff2[dff2['QuestionText'] == method]
        dff2 = dff2[dff2['Group'] == status]
        name2 = "Dons annuels moyens"
        # name2 = "Average donation"

        title = '{}, {}'.format(
            "Taux et montant moyen des dons " +
            str(method).lower() +
            " selon " +
            str(status).lower(),
            region)
        # a = ['At work', 'Online', 'On own', 'In memoriam', 'Door-to-door canvassing']
        # b = ['Mail request', 'Telephone request', 'TV or radio request', 'Sponsoring someone']
        # c = ['Charity event', 'Public place', 'Place of worship']

        # if str(method) in a:
        #     title = '{}, {}'.format("Donations made " + str(method).lower() + " by immigration status", region)
        # elif str(method) in b:
        #     title = '{}, {}'.format("Donations made by " + str(method).lower() + " by immigration status", region)
        # elif str(method) in c:
        #     title = '{}, {}'.format("Donations made at " + str(method).lower() + " by immigration status", region)
        # else:
        #     title = '{}, {}'.format(str(method) + " by immigration status", region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)
