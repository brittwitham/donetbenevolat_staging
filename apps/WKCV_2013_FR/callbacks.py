# Callbacks file for WKCV_2013_FR converted from WKC020613_fr.py

import dash
from .data_processing import *
from .graphs import *


def register_callbacks(app):
    @app.callback(
        dash.dependencies.Output('BarriersVolOverall_13', 'figure'),
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
        dash.dependencies.Output('BarriersVolAvgHrs_13', 'figure'),
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
        dash.dependencies.Output('BarriersVol-Gndr_13', 'figure'),
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
        dash.dependencies.Output('BarriersVol-Age_13', 'figure'),
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

    # @app.callback(
    #     dash.dependencies.Output('BarriersVol-Educ', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value'),
    #         dash.dependencies.Input('barrier-selection-educ', 'value')

    #     ])
    # def update_graph(region, barrier):
    #     dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
    #     dff["Attribute"] = dff["Attribute"].str.wrap(20, break_long_words=False)
    #     dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
    #     dff = dff[dff['Region'] == region]
    #     dff = dff[dff["Group"] == "Éducation"]
    #     dff = dff[dff["QuestionText"] == barrier]
    #     title = '{}, {}'.format("Barrière de bénévoles: " + str(barrier) + " selon l’éducation formelle", region)
    #     return vertical_percentage_graph_volunteers(dff, title)

    # @app.callback(
    #     dash.dependencies.Output('BarriersVol-Inc_13', 'figure'),
    #     [
    #         dash.dependencies.Input('region-selection', 'value'),
    #         dash.dependencies.Input('barrier-selection-income', 'value')

    #     ])
    # def update_graph(region, barrier):
    #     dff = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
    #     dff["Attribute"] = dff["Attribute"].str.wrap(20, break_long_words=False)
    #     dff["Attribute"] = dff["Attribute"].replace({'\n': '<br>'}, regex=True)
    #     dff = dff[dff['Region'] == region]
    #     dff = dff[dff["Group"] == "Catégorie de revenu familial"]
    #     dff = dff[dff["QuestionText"] == barrier]
    #     title = '{}, {}'.format("Barrière de bénévoles: " + str(barrier) + " selon le revenu", region)
    #     return vertical_percentage_graph_volunteers(dff, title)

    @app.callback(
        dash.dependencies.Output('BarriersVol-Inc_13', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('barrier-selection-income', 'value')

        ])
    def update_graph(region, barrier):
        df = BarriersVol_2018.append(BarriersVolMore_2018, ignore_index=True)
        df["Attribute"] = df["Attribute"].str.wrap(20, break_long_words=False)
        df["Attribute"] = df["Attribute"].replace({'\n': '<br>'}, regex=True)

        df = df.replace('15 Ã\xa0 24 ans', '15 à 24 ans')
        df = df.replace('25 Ã\xa0 34 ans', '25 à 34 ans')
        df = df.replace('35 Ã\xa0 44 ans', '35 à 44 ans')
        df = df.replace('45 Ã\xa0 54 ans', '45 à 54 ans')
        df = df.replace('55 Ã\xa0 64 ans', '55 à 64 ans')
        df = df.replace('65 Ã\xa0 74 ans', '65 à 74 ans')
        df = df.replace('75 ans et plus', '75 ans et plus')

        # EDUCATION
        df = df.replace(
            "Sans diplÃ´me d'Ã©tudes secondaires",
            "Sans diplôme d'études secondaires")
        df = df.replace(
            "DiplÃ´me d'Ã©tudes secondaires",
            "Diplôme d'études secondaires")
        df = df.replace('DiplÃ´me post-secondaire', 'Diplôme post-secondaire')
        df = df.replace('DiplÃ´me universtaire', "Diplôme universtaire")

        # INCOME
        df = df.replace('Less than $25,000', 'Moins de 25 000 $')
        df = df.replace('25 000 $ Ã\xa0 49 999 $', '25 000 $ à 49 999 $')
        df = df.replace('50 000 $ a 74 999 $', '50 000 $ a 74 999 $')
        df = df.replace('75 000 $ Ã\xa0 99 999 $', '75 000 $ à 99 999 $')
        df = df.replace('100 000 $ Ã\xa0 124 999 $', '100 000 $ à 124 999 $')
        df = df.replace('125 000 $ et plus', '125 000 $ et plus')

        # RELIGIOUS ATTENDANCE
        df = df.replace('At least once a week', 'Au moins 1 fois par semaine')
        df = df.replace('At least once a month', 'Au moins 1 fois par mois')
        df = df.replace('At least 3 times a year', 'Au moins 3 fois par mois')
        df = df.replace('Once or twice a year', '1 ou 2 fois par an')
        df = df.replace('Not at all', 'Pas du tout')

        # MARITAL STATUS
        df = df.replace('MariÃ©.e/union de fait', 'Marié.e/union de fait')
        df = df.replace('SÃ©parÃ©.e/divorcÃ©.e', 'Séparé.e/divorcé.e')

        df = df.replace('MariÃ©.e', 'Marié.e')
        df = df.replace('Living common-law', 'Union de fait')
        df = df.replace('SÃ©parÃ©.e', 'Séparé.e')
        df = df.replace('divorcÃ©.e', 'divorcé.e')
        df = df.replace("Divorcé.e", 'divorcé.e')
        df = df.replace('Widowed', 'Veuf.ve')
        df = df.replace(
            'CÃ©libataire, jamais mariÃ©.e',
            'Célibataire, jamais marié.e')

        # EMPLOYMENT STATUS
        df = df.replace('EmployÃ©.e', 'Employé.e')
        df = df.replace('Au chÃ´mage', 'Au chômage')
        df = df.replace('Not in labour force', 'Pas dans la population active')

        # IMMIGRATON STATUS
        df = df.replace('NÃ©.e au Canada', 'Né.e au Canada')
        df = df.replace('NaturalisÃ©.e', 'Naturalisé.e')
        df = df.replace('Non-Canadian', 'Non canadien.ne')

        df = df.replace("Groupe d'Ã¢ge", "Groupe d'âge")
        df = df.replace('Gender', "Genre")
        df = df.replace("Ã\x89ducation", "Éducation")
        df = df.replace('Ã\x89tat civil (original)', "État civil (original)")
        df = df.replace('Ã\x89tat civil (Original)', "État civil (original)")
        df = df.replace('Ã\x89tat civil', "État civil")
        df = df.replace("Situation d'activitÃ©", "Situation d'activité")
        df = df.replace(
            'CatÃ©gorie de revenu personnel',
            "Catégorie de revenu personnel")
        df = df.replace(
            "CatÃ©gorie de revenu familial",
            "Catégorie de revenu familial")
        df = df.replace(
            "CatÃ©gorie de revenu familial",
            "Catégorie de revenu familial")
        df = df.replace(
            'FrÃ©quence de la frÃ©quentation religieuse',
            "Fréquence de la fréquentation religieuse")
        df = df.replace('Immigration status', "Statut d'immigration")

        df = df[df['Region'] == region]
        df = df[df["Group"] == "Catégorie de revenu familial"]
        df = df[df["QuestionText"] == barrier]
        title = '{}, {}'.format(
            "Barrière de bénévoles: " +
            str(barrier) +
            " selon le revenu income",
            region)
        return vertical_percentage_graph_volunteers(df, title)

    @app.callback(
        dash.dependencies.Output('BarriersVol-Labour_13', 'figure'),
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
        dash.dependencies.Output('status-sel-volbarrier_13', 'figure'),
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
        dash.dependencies.Output('BarriersVolCauses_13', 'figure'),
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
