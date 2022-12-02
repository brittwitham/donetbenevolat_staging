
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import os
import os.path as op

def get_data():
    filepath = op.join(os.getcwd(), "tables","{}")

    BarriersVol_2018 = pd.read_csv(op.abspath(filepath.format("2013-BarriersToVolunteering_FR.csv")))
    # BarriersVolMore_2018 = pd.read_csv(op.abspath(filepath.format("2013-BarriersToVolunteeringMore_FR.csv")))
    BarriersVolMore_20188 = pd.read_csv('tables/2013-BarriersToVolunteeringMore-updated_fr.csv', encoding = 'unicode_escape', engine ='python')
    BarriersVolMore_2018 = pd.read_csv('tables/2013-BarriersToVolunteeringMore-updated_fr.csv')
    AvgHoursBarriersVol_2018 = pd.read_csv(op.abspath(filepath.format("2013-AvgHoursBarriers_FR.csv")))
    BarriersVolByCause_2018 = pd.read_csv(op.abspath(filepath.format("2013-BarriersVolByCause_FR.csv")))

    BarriersVol_2018['Estimate'] = BarriersVol_2018['Estimate'] * 100
    BarriersVol_2018['CI Upper'] = BarriersVol_2018['CI Upper'] * 100
    BarriersVolMore_2018['Estimate'] = BarriersVolMore_2018['Estimate'] * 100
    BarriersVolMore_2018['CI Upper'] = BarriersVolMore_2018['CI Upper'] * 100
    BarriersVolMore_20188['Estimate'] = BarriersVolMore_20188['Estimate'] * 100
    BarriersVolMore_20188['CI Upper'] = BarriersVolMore_20188['CI Upper'] * 100
    BarriersVolByCause_2018['Estimate'] = BarriersVolByCause_2018['Estimate'] * 100
    BarriersVolByCause_2018['CI Upper'] = BarriersVolByCause_2018['CI Upper'] * 100

    return BarriersVol_2018, BarriersVolMore_2018, AvgHoursBarriersVol_2018, BarriersVolByCause_2018, BarriersVolMore_20188

def process_data(data):
    for i in range(len(data)):
        data[i]["Estimate"] = np.where(data[i]["Marker"] == "...", 0, data[i]["Estimate"])
        data[i]["CI Upper"] = np.where(data[i]["Marker"] == "...", 0, data[i]["CI Upper"])

        data[i]["Group"] = np.where(data[i]["Attribute"] == "Unable to determine", "", data[i]["Group"])
        data[i]["Group"] = np.where(data[i]["Attribute"] == "Unknown", "", data[i]["Group"])

        # if not data[i]["Attribute"].isna().all():
        #     data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15, break_long_words=False)
        #     data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)
        #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Do not support<br>cause", "Do not support cause", data[i]["Attribute"])
        #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Do not report<br>barrier", "Do not report barrier", data[i]["Attribute"])
        #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Report<br>barrier", "Report barrier", data[i]["Attribute"])

        # data[i]["QuestionText"] = data[i]["QuestionText"].str.wrap(20, break_long_words=False)
        # data[i]["QuestionText"] = data[i]["QuestionText"].replace({'\n': '<br>'}, regex=True)

        # data[i]['Estimate'] = data[i]['Estimate'].round(0).astype(int)
        # data[i]["CI Upper"] = data[i]["CI Upper"].round(0).astype(int)
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
