import dash
from app import app
from .data_processing import get_data
from .graphs import *

jobsType, wagesType, jobsDemog, wagesDemog = get_data()


def register_callbacks(app):
    @app.callback(
        dash.dependencies.Output('jobsType', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        jobsType['refDate'] = pd.to_datetime(jobsType['refDate'])
        title = "Nombre et pourcentage d'employés à temps plein et partiel par sous-secteur, " + \
            str(max(jobsType['refDate'].dt.year)) + " - " + geo + '<br>' + '<sup>' + "Remarque : placer le curseur sur la barre pour connaître le nombre absolu d'employés." + '</sup>'
        df = jobsType[jobsType['geo'] == geo]
        return jobsType_fig(df, title)

    @app.callback(
        dash.dependencies.Output('wagesType', 'figure'),
        [dash.dependencies.Input('geo-selection', 'value'),])
    def update_graph(geo):
        wagesType['refDate'] = pd.to_datetime(wagesType['refDate'])
        title = "Salaires moyens par type d'emploi et par sous-secteur, " + \
            str(max((wagesType['refDate']).dt.year)) + " - " + geo
        df = wagesType[wagesType['geo'] == geo]
        return wagesType_fig(df, title)

    @app.callback(dash.dependencies.Output('jobsDemog',
                                           'figure'),
                  [dash.dependencies.Input('geo-selection',
                                           'value'),
                   dash.dependencies.Input('demo-selection-jobs',
                                           'value')])
    def update_graph(geo, demo):
        jobsDemog['refDate'] = pd.to_datetime(jobsDemog['refDate'])
        df = jobsDemog[(jobsDemog['geo'] == geo) &
                       (jobsDemog['class'] == demo)]
        title = "Répartition des employés des organismes à but non lucratif par caractéristique démographique et par sous-secteur., " + \
            str(max(jobsDemog['refDate'].dt.year)) + " - " + geo + '<br>' + '<sup>' + " Remarque : placer le curseur sur la barre pour connaître le nombre absolu d'employés." + '</sup>'
        return EmpDemog(df, title)

    @app.callback(dash.dependencies.Output('wagesDemog',
                                           'figure'),
                  [dash.dependencies.Input('geo-selection',
                                           'value'),
                   dash.dependencies.Input('demo-selection-wages',
                                           'value')])
    def update_graph(geo, demo):
        df = wagesDemog[(wagesDemog['geo'] == geo) &
                        (wagesDemog['class'] == demo)]
        wagesDemog['refDate'] = pd.to_datetime(wagesDemog['refDate'])
        title = "Salaires moyens par caractéristique démographique et par sous-secteur, " + \
            str(max(wagesDemog['refDate'].dt.year)) + " - " + geo
        return EmpDemog(df, title, jobs=False)
