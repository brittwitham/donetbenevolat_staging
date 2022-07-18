import numpy as np
import pandas as pd
import os
import os.path as op

def get_data():
    filepath = op.join(os.getcwd(), "tables","{}")
        
    ReasonsVol_2018 = pd.read_csv(op.abspath(filepath.format("2018-ReasonsForVolunteering_FR.csv")))
    AvgHrsReasons_2018 = pd.read_csv(op.abspath(filepath.format("2018-AvgHoursMotivations_FR.csv")))
    MotivationsVolByCause_2018 = pd.read_csv(op.abspath(filepath.format("2018-MotivationsVolByCause_FR.csv")))

    ReasonsVol_2018['Estimate'] = ReasonsVol_2018['Estimate'] * 100
    ReasonsVol_2018['CI Upper'] = ReasonsVol_2018['CI Upper'] * 100
    MotivationsVolByCause_2018['Estimate'] = MotivationsVolByCause_2018['Estimate'] * 100
    MotivationsVolByCause_2018['CI Upper'] = MotivationsVolByCause_2018['CI Upper'] * 100

    return ReasonsVol_2018, AvgHrsReasons_2018, MotivationsVolByCause_2018

def process_data(data):
    for i in range(len(data)):
        data[i]["Estimate"] = np.where(data[i]["Marker"] == "...", 0, data[i]["Estimate"])
        data[i]["CI Upper"] = np.where(data[i]["Marker"] == "...", 0, data[i]["CI Upper"])

        data[i]["Group"] = np.where(data[i]["Attribute"] == "Unable to determine", "", data[i]["Group"])
        data[i]["Group"] = np.where(data[i]["Attribute"] == "Unknown", "", data[i]["Group"])

        data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15)
        data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Do not support<br>cause", "Do not support cause", data[i]["Attribute"])
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Do not report<br>motivation", "Do not report motivation", data[i]["Attribute"])
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Report<br>motivation", "Report motivation", data[i]["Attribute"])

        data[i]["QuestionText"] = data[i]["QuestionText"].str.wrap(30)
        data[i]["QuestionText"] = data[i]["QuestionText"].replace({'\n': '<br>'}, regex=True)

        data[i]['Estimate'] = data[i]['Estimate'].round(0).astype(int)
        data[i]["CI Upper"] = data[i]["CI Upper"].round(0).astype(int)
        data[i]['cv'] = data[i]['cv'].round(2)


def translate(df):
    df = df.replace('Age group', "Groupe d'âge")
    df = df.replace('Gender', "Genre")
    df = df.replace('Education', "Éducation")
    df = df.replace('Marital status (original)', "État civil (original)")
    df = df.replace('Marital status (Original)', "État civil (original)")
    df = df.replace('Marital status', "État civil") 
    df = df.replace('Labour force status', "Situation d'activité")
    df = df.replace('Personal income category', "Catégorie de revenu personnel")
    df = df.replace('Family income category', "Catégorie de revenu familial")
    df = df.replace('Frequency of religious attendance', "Fréquence de la fréquentation religieuse")
    df = df.replace('Immigration status', "Statut d'immigration")
    
    #GENDER
    df = df.replace('Male gender', "Hommes")
    df = df.replace('Female gender', "Femmes")

    #AGE
    df = df.replace('15 to 24 years', '15 à 24 ans')
    df = df.replace('25 to 34 years', '25 à 34 ans')
    df = df.replace('35 to 44 years', '35 à 44 ans')
    df = df.replace('45 to 54 years', '45 à 54 ans')
    df = df.replace('55 to 64 years', '55 à 64 ans')
    df = df.replace('65 to 74 years', '65 à 74 ans')
    df = df.replace('75 years and over', '75 ans et plus')

    #EDUCATION
    df = df.replace('Less than High School', "Sans diplôme d'études secondaires")
    df = df.replace('Graduated from High school', "Diplôme d'études secondaires")
    df = df.replace('Post-secondary diploma', 'Diplôme post-secondaire')
    df = df.replace('University Diploma', "Diplôme universtaire")

    #INCOME
    df = df.replace('Less than $25,000', 'Moins de 25 000 $')
    df = df.replace('$25,000 to $49,999', '25 000 $ à 49 999 $')
    df = df.replace('$50,000 to $74,999', '50 000 $ a 74 999 $')
    df = df.replace('$75,000 to $99,999', '75 000 $ à 99 999 $')
    df = df.replace('$100,000 to $124,999', '100 000 $ à 124 999 $')
    df = df.replace('$125,000 and more', '125 000 $ et plus')

    #RELIGIOUS ATTENDANCE
    df = df.replace('At least once a week', 'Au moins 1 fois par semaine')
    df = df.replace('At least once a month', 'Au moins 1 fois par mois')
    df = df.replace('At least 3 times a year', 'Au moins 3 fois par mois')
    df = df.replace('Once or twice a year', '1 ou 2 fois par an')
    df = df.replace('Not at all', 'Pas du tout')

    #MARITAL STATUS
    df = df.replace('Married/common-law', 'Marié.e/union de fait')
    df = df.replace('Separated/divorced', 'Séparé.e/divorcé.e')

    df = df.replace('Married', 'Marié.e')
    df = df.replace('Living common-law', 'Union de fait')
    df = df.replace('Separated', 'Séparé.e')
    df = df.replace('Divorced', 'divorcé.e')
    df = df.replace('Widowed', 'Veuf.ve')
    df = df.replace('Single, never married', 'Célibataire, jamais marié.e')

    #EMPLOYMENT STATUS
    df = df.replace('Employed', 'Employé.e')
    df = df.replace('Unemployed', 'Au chômage')
    df = df.replace('Not in labour force', 'Pas dans la population active')

    #IMMIGRATON STATUS
    df = df.replace('Native-born', 'Né.e au Canada')
    df = df.replace('Naturalized', 'Naturalisé.e')
    df = df.replace('Non-Canadian', 'Non canadien.ne')
    
    return df

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