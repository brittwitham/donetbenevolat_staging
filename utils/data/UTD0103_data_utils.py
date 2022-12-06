import pandas as pd
import numpy as np
import os
import os.path as op

def get_data():
    filepath = os.path.join(os.getcwd(),"tables","{}")

    TopDonorsMotivations_2018 = pd.read_csv(os.path.abspath(filepath.format("2018-TopDonorsMotivationsForGiving_FR.csv")))
    TopDonorsBarriers_2018 = pd.read_csv(os.path.abspath(filepath.format("2018-TopDonorsBarriersToGiving_FR.csv")))
    TopDonorsPercTotDonations_2018 = pd.read_csv(os.path.abspath(filepath.format("2018-TopDonorsPercTotDonations_FR.csv")))
    TopDonorsPercTotDonors_2018 = pd.read_csv(os.path.abspath(filepath.format("2018-TopDonorsPercTotDonors_FR.csv")))
    TopDonorsDonRates_2018 = pd.read_csv(os.path.abspath(filepath.format("2018-TopDonorsDonRates_FR.csv")))
    TopDonorsDemoLikelihoods = pd.read_csv(os.path.abspath(filepath.format("2018-TopDonorsDemoLikelihoods_FR.csv")))

    TopDonorsMotivations_2018['Estimate'] = TopDonorsMotivations_2018['Estimate']*100
    TopDonorsMotivations_2018['CI Upper'] = TopDonorsMotivations_2018['CI Upper']*100
    TopDonorsBarriers_2018['Estimate'] = TopDonorsBarriers_2018['Estimate']*100
    TopDonorsBarriers_2018['CI Upper'] = TopDonorsBarriers_2018['CI Upper']*100
    TopDonorsPercTotDonations_2018['Estimate'] = TopDonorsPercTotDonations_2018['Estimate']*100
    TopDonorsPercTotDonations_2018['CI Upper'] = TopDonorsPercTotDonations_2018['CI Upper']*100
    TopDonorsPercTotDonors_2018['Estimate'] = TopDonorsPercTotDonors_2018['Estimate']*100
    TopDonorsPercTotDonors_2018['CI Upper'] = TopDonorsPercTotDonors_2018['CI Upper']*100
    TopDonorsDonRates_2018['Estimate'] = TopDonorsDonRates_2018['Estimate']*100
    TopDonorsDonRates_2018['CI Upper'] = TopDonorsDonRates_2018['CI Upper']*100
    TopDonorsDemoLikelihoods['Estimate'] = TopDonorsDemoLikelihoods['Estimate']*100
    TopDonorsDemoLikelihoods['CI Upper'] = TopDonorsDemoLikelihoods['CI Upper']*100

    return TopDonorsMotivations_2018, TopDonorsBarriers_2018, TopDonorsPercTotDonations_2018, TopDonorsPercTotDonors_2018, TopDonorsDonRates_2018, TopDonorsDemoLikelihoods

def process_data(data):
    for i in range(len(data)):
        data[i]["Estimate"] = np.where(data[i]["Marker"]=="...", 0, data[i]["Estimate"])
        data[i]["CI Upper"] = np.where(data[i]["Marker"]=="...", 0, data[i]["CI Upper"])

        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unable to determine", "", data[i]["Group"])
        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unknown", "", data[i]["Group"])

        data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15, break_long_words=False)
        data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)

        data[i]["QuestionText"] = data[i]["QuestionText"].str.wrap(20, break_long_words=False)
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
