# Callbacks file for WKCV_2018_FR converted from
# Qu_est_ce_qui_empeche_de_faire_du_benevolat_2018.py

import dash
from .data_processing import *
from .graphs import *


def register_callbacks(app):
    @app.callback(
        dash.dependencies.Output('BarriersVolOverall', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
        ])
    def update_graph(region):
        dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
        dff["QuestionText"] = dff["QuestionText"].str.wrap(27)
        dff["QuestionText"] = dff["QuestionText"].replace({'\n': '<br>'}, regex=True)
        dff = dff[dff['Region'] == region]
        dff = dff[dff["Group"] == "All"]
        title = '{}, {}'.format("Freins au bénévolat, bénévoles et non-bénévoles", region)
        return vertical_percentage_graph_volunteers(dff, title, by="QuestionText")

    @app.callback(
        dash.dependencies.Output('BarriersVolAvgHrs', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),

        ])
    def update_graph(region):
        dff = AvgHoursBarriersVol_2018[AvgHoursBarriersVol_2018['Region'] == region]
        dff["Group"] = dff["Group"].str.wrap(28)
        dff["Group"] = dff["Group"].replace({'\n': '<br>'}, regex=True)
        dff = dff.replace("Report barrier", "Signalent un frein")
        dff = dff.replace("Do not report barrier", "Ne signalent aucun frein")
        
        # name1 = "Report barrier"
        name1 = "Signalent un frein"
        # name2 = "Do not report barrier"
        name2 = "Ne signalent aucun frein"
        # title_text = 'Average hours volunteered by volunteers reporting and not reporting specific barriers'
        # title_text =  textwrap.fill(text = title_text, width=25)
        title = '{}, {}'.format('Nombre moyen d’heures de bénévolat des bénévoles <br> faisant ou non état de freins précis', region)
        return vertical_hours_graph(dff, name1, name2, title)

    @app.callback(
        dash.dependencies.Output('BarriersVol-Gndr', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('barrier-selection', 'value')

        ])
    def update_graph(region, barrier):
        dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
        dff["Attribute"] = dff["Attribute"].str.wrap(
            20, break_long_words=False)
        dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
        dff = dff[dff['Region'] == region]
        dff = dff[dff["Group"] == "Genre"]
        dff = dff[dff["QuestionText"] == barrier]
        title = '{}, {}'.format(
            "Barrière de bénévoles: " +
            str(barrier) +
            " selon le genre",
            region)
        return vertical_percentage_graph_volunteers(dff, title)

    @app.callback(
        dash.dependencies.Output('BarriersVol-Age', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('barrier-selection-age', 'value')

        ])
    def update_graph(region, barrier):
        dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
        dff["Attribute"] = dff["Attribute"].str.wrap(
            20, break_long_words=False)
        dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
        dff = dff[dff['Region'] == region]
        dff = dff[dff["Group"] == "Groupe d'âge"]
        dff = dff[dff["QuestionText"] == barrier]
        title = '{}, {}'.format(
            "Barrière de bénévoles: " +
            str(barrier) +
            " selon l’âge",
            region)
        return vertical_percentage_graph_volunteers(dff, title)

    @app.callback(
        dash.dependencies.Output('BarriersVol-Educ', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('barrier-selection-educ', 'value')

        ])
    def update_graph(region, barrier):
        dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
        dff["Attribute"] = dff["Attribute"].str.wrap(
            20, break_long_words=False)
        dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
        dff = dff[dff['Region'] == region]
        dff = dff[dff["Group"] == "Éducation"]
        dff = dff[dff["QuestionText"] == barrier]
        title = '{}, {}'.format(
            "Barrière de bénévoles: " +
            str(barrier) +
            " selon l’éducation formelle",
            region)
        return vertical_percentage_graph_volunteers(dff, title)

    @app.callback(
        dash.dependencies.Output('BarriersVol-Inc', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('barrier-selection-income', 'value')

        ])
    def update_graph(region, barrier):
        dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
        dff["Attribute"] = dff["Attribute"].str.wrap(
            20, break_long_words=False)
        dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
        dff = dff[dff['Region'] == region]
        dff = dff[dff["Group"] == "Catégorie de revenu familial"]
        dff = dff[dff["QuestionText"] == barrier]
        title = '{}, {}'.format(
            "Barrière de bénévoles: " +
            str(barrier) +
            " selon le revenu",
            region)
        return vertical_percentage_graph_volunteers(dff, title)

    @app.callback(
        dash.dependencies.Output('BarriersVol-Labour', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('barrier-selection-labour', 'value')

        ])
    def update_graph(region, barrier):
        dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
        dff["Attribute"] = dff["Attribute"].str.wrap(
            20, break_long_words=False)
        dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
        dff = dff[dff['Region'] == region]
        dff = dff[dff["Group"] == "Situation d'activité"]
        dff = dff[dff["QuestionText"] == barrier]
        title = '{}, {}'.format(
            "Barrière de bénévoles: " +
            str(barrier) +
            " selon la situation d’emploi",
            region)
        return vertical_percentage_graph_volunteers(dff, title)

    # @app.callback(
    #     dash.dependencies.Output('BarriersVol-Marstat', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value'),
    #         dash.dependencies.Input('barrier-selection', 'value')

    #     ])
    # def update_graph(region, barrier):
    #     dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
    #     dff["Attribute"] = dff["Attribute"].str.wrap(20, break_long_words=False)
    #     dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
    #     dff = dff[dff['Region'] == region]
    #     dff = dff[dff["Group"] == "Marital status"]
    #     dff = dff[dff["QuestionText"] == barrier]
    #     title = '{}, {}'.format("Barriers to volunteering by marital status", region)
    #     return vertical_percentage_graph_volunteers(dff, title)

    # @app.callback(
    #     dash.dependencies.Output('BarriersVol-Labour', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value'),
    #         dash.dependencies.Input('barrier-selection', 'value')

    #     ])
    # def update_graph(region, barrier):
    #     dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
    #     dff["Attribute"] = dff["Attribute"].str.wrap(20, break_long_words=False)
    #     dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
    #     dff = dff[dff['Region'] == region]
    #     dff = dff[dff["Group"] == "Labour force status"]
    #     dff = dff[dff["QuestionText"] == barrier]
    #     title = '{}, {}'.format("Barriers to volunteering by labour force status", region)
    #     return vertical_percentage_graph_volunteers(dff, title)

    # @app.callback(
    #     dash.dependencies.Output('BarriersVol-Immstat', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value'),
    #         dash.dependencies.Input('barrier-selection', 'value')
    #     ])
    # def update_graph(region, barrier, status):
    #     dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
    #     dff["Attribute"] = dff["Attribute"].str.wrap(20, break_long_words=False)
    #     dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
    #     dff = dff[dff['Region'] == region]
    #     dff = dff[dff["Group"] == status]
    #     dff = dff[dff["QuestionText"] == barrier]
    #     title = '{}, {}'.format("Barriers to volunteering by immigration status", region)
    #     return vertical_percentage_graph_volunteers(dff, title)

    @app.callback(
        dash.dependencies.Output('status-sel-volbarrier', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('barrier-selection-other', 'value'),
            dash.dependencies.Input('status-selection-volbarrier', 'value')
        ])
    def update_graph(region, barrier, status):
        dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
        # dff["Attribute"] = dff["Attribute"].str.wrap(20, break_long_words=False)
        # dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
        dff = dff[dff['Region'] == region]
        dff = dff[dff["Group"] == status]
        dff = dff[dff["QuestionText"] == barrier]
        title = '{}, {}'.format(
            "Barrière de bénévoles: " +
            str(barrier).lower() +
            '<br>' +
            ' selon ' +
            str(status).lower(),
            region)
        return vertical_percentage_graph_volunteers(dff, title)

    @app.callback(
        dash.dependencies.Output('BarriersVolCauses', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('cause-selection', 'value')
        ])
    def update_graph(region, cause):
        dff = BarriersVolByCause_2018[BarriersVolByCause_2018['Region'] == region]
        dff = dff[dff["Group"] == cause]
        dff["QuestionText"] = dff["QuestionText"].str.wrap(28)
        dff["QuestionText"] = dff["QuestionText"].replace(
            {'\n': '<br>'}, regex=True)
        dff = dff.replace("Support cause", "Soutiennent la cause")
        dff = dff.replace(
            "Do not support cause",
            "Ne soutiennent pas la cause")

        # name1 = "Support cause"
        name1 = "Soutiennent la cause"
        name2 = "Ne soutiennent pas la cause"
        # name2 = "Do not support cause"
        title = '{}, {}'.format(
            str(cause) +
            " les partisan.e.s et de non-partisan.e.s signalent chaque frein",
            region)
        return vertical_percentage_graph(dff, title, name1, name2)
