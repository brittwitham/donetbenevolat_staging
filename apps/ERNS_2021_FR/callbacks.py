import dash
from app import app
from .data_processing import get_data
from .graphs import *


gdpGrowth, gdpSubSec, gdpSubSecActivity, perNatGDP = get_data()


def register_callbacks(app):
    @app.callback(
        dash.dependencies.Output('gdpSubSec', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        title = f"Percentage and amount of nonprofit GDP by sub-sector - {geo}"
        df = gdpSubSec[gdpSubSec['geo'] == geo]
        return SubSec(df, title)

    @app.callback(
        dash.dependencies.Output('gdpGrowth', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        title = f"Relative growth of nominal GDP by sub-sector, {geo} - 2009 - 2021 (2009 = 1.0)"
        df = gdpGrowth[gdpGrowth['geo'] == geo]
        trace_settings = {'TotEcon': {'name': "Total<br>economy",
                                      'line_dict': dict(color="#7A4A89", dash="solid")},
                          'TotNPOs': {'name': "All<br>nonprofits",
                                      'line_dict': dict(color="#ffc72c", dash="solid")},
                          'CommNPOs': {'name': "Community<br>nonprofits",
                                       'line_dict': dict(color="#c8102e", dash="dash")},
                          'BusNPOs': {'name': "Business<br>nonprofits",
                                      "line_dict": dict(color="#c8102e", dash="dot")},
                          'GovNPOs': {'name': "Gouvernement<br>nonprofits",
                                      'line_dict': dict(color="#7BAFD4", dash="dash")}
                          }
        return Growth(df, title, trace_settings)

    @app.callback(
        dash.dependencies.Output('gdpSubSecActivity', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        gdpSubSecActivity['refDate'] = pd.to_datetime(
            gdpSubSecActivity['refDate'])

        title = f"Percentage of nonprofit GDP by sub-sector and activity area ({geo}) - " + str(
            min(gdpSubSecActivity['refDate'].dt.year))
        df = gdpSubSecActivity[gdpSubSecActivity['geo'] == geo]
        return SubSecActivity(df, title, ('perCoreGDP', 'perGovtGDP'))
