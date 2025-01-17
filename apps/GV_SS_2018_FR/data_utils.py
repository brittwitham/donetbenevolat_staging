import pandas as pd
import plotly.graph_objects as go
import numpy as np
import os
import os.path as op


def get_data():
    filepath = op.join(os.getcwd(), "tables", "{}")

    SubSecAvgDon_2018 = pd.read_csv(op.abspath(
        filepath.format("2018-SubSecAvgDon_FR.csv")))
    SubSecDonRates_2018 = pd.read_csv(op.abspath(
        filepath.format("2018-SubSecDonRates_FR.csv")))
    SubSecDonRatesFoc_2018 = pd.read_csv(op.abspath(
        filepath.format("2018-SubSecDonRates-Focussed_FR.csv")))
    SubSecAvgHrs_2018 = pd.read_csv(op.abspath(
        filepath.format("2018-SubSecAvgHrs_FR.csv")))
    SubSecVolRates_2018 = pd.read_csv(op.abspath(
        filepath.format("2018-SubSecVolRates_FR.csv")))
    SubSecVolRatesFoc_2018 = pd.read_csv(op.abspath(
        filepath.format("2018-SubSecVolRates-Focussed_FR.csv")))
    SocSerDonorsBarriers_2018 = pd.read_csv(op.abspath(
        filepath.format("2018-SocSerDonorsBarriers_FR.csv")))
    SocSerDonorsDonMeth_2018 = pd.read_csv(op.abspath(
        filepath.format("2018-SocSerDonorsDonMeth_FR.csv")))
    SocSerDonorsDonRates_2018 = pd.read_csv(op.abspath(
        filepath.format("2018-SocSerDonorsDonRates_FR.csv")))
    SocSerDonorsMotivations_2018 = pd.read_csv(op.abspath(
        filepath.format("2018-SocSerDonorsMotivations_FR.csv")))
    SocSerVolsActivities_2018 = pd.read_csv(op.abspath(
        filepath.format("2018-SocSerVolsActivities_FR.csv")))
    SocSerVolsBarriers_2018 = pd.read_csv(op.abspath(
        filepath.format("2018-SocSerVolsBarriers_FR.csv")))
    SocSerVolsMotivations_2018 = pd.read_csv(op.abspath(
        filepath.format("2018-SocSerVolsReasons_FR.csv")))
    SocSerVolsVolRates_2018 = pd.read_csv(op.abspath(
        filepath.format("2018-SocSerVolsVolRates_FR.csv")))

    SubSecDonRates_2018['Estimate'] = SubSecDonRates_2018['Estimate'] * 100
    SubSecDonRates_2018['CI Upper'] = SubSecDonRates_2018['CI Upper'] * 100

    SubSecDonRatesFoc_2018['Estimate'] = SubSecDonRatesFoc_2018['Estimate'] * 100
    SubSecDonRatesFoc_2018['CI Upper'] = SubSecDonRatesFoc_2018['CI Upper'] * 100
    SubSecDonRatesFoc_2018 = SubSecDonRatesFoc_2018[
        SubSecDonRatesFoc_2018['QuestionText'] == "Social services"]

    SubSecVolRates_2018['Estimate'] = SubSecVolRates_2018['Estimate'] * 100
    SubSecVolRates_2018['CI Upper'] = SubSecVolRates_2018['CI Upper'] * 100

    SubSecVolRatesFoc_2018['Estimate'] = SubSecVolRatesFoc_2018['Estimate'] * 100
    SubSecVolRatesFoc_2018['CI Upper'] = SubSecVolRatesFoc_2018['CI Upper'] * 100
    SubSecVolRatesFoc_2018 = SubSecVolRatesFoc_2018[
        SubSecVolRatesFoc_2018['QuestionText'] == "Social services"]

    SocSerDonorsBarriers_2018['Estimate'] = SocSerDonorsBarriers_2018['Estimate'] * 100
    SocSerDonorsBarriers_2018['CI Upper'] = SocSerDonorsBarriers_2018['CI Upper'] * 100
    SocSerDonorsDonMeth_2018['Estimate'] = SocSerDonorsDonMeth_2018['Estimate'] * 100
    SocSerDonorsDonMeth_2018['CI Upper'] = SocSerDonorsDonMeth_2018['CI Upper'] * 100
    SocSerDonorsDonRates_2018['Estimate'] = SocSerDonorsDonRates_2018['Estimate'] * 100
    SocSerDonorsDonRates_2018['CI Upper'] = SocSerDonorsDonRates_2018['CI Upper'] * 100
    SocSerDonorsMotivations_2018['Estimate'] = SocSerDonorsMotivations_2018['Estimate'] * 100
    SocSerDonorsMotivations_2018['CI Upper'] = SocSerDonorsMotivations_2018['CI Upper'] * 100
    SocSerVolsActivities_2018['Estimate'] = SocSerVolsActivities_2018['Estimate'] * 100
    SocSerVolsActivities_2018['CI Upper'] = SocSerVolsActivities_2018['CI Upper'] * 100
    SocSerVolsBarriers_2018['Estimate'] = SocSerVolsBarriers_2018['Estimate'] * 100
    SocSerVolsBarriers_2018['CI Upper'] = SocSerVolsBarriers_2018['CI Upper'] * 100
    SocSerVolsMotivations_2018['Estimate'] = SocSerVolsMotivations_2018['Estimate'] * 100
    SocSerVolsMotivations_2018['CI Upper'] = SocSerVolsMotivations_2018['CI Upper'] * 100
    SocSerVolsVolRates_2018['Estimate'] = SocSerVolsVolRates_2018['Estimate'] * 100
    SocSerVolsVolRates_2018['CI Upper'] = SocSerVolsVolRates_2018['CI Upper'] * 100

    return SubSecAvgDon_2018, SubSecDonRates_2018, SubSecDonRatesFoc_2018, SubSecAvgHrs_2018, SubSecVolRates_2018, SubSecVolRatesFoc_2018, SocSerDonorsBarriers_2018, SocSerDonorsDonMeth_2018, SocSerDonorsDonRates_2018, SocSerDonorsMotivations_2018, SocSerVolsActivities_2018, SocSerVolsBarriers_2018, SocSerVolsMotivations_2018, SocSerVolsVolRates_2018


