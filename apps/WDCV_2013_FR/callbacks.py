# CALLBACKS file for WDCV_2013_FR converted from WDC020513_fr.py

import dash
from .data_processing import *
from .graphs import *


def register_callbacks(app):


    @app.callback(
        dash.dependencies.Output('MotivationsOverall-13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = ReasonsVol_2018[ReasonsVol_2018['Region'] == region]
        dff = dff[dff["Group"] == "All"]
        title = '{}, {}'.format("Motivations signalées par les bénévoles", region)
        return single_vertical_percentage_graph(
            dff, title, by="QuestionText", sort=True)


    @app.callback(
        dash.dependencies.Output('MotivationsAvgHrs_13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        df = AvgHrsReasons_2018[AvgHrsReasons_2018['Region'] == region]
        df["Group"] = df["Group"].str.wrap(30, break_long_words=False)
        df["Group"] = df["Group"].replace({'\n': '<br>'}, regex=True)
        df = df.replace("Report motivation", "Signalent une motivation")
        df = df.replace(
            "Do not report motivation",
            "Ne signalent aucune motivation")

        name1 = "Signalent une motivation"
        # name1 = "Report motivation"
        name2 = "Ne signalent aucune motivation"
        # name2 = "Do not report motivation"
        title = '{}, {}'.format(
            "Nombre moyen d’heures de bénévolat pour les bénévoles faisant <br> état ou non de motivations précises",
            region)
        return vertical_hours_graph(df, name1, name2, title)


    @app.callback(
        dash.dependencies.Output('Motivations-Gndr-13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('motivation_selection', 'value')

        ])
    def update_graph(region, motivation):
        dff = ReasonsVol_2018[ReasonsVol_2018['Region'] == region]
        dff["QuestionText"] = dff["QuestionText"].replace(
            {'<br>': ' '}, regex=True)
        dff = dff[dff["Group"] == "Genre"]
        dff = dff.replace("Male", "Hommes")
        dff = dff.replace("Female", "Femmes")
        dff = dff[dff["QuestionText"] == motivation]
        title = '{}, {}'.format(
            "La motivation des bénévoles: " +
            str(motivation) +
            " selon le genre",
            region)
        return single_vertical_percentage_graph(dff, title)


    @app.callback(
        dash.dependencies.Output('Motivations-Age-13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('motivation_selection-age', 'value')

        ])
    def update_graph(region, motivation):
        dff = ReasonsVol_2018[ReasonsVol_2018['Region'] == region]
        dff["QuestionText"] = dff["QuestionText"].replace(
            {'<br>': ' '}, regex=True)
        dff = dff[dff["Group"] == "Groupe d'âge"]
        dff = dff[dff["QuestionText"] == motivation]
        title = '{}, {}'.format(
            "La motivation des bénévoles: " +
            str(motivation) +
            " selon l’âge",
            region)
        return single_vertical_percentage_graph(dff, title)


    @app.callback(
        dash.dependencies.Output('Motivations-Educ-13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('motivation_selection-educ', 'value')

        ])
    def update_graph(region, motivation):
        dff = ReasonsVol_2018[ReasonsVol_2018['Region'] == region]
        dff["QuestionText"] = dff["QuestionText"].replace(
            {'<br>': ' '}, regex=True)
        dff = dff[dff["Group"] == "Éducation"]
        dff = dff[dff["QuestionText"] == motivation]
        title = '{}, {}'.format(
            "La motivation des bénévoles: " +
            str(motivation) +
            " selon l’éducation formelle",
            region)
        return single_vertical_percentage_graph(dff, title)


    @app.callback(
        dash.dependencies.Output('Motivations-Inc-13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('motivation_selection-income', 'value')

        ])
    def update_graph(region, motivation):
        dff = ReasonsVol_2018[ReasonsVol_2018['Region'] == region]
        dff["QuestionText"] = dff["QuestionText"].replace(
            {'<br>': ' '}, regex=True)
        dff = dff[dff["Group"] == "Catégorie de revenu familial"]
        dff = dff[dff["QuestionText"] == motivation]
        title = '{}, {}'.format(
            "La motivation des bénévoles: " +
            str(motivation) +
            " <br> selon le revenu du ménage",
            region)
        return single_vertical_percentage_graph(dff, title)


    @app.callback(
        dash.dependencies.Output('status-selfr-13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('motivation_selection-other', 'value'),
            dash.dependencies.Input('status-selection', 'value')
        ])
    def update_graph(region, motivation, status):
        dff = ReasonsVol_2018[ReasonsVol_2018['Region'] == region]
        dff["QuestionText"] = dff["QuestionText"].replace(
            {'<br>': ' '}, regex=True)
        dff = dff[dff["Group"] == status]
        dff = dff[dff["QuestionText"] == motivation]
        title = '{}, {}'.format(
            "La motivation des bénévoles: " +
            str(motivation) +
            '<br>' +
            ' selon ' +
            str(status).lower(),
            region)
        return single_vertical_percentage_graph(dff, title)


    @app.callback(
        dash.dependencies.Output('MotivationsCauses-13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('cause-selection', 'value')
        ])
    def update_graph(region, cause):
        dff = MotivationsVolByCause_2018[MotivationsVolByCause_2018['Region'] == region]
        dff = dff[dff["Group"] == cause]
        dff = dff.replace("Support cause", "Soutiennent la cause")
        dff = dff.replace("Do not support cause", "Ne soutiennent pas la cause")

        # name1 = "Support cause"
        name1 = "Soutiennent la cause"
        # name2 = "Do not support cause"
        name2 = "Ne soutiennent pas la cause"

        title = '{}, {}'.format(
            "Pourcentages de partisan.e.s et de non-partisan.e.s d’une cause faisant <br> état de chaque motivation, selon la cause",
            region)
        return vertical_percentage_graph(dff, title, name1, name2)
