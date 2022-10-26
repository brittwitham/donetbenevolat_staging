import pandas as pd
import plotly.graph_objects as go
import numpy as np
import os
import os.path as op

def get_data():
    filepath = op.join(os.getcwd(), "tables","{}")
    
    SubSecAvgDon_2018 = pd.read_csv(op.abspath(filepath.format("2018-SubSecAvgDon.csv")))
    SubSecDonRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-SubSecDonRates.csv")))
    SubSecAvgHrs_2018 = pd.read_csv(op.abspath(filepath.format("2018-SubSecAvgHrs.csv")))
    SubSecVolRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-SubSecVolRates.csv")))
    EducDonorsBarriers_2018 = pd.read_csv(op.abspath(filepath.format("2018-EducDonorsBarriers.csv")))
    EducDonorsDonMeth_2018 = pd.read_csv(op.abspath(filepath.format("2018-EducDonorsDonMeth.csv")))
    EducDonorsDonRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-EducDonorsDonRates.csv")))
    EducDonorsMotivations_2018 = pd.read_csv(op.abspath(filepath.format("2018-EducDonorsMotivations.csv")))
    EducVolsActivities_2018 = pd.read_csv(op.abspath(filepath.format("2018-EducVolsActivities.csv")))
    EducVolsBarriers_2018 = pd.read_csv(op.abspath(filepath.format("2018-EducVolsBarriers.csv")))
    EducVolsMotivations_2018 = pd.read_csv(op.abspath(filepath.format("2018-EducVolsReasons.csv")))
    EducVolsVolRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-EducVolsVolRates.csv")))

    SubSecDonRates_2018['Estimate'] = SubSecDonRates_2018['Estimate']*100
    SubSecDonRates_2018['CI Upper'] = SubSecDonRates_2018['CI Upper']*100
    SubSecVolRates_2018['Estimate'] = SubSecVolRates_2018['Estimate']*100
    SubSecVolRates_2018['CI Upper'] = SubSecVolRates_2018['CI Upper']*100
    EducDonorsBarriers_2018['Estimate'] = EducDonorsBarriers_2018['Estimate']*100
    EducDonorsBarriers_2018['CI Upper'] = EducDonorsBarriers_2018['CI Upper']*100
    EducDonorsDonMeth_2018['Estimate'] = EducDonorsDonMeth_2018['Estimate']*100
    EducDonorsDonMeth_2018['CI Upper'] = EducDonorsDonMeth_2018['CI Upper']*100
    EducDonorsDonRates_2018['Estimate'] = EducDonorsDonRates_2018['Estimate']*100
    EducDonorsDonRates_2018['CI Upper'] = EducDonorsDonRates_2018['CI Upper']*100
    EducDonorsMotivations_2018['Estimate'] = EducDonorsMotivations_2018['Estimate']*100
    EducDonorsMotivations_2018['CI Upper'] = EducDonorsMotivations_2018['CI Upper']*100
    EducVolsActivities_2018['Estimate'] = EducVolsActivities_2018['Estimate']*100
    EducVolsActivities_2018['CI Upper'] = EducVolsActivities_2018['CI Upper']*100
    EducVolsBarriers_2018['Estimate'] = EducVolsBarriers_2018['Estimate']*100
    EducVolsBarriers_2018['CI Upper'] = EducVolsBarriers_2018['CI Upper']*100
    EducVolsMotivations_2018['Estimate'] = EducVolsMotivations_2018['Estimate']*100
    EducVolsMotivations_2018['CI Upper'] = EducVolsMotivations_2018['CI Upper']*100
    EducVolsVolRates_2018['Estimate'] = EducVolsVolRates_2018['Estimate']*100
    EducVolsVolRates_2018['CI Upper'] = EducVolsVolRates_2018['CI Upper']*100

    return SubSecAvgDon_2018, SubSecDonRates_2018, SubSecAvgHrs_2018, SubSecVolRates_2018, EducDonorsBarriers_2018, EducDonorsDonMeth_2018, EducDonorsDonRates_2018, EducDonorsMotivations_2018, EducVolsActivities_2018, EducVolsBarriers_2018, EducVolsMotivations_2018, EducVolsVolRates_2018

def process_data(data):
    for i in range(len(data)):
        # Suppress Estimate and CI Upper where necessary (for visualizations and error bars)
        data[i]["Estimate"] = np.where(data[i]["Marker"]=="...", 0, data[i]["Estimate"])
        data[i]["CI Upper"] = np.where(data[i]["Marker"]=="...", 0, data[i]["CI Upper"])

        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unable to determine", "", data[i]["Group"])
        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unknown", "", data[i]["Group"])

        data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15)
        data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Education and<br>research<br>volunteer", "Education and research volunteer", data[i]["Attribute"])
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Education and<br>research donors", "Education and research donors", data[i]["Attribute"])
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Education and<br>research donor", "Education and research donor", data[i]["Attribute"])
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Non-education<br>and research<br>volunteer", "Non-education and research volunteer", data[i]["Attribute"])
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Non-education<br>and research<br>donors", "Non-education and research donors", data[i]["Attribute"])
        data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Non-education<br>and research<br>donor", "Non-education and research donor", data[i]["Attribute"])

        data[i]["QuestionText"] = data[i]["QuestionText"].str.wrap(15)
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
