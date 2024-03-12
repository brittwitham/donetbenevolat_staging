from dash.dependencies import Input, Output
import dash
from .data_processing import data
from .graphs import *

# Rename these accordingly
expectedObstaclesChange, org3MonthObstacles, orgGreatestObstacle = data

def register_callbacks(app):
    @app.callback(
    dash.dependencies.Output('org3MonthObstacles', 'figure'),
    [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        title = f"Au cours des trois prochains mois, quels éléments parmi les suivants constitueront des obstacles pour cette entreprise ou cet organisme? - {geo}"
        df = org3MonthObstacles[(org3MonthObstacles['geoAbb'] == geo) & (org3MonthObstacles['item2'] != "Labour issues")]
        return OrgQuad1(df, title)

    @app.callback(
        dash.dependencies.Output('orgGreatestObstacle', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        title = f"Parmi les obstacles sélectionnés à la question précédente, lequel sera le plus difficile à surmonter au cours des trois prochains mois? - {geo}"
        df = orgGreatestObstacle[orgGreatestObstacle['geoAbb'] == geo]
        return OrgQuad1(df, title)

    @app.callback(
        dash.dependencies.Output('expectedObstaclesChange', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),
        dash.dependencies.Input('expectedObstaclesChange_filter', 'value')])
    def update_graph(geo, item):
        title = f"Au cours des trois prochains mois, quels éléments parmi les suivants constitueront des obstacles pour cette entreprise ou cet organisme? - {geo}"
        df = expectedObstaclesChange[(expectedObstaclesChange['geoAbb'] == geo) & (expectedObstaclesChange['item2'] == item)]
        return OrgQuad2(df, title)
