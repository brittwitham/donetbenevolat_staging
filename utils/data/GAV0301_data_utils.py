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
    SubSecAvgHrs_2018 = pd.read_csv(op.abspath(filepath.format("2018-SubSecAvgHrs_FR.csv")))
    SubSecVolRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-SubSecVolRates_FR.csv")))
    HealthDonorsBarriers_2018 = pd.read_csv(op.abspath(filepath.format("2018-HealthDonorsBarriers_FR.csv")))
    HealthDonorsDonMeth_2018 = pd.read_csv(op.abspath(filepath.format("2018-HealthDonorsDonMeth_FR.csv")))
    HealthDonorsDonRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-HealthDonorsDonRates_FR.csv")))
    HealthDonorsMotivations_2018 = pd.read_csv(op.abspath(filepath.format("2018-HealthDonorsMotivations_FR.csv")))
    HealthVolsActivities_2018 = pd.read_csv(op.abspath(filepath.format("2018-HealthVolsActivities_FR.csv")))
    HealthVolsBarriers_2018 = pd.read_csv(op.abspath(filepath.format("2018-HealthVolsBarriers_FR.csv")))
    HealthVolsMotivations_2018 = pd.read_csv(op.abspath(filepath.format("2018-HealthVolsReasons_FR.csv")))
    HealthVolsVolRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-HealthVolsVolRates.csv")))

    SubSecDonRates_2018['Estimate'] = SubSecDonRates_2018['Estimate']*100
    SubSecDonRates_2018['CI Upper'] = SubSecDonRates_2018['CI Upper']*100
    SubSecVolRates_2018['Estimate'] = SubSecVolRates_2018['Estimate']*100
    SubSecVolRates_2018['CI Upper'] = SubSecVolRates_2018['CI Upper']*100
    HealthDonorsBarriers_2018['Estimate'] = HealthDonorsBarriers_2018['Estimate']*100
    HealthDonorsBarriers_2018['CI Upper'] = HealthDonorsBarriers_2018['CI Upper']*100
    HealthDonorsDonMeth_2018['Estimate'] = HealthDonorsDonMeth_2018['Estimate']*100
    HealthDonorsDonMeth_2018['CI Upper'] = HealthDonorsDonMeth_2018['CI Upper']*100
    HealthDonorsDonRates_2018['Estimate'] = HealthDonorsDonRates_2018['Estimate']*100
    HealthDonorsDonRates_2018['CI Upper'] = HealthDonorsDonRates_2018['CI Upper']*100
    HealthDonorsMotivations_2018['Estimate'] = HealthDonorsMotivations_2018['Estimate']*100
    HealthDonorsMotivations_2018['CI Upper'] = HealthDonorsMotivations_2018['CI Upper']*100
    HealthVolsActivities_2018['Estimate'] = HealthVolsActivities_2018['Estimate']*100
    HealthVolsActivities_2018['CI Upper'] = HealthVolsActivities_2018['CI Upper']*100
    HealthVolsBarriers_2018['Estimate'] = HealthVolsBarriers_2018['Estimate']*100
    HealthVolsBarriers_2018['CI Upper'] = HealthVolsBarriers_2018['CI Upper']*100
    HealthVolsMotivations_2018['Estimate'] = HealthVolsMotivations_2018['Estimate']*100
    HealthVolsMotivations_2018['CI Upper'] = HealthVolsMotivations_2018['CI Upper']*100
    HealthVolsVolRates_2018['Estimate'] = HealthVolsVolRates_2018['Estimate']*100
    HealthVolsVolRates_2018['CI Upper'] = HealthVolsVolRates_2018['CI Upper']*100

    return SubSecAvgDon_2018, SubSecDonRates_2018, SubSecAvgHrs_2018, SubSecVolRates_2018, HealthDonorsBarriers_2018, HealthDonorsDonMeth_2018, HealthDonorsDonRates_2018, HealthDonorsMotivations_2018, HealthVolsActivities_2018, HealthVolsBarriers_2018, HealthVolsMotivations_2018, HealthVolsVolRates_2018

def process_data(data):
    for i in range(len(data)):
        # Suppress Estimate and CI Upper where necessary (for visualizations and error bars)
        data[i]["Estimate"] = np.where(data[i]["Marker"]=="...", 0, data[i]["Estimate"])
        data[i]["CI Upper"] = np.where(data[i]["Marker"]=="...", 0, data[i]["CI Upper"])

        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unable to determine", "", data[i]["Group"])
        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unknown", "", data[i]["Group"])


        data[i]["Attribute"] = data[i]["Attribute"].str.wrap(10)
        data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Health<br>volunteer", "Health volunteer", data[i]["Attribute"])
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Health<br>donors", "Health donors", data[i]["Attribute"])
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Non-health<br>volunteer", "Non-health volunteer", data[i]["Attribute"])
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Non-health<br>donors", "Non-health donors", data[i]["Attribute"])
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Non-health<br>donor", "Non-health donor", data[i]["Attribute"])

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
