import dash
from app import app
from .data_processing import get_data
from .graphs import *

revGrowth, revSubSec, revSubSecActivity, revGrowthActivity, revSource, revGrowthSource = get_data()


def register_callbacks(app):
    @app.callback(
        dash.dependencies.Output('revSubSec', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value')])
    def update_graph(geo):
        df = revSubSec[revSubSec['geo'] == geo]
        # TODO: Does the year need to update dynamically?
        title = "Nonprofit revenue by sub-sector, 2021" + " - " + geo
        return SubSec(df, title)

    @app.callback(
        dash.dependencies.Output('revGrowth', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value')])
    def update_graph(geo):
        df = revGrowth[revGrowth['geo'] == geo]
        # TODO: Does the year need to update dynamically?

        revGrowth['refDate'] = pd.to_datetime(revGrowth['refDate'])

        title = "Relative growth of revenues by sub-sector, " + str(min(revGrowth['refDate'].dt.year)) + " to " + str(max(revGrowth['refDate'].dt.year)) + " - " + geo + " (" + str(
            min(revGrowth['refDate'].dt.year)) + " = 1.0)" + '<br>' + '<sup>' + "Note: Hover over line for absolute values" + '</sup>'
        trace_settings = {
            'valNormP_TotNPOs': {
                'name': "All nonprofits", 'line_dict': dict(
                    color="#7A4A89", dash="solid")}, 'valNormP_CommNPOs': {
                'name': "Community nonprofits", 'line_dict': dict(
                    color="#c8102e", dash="dash")}, 'valNormP_BusNPOs': {
                        'name': "Business nonprofits", 'line_dict': dict(
                            color="#c8102e", dash="dot")}, 'valNormP_GovNPOs': {
                                'name': "Government nonprofits", 'line_dict': dict(
                                    color="#7BAFD4", dash="dash")}}
        return Growth(df, title, trace_settings)

    @app.callback(
        dash.dependencies.Output('revSubSecActivity', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value')])
    def update_graph(geo):
        df = revSubSecActivity[revSubSecActivity['geo'] == geo]
        # TODO: Does the year need to update dynamically?
        title = "Percentage of nonprofit revenues by sub-sector and activity area, 2021" + \
            " - " + geo + '<br>' + '<sup>' + "Note: Hover over bar for absolute values" + '</sup>'
        vars = ('perCoreRev', 'perGovtRev')
        return SubSecActivity(df, title, vars)

    @app.callback(
        dash.dependencies.Output('revGrowthActivity_core', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value')])
    def update_graph(geo):
        df = revGrowthActivity[revGrowthActivity['geo'] == geo]

        revGrowthActivity['refDate'] = pd.to_datetime(
            revGrowthActivity['refDate'])

        # TODO: Does the year need to update dynamically?
        title = "Relative growth of revenues by core activity area, " + str(min(revGrowthActivity['refDate'].dt.year)) + " to " + str(max(revGrowthActivity['refDate'].dt.year)) + " - " + geo + " (" + str(
            min(revGrowthActivity['refDate'].dt.year)) + " = 1.0)" + '<br>' + '<sup>' + "Note: Hover over line for absolute values" + '</sup>'
        trace_settings = {'valNormP_coreRev_Sports': {'name': "Sports & rec.",
                                                      'line_dict': dict(color="#7A4A89", dash="solid")},
                          'valNormP_coreRev_Education': {'name': "Education",
                                                         'line_dict': dict(color="#7A4A89", dash="dash")},
                          'valNormP_coreRev_Health': {'name': "Health",
                                                      'line_dict': dict(color="#7A4A89", dash="dot")},
                          'valNormP_coreRev_SocServ': {'name': "Social services",
                                                       'line_dict': dict(color="#c8102e", dash="solid")},
                          'valNormP_coreRev_Environment': {'name': "Environment",
                                                           'line_dict': dict(color="#c8102e", dash="dash")},
                          'valNormP_coreRev_DevtHousing': {'name': "Devt. & housing",
                                                           'line_dict': dict(color="#c8102e", dash="dot")},
                          'valNormP_coreRev_Advocacy': {'name': "Advocacy",
                                                        'line_dict': dict(color="#7BAFD4", dash="solid")},
                          'valNormP_coreRev_Religion': {'name': "Religion",
                                                        'line_dict': dict(color="#7BAFD4", dash="dash")},
                          'valNormP_coreRev_Fdns': {'name': "Philanthropic<br>intermediaries",
                                                    'line_dict': dict(color="#7BAFD4", dash="dot")},
                          'valNormP_coreRev_International': {'name': "International",
                                                             'line_dict': dict(color="#50a684", dash="solid")},
                          'valNormP_coreRev_ProfAssoc': {'name': "Professional<br>associations",
                                                         'line_dict': dict(color="#50a684", dash="dash")},
                          'valNormP_coreRev_Other': {'name': "Other",
                                                     'line_dict': dict(color="#50a684", dash="dot")}}
        return Growth(df, title, trace_settings)

    @app.callback(
        dash.dependencies.Output('revGrowthActivity_gov', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value')])
    def update_graph(geo):
        df = revGrowthActivity[revGrowthActivity['geo'] == geo]

        revGrowthActivity['refDate'] = pd.to_datetime(
            revGrowthActivity['refDate'])

        # TODO: Does the year need to update dynamically?
        title = "Relative growth of revenues by government activity area, " + str(min(revGrowthActivity['refDate'].dt.year)) + " to " + str(max(
            revGrowthActivity['refDate'].dt.year)) + " - " + geo + " (" + str(min(revGrowthActivity['refDate'].dt.year)) + " = 1.0)" + '<br>' + '<sup>' + "Note: Hover over line for absolute values" + '</sup>'
        trace_settings = {
            'valNormP_govtRev_Health': {
                'name': "Health & social services", 'line_dict': dict(
                    color="#c8102e", dash="solid")}, 'valNormP_govtRev_Education': {
                'name': "Education", 'line_dict': dict(
                    color="#7BAFD4", dash="dash")}}
        return Growth(df, title, trace_settings)

    @app.callback(
        dash.dependencies.Output('revSource', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value')])
    def update_graph(geo):
        df = revSource[revSource['geo'] == geo]
        title = "Revenues by source and sub-sector, 2021 - " + geo + '<br>' + \
            '<sup>' + "Note: Hover over line for absolute values" + '</sup>'
        return Source(df, title)

    @app.callback(
        dash.dependencies.Output('revGrowthSource', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value')])
    def update_graph(geo):
        df = revGrowthSource[revGrowthSource['geo'] == geo]

        df['refDate'] = pd.to_datetime(df['refDate'])

        title = "Relative growth of revenue sources by sub-sector, " + str(min(df['refDate'].dt.year)) + " to " + str(max(df['refDate'].dt.year)) + " - " + geo + " (" + str(
            min(df['refDate'].dt.year)) + " = 1.0)" + '<br>' + '<sup>' + "Note: Hover over line for absolute values" + '</sup>'
        return GrowthSource(df, title)
