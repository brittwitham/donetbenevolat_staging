import pandas as pd
import plotly.graph_objects as go
import numpy as np
import os
import os.path as op
from .data_utils import *


def get_data():
    filepath = op.join(os.getcwd(), "tables", "{}")

    revGrowth = pd.read_csv(op.abspath(filepath.format("revGrowth.csv")))
    revSubSec = pd.read_csv(op.abspath(filepath.format("revSubSec.csv")))
    revSubSecActivity = pd.read_csv(op.abspath(
        filepath.format("revSubSecActivity.csv")))
    revGrowthActivity = pd.read_csv(op.abspath(
        filepath.format("revGrowthActivity.csv")))
    revSource = pd.read_csv(op.abspath(filepath.format("revSource.csv")))
    revGrowthSource = pd.read_csv(op.abspath(
        filepath.format("revGrowthSource.csv")))

    return revGrowth, revSubSec, revSubSecActivity, revGrowthActivity, revSource, revGrowthSource
