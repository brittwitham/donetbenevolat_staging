# Data processing file for WDCV_2013_FR converted from WDC020513_fr.py

from .data_utils import *


ReasonsVol_2018, AvgHrsReasons_2018, MotivationsVolByCause_2018 = get_data()
# data = [ReasonsVol_2018, AvgHrsReasons_2018, MotivationsVolByCause_2018]
data = [MotivationsVolByCause_2018]
data2 = [ReasonsVol_2018, AvgHrsReasons_2018]
data = process_data(data)
data2 = process_data2(data2)

# ReasonsVol_2018 = translate(ReasonsVol_2018)
# AvgHrsReasons_2018 = translate(AvgHrsReasons_2018)
# MotivationsVolByCause_2018 = translate(MotivationsVolByCause_2018)

region_values = get_region_values()
region_names = get_region_names()
cause_names = MotivationsVolByCause_2018["Group"].unique()
motivations_names = ReasonsVol_2018["QuestionText"].unique()
status_names = [
    'État civil',
    "Situation d'activité",
    "Statut d'immigration",
    "Fréquence de la fréquentation religieuse"]

clean_names = []
for i in motivations_names:
    x = i.replace('<br>', ' ')
    clean_names.append(x)

motivations_names = clean_names
