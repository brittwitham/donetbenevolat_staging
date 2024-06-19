# Callbacks file for UTV_2018_FR converted from Comprendre_les_benevoles_tres_engages_2018.py

import dash
from .data_processing import *
from .graphs import *

def register_callbacks(app):
    @app.callback(
        dash.dependencies.Output('TopVolsTotalHours', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff2 = TopVolsPercTotVols_2018[TopVolsPercTotVols_2018['Region'] == region]
        dff1 = TopVolsPercTotHours_2018[TopVolsPercTotHours_2018['Region'] == region]
        # dff1 = dff1.replace("", "")
        # dff1 = dff1.replace("", "")
        # dff1 = dff1.replace("", "")
        # dff1 = dff1.replace("", "")
        
        dff1 = dff1.replace("% volunteers", "% bénévoles")
        # name1 = "% volunteers"
        name2 = "% bénévoles"
        
        dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
        name1 = "% heures de bénévolat"
        # name2 = "% volunteer hours"

        title = '{}, {}'.format("Répartition des heures de bénévolat totales", region)
        return dist_total_donations(dff1, dff2, name1, name2, title)

    @app.callback(
        dash.dependencies.Output('TopVolsDemographics', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('demo-selection', 'value')
        ])
    def update_graph(region, demo):
        dff = TopVolsDemoLikelihoods[TopVolsDemoLikelihoods['Region'] == region]
        dff = dff[dff['Group'] == demo]

        title = '{}, {}'.format("Probabilité d'être un.e bénévole très engagé.e selon " + str(demo).lower(), region)
        return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('TopVolsSubSecSupport', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = TopVolsVolRates_2018[TopVolsVolRates_2018['Region'] == region]
        dff = dff.replace('Health', 'Santé')
        dff = dff.replace('Social services', 'Services sociaux')
        dff = dff.replace('Hospitals', 'Hôpitaux')
        dff = dff.replace('Grant-making, fundraising', 'Subventions, collecte de fonds')
        dff = dff.replace('Grantmaking, fundraising', 'Subventions, collecte de fonds')
        dff = dff.replace('Sports & recreation', 'Sport et loisir')
        dff = dff.replace('Sports & Recreation', 'Sport et loisir')
        dff = dff.replace('Education & research', 'Éducation et recherche')
        dff = dff.replace('Environment', 'Environnement')
        dff = dff.replace('Law, advocacy & politics', 'Droit, plaidoyer et politique')
        dff = dff.replace('Law, advocacy', 'Droit, plaidoyer et politique')
        dff = dff.replace('Arts & culture', 'Arts et culture')
        dff = dff.replace('Universities & colleges', 'Universités et collèges')
        dff = dff.replace('Development & housing', 'Aménagement et logement')
        dff = dff.replace('Other', 'Autre')
        dff = dff.replace('Business & professional', 'Entreprises et professionnels')
        dff = dff.replace('Top volunteer', 'Bénévoles très engagé.e.s')
        dff = dff.replace('Regular volunteer', 'Autres bénévoles')
        
        name1 = "Bénévoles très engagé.e.s"
        name2 = "Autres bénévoles"

        title = '{}, {}'.format("Niveaux de soutien selon la cause, bénévoles très engagé.e.s et autres bénévoles ", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('TopVolsMotivations', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = TopVolsMotivations_2018[TopVolsMotivations_2018['Region'] == region]
        
        dff = dff.replace('Top volunteer', 'Bénévoles très engagé.e.s')
        dff = dff.replace('Regular volunteer', 'Autres bénévoles')
        
        name1 = "Bénévoles très engagé.e.s"
        name2 = "Autres bénévoles"
        # name1 = "Top volunteer"
        # name2 = "Regular volunteer"

        title = '{}, {}'.format("Motivations du bénévolat, bénévoles très engagé.e.s et autres bénévoles", region)
        return vertical_percentage_graph(dff, title, name1, name2)

    @app.callback(
        dash.dependencies.Output('TopVolsBarriers', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = TopVolsBarriers_2018[TopVolsBarriers_2018['Region'] == region]
        dff = dff.replace('Top volunteer', 'Bénévoles très engagé.e.s')
        dff = dff.replace('Regular volunteer', 'Autres bénévoles')
        
        name1 = "Bénévoles très engagé.e.s"
        name2 = "Autres bénévoles"
        # name1 = "Top volunteer"
        # name2 = "Regular volunteer"

        title = '{}, {}'.format("Freins empêchant de faire plus de bénévolat, bénévoles <br> très engagé.e.s et autres bénévoles", region)
        return vertical_percentage_graph(dff, title, name1, name2)