def process_data(data):
    for i in range(len(data)):
        # Suppress Estimate and CI Upper where necessary (for visualizations
        # and error bars)
        data[i]["Estimate"] = np.where(
            data[i]["Marker"] == "...", 0, data[i]["Estimate"])
        data[i]["CI Upper"] = np.where(
            data[i]["Marker"] == "...", 0, data[i]["CI Upper"])

        data[i]["Group"] = np.where(
            data[i]["Attribute"] == "Unable to determine",
            "",
            data[i]["Group"])
        data[i]["Group"] = np.where(
            data[i]["Attribute"] == "Unknown", "", data[i]["Group"])

        data[i]["QuestionText"] = data[i]["QuestionText"].str.wrap(
            35, break_long_words=False)
        data[i]["QuestionText"] = data[i]["QuestionText"].replace(
            {'\n': '<br>'}, regex=True)

        # data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15, break_long_words=False)
        # data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)
        # data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Social services<br>volunteer", "Social services volunteer", data[i]["Attribute"])
        # data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Non-social services<br>volunteer", "Non-social services volunteer", data[i]["Attribute"])
        # data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Non-social services<br>donors", "Non-social services donors", data[i]["Attribute"])
        # data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Non-social services<br>donor", "Non-social services donor", data[i]["Attribute"])

        # Round rates and dollar amounts to zero decimal places
        data[i]['Estimate'] = data[i]['Estimate'].round(0).astype(int)
        data[i]["CI Upper"] = data[i]["CI Upper"].round(0).astype(int)
        data[i]['cv'] = data[i]['cv'].round(2)

    return data


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
