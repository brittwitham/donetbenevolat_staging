# Data processing file for UTD_2018_FR converted from
# Comprendre_les_grands_donateurs_2018.py

from .data_utils import *


TopDonorsMotivations_2018, TopDonorsBarriers_2018, TopDonorsPercTotDonations_2018, TopDonorsPercTotDonors_2018, TopDonorsDonRates_2018, TopDonorsDemoLikelihoods = get_data()

data = [
    TopDonorsMotivations_2018,
    TopDonorsBarriers_2018,
    TopDonorsPercTotDonations_2018,
    TopDonorsPercTotDonors_2018,
    TopDonorsDonRates_2018,
    TopDonorsDemoLikelihoods]
data = process_data(data)

region_values = get_region_values()
region_names = get_region_names()
demo_names = TopDonorsDemoLikelihoods["Group"].unique()
