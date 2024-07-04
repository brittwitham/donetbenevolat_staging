# Data processing file for HDCD_2018_FR converted from
# Comment_donne_t_on_au_Canada_2018.py

from .data_utils import *


DonMethAvgDon_2018, DonMethDonRates_2018 = get_data()

data = [DonMethAvgDon_2018, DonMethDonRates_2018]

# translate_data(data)
data = process_data(data)

region_values = get_region_values()
region_names = get_region_names()
method_names = DonMethAvgDon_2018["QuestionText"].unique()

status_names = ['État civil', "Situation d'activité", "Statut d'immigration"]
