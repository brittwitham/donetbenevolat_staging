import numpy as np
import pandas as pd
import os
import os.path as op

def get_data():
    filepath = op.join(os.getcwd(), "tables","{}")
        
    TopVolsMotivations_2018 = pd.read_csv(op.abspath(filepath.format("2018-TopVolunteersMotivationsForVolunteering_FR.csv")))
    TopVolsBarriers_2018 = pd.read_csv(op.abspath(filepath.format("2018-TopVolsBarriersToVolunteering_FR.csv")))
    TopVolsPercTotHours_2018 = pd.read_csv(op.abspath(filepath.format("2018-TopVolsPercTotHours-updated.csv")))
    TopVolsPercTotVols_2018 = pd.read_csv(op.abspath(filepath.format("2018-TopVolsPercTotVols-updated.csv")))
    TopVolsVolRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-TopVolsVolRates_FR.csv")))
    TopVolsDemoLikelihoods = pd.read_csv(op.abspath(filepath.format("2018-TopVolsDemoLikelihoods_FR.csv")))


    TopVolsMotivations_2018['Estimate'] = TopVolsMotivations_2018['Estimate'] * 100
    TopVolsMotivations_2018['CI Upper'] = TopVolsMotivations_2018['CI Upper'] * 100
    TopVolsBarriers_2018['Estimate'] = TopVolsBarriers_2018['Estimate'] * 100
    TopVolsBarriers_2018['CI Upper'] = TopVolsBarriers_2018['CI Upper'] * 100
    TopVolsPercTotHours_2018['Estimate'] = TopVolsPercTotHours_2018['Estimate'] * 100
    TopVolsPercTotHours_2018['CI Upper'] = TopVolsPercTotHours_2018['CI Upper'] * 100
    TopVolsPercTotVols_2018['Estimate'] = TopVolsPercTotVols_2018['Estimate'] * 100
    TopVolsPercTotVols_2018['CI Upper'] = TopVolsPercTotVols_2018['CI Upper'] * 100
    TopVolsVolRates_2018['Estimate'] = TopVolsVolRates_2018['Estimate'] * 100
    TopVolsVolRates_2018['CI Upper'] = TopVolsVolRates_2018['CI Upper'] * 100
    TopVolsDemoLikelihoods['Estimate'] = TopVolsDemoLikelihoods['Estimate'] * 100
    TopVolsDemoLikelihoods['CI Upper'] = TopVolsDemoLikelihoods['CI Upper'] * 100

    return TopVolsMotivations_2018, TopVolsBarriers_2018, TopVolsPercTotHours_2018, TopVolsPercTotVols_2018, TopVolsVolRates_2018, TopVolsDemoLikelihoods

def process_data(data):
    for i in range(len(data)):
        data[i]["Estimate"] = np.where(data[i]["Marker"] == "...", 0, data[i]["Estimate"])
        data[i]["CI Upper"] = np.where(data[i]["Marker"] == "...", 0, data[i]["CI Upper"])

        data[i]["Group"] = np.where(data[i]["Attribute"] == "Unable to determine", "", data[i]["Group"])
        data[i]["Group"] = np.where(data[i]["Attribute"] == "Unknown", "", data[i]["Group"])

        data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15)
        data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Regular<br>volunteer", "Regular volunteer", data[i]["Attribute"])

        data[i]["QuestionText"] = data[i]["QuestionText"].str.wrap(20)
        data[i]["QuestionText"] = data[i]["QuestionText"].replace({'\n': '<br>'}, regex=True)

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