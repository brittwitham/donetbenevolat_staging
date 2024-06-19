# Raw copy-paste file for GV_SE_2018_FR converted from GAV0307_fr.py
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import os
import os.path as op


def get_dataframe(csv_name):
    filepath = op.join(os.getcwd(), "tables", "{}")
    df = pd.read_csv(op.abspath(filepath.format(csv_name)))
    return df


SeniorsAvgDonAmt_2018 = get_dataframe("2018-SeniorsAvgDonAmt_FR.csv")
SeniorsAvgDonByCause_2018 = get_dataframe("2018-SeniorsAvgDonByCause_FR.csv")
SeniorsAvgDonByMeth_2018 = get_dataframe("2018-SeniorsAvgDonByMeth_FR.csv")
SeniorsAvgHrs_2018 = get_dataframe("2018-SeniorsAvgHrs_FR.csv")
SeniorsAvgHrsByActivity_2018 = get_dataframe(
    "2018-SeniorsAvgHrsByActivity_FR.csv")
SeniorsAvgHrsByCause_2018 = get_dataframe("2018-SeniorsAvgHrsByCause_FR.csv")
SeniorsAvgHrsCommInvolve_2018 = get_dataframe(
    "2018-SeniorsAvgHrsCommInvolve_FR.csv")
SeniorsAvgHrsHelpDirectly_2018 = get_dataframe(
    "2018-SeniorsAvgHrsHelpDirectly_FR.csv")
SeniorsBarriers_2018 = get_dataframe("2018-SeniorsBarriersGiving_FR.csv")
SeniorsBarriersVol_2018 = get_dataframe("2018-SeniorsBarriersVol_FR.csv")
SeniorsCommInvolveRate_2018 = get_dataframe(
    "2018-SeniorsCommInvolveRate_FR.csv")
SeniorsDonRateByCause_2018 = get_dataframe("2018-SeniorsDonRateByCause_FR.csv")
SeniorsDonRateByMeth_2018 = get_dataframe("2018-SeniorsDonRateByMeth_FR.csv")
SeniorsDonRates_2018 = get_dataframe("2018-SeniorsDonRates_FR.csv")
SeniorsEfficiencyConcerns_2018 = get_dataframe(
    "2018-SeniorsEfficiencyConcerns_FR.csv")
SeniorsHelpDirectlyRate_2018 = get_dataframe(
    "2018-SeniorsHelpDirectlyRate_FR.csv")
SeniorsReasonsGiving_2018 = get_dataframe("2018-SeniorsReasonsGiving_FR.csv")
SeniorsReasonsVol_2018 = get_dataframe("2018-SeniorsReasonsVol_FR.csv")
SeniorsSolicitationConcerns_2018 = get_dataframe(
    "2018-SeniorsSolicitationConcerns_FR.csv")
SeniorsVolRateByActivity_2018 = get_dataframe(
    "2018-SeniorsVolRateByActivity_FR.csv")
SeniorsVolRateByCause_2018 = get_dataframe("2018-SeniorsVolRateByCause_FR.csv")
SeniorsVolRate_2018 = get_dataframe("2018-SeniorsVolRates_FR.csv")

rates = [SeniorsBarriers_2018,
         SeniorsBarriersVol_2018,
         SeniorsCommInvolveRate_2018,
         SeniorsDonRateByCause_2018,
         SeniorsDonRateByMeth_2018,
         SeniorsDonRates_2018,
         SeniorsEfficiencyConcerns_2018,
         SeniorsHelpDirectlyRate_2018,
         SeniorsReasonsGiving_2018,
         SeniorsReasonsVol_2018,
         SeniorsSolicitationConcerns_2018,
         SeniorsVolRateByActivity_2018,
         SeniorsVolRateByCause_2018,
         SeniorsVolRate_2018]

data = [SeniorsAvgDonAmt_2018,
        SeniorsAvgDonByCause_2018,
        SeniorsAvgDonByMeth_2018,
        SeniorsAvgHrs_2018,
        SeniorsAvgHrsByActivity_2018,
        SeniorsAvgHrsByCause_2018,
        SeniorsAvgHrsCommInvolve_2018,
        SeniorsAvgHrsHelpDirectly_2018,
        SeniorsBarriers_2018,
        SeniorsBarriersVol_2018,
        SeniorsCommInvolveRate_2018,
        SeniorsDonRateByCause_2018,
        SeniorsDonRateByMeth_2018,
        SeniorsDonRates_2018,
        SeniorsEfficiencyConcerns_2018,
        SeniorsHelpDirectlyRate_2018,
        SeniorsReasonsGiving_2018,
        SeniorsReasonsVol_2018,
        SeniorsSolicitationConcerns_2018,
        SeniorsVolRateByActivity_2018,
        SeniorsVolRateByCause_2018,
        SeniorsVolRate_2018]

for i in range(len(rates)):
    rates[i]['Estimate'] = rates[i]['Estimate'] * 100
    rates[i]['CI Upper'] = rates[i]['CI Upper'] * 100


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
        data[i]["Attribute"] == "Unknown",
        "",
        data[i]["Group"])

    data[i]['Estimate'] = data[i]['Estimate'].round(0).astype(int)
    data[i]["CI Upper"] = data[i]["CI Upper"].round(0).astype(int)
    data[i]['cv'] = data[i]['cv'].round(2)

    # if not data[i]["Attribute"].isna().all():
    #     data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15, break_long_words=False)
    #     data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)
    #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Do not support<br>cause", "Do not support cause", data[i]["Attribute"])
    #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Do not report<br>barrier", "Do not report barrier", data[i]["Attribute"])
    #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Report<br>barrier", "Report barrier", data[i]["Attribute"])

    data[i]["QuestionText"] = data[i]["QuestionText"].str.wrap(
        35, break_long_words=False)
    data[i]["QuestionText"] = data[i]["QuestionText"].replace(
        {'\n': '<br>'}, regex=True)

region_values = np.array(
    ['CA', 'BC', 'AB', 'PR', 'ON', 'QC', 'AT'], dtype=object)
region_names = np.array(['Canada',
                         'British Columbia',
                         'Alberta',
                         'Prairie Provinces (SK, MB)',
                         'Ontario',
                         'Quebec',
                         'Atlantic Provinces (NB, NS, PE, NL)'], dtype=str)
