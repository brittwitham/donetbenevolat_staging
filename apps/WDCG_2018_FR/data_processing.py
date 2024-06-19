# Data processing file for WDCG_2018_FR converted from
# Pourquoi_donne_t_on_au_Canada_2018.py

from .data_utils import *


Reasons_2018, AvgAmtReasons_2018, MotivationsByCause_2018 = get_data()

data = [Reasons_2018, AvgAmtReasons_2018, MotivationsByCause_2018]

cause_names = MotivationsByCause_2018["Group"].unique()
motivations_names = Reasons_2018["QuestionText"].unique()
status_names = ["État civil", "Situation d'activité", "Statut d'immigration"]

data = process_data(data)

region_values = get_region_values()
region_names = get_region_names()
