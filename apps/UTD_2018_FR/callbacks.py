# Callbacks file for UTD_2018_FR converted from
# Comprendre_les_grands_donateurs_2018.py

import dash
from .data_processing import *
from .graphs import *


def register_callbacks(app):
    @app.callback(
        dash.dependencies.Output('TopDonorsTotalDonations', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff2 = TopDonorsPercTotDonors_2018[TopDonorsPercTotDonors_2018['Region'] == region]
        dff1 = TopDonorsPercTotDonations_2018[TopDonorsPercTotDonations_2018['Region'] == region]

        name2 = "% donateur.trice.s"
        name1 = "% valeur des dons"

        title = '{}, {}'.format(
            "Répartition de la totalité des dons selon leur montant", region)
        return dist_total_donations(dff1, dff2, name1, name2, title)

    @app.callback(
        dash.dependencies.Output('TopDonorsDemographics', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('demo-selection', 'value')
        ])
    def update_graph(region, demo):
        dff = TopDonorsDemoLikelihoods[TopDonorsDemoLikelihoods['Region'] == region]
        dff = dff[dff['Group'] == demo]

        title = '{}, {}'.format(
            "Probabilité d’être un.e grand.e donateur.trice selon le profil démographique ",
            region)
        return triple_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('TopDonorsSubSecSupport', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = TopDonorsDonRates_2018[TopDonorsDonRates_2018['Region'] == region]

        title = '{}, {}'.format(
            "Niveaux de soutien selon la cause, <br> grand.e.s donateur.trice.s et donateur.trice.s ordinaires",
            region)
        return vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('TopDonorsMotivations', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = TopDonorsMotivations_2018[TopDonorsMotivations_2018['Region'] == region]

        title = '{}, {}'.format(
            "Motivations des dons, grand.e.s donateur.trice.s <br> et donateur.trice.s ordinaires",
            region)
        return vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('TopDonorsBarriers', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = TopDonorsBarriers_2018[TopDonorsBarriers_2018['Region'] == region]

        title = '{}, {}'.format(
            "Freins empêchant de donner plus, grand.e.s <br> donateur.trice.s et donateur.trice.s ordinaires",
            region)
        return vertical_percentage_graph(dff, title)
