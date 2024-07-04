# Data processing file for GV_NC_2018_FR converted from GAV0306_fr.py

from .data_utils import *

NewCanadiansAvgDonAmt_2018, NewCanadiansAvgDonByCause_2018, NewCanadiansAvgDonByMeth_2018, NewCanadiansAvgHrs_2018, NewCanadiansAvgHrsByActivity_2018, NewCanadiansAvgHrsByCause_2018, NewCanadiansAvgHrsCommInvolve_2018, NewCanadiansAvgHrsHelpDirectly_2018, NewCanadiansBarriers_2018, NewCanadiansBarriersVol_2018, NewCanadiansCommInvolveRate_2018, NewCanadiansDonRateByCause_2018, NewCanadiansDonRateByMeth_2018, NewCanadiansDonRates_2018, NewCanadiansEfficiencyConcerns_2018, NewCanadiansHelpDirectlyRate_2018, NewCanadiansReasonsGiving_2018, NewCanadiansReasonsVol_2018, NewCanadiansSolicitationConcerns_2018, NewCanadiansVolRateByActivity_2018, NewCanadiansVolRateByCause_2018, NewCanadiansVolRate_2018 = get_data()

# rates = [NewCanadiansBarriers_2018,
#          NewCanadiansBarriersVol_2018,
#          NewCanadiansCommInvolveRate_2018,
#          NewCanadiansDonRateByCause_2018,
#          NewCanadiansDonRateByMeth_2018,
#          NewCanadiansDonRates_2018,
#          NewCanadiansEfficiencyConcerns_2018,
#          NewCanadiansHelpDirectlyRate_2018,
#          NewCanadiansReasonsGiving_2018,
#          NewCanadiansReasonsVol_2018,
#          NewCanadiansSolicitationConcerns_2018,
#          NewCanadiansVolRateByActivity_2018,
#          NewCanadiansVolRateByCause_2018,
#          NewCanadiansVolRate_2018]

# data = [NewCanadiansAvgDonAmt_2018,
#         NewCanadiansAvgDonByCause_2018,
#         NewCanadiansAvgDonByMeth_2018,
#         NewCanadiansAvgHrs_2018,
#         NewCanadiansAvgHrsByActivity_2018,
#         NewCanadiansAvgHrsByCause_2018,
#         NewCanadiansAvgHrsCommInvolve_2018,
#         NewCanadiansAvgHrsHelpDirectly_2018,
#         NewCanadiansBarriers_2018,
#         NewCanadiansBarriersVol_2018,
#         NewCanadiansCommInvolveRate_2018,
#         NewCanadiansDonRateByCause_2018,
#         NewCanadiansDonRateByMeth_2018,
#         NewCanadiansDonRates_2018,
#         NewCanadiansEfficiencyConcerns_2018,
#         NewCanadiansHelpDirectlyRate_2018,
#         NewCanadiansReasonsGiving_2018,
#         NewCanadiansReasonsVol_2018,
#         NewCanadiansSolicitationConcerns_2018,
#         NewCanadiansVolRateByActivity_2018,
#         NewCanadiansVolRateByCause_2018,
#         NewCanadiansVolRate_2018]

# process_data(data)
# process_rates(rates)

# region_values = get_region_values()
# region_names = get_region_names()
NewCanadiansAvgDonAmt_2018 = get_dataframe("2018-NewCanadiansAvgDonAmt_FR.csv")
NewCanadiansAvgDonByCause_2018 = get_dataframe(
    "2018-NewCanadiansAvgDonByCause_FR.csv")
NewCanadiansAvgDonByMeth_2018 = get_dataframe(
    "2018-NewCanadiansAvgDonByMeth_FR.csv")
NewCanadiansAvgHrs_2018 = get_dataframe("2018-NewCanadiansAvgHrs_FR.csv")
NewCanadiansAvgHrsByActivity_2018 = get_dataframe(
    "2018-NewCanadiansAvgHrsByActivity_FR.csv")
NewCanadiansAvgHrsByCause_2018 = get_dataframe(
    "2018-NewCanadiansAvgHrsByCause_FR.csv")
