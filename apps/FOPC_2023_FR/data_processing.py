import pandas as pd
import numpy as np
from .data_utils import *

# Rename these accordingly
futureOutlook, futureOutlookByQuarter, org3MonthExpectations, org3MonthExpectations_facet = get_data()

# Example structure
data = [futureOutlook, futureOutlookByQuarter, org3MonthExpectations, org3MonthExpectations_facet]
# data = process_data(data)
region_values = get_region_values()
list_factors = get_list_factors()
bus_char = get_bus_char()
# region_names = get_region_names()
# demo_names = get_demo_names()

