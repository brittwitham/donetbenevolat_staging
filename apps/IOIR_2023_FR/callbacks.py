from dash.dependencies import Input, Output
import dash
from .data_processing import data
from .graphs import *

# Rename these accordingly
greatestImpactInterestRates, impactLevelInterestRates, org3MonthObstaclesImpact, orgExpectedObstaclesChange, orgGreatestObstacleImpact = data

def register_callbacks(app):
    @app.callback(
    dash.dependencies.Output('org3MonthObstaclesImpact', 'figure'),
    [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        title = f"Au cours des trois prochains mois, quels éléments parmi les suivants constitueront des obstacles pour cette entreprise ou cet organisme? - {geo}"
        df = org3MonthObstaclesImpact[org3MonthObstaclesImpact['geoAbb'] == geo]
        return ImpactRates(df, title, 'item2')

    @app.callback(
        dash.dependencies.Output('orgGreatestObstacleImpact', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        title = f"Parmi les obstacles sélectionnés à la question précédente, lequel sera le plus difficile à surmonter au cours des trois prochains mois? - {geo}"
        df = orgGreatestObstacleImpact[orgGreatestObstacleImpact['geoAbb'] == geo]
        return ImpactRates(df, title, 'item2')

    @app.callback(
        dash.dependencies.Output('orgExpectedObstaclesChange', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),
        dash.dependencies.Input('item2-selection', 'value')])
    def update_graph(geo, item):
        title = f"Au cours des trois prochains mois, quels éléments parmi les suivants constitueront des obstacles pour cette entreprise ou cet organisme? - {geo}"
        df = orgExpectedObstaclesChange[(orgExpectedObstaclesChange['geoAbb'] == geo) & (orgExpectedObstaclesChange['item2'] == item)]
        return ImpactOrgType(df, title)

    @app.callback(
        dash.dependencies.Output('greatestImpactInterestRates', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        title = f"Quels éléments parmi les suivants ont été les plus touchés par les taux d'intérêt pour cette entreprise ou cet organisme? - {geo}"
        df = greatestImpactInterestRates[greatestImpactInterestRates['geoAbb'] == geo]
        return ImpactRates(df, title, 'item2')

    @app.callback(
        dash.dependencies.Output('impactLevelInterestRates', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        title = f"Quelle incidence les taux d'intérêt ont-ils eu sur cette entreprise ou cet organisme? - {geo}"
        df = impactLevelInterestRates[impactLevelInterestRates['geoAbb'] == geo]
        df = df.loc[df['item2'].map({"Inconnu": 0, "Aucun": 1, "Faible": 2, "Moyen": 3, "Élevé": 4}).sort_values().index]
        return ImpactOrgVertical(df, title)
