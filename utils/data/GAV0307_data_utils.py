import pandas as pd
import plotly.graph_objects as go
import numpy as np
import os
import os.path as op

def get_data():
    filepath = op.join(os.getcwd(), "tables","{}")
    
    # SubSecAvgDon_2018 = pd.read_csv(op.abspath(filepath.format("2018-SubSecAvgDon.csv")))
    SeniorsAvgDonAmt_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsAvgDonAmt.csv")))
    SeniorsAvgDonByCause_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsAvgDonByCause.csv")))
    SeniorsAvgDonByMeth_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsAvgDonByMeth.csv")))
    SeniorsAvgHrs_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsAvgHrs.csv")))
    SeniorsAvgHrsByActivity_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsAvgHrsByActivity.csv")))
    SeniorsAvgHrsByCause_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsAvgHrsByCause.csv")))
    SeniorsAvgHrsCommInvolve_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsAvgHrsCommInvolve.csv")))
    SeniorsAvgHrsHelpDirectly_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsAvgHrsHelpDirectly.csv")))
    SeniorsBarriers_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsBarriersGiving.csv")))
    SeniorsBarriersVol_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsBarriersVol.csv")))
    SeniorsCommInvolveRate_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsCommInvolveRate.csv")))
    SeniorsDonRateByCause_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsDonRateByCause.csv")))
    SeniorsDonRateByMeth_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsDonRateByMeth.csv")))
    SeniorsDonRates_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsDonRates.csv")))
    SeniorsEfficiencyConcerns_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsEfficiencyConcerns.csv")))
    SeniorsHelpDirectlyRate_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsHelpDirectlyRate.csv")))
    SeniorsReasonsGiving_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsReasonsGiving.csv")))
    SeniorsReasonsVol_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsReasonsVol.csv")))
    SeniorsSolicitationConcerns_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsSolicitationConcerns.csv")))
    SeniorsVolRateByActivity_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsVolRateByActivity.csv")))
    SeniorsVolRateByCause_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsVolRateByCause.csv")))
    SeniorsVolRate_2018 = pd.read_csv(op.abspath(filepath.format("2018-SeniorsVolRates.csv")))

    return SeniorsAvgDonAmt_2018 ,SeniorsAvgDonByCause_2018 ,SeniorsAvgDonByMeth_2018 ,SeniorsAvgHrs_2018 ,SeniorsAvgHrsByActivity_2018 ,SeniorsAvgHrsByCause_2018 ,SeniorsAvgHrsCommInvolve_2018 ,SeniorsAvgHrsHelpDirectly_2018 ,SeniorsBarriers_2018 ,SeniorsBarriersVol_2018 ,SeniorsCommInvolveRate_2018 ,SeniorsDonRateByCause_2018 ,SeniorsDonRateByMeth_2018 ,SeniorsDonRates_2018 ,SeniorsEfficiencyConcerns_2018 ,SeniorsHelpDirectlyRate_2018 ,SeniorsReasonsGiving_2018 ,SeniorsReasonsVol_2018 ,SeniorsSolicitationConcerns_2018 ,SeniorsVolRateByActivity_2018 ,SeniorsVolRateByCause_2018 ,SeniorsVolRate_2018 

        
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
