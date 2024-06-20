# Data processing file for HDCD_2013_FR converted from HDC010213_fr.py

from .data_utils import *

# DonMethAvgDon_2013, DonMethDonRates_2013 = get_data()

# data = [DonMethAvgDon_2013, DonMethDonRates_2013]
# process_data(data)

# region_values = get_region_values()
# region_names = get_region_names()
# method_names = DonMethAvgDon_2013["QuestionText"].unique()
DonMethAvgDon_2013, DonMethDonRates_2013 = get_data()

data = [DonMethAvgDon_2013, DonMethDonRates_2013]
data = process_data(data)

region_values = get_region_values()
region_names = get_region_names()
method_names = DonMethAvgDon_2013["QuestionText"].unique()
status_names = ['État civil', "Situation d'activité", "Statut d'immigration"]
