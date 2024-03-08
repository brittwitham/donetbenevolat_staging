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
    
    accessLiquidity = pd.read_csv(op.abspath(filepath.format("accessLiquidity_FR.csv")), keep_default_na=False, na_values = na_values)
    accessLiquidityChange = pd.read_csv(op.abspath(filepath.format("accessLiquidityChange_FR.csv")), keep_default_na=False, na_values = na_values)
    receiveCEBA = pd.read_csv(op.abspath(filepath.format("receiveCEBA_FR.csv")), keep_default_na=False, na_values = na_values)
    statusCEBA = pd.read_csv(op.abspath(filepath.format("statusCEBA_FR.csv")), keep_default_na=False, na_values = na_values)
    willPayCEBA = pd.read_csv(op.abspath(filepath.format("willPayCEBA_FR.csv")), keep_default_na=False, na_values = na_values)

    return accessLiquidity, accessLiquidityChange, receiveCEBA, statusCEBA, willPayCEBA


# def process_data(data):
#     for i in range(len(data)):
#         # Replace pass with data processing
#         pass

#     return data

def get_region_values():
    return np.array(["CA", "BC", "AB", "SK", "MB", "ON", "QC", "NB", "NS", "PE", "NL", "YT", "NT", "NU"], dtype=object)

def get_list_factors():
    return np.array(["A suffisamment de liquidités",
                     "Pourra avoir accès à suffisamment de liquidités",
                     "Ne pourra pas avoir accès à suffisamment de liquidités",
                     "Incertain s'il (si elle) pourra avoir accès à suffisamment de liquidités"], dtype=object)