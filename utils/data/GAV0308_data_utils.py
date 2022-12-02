import pandas as pd
import plotly.graph_objects as go
import numpy as np
import os
import os.path as op

def get_data():
    filepath = op.join(os.getcwd(), "tables","{}")

    # SubSecAvgDon_2018 = pd.read_csv(op.abspath(filepath.format("2018-SubSecAvgDon.csv")))
    YouthAvgDonAmt_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthAvgDonAmt.csv")))
    YouthAvgDonByCause_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthAvgDonByCause.csv")))
    YouthAvgDonByMeth_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthAvgDonByMeth.csv")))
    YouthAvgHrs_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthAvgHrs.csv")))
    YouthAvgHrsByActivity_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthAvgHrsByActivity.csv")))
    YouthAvgHrsByCause_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthAvgHrsByCause.csv")))
    YouthAvgHrsCommInvolve_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthAvgHrsCommInvolve.csv")))
    YouthAvgHrsHelpDirectly_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthAvgHrsHelpDirectly.csv")))
    YouthBarriers_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthBarriersGiving.csv")))
    YouthBarriersVol_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthBarriersVol.csv")))
    YouthCommInvolveRate_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthCommInvolveRate.csv")))
    YouthDonRateByCause_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthDonRateByCause.csv")))
    YouthDonRateByMeth_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthDonRateByMeth.csv")))
    YouthDonRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthDonRates.csv")))
    YouthEfficiencyConcerns_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthEfficiencyConcerns.csv")))
    YouthHelpDirectlyRate_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthHelpDirectlyRate.csv")))
    YouthReasonsGiving_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthReasonsGiving.csv")))
    YouthReasonsVol_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthReasonsVol.csv")))
    YouthSolicitationConcerns_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthSolicitationConcerns.csv")))
    YouthVolRateByActivity_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthVolRateByActivity.csv")))
    YouthVolRateByCause_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthVolRateByCause.csv")))
    YouthVolRate_2018 = pd.read_csv(op.abspath(filepath.format("2018-YouthVolRates.csv")))

    return YouthAvgDonAmt_2018 ,YouthAvgDonByCause_2018 ,YouthAvgDonByMeth_2018,YouthAvgHrs_2018 ,YouthAvgHrsByActivity_2018 ,YouthAvgHrsByCause_2018 ,YouthAvgHrsCommInvolve_2018 ,YouthAvgHrsHelpDirectly_2018 ,YouthBarriers_2018,YouthBarriersVol_2018 ,YouthCommInvolveRate_2018 ,YouthDonRateByCause_2018 ,YouthDonRateByMeth_2018 ,YouthDonRates_2018 ,YouthEfficiencyConcerns_2018 ,YouthHelpDirectlyRate_2018 ,YouthReasonsGiving_2018 ,YouthReasonsVol_2018,YouthSolicitationConcerns_2018 ,YouthVolRateByActivity_2018 ,YouthVolRateByCause_2018 , YouthVolRate_2018



def process_data(data):
    for i in range(len(data)):
        data[i]["Estimate"] = np.where(data[i]["Marker"] == "...", 0, data[i]["Estimate"])
        data[i]["CI Upper"] = np.where(data[i]["Marker"] == "...", 0, data[i]["CI Upper"])
        data[i]["Group"] = np.where(data[i]["Attribute"] == "Unable to determine", "", data[i]["Group"])
        data[i]["Group"] = np.where(data[i]["Attribute"] == "Unknown", "", data[i]["Group"])

        data[i]['Estimate'] = data[i]['Estimate'].round(0).astype(int)
        data[i]["CI Upper"] = data[i]["CI Upper"].round(0).astype(int)
        data[i]['cv'] = data[i]['cv'].round(2)

        # if not data[i]["Attribute"].isna().all():
        #     data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15, break_long_words=False)
        #     data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)
        #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Do not support<br>cause", "Do not support cause", data[i]["Attribute"])
        #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Do not report<br>barrier", "Do not report barrier", data[i]["Attribute"])
        #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Report<br>barrier", "Report barrier", data[i]["Attribute"])

        data[i]["QuestionText"] = data[i]["QuestionText"].str.wrap(20, break_long_words=False)
        data[i]["QuestionText"] = data[i]["QuestionText"].replace({'\n': '<br>'}, regex=True)

def process_rates(rates):
    for i in range(len(rates)):
        rates[i]['Estimate'] = rates[i]['Estimate'] * 100
        rates[i]['CI Upper'] = rates[i]['CI Upper'] * 100

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
