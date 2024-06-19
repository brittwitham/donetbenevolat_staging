# Callbacks file for WVHT_2018_FR converted from Qui_sont_les_benevoles_et_combien_heures_donnent_ils_2018.py

import dash
from .data_processing import *
from .graphs import *

def register_callbacks(app):
    @app.callback(
        dash.dependencies.Output('FormsVolunteering', 'figure'),
        [

            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):

        dff1 = FormsVolunteering_2018[FormsVolunteering_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "All"]
        dff1 = dff1.replace("Formal volunteer", "Bénévolat <br> encadré")
        dff1 = dff1.replace("Informal volunteer", "Bénévolat <br> non encadré")
        dff1 = dff1.replace("Help people directly", "Aider les gens <br> directement")
        dff1 = dff1.replace("Improve community", "Améliorer <br> la communauté")

        title = '{}, {}'.format("Formes de bénévolat", region)

        return forms_of_giving(dff1, title)

    @app.callback(
        dash.dependencies.Output('VolRateAvgHours-Gndr', 'figure'),
        [

            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):

        dff1 = VolRate_2018[VolRate_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Genre"]
        # dff1 = dff1.replace("Male gender", "Hommes")
        # dff1 = dff1.replace("Female gender", "Femmes")
        dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")

        # name1 = "Volunteer rate"
        name1 = 'Taux de bénévolat'


        dff2 = AvgTotHours_2018[AvgTotHours_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Genre"]
        # dff2 = dff2.replace("Male gender", "Hommes")
        # dff2 = dff2.replace("Female gender", "Femmes")
        dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")

        # name2 = "Average hours"
        name2 = "Nombre d'heures moyen"

        title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures de bénévolat selon le genre", region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(
        dash.dependencies.Output('PercVolHours-Gndr', 'figure'),
        [

            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff1 = PercTotVols_2018[PercTotVols_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Genre"]
        # dff1 = dff1[dff1['Group'] == "Gender"]
        # dff1 = dff1.replace("Male gender", "Hommes")
        # dff1 = dff1.replace("Female gender", "Femmes")
        dff1 = dff1.replace("% volunteers", "% population")
        # name1 = "% volunteers"
        name1 = "% population"


        dff2 = PercTotHours_2018[PercTotHours_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Genre"]
        # dff2 = dff2.replace("Male gender", "Hommes")
        # dff2 = dff2.replace("Female gender", "Femmes")
        dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
        name2 = "% heures de bénévolat"

        title = '{}, {}'.format("Pourcentage de la population et nombre total d’heures de bénévolat selon le genre", region)

        return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    @app.callback(
        dash.dependencies.Output('PercVolHours-Age', 'figure'),
        [

            dash.dependencies.Input('region-selection', 'value')
        ])

    def update_graph(region):
        dff1 = PercTotVols_2018[PercTotVols_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Groupe d'âge"]
        # dff1 = dff1.replace('15 to 24 years', '15 à 24 ans')
        # dff1 = dff1.replace('25 to 34 years', '25 à 34 ans')
        # dff1 = dff1.replace('35 to 44 years', '35 à 44 ans')
        # dff1 = dff1.replace('45 to 54 years', '45 à 54 ans')
        # dff1 = dff1.replace('55 to 64 years', '55 à 64 ans')
        # dff1 = dff1.replace('65 to 74 years', '65 à 74 ans')
        # dff1 = dff1.replace('75 years and over', '75 ans et plus')
        dff1 = dff1.replace("% volunteers", "% population")
        # name1 = "% volunteers"
        name1 = "% population"


        dff2 = PercTotHours_2018[PercTotHours_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Groupe d'âge"]
        # dff2 = dff2.replace('15 to 24 years', '15 à 24 ans')
        # dff2 = dff2.replace('25 to 34 years', '25 à 34 ans')
        # dff2 = dff2.replace('35 to 44 years', '35 à 44 ans')
        # dff2 = dff2.replace('45 to 54 years', '45 à 54 ans')
        # dff2 = dff2.replace('55 to 64 years', '55 à 64 ans')
        # dff2 = dff2.replace('65 to 74 years', '65 à 74 ans')
        # dff2 = dff2.replace('75 years and over', '75 ans et plus')
        dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
        name2 = "% heures de bénévolat"
        # name2 = "% volunteer hours"

        title = '{}, {}'.format("Pourcentage de la population et du <br> nombre total d’heures de bénévolat selon l’âge", region)

        return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    @app.callback(
        dash.dependencies.Output('VolRateAvgHours-Age', 'figure'),
        [

            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):

        dff1 = VolRate_2018[VolRate_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Groupe d'âge"]
        # dff1 = dff1.replace('15 to 24 years', '15 à 24 ans')
        # dff1 = dff1.replace('25 to 34 years', '25 à 34 ans')
        # dff1 = dff1.replace('35 to 44 years', '35 à 44 ans')
        # dff1 = dff1.replace('45 to 54 years', '45 à 54 ans')
        # dff1 = dff1.replace('55 to 64 years', '55 à 64 ans')
        # dff1 = dff1.replace('65 to 74 years', '65 à 74 ans')
        # dff1 = dff1.replace('75 years and over', '75 ans et plus')
        dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")

        # name1 = "Volunteer rate"
        name1 = 'Taux de bénévolat'

        dff2 = AvgTotHours_2018[AvgTotHours_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Groupe d'âge"]
        # dff2 = dff2.replace('15 to 24 years', '15 à 24 ans')
        # dff2 = dff2.replace('25 to 34 years', '25 à 34 ans')
        # dff2 = dff2.replace('35 to 44 years', '35 à 44 ans')
        # dff2 = dff2.replace('45 to 54 years', '45 à 54 ans')
        # dff2 = dff2.replace('55 to 64 years', '55 à 64 ans')
        # dff2 = dff2.replace('65 to 74 years', '65 à 74 ans')
        # dff2 = dff2.replace('75 years and over', '75 ans et plus')
        # dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
        dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")

        # name2 = "Average hours"
        name2 = "Nombre d'heures moyen"

        title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures <br> de bénévolat selon le groupe d'âge", region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)


    @app.callback(
        dash.dependencies.Output('VolRateAvgHours-Educ', 'figure'),
        [

            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):

        dff1 = VolRate_2018[VolRate_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Éducation"]
        # dff1 = dff1.replace('Less than High School', "Sans diplôme d'études secondaires")
        # dff1 = dff1.replace('Graduated from High school', "Diplôme d'études secondaires")
        # dff1 = dff1.replace('Post-secondary diploma', 'Diplôme post-secondaire')
        # dff1 = dff1.replace('University Diploma', "Diplôme universtaire")
        dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")

        # name1 = "Volunteer rate"
        name1 = 'Taux de bénévolat'


        dff2 = AvgTotHours_2018[AvgTotHours_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Éducation"]
        # dff2 = dff2.replace('Less than High School', "Sans diplôme d'études secondaires")
        # dff2 = dff2.replace('Graduated from High school', "Diplôme d'études secondaires")
        # dff2 = dff2.replace('Post-secondary diploma', 'Diplôme post-secondaire')
        # dff2 = dff2.replace('University Diploma', "Diplôme universtaire")
        # dff2 = dff2.replace("Volunteer rate", "Taux de bénévolat")
        dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")

        # name2 = "Average hours"
        name2 = "Nombre d'heures moyen"

        title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures <br> de bénévolat selon l’éducation ", region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)


    @app.callback(
        dash.dependencies.Output('PercVolHours-Educ', 'figure'),
        [

            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):



        dff1 = PercTotVols_2018[PercTotVols_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Éducation"]
        # dff1 = dff1.replace('Less than High School', "Sans diplôme d'études secondaires")
        # dff1 = dff1.replace('Graduated from High school', "Diplôme d'études secondaires")
        # dff1 = dff1.replace('Post-secondary diploma', 'Diplôme post-secondaire')
        # dff1 = dff1.replace('University Diploma', "Diplôme universtaire")
        # dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")
        dff1 = dff1.replace("% volunteers", "% population")
        # name1 = "% volunteers"
        name1 = "% population"


        dff2 = PercTotHours_2018[PercTotHours_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Éducation"]
        # dff2 = dff2.replace('Less than High School', "Sans diplôme d'études secondaires")
        # dff2 = dff2.replace('Graduated from High school', "Diplôme d'études secondaires")
        # dff2 = dff2.replace('Post-secondary diploma', 'Diplôme post-secondaire')
        # dff2 = dff2.replace('University Diploma', "Diplôme universtaire")
        # dff2 = dff2.replace("Volunteer rate", "Taux de bénévolat")
        dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
        name2 = "% heures de bénévolat"
        # name2 = "% volunteer hours"

        title = '{}, {}'.format("Pourcentage de la population et du nombre total <br> d’heures de bénévolat selon l’éducation", region)

        return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    @app.callback(
        dash.dependencies.Output('VolRateAvgHours-MarStat', 'figure'),
        [

            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):

        dff1 = VolRate_2018[VolRate_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "État civil"]
        # dff1 = dff1.replace('Married/common-law', 'Marié.e/union de fait')
        # dff1 = dff1.replace('Separated/divorced', 'Séparé.e/divorcé.e')
        # dff1 = dff1.replace('Married', 'Marié.e')
        # dff1 = dff1.replace('Living common-law', 'Union de fait')
        # dff1 = dff1.replace('Separated', 'Séparé.e')
        # dff1 = dff1.replace('Divorced', 'divorcé.e')
        # dff1 = dff1.replace('Widowed', 'Veuf.ve')
        # dff1 = dff1.replace('Single, never married', 'Célibataire, jamais marié.e')
        dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")

        # name1 = "Volunteer rate"
        name1 = 'Taux de bénévolat'


        dff2 = AvgTotHours_2018[AvgTotHours_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "État civil"]
        # dff2 = dff2.replace('Married/common-law', 'Marié.e/union de fait')
        # dff2 = dff2.replace('Separated/divorced', 'Séparé.e/divorcé.e')
        # dff2 = dff2.replace('Married', 'Marié.e')
        # dff2 = dff2.replace('Living common-law', 'Union de fait')
        # dff2 = dff2.replace('Separated', 'Séparé.e')
        # dff2 = dff2.replace('Divorced', 'divorcé.e')
        # dff2 = dff2.replace('Widowed', 'Veuf.ve')
        # dff2 = dff2.replace('Single, never married', 'Célibataire, jamais marié.e')

        dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")

        # name2 = "Average hours"
        name2 = "Nombre d'heures moyen"

        title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures <br> de bénévolat selon la situation matrimoniale", region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)


    @app.callback(
        dash.dependencies.Output('PercVolHours-MarStat', 'figure'),
        [

            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff1 = PercTotVols_2018[PercTotVols_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "État civil"]
        # dff1 = dff1.replace('Married/common-law', 'Marié.e/union de fait')
        # dff1 = dff1.replace('Separated/divorced', 'Séparé.e/divorcé.e')
        # dff1 = dff1.replace('Married', 'Marié.e')
        # dff1 = dff1.replace('Living common-law', 'Union de fait')
        # dff1 = dff1.replace('Separated', 'Séparé.e')
        # dff1 = dff1.replace('Divorced', 'divorcé.e')
        # dff1 = dff1.replace('Widowed', 'Veuf.ve')
        # dff1 = dff1.replace('Single, never married', 'Célibataire, jamais marié.e')
        dff1 = dff1.replace("% volunteers", "% population")
        # name1 = "% volunteers"
        name1 = "% population"


        dff2 = PercTotHours_2018[PercTotHours_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "État civil"]
        # dff2 = dff2.replace('Married/common-law', 'Marié.e/union de fait')
        # dff2 = dff2.replace('Separated/divorced', 'Séparé.e/divorcé.e')
        # dff2 = dff2.replace('Married', 'Marié.e')
        # dff2 = dff2.replace('Living common-law', 'Union de fait')
        # dff2 = dff2.replace('Separated', 'Séparé.e')
        # dff2 = dff2.replace('Divorced', 'divorcé.e')
        # dff2 = dff2.replace('Widowed', 'Veuf.ve')
        # dff2 = dff2.replace('Single, never married', 'Célibataire, jamais marié.e')
        # dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
        dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
        name2 = "% heures de bénévolat"
        # name2 = "% volunteer hours"

        title = '{}, {}'.format("Pourcentage de la population et du nombre total <br> d’heures de bénévolat selon la situation matrimoniale", region)

        return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    @app.callback(
        dash.dependencies.Output('VolRateAvgHours-Inc', 'figure'),
        [

            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff1 = VolRate_2018[VolRate_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Catégorie de revenu personnel"]
        # dff1 = dff1.replace('Less than $25,000', 'Moins de 25,000 $')
        # dff1 = dff1.replace('$25,000 to $49,999', '25,000 $ à 49,999 $')
        # dff1 = dff1.replace('$50,000 to $74,999', '50,000 $ a 74,999 $')
        # dff1 = dff1.replace('$75,000 to $99,999', '75,000 $ à 99,999 $')
        # dff1 = dff1.replace('$100,000 to $124,999', '100,000 $ à 124,999 $')
        # dff1 = dff1.replace('$125,000 and more', '125,000 $ et plus')
        dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")

        # name1 = "Volunteer rate"
        name1 = 'Taux de bénévolat'


        dff2 = AvgTotHours_2018[AvgTotHours_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Catégorie de revenu personnel"]
        # dff2 = dff2.replace('Less than $25,000', 'Moins de 25,000 $')
        # dff2 = dff2.replace('$25,000 to $49,999', '25,000 $ à 49,999 $')
        # dff2 = dff2.replace('$50,000 to $74,999', '50,000 $ a 74,999 $')
        # dff2 = dff2.replace('$75,000 to $99,999', '75,000 $ à 99,999 $')
        # dff2 = dff2.replace('$100,000 to $124,999', '100,000 $ à 124,999 $')
        # dff2 = dff2.replace('$125,000 and more', '125,000 $ et plus')
        # dff2 = dff2.replace("Volunteer rate", "Taux de bénévolat")
        dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")

        # name2 = "Average hours"
        name2 = "Nombre d'heures moyen"

        title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures <br> de bénévolat selon le revenu", region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(
        dash.dependencies.Output('PercVolHours-Inc', 'figure'),
        [

            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff1 = PercTotVols_2018[PercTotVols_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Catégorie de revenu personnel"]
        # dff1 = dff1.replace('Less than $25,000', 'Moins de 25,000 $')
        # dff1 = dff1.replace('$25,000 to $49,999', '25,000 $ à 49,999 $')
        # dff1 = dff1.replace('$50,000 to $74,999', '50,000 $ a 74,999 $')
        # dff1 = dff1.replace('$75,000 to $99,999', '75,000 $ à 99,999 $')
        # dff1 = dff1.replace('$100,000 to $124,999', '100,000 $ à 124,999 $')
        # dff1 = dff1.replace('$125,000 and more', '125,000 $ et plus')
        dff1 = dff1.replace("% volunteers", "% population")
        # name1 = "% volunteers"
        name1 = "% population"


        dff2 = PercTotHours_2018[PercTotHours_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Catégorie de revenu personnel"]
        dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
        # dff2 = dff2.replace('Less than $25,000', 'Moins de 25,000 $')
        # dff2 = dff2.replace('$25,000 to $49,999', '25,000 $ à 49,999 $')
        # dff2 = dff2.replace('$50,000 to $74,999', '50,000 $ a 74,999 $')
        # dff2 = dff2.replace('$75,000 to $99,999', '75,000 $ à 99,999 $')
        # dff2 = dff2.replace('$100,000 to $124,999', '100,000 $ à 124,999 $')
        # dff2 = dff2.replace('$125,000 and more', '125,000 $ et plus')
        # dff2 = dff2.replace("Volunteer rate", "Taux de bénévolat")
        # dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
        name2 = "% heures de bénévolat"
        # name2 = "% volunteer hours"

        title = '{}, {}'.format("Pourcentage de la population et du nombre total <br> d’heures de bénévolat selon le revenu", region)

        return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    @app.callback(
        dash.dependencies.Output('VolRateAvgHours-Relig', 'figure'),
        [

            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):

        dff1 = VolRate_2018[VolRate_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Fréquence de la fréquentation religieuse"]
        # dff1 = dff1.replace('At least once a week', 'Au moins 1 fois par semaine')
        # dff1 = dff1.replace('At least once a month', 'Au moins 1 fois par mois')
        # dff1 = dff1.replace('At least 3 times a year', 'Au moins 3 fois par mois')
        # dff1 = dff1.replace('Once or twice a year', '1 ou 2 fois par an')
        # dff1 = dff1.replace('Not at all', 'Pas du tout')
        dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")

        # name1 = "Volunteer rate"
        name1 = 'Taux de bénévolat'


        dff2 = AvgTotHours_2018[AvgTotHours_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Fréquence de la fréquentation religieuse"]
        # dff2 = dff2.replace('At least once a week', 'Au moins 1 fois par semaine')
        # dff2 = dff2.replace('At least once a month', 'Au moins 1 fois par mois')
        # dff2 = dff2.replace('At least 3 times a year', 'Au moins 3 fois par mois')
        # dff2 = dff2.replace('Once or twice a year', '1 ou 2 fois par an')
        # dff2 = dff2.replace('Not at all', 'Pas du tout')
        dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")

        # name2 = "Average hours"
        name2 = "Nombre d'heures moyen"

        title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures de <br> bénévolat selon la pratique religieuse", region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)

    @app.callback(
        dash.dependencies.Output('PercVolHours-Relig', 'figure'),
        [

            dash.dependencies.Input('region-selection', 'value')
        ])
    def update_graph(region):
        dff1 = PercTotVols_2018[PercTotVols_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == "Fréquence de la fréquentation religieuse"]
        # dff1 = dff1.replace('At least once a week', 'Au moins 1 fois par semaine')
        # dff1 = dff1.replace('At least once a month', 'Au moins 1 fois par mois')
        # dff1 = dff1.replace('At least 3 times a year', 'Au moins 3 fois par mois')
        # dff1 = dff1.replace('Once or twice a year', '1 ou 2 fois par an')
        # dff1 = dff1.replace('Not at all', 'Pas du tout')
        dff1 = dff1.replace("% volunteers", "% population")
        # name1 = "% volunteers"
        name1 = "% population"


        dff2 = PercTotHours_2018[PercTotHours_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == "Fréquence de la fréquentation religieuse"]
        # dff2 = dff2.replace('At least once a week', 'Au moins 1 fois par semaine')
        # dff2 = dff2.replace('At least once a month', 'Au moins 1 fois par mois')
        # dff2 = dff2.replace('At least 3 times a year', 'Au moins 3 fois par mois')
        # dff2 = dff2.replace('Once or twice a year', '1 ou 2 fois par an')
        # dff2 = dff2.replace('Not at all', 'Pas du tout')
        # dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
        dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
        name2 = "% heures de bénévolat"
        # name2 = "% volunteer hours"

        title = '{}, {}'.format("Pourcentage de la population et du nombre total <br> d’heures de bénévolat selon la pratique religieuse", region)

        return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    # @app.callback(
    #     dash.dependencies.Output('VolRateAvgHours-Labour', 'figure'),
    #     [

    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):

    #     dff1 = VolRate_2018[VolRate_2018['Region'] == region]
    #     dff1 = dff1[dff1['Group'] == "Situation d'activité"]
    #     # dff1 = dff1.replace('Employed', 'Employé.e')
    #     # dff1 = dff1.replace('Unemployed', 'Au chômage')
    #     # dff1 = dff1.replace('Not in labour force', 'Pas dans la population active')
    #     dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")

    #     # name1 = "Volunteer rate"
    #     name1 = 'Taux de bénévolat'


    #     dff2 = AvgTotHours_2018[AvgTotHours_2018['Region'] == region]
    #     dff2 = dff2[dff2['Group'] == "Situation d'activité"]
    #     # dff2 = dff2.replace('Employed', 'Employé.e')
    #     # dff2 = dff2.replace('Unemployed', 'Au chômage')
    #     # dff2 = dff2.replace('Not in labour force', 'Pas dans la population active')
    #     dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")

    #     # name2 = "Average hours"
    #     name2 = "Nombre d'heures moyen"

    #     title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures de <br> bénévolat selon la situation d’emploi", region)

    #     return don_rate_avg_don(dff1, dff2, name1, name2, title)


    # @app.callback(
    #     dash.dependencies.Output('PercVolHours-Labour', 'figure'),
    #     [

    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):

    #     dff1 = PercTotVols_2018[PercTotVols_2018['Region'] == region]
    #     dff1 = dff1[dff1['Group'] == "Situation d'activité"]
    #     # dff1 = dff1.replace('Employed', 'Employé.e')
    #     # dff1 = dff1.replace('Unemployed', 'Au chômage')
    #     # dff1 = dff1.replace('Not in labour force', 'Pas dans la population active')
    #     # dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")
    #     dff1 = dff1.replace("% volunteers", "% population")
    #     # name1 = "% volunteers"
    #     name1 = "% population"


    #     dff2 = PercTotHours_2018[PercTotHours_2018['Region'] == region]
    #     dff2 = dff2[dff2['Group'] == "Situation d'activité"]
    #     # dff2 = dff2.replace('Employed', 'Employé.e')
    #     # dff2 = dff2.replace('Unemployed', 'Au chômage')
    #     # dff2 = dff2.replace('Not in labour force', 'Pas dans la population active')
    #     # dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
    #     dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
    #     name2 = "% heures de bénévolat"
    #     # name2 = "% volunteer hours"

    #     title = '{}, {}'.format("Pourcentage de la population et du nombre total <br> d’heures de bénévolat selon la situation d’emploi", region)

    #     return perc_don_perc_amt(dff1, dff2, name1, name2, title)

    # @app.callback(
    #     dash.dependencies.Output('VolRateAvgHours-ImmStat', 'figure'),
    #     [

    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):

    #     dff1 = VolRate_2018[VolRate_2018['Region'] == region]
    #     dff1 = dff1[dff1['Group'] == "Statut d'immigration"]
    #     # dff1 = dff1.replace('Native-born', 'Né.e au Canada')
    #     # dff1 = dff1.replace('Naturalized', 'Naturalisé.e')
    #     # dff1 = dff1.replace('Non-Canadian', 'Non canadien.ne')
    #     dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")

    #     # name1 = "Volunteer rate"
    #     name1 = 'Taux de bénévolat'


    #     dff2 = AvgTotHours_2018[AvgTotHours_2018['Region'] == region]
    #     dff2 = dff2[dff2['Group'] == "Statut d'immigration"]
    #     # dff2 = dff2.replace('Native-born', 'Né.e au Canada')
    #     # dff2 = dff2.replace('Naturalized', 'Naturalisé.e')
    #     # dff2 = dff2.replace('Non-Canadian', 'Non canadien.ne')
    #     dff2 = dff2.replace("Volunteer rate", "Taux de bénévolat")
    #     dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")

    #     # name2 = "Average hours"
    #     name2 = "Nombre d'heures moyen"

    #     title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures de <br> bénévolat selon le statut d’immigration", region)

    #     return don_rate_avg_don(dff1, dff2, name1, name2, title)

    # @app.callback(
    #     dash.dependencies.Output('PercVolHours-ImmStat', 'figure'),
    #     [

    #         dash.dependencies.Input('region-selection', 'value')
    #     ])
    # def update_graph(region):
    #     dff1 = PercTotVols_2018[PercTotVols_2018['Region'] == region]
    #     dff1 = dff1[dff1['Group'] == "Statut d'immigration"]
    #     # dff1 = dff1.replace('Native-born', 'Né.e au Canada')
    #     # dff1 = dff1.replace('Naturalized', 'Naturalisé.e')
    #     # dff1 = dff1.replace('Non-Canadian', 'Non canadien.ne')
    #     dff1 = dff1.replace("% volunteers", "% population")
    #     # name1 = "% volunteers"
    #     name1 = "% population"


    #     dff2 = PercTotHours_2018[PercTotHours_2018['Region'] == region]
    #     dff2 = dff2[dff2['Group'] == "Statut d'immigration"]
    #     # dff2 = dff2.replace('Native-born', 'Né.e au Canada')
    #     # dff2 = dff2.replace('Naturalized', 'Naturalisé.e')
    #     # dff2 = dff2.replace('Non-Canadian', 'Non canadien.ne')
    #     # dff2 = dff2.replace("Volunteer rate", "Taux de bénévolat")
    #     dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
    #     name2 = "% heures de bénévolat"
    #     # name2 = "% volunteer hours"

    #     title = '{}, {}'.format("Pourcentage de la population et du nombre total <br> d’heures de bénévolat selon le statut d’immigration", region)

    #     return perc_don_perc_amt(dff1, dff2, name1, name2, title)


    @app.callback(
        dash.dependencies.Output('status-hours', 'figure'),
        [

            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('status-selection2', 'value')

        ])
    def update_graph(region, status):

        dff1 = VolRate_2018[VolRate_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == status]
        dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")
        # name1 = "Volunteer rate"
        name1 = "Taux de bénévolat"


        dff2 = AvgTotHours_2018[AvgTotHours_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == status]

        dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")

        # name2 = "Average hours"
        name2 = "Nombre d'heures moyen"

        title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures de <br> bénévolat selon " + str(status).lower(), region)

        return don_rate_avg_don(dff1, dff2, name1, name2, title)


    @app.callback(
        dash.dependencies.Output('status-perc', 'figure'),
        [

            dash.dependencies.Input('region-selection', 'value'),
            dash.dependencies.Input('status-selection', 'value')

        ])
    def update_graph(region, status):
        dff1 = PercTotVols_2018[PercTotVols_2018['Region'] == region]
        dff1 = dff1[dff1['Group'] == status]
        dff1 = dff1.replace("% volunteers", "% population")
        # name1 = "% Canadians"
        name1 = "% population"


        dff2 = PercTotHours_2018[PercTotHours_2018['Region'] == region]
        dff2 = dff2[dff2['Group'] == status]
        dff2 = dff2.replace("% volunteer hours", "% heures de bénévolat")
        name2 = "% heures de bénévolat"
        # name2 = "% volunteer hours"

        title = '{}, {}'.format("Pourcentage de la population et du nombre total <br> d’heures de bénévolat selon " + str(status).lower(), region)

        return perc_don_perc_amt(dff1, dff2, name1, name2, title)
