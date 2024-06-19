# Data processing file for WVHT_2018_FR converted from Qui_sont_les_benevoles_et_combien_heures_donnent_ils_2018.py

from .data_utils import *


VolRate_2018, AvgTotHours_2018, FormsVolunteering_2018, PercTotVols_2018, PercTotHours_2018 = get_data()

PercTotVols_2018 = translate(PercTotVols_2018)
PercTotHours_2018 = translate(PercTotHours_2018)

VolRate_2018 = translate(VolRate_2018)
AvgTotHours_2018 = translate(AvgTotHours_2018)

data = [VolRate_2018, AvgTotHours_2018, PercTotVols_2018, PercTotHours_2018, FormsVolunteering_2018]

data = process_data(data)

region_values = get_region_values()
region_names = get_region_names()

status_names = ["Situation d'activité", "Statut d'immigration"]

