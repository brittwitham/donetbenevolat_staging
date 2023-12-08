import pandas as pd
import plotly.graph_objects as go
import numpy as np
import os
import os.path as op
from .data_utils import *


def get_data():
    filepath = op.join(os.getcwd(), "tables", "{}")

    empGrowth = pd.read_csv(op.abspath(filepath.format("empGrowth.csv")))
    empSubSec = pd.read_csv(op.abspath(filepath.format("empSubSec.csv")))
    empSubSecActivity = pd.read_csv(op.abspath(
        filepath.format("empSubSecActivity.csv")))
    empGrowthActivity = pd.read_csv(op.abspath(
        filepath.format("empGrowthActivity.csv")))

    return empGrowth, empSubSec, empSubSecActivity, empGrowthActivity
