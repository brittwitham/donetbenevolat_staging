import pandas as pd
import plotly.graph_objects as go
import numpy as np
import os
import os.path as op

def get_data():
    filepath = op.join(os.getcwd(), "tables","{}")
    
    BarriersVol_2018 = pd.read_csv(op.abspath(filepath.format("2018-BarriersToVolunteering.csv")))
    SubSecAvgHrs_2018 = pd.read_csv(op.abspath(filepath.format("2018-SubSecAvgHrs.csv")))
    SubSecVolRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-SubSecVolRates.csv")))
    AllocationVol_2018 = pd.read_csv(op.abspath(filepath.format("2018-VolAllocationByCause.csv")))

    SubSecVolRates_2018['Estimate'] = SubSecVolRates_2018['Estimate']*100
    SubSecVolRates_2018['CI Upper'] = SubSecVolRates_2018['CI Upper']*100
    AllocationVol_2018['Estimate'] = AllocationVol_2018['Estimate']*100
    AllocationVol_2018['CI Upper'] = AllocationVol_2018['CI Upper']*100

    return BarriersVol_2018, SubSecAvgHrs_2018, SubSecVolRates_2018, AllocationVol_2018

def process_data(data):
    for i in range(len(data)):
        data[i]["Estimate"] = np.where(data[i]["Marker"]=="...", 0, data[i]["Estimate"])
        data[i]["CI Upper"] = np.where(data[i]["Marker"]=="...", 0, data[i]["CI Upper"])

        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unable to determine", "", data[i]["Group"])
        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unknown", "", data[i]["Group"])

        data[i]["QuestionText"] = data[i]["QuestionText"].str.wrap(15)
        data[i]["QuestionText"] = data[i]["QuestionText"].replace({'\n': '<br>'}, regex=True)

        data[i]['Estimate'] = data[i]['Estimate'].round(0).astype(int)
        data[i]["CI Upper"] = data[i]["CI Upper"].round(0).astype(int)
        data[i]['cv'] = data[i]['cv'].round(2)
    
def get_region_names():
    return np.array(['CA', 'BC', 'AB', 'PR', 'ON', 'QC', 'AT'], dtype=object)

def get_region_values():
    return np.array(['Canada',
                         'British Columbia',
                         'Alberta',
                         'Prairie Provinces (SK, MB)',
                         'Ontario',
                         'Quebec',
                         'Atlantic Provinces (NB, NS, PE, NL)'], dtype=str)