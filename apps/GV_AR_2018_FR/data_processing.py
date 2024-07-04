# Data processing file for GV_AR_2018_FR converted from GAV0305_fr.py

from .data_utils import *


SubSecAvgDon_2018, SubSecDonRates_2018, SubSecDonRatesFoc_2018, SubSecAvgHrs_2018, SubSecVolRates_2018, SubSecVolRatesFoc_2018, ArtRecDonorsBarriers_2018, ArtRecDonorsDonMeth_2018, ArtRecDonorsDonRates_2018, ArtRecDonorsMotivations_2018, ArtRecVolsActivities_2018, ArtRecVolsBarriers_2018, ArtRecVolsMotivations_2018, ArtRecVolsVolRates_2018 = get_data()
data = [
    SubSecAvgDon_2018,
    SubSecDonRates_2018,
    SubSecDonRatesFoc_2018,
    ArtRecDonorsBarriers_2018,
    ArtRecDonorsDonMeth_2018,
    ArtRecDonorsDonRates_2018,
    ArtRecDonorsMotivations_2018,
    ArtRecVolsActivities_2018,
    ArtRecVolsBarriers_2018,
    ArtRecVolsMotivations_2018,
    ArtRecVolsVolRates_2018,
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
