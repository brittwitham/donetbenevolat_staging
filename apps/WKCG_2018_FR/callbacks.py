# Callbacks file for WKCG_2018_FR converted from
# Qu_est_ce_qui_empeche_de_donner_plus_2018.py

import dash
from .data_processing import *
from .graphs import *


def register_callbacks(app):
    @app.callback(
        dash.dependencies.Output('BarriersOverall', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = Barriers_2018[Barriers_2018['Region'] == region]
        dff = dff[dff["Group"] == "All"]
        title = '{}, {}'.format(
            "Freins signalés par les donateur.trice.s", region)
        return single_vertical_percentage_graph(
            dff, title, by="QuestionText", sort=True)

    @app.callback(
        dash.dependencies.Output('BarriersAvgAmts', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = AvgAmtBarriers_2018[AvgAmtBarriers_2018['Region'] == region]
        dff = dff.replace("Report barrier", "Signalent un frein")
        dff = dff.replace("Do not report barrier", "Ne signalent aucun frein")
        # name1 = "Report barrier"
        name1 = "Signalent un frein"
        # name2 = "Do not report barrier"
        name2 = 'Ne signalent aucun frein'
        title = '{}, {}'.format(
            "Montants moyens des contributions des donateur.trice.s <br> faisant état ou non de freins précis",
            region)
        return vertical_dollar_graph(dff, name1, name2, title)

    @app.callback(
        dash.dependencies.Output('EfficiencyConcerns', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = GivingConcerns_2018[GivingConcerns_2018['Region'] == region]
        dff = dff[dff["Group"] == "All"]
        title = '{}, {}'.format(
            "Préoccupations concernant l’efficience et l’efficacité", region)
        return single_vertical_percentage_graph(
            dff, title, by="QuestionText", sort=True)

    @app.callback(
        dash.dependencies.Output('DislikeSolicitations', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff = SolicitationConcerns_2018[SolicitationConcerns_2018['Region'] == region]
        dff = dff[dff["Group"] == "All"]
        title = '{}, {}'.format(
            "Raisons de l’aversion à l’égard des sollicitations", region)
        return single_vertical_percentage_graph(
            dff, title, by="QuestionText", sort=True)

    @app.callback(
        dash.dependencies.Output('Barriers-Gndr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('barrier-selection', 'value')

        ])
    def update_graph(region, barrier):
        dff = Barriers_2018[Barriers_2018['Region'] == region]
        dff["QuestionText"] = dff["QuestionText"].replace(
            {'<br>': ' '}, regex=True)
        dff = dff[dff["Group"] == "Genre"]
        dff = dff[dff["QuestionText"] == barrier]
        title = '{}, {}'.format(
            "Barrière de donateurs: " +
            str(barrier) +
            " selon le genre",
            region)
        return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('Barriers-Age', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('barrier-selection-age', 'value')

        ])
    def update_graph(region, barrier):
        dff = Barriers_2018[Barriers_2018['Region'] == region]
        dff["QuestionText"] = dff["QuestionText"].replace(
            {'<br>': ' '}, regex=True)
        dff = dff[dff["Group"] == "Groupe d'âge"]
        dff = dff[dff["QuestionText"] == barrier]
        title = '{}, {}'.format(
            "Barrière de donateurs: " +
            str(barrier) +
            " selon l’âge",
            region)
        return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('Barriers-Educ', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('barrier-selection-educ', 'value')

        ])
    def update_graph(region, barrier):
        dff = Barriers_2018[Barriers_2018['Region'] == region]
        dff["QuestionText"] = dff["QuestionText"].replace(
            {'<br>': ' '}, regex=True)
        dff = dff[dff["Group"] == "Éducation"]
        dff = dff[dff["QuestionText"] == barrier]
        title = '{}, {}'.format(
            "Barrière de donateurs: " +
            str(barrier) +
            " selon l’éducation formelle",
            region)
        return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('Barriers-Inc', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('barrier-selection-income', 'value')

        ])
    def update_graph(region, barrier):
        dff = Barriers_2018[Barriers_2018['Region'] == region]
        dff["QuestionText"] = dff["QuestionText"].replace(
            {'<br>': ' '}, regex=True)
        dff = dff[dff["Group"] == "Catégorie de revenu familial"]
        dff = dff[dff["QuestionText"] == barrier]
        title = '{}, {}'.format(
            "Barrière de donateurs: " +
            str(barrier) +
            " selon le revenu du ménage",
            region)
        return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('Barriers-Relig', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('barrier-selection-religion', 'value')

        ])
    def update_graph(region, barrier):
        dff = Barriers_2018[Barriers_2018['Region'] == region]
        dff["QuestionText"] = dff["QuestionText"].replace(
            {'<br>': ' '}, regex=True)
        dff = dff[dff["Group"] == "Fréquence de la fréquentation religieuse"]
        dff = dff[dff["QuestionText"] == barrier]
        title = '{}, {}'.format(
            "Barrière de donateurs: " +
            str(barrier) +
            " selon la pratique religiouse",
            region)
        return single_vertical_percentage_graph(dff, title)

    # @app.callback(
    #     dash.dependencies.Output('Barriers-Marstat', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value'),
    #         dash.dependencies.Input('barrier-selection', 'value')

    #     ])
    # def update_graph(region, barrier):
    #     dff = Barriers_2018[Barriers_2018['Region'] == region]
    #     dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    #     dff = dff[dff["Group"] == "Marital status"]
    #     dff = dff[dff["QuestionText"] == barrier]
    #     title = '{}, {}'.format("Barriers reported by marital status", region)
    #     return single_vertical_percentage_graph(dff, title)

    # @app.callback(
    #     dash.dependencies.Output('Barriers-Labour', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value'),
    #         dash.dependencies.Input('barrier-selection', 'value')

    #     ])
    # def update_graph(region, barrier):
    #     dff = Barriers_2018[Barriers_2018['Region'] == region]
    #     dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    #     dff = dff[dff["Group"] == "Labour force status"]
    #     dff = dff[dff["QuestionText"] == barrier]
    #     title = '{}, {}'.format("Barriers reported by labour force status", region)
    #     return single_vertical_percentage_graph(dff, title)

    # @app.callback(
    #     dash.dependencies.Output('Barriers-Immstat', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value'),
    #         dash.dependencies.Input('barrier-selection', 'value')
    #     ])
    # def update_graph(region, barrier):
    #     dff = Barriers_2018[Barriers_2018['Region'] == region]
    #     dff["QuestionText"] = dff["QuestionText"].replace({'<br>': ' '}, regex=True)
    #     dff = dff[dff["Group"] == "Immigration status"]
    #     dff = dff[dff["QuestionText"] == barrier]
    #     title = '{}, {}'.format("Barriers reported by immigration status", region)
    #     return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('status-sel-barrier', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('barrier-selection-other', 'value'),
            dash.dependencies.Input('status-selection', 'value')
        ])
    def update_graph(region, barrier, status):
        dff = Barriers_2018[Barriers_2018['Region'] == region]
        dff["QuestionText"] = dff["QuestionText"].replace(
            {'<br>': ' '}, regex=True)
        dff = dff[dff["Group"] == status]
        dff = dff[dff["QuestionText"] == barrier]
        title = '{}, {}'.format(
            "Barrière de donateurs: " +
            str(barrier).lower() +
            " selon " +
            str(status).lower(),
            region)
        return single_vertical_percentage_graph(dff, title)

    @app.callback(
        dash.dependencies.Output('BarriersCauses', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('cause-selection', 'value')
        ])
    def update_graph(region, cause):
        dff = BarriersByCause_2018[BarriersByCause_2018['Region'] == region]
        dff = dff[dff["Group"] == cause]
        dff = dff.replace('Support cause', 'Soutenir la cause')
        dff = dff.replace('Do not support cause', "Ne pas soutenir la cause")
        # name1 = "Support cause"
        name1 = "Soutenir la cause"
        # name2 = "Do not support cause"
        name2 = "Ne pas soutenir la cause"
        title = '{}, {}'.format(
            "Pourcentages de partisan.e.s et de non-partisan.e.s <br> d’une cause faisant état de chaque frein, selon la cause",
            region)
        return vertical_percentage_graph(dff, title, name1, name2)
