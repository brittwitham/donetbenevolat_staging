# Data processing file for UTV_2018_FR converted from Comprendre_les_benevoles_tres_engages_2018.py

from .data_utils import *


TopVolsMotivations_2018, TopVolsBarriers_2018, TopVolsPercTotHours_2018, TopVolsPercTotVols_2018, TopVolsVolRates_2018, TopVolsDemoLikelihoods = get_data()

data = [TopVolsMotivations_2018, TopVolsBarriers_2018, TopVolsPercTotHours_2018, TopVolsPercTotVols_2018, TopVolsVolRates_2018, TopVolsDemoLikelihoods]

data = process_data(data)

region_values = get_region_values()
region_names = get_region_names()

demo_names = list(set(TopVolsDemoLikelihoods["Group"]))
demo_names.remove('État civil (original)')
# demo_names.remove('')

