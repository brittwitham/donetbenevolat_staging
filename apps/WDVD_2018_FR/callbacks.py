# CALLBACKS file for WDVD_2018_FR converted from Quelles_sont_les_activites_des_benevoles_2018.py

import dash
from .data_processing import *
from .graphs import *

def register_callbacks(app):
    @app.callback(
        dash.dependencies.Output('ActivitiesVolRateAvgHrs', 'figure'),
        [

            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):

        dff1 = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "All"]
        dff1 = dff1.replace("Health care or support", "Soins de santé ou soutien")
        # name1 = "Volunteer rate"
        name1 = 'Taux de bénévolat'

        dff2 = AvgHoursVol_2018[AvgHoursVol_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "All"]
        dff2 = dff2.replace("Health care or support", "Soins de santé ou soutien")
        dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")

        # name2 = "Average hours"
        name2 = "Nombre d'heures moyen"

        title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures de bénévolat par activité", region)

        return vol_rate_avg_hrs_qt(dff1, dff2, name1, name2, title)


    @app.callback(
        dash.dependencies.Output('ActivityVolRate-Gndr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('activity-selection', 'value')
        ])
    def update_graph(region, activity):
        dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
        dff = dff[dff['QuestionText'] == activity]
        dff = dff[dff['Group'] == "Genre"]

        title = '{}, {}'.format(str(activity) + " selon le genre", region)
        return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('ActivityVolRate-Age', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('activity-selection', 'value')
        ])
    def update_graph(region, activity):
        dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
        dff = dff[dff['QuestionText'] == activity]
        dff = dff[dff['Group'] == "Groupe d'âge"]

        title = '{}, {}'.format(str(activity) + " selon l’âge", region)
        return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('ActivityVolRate-Educ', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('activity-selection', 'value')
        ])
    def update_graph(region, activity):
        dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
        dff = dff[dff['QuestionText'] == activity]
        dff = dff[dff['Group'] == "Éducation"]

        title = '{}, {}'.format(str(activity) + " l’éducation formelle", region)
        return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('ActivityVolRate-MarStat', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('activity-selection', 'value')
        ])
    def update_graph(region, activity):
        dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
        dff = dff[dff['QuestionText'] == activity]
        dff = dff[dff['Group'] == "État civil"]

        title = '{}, {}'.format(str(activity) + " selon la situation matrimoniale", region)
        return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('ActivityVolRate-Inc', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('activity-selection', 'value')
        ])
    def update_graph(region, activity):
        dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
        dff = dff[dff['QuestionText'] == activity]
        dff = dff[dff['Group'] == "Catégorie de revenu familial"]

        title = '{}, {}'.format(str(activity) + " selon le revenu du ménage", region)
        return single_vertical_percentage_graph(dff, title)


    @app.callback(
        dash.dependencies.Output('ActivityVolRate-Relig', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('activity-selection', 'value')
        ])
    def update_graph(region, activity):
        dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
        dff = dff[dff['QuestionText'] == activity]
        dff = dff[dff['Group'] == "Fréquence de la fréquentation religieuse"]

        title = '{}, {}'.format(str(activity) + " selon la pratique religieuse", region)
        return single_vertical_percentage_graph(dff, title)


    # @app.callback(
    #     dash.dependencies.Output('ActivityVolRate-Labour', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value'),
    #         dash.dependencies.Input('activity-selection', 'value')
    #     ])
    # def update_graph(region, activity):
    #     dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
    #     dff = dff[dff['QuestionText'] == activity]
    #     dff = dff[dff['Group'] == "Situation d'activité"]

    #     title = '{}, {}'.format(str(activity) + " selon la situation d’emploi", region)
    #     return single_vertical_percentage_graph(dff, title)


    # @app.callback(
    #     dash.dependencies.Output('ActivityVolRate-ImmStat', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value'),
    #         dash.dependencies.Input('activity-selection', 'value')
    #     ])
    # def update_graph(region, activity):
    #     dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
    #     dff = dff[dff['QuestionText'] == activity]
    #     dff = dff[dff['Group'] == "Statut d'immigration"]

    #     title = '{}, {}'.format(str(activity) + " selon le statut d’immigration", region)
    #     return single_vertical_percentage_graph(dff, title)


    @app.callback(
        dash.dependencies.Output('status-fig', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('activity-selection', 'value'),
            dash.dependencies.Input('status-selection', 'value')

        ])
    def update_graph(region, activity, status):
        dff = ActivityVolRate_2018[ActivityVolRate_2018['Region'] == region]
        dff = dff[dff['QuestionText'] == activity]
        dff = dff[dff['Group'] == status]

        title = '{}, {}'.format(str(activity) + " selon " + str(status).lower(), region)
        return single_vertical_percentage_graph(dff, title)
