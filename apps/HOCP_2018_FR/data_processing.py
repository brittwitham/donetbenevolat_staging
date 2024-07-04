# Data processing file for HOCP_2018_FR converted from
# Aide_autrui_et_amelioration_communautaire_2018.py

from .data_utils import *


VolRate_2018, CommInvolveHrs_2018, CommInvolveRate_2018, HelpDirectHrs_2018, HelpDirectRate_2018, FormsVolunteering_2018 = get_data()
data = [
    VolRate_2018,
    CommInvolveHrs_2018,
    CommInvolveRate_2018,
    HelpDirectHrs_2018,
    HelpDirectRate_2018,
    FormsVolunteering_2018]

data = process_data(data)
region_values = get_region_values()
region_names = get_region_names()

# demo_names = ['Age group', 'Gender', 'Education',
#             'Marital status', 'Labour force status', 'Catégorie de revenu personnel',
#             'Frequency of religious attendance', 'Immigration status']
demo_names = [
    "Groupe d'âge",
    'Genre',
    'Éducation',
    'État civil',
    "Situation d'activité",
    'Catégorie de revenu familial',
    'Fréquence de la fréquentation religieuse',
    "Statut d'immigration"]
