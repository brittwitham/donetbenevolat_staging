# Callbacks file for HOCP_2018_FR converted from
# Aide_autrui_et_amelioration_communautaire_2018.py

import dash
from .data_processing import *
from .graphs import *


def register_callbacks(app):
    # @app.callback(
    #     dash.dependencies.Output('FormsVolunteering', 'figure'),
    #     [

    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):

    #     dff1 = FormsVolunteering_2018[FormsVolunteering_2018['Region'] == region]
    #     dff1 = dff1[dff1['Group'] == "All"]

    #     title = '{}, {}'.format("Forms of giving", region)

    #     return forms_of_giving(dff1, title)

    @app.callback(
        dash.dependencies.Output('VolRateAvgHrs-Helping', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff1 = HelpDirectRate_2018[HelpDirectRate_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "All"]
        dff1 = dff1.replace("Helping others rate", "Taux d'aide aux autres")
        name1 = "Taux d'aide aux autres"
        # name1 = "Helping others rate"

        dff2 = HelpDirectHrs_2018[HelpDirectHrs_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "All"]
        dff2 = dff2.replace('Average hours', "Nbre d'h moyen")
        name2 = "Nbre d'h moyen"

        title = '{}, {}'.format("Formes d’aide", region)

        return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)

    @app.callback(
        dash.dependencies.Output('VolRateAvgHrs-Community', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff1 = CommInvolveRate_2018[CommInvolveRate_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "All"]
        dff1 = dff1.replace('Community improvement rate', "")
        name1 = "Community improvement rate"

        dff2 = CommInvolveHrs_2018[CommInvolveHrs_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "All"]
        dff2 = dff2.replace('Average hours', "Nbre d'h moyen")
        name2 = "Nbre d'h moyen"
        # name2 = "Average hours"

        title = '{}, {}'.format("Formes d’amélioration communautaire", region)

        return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)

    @app.callback(
        dash.dependencies.Output('VolRates-All', 'figure'),
        [
            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('demo-selection', 'value')
        ])
    def update_graph(region, demo):
        dff1 = VolRate_2018[VolRate_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == demo]
        # name1 = "Volunteering"
        name1 = 'Volontariat'

        dff2 = FormsVolunteering_2018[FormsVolunteering_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == demo]
        dff2 = dff2[dff2['QuestionText'] == 'Help people<br>directly']
        name2 = "Aider les autres"

        dff3 = FormsVolunteering_2018[FormsVolunteering_2018['Region'] == region]
        dff3 = dff3[dff3['Group'] == demo]
        dff3 = dff3[dff3['QuestionText'] == 'Improve<br>community']
        name3 = "Participation de la communauté"

        title = '{}, {}'.format(
            "Probabilité de soutenir selon les caractéristiques personnelles et économiques clés",
            region)

        return triple_vertical_graphs_rates(
            dff1, dff2, dff3, title, name1, name2, name3, type="percent")

    # def update_graph(region, demo):
    #     dff1 = VolRate_2018[VolRate_2018['Region'] == region]
    #     dff1 = dff1[dff1['Group'] == demo]
    #     dff1 = dff1.replace('Volunteering', 'Volontariat')
    #     name1 = "Volontariat"

    #     dff2 = FormsVolunteering_2018[FormsVolunteering_2018['Region'] == region]
    #     dff2 = dff2[dff2['Group'] == demo]
    #     dff2 = dff2[dff2['QuestionText'] == 'Aider les gens directement']
    #     dff2 = dff2.replace("Helping others", "Aider les autres")
    #     # name2 = "Helping others"
    #     name2 = "Aider les autres"

    #     dff3 = FormsVolunteering_2018[FormsVolunteering_2018['Region'] == region]
    #     dff3 = dff3[dff3['Group'] == demo]
    #     dff3 = dff3[dff3['QuestionText'] == 'Améliorer la communauté']
    #     dff3 = dff3.replace("Community involvement", "Participation de la communauté")
    #     # name3 = "Community involvement"
    #     name3 = "Participation de la communauté"

    #     title = '{}, {}'.format("Probabilité de soutenir selon les caractéristiques personnelles et économiques clés", region)

    # return triple_vertical_graphs_rates(dff1, dff2, dff3, title, name1,
    # name2, name3, type="percent")
