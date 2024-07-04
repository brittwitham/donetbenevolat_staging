# Data processing file for WDVD_2013_FR converted from WDV020213_fr.py

from .data_utils import *


ActivityVolRate_2018, AvgHoursVol_2018 = get_data()
data = [ActivityVolRate_2018, AvgHoursVol_2018]
data = process_data(data)

# Extract info from data for selection menus
region_values = get_region_values()
region_names = get_region_names()
activity_names = ActivityVolRate_2018.QuestionText.unique()
status_names = ["Situation d'activité", "Statut d'immigration"]

names = []
for i in activity_names:
    i.replace("<br>", '')
    names.append(i)

activity_names = names
