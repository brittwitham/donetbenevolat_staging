import pandas as pd
import numpy as np
from .data_utils import *

# Rename these accordingly
expectedObstaclesChange, org3MonthObstacles, orgGreatestObstacle= get_data()

# Example structure
data = [expectedObstaclesChange, org3MonthObstacles, orgGreatestObstacle]
# data = process_data(data)
region_values = get_region_values()
list_factors = get_list_factors()
# region_names = get_region_names()
# demo_names = get_demo_names()

