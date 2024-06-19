# Data processing file for GV_EO_2018_FR converted from GAV0303_fr.py

from .data_utils import *


SubSecAvgDon_2018, SubSecDonRates_2018, SubSecDonRatesFoc_2018, SubSecAvgHrs_2018, SubSecVolRates_2018, SubSecVolRatesFoc_2018, EducDonorsBarriers_2018, EducDonorsDonMeth_2018, EducDonorsDonRates_2018, EducDonorsMotivations_2018, EducVolsActivities_2018, EducVolsBarriers_2018, EducVolsMotivations_2018, EducVolsVolRates_2018 = get_data()
data = [
    SubSecAvgDon_2018,
    SubSecDonRates_2018,
    SubSecDonRatesFoc_2018,
    EducDonorsBarriers_2018,
    EducDonorsDonMeth_2018,
    EducDonorsDonRates_2018,
    EducDonorsMotivations_2018,
    EducVolsActivities_2018,
    EducVolsBarriers_2018,
    EducVolsMotivations_2018,
    EducVolsVolRates_2018,
    SubSecAvgHrs_2018,
    SubSecVolRates_2018,
    SubSecVolRatesFoc_2018]
process_data(data)

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
