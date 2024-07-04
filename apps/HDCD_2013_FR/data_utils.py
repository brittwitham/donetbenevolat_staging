# data_utils.py
import pandas as pd
import numpy as np
import os
import os.path as op

values = ["Use with caution", "Estimate suppressed", ""]


def get_data():
    filepath = op.join(os.getcwd(), "tables", "{}")

    # DonMethAvgDon_2018 = pd.read_csv(op.abspath(filepath.format("2018-DonMethAvgDon.csv")))
    DonMethAvgDon_2013 = pd.read_csv(op.abspath(
        filepath.format("2013-DonMethAvgDon_FR.csv")))
    DonMethDonRates_2013 = pd.read_csv(op.abspath(
        filepath.format("2013-DonMethDonRates_FR.csv")))

    DonMethDonRates_2013['Estimate'] = DonMethDonRates_2013['Estimate'] * 100
    DonMethDonRates_2013['CI Upper'] = DonMethDonRates_2013['CI Upper'] * 100

    return DonMethAvgDon_2013, DonMethDonRates_2013


def process_data(data):
    for i in range(len(data)):
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
        data[i]["Group"] = np.where(
            data[i]["Attribute"] == "Not stated", "", data[i]["Group"])

        data[i]["Attribute"] = data[i]["Attribute"].str.wrap(
            15, break_long_words=False)
        data[i]["Attribute"] = data[i]["Attribute"].replace(
            {'\n': '<br>'}, regex=True)

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
