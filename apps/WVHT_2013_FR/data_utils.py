import pandas as pd
import plotly.graph_objects as go
import numpy as np
import os
import os.path as op


def get_data():
    filepath = op.join(os.getcwd(), "tables", "{}")

    # DonMethAvgDon_2018 = pd.read_csv(op.abspath(filepath.format("2018-DonMethAvgDon.csv")))
    VolRate_2018 = pd.read_csv(op.abspath(
        filepath.format("2013-VolRate_FR.csv")))
    AvgTotHours_2018 = pd.read_csv(op.abspath(
        filepath.format("2013-AvgTotHours_FR.csv")))
    FormsVolunteering_2018 = pd.read_csv(op.abspath(
        filepath.format("2013-FormsVolunteering_FR.csv")))
    # PercTotVols_2018 = pd.read_csv(op.abspath(filepath.format("2018-PercTotVolunteers-updated_FR.csv")))
    PercTotVols_2018 = pd.read_csv(op.abspath(
        filepath.format("2013-PercTotPopn_FR.csv")))
    # PercTotVols_2018 = pd.read_csv('tables/2018-PercTotVolunteers-updated.csv', encoding = 'unicode_escape', engine ='python')
    PercTotHours_2018 = pd.read_csv(op.abspath(
        filepath.format("2013-PercTotHours_FR.csv")))

    VolRate_2018['Estimate'] = VolRate_2018['Estimate'] * 100
    VolRate_2018['CI Upper'] = VolRate_2018['CI Upper'] * 100
    FormsVolunteering_2018['Estimate'] = FormsVolunteering_2018['Estimate'] * 100
    FormsVolunteering_2018['CI Upper'] = FormsVolunteering_2018['CI Upper'] * 100
    PercTotVols_2018['Estimate'] = PercTotVols_2018['Estimate'] * 100
    PercTotVols_2018['CI Upper'] = PercTotVols_2018['CI Upper'] * 100
    PercTotHours_2018['Estimate'] = PercTotHours_2018['Estimate'] * 100
    PercTotHours_2018['CI Upper'] = PercTotHours_2018['CI Upper'] * 100

    return VolRate_2018, AvgTotHours_2018, FormsVolunteering_2018, PercTotVols_2018, PercTotHours_2018


def process_data(data):
    for i in range(len(data)):
        data[i]["Estimate"] = np.where(
            data[i]["Marker"] == "...", 0, data[i]["Estimate"])
        data[i]["CI Upper"] = np.where(
            data[i]["Marker"] == "...", 0, data[i]["CI Upper"])

        data[i]["Region"] = np.select([data[i]["Province"] == "SK",
                                       data[i]["Province"] == "MB",
                                       data[i]["Province"] == "NB",
                                       data[i]["Province"] == "NS",
                                       data[i]["Province"] == "PE",
                                       data[i]["Province"] == "NL"],
                                      ["SK", "MB", "NB", "NS", "PE", "NL"], default=data[i]["Region"])

        data[i]["Group"] = np.where(
            data[i]["Attribute"] == "Unable to determine",
            "",
            data[i]["Group"])
        data[i]["Group"] = np.where(
            data[i]["Attribute"] == "Unknown", "", data[i]["Group"])

        data[i]["Attribute"] = data[i]["Attribute"].str.wrap(
            15, break_long_words=False)
        data[i]["Attribute"] = data[i]["Attribute"].replace(
            {'\n': '<br>'}, regex=True)

        data[i]['Estimate'] = data[i]['Estimate'].round(0).astype(int)
        data[i]["CI Upper"] = data[i]["CI Upper"].round(0).astype(int)
        data[i]['cv'] = data[i]['cv'].round(2)

    return data


