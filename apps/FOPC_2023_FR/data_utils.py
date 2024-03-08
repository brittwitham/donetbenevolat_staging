import pandas as pd
import numpy as np
import os
import os.path as op

# define NA values
na_values = [' ',  '-NaN', '-nan', '<NA>', 'N/A', 'NA', 'NULL', 'NaN', 'n/a', 'nan', 'null']

# Example functions
def get_data():
    filepath = op.join(os.getcwd(), "tables", "{}")

    futureOutlook = pd.read_csv("tables/futureOutlook_FR.csv", keep_default_na=False, na_values = na_values)
    futureOutlookByQuarter = pd.read_csv("tables/futureOutlookByQuarter_FR.csv", keep_default_na=False, na_values = na_values)
    org3MonthExpectations = pd.read_csv("tables/org3MonthExpectations_FR.csv", keep_default_na=False, na_values = na_values)
    org3MonthExpectations_facet = pd.read_csv("tables/org3MonthExpectations_facet_FR.csv", keep_default_na=False, na_values = na_values)

    return futureOutlook, futureOutlookByQuarter, org3MonthExpectations, org3MonthExpectations_facet

def get_region_values():
    return np.array(["CA", "BC", "AB", "SK", "MB", "ON", "QC", "NB", "NS", "PE", "NL", "YT", "NT", "NU"], dtype=object)

def get_bus_char():
    return np.array(["Organismes communautaires à but non lucratif", "Institutions commerciales à but non lucratif", 
                     "Institutions gouvernementales", "Entreprises"], dtype=object)

def get_list_factors():
    return np.array(['Dépenses opérationnelles', 'Demande', 'Nombre d’employés', 'Dépenses liées à la formation', 'Résultat opérationnel', 
                     'Budget de marketing', 'Dépenses en capital', 'Prix de vente', 'Ventes', 'Réserves de trésorerie', 'Rentabilité', 
                     'Postes vacants', 'Dépenses liées à la recherche et au développement', 'Importations', 'Exportations'], dtype=object)