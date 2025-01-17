import pandas as pd
import plotly.graph_objects as go
import numpy as np
import os
import os.path as op


def get_data():
    filepath = op.join(os.getcwd(), "tables", "{}")

    empGrowth = pd.read_csv(op.abspath(filepath.format("empGrowth.csv")))
    empSubSec = pd.read_csv(
        op.abspath(
            filepath.format("tables/empSubSec.csv")))
    empSubSecActivity = pd.read_csv(op.abspath(
        filepath.format("tables/empSubSecActivity.csv")))
    empGrowthActivity = pd.read_csv(op.abspath(
        filepath.format("tables/empGrowthActivity.csv")))

    return empGrowth, empSubSec, empSubSecActivity, empGrowthActivity


# def process_data(data):
#     for i in range(len(data)):
#         data[i]["Estimate"] = np.where(
#             data[i]["Marker"] == "...", 0, data[i]["Estimate"])
#         data[i]["CI Upper"] = np.where(
#             data[i]["Marker"] == "...", 0, data[i]["CI Upper"])

#         data[i]["Region"] = np.select([data[i]["Province"] == "SK",
#                                        data[i]["Province"] == "MB",
#                                        data[i]["Province"] == "NB",
#                                        data[i]["Province"] == "NS",
#                                        data[i]["Province"] == "PE",
#                                        data[i]["Province"] == "NL"],
#                                       ["SK", "MB", "NB", "NS", "PE", "NL"], default=data[i]["Region"])

#         data[i]["Group"] = np.where(
#             data[i]["Attribute"] == "Unable to determine",
#             "",
#             data[i]["Group"])
#         data[i]["Group"] = np.where(
#             data[i]["Attribute"] == "Unknown", "", data[i]["Group"])

#         data[i]["Attribute"] = data[i]["Attribute"].str.wrap(
#             15, break_long_words=False)
#         data[i]["Attribute"] = data[i]["Attribute"].replace(
#             {'\n': '<br>'}, regex=True)

#         data[i]['Estimate'] = data[i]['Estimate'].round(0).astype(int)
#         data[i]["CI Upper"] = data[i]["CI Upper"].round(0).astype(int)
#         data[i]['cv'] = data[i]['cv'].round(2)

#     return data


# def get_region_values():
#     return np.array(['CA', 'BC', 'AB', 'PR', 'SK', 'MB', 'ON',
#                     'QC', 'AT', 'NB', 'NS', 'PE', 'NL'], dtype=object)


# def get_region_names():
#     return np.array(['Canada',
#                      'British Columbia',
#                      'Alberta',
#                      'Prairie Provinces (SK, MB)',
#                      'Saskatchewan',
#                      'Manitoba',
#                      'Ontario',
#                      'Quebec',
#                      'Atlantic Provinces (NB, NS, PE, NL)',
#                      'New Brunswick',
#                      'Nova Scotia',
#                      'Prince Edward Island',
#                      'Newfoundland and Labrador'], dtype=str)
