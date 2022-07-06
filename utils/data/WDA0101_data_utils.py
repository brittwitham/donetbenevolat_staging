# data_utils.py
import pandas as pd
import numpy as np
import glob
import os.path as op
import os

values = ["Use with caution", "Estimate suppressed", ""]

def process_data(data):
    for i in range(len(data)):
        # Suppress Estimate and CI Upper where necessary (for visualizations and error bars)
        data[i]["Estimate"] = np.where(data[i]["Marker"]=="...", 0, data[i]["Estimate"])
        data[i]["CI Upper"] = np.where(data[i]["Marker"]=="...", 0, data[i]["CI Upper"])

        data[i]["Region"] = np.select([data[i]["Province"] == "SK",
                                    data[i]["Province"] == "MB",
                                    data[i]["Province"] == "NB",
                                    data[i]["Province"] == "NS",
                                    data[i]["Province"] == "PE",
                                    data[i]["Province"] == "NL"],
                                    ["SK", "MB", "NB", "NS", "PE", "NL"], default=data[i]["Region"])

        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unable to determine", "", data[i]["Group"])
        data[i]["Group"] = np.where(data[i]["Attribute"]=="Unknown", "", data[i]["Group"])

        data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15)
        data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)

        # Round rates and dollar amounts to zero decimal places
        data[i]['Estimate'] = data[i]['Estimate'].round(0).astype(int)
        data[i]["CI Upper"] = data[i]["CI Upper"].round(0).astype(int)
        data[i]['cv'] = data[i]['cv'].round(2)


def process_data_num(data_num):
    for i in range(len(data_num)):
        # Suppress Estimate and CI Upper where necessary (for visualizations and error bars)
        data_num[i]["Estimate"] = np.where(data_num[i]["Marker"]=="...", 0, data_num[i]["Estimate"])
        data_num[i]["CI Upper"] = np.where(data_num[i]["Marker"]=="...", 0, data_num[i]["CI Upper"])

        data_num[i]["Region"] = np.select([data_num[i]["Province"] == "SK",
                                        data_num[i]["Province"] == "MB",
                                        data_num[i]["Province"] == "NB",
                                        data_num[i]["Province"] == "NS",
                                        data_num[i]["Province"] == "PE",
                                        data_num[i]["Province"] == "NL"],
                                        ["SK", "MB", "NB", "NS", "PE", "NL"], default=data_num[i]["Region"])

        data_num[i]["Group"] = np.where(data_num[i]["Attribute"]=="Unable to determine", "", data_num[i]["Group"])
        data_num[i]["Group"] = np.where(data_num[i]["Attribute"]=="Unknown", "", data_num[i]["Group"])

        data_num[i]["Attribute"] = data_num[i]["Attribute"].str.wrap(15)
        data_num[i]["Attribute"] = data_num[i]["Attribute"].replace({'\n': '<br>'}, regex=True)

        # Round number amounts to two decimal places
        data_num[i]['Estimate'] = data_num[i]['Estimate'].round(1)
        data_num[i]["CI Upper"] = data_num[i]["CI Upper"].round(1)
        data_num[i]['cv'] = data_num[i]['cv'].round(2)

# TODO: Refactor into functions once working example complete
def get_data():
    filepath = op.join(os.getcwd(),"tables","{}")

    DonRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-DonRate.csv")))
    AvgTotDon_2018 = pd.read_csv(op.abspath(filepath.format("2018-AvgTotDon.csv")))
    AvgNumCauses_2018 = pd.read_csv(op.abspath(filepath.format("2018-AvgNumCauses.csv")))
    FormsGiving_2018 = pd.read_csv(op.abspath(filepath.format("2018-FormsGiving.csv")))
    TopCauseFocus_2018 = pd.read_csv(op.abspath(filepath.format("2018-TopCauseFocus.csv")))
    PropTotDon_2018 = pd.read_csv(op.abspath(filepath.format("2018-PercTotDonors.csv")))
    PropTotDonAmt_2018 = pd.read_csv(op.abspath(filepath.format("2018-PercTotDonations.csv")))

    # Format donation rates as percentage
    DonRates_2018['Estimate'] = DonRates_2018['Estimate']*100
    DonRates_2018['CI Upper'] = DonRates_2018['CI Upper']*100
    FormsGiving_2018['Estimate'] = FormsGiving_2018['Estimate']*100
    FormsGiving_2018['CI Upper'] = FormsGiving_2018['CI Upper']*100
    TopCauseFocus_2018['Estimate'] = TopCauseFocus_2018['Estimate']*100
    TopCauseFocus_2018['CI Upper'] = TopCauseFocus_2018['CI Upper']*100
    PropTotDon_2018['Estimate'] = PropTotDon_2018['Estimate']*100
    PropTotDon_2018['CI Upper'] = PropTotDon_2018['CI Upper']*100
    PropTotDonAmt_2018['Estimate'] = PropTotDonAmt_2018['Estimate']*100
    PropTotDonAmt_2018['CI Upper'] = PropTotDonAmt_2018['CI Upper']*100

    # return DonRates_2018, AvgTotDon_2018, AvgNumCauses_2018, FormsGiving_2018, TopCauseFocus_2018, PropTotDon_2018, PropTotDonAmt_2018
    return DonRates_2018, AvgTotDon_2018, AvgNumCauses_2018, FormsGiving_2018, TopCauseFocus_2018, PropTotDon_2018, PropTotDonAmt_2018

def get_region_names():
    return np.array(['Canada',
                         'British Columbia',
                         'Alberta',
                         'Prairie Provinces (SK, MB)',
                         'Saskatchewan',
                         'Manitoba',
                         'Ontario',
                         'Quebec',
                         'Atlantic Provinces (NB, NS, PE, NL)',
                         'New Brunswick',
                         'Nova Scotia',
                         'Prince Edward Island',
                         'Newfoundland and Labrador'], dtype=str)

def get_region_values():
    return np.array(['CA', 'BC', 'AB', 'PR', 'SK', 'MB', 'ON', 'QC', 'AT', 'NB', 'NS', 'PE', 'NL'], dtype=object)
