import pandas as pd
import numpy as np
from .data_utils import *

# # Rename these accordingly
donationChallenges, donationChallengesDetailed, donationImpact, donationImpactDetailed = get_data()

# # Example structure
data = [donationChallenges, donationChallengesDetailed, donationImpact, donationImpactDetailed]
# data = process_data(data)
region_values = get_region_values()
bus_groups = get_bus_groups()
text_items_1 = get_text_items_1()
text_items_2 = get_text_items_2()
# region_names = get_region_names()
# demo_names = get_demo_names()

