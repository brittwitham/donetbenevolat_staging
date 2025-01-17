import dash
from app import app
from .data_processing import get_data
from .graphs import *
import textwrap

empGrowth, empSubSec, empSubSecActivity, empGrowthActivity = get_data()


def register_callbacks(app):
    @app.callback(
        dash.dependencies.Output('empSubSec', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        title = f"Emploi dans les organismes à but non lucratif par sous-secteur, 2021 - {geo}"
        df = empSubSec[empSubSec['geo'] == geo]
        return SubSec(df, title)

    @app.callback(
        dash.dependencies.Output('empGrowth', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        title = f"Croissance relative de l'emploi par sous-secteur, {geo} - 2007 - 2021 (2007 = 1.0)"
        df = empGrowth[empGrowth['geo'] == geo]
        trace_settings = {
            'valNormP_TotNPOs': {
                'name': "Tous les organismes à but non lucratif", 'line_dict': dict(
                    color="#6F2DA4", dash="solid")}, 'valNormP_CommNPOs': {
                'name': "Organismes communautaires à but non lucratif", 'line_dict': dict(
                    color="#FD7B5F", dash="dash")}, 'valNormP_BusNPOs': {
                        'name': "institutions commerciales à but non lucratif", 'line_dict': dict(
                            color="#FD7B5F", dash="dot")}, 'valNormP_GovNPOs': {
                                'name': "Institutions gouvernementales à but non lucratif", "line_dict": dict(
                                    color="#234C66", dash="dash")}}
        return Growth(df, title, trace_settings)

    @app.callback(
        dash.dependencies.Output('empSubSecActivity', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        # + str(min(empSubSecActivity['refDate'].dt.year))
        title = "<br>".join(textwrap.wrap(f"Pourcentage de l'emploi dans les organismes à but non lucratif par sous-secteur et par secteur d'activités ({geo}) - 2021", width=80))
        df = empSubSecActivity[empSubSecActivity['geo'] == geo]
        return SubSecActivity(df, title, ('percoreEmp', 'pergovtEmp'))

    @app.callback(
        dash.dependencies.Output('empGrowthActivity_core', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        title = f"Relative growth of employment by core activity area, {geo} - 2007 - 2021 (2007 = 1.0)"
        df = empGrowthActivity[empGrowthActivity['geo'] == geo]
        trace_settings = {'valNormP_coreEmp_Sports': {'name': "Sports & rec.",
                                                      'line_dict': dict(color="#6F2DA4", dash="solid")},
                          'valNormP_coreEmp_Education': {'name': "Éducation",
                                                         'line_dict': dict(color="#6F2DA4", dash="dash")},
                          'valNormP_coreEmp_Health': {'name': "Santé",
                                                      'line_dict': dict(color="#6F2DA4", dash="dot")},
                          'valNormP_coreEmp_SocServ': {'name': "Services sociaux",
                                                       'line_dict': dict(color="#FD7B5F", dash="solid")},
                          'valNormP_coreEmp_Environment': {'name': "Environnement",
                                                           'line_dict': dict(color="#FD7B5F", dash="dash")},
                          'valNormP_coreEmp_DevtHousing': {'name': "Dévt. et logement",
                                                           'line_dict': dict(color="#FD7B5F", dash="dot")},
                          'valNormP_coreEmp_Advocacy': {'name': "Défense des intérêts",
                                                        'line_dict': dict(color="#234C66", dash="solid")},
                          'valNormP_coreEmp_Religion': {'name': "Religion",
                                                        'line_dict': dict(color="#234C66", dash="dash")},
                          'valNormP_coreEmp_Fdns': {'name': "Intermédiaires<br>philanthropiques",
                                                    'line_dict': dict(color="#234C66", dash="dot")},
                          'valNormP_coreEmp_International': {'name': "International",
                                                             'line_dict': dict(color="#0B6623", dash="solid")},
                          'valNormP_coreEmp_ProfAssoc': {'name': "Associations<br>professionnelles",
                                                         'line_dict': dict(color="#0B6623", dash="dash")},
                          'valNormP_coreEmp_Other': {'name': "Autre",
                                                     'line_dict': dict(color="#0B6623", dash="dot")}
                          }
        return Growth(df, title, trace_settings)

    @app.callback(
        dash.dependencies.Output('empGrowthActivity_govt', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        title = f"Relative growth of employment by government activity area, {geo} - 2007 - 2021 (2007 = 1.0)"
        df = empGrowthActivity[empGrowthActivity['geo'] == geo]
        trace_settings = {
            'valNormP_govtEmp_Health': {
                'name': "Santé & social services", 'line_dict': dict(
                    color="#FD7B5F", dash="solid")}, 'valNormP_govtEmp_Education': {
                'name': "Éducation", 'line_dict': dict(
                    color="#234C66", dash="dash")}}
        return Growth(df, title, trace_settings)