def translate(df):
    df = df.replace('Age group', "Groupe d'âge")
    df = df.replace('Gender', "Genre")
    df = df.replace('Education', "Éducation")
    df = df.replace('Marital status (original)', "État civil (original)")
    df = df.replace('Marital status (Original)', "État civil (original)")
    df = df.replace('Marital status', "État civil")
    df = df.replace('Labour force status', "Situation d'activité")
    df = df.replace(
        'Personal income category',
        "Catégorie de revenu personnel")
    df = df.replace('Family income category', "Catégorie de revenu familial")
    df = df.replace(
        'Frequency of religious attendance',
        "Fréquence de la fréquentation religieuse")
    df = df.replace('Immigration status', "Statut d'immigration")

    # GENDER
    df = df.replace('Male gender', "Hommes")
    df = df.replace('Female gender', "Femmes")

    # AGE
    df = df.replace('15 to 24 years', '15 à 24 ans')
    df = df.replace('25 to 34 years', '25 à 34 ans')
    df = df.replace('35 to 44 years', '35 à 44 ans')
    df = df.replace('45 to 54 years', '45 à 54 ans')
    df = df.replace('55 to 64 years', '55 à 64 ans')
    df = df.replace('65 to 74 years', '65 à 74 ans')
    df = df.replace('75 years and over', '75 ans et plus')

    # EDUCATION
    df = df.replace(
        'Less than High School',
        "Sans diplôme d'études secondaires")
    df = df.replace(
        'Graduated from High school',
        "Diplôme d'études secondaires")
    df = df.replace('Post-secondary diploma', 'Diplôme post-secondaire')
    df = df.replace('University Diploma', "Diplôme universtaire")

    # INCOME
    df = df.replace('Less than $25,000', 'Moins de 25 000 $')
    df = df.replace('$25,000 to $49,999', '25 000 $ à 49 999 $')
    df = df.replace('$50,000 to $74,999', '50 000 $ a 74 999 $')
    df = df.replace('$75,000 to $99,999', '75 000 $ à 99 999 $')
    df = df.replace('$100,000 to $124,999', '100 000 $ à 124 999 $')
    df = df.replace('$125,000 and more', '125 000 $ et plus')

    # RELIGIOUS ATTENDANCE
    df = df.replace('At least once a week', 'Au moins 1 fois par semaine')
    df = df.replace('At least once a month', 'Au moins 1 fois par mois')
    df = df.replace('At least 3 times a year', 'Au moins 3 fois par mois')
    df = df.replace('Once or twice a year', '1 ou 2 fois par an')
    df = df.replace('Not at all', 'Pas du tout')

    # MARITAL STATUS
    df = df.replace('Married/common-law', 'Marié.e/union de fait')
    df = df.replace('Separated/divorced', 'Séparé.e/divorcé.e')

    df = df.replace('Married', 'Marié.e')
    df = df.replace('Living common-law', 'Union de fait')
    df = df.replace('Separated', 'Séparé.e')
    df = df.replace('Divorced', 'divorcé.e')
    df = df.replace('Widowed', 'Veuf.ve')
    df = df.replace('Single, never married', 'Célibataire, jamais marié.e')

    # EMPLOYMENT STATUS
    df = df.replace('Employed', 'Employé.e')
    df = df.replace('Unemployed', 'Au chômage')
    df = df.replace('Not in labour force', 'Pas dans la population active')

    # IMMIGRATON STATUS
    df = df.replace('Native-born', 'Né.e au Canada')
    df = df.replace('Naturalized', 'Naturalisé.e')
    df = df.replace('Non-Canadian', 'Non canadien.ne')

    return df


def get_region_values():
    return np.array(['CA', 'BC', 'AB', 'PR', 'SK', 'MB', 'ON',
                    'QC', 'AT', 'NB', 'NS', 'PE', 'NL'], dtype=object)


def get_region_names():
    return np.array(['Canada',
                     'British Columbia',
                     'Alberta',
                     'Prairie Provinces (SK, MB)',
                     'Saskatchewan',
                     'Manitoba',
                     'Ontario',
                     'Quebec',
                     'Atlantic Provinces (NB, NS, PE, NL)',
                     'New Brunswick',
                     'Nova Scotia',
                     'Prince Edward Island',
                     'Newfoundland and Labrador'], dtype=str)
