# Data processing file for WTOS_2018_FR converted from
# Quels_types_organismes_soutient_on_au_Canada_2018.py

from .data_utils import *


SubSecDonRates_2018, SubSecAvgDon_2018, Allocation_2018 = get_data()
data = [SubSecDonRates_2018, SubSecAvgDon_2018, Allocation_2018]
data = process_data(data)

region_values = get_region_values()
region_names = get_region_names()
