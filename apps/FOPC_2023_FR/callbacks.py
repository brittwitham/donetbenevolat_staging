from dash.dependencies import Input, Output
import dash
from .data_processing import data
from .graphs import *

# Rename these accordingly
futureOutlook, futureOutlookByQuarter, org3MonthExpectations, org3MonthExpectations_facet = data

def register_callbacks(app): 
    @app.callback(
    dash.dependencies.Output('FutureOutlook', 'figure'),
    [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        title = f"Quelles sont les perspectives d'avenir de cette entreprise ou de cet organisme pour les douze prochains mois? - {geo}"
        df = futureOutlook[futureOutlook['geoAbb'] == geo]
        return FutureOptimism(df, title, 'busChar')

    @app.callback(
        dash.dependencies.Output('futureOutlookByQuarter', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),
        dash.dependencies.Input('busChar-selection', 'value'),])
    def update_graph(geo, bus):
        title = f"Quelles sont les perspectives d'avenir de cette entreprise ou de cet organisme pour les douze prochains mois? - {geo}"
        df = futureOutlookByQuarter[(futureOutlookByQuarter['geoAbb'] == geo) & (futureOutlookByQuarter['busChar'] == bus)]
        return FutureOptimism(df, title, "dateLabel")
    
    @app.callback(
    dash.dependencies.Output('org3MonthExpectations_facet', 'figure'),
    [dash.dependencies.Input('geo-selection', 'value')])
    def update_graph(geo):
        title = f"Au cours des trois prochains mois, à quel point chacun des éléments suivants changera-t-il au sein de cette entreprise ou de cet organisme? - {geo}"
        df = org3MonthExpectations_facet[(org3MonthExpectations['geoAbb'] == geo)]
        return FutureFacet(df, title)

    @app.callback(
        dash.dependencies.Output('org3MonthExpectations', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),
        dash.dependencies.Input('item2-selection', 'value'),])
    def update_graph(geo, item):
        title = f"Au cours des trois prochains mois, à quel point chacun des éléments suivants changera-t-il au sein de cette entreprise ou de cet organisme? - {geo}"
        df = org3MonthExpectations[(org3MonthExpectations['geoAbb'] == geo) & (org3MonthExpectations['item2'] == item)]
        return FutureExpectations(df, title)
