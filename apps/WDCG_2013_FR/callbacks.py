# Callbacks file for WDCG_2013_FR converted from WDC010513_fr.py

import dash
from .data_processing import *
from .graphs import *


def register_callbacks(app):

    @app.callback(
        dash.dependencies.Output('MotivationsOverall_13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = Reasons_2018[Reasons_2018['Region'] == region]
        dff = dff[dff["Group"] == "All"]
        title = '{}, {}'.format(
            "Motivations signalées par les donateur.trice.s", region)
        return single_vertical_percentage_graph(
            dff, title, by="QuestionText", sort=True)

    @app.callback(
        dash.dependencies.Output('MotivationsAvgAmts_13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = AvgAmtReasons_2018[AvgAmtReasons_2018['Region'] == region]
        # name1 = "Report motivation"
        # name2 = "Do not report motivation"
        name1 = 'Signalent une motivation'
        name2 = 'Ne signalent aucune motivation'
        title = '{}, {}'.format(
            "Montants moyens des contributions des donateur.trice.s faisant état ou non de motivations précises",
            region)
        return vertical_dollar_graph(dff, name1, name2, title)

    @app.callback(
        dash.dependencies.Output('Motivations-Gndr_13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('motivation_selection', 'value')

        ])
    def update_graph(region, motivation):
        dff = Reasons_2018[Reasons_2018['Region'] == region]
        dff["QuestionText"] = dff["QuestionText"].replace(
            {'<br>': ' '}, regex=True)
        dff = dff[dff["Group"] == "Genre"]
        dff = dff[dff["QuestionText"] == motivation]
        title = '{}, {}'.format(
            "Motivations des donateur.trice.s: " +
            str(motivation) +
            " selon le genre",
            region)
        return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('Motivations-Age_13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('motivation_selection', 'value')

        ])
    def update_graph(region, motivation):
        dff = Reasons_2018[Reasons_2018['Region'] == region]
        dff["QuestionText"] = dff["QuestionText"].replace(
            {'<br>': ' '}, regex=True)
        dff = dff[dff["Group"] == "Groupe d'âge"]
        dff = dff[dff["QuestionText"] == motivation]
        # title = '{}, {}'.format("Donor motivations by age", region)
        title = '{}, {}'.format(
            "Motivations des donateur.trice.s: " +
            str(motivation) +
            " selon l’âge",
            region)
        return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('Motivations-Educ_13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('motivation_selection', 'value')

        ])
    def update_graph(region, motivation):
        dff = Reasons_2018[Reasons_2018['Region'] == region]
        dff["QuestionText"] = dff["QuestionText"].replace(
            {'<br>': ' '}, regex=True)
        dff = dff[dff["Group"] == "Éducation"]
        dff = dff[dff["QuestionText"] == motivation]
        title = '{}, {}'.format(
            "Motivations des donateur.trice.s: " +
            str(motivation) +
            " selon l’éducation formelle",
            region)
        return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('Motivations-Inc_13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('motivation_selection', 'value')

        ])
    def update_graph(region, motivation):
        dff = Reasons_2018[Reasons_2018['Region'] == region]
        dff["QuestionText"] = dff["QuestionText"].replace(
            {'<br>': ' '}, regex=True)
        dff = dff[dff["Group"] == "Catégorie de revenu familial"]
        dff = dff[dff["QuestionText"] == motivation]
        title = '{}, {}'.format(
            "Motivations des donateur.trice.s: " +
            str(motivation) +
            " selon le revenu du ménage",
            region)
        return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('Motivations-Relig_13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('motivation_selection', 'value')

        ])
    def update_graph(region, motivation):
        dff = Reasons_2018[Reasons_2018['Region'] == region]
        dff["QuestionText"] = dff["QuestionText"].replace(
            {'<br>': ' '}, regex=True)
        dff = dff[dff["Group"] == "Fréquence de la fréquentation religieuse"]
        dff = dff[dff["QuestionText"] == motivation]
        title = '{}, {}'.format(
            "Motivations des donateur.trice.s: " +
            str(motivation) +
            " selon la pratique religieuse",
            region)
        return single_vertical_percentage_graph(dff, title)

    # @app.callback(
    #     dash.dependencies.Output('Motivations-Marstat', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value'),
    #         dash.dependencies.Input('motivation_selection', 'value')

    #     ])
    # def update_graph(region, motivation):
    #     dff = Reasons_2018[Reasons_2018['Region'] == region]
    #     dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    #     dff = dff[dff["Group"] == "Marital status"]
    #     dff = dff[dff["QuestionText"] == motivation]
    #     title = '{}, {}'.format("Donor motivation: " + str(motivation) + " by marital status", region)
    #     return single_vertical_percentage_graph(dff, title)

    # @app.callback(
    #     dash.dependencies.Output('Motivations-Labour', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value'),
    #         dash.dependencies.Input('motivation_selection', 'value')

    #     ])
    # def update_graph(region, motivation):
    #     dff = Reasons_2018[Reasons_2018['Region'] == region]
    #     dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    #     dff = dff[dff["Group"] == "Labour force status"]
    #     dff = dff[dff["QuestionText"] == motivation]
    #     title = '{}, {}'.format("Donor motivation: " + str(motivation) + " by labour force status", region)
    #     return single_vertical_percentage_graph(dff, title)

    # @app.callback(
    #     dash.dependencies.Output('Motivations-Immstat', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value'),
    #         dash.dependencies.Input('motivation_selection', 'value')
    #     ])
    # def update_graph(region, motivation):
    #     dff = Reasons_2018[Reasons_2018['Region'] == region]
    #     dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    #     dff = dff[dff["Group"] == "Immigration status"]
    #     dff = dff[dff["QuestionText"] == motivation]
    #     title = '{}, {}'.format("Donor motivation: " + str(motivation) + " by immigration status", region)
    #     return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('status-sel13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('motivation_selection', 'value'),
            dash.dependencies.Input('status-selection', 'value')
        ])
    def update_graph(region, motivation, status):
        dff = Reasons_2018[Reasons_2018['Region'] == region]
        dff["QuestionText"] = dff["QuestionText"].replace(
            {'<br>': ' '}, regex=True)
        dff = dff[dff["Group"] == status]
        dff = dff[dff["QuestionText"] == motivation]
        title = '{}, {}'.format(
            "Motivations des donateur.trice.s " +
            str(motivation) +
            " selon " +
            str(status).lower(),
            region)
        return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('MotivationsCauses_13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('cause-selection', 'value')
        ])
    def update_graph(region, cause):
        dff = MotivationsByCause_2018[MotivationsByCause_2018['Region'] == region]
        dff = dff[dff["Group"] == cause]
        name1 = "Soutenir la cause"
        # name1 = 'Support cause'
        name2 = "Ne pas soutenir la cause"
        # name2 = 'Do not support cause'
        title = '{}, {}'.format(
            "Pourcentages de partisan.e.s et de non-partisan.e.s d’une cause faisant état de chaque motivation, selon la cause",
            region)
        return vertical_percentage_graph(dff, title, name1, name2)
