import pandas as pd
import os.path as op
import os

filepath = op.join(os.getcwd(), "tables", "{}")

def get_dataframe(csv_name):
    df = pd.read_csv(op.abspath(filepath.format(csv_name)))
    return df