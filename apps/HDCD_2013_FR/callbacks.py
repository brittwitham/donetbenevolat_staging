# Callbacks file for HDCD_2013_FR converted from HDC010213_fr.py

import dash
from .data_processing import *
from .graphs import *


def register_callbacks(app):

    @app.callback(

        dash.dependencies.Output('DonMethDonRateAvgDonAmt-Method-13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):

        dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
        dff1 = dff1[dff1['Group'] == "All"]
        # name1 = "% donating"
        name1 = "Taux de donateur.trice.s"

        dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
        dff2 = dff2[dff2['Group'] == "All"]
        # name2 = "Average amount"
        name2 = "Dons annuels moyens"

        title = '{}, {}'.format(
            "Taux et montant moyen des dons par méthode", region)

        return don_rate_avg_don_by_meth(dff1, dff2, name1, name2, title)

    @app.callback(

        dash.dependencies.Output('DonMethDonRateAvgDonAmt-Age-13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('method-selection', 'value')
        ])
    def update_graph(region, method):

        dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
        dff1 = dff1[dff1['QuestionText'] == method]
        dff1 = dff1[dff1['Group'] == "Groupe d'âge"]
        # name1 = "% donating"
        name1 = "Taux de donateur.trice.s"

        dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
        dff2 = dff2[dff2['QuestionText'] == method]
        # dff2 = dff2[dff2['Group'] == "Age group"]
        dff2 = dff2[dff2['Group'] == "Groupe d'âge"]
        # name2 = "Average amount"
        name2 = "Dons annuels moyens"

        title = '{}, {}'.format(
            "Taux et montant moyen des dons " +
            str(method).lower() +
            " selon l’âge",
            region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(

        dash.dependencies.Output('DonMethDonRateAvgDonAmt-Gndr-13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('method-selection', 'value')
        ])
    def update_graph(region, method):
        dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
        dff1 = dff1[dff1['QuestionText'] == method]
        dff1 = dff1[dff1['Group'] == "Genre"]
        dff1 = dff1.replace("Male", "Hommes")
        dff1 = dff1.replace("Female", "Femmes")
        # name1 = "% donating"
        name1 = "Taux de donateur.trice.s"

        dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
        dff2 = dff2[dff2['QuestionText'] == method]
        dff2 = dff2[dff2['Group'] == "Genre"]
        dff2 = dff2.replace("Male", "Hommes")
        dff2 = dff2.replace("Female", "Femmes")
        # name2 = "Average amount"
        name2 = "Dons annuels moyens"

        title = '{}, {}'.format(
            "Taux et montant moyen des dons " +
            str(method).lower() +
            " selon le genre",
            region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(dash.dependencies.Output('DonMethDonRateAvgDonAmt-MarStat-13',
                                           'figure'),
                  [dash.dependencies.Input('region-selection',
                                           'value'),
                   dash.dependencies.Input('method-selection',
                                           'value')])
    def update_graph(region, method):
        dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
        dff1 = dff1[dff1['QuestionText'] == method]
        dff1 = dff1[dff1['Group'] == "Marital status"]
        name1 = "% donating"

        dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
        dff2 = dff2[dff2['QuestionText'] == method]
        dff2 = dff2[dff2['Group'] == "Marital status"]
        name2 = "Average amount"

        title = '{}, {}'.format(
            "Donation rate & average donation amount per method by marital status", region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(

        dash.dependencies.Output('DonMethDonRateAvgDonAmt-Educ-13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('method-selection', 'value')
        ])
    def update_graph(region, method):
        dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
        dff1 = dff1[dff1['QuestionText'] == method]
        dff1 = dff1[dff1['Group'] == "Éducation"]
        # name1 = "% donating"
        name1 = "Taux de donateur.trice.s"

        dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
        dff2 = dff2[dff2['QuestionText'] == method]
        dff2 = dff2[dff2['Group'] == "Éducation"]
        # name2 = "Average amount"
        name2 = "Dons annuels moyens"

        title = '{}, {}'.format(
            "Taux et montant moyen des dons " +
            str(method).lower() +
            " selon l’éducation",
            region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(dash.dependencies.Output('DonMethDonRateAvgDonAmt-Labour-13',
                                           'figure'),
                  [dash.dependencies.Input('region-selection',
                                           'value'),
                   dash.dependencies.Input('method-selection',
                                           'value')])
    def update_graph(region, method):
        dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
        dff1 = dff1[dff1['QuestionText'] == method]
        dff1 = dff1[dff1['Group'] == "Labour force status"]
        # name1 = "% donating"
        name1 = "Taux de donateur.trice.s"

        dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
        dff2 = dff2[dff2['QuestionText'] == method]
        dff2 = dff2[dff2['Group'] == "Labour force status"]
        # name2 = "Average amount"
        name2 = "Dons annuels moyens"

        title = '{}, {}'.format(
            "Donation rate & average donation amount per method by employment status",
            region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(

        dash.dependencies.Output('DonMethDonRateAvgDonAmt-Relig-13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('method-selection', 'value')
        ])
    def update_graph(region, method):
        dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
        dff1 = dff1[dff1['QuestionText'] == method]
        dff1 = dff1[dff1['Group'] ==
                    "Fréquence de la fréquentation religieuse"]
        # name1 = "% donating"
        name1 = "Taux de donateur.trice.s"

        dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
        dff2 = dff2[dff2['QuestionText'] == method]
        dff2 = dff2[dff2['Group'] ==
                    "Fréquence de la fréquentation religieuse"]
        # name2 = "Average amount"
        name2 = "Dons annuels moyens"

        title = '{}, {}'.format(
            "Taux et montant moyen des dons " +
            str(method).lower() +
            " selon la pratique religieuse",
            region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(

        dash.dependencies.Output('DonMethDonRateAvgDonAmt-Inc-13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('method-selection', 'value')
        ])
    def update_graph(region, method):
        dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
        dff1 = dff1[dff1['QuestionText'] == method]
        dff1 = dff1[dff1['Group'] == "Catégorie de revenu personnel"]
        # name1 = "% donating"
        name1 = "Taux de donateur.trice.s"

        dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
        dff2 = dff2[dff2['QuestionText'] == method]
        dff2 = dff2[dff2['Group'] == "Catégorie de revenu personnel"]
        # name2 = "Average amount"
        name2 = "Dons annuels moyens"

        title = '{}, {}'.format(
            "Taux et montant moyen des dons " +
            str(method).lower() +
            " selon le revenu",
            region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(dash.dependencies.Output('DonMethDonRateAvgDonAmt-ImmStat-13',
                                           'figure'),
                  [dash.dependencies.Input('region-selection',
                                           'value'),
                   dash.dependencies.Input('method-selection',
                                           'value')])
    def update_graph(region, method):
        dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
        dff1 = dff1[dff1['QuestionText'] == method]
        dff1 = dff1[dff1['Group'] == "Immigration status"]
        name1 = "% donating"

        dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
        dff2 = dff2[dff2['QuestionText'] == method]
        dff2 = dff2[dff2['Group'] == "Immigration status"]
        name2 = "Average amount"

        title = '{}, {}'.format(
            "Donation rate & average donation amount per method by immigration status",
            region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    # @app.callback(

    #     dash.dependencies.Output('status-sel-13', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value'),
    #         dash.dependencies.Input('method-selection', 'value'),
    #         dash.dependencies.Input('status-selection', 'value')
    #     ])
    # def update_graph(region, method, status):
    #     dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
    #     dff1 = dff1[dff1['QuestionText'] == method]
    #     dff1 = dff1[dff1['Group'] == status]
    #     name1 = "Donation rate"

    #     dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
    #     dff2 = dff2[dff2['QuestionText'] == method]
    #     dff2 = dff2[dff2['Group'] == status]
    #     name2 = "Average donation"

    #     # title = '{}, {}'.format("Donation rate & average donation amount per method by immigration status", region)
    #     a = ['At work', 'Online', 'On own', 'In memoriam', 'Door-to-door canvassing']
    #     b = ['Mail request', 'Telephone request', 'TV or radio request', 'Sponsoring someone']
    #     c = ['Charity event', 'Public place', 'Place of worship']

    #     if str(method) in a:
    #         title = '{}, {}'.format("Donations made " + str(method).lower() + " by immigration status", region)
    #     elif str(method) in b:
    #         title = '{}, {}'.format("Donations made by " + str(method).lower() + " by immigration status", region)
    #     elif str(method) in c:
    #         title = '{}, {}'.format("Donations made at " + str(method).lower() + " by immigration status", region)
    #     else:
    #         title = '{}, {}'.format(str(method) + " by immigration status", region)

    #     return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(

        dash.dependencies.Output('status-sel-13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('method-selection', 'value'),
            dash.dependencies.Input('status-selection', 'value')
        ])
    def update_graph(region, method, status):
        dff1 = DonMethDonRates_2013[DonMethDonRates_2013['Region'] == region]
        dff1 = dff1[dff1['QuestionText'] == method]
        dff1 = dff1[dff1['Group'] == status]
        # name1 = "Donation rate"
        name1 = "Taux de donateur.trice.s"

        dff2 = DonMethAvgDon_2013[DonMethAvgDon_2013['Region'] == region]
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
