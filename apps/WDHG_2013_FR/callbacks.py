# Callbacks file for WDHG_2013_FR converted from WDA010113_fr.py

import dash
from .data_processing import *
from .graphs import *
from dash.dependencies import Input, Output, State, ClientsideFunction


def register_callbacks(app):

    app.clientside_callback(
        ClientsideFunction("clientside", "stickyHeader"),
        Output("sticky", "data-loaded_13"),  # Just put some dummy output here
        # This will trigger the callback when the object is injected in the DOM
        [Input("sticky", "id")],
    )

    # @app.callback(
    #     # Output: change to graph-1
    #     dash.dependencies.Output('FormsGiving_13', 'figure'),
    #     [
    #         # Input: selected region from region-selection (dropdown menu)
    #         # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     """
    # Construct or update graph according to input from 'region-selection'
    # dropdown menu.

    #     :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
    #     :return: Plot.ly graph object, produced by don_rate_avg_don().
    #     """
    #     # Donation rate data, filtered for selected region and demographic group (age group)
    #     # Corresponding name assigned
    #     dff1 = FormsGiving_2018[FormsGiving_2018['Region'] == region]
    #     dff1 = dff1[dff1['Group'] == "All"]

    #     # dff1['QuestionText'] = dff1['QuestionText'].replace('Financial donation', 'Don financier')
    #     # dff1['QuestionText'] = dff1['QuestionText'].replace('Food bank', 'Banque alimentaire')
    #     # dff1['QuestionText'] = dff1['QuestionText'].replace('In-kind', 'En nature')
    #     # dff1['QuestionText'] = dff1['QuestionText'].replace('Bequest, planned gift', 'Leg, don planifié')

    #     # Format title according to dropdown input
    #     title = '{}, {}'.format("Formes de don", region)

    #     # Uses external function with dataframes, names, and title set up above
    #     return forms_of_giving(dff1, title)

    @app.callback(
        # Output: change to graph-1
        dash.dependencies.Output('FormsGiving_13', 'figure'),
        [
            # Input: selected region from region-selection (dropdown menu)
            # In the case of multiple inputs listed here, they will enter as
            # arguments into the function below in the order they are listed
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        """
        Construct or update graph according to input from 'region-selection' dropdown menu.

        :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
        :return: Plot.ly graph object, produced by don_rate_avg_don().
        """
        # Donation rate data, filtered for selected region and demographic group (age group)
        # Corresponding name assigned
        dff1 = FormsGiving_2018[FormsGiving_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "All"]

        dff1['QuestionText'] = dff1['QuestionText'].replace(
            'Financial donation', 'Don financier')
        dff1['QuestionText'] = dff1['QuestionText'].replace(
            'Food bank', 'Banque alimentaire')
        dff1['QuestionText'] = dff1['QuestionText'].replace(
            'In-kind', 'En nature')
        dff1['QuestionText'] = dff1['QuestionText'].replace(
            'Bequest, planned gift', 'Leg, don planifié')

        # Format title according to dropdown input
        title = '{}, {}'.format("Formes de don", region)

        # Uses external function with dataframes, names, and title set up above
        return forms_of_giving(dff1, title)

    @app.callback(
        dash.dependencies.Output('DonRateAvgDonAmt-Age_13', 'figure'),
        [dash.dependencies.Input('region-selection', 'value')])
    def update_graph(region):
        dff1 = DonRates_2018[DonRates_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Groupe d'âge"]
        name1 = "Taux de donateur.trice.s"

        dff2 = AvgTotDon_2018[AvgTotDon_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Groupe d'âge"]
        name2 = "Dons annuels moyens"

        # title = 'Region selected: {}'.format(region)
        title = '{}, {}'.format(
            "Taux de donateur.trice.s et montant moyen des dons<br>selon le groupe d'âge",
            region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-1
        dash.dependencies.Output('DonRateAvgDonAmt-Gndr_13', 'figure'),
        [
            # Input: selected region from region-selection (dropdown menu)
            # In the case of multiple inputs listed here, they will enter as
            # arguments into the function below in the order they are listed
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        """
        Construct or update graph according to input from 'region-selection' dropdown menu.

        :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
        :return: Plot.ly graph object, produced by don_rate_avg_don().
        """
        # Donation rate data, filtered for selected region and demographic group (age group)
        # Corresponding name assigned
        dff1 = DonRates_2018[DonRates_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Genre"]
        dff1 = dff1.replace('Male', 'Hommes')
        dff1 = dff1.replace('Female', 'Femmes')
        name1 = "Taux de donateur.trice.s"

        # Average annual donation data, filtered for selected region and demographic group (age group)
        # Corresponding name assigned
        dff2 = AvgTotDon_2018[AvgTotDon_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Genre"]
        dff2 = dff2.replace('Male', 'Hommes')
        dff2 = dff2.replace('Female', 'Femmes')
        name2 = "Dons annuels moyens"

        # Format title according to dropdown input
        title = '{}, {}'.format(
            "Taux de donateur.trice.s et montant moyen des dons<br>selon le genre", region)

        # Uses external function with dataframes, names, and title set up above
        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-2
        dash.dependencies.Output('PercDon-Gndr_13', 'figure'),
        [
            # Input: selected region from region-selection (dropdown menu)
            # In the case of multiple inputs listed here, they will enter as
            # arguments into the function below in the order they are listed
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        """
            Construct or update graph according to input from 'region-selection' dropdown menu.

            :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
            :return: Plot.ly graph object, produced by don_rate_avg_don().
        """

        # Donation rate data, filtered for selected region and demographic group (education)
        # Corresponding name assigned
        dff1 = PropTotDon_2018[PropTotDon_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Genre"]
        name1 = "Pourcentage de la population"

        # Average annual donation data, filtered for selected region and demographic group (education)
        # Corresponding name assigned
        dff2 = PropTotDonAmt_2018[PropTotDonAmt_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Genre"]
        name2 = "Pourcentage de la valeur des dons"

        # Format title according to dropdown input
        title = '{}, {}'.format(
            "Pourcentage de la population et de la valeur totale des dons<br>selon le genre",
            region)

        # Uses external function with dataframes, names, and title set up above
        return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-4
        dash.dependencies.Output('PrimCauseNumCause-Gndr_13', 'figure'),
        [
            # Inputs: selected region from region-selection and selected
            # demographic group from graph-4-demos (dropdown menu)
            dash.dependencies.Input('region-selection', 'value'),
        ])
    def update_graph(region):
        """
            Construct or update graph according to input from 'region-selection' dropdown menu.

            :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
            :param demo: Demographic group name (str). Automatically inherited from 'graph-4-demos' dcc.Dropdown() input via dash.dependencies.Input('graph-4-demos', 'value') above.
            :return: Plot.ly graph object, produced by don_rate_avg_don().
        """

        # Average number of annual donations data, filtered for selected region and demographic group
        # Corresponding name assigned
        dff1 = AvgNumCauses_2018[AvgNumCauses_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Genre"]
        name1 = "Nombre moyen de causes"

        # Average number of causes supported data, filtered for selected region and demographic group
        # Corresponding name assigned
        dff2 = TopCauseFocus_2018[TopCauseFocus_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Genre"]
        name2 = "Concentration moyenne sur la 1ère cause"

        # Format title according to dropdown input
        title = '{}, {}'.format(
            "Concentration sur la cause principale et nombre moyen de causes soutenues<br>selon le genre",
            region)

        # Uses external function with dataframes, names, and title set up above
        return prim_cause_num_cause(dff2, dff1, name2, name1, title)

    @app.callback(
        # Output: change to graph-2
        dash.dependencies.Output('PercDon-Age_13', 'figure'),
        [
            # Input: selected region from region-selection (dropdown menu)
            # In the case of multiple inputs listed here, they will enter as
            # arguments into the function below in the order they are listed
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        """
            Construct or update graph according to input from 'region-selection' dropdown menu.

            :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
            :return: Plot.ly graph object, produced by don_rate_avg_don().
        """

        # Donation rate data, filtered for selected region and demographic group (education)
        # Corresponding name assigned
        dff1 = PropTotDon_2018[PropTotDon_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Groupe d'âge"]
        name1 = "Pourcentage de la population"

        # Average annual donation data, filtered for selected region and demographic group (education)
        # Corresponding name assigned
        dff2 = PropTotDonAmt_2018[PropTotDonAmt_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Groupe d'âge"]
        name2 = "Pourcentage de la valeur des dons"

        # Format title according to dropdown input
        title = '{}, {}'.format(
            "Pourcentage de la population et de la valeur totale des dons<br>selon l’âge",
            region)

        # Uses external function with dataframes, names, and title set up above
        return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-4
        dash.dependencies.Output('PrimCauseNumCause-Age_13', 'figure'),
        [
            # Inputs: selected region from region-selection and selected
            # demographic group from graph-4-demos (dropdown menu)
            dash.dependencies.Input('region-selection', 'value'),
        ])
    def update_graph(region):
        """
            Construct or update graph according to input from 'region-selection' dropdown menu.

            :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
            :param demo: Demographic group name (str). Automatically inherited from 'graph-4-demos' dcc.Dropdown() input via dash.dependencies.Input('graph-4-demos', 'value') above.
            :return: Plot.ly graph object, produced by don_rate_avg_don().
        """

        # Average number of annual donations data, filtered for selected region and demographic group
        # Corresponding name assigned
        dff1 = AvgNumCauses_2018[AvgNumCauses_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Groupe d'âge"]
        name1 = "Nombre moyen de causes"

        # Average number of causes supported data, filtered for selected region and demographic group
        # Corresponding name assigned
        dff2 = TopCauseFocus_2018[TopCauseFocus_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Groupe d'âge"]
        name2 = "Concentration moyenne sur la 1ère cause"

        # Format title according to dropdown input
        title = '{}, {}'.format(
            "Concentration sur la cause principale et nombre moyen de causes soutenues<br>selon l’âge",
            region)

        # Uses external function with dataframes, names, and title set up above
        return prim_cause_num_cause(dff2, dff1, name2, name1, title)

    @app.callback(
        # Output: change to graph-1
        dash.dependencies.Output('DonRateAvgDonAmt-Educ_13', 'figure'),
        [
            # Input: selected region from region-selection (dropdown menu)
            # In the case of multiple inputs listed here, they will enter as
            # arguments into the function below in the order they are listed
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        """
        Construct or update graph according to input from 'region-selection' dropdown menu.

        :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
        :return: Plot.ly graph object, produced by don_rate_avg_don().
        """
        # Donation rate data, filtered for selected region and demographic group (age group)
        # Corresponding name assigned
        dff1 = DonRates_2018[DonRates_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Éducation"]
        dff1 = dff1[dff1['Attribute'] != "Non indiqué"]
        name1 = "Taux de donateur.trice.s"

        # Average annual donation data, filtered for selected region and demographic group (age group)
        # Corresponding name assigned
        dff2 = AvgTotDon_2018[AvgTotDon_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Éducation"]
        dff2 = dff2[dff2['Attribute'] != "Non indiqué"]
        name2 = "Dons annuels moyens"

        # Format title according to dropdown input
        title = '{}, {}'.format(
            "Taux de donateur.trice.s et montant moyen des dons<br>selon l’éducation",
            region)

        # Uses external function with dataframes, names, and title set up above
        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-2
        dash.dependencies.Output('PercDon-Educ_13', 'figure'),
        [
            # Input: selected region from region-selection (dropdown menu)
            # In the case of multiple inputs listed here, they will enter as
            # arguments into the function below in the order they are listed
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        """
            Construct or update graph according to input from 'region-selection' dropdown menu.

            :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
            :return: Plot.ly graph object, produced by don_rate_avg_don().
        """

        # Donation rate data, filtered for selected region and demographic group (education)
        # Corresponding name assigned
        dff1 = PropTotDon_2018[PropTotDon_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Éducation"]
        name1 = "Pourcentage de la population"

        # Average annual donation data, filtered for selected region and demographic group (education)
        # Corresponding name assigned
        dff2 = PropTotDonAmt_2018[PropTotDonAmt_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Éducation"]
        name2 = "Pourcentage de la valeur des dons"

        # Format title according to dropdown input
        title = '{}, {}'.format(
            "Pourcentage de la population et de la valeur totale des dons<br>selon l’éducation",
            region)

        # Uses external function with dataframes, names, and title set up above
        return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-4
        dash.dependencies.Output('PrimCauseNumCause-Educ_13', 'figure'),
        [
            # Inputs: selected region from region-selection and selected
            # demographic group from graph-4-demos (dropdown menu)
            dash.dependencies.Input('region-selection', 'value'),
        ])
    def update_graph(region):
        """
            Construct or update graph according to input from 'region-selection' dropdown menu.

            :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
            :param demo: Demographic group name (str). Automatically inherited from 'graph-4-demos' dcc.Dropdown() input via dash.dependencies.Input('graph-4-demos', 'value') above.
            :return: Plot.ly graph object, produced by don_rate_avg_don().
        """

        # Average number of annual donations data, filtered for selected region and demographic group
        # Corresponding name assigned
        AvgNumCauses_2018.Attribute = AvgNumCauses_2018.Attribute.replace(
            "Less than High School", "Sans diplôme d'études secondaires")
        TopCauseFocus_2018.Attribute = TopCauseFocus_2018.Attribute.replace(
            "Less than High School", "Sans diplôme d'études secondaires")

        dff1 = AvgNumCauses_2018[AvgNumCauses_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Éducation"]
        name1 = "Nombre moyen de causes"

        # Average number of causes supported data, filtered for selected region and demographic group
        # Corresponding name assigned
        dff2 = TopCauseFocus_2018[TopCauseFocus_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Éducation"]
        name2 = "Concentration moyenne sur la 1ère cause"

        # Format title according to dropdown input
        title = '{}, {}'.format(
            "Concentration sur la cause principale et nombre moyen de causes soutenues<br>selon l’éducation ",
            region)

        # Uses external function with dataframes, names, and title set up above
        return prim_cause_num_cause(dff2, dff1, name2, name1, title)

    @app.callback(
        # Output: change to graph-1
        dash.dependencies.Output('DonRateAvgDonAmt-Inc_13', 'figure'),
        [
            # Input: selected region from region-selection (dropdown menu)
            # In the case of multiple inputs listed here, they will enter as
            # arguments into the function below in the order they are listed
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        """
        Construct or update graph according to input from 'region-selection' dropdown menu.

        :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
        :return: Plot.ly graph object, produced by don_rate_avg_don().
        """
        # Donation rate data, filtered for selected region and demographic group (age group)
        # Corresponding name assigned
        dff1 = DonRates_2018[DonRates_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Catégorie de revenu familial"]
        name1 = "Taux de donateur.trice.s"

        # Average annual donation data, filtered for selected region and demographic group (age group)
        # Corresponding name assigned
        dff2 = AvgTotDon_2018[AvgTotDon_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Catégorie de revenu familial"]
        name2 = "Dons annuels moyens"

        # Format title according to dropdown input
        title = '{}, {}'.format(
            "Taux de donateur.trice.s et montant moyen des dons<br>selon le revenu",
            region)

        # Uses external function with dataframes, names, and title set up above
        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-2
        dash.dependencies.Output('PercDon-Inc_13', 'figure'),
        [
            # Input: selected region from region-selection (dropdown menu)
            # In the case of multiple inputs listed here, they will enter as
            # arguments into the function below in the order they are listed
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        """
            Construct or update graph according to input from 'region-selection' dropdown menu.

            :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
            :return: Plot.ly graph object, produced by don_rate_avg_don().
        """

        # Donation rate data, filtered for selected region and demographic group (education)
        # Corresponding name assigned
        dff1 = PropTotDon_2018[PropTotDon_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Catégorie de revenu familial"]
        name1 = "Pourcentage de la population"

        # Average annual donation data, filtered for selected region and demographic group (education)
        # Corresponding name assigned
        dff2 = PropTotDonAmt_2018[PropTotDonAmt_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Catégorie de revenu familial"]
        name2 = "Pourcentage de la valeur des dons"

        # Format title according to dropdown input
        title = '{}, {}'.format(
            "Pourcentage de la population et de la valeur totale des dons<br>selon le revenu",
            region)

        # Uses external function with dataframes, names, and title set up above
        return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-4
        dash.dependencies.Output('PrimCauseNumCause-Inc_13', 'figure'),
        [
            # Inputs: selected region from region-selection and selected
            # demographic group from graph-4-demos (dropdown menu)
            dash.dependencies.Input('region-selection', 'value'),
        ])
    def update_graph(region):
        """
            Construct or update graph according to input from 'region-selection' dropdown menu.

            :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
            :param demo: Demographic group name (str). Automatically inherited from 'graph-4-demos' dcc.Dropdown() input via dash.dependencies.Input('graph-4-demos', 'value') above.
            :return: Plot.ly graph object, produced by don_rate_avg_don().
        """

        # Average number of annual donations data, filtered for selected region and demographic group
        # Corresponding name assigned
        dff1 = AvgNumCauses_2018[AvgNumCauses_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Catégorie de revenu familial"]
        name1 = "Nombre moyen de causes"

        # Average number of causes supported data, filtered for selected region and demographic group
        # Corresponding name assigned
        dff2 = TopCauseFocus_2018[TopCauseFocus_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Catégorie de revenu familial"]
        name2 = "Concentration moyenne sur la 1ère cause"

        # Format title according to dropdown input
        title = '{}, {}'.format(
            "Concentration sur la cause principale et nombre moyen de causes soutenues<br>selon le revenu",
            region)

        # Uses external function with dataframes, names, and title set up above
        return prim_cause_num_cause(dff2, dff1, name2, name1, title)

    @app.callback(
        # Output: change to graph-1
        dash.dependencies.Output('DonRateAvgDonAmt-Relig_13', 'figure'),
        [
            # Input: selected region from region-selection (dropdown menu)
            # In the case of multiple inputs listed here, they will enter as
            # arguments into the function below in the order they are listed
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        """
        Construct or update graph according to input from 'region-selection' dropdown menu.

        :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
        :return: Plot.ly graph object, produced by don_rate_avg_don().
        """
        # Donation rate data, filtered for selected region and demographic group (age group)
        # Corresponding name assigned
        dff1 = DonRates_2018[DonRates_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] ==
                    "Fréquence de la fréquentation religieuse"]
        dff1 = dff1[dff1['Attribute'] != "Non indiqué"]
        name1 = "Taux de donateur.trice.s"

        # Average annual donation data, filtered for selected region and demographic group (age group)
        # Corresponding name assigned
        dff2 = AvgTotDon_2018[AvgTotDon_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] ==
                    "Fréquence de la fréquentation religieuse"]
        dff2 = dff2[dff2['Attribute'] != "Non indiqué"]
        name2 = "Dons annuels moyens"

        # Format title according to dropdown input
        title = '{}, {}'.format(
            "Taux de donateur.trice.s et montant moyen des dons<br>selon la pratique religieuse",
            region)

        # Uses external function with dataframes, names, and title set up above
        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-2
        dash.dependencies.Output('PercDon-Relig_13', 'figure'),
        [
            # Input: selected region from region-selection (dropdown menu)
            # In the case of multiple inputs listed here, they will enter as
            # arguments into the function below in the order they are listed
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        """
            Construct or update graph according to input from 'region-selection' dropdown menu.

            :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
            :return: Plot.ly graph object, produced by don_rate_avg_don().
        """

        # Donation rate data, filtered for selected region and demographic group (education)
        # Corresponding name assigned
        dff1 = PropTotDon_2018[PropTotDon_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] ==
                    "Fréquence de la fréquentation religieuse"]
        name1 = "Pourcentage de la population"

        # Average annual donation data, filtered for selected region and demographic group (education)
        # Corresponding name assigned
        dff2 = PropTotDonAmt_2018[PropTotDonAmt_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] ==
                    "Fréquence de la fréquentation religieuse"]
        name2 = "Pourcentage de la valeur des dons"

        # Format title according to dropdown input
        title = '{}, {}'.format(
            "Pourcentage de la population et de la valeur totale des dons<br>selon la pratique religieuse",
            region)

        # Uses external function with dataframes, names, and title set up above
        return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-4
        dash.dependencies.Output('PrimCauseNumCause-Relig_fr_13', 'figure'),
        [
            # Inputs: selected region from region-selection and selected
            # demographic group from graph-4-demos (dropdown menu)
            dash.dependencies.Input('region-selection', 'value'),
        ])
    def update_graph(region):
        """
            Construct or update graph according to input from 'region-selection' dropdown menu.

            :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
            :param demo: Demographic group name (str). Automatically inherited from 'graph-4-demos' dcc.Dropdown() input via dash.dependencies.Input('graph-4-demos', 'value') above.
            :return: Plot.ly graph object, produced by don_rate_avg_don().
        """

        # Average number of annual donations data, filtered for selected region and demographic group
        # Corresponding name assigned
        dff1 = AvgNumCauses_2018[AvgNumCauses_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] ==
                    "Fréquence de la fréquentation religieuse"]
        name1 = "Nombre moyen de causes"

        # Average number of causes supported data, filtered for selected region and demographic group
        # Corresponding name assigned
        dff2 = TopCauseFocus_2018[TopCauseFocus_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] ==
                    "Fréquence de la fréquentation religieuse"]
        name2 = "Concentration moyenne sur la 1ère cause"

        # Format title according to dropdown input
        title = '{}, {}'.format(
            "Concentration sur la cause principale et nombre moyen de causes soutenues<br>selon la pratique religieuse ",
            region)

        # Uses external function with dataframes, names, and title set up above
        return prim_cause_num_cause(dff2, dff1, name2, name1, title)

    @app.callback(
        # Output: change to graph-1
        dash.dependencies.Output('DonRateAvgDonAmt-other_13', 'figure'),
        [
            # Input: selected region from region-selection (dropdown menu)
            # In the case of multiple inputs listed here, they will enter as
            # arguments into the function below in the order they are listed
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('status-selection1', 'value')
        ])
    def update_graph(region, status):
        """
        Construct or update graph according to input from 'region-selection' dropdown menu.

        :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
        :return: Plot.ly graph object, produced by don_rate_avg_don().
        """
        # Donation rate data, filtered for selected region and demographic group (age group)
        # Corresponding name assigned
        dff1 = DonRates_2018[DonRates_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == status]
        name1 = "Taux de donateur.trice.s"

        # Average annual donation data, filtered for selected region and demographic group (age group)
        # Corresponding name assigned
        dff2 = AvgTotDon_2018[AvgTotDon_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == status]
        name2 = "Dons annuels moyens"

        # Format title according to dropdown input
        title = '{}, {}'.format(
            "Taux de donateur.trice.s et montant moyen des dons<br>selon " +
            str(status).lower(),
            region)

        # Uses external function with dataframes, names, and title set up above
        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-2
        dash.dependencies.Output('PercDon-other_13', 'figure'),
        [
            # Input: selected region from region-selection (dropdown menu)
            # In the case of multiple inputs listed here, they will enter as
            # arguments into the function below in the order they are listed
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('status-selection2', 'value')
        ])
    def update_graph(region, status):
        """
            Construct or update graph according to input from 'region-selection' dropdown menu.

            :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
            :return: Plot.ly graph object, produced by don_rate_avg_don().
        """

        # Donation rate data, filtered for selected region and demographic group (education)
        # Corresponding name assigned
        dff1 = PropTotDon_2018[PropTotDon_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == status]
        name1 = "Pourcentage de la population"

        # Average annual donation data, filtered for selected region and demographic group (education)
        # Corresponding name assigned
        dff2 = PropTotDonAmt_2018[PropTotDonAmt_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == status]
        name2 = "Pourcentage de la valeur des dons"

        # Format title according to dropdown input
        title = '{}, {}'.format(
            "Pourcentage de la population et de la valeur totale des dons<br>selon " +
            str(status).lower(),
            region)

        # Uses external function with dataframes, names, and title set up above
        return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-4
        dash.dependencies.Output('PrimCauseNumCause-other13_fr', 'figure'),
        [
            # Inputs: selected region from region-selection and selected
            # demographic group from graph-4-demos (dropdown menu)
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('status-selection3', 'value')
        ])
    def update_graph(region, status):
        """
            Construct or update graph according to input from 'region-selection' dropdown menu.

            :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
            :param demo: Demographic group name (str). Automatically inherited from 'graph-4-demos' dcc.Dropdown() input via dash.dependencies.Input('graph-4-demos', 'value') above.
            :return: Plot.ly graph object, produced by don_rate_avg_don().
        """

        # Average number of annual donations data, filtered for selected region and demographic group
        # Corresponding name assigned
        dff1 = AvgNumCauses_2018[AvgNumCauses_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == status]
        name1 = "Nombre moyen de causes"

        # Average number of causes supported data, filtered for selected region and demographic group
        # Corresponding name assigned
        dff2 = TopCauseFocus_2018[TopCauseFocus_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == status]
        name2 = "Concentration moyenne sur la 1ère cause"

        # Format title according to dropdown input
        title = '{}, {}'.format(
            "Concentration sur la cause principale et nombre <br> moyen de causes soutenues<br>selon " +
            str(status).lower(),
            region)

        # Uses external function with dataframes, names, and title set up above
        return prim_cause_num_cause(dff2, dff1, name2, name1, title)

    # if __name__ == "__main__":
    #     app.run_server(debug=True)
