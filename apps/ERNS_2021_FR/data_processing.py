import pandas as pd
import plotly.graph_objects as go
import numpy as np
import os
import os.path as op
from .data_utils import *


def get_data():
    filepath = op.join(os.getcwd(), "tables", "{}")

    gdpGrowth = pd.read_csv(op.abspath(filepath.format("gdpGrowth.csv")))
    gdpSubSec = pd.read_csv(op.abspath(filepath.format("gdpSubSec.csv")))
    gdpSubSecActivity = pd.read_csv(op.abspath(
        filepath.format("gdpSubSecActivity.csv")))
    perNatGDP = pd.read_csv(op.abspath(filepath.format("perNatGDP.csv")))

    return gdpGrowth, gdpSubSec, gdpSubSecActivity, perNatGDP
