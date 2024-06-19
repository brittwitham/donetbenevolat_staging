# Data processing file for GV_YO_2018_FR converted from
# les_dons_et_le_benevolat_des_jeunes_2018.py

from .data_utils import *


YouthAvgDonAmt_2018 = get_dataframe("2018-YouthAvgDonAmt_FR.csv")
YouthAvgDonByCause_2018 = get_dataframe("2018-YouthAvgDonByCause_FR.csv")
YouthAvgDonByMeth_2018 = get_dataframe("2018-YouthAvgDonByMeth_FR.csv")
YouthAvgHrs_2018 = get_dataframe("2018-YouthAvgHrs_FR.csv")
YouthAvgHrsByActivity_2018 = get_dataframe("2018-YouthAvgHrsByActivity_FR.csv")
YouthAvgHrsByCause_2018 = get_dataframe("2018-YouthAvgHrsByCause_FR.csv")
YouthAvgHrsCommInvolve_2018 = get_dataframe(
    "2018-YouthAvgHrsCommInvolve_FR.csv")
YouthAvgHrsHelpDirectly_2018 = get_dataframe(
    "2018-YouthAvgHrsHelpDirectly_FR.csv")
YouthBarriers_2018 = get_dataframe("2018-YouthBarriersGiving_FR.csv")
YouthBarriersVol_2018 = get_dataframe("2018-YouthBarriersVol_FR.csv")
YouthCommInvolveRate_2018 = get_dataframe("2018-YouthCommInvolveRate_FR.csv")
YouthDonRateByCause_2018 = get_dataframe("2018-YouthDonRateByCause_FR.csv")
YouthDonRateByMeth_2018 = get_dataframe("2018-YouthDonRateByMeth_FR.csv")
YouthDonRates_2018 = get_dataframe("2018-YouthDonRates_FR.csv")
YouthEfficiencyConcerns_2018 = get_dataframe(
    "2018-YouthEfficiencyConcerns_FR.csv")
YouthHelpDirectlyRate_2018 = get_dataframe("2018-YouthHelpDirectlyRate_FR.csv")
YouthReasonsGiving_2018 = get_dataframe("2018-YouthReasonsGiving_FR.csv")
YouthReasonsVol_2018 = get_dataframe("2018-YouthReasonsVol_FR.csv")
YouthSolicitationConcerns_2018 = get_dataframe(
    "2018-YouthSolicitationConcerns_FR.csv")
YouthVolRateByActivity_2018 = get_dataframe(
    "2018-YouthVolRateByActivity_FR.csv")
YouthVolRateByCause_2018 = get_dataframe("2018-YouthVolRateByCause_FR.csv")
YouthVolRate_2018 = get_dataframe("2018-YouthVolRates_FR.csv")

rates = [YouthBarriers_2018,
         YouthBarriersVol_2018,
         YouthCommInvolveRate_2018,
         YouthDonRateByCause_2018,
         YouthDonRateByMeth_2018,
         YouthDonRates_2018,
         YouthEfficiencyConcerns_2018,
         YouthHelpDirectlyRate_2018,
         YouthReasonsGiving_2018,
         YouthReasonsVol_2018,
         YouthSolicitationConcerns_2018,
         YouthVolRateByActivity_2018,
         YouthVolRateByCause_2018,
         YouthVolRate_2018]

data = [YouthAvgDonAmt_2018,
        YouthAvgDonByCause_2018,
        YouthAvgDonByMeth_2018,
        YouthAvgHrs_2018,
        YouthAvgHrsByActivity_2018,
        YouthAvgHrsByCause_2018,
        YouthAvgHrsCommInvolve_2018,
        YouthAvgHrsHelpDirectly_2018,
        YouthBarriers_2018,
        YouthBarriersVol_2018,
        YouthCommInvolveRate_2018,
        YouthDonRateByCause_2018,
        YouthDonRateByMeth_2018,
        YouthDonRates_2018,
        YouthEfficiencyConcerns_2018,
        YouthHelpDirectlyRate_2018,
        YouthReasonsGiving_2018,
        YouthReasonsVol_2018,
        YouthSolicitationConcerns_2018,
        YouthVolRateByActivity_2018,
        YouthVolRateByCause_2018,
        YouthVolRate_2018]

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
