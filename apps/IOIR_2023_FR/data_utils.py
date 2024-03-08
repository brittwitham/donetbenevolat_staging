import pandas as pd
import numpy as np
import os
import os.path as op

# define NA values
na_values = [' ',  '-NaN', '-nan', '<NA>', 'N/A', 'NA', 'NULL', 'NaN', 'n/a', 'nan', 'null']

# Example functions
def get_data():
    filepath = op.join(os.getcwd(), "tables", "{}")

    #df1 = pd.read_csv(op.abspath(filepath.format("<DF1 CSV FILE>.csv")))
    
    greatestImpactInterestRates = pd.read_csv("tables/greatestImpactInterestRates_FR.csv", keep_default_na=False, na_values = na_values)
    impactLevelInterestRates = pd.read_csv("tables/impactLevelInterestRates_FR.csv", keep_default_na=False, na_values = na_values)
    org3MonthObstaclesImpact = pd.read_csv("tables/org3MonthObstaclesImpact_FR.csv", keep_default_na=False, na_values = na_values)
    orgExpectedObstaclesChange = pd.read_csv("tables/orgExpectedObstaclesChange_FR.csv", keep_default_na=False, na_values = na_values)
    orgGreatestObstacleImpact = pd.read_csv("tables/orgGreatestObstacleImpact_FR.csv", keep_default_na=False, na_values = na_values)

    return greatestImpactInterestRates, impactLevelInterestRates, org3MonthObstaclesImpact, orgExpectedObstaclesChange, orgGreatestObstacleImpact

def get_region_values():
    return np.array(["CA", "BC", "AB", "SK", "MB", "ON", "QC", "NB", "NS", "PE", "NL", "YT", "NT", "NU"], dtype=object)

def get_list_factors():
    return np.array(["Inflation", "Taux d'intérêt"])