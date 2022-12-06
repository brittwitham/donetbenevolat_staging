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
    SubSecDonRatesFoc_2018 = pd.read_csv(op.abspath(filepath.format("2018-SubSecDonRates-Focussed_FR.csv")))
    SubSecAvgHrs_2018 = pd.read_csv(op.abspath(filepath.format("2018-SubSecAvgHrs_FR.csv")))
    SubSecVolRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-SubSecVolRates_FR.csv")))
    SubSecVolRatesFoc_2018 = pd.read_csv(op.abspath(filepath.format("2018-SubSecVolRates-Focussed_FR.csv")))
    ReligionDonorsBarriers_2018 = pd.read_csv(op.abspath(filepath.format("2018-ReligionDonorsBarriers_FR.csv")))
    ReligionDonorsDonMeth_2018 = pd.read_csv(op.abspath(filepath.format("2018-ReligionDonorsDonMeth_FR.csv")))
    ReligionDonorsDonRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-ReligionDonorsDonRates_FR.csv")))
    ReligionDonorsMotivations_2018 = pd.read_csv(op.abspath(filepath.format("2018-ReligionDonorsMotivations_FR.csv")))
    ReligionVolsActivities_2018 = pd.read_csv(op.abspath(filepath.format("2018-ReligionVolsActivities_FR.csv")))
    ReligionVolsBarriers_2018 = pd.read_csv(op.abspath(filepath.format("2018-ReligionVolsBarriers_FR.csv")))
    ReligionVolsMotivations_2018 = pd.read_csv(op.abspath(filepath.format("2018-ReligionVolsReasons_FR.csv")))
    ReligionVolsVolRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-ReligionVolsVolRates_FR.csv")))

    SubSecDonRates_2018['Estimate'] = SubSecDonRates_2018['Estimate']*100
    SubSecDonRates_2018['CI Upper'] = SubSecDonRates_2018['CI Upper']*100

    SubSecDonRatesFoc_2018['Estimate'] = SubSecDonRatesFoc_2018['Estimate'] * 100
    SubSecDonRatesFoc_2018['CI Upper'] = SubSecDonRatesFoc_2018['CI Upper'] * 100
    SubSecDonRatesFoc_2018 = SubSecDonRatesFoc_2018[SubSecDonRatesFoc_2018['QuestionText'] == "Religion"]


    SubSecVolRates_2018['Estimate'] = SubSecVolRates_2018['Estimate']*100
    SubSecVolRates_2018['CI Upper'] = SubSecVolRates_2018['CI Upper']*100

    SubSecVolRatesFoc_2018['Estimate'] = SubSecVolRatesFoc_2018['Estimate'] * 100
    SubSecVolRatesFoc_2018['CI Upper'] = SubSecVolRatesFoc_2018['CI Upper'] * 100
    SubSecVolRatesFoc_2018 = SubSecVolRatesFoc_2018[SubSecVolRatesFoc_2018['QuestionText'] == "Religion"]

    ReligionDonorsBarriers_2018['Estimate'] = ReligionDonorsBarriers_2018['Estimate']*100
    ReligionDonorsBarriers_2018['CI Upper'] = ReligionDonorsBarriers_2018['CI Upper']*100
    ReligionDonorsDonMeth_2018['Estimate'] = ReligionDonorsDonMeth_2018['Estimate']*100
    ReligionDonorsDonMeth_2018['CI Upper'] = ReligionDonorsDonMeth_2018['CI Upper']*100
    ReligionDonorsDonRates_2018['Estimate'] = ReligionDonorsDonRates_2018['Estimate']*100
    ReligionDonorsDonRates_2018['CI Upper'] = ReligionDonorsDonRates_2018['CI Upper']*100
    ReligionDonorsMotivations_2018['Estimate'] = ReligionDonorsMotivations_2018['Estimate']*100
    ReligionDonorsMotivations_2018['CI Upper'] = ReligionDonorsMotivations_2018['CI Upper']*100
    ReligionVolsActivities_2018['Estimate'] = ReligionVolsActivities_2018['Estimate']*100
    ReligionVolsActivities_2018['CI Upper'] = ReligionVolsActivities_2018['CI Upper']*100
    ReligionVolsBarriers_2018['Estimate'] = ReligionVolsBarriers_2018['Estimate']*100
    ReligionVolsBarriers_2018['CI Upper'] = ReligionVolsBarriers_2018['CI Upper']*100
    ReligionVolsMotivations_2018['Estimate'] = ReligionVolsMotivations_2018['Estimate']*100
    ReligionVolsMotivations_2018['CI Upper'] = ReligionVolsMotivations_2018['CI Upper']*100
    ReligionVolsVolRates_2018['Estimate'] = ReligionVolsVolRates_2018['Estimate']*100
    ReligionVolsVolRates_2018['CI Upper'] = ReligionVolsVolRates_2018['CI Upper']*100

    return SubSecAvgDon_2018,SubSecDonRates_2018, SubSecDonRatesFoc_2018, SubSecAvgHrs_2018 ,SubSecVolRates_2018, SubSecVolRatesFoc_2018, ReligionDonorsBarriers_2018, ReligionDonorsDonMeth_2018, ReligionDonorsDonRates_2018, ReligionDonorsMotivations_2018, ReligionVolsActivities_2018, ReligionVolsBarriers_2018, ReligionVolsMotivations_2018, ReligionVolsVolRates_2018

def process_data(data):
    for i in range(len(data)):
    # Suppress Estimate and CI Upper where necessary (for visualizations and error bars)
        data[i]["Estimate"] = np.where(data[i]["Marker"]=="...", 0, data[i]["Estimate"])
        data[i]["CI Upper"] = np.where(data[i]["Marker"]=="...", 0, data[i]["CI Upper"])

        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unable to determine", "", data[i]["Group"])
        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unknown", "", data[i]["Group"])

        data[i]["QuestionText"] = data[i]["QuestionText"].str.wrap(35, break_long_words=False)
        data[i]["QuestionText"] = data[i]["QuestionText"].replace({'\n': '<br>'}, regex=True)

        data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15, break_long_words=False)
        data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Religion<br>volunteer", "Religion volunteer", data[i]["Attribute"])
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Non-religion<br>volunteer", "Non-religion volunteer", data[i]["Attribute"])
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Non-religion<br>donors", "Non-religion donors", data[i]["Attribute"])
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Non-religion<br>donor", "Non-religion donor", data[i]["Attribute"])

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
