import dash
from app import app
from .data_processing import get_data
from .graphs import *
import textwrap

revGrowth, revSubSec, revSubSecActivity, revGrowthActivity, revSource, revGrowthSource = get_data()


def register_callbacks(app):
    @app.callback(
        dash.dependencies.Output('revSubSec', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value')])
    def update_graph(geo):
        df = revSubSec[revSubSec['geo'] == geo]
        # TODO: Does the year need to update dynamically?
        title = "Revenus des organismes à but non lucratif par sous-secteur, 2021" + " - " + geo
        return SubSec(df, title)

    @app.callback(
        dash.dependencies.Output('revGrowth', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value')])
    def update_graph(geo):
        df = revGrowth[revGrowth['geo'] == geo]
        # TODO: Does the year need to update dynamically?

        revGrowth['refDate'] = pd.to_datetime(revGrowth['refDate'])

        title = "Croissance relative des revenus par sous-secteur, " + str(min(revGrowth['refDate'].dt.year)) + " to " + str(max(revGrowth['refDate'].dt.year)) + " - " + geo + " (" + str(
            min(revGrowth['refDate'].dt.year)) + " = 1.0)" + '<br>' + '<sup>' + " Remarque : placer le curseur sur la ligne pour connaître les valeurs absolues." + '</sup>'
        trace_settings = {
            'valNormP_TotNPOs': {
                'name': "Tous les organismes à but non lucratif", 'line_dict': dict(
                    color="#6F2DA4", dash="solid")}, 'valNormP_CommNPOs': {
                'name': "Organismes communautaires à but non lucratif", 'line_dict': dict(
                    color="#FD7B5F", dash="dash")}, 'valNormP_BusNPOs': {
                        'name': "institutions commerciales à but non lucratif", 'line_dict': dict(
                            color="#FD7B5F", dash="dot")}, 'valNormP_GovNPOs': {
                                'name': "Institutions gouvernementales à but non lucratif", 'line_dict': dict(
                                    color="#234C66", dash="dash")}}
        return Growth(df, title, trace_settings)

    @app.callback(
        dash.dependencies.Output('revSubSecActivity', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value')])
    def update_graph(geo):
        df = revSubSecActivity[revSubSecActivity['geo'] == geo]
        # TODO: Does the year need to update dynamically?
        title = "<br>".join(textwrap.wrap("Pourcentage des revenus des organismes à but non lucratif par sous-secteur et par secteur d'activités, 2021" + \
            " - " + geo, width=80)) + '<br>' + '<sup>' + " Remarque : placer le curseur sur la barre pour connaître le nombre absolu d'employés." + '</sup>'
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
        title = "Croissance relative de par secteur d'activités de base, " + str(min(revGrowthActivity['refDate'].dt.year)) + " to " + str(max(revGrowthActivity['refDate'].dt.year)) + " - " + geo + " (" + str(
            min(revGrowthActivity['refDate'].dt.year)) + " = 1.0)" + '<br>' + '<sup>' + " Remarque : placer le curseur sur la ligne pour connaître les valeurs absolues." + '</sup>'
        trace_settings = {'valNormP_coreRev_Sports': {'name': "Sports & rec.",
                                                      'line_dict': dict(color="#6F2DA4", dash="solid")},
                          'valNormP_coreRev_Education': {'name': "Éducation",
                                                         'line_dict': dict(color="#6F2DA4", dash="dash")},
                          'valNormP_coreRev_Health': {'name': "Santé",
                                                      'line_dict': dict(color="#6F2DA4", dash="dot")},
                          'valNormP_coreRev_SocServ': {'name': "Services sociaux",
                                                       'line_dict': dict(color="#FD7B5F", dash="solid")},
                          'valNormP_coreRev_Environment': {'name': "Environnement",
                                                           'line_dict': dict(color="#FD7B5F", dash="dash")},
                          'valNormP_coreRev_DevtHousing': {'name': "Dévt. et logement",
                                                           'line_dict': dict(color="#FD7B5F", dash="dot")},
                          'valNormP_coreRev_Advocacy': {'name': "Défense des intérêts",
                                                        'line_dict': dict(color="#234C66", dash="solid")},
                          'valNormP_coreRev_Religion': {'name': "Religion",
                                                        'line_dict': dict(color="#234C66", dash="dash")},
                          'valNormP_coreRev_Fdns': {'name': "Intermédiaires<br>philanthropiques",
                                                    'line_dict': dict(color="#234C66", dash="dot")},
                          'valNormP_coreRev_International': {'name': "International",
                                                             'line_dict': dict(color="#0B6623", dash="solid")},
                          'valNormP_coreRev_ProfAssoc': {'name': "Associations<br>professionnelles",
                                                         'line_dict': dict(color="#0B6623", dash="dash")},
                          'valNormP_coreRev_Other': {'name': "Autre",
                                                     'line_dict': dict(color="#0B6623", dash="dot")}}
        return Growth(df, title, trace_settings)

    @app.callback(
        dash.dependencies.Output('revGrowthActivity_gov', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value')])
    def update_graph(geo):
        df = revGrowthActivity[revGrowthActivity['geo'] == geo]

        revGrowthActivity['refDate'] = pd.to_datetime(
            revGrowthActivity['refDate'])

        # TODO: Does the year need to update dynamically?
        title = "Croissance relative des revenus par secteur d'activités gouvernemental, " + str(min(revGrowthActivity['refDate'].dt.year)) + " to " + str(max(
            revGrowthActivity['refDate'].dt.year)) + " - " + geo + " (" + str(min(revGrowthActivity['refDate'].dt.year)) + " = 1.0)" + '<br>' + '<sup>' + " Remarque : placer le curseur sur la ligne pour connaître les valeurs absolues." + '</sup>'
        trace_settings = {
            'valNormP_govtRev_Health': {
                'name': "Santé & social services", 'line_dict': dict(
                    color="#FD7B5F", dash="solid")}, 'valNormP_govtRev_Education': {
                'name': "Éducation", 'line_dict': dict(
                    color="#234C66", dash="dash")}}
        return Growth(df, title, trace_settings)

    @app.callback(
        dash.dependencies.Output('revSource', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value')])
    def update_graph(geo):
        df = revSource[revSource['geo'] == geo]
        title = "Revenus par source et par sous-secteur, 2021 - " + geo + '<br>' + \
            '<sup>' + " Remarque : placer le curseur sur la ligne pour connaître les valeurs absolues." + '</sup>'
        return Source(df, title)

    @app.callback(
        dash.dependencies.Output('revGrowthSource', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value')])
    def update_graph(geo):
        df = revGrowthSource[revGrowthSource['geo'] == geo]

        df['refDate'] = pd.to_datetime(df['refDate'])

        title = "Croissance relative des sources de revenu par sous-secteur, " + str(min(df['refDate'].dt.year)) + " to " + str(max(df['refDate'].dt.year)) + " - " + geo + " (" + str(
            min(df['refDate'].dt.year)) + " = 1.0)" + '<br>' + '<sup>' + " Remarque : placer le curseur sur la ligne pour connaître les valeurs absolues." + '</sup>'
        return GrowthSource(df, title)
