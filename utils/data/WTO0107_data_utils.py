import pandas as pd
import plotly.graph_objects as go
import numpy as np
import os
import os.path as op

def get_data():
    filepath = op.join(os.getcwd(), "tables","{}")
    
    # DonMethAvgDon_2018 = pd.read_csv(op.abspath(filepath.format("2018-DonMethAvgDon.csv")))
    SubSecAvgDon_2018 = pd.read_csv(op.abspath(filepath.format("2018-SubSecAvgDon_FR.csv")))
    SubSecDonRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-SubSecDonRates_FR.csv")))
    Allocation_2018 = pd.read_csv(op.abspath(filepath.format("2018-AllocationByCause_FR.csv")))

    SubSecDonRates_2018['Estimate'] = SubSecDonRates_2018['Estimate']*100
    SubSecDonRates_2018['CI Upper'] = SubSecDonRates_2018['CI Upper']*100
    Allocation_2018['Estimate'] = Allocation_2018['Estimate']*100
    Allocation_2018['CI Upper'] = Allocation_2018['CI Upper']*100

    return SubSecAvgDon_2018, SubSecDonRates_2018, Allocation_2018

def process_data(data):
    for i in range(len(data)):
        data[i]["Estimate"] = np.where(data[i]["Marker"]=="...", 0, data[i]["Estimate"])
        data[i]["CI Upper"] = np.where(data[i]["Marker"]=="...", 0, data[i]["CI Upper"])

        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unable to determine", "", data[i]["Group"])
        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unknown", "", data[i]["Group"])

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
