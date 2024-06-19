# Data processing file for WKCV_2018_FR converted from
# Qu_est_ce_qui_empeche_de_faire_du_benevolat_2018.py

from .data_utils import *


BarriersVol_2018, BarriersVolMore_2018, AvgHoursBarriersVol_2018, BarriersVolByCause_2018 = get_data()

data = [
    BarriersVol_2018,
    BarriersVolMore_2018,
    AvgHoursBarriersVol_2018,
    BarriersVolByCause_2018]
data = process_data(data)

cause_names = BarriersVolByCause_2018["Group"].unique()
barriers_names = BarriersVol_2018["QuestionText"].unique()
region_values = get_region_values()
region_names = get_region_names()
status_names = [
    'État civil',
    'Fréquence de la fréquentation religieuse',
    "Statut d'immigration"]
