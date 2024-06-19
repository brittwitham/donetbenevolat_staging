# Data processing file for GV_HO_2018_FR converted from GAV0301_fr.py

from .data_utils import *


SubSecAvgDon_2018, SubSecDonRates_2018, SubSecDonRatesFoc_2018, SubSecAvgHrs_2018, SubSecVolRates_2018, SubSecVolRatesFoc_2018, HealthDonorsBarriers_2018, HealthDonorsDonMeth_2018, HealthDonorsDonRates_2018, HealthDonorsMotivations_2018, HealthVolsActivities_2018, HealthVolsBarriers_2018, HealthVolsMotivations_2018, HealthVolsVolRates_2018 = get_data()
data = [
    SubSecAvgDon_2018,
    SubSecDonRates_2018,
    SubSecDonRatesFoc_2018,
    HealthDonorsBarriers_2018,
    HealthDonorsDonMeth_2018,
    HealthDonorsDonRates_2018,
    HealthDonorsMotivations_2018,
    HealthVolsActivities_2018,
    HealthVolsBarriers_2018,
    HealthVolsMotivations_2018,
    HealthVolsVolRates_2018,
    SubSecAvgHrs_2018,
    SubSecVolRates_2018,
    SubSecVolRatesFoc_2018]
data = process_data(data)

region_values = get_region_values()
region_names = get_region_names()
demo_names = [
    "Groupe d'âge",
    'Genre',
    'Éducation',
    'État civil',
    "Situation d'activité",
    'Catégorie de revenu personnel',
    'Catégorie de revenu familial',
    'Fréquence de la fréquentation religieuse',
    "Statut d'immigration"]
