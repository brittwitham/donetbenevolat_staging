# data_utils.py
import pandas as pd
import numpy as np
import glob
import os.path as op
import os

values = ["Use with caution", "Estimate suppressed", ""]

def process_data(data):
    for i in range(len(data)):
        # Suppress Estimate and CI Upper where necessary (for visualizations and error bars)
        data[i]["Estimate"] = np.where(data[i]["Marker"]=="...", 0, data[i]["Estimate"])
        data[i]["CI Upper"] = np.where(data[i]["Marker"]=="...", 0, data[i]["CI Upper"])

        data[i]["Region"] = np.select([data[i]["Province"] == "SK",
                                    data[i]["Province"] == "MB",
                                    data[i]["Province"] == "NB",
                                    data[i]["Province"] == "NS",
                                    data[i]["Province"] == "PE",
                                    data[i]["Province"] == "NL"],
                                    ["SK", "MB", "NB", "NS", "PE", "NL"], default=data[i]["Region"])

        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unable to determine", "", data[i]["Group"])
        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unknown", "", data[i]["Group"])

        data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15)
        data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)

        # Round rates and dollar amounts to zero decimal places
        data[i]['Estimate'] = data[i]['Estimate'].round(0).astype(int)
        data[i]["CI Upper"] = data[i]["CI Upper"].round(0).astype(int)
        data[i]['cv'] = data[i]['cv'].round(2)


def process_data_num(data_num):
    for i in range(len(data_num)):
        # Suppress Estimate and CI Upper where necessary (for visualizations and error bars)
        data_num[i]["Estimate"] = np.where(data_num[i]["Marker"]=="...", 0, data_num[i]["Estimate"])
        data_num[i]["CI Upper"] = np.where(data_num[i]["Marker"]=="...", 0, data_num[i]["CI Upper"])

        data_num[i]["Region"] = np.select([data_num[i]["Province"] == "SK",
                                        data_num[i]["Province"] == "MB",
                                        data_num[i]["Province"] == "NB",
                                        data_num[i]["Province"] == "NS",
                                        data_num[i]["Province"] == "PE",
                                        data_num[i]["Province"] == "NL"],
                                        ["SK", "MB", "NB", "NS", "PE", "NL"], default=data_num[i]["Region"])

        data_num[i]["Group"] = np.where(data_num[i]["Attribute"]=="Unable to determine", "", data_num[i]["Group"])
        data_num[i]["Group"] = np.where(data_num[i]["Attribute"]=="Unknown", "", data_num[i]["Group"])

        data_num[i]["Attribute"] = data_num[i]["Attribute"].str.wrap(15)
        data_num[i]["Attribute"] = data_num[i]["Attribute"].replace({'\n': '<br>'}, regex=True)

        # Round number amounts to two decimal places
        data_num[i]['Estimate'] = data_num[i]['Estimate'].round(1)
        data_num[i]["CI Upper"] = data_num[i]["CI Upper"].round(1)
        data_num[i]['cv'] = data_num[i]['cv'].round(2)

# TODO: Refactor into functions once working example complete
def get_data():
    filepath = op.join(os.getcwd(),"tables","{}")

    DonRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-DonRate_FR.csv")))
    AvgTotDon_2018 = pd.read_csv(op.abspath(filepath.format("2018-AvgTotDon_FR.csv")))
    AvgNumCauses_2018 = pd.read_csv(op.abspath(filepath.format("2018-AvgNumCauses_FR.csv")))
    FormsGiving_2018 = pd.read_csv(op.abspath(filepath.format("2018-FormsGiving.csv")))
    TopCauseFocus_2018 = pd.read_csv(op.abspath(filepath.format("2018-TopCauseFocus_FR.csv")))
    PropTotDon_2018 = pd.read_csv(op.abspath(filepath.format("2018-PercTotDonors-updated_FR.csv")))
    # PropTotDon_2018 = pd.read_csv('tables/2018-PercTotDonors-updated.csv', encoding = 'unicode_escape', engine ='python')
    PropTotDonAmt_2018 = pd.read_csv(op.abspath(filepath.format("2018-PercTotDonations_FR.csv")))

    # Format donation rates as percentage
    DonRates_2018['Estimate'] = DonRates_2018['Estimate']*100
    DonRates_2018['CI Upper'] = DonRates_2018['CI Upper']*100
    FormsGiving_2018['Estimate'] = FormsGiving_2018['Estimate']*100
    FormsGiving_2018['CI Upper'] = FormsGiving_2018['CI Upper']*100
    TopCauseFocus_2018['Estimate'] = TopCauseFocus_2018['Estimate']*100
    TopCauseFocus_2018['CI Upper'] = TopCauseFocus_2018['CI Upper']*100
    PropTotDon_2018['Estimate'] = PropTotDon_2018['Estimate']*100
    PropTotDon_2018['CI Upper'] = PropTotDon_2018['CI Upper']*100
    PropTotDonAmt_2018['Estimate'] = PropTotDonAmt_2018['Estimate']*100
    PropTotDonAmt_2018['CI Upper'] = PropTotDonAmt_2018['CI Upper']*100

    # return DonRates_2018, AvgTotDon_2018, AvgNumCauses_2018, FormsGiving_2018, TopCauseFocus_2018, PropTotDon_2018, PropTotDonAmt_2018
    return DonRates_2018, AvgTotDon_2018, AvgNumCauses_2018, FormsGiving_2018, TopCauseFocus_2018, PropTotDon_2018, PropTotDonAmt_2018


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

def get_region_values():
    return np.array(['CA', 'BC', 'AB', 'PR', 'SK', 'MB', 'ON', 'QC', 'AT', 'NB', 'NS', 'PE', 'NL'], dtype=object)
