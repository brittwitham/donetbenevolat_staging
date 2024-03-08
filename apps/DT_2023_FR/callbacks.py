from dash.dependencies import Input, Output
import dash
from .data_processing import data
from .graphs import *

# Rename these accordingly
donationChallenges, donationChallengesDetailed, donationImpact, donationImpactDetailed = data

def register_callbacks(app):
    @app.callback(
    dash.dependencies.Output('donationChallenges', 'figure'),
    [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        title = f"Quels défis parmi les suivants cet organisme doit-il relever en ce qui a trait aux dons du public? - {geo}"
        df = donationChallenges[donationChallenges['geoAbb'] == geo]
        return DonationDouble(df, title)

    @app.callback(
        dash.dependencies.Output('donationChallengesDetailed', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),
        dash.dependencies.Input('donationChallengesDetailed_filter_1', 'value'),
        dash.dependencies.Input('donationChallengesDetailed_filter_2', 'value')])
    def update_graph(geo, busGroup, item):
        title = f"Quels défis parmi les suivants cet organisme doit-il relever en ce qui a trait aux dons du public? - {geo}"
        df = donationChallengesDetailed[(donationChallengesDetailed['geoAbb'] == geo) &
                                        (donationChallengesDetailed['busGroup'] == busGroup) &
                                        (donationChallengesDetailed['item2'] == item)]
        return DonationSingle(df, title)

    @app.callback(
        dash.dependencies.Output('donationImpact', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        title = f"Quels éléments parmi les suivants constituent des répercussions prévues des défis associés aux dons? - {geo}"
        df = donationImpact[donationImpact['geoAbb'] == geo]
        return DonationDouble(df, title)

    @app.callback(
        dash.dependencies.Output('donationImpactDetailed', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),
        dash.dependencies.Input('donationImpactDetailed_filter_1', 'value'),
        dash.dependencies.Input('donationImpactDetailed_filter_2', 'value')])
    def update_graph(geo, busGroup, item):
        title = f"Quels éléments parmi les suivants constituent des répercussions prévues des défis associés aux dons? - {geo}"
        df = donationImpactDetailed[(donationImpactDetailed['geoAbb'] == geo) &
                                        (donationImpactDetailed['busGroup'] == busGroup) &
                                        (donationImpactDetailed['item2'] == item)]
        return DonationSingle(df, title)