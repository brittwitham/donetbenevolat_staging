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

revGrowth = pd.read_csv(op.abspath(filepath.format("revGrowth.csv")))
revGrowthSource = pd.read_csv(op.abspath(filepath.format("revGrowthSource.csv")))
revSource = pd.read_csv(op.abspath(filepath.format("revSource.csv")))
revGrowthActivity = pd.read_csv(op.abspath(filepath.format("revGrowthActivity.csv")))
revSubSecActivity = pd.read_csv(op.abspath(filepath.format("revSubSecActivity.csv")))

Growth_dfs = [revGrowth, revGrowthSource, revSource, revGrowthActivity, revSubSecActivity]
Growth_filepaths = ["revGrowth.csv", "revGrowthSource.csv", "revSource.csv", "revGrowthActivity.csv"]

def format_fr(parts):
    if isinstance(parts, str):
        return ""
    if parts[-1] == "M":
        letter = "M"
    elif parts[-1] == "B":
        letter = "G"
    else:
        print(parts)
        return ""
    return f"{parts[0]}.{parts[1]} {letter}$"

for df in SubSec_dfs:
    split = [re.findall(r"[^\W\d_]+|\d+", label) if isinstance(label, str) else "" for label in df['label']]
    formatted = [format_fr(parts) for parts in split]

    df['label_FR'] = formatted

for df in Growth_dfs:
    for col in df.columns:
        if "label" in col and "_FR" not in col:
            split = [re.findall(r"[^\W\d_]+|\d+", label) if isinstance(label, str) else "" for label in df[col]]
            formatted = [format_fr(parts) for parts in split]

            df[col+"_FR"] = formatted

gdpSubSec.to_csv(op.abspath(filepath.format("gdpSubSec.csv")))
revSubSec.to_csv(op.abspath(filepath.format("revSubSec.csv")))

revGrowth.to_csv(op.abspath(filepath.format("revGrowth.csv")))
revGrowthActivity.to_csv(op.abspath(filepath.format("revGrowthActivity.csv")))
revGrowthSource.to_csv(op.abspath(filepath.format("revGrowthSource.csv")))
revSource.to_csv(op.abspath(filepath.format("revSource.csv")))
revSubSecActivity.to_csv(op.abspath(filepath.format("revSubSecActivity.csv")))

