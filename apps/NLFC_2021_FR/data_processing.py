import pandas as pd
import plotly.graph_objects as go
import numpy as np
import os
import os.path as op
from .data_utils import *


def get_data():
    filepath = op.join(os.getcwd(), "tables", "{}")

    jobsType = pd.read_csv(op.abspath(filepath.format("jobsType.csv")))
    wagesType = pd.read_csv(op.abspath(filepath.format("wagesType.csv")))
    jobsDemog = pd.read_csv(op.abspath(filepath.format("jobsDemog.csv")))
    wagesDemog = pd.read_csv(op.abspath(filepath.format("wagesDemog.csv")))

    return jobsType, wagesType, jobsDemog, wagesDemog
