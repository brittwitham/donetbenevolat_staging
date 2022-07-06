import numpy as np
import pandas as pd
import os
import os.path as op

def get_data():
    filepath = op.join(os.getcwd(), "tables","{}")
        
    VolRate_2018 = pd.read_csv(op.abspath(filepath.format("2018-VolRate.csv")))
    CommInvolveHrs_2018 = pd.read_csv(op.abspath(filepath.format("2018-CommInvolveHrs.csv")))
    CommInvolveRate_2018 = pd.read_csv(op.abspath(filepath.format("2018-CommInvolveRate.csv")))
    HelpDirectHrs_2018 = pd.read_csv(op.abspath(filepath.format("2018-HelpDirectHrs.csv")))
    HelpDirectRate_2018 = pd.read_csv(op.abspath(filepath.format("2018-HelpDirectRate.csv")))
    FormsVolunteering_2018 = pd.read_csv(op.abspath(filepath.format("2018-FormsVolunteering.csv")))

    VolRate_2018['Estimate'] = VolRate_2018['Estimate']*100
    VolRate_2018['CI Upper'] = VolRate_2018['CI Upper']*100
    FormsVolunteering_2018['Estimate'] = FormsVolunteering_2018['Estimate']*100
    FormsVolunteering_2018['CI Upper'] = FormsVolunteering_2018['CI Upper']*100
    CommInvolveRate_2018['Estimate'] = CommInvolveRate_2018['Estimate']*100
    CommInvolveRate_2018['CI Upper'] = CommInvolveRate_2018['CI Upper']*100
    HelpDirectRate_2018['Estimate'] = HelpDirectRate_2018['Estimate']*100
    HelpDirectRate_2018['CI Upper'] = HelpDirectRate_2018['CI Upper']*100

    return VolRate_2018, CommInvolveHrs_2018, CommInvolveRate_2018, HelpDirectHrs_2018, HelpDirectRate_2018, FormsVolunteering_2018

def process_data(data):
    for i in range(len(data)):
        data[i]["Estimate"] = np.where(data[i]["Marker"]=="...", 0, data[i]["Estimate"])
        data[i]["CI Upper"] = np.where(data[i]["Marker"]=="...", 0, data[i]["CI Upper"])

        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unable to determine", "", data[i]["Group"])
        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unknown", "", data[i]["Group"])

        data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15)
        data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)

        data[i]["QuestionText"] = data[i]["QuestionText"].str.wrap(15)
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
