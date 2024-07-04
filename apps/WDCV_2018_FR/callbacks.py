# CALLBACKS file for WDCV_2018_FR converted from
# Pourquoi_fait_on_du_benevolat_2018.py

import dash
from .data_processing import *
from .graphs import *


def register_callbacks(app):
    @app.callback(
        dash.dependencies.Output('MotivationsOverall-2', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = ReasonsVol_2018[ReasonsVol_2018['Region'] == region]
        dff = dff[dff["Group"] == "All"]
        title = '{}, {}'.format(
            "Motivations signalées par les bénévoles", region)
        return single_vertical_percentage_graph(
            dff, title, by="QuestionText", sort=True)

    @app.callback(
        dash.dependencies.Output('MotivationsAvgHrs', 'figure'),
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
            "Nombre moyen d’heures de bénévolat pour les bénévoles faisant état ou non de motivations précises",
            region)
        return vertical_hours_graph(df, name1, name2, title)

    @app.callback(
        dash.dependencies.Output('Motivations-Gndr-2', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('motivation_selection', 'value')

        ])
    def update_graph(region, motivation):
        dff = ReasonsVol_2018[ReasonsVol_2018['Region'] == region]
        dff["QuestionText"] = dff["QuestionText"].replace(
            {'<br>': ' '}, regex=True)
        dff = dff[dff["Group"] == "Genre"]
        dff = dff[dff["QuestionText"] == motivation]
        title = '{}, {}'.format(
            "La motivation des bénévoles: " +
            str(motivation) +
            " selon le genre",
            region)
        return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('Motivations-Age-2', 'figure'),
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
        dash.dependencies.Output('Motivations-Educ-2', 'figure'),
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
        dash.dependencies.Output('Motivations-Inc-2', 'figure'),
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

    # @app.callback(
    #     dash.dependencies.Output('Motivations-Relig-2', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value'),
    #         dash.dependencies.Input('motivation_selection-relig', 'value')

    #     ])
    # def update_graph(region, motivation):
    #     dff = ReasonsVol_2018[ReasonsVol_2018['Region'] == region]
    #     dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    #     dff = dff[dff["Group"] == "Fréquence de la fréquentation religieuse"]
    #     dff = dff[dff["QuestionText"] == motivation]
    #     title = '{}, {}'.format("La motivation des bénévoles: " + str(motivation) + " selon la pratique religieuse", region)
    #     return single_vertical_percentage_graph(dff, title)

    # @app.callback(
    #     dash.dependencies.Output('Motivations-Marstat-2', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value'),
    #         dash.dependencies.Input('motivation_selection', 'value')

    #     ])
    # def update_graph(region, motivation):
    #     dff = ReasonsVol_2018[ReasonsVol_2018['Region'] == region]
    #     dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    #     dff = dff[dff["Group"] == "Marital status"]
    #     dff = dff[dff["QuestionText"] == motivation]
    #     title = '{}, {}'.format("Volunteer motivations by marital status", region)
    #     return single_vertical_percentage_graph(dff, title)

    # @app.callback(
    #     dash.dependencies.Output('Motivations-Labour-2', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value'),
    #         dash.dependencies.Input('motivation_selection', 'value')

    #     ])
    # def update_graph(region, motivation):
    #     dff = ReasonsVol_2018[ReasonsVol_2018['Region'] == region]
    #     dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    #     dff = dff[dff["Group"] == "Labour force status"]
    #     dff = dff[dff["QuestionText"] == motivation]
    #     title = '{}, {}'.format("Volunteer motivations by labour force status", region)
    #     return single_vertical_percentage_graph(dff, title)

    # @app.callback(
    #     dash.dependencies.Output('Motivations-Immstat-2', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value'),
    #         dash.dependencies.Input('motivation_selection', 'value')
    #     ])
    # def update_graph(region, motivation):
    #     dff = ReasonsVol_2018[ReasonsVol_2018['Region'] == region]
    #     dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    #     dff = dff[dff["Group"] == "Immigration status"]
    #     dff = dff[dff["QuestionText"] == motivation]
    #     title = '{}, {}'.format("Volunteer motivations by immigration status", region)
    #     return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('status-sel2', 'figure'),
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
            ' selon ' +
            str(status).lower(),
            region)
        return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('MotivationsCauses-2', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('cause-selection', 'value')
        ])
    def update_graph(region, cause):
        dff = MotivationsVolByCause_2018[MotivationsVolByCause_2018['Region'] == region]
        dff = dff[dff["Group"] == cause]
        dff = dff.replace("Support cause", "Soutiennent la cause")
        dff = dff.replace(
            "Do not support cause",
            "Ne soutiennent pas la cause")

        # name1 = "Support cause"
        name1 = "Soutiennent la cause"
        # name2 = "Do not support cause"
        name2 = "Ne soutiennent pas la cause"

        title = '{}, {}'.format(
            "Pourcentages de partisan.e.s et de non-partisan.e.s d’une cause faisant état de chaque motivation, selon la cause",
            region)
        return vertical_percentage_graph(dff, title, name1, name2)
