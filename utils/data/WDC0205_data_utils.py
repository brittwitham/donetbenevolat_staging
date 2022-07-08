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