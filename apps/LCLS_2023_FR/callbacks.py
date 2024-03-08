from dash.dependencies import Input, Output
import dash
from .data_processing import data
from .graphs import *

# Rename these accordingly
accessLiquidity, accessLiquidityChange, receiveCEBA, statusCEBA, willPayCEBA = data

def register_callbacks(app):
    @app.callback(
        dash.dependencies.Output('accessLiquidity', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        title = f"L'entreprise ou l'organisme a-t-il les avoirs en espèces ou les liquidités nécessaires pour poursuivre ses activités pendant les trois prochains mois? - {geo}"
        df = accessLiquidity[accessLiquidity['geoAbb'] == geo]
        df = df.loc[df['item2'].map({"A suffisamment de liquidités": 4,
                                    "Pourra avoir accès à suffisamment de liquidités": 3,
                                    "Ne pourra pas avoir accès à suffisamment de liquidités": 2,
                                    "Incertain s'il (si elle) pourra avoir accès à suffisamment de liquidités": 1,
                                    "Statut des liquidités inconnu": 0}).sort_values().index]
        return ImpactRates(df, title, 'item2', accessLiquidity=True)

    @app.callback(
        dash.dependencies.Output('accessLiquidityChange', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),
        dash.dependencies.Input('item2-selection', 'value')])
    def update_graph(geo, item):
        title = f"L'entreprise ou l'organisme a-t-il les avoirs en espèces ou les liquidités nécessaires pour poursuivre ses activités pendant les trois prochains mois? - {geo}"
        df = accessLiquidityChange[(accessLiquidityChange['geoAbb'] == geo) & (accessLiquidityChange['item2'] == item)]
        return ImpactOrgType(df, title)

    @app.callback(
        dash.dependencies.Output('receiveCEBA', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        title = f"Cette entreprise ou cet organisme a-t-il obtenu un prêt remboursable du Compte d'urgence pour les entreprises canadiennes (CUEC)? - {geo}"
        df = receiveCEBA[receiveCEBA['geoAbb'] == geo]
        return ReceiveCEBA(df, title)

    @app.callback(
        dash.dependencies.Output('statusCEBA', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        title = f"Le prêt a-t-il été entièrement remboursé? - {geo}"
        df = statusCEBA[statusCEBA['geoAbb'] == geo]
        return StatusCEBA(df, title)

    @app.callback(
        dash.dependencies.Output('willPayCEBA', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        title = f"Cette entreprise ou cet organisme prévoit-il avoir les liquidités ou l'accès au crédit nécessaires pour rembourser son prêt du CUEC d'ici le 31 décembre 2026? - {geo}"
        df = willPayCEBA[willPayCEBA['geoAbb'] == geo]
        df = df.loc[df['item2'].map({"Sera remboursé": 0,
                                    "Ne sera pas remboursé": 1,
                                    "Inconnu": 2}).sort_values().index]
        return ImpactOrgVertical(df, title)
