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
        title = f"Pourcentage et montant du PIB des organismes à but non lucratif par sous-secteur - {geo}"
        df = gdpSubSec[gdpSubSec['geo'] == geo]
        return SubSec(df, title)

    @app.callback(
        dash.dependencies.Output('gdpGrowth', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        title = f"Croissance relative du PIB nominal par sous-secteur, {geo} - 2007 - 2021 (2007 = 1.0)"
        df = gdpGrowth[gdpGrowth['geo'] == geo]
        trace_settings = {'TotEcon': {'name': "Ensemble de l'économie",
                                      'line_dict': dict(color="#6F2DA4", dash="solid")},
                          'TotNPOs': {'name': "Tous les organismes<br>à but non lucratif",
                                      'line_dict': dict(color="#FCD12A", dash="solid")},
                          'CommNPOs': {'name': "Organismes communautaires<br>à but non lucratif",
                                       'line_dict': dict(color="#FD7B5F", dash="dash")},
                          'BusNPOs': {'name': "institutions commerciales<br>but non lucratif",
                                      "line_dict": dict(color="#FD7B5F", dash="dot")},
                          'GovNPOs': {'name': "Institutions gouvernementales<br>à but non lucratif",
                                      'line_dict': dict(color="#234C66", dash="dash")}
                          }
        return Growth(df, title, trace_settings)

    @app.callback(
        dash.dependencies.Output('gdpSubSecActivity', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        gdpSubSecActivity['refDate'] = pd.to_datetime(
            gdpSubSecActivity['refDate'])

        title = "<br>".join(textwrap.wrap(f"Pourcentage du PIB des organismes à but non lucratif par sous-secteur et par secteur d'activités ({geo}) - " + str(
            min(gdpSubSecActivity['refDate'].dt.year)), width=80))
        df = gdpSubSecActivity[gdpSubSecActivity['geo'] == geo]
        return SubSecActivity(df, title, ('perCoreGDP', 'perGovtGDP'))
