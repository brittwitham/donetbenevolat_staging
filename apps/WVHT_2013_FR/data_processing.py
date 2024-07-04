# Data processing file for WVHT_2013_FR converted from WVA020113_fr.py

from .data_utils import *


VolRate_2018, AvgTotHours_2018, FormsVolunteering_2018, PercTotVols_2018, PercTotHours_2018 = get_data()

data = [
    VolRate_2018,
    AvgTotHours_2018,
    PercTotVols_2018,
    PercTotHours_2018,
    FormsVolunteering_2018]

data = process_data(data)

PercTotVols_2018 = translate(PercTotVols_2018)
PercTotHours_2018 = translate(PercTotHours_2018)

region_values = get_region_values()
region_names = get_region_names()

status_names = ["Situation d'activité", "Statut d'immigration"]
