import numpy as np
import pandas as pd
import os
import os.path as op

def get_data():
    filepath = op.join(os.getcwd(), "tables","{}")
        
    # DonMethAvgDon_2018 = pd.read_csv(op.abspath(filepath.format("2018-BarriersToGiving.csv")))
    Barriers_2018 = pd.read_csv(op.abspath(filepath.format("2018-BarriersToGiving_FR.csv")))
    AvgAmtBarriers_2018 = pd.read_csv(op.abspath(filepath.format("2018-AvgAmtBarriers_FR.csv")))
    GivingConcerns_2018 = pd.read_csv(op.abspath(filepath.format("2018-GivingConcerns_FR.csv")))
    SolicitationConcerns_2018 = pd.read_csv(op.abspath(filepath.format("2018-SolicitationConcerns_FR.csv")))
    BarriersByCause_2018 = pd.read_csv(op.abspath(filepath.format("2018-BarriersByCause_FR.csv")))

    Barriers_2018['Estimate'] = Barriers_2018['Estimate'] * 100
    Barriers_2018['CI Upper'] = Barriers_2018['CI Upper'] * 100
    GivingConcerns_2018['Estimate'] = GivingConcerns_2018['Estimate'] * 100
    GivingConcerns_2018['CI Upper'] = GivingConcerns_2018['CI Upper'] * 100
    SolicitationConcerns_2018['Estimate'] = SolicitationConcerns_2018['Estimate'] * 100
    SolicitationConcerns_2018['CI Upper'] = SolicitationConcerns_2018['CI Upper'] * 100
    BarriersByCause_2018['Estimate'] = BarriersByCause_2018['Estimate'] * 100
    BarriersByCause_2018['CI Upper'] = BarriersByCause_2018['CI Upper'] * 100

    return Barriers_2018, AvgAmtBarriers_2018, GivingConcerns_2018, SolicitationConcerns_2018, BarriersByCause_2018 

def process_data(data):
    for i in range(len(data)):
        data[i]["Estimate"] = np.where(data[i]["Marker"] == "...", 0, data[i]["Estimate"])
        data[i]["CI Upper"] = np.where(data[i]["Marker"] == "...", 0, data[i]["CI Upper"])

        data[i]["Group"] = np.where(data[i]["Attribute"] == "Unable to determine", "", data[i]["Group"])
        data[i]["Group"] = np.where(data[i]["Attribute"] == "Unknown", "", data[i]["Group"])

        if not data[i]["Attribute"].isna().all():
            data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15)
            data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)
            data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Do not support<br>cause", "Do not support cause", data[i]["Attribute"])
            data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Do not report<br>barrier", "Do not report barrier", data[i]["Attribute"])
            data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Report<br>barrier", "Report barrier", data[i]["Attribute"])

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