# data_utils.py
import pandas as pd
import numpy as np
import os
import os.path as op

values = ["Use with caution", "Estimate suppressed", ""]

def get_data():
    filepath = op.join(os.getcwd(),"tables","{}")

    DonMethAvgDon_2018 = pd.read_csv(op.abspath(filepath.format("2018-DonMethAvgDon_FR.csv")))
    DonMethDonRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-DonMethDonRates_FR.csv")))
    # DonMethAvgDon_2018 = pd.read_csv(os.path.abspath(filepath.format("2018-DonMethAvgDon.csv")))
    # DonMethDonRates_2018 = pd.read_csv(os.path.abspath(filepath.format("2018-DonMethDonRates.csv")))
    # DonMethAvgDon_2018 = pd.read_csv("./tables/2018-DonMethAvgDon.csv")
    # DonMethDonRates_2018 = pd.read_csv("./tables/2018-DonMethDonRates.csv")

    DonMethDonRates_2018['Estimate'] = DonMethDonRates_2018['Estimate']*100
    DonMethDonRates_2018['CI Upper'] = DonMethDonRates_2018['CI Upper']*100

    return DonMethAvgDon_2018, DonMethDonRates_2018

def process_data(data):
    
    for i in range(len(data)):
        data[i]["Estimate"] = np.where(data[i]["Marker"]=="...", 0, data[i]["Estimate"])
        data[i]["CI Upper"] = np.where(data[i]["Marker"]=="...", 0, data[i]["CI Upper"])


        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unable to determine", "", data[i]["Group"])
        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unknown", "", data[i]["Group"])

        data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15)
        data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)

        data[i]['Estimate'] = data[i]['Estimate'].round(0).astype(int)
        data[i]["CI Upper"] = data[i]["CI Upper"].round(0).astype(int)
        data[i]['cv'] = data[i]['cv'].round(2)

def get_region_values():
    return np.array(['CA', 'BC', 'AB', 'PR', 'ON', 'QC', 'AT'], dtype=object)

def get_region_names():
    return np.array(['Canada',
                         'British Columbia',
                         'Alberta',
                         'Prairie Provinces (SK, MB)',
                         'Ontario',
                         'Quebec',
                         'Atlantic Provinces (NB, NS, PE, NL)'], dtype=str)
    
    
# def translate_data(df):
#     df.QuestionText = df.QuestionText.replace('Public place', 'Lieu public')
#     df.QuestionText = df.QuestionText.replace('Place of worship', 'Lieu de culture')
#     df.QuestionText = df.QuestionText.replace('Sponsoring someone', "Parrainage de quelqu'un")
#     df.QuestionText = df.QuestionText.replace('On own', 'Initiative personnelle')
#     df.QuestionText = df.QuestionText.replace('In memoriam', 'À la mémoire')
#     df.QuestionText = df.QuestionText.replace('Door-to-door canvassing', 'Porte-à-porte')
#     df.QuestionText = df.QuestionText.replace('Charity event', 'Activité caritative')
#     df.QuestionText = df.QuestionText.replace('At work', 'Au travail')
#     df.QuestionText = df.QuestionText.replace('Mail request', 'Demande par lettre')
#     df.QuestionText = df.QuestionText.replace('Online', 'En ligne')
#     df.QuestionText = df.QuestionText.replace('TV or radio request', 'Demande à la télé ou la radio')
#     df.QuestionText = df.QuestionText.replace('Telephone request', 'Demande au téléphone')
#     df.QuestionText = df.QuestionText.replace('Any other method', 'Autre méthode')

#     #GENDER
#     df.Attribute = df.Attribute.replace('Male gender', "Hommes")
#     df.Attribute = df.Attribute.replace('Female gender', "Femmes")

#     #AGE
#     df.Attribute = df.Attribute.replace('15 to 24 years', '15 à 24 ans')
#     df.Attribute = df.Attribute.replace('25 to 34 years', '25 à 34 ans')
#     df.Attribute = df.Attribute.replace('35 to 44 years', '35 à 44 ans')
#     df.Attribute = df.Attribute.replace('45 to 54 years', '45 à 54 ans')
#     df.Attribute = df.Attribute.replace('55 to 64 years', '55 à 64 ans')
#     df.Attribute = df.Attribute.replace('65 to 74 years', '65 à 74 ans')
#     df.Attribute = df.Attribute.replace('75 years and over', '75 ans et plus')

#     #EDUCATION
#     df.Attribute = df.Attribute.replace('Less than High School', "Sans diplôme d'études secondaires")
#     df.Attribute = df.Attribute.replace('Graduated from High school', "Diplôme d'études secondaires")
#     df.Attribute = df.Attribute.replace('Post-secondary diploma', 'Diplôme post-secondaire')
#     df.Attribute = df.Attribute.replace('University Diploma', "Diplôme universtaire")

#     #INCOME
#     df.Attribute = df.Attribute.replace('Less than $25,000', 'Moins de 25 000 $')
#     df.Attribute = df.Attribute.replace('$25,000 to $49,999', '25 000 $ à 49 999 $')
#     df.Attribute = df.Attribute.replace('$50,000 to $74,999', '$50,000 to $74,999')
#     df.Attribute = df.Attribute.replace('$75,000 to $99,999', '75 000 $ à 99 999 $')
#     df.Attribute = df.Attribute.replace('$100,000 to $124,999', '100 000 $ à 124 999 $')
#     df.Attribute = df.Attribute.replace('$125,000 and more', '125 000 $ et plus')

#     #RELIGIOUS ATTENDANCE
#     df.Attribute = df.Attribute.replace('At least once a week', 'Au moins 1 fois par semaine')
#     df.Attribute = df.Attribute.replace('At least once a month', 'Au moins 1 fois par mois')
#     df.Attribute = df.Attribute.replace('At least 3 times a year', 'Au moins 3 fois par mois')
#     df.Attribute = df.Attribute.replace('Once or twice a year', '1 ou 2 fois par an')
#     df.Attribute = df.Attribute.replace('Not at all', 'Pas du tout')

#     #MARITAL STATUS
#     df.Attribute = df.Attribute.replace('Married/common-law', 'Marié.e/union de fait')
#     df.Attribute = df.Attribute.replace('Separated/divorced', 'Séparé.e/divorcé.e')

#     df.Attribute = df.Attribute.replace('Married', 'Marié.e')
#     df.Attribute = df.Attribute.replace('Living common-law', 'Union de fait')
#     df.Attribute = df.Attribute.replace('Separated', 'Séparé.e')
#     df.Attribute = df.Attribute.replace('Divorced', 'divorcé.e')
#     df.Attribute = df.Attribute.replace('Widowed', 'Veuf.ve')
#     df.Attribute = df.Attribute.replace('Single, never married', 'Célibataire, jamais marié.e')

#     #EMPLOYMENT STATUS
#     df.Attribute = df.Attribute.replace('Employed', 'Employé.e')
#     df.Attribute = df.Attribute.replace('Unemployed', 'Au chômage')
#     df.Attribute = df.Attribute.replace('Not in labour force', 'Pas dans la population active')

#     #IMMIGRATON STATUS
#     df.Attribute = df.Attribute.replace('Native-born', 'Né.e au Canada')
#     df.Attribute = df.Attribute.replace('Naturalized', 'Naturalisé.e')
#     df.Attribute = df.Attribute.replace('Non-Canadian', 'Non canadien.ne')