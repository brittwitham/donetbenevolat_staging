import pandas as pd
import numpy as np
import os
import os.path as op

# define NA values
na_values = [' ',  '-NaN', '-nan', '<NA>', 'N/A', 'NA', 'NULL', 'NaN', 'n/a', 'nan', 'null']

# Example functions
def get_data():
    filepath = op.join(os.getcwd(), "tables", "{}")

    donationChallenges = pd.read_csv("tables/donationChallenges_FR.csv", keep_default_na=False, na_values = na_values)
    donationChallengesDetailed = pd.read_csv("tables/donationChallengesDetailed_FR.csv", keep_default_na=False, na_values = na_values)
    donationImpact = pd.read_csv("tables/donationImpact_FR.csv", keep_default_na=False, na_values = na_values)
    donationImpactDetailed = pd.read_csv("tables/donationImpactDetailed_FR.csv", keep_default_na=False, na_values = na_values)

    return donationChallenges, donationChallengesDetailed, donationImpact, donationImpactDetailed

def get_region_values():
    return np.array(["CA", "BC", "AB", "SK", "MB", "ON", "QC", "NB", "NS", "PE", "NL", "YT", "NT", "NU"], dtype=object)

def get_bus_groups():
    return np.array(["Emploi", "Lieu", "Âge de l'entreprise"], dtype=object)

def get_text_items_1():
    return np.array(["Recherche de nouveaux donateurs", 
                     "Sommes versées par les donateurs pas aussi élevées qu'avant", 
                     "Conservation des donateurs",
                     "Manque de temps ou de ressources", "Autre", "Aucun"], dtype=object)

def get_text_items_2():
    return np.array(["Dépendance accrue aux bénévoles", 
                     "Exploration d'autres sources de revenus", 
                     "Réduction des dépenses non liées au personnel",
                     "Réduction du nombre de programmes", 
                     "Réduction du personnel", 
                     "Annulation de programmes", 
                     "Incapacité d'accepter de nouveaux clients", 
                     "Risque de fermeture",
                     "Autre", "Aucun"], dtype=object)