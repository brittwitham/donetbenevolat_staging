import pandas as pd
import plotly.graph_objects as go
import numpy as np
import os
import os.path as op

def get_data():
    filepath = op.join(os.getcwd(), "tables","{}")
    
    NewCanadiansAvgDonAmt_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansAvgDonAmt.csv")))
    NewCanadiansAvgDonByCause_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansAvgDonByCause.csv")))
    NewCanadiansAvgDonByMeth_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansAvgDonByMeth.csv")))
    NewCanadiansAvgHrs_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansAvgHrs.csv")))
    NewCanadiansAvgHrsByActivity_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansAvgHrsByActivity.csv")))
    NewCanadiansAvgHrsByCause_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansAvgHrsByCause.csv")))
    NewCanadiansAvgHrsCommInvolve_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansAvgHrsCommInvolve.csv")))
    NewCanadiansAvgHrsHelpDirectly_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansAvgHrsHelpDirectly.csv")))
    NewCanadiansBarriers_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansBarriersGiving.csv")))
    NewCanadiansBarriersVol_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansBarriersVol.csv")))
    NewCanadiansCommInvolveRate_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansCommInvolveRate.csv")))
    NewCanadiansDonRateByCause_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansDonRateByCause.csv")))
    NewCanadiansDonRateByMeth_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansDonRateByMeth.csv")))
    NewCanadiansDonRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansDonRates.csv")))
    NewCanadiansEfficiencyConcerns_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansEfficiencyConcerns.csv")))
    NewCanadiansHelpDirectlyRate_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansHelpDirectlyRate.csv")))
    NewCanadiansReasonsGiving_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansReasonsGiving.csv")))
    NewCanadiansReasonsVol_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansReasonsVol.csv")))
    NewCanadiansSolicitationConcerns_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansSolicitationConcerns.csv")))
    NewCanadiansVolRateByActivity_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansVolRateByActivity.csv")))
    NewCanadiansVolRateByCause_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansVolRateByCause.csv")))
    NewCanadiansVolRate_2018 = pd.read_csv(op.abspath(filepath.format("2018-NewCanadiansVolRates.csv")))

    return NewCanadiansAvgDonAmt_2018 ,NewCanadiansAvgDonByCause_2018 ,NewCanadiansAvgDonByMeth_2018,NewCanadiansAvgHrs_2018 ,NewCanadiansAvgHrsByActivity_2018,NewCanadiansAvgHrsByCause_2018 ,NewCanadiansAvgHrsCommInvolve_2018 ,NewCanadiansAvgHrsHelpDirectly_2018,NewCanadiansBarriers_2018 ,NewCanadiansBarriersVol_2018 ,NewCanadiansCommInvolveRate_2018 ,NewCanadiansDonRateByCause_2018,NewCanadiansDonRateByMeth_2018,NewCanadiansDonRates_2018 ,NewCanadiansEfficiencyConcerns_2018,NewCanadiansHelpDirectlyRate_2018 ,NewCanadiansReasonsGiving_2018 ,NewCanadiansReasonsVol_2018 ,NewCanadiansSolicitationConcerns_2018,NewCanadiansVolRateByActivity_2018 ,NewCanadiansVolRateByCause_2018,NewCanadiansVolRate_2018

        
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
        #     data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15)
        #     data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)
        #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Do not support<br>cause", "Do not support cause", data[i]["Attribute"])
        #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Do not report<br>barrier", "Do not report barrier", data[i]["Attribute"])
        #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Report<br>barrier", "Report barrier", data[i]["Attribute"])

        data[i]["QuestionText"] = data[i]["QuestionText"].str.wrap(20)
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