NewCanadiansAvgHrsCommInvolve_2018 = get_dataframe(
    "2018-NewCanadiansAvgHrsCommInvolve_FR.csv")
NewCanadiansAvgHrsHelpDirectly_2018 = get_dataframe(
    "2018-NewCanadiansAvgHrsHelpDirectly_FR.csv")
NewCanadiansBarriers_2018 = get_dataframe(
    "2018-NewCanadiansBarriersGiving_FR.csv")
NewCanadiansBarriersVol_2018 = get_dataframe(
    "2018-NewCanadiansBarriersVol_FR.csv")
NewCanadiansCommInvolveRate_2018 = get_dataframe(
    "2018-NewCanadiansCommInvolveRate_FR.csv")
NewCanadiansDonRateByCause_2018 = get_dataframe(
    "2018-NewCanadiansDonRateByCause_FR.csv")
NewCanadiansDonRateByMeth_2018 = get_dataframe(
    "2018-NewCanadiansDonRateByMeth_FR.csv")
NewCanadiansDonRates_2018 = get_dataframe("2018-NewCanadiansDonRates_FR.csv")
NewCanadiansEfficiencyConcerns_2018 = get_dataframe(
    "2018-NewCanadiansEfficiencyConcerns_FR.csv")
NewCanadiansHelpDirectlyRate_2018 = get_dataframe(
    "2018-NewCanadiansHelpDirectlyRate_FR.csv")
NewCanadiansReasonsGiving_2018 = get_dataframe(
    "2018-NewCanadiansReasonsGiving_FR.csv")
NewCanadiansReasonsVol_2018 = get_dataframe(
    "2018-NewCanadiansReasonsVol_FR.csv")
NewCanadiansSolicitationConcerns_2018 = get_dataframe(
    "2018-NewCanadiansSolicitationConcerns_FR.csv")
NewCanadiansVolRateByActivity_2018 = get_dataframe(
    "2018-NewCanadiansVolRateByActivity_FR.csv")
NewCanadiansVolRateByCause_2018 = get_dataframe(
    "2018-NewCanadiansVolRateByCause_FR.csv")
NewCanadiansVolRate_2018 = get_dataframe("2018-NewCanadiansVolRates_FR.csv")

rates = [NewCanadiansBarriers_2018,
         NewCanadiansBarriersVol_2018,
         NewCanadiansCommInvolveRate_2018,
         NewCanadiansDonRateByCause_2018,
         NewCanadiansDonRateByMeth_2018,
         NewCanadiansDonRates_2018,
         NewCanadiansEfficiencyConcerns_2018,
         NewCanadiansHelpDirectlyRate_2018,
         NewCanadiansReasonsGiving_2018,
         NewCanadiansReasonsVol_2018,
         NewCanadiansSolicitationConcerns_2018,
         NewCanadiansVolRateByActivity_2018,
         NewCanadiansVolRateByCause_2018,
         NewCanadiansVolRate_2018]

data = [NewCanadiansAvgDonAmt_2018,
        NewCanadiansAvgDonByCause_2018,
        NewCanadiansAvgDonByMeth_2018,
        NewCanadiansAvgHrs_2018,
        NewCanadiansAvgHrsByActivity_2018,
        NewCanadiansAvgHrsByCause_2018,
        NewCanadiansAvgHrsCommInvolve_2018,
        NewCanadiansAvgHrsHelpDirectly_2018,
        NewCanadiansBarriers_2018,
        NewCanadiansBarriersVol_2018,
        NewCanadiansCommInvolveRate_2018,
        NewCanadiansDonRateByCause_2018,
        NewCanadiansDonRateByMeth_2018,
        NewCanadiansDonRates_2018,
        NewCanadiansEfficiencyConcerns_2018,
        NewCanadiansHelpDirectlyRate_2018,
        NewCanadiansReasonsGiving_2018,
        NewCanadiansReasonsVol_2018,
        NewCanadiansSolicitationConcerns_2018,
        NewCanadiansVolRateByActivity_2018,
        NewCanadiansVolRateByCause_2018,
        NewCanadiansVolRate_2018]

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
