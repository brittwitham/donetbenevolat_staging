# Data processing file for WKCG_2013_FR converted from WKC010613_fr.py

from .data_utils import *


Barriers_2018, AvgAmtBarriers_2018, GivingConcerns_2018, SolicitationConcerns_2018, BarriersByCause_2018 = get_data()

data = [
    Barriers_2018,
    AvgAmtBarriers_2018,
    GivingConcerns_2018,
    SolicitationConcerns_2018,
    BarriersByCause_2018]

cause_names = BarriersByCause_2018["Group"].unique()
barriers_names = Barriers_2018["QuestionText"].unique()
status_names = ["État civil", "Situation d'activité",
                "Fréquence de la fréquentation religieuse"]

data = process_data(data)

region_values = get_region_values()
region_names = get_region_names()
