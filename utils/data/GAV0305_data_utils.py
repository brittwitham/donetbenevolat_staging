import pandas as pd
import plotly.graph_objects as go
import numpy as np
import os
import os.path as op

def get_data():
    filepath = op.join(os.getcwd(), "tables","{}")

    # SubSecAvgDon_2018 = pd.read_csv(op.abspath(filepath.format("2018-SubSecAvgDon.csv")))
    SubSecAvgDon_2018 = pd.read_csv(op.abspath(filepath.format("2018-SubSecAvgDon_FR.csv")))
    SubSecDonRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-SubSecDonRates_FR.csv")))
    SubSecAvgHrs_2018 = pd.read_csv(op.abspath(filepath.format("2018-SubSecAvgHrs_FR.csv")))
    SubSecVolRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-SubSecVolRates_FR.csv")))
    ArtRecDonorsBarriers_2018 = pd.read_csv(op.abspath(filepath.format("2018-ArtRecDonorsBarriers_FR.csv")))
    ArtRecDonorsDonMeth_2018 = pd.read_csv(op.abspath(filepath.format("2018-ArtRecDonorsDonMeth_FR.csv")))
    ArtRecDonorsDonRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-ArtRecDonorsDonRates_FR.csv")))
    ArtRecDonorsMotivations_2018 = pd.read_csv(op.abspath(filepath.format("2018-ArtRecDonorsMotivations_FR.csv")))
    ArtRecVolsActivities_2018 = pd.read_csv(op.abspath(filepath.format("2018-ArtRecVolsActivities_FR.csv")))
    ArtRecVolsBarriers_2018 = pd.read_csv(op.abspath(filepath.format("2018-ArtRecVolsBarriers_FR.csv")))
    ArtRecVolsMotivations_2018 = pd.read_csv(op.abspath(filepath.format("2018-ArtRecVolsReasons_FR.csv")))
    ArtRecVolsVolRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-ArtRecVolsVolRates_FR.csv")))

    SubSecDonRates_2018['Estimate'] = SubSecDonRates_2018['Estimate']*100
    SubSecDonRates_2018['CI Upper'] = SubSecDonRates_2018['CI Upper']*100
    SubSecVolRates_2018['Estimate'] = SubSecVolRates_2018['Estimate']*100
    SubSecVolRates_2018['CI Upper'] = SubSecVolRates_2018['CI Upper']*100
    ArtRecDonorsBarriers_2018['Estimate'] = ArtRecDonorsBarriers_2018['Estimate']*100
    ArtRecDonorsBarriers_2018['CI Upper'] = ArtRecDonorsBarriers_2018['CI Upper']*100
    ArtRecDonorsDonMeth_2018['Estimate'] = ArtRecDonorsDonMeth_2018['Estimate']*100
    ArtRecDonorsDonMeth_2018['CI Upper'] = ArtRecDonorsDonMeth_2018['CI Upper']*100
    ArtRecDonorsDonRates_2018['Estimate'] = ArtRecDonorsDonRates_2018['Estimate']*100
    ArtRecDonorsDonRates_2018['CI Upper'] = ArtRecDonorsDonRates_2018['CI Upper']*100
    ArtRecDonorsMotivations_2018['Estimate'] = ArtRecDonorsMotivations_2018['Estimate']*100
    ArtRecDonorsMotivations_2018['CI Upper'] = ArtRecDonorsMotivations_2018['CI Upper']*100
    ArtRecVolsActivities_2018['Estimate'] = ArtRecVolsActivities_2018['Estimate']*100
    ArtRecVolsActivities_2018['CI Upper'] = ArtRecVolsActivities_2018['CI Upper']*100
    ArtRecVolsBarriers_2018['Estimate'] = ArtRecVolsBarriers_2018['Estimate']*100
    ArtRecVolsBarriers_2018['CI Upper'] = ArtRecVolsBarriers_2018['CI Upper']*100
    ArtRecVolsMotivations_2018['Estimate'] = ArtRecVolsMotivations_2018['Estimate']*100
    ArtRecVolsMotivations_2018['CI Upper'] = ArtRecVolsMotivations_2018['CI Upper']*100
    ArtRecVolsVolRates_2018['Estimate'] = ArtRecVolsVolRates_2018['Estimate']*100
    ArtRecVolsVolRates_2018['CI Upper'] = ArtRecVolsVolRates_2018['CI Upper']*100

    return SubSecAvgDon_2018, SubSecDonRates_2018, SubSecAvgHrs_2018, SubSecVolRates_2018, ArtRecDonorsBarriers_2018, ArtRecDonorsDonMeth_2018, ArtRecDonorsDonRates_2018, ArtRecDonorsMotivations_2018, ArtRecVolsActivities_2018, ArtRecVolsBarriers_2018, ArtRecVolsMotivations_2018, ArtRecVolsVolRates_2018


def process_data(data):
    for i in range(len(data)):
        # Suppress Estimate and CI Upper where necessary (for visualizations and error bars)
        data[i]["Estimate"] = np.where(data[i]["Marker"]=="...", 0, data[i]["Estimate"])
        data[i]["CI Upper"] = np.where(data[i]["Marker"]=="...", 0, data[i]["CI Upper"])

        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unable to determine", "", data[i]["Group"])
        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unknown", "", data[i]["Group"])

        data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15)
        data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Arts and<br>recreation<br>volunteer", "Arts and recreation volunteer", data[i]["Attribute"])
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Arts and<br>recreation<br>donors", "Arts and recreation donors", data[i]["Attribute"])
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Arts and<br>recreation<br>donor", "Arts and recreation donor", data[i]["Attribute"])
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Non-arts and<br>recreation<br>volunteer", "Non-arts and recreation volunteer", data[i]["Attribute"])
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Non-arts and<br>recreation<br>donors", "Non-arts and recreation donors", data[i]["Attribute"])
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Non-arts and<br>recreation<br>donor", "Non-arts and recreation donor", data[i]["Attribute"])

        data[i]["QuestionText"] = data[i]["QuestionText"].str.wrap(35)
        data[i]["QuestionText"] = data[i]["QuestionText"].replace({'\n': '<br>'}, regex=True)

        # Round rates and dollar amounts to zero decimal places
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
