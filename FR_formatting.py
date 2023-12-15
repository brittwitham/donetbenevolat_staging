import pandas as pd
import numpy as np
import os
import os.path as op
import re

# Subsec tables
filepath = op.join(os.getcwd(), "tables", "{}")

gdpSubSec = pd.read_csv(op.abspath(filepath.format("gdpSubSec.csv")))
revSubSec = pd.read_csv(op.abspath(filepath.format("revSubSec.csv")))
SubSec_dfs = [gdpSubSec, revSubSec]
SubSec_filepaths = ["gdpSubSec.csv", "revSubSec.csv"]

def format_fr(parts):
    if isinstance(parts, str):
        return ""
    if parts[-1] == "M":
        letter = "M"
    elif parts[-1] == "B":
        letter = "G"
    return f"{parts[0]}.{parts[1]} {letter}$"

for df in SubSec_dfs:
    split = [re.findall(r"[^\W\d_]+|\d+", label) if isinstance(label, str) else "" for label in df['label']]
    formatted = [format_fr(parts) for parts in split]

    df['label_FR'] = formatted

gdpSubSec = gdpSubSec.to_csv(op.abspath(filepath.format("gdpSubSec.csv")))
revSubSec = revSubSec.to_csv(op.abspath(filepath.format("revSubSec.csv")))


