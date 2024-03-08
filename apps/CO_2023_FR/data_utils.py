import pandas as pd
import numpy as np
import os
import os.path as op

# define NA values
na_values = [' ',  '-NaN', '-nan', '<NA>', 'N/A', 'NA', 'NULL', 'NaN', 'n/a', 'nan', 'null']

# Example functions
def get_data():
    filepath = op.join(os.getcwd(), "tables", "{}")

    expectedObstaclesChange = pd.read_csv("tables/expectedObstaclesChange_FR.csv", keep_default_na=False, na_values = na_values)
    org3MonthObstacles = pd.read_csv("tables/org3MonthObstacles_FR.csv", keep_default_na=False, na_values = na_values)
    orgGreatestObstacle = pd.read_csv("tables/orgGreatestObstacle_FR.csv", keep_default_na=False, na_values = na_values)

    return expectedObstaclesChange, org3MonthObstacles, orgGreatestObstacle

def get_region_values():
    return np.array(["CA", "BC", "AB", "SK", "MB", "ON", "QC", "NB", "NS", "PE", "NL", "YT", "NT", "NU"], dtype=object)

def get_list_factors():
    return np.array(["Défis liés à la main-d'œuvre", 
                     "Inflation", 
                     "Recrutement d'employés qualifiés",
                     "Conservation d'employés qualifiés", 
                     "Pénurie de main-d'œuvre",
                     "Augmentation des coûts liés aux intrants", 
                     "Coûts liés à l'assurance",
                     "Difficulté à attirer de nouveaux clients", 
                     "Pénurie d'espace ou d'équipement",
                     "Coûts liés au transport", 
                     "Flux de trésorerie ou dette", 
                     "Obtention de financement",
                     "Coûts liés à l'immobilier", 
                     "Acquisition d'intrants au pays",
                     "Insuffisance de la demande", 
                     "Taux d'intérêt", 
                     "Fluctuations de la demande",
                     "Augmentation de la concurrence", 
                     "Maintien des stocks",
                     "Acquisition d'intrants à l'étranger", 
                     "Défis liés à l'exportation",
                     "Autre obstacle", 
                     "Aucun"], dtype=object)