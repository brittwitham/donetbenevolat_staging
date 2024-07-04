# Data processing file for WDHG_2013_FR converted from WDA010113_fr.py

from .data_utils import *


[DonRates_2018, AvgTotDon_2018, AvgNumCauses_2018, FormsGiving_2018,
    TopCauseFocus_2018, PropTotDon_2018, PropTotDonAmt_2018] = get_data()
data = [
    DonRates_2018,
    AvgTotDon_2018,
    FormsGiving_2018,
    TopCauseFocus_2018,
    PropTotDon_2018,
    PropTotDonAmt_2018]
data_num = [AvgNumCauses_2018]
values = ["Utiliser avec précaution", 'Estimation supprimée', '']
status_names = ["État civil", "Situation d'activité", "Statut d'immigration"]

data = process_data(data)
data_num = process_data_num(data_num)
#
# Extract info from data for selection menus
region_values = get_region_values()
region_names = get_region_names()
