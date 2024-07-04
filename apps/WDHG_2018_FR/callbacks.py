# Callbacks file for WDHG_2018_FR converted from
# Qui_donne_aux_organismes_caritatifs_et_combien_2018.py

import dash
from .data_processing import *
from .graphs import *
from dash.dependencies import Input, Output, ClientsideFunction


def register_callbacks(app):
    app.clientside_callback(
        ClientsideFunction("clientside", "stickyHeader"),
        Output("sticky", "data-loaded_fr"),  # Just put some dummy output here
        # This will trigger the callback when the object is injected in the DOM
        [Input("sticky", "id")],
    )

    @app.callback(
        # Output: change to graph-1
        dash.dependencies.Output('FormsGiving_fr', 'figure'),
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

    # @app.callback(
    #     dash.dependencies.Output('DonRateAvgDonAmt-prv_fr', 'figure'),
    # #     )
    # def update_graph():

    #     name1 = "Taux de donateur.trice.s"

    #     name2 = "Montant moyen des dons"

    #     # title = 'Region selected: {}'.format(region)
    #     title = '{}, {}'.format("Donation rate and average annual donation by province")

    # return don_rate_avg_don_amt_prv(DonRates_2018, AvgTotDon_2018, name1,
    # name2, title)

    @app.callback(
        dash.dependencies.Output('DonRateAvgDonAmt-Age_fr', 'figure'),
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
            "Taux de donateur.trice.s et montant moyen des dons selon le groupe d'âge",
            region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-1
        dash.dependencies.Output('DonRateAvgDonAmt-Gndr_fr', 'figure'),
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
        name1 = "Taux de donateur.trice.s"

        # Average annual donation data, filtered for selected region and demographic group (age group)
        # Corresponding name assigned
        dff2 = AvgTotDon_2018[AvgTotDon_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Genre"]
        name2 = "Dons annuels moyens"

        # Format title according to dropdown input
        title = '{}, {}'.format(
            "Taux de donateur.trice.s et montant moyen des dons selon le genre", region)

        # Uses external function with dataframes, names, and title set up above
        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-2
        dash.dependencies.Output('PercDon-Gndr_fr', 'figure'),
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
            "Pourcentage de la population et de la valeur totale des dons selon le genre",
            region)

        # Uses external function with dataframes, names, and title set up above
        return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-4
        dash.dependencies.Output('PrimCauseNumCause-Gndr_fr', 'figure'),
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
            "Concentration sur la cause principale et nombre moyen de causes soutenues selon le genre",
            region)

        # Uses external function with dataframes, names, and title set up above
        return prim_cause_num_cause(dff2, dff1, name2, name1, title)

    @app.callback(
        # Output: change to graph-2
        dash.dependencies.Output('PercDon-Age_fr', 'figure'),
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
            "Pourcentage de la population et de la valeur totale des dons selon l’âge",
            region)

        # Uses external function with dataframes, names, and title set up above
        return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-4
        dash.dependencies.Output('PrimCauseNumCause-Age_fr', 'figure'),
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
            "Concentration sur la cause principale et nombre moyen de causes soutenues selon l’âge",
            region)

        # Uses external function with dataframes, names, and title set up above
        return prim_cause_num_cause(dff2, dff1, name2, name1, title)

    @app.callback(
        # Output: change to graph-1
        dash.dependencies.Output('DonRateAvgDonAmt-Educ_fr', 'figure'),
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
        name1 = "Taux de donateur.trice.s"

        # Average annual donation data, filtered for selected region and demographic group (age group)
        # Corresponding name assigned
        dff2 = AvgTotDon_2018[AvgTotDon_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Éducation"]
        name2 = "Dons annuels moyens"

        # Format title according to dropdown input
        title = '{}, {}'.format(
            "Taux de donateur.trice.s et montant moyen des dons selon l’éducation", region)

        # Uses external function with dataframes, names, and title set up above
        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-2
        dash.dependencies.Output('PercDon-Educ_fr', 'figure'),
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
            "Pourcentage de la population et de la valeur totale des dons selon l’éducation",
            region)

        # Uses external function with dataframes, names, and title set up above
        return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-4
        dash.dependencies.Output('PrimCauseNumCause-Educ_fr', 'figure'),
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
            "Concentration sur la cause principale et nombre moyen de causes soutenues selon l’éducation ",
            region)

        # Uses external function with dataframes, names, and title set up above
        return prim_cause_num_cause(dff2, dff1, name2, name1, title)

    @app.callback(
        # Output: change to graph-1
        dash.dependencies.Output('DonRateAvgDonAmt-Inc_fr', 'figure'),
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
            "Taux de donateur.trice.s et montant moyen des dons selon le revenu", region)

        # Uses external function with dataframes, names, and title set up above
        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-2
        dash.dependencies.Output('PercDon-Inc_fr', 'figure'),
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
            "Pourcentage de la population et de la valeur totale des dons selon le revenu",
            region)

        # Uses external function with dataframes, names, and title set up above
        return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-4
        dash.dependencies.Output('PrimCauseNumCause-Inc_fr', 'figure'),
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
            "Concentration sur la cause principale et nombre moyen de causes soutenues selon le revenu",
            region)

        # Uses external function with dataframes, names, and title set up above
        return prim_cause_num_cause(dff2, dff1, name2, name1, title)

    @app.callback(
        # Output: change to graph-1
        dash.dependencies.Output('DonRateAvgDonAmt-Relig_fr', 'figure'),
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
        name1 = "Taux de donateur.trice.s"

        # Average annual donation data, filtered for selected region and demographic group (age group)
        # Corresponding name assigned
        dff2 = AvgTotDon_2018[AvgTotDon_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] ==
                    "Fréquence de la fréquentation religieuse"]
        name2 = "Dons annuels moyens"

        # Format title according to dropdown input
        title = '{}, {}'.format(
            "Taux de donateur.trice.s et montant moyen des dons selon la pratique religieuse",
            region)

        # Uses external function with dataframes, names, and title set up above
        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-2
        dash.dependencies.Output('PercDon-Relig_fr', 'figure'),
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
            "Pourcentage de la population et de la valeur totale des dons selon la pratique religieuse",
            region)

        # Uses external function with dataframes, names, and title set up above
        return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-4
        dash.dependencies.Output('PrimCauseNumCause-Relig_fr', 'figure'),
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
            "Concentration sur la cause principale et nombre moyen de causes soutenues selon la pratique religieuse ",
            region)

        # Uses external function with dataframes, names, and title set up above
        return prim_cause_num_cause(dff2, dff1, name2, name1, title)

    # @app.callback(
    #     # Output: change to graph-1
    #     dash.dependencies.Output('DonRateAvgDonAmt-MarStat', 'figure'),
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
    #     dff1 = DonRates_2018[DonRates_2018['Region'] == region]
    #     dff1 = dff1[dff1['Group'] == "Marital status"]
    #     name1 = "Donation rate"

    #     # Average annual donation data, filtered for selected region and demographic group (age group)
    #     # Corresponding name assigned
    #     dff2 = AvgTotDon_2018[AvgTotDon_2018['Region'] == region]
    #     dff2 = dff2[dff2['Group'] == "Marital status"]
    #     name2 = "Average annual donations"

    #     # Format title according to dropdown input
    #     title = '{}, {}'.format("Donation rate and average annual donation by marital status", region)

    #     # Uses external function with dataframes, names, and title set up above
    #     return don_rate_avg_don(dff1, dff2, name1, name2, title)

    # @app.callback(
    #     # Output: change to graph-1
    #     dash.dependencies.Output('DonRateAvgDonAmt-Labour', 'figure'),
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
    #     dff1 = DonRates_2018[DonRates_2018['Region'] == region]
    #     dff1 = dff1[dff1['Group'] == "Labour force status"]
    #     name1 = "Donation rate"

    #     # Average annual donation data, filtered for selected region and demographic group (age group)
    #     # Corresponding name assigned
    #     dff2 = AvgTotDon_2018[AvgTotDon_2018['Region'] == region]
    #     dff2 = dff2[dff2['Group'] == "Labour force status"]
    #     name2 = "Average annual donations"

    #     # Format title according to dropdown input
    #     title = '{}, {}'.format("Donation rate and average annual donation by employment status", region)

    #     # Uses external function with dataframes, names, and title set up above
    #     return don_rate_avg_don(dff1, dff2, name1, name2, title)

    # @app.callback(
    #     # Output: change to graph-1
    #     dash.dependencies.Output('DonRateAvgDonAmt-ImmStat', 'figure'),
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
    #     dff1 = DonRates_2018[DonRates_2018['Region'] == region]
    #     dff1 = dff1[dff1['Group'] == "Immigration status"]
    #     name1 = "Donation rate"

    #     # Average annual donation data, filtered for selected region and demographic group (age group)
    #     # Corresponding name assigned
    #     dff2 = AvgTotDon_2018[AvgTotDon_2018['Region'] == region]
    #     dff2 = dff2[dff2['Group'] == "Immigration status"]
    #     name2 = "Average annual donations"

    #     # Format title according to dropdown input
    #     title = '{}, {}'.format("Donation rate and average annual donation by immigration status", region)

    #     # Uses external function with dataframes, names, and title set up above
    #     return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-1
        dash.dependencies.Output('DonRateAvgDonAmt-other_fr', 'figure'),
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
            "Taux de donateur.trice.s et montant moyen des dons selon " +
            str(status).lower(),
            region)

        # Uses external function with dataframes, names, and title set up above
        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    # @app.callback(
    #     # Output: change to graph-2
    #     dash.dependencies.Output('PercDon-MarStat', 'figure'),
    #     [
    #         # Input: selected region from region-selection (dropdown menu)
    #         # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     """
    # Construct or update graph according to input from 'region-selection'
    # dropdown menu.

    #         :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
    #         :return: Plot.ly graph object, produced by don_rate_avg_don().
    #     """

    #     # Donation rate data, filtered for selected region and demographic group (education)
    #     # Corresponding name assigned
    #     dff1 = PropTotDon_2018[PropTotDon_2018['Region'] == region]
    #     dff1 = dff1[dff1['Group'] == "Marital status (original)"]
    #     name1 = "Proportion of donors"

    #     # Average annual donation data, filtered for selected region and demographic group (education)
    #     # Corresponding name assigned
    #     dff2 = PropTotDonAmt_2018[PropTotDonAmt_2018['Region'] == region]
    #     dff2 = dff2[dff2['Group'] == "Marital status"]
    #     name2 = "Percentage of donation value"

    #     # Format title according to dropdown input
    #     title = '{}, {}'.format("Percentage of Canadians & total donation value by marital status", region)

    #     # Uses external function with dataframes, names, and title set up above
    #     return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    # @app.callback(
    #     # Output: change to graph-2
    #     dash.dependencies.Output('PercDon-Labour', 'figure'),
    #     [
    #         # Input: selected region from region-selection (dropdown menu)
    #         # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     """
    # Construct or update graph according to input from 'region-selection'
    # dropdown menu.

    #         :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
    #         :return: Plot.ly graph object, produced by don_rate_avg_don().
    #     """

    #     # Donation rate data, filtered for selected region and demographic group (education)
    #     # Corresponding name assigned
    #     dff1 = PropTotDon_2018[PropTotDon_2018['Region'] == region]
    #     dff1 = dff1[dff1['Group'] == "Labour force status"]
    #     name1 = "Proportion of donors"

    #     # Average annual donation data, filtered for selected region and demographic group (education)
    #     # Corresponding name assigned
    #     dff2 = PropTotDonAmt_2018[PropTotDonAmt_2018['Region'] == region]
    #     dff2 = dff2[dff2['Group'] == "Labour force status"]
    #     name2 = "Percentage of donation value"

    #     # Format title according to dropdown input
    #     title = '{}, {}'.format("Percentage of Canadians & total donation value by employment", region)

    #     # Uses external function with dataframes, names, and title set up above
    #     return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    # @app.callback(
    #     # Output: change to graph-2
    #     dash.dependencies.Output('PercDon-ImmStat', 'figure'),
    #     [
    #         # Input: selected region from region-selection (dropdown menu)
    #         # In the case of multiple inputs listed here, they will enter as arguments into the function below in the order they are listed
    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     """
    # Construct or update graph according to input from 'region-selection'
    # dropdown menu.

    #         :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
    #         :return: Plot.ly graph object, produced by don_rate_avg_don().
    #     """

    #     # Donation rate data, filtered for selected region and demographic group (education)
    #     # Corresponding name assigned
    #     dff1 = PropTotDon_2018[PropTotDon_2018['Region'] == region]
    #     dff1 = dff1[dff1['Group'] == "Immigration status"]
    #     name1 = "Proportion of donors"

    #     # Average annual donation data, filtered for selected region and demographic group (education)
    #     # Corresponding name assigned
    #     dff2 = PropTotDonAmt_2018[PropTotDonAmt_2018['Region'] == region]
    #     dff2 = dff2[dff2['Group'] == "Immigration status"]
    #     name2 = "Percentage of donation value"

    #     # Format title according to dropdown input
    #     title = '{}, {}'.format("Percentage of Canadians & total donation value by immigration status", region)

    #     # Uses external function with dataframes, names, and title set up above
    #     return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    @app.callback(
        # Output: change to graph-2
        dash.dependencies.Output('PercDon-other_fr', 'figure'),
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
            "Pourcentage de la population et de la valeur totale des dons selon " +
            str(status).lower(),
            region)

        # Uses external function with dataframes, names, and title set up above
        return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    # @app.callback(
    #     # Output: change to graph-4
    #     dash.dependencies.Output('PrimCauseNumCause-MarStat', 'figure'),
    #     [
    #         # Inputs: selected region from region-selection and selected demographic group from graph-4-demos (dropdown menu)
    #         dash.dependencies.Input('region-selection', 'value'),
    #     ])
    # def update_graph(region):
    #     """
    # Construct or update graph according to input from 'region-selection'
    # dropdown menu.

    #         :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
    #         :param demo: Demographic group name (str). Automatically inherited from 'graph-4-demos' dcc.Dropdown() input via dash.dependencies.Input('graph-4-demos', 'value') above.
    #         :return: Plot.ly graph object, produced by don_rate_avg_don().
    #     """

    #     # Average number of annual donations data, filtered for selected region and demographic group
    #     # Corresponding name assigned
    #     dff1 = AvgNumCauses_2018[AvgNumCauses_2018['Region'] == region]
    #     dff1 = dff1[dff1['Group'] == "Marital status"]
    #     name1 = "Average number of causes"

    #     # Average number of causes supported data, filtered for selected region and demographic group
    #     # Corresponding name assigned
    #     dff2 = TopCauseFocus_2018[TopCauseFocus_2018['Region'] == region]
    #     dff2 = dff2[dff2['Group'] == "Marital status"]
    #     name2 = "Average concentration on first cause"

    #     # Format title according to dropdown input
    #     title = '{}, {}'.format("Focus on primary cause & average number of causes supported by marital status", region)

    #     # Uses external function with dataframes, names, and title set up above
    #     return prim_cause_num_cause(dff2, dff1, name2, name1, title)

    # @app.callback(
    #     # Output: change to graph-4
    #     dash.dependencies.Output('PrimCauseNumCause-Labour', 'figure'),
    #     [
    #         # Inputs: selected region from region-selection and selected demographic group from graph-4-demos (dropdown menu)
    #         dash.dependencies.Input('region-selection', 'value'),
    #     ])
    # def update_graph(region):
    #     """
    # Construct or update graph according to input from 'region-selection'
    # dropdown menu.

    #         :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
    #         :param demo: Demographic group name (str). Automatically inherited from 'graph-4-demos' dcc.Dropdown() input via dash.dependencies.Input('graph-4-demos', 'value') above.
    #         :return: Plot.ly graph object, produced by don_rate_avg_don().
    #     """

    #     # Average number of annual donations data, filtered for selected region and demographic group
    #     # Corresponding name assigned
    #     dff1 = AvgNumCauses_2018[AvgNumCauses_2018['Region'] == region]
    #     dff1 = dff1[dff1['Group'] == "Labour force status"]
    #     name1 = "Average number of causes"

    #     # Average number of causes supported data, filtered for selected region and demographic group
    #     # Corresponding name assigned
    #     dff2 = TopCauseFocus_2018[TopCauseFocus_2018['Region'] == region]
    #     dff2 = dff2[dff2['Group'] == "Labour force status"]
    #     name2 = "Average concentration on first cause"

    #     # Format title according to dropdown input
    #     title = '{}, {}'.format("Focus on primary cause & average number of causes supported by employment status", region)

    #     # Uses external function with dataframes, names, and title set up above
    #     return prim_cause_num_cause(dff2, dff1, name2, name1, title)

    # @app.callback(
    #     # Output: change to graph-4
    #     dash.dependencies.Output('PrimCauseNumCause-ImmStat', 'figure'),
    #     [
    #         # Inputs: selected region from region-selection and selected demographic group from graph-4-demos (dropdown menu)
    #         dash.dependencies.Input('region-selection', 'value'),
    #     ])
    # def update_graph(region):
    #     """
    # Construct or update graph according to input from 'region-selection'
    # dropdown menu.

    #         :param region: Region name (str). Automatically inherited from 'region-selection' dcc.Dropdown() input via dash.dependencies.Input('region-selection', 'value') above.
    #         :param demo: Demographic group name (str). Automatically inherited from 'graph-4-demos' dcc.Dropdown() input via dash.dependencies.Input('graph-4-demos', 'value') above.
    #         :return: Plot.ly graph object, produced by don_rate_avg_don().
    #     """

    #     # Average number of annual donations data, filtered for selected region and demographic group
    #     # Corresponding name assigned
    #     dff1 = AvgNumCauses_2018[AvgNumCauses_2018['Region'] == region]
    #     dff1 = dff1[dff1['Group'] == "Immigration status"]
    #     name1 = "Average number of causes"

    #     # Average number of causes supported data, filtered for selected region and demographic group
    #     # Corresponding name assigned
    #     dff2 = TopCauseFocus_2018[TopCauseFocus_2018['Region'] == region]
    #     dff2 = dff2[dff2['Group'] == "Immigration status"]
    #     name2 = "Average concentration on first cause"

    #     # Format title according to dropdown input
    #     title = '{}, {}'.format("Focus on primary cause & average number of causes supported by immigration status", region)

    #     # Uses external function with dataframes, names, and title set up above
    #     return prim_cause_num_cause(dff2, dff1, name2, name1, title)

    @app.callback(
        # Output: change to graph-4
        dash.dependencies.Output('PrimCauseNumCause-other3_fr', 'figure'),
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
            "Concentration sur la cause principale et nombre <br> moyen de causes soutenues selon " +
            str(status).lower(),
            region)

        # Uses external function with dataframes, names, and title set up above
        return prim_cause_num_cause(dff2, dff1, name2, name1, title)


# if __name__ == "__main__":
#     app.run_server(debug=True)
