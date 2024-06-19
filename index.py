from dash import dcc, html
from dash.dependencies import Input, Output
from app import app, server

from apps import (
    # Qui_donne_aux_organismes_caritatifs_et_combien_2018,
    # Comment_donne_t_on_au_Canada_2018,
    # Comprendre_les_grands_donateurs_2018,
    # Pourquoi_donne_t_on_au_Canada_2018,
    # Qu_est_ce_qui_empeche_de_donner_plus_2018,
    # Quels_types_organismes_soutient_on_au_Canada_2018,
    # Qui_sont_les_benevoles_et_combien_heures_donnent_ils_2018,
    # Quelles_sont_les_activites_des_benevoles_2018,
    # Comprendre_les_benevoles_tres_engages_2018,
    # Aide_autrui_et_amelioration_communautaire_2018,
    Pourquoi_fait_on_du_benevolat_2018,
    Qu_est_ce_qui_empeche_de_faire_du_benevolat_2018,
    A_quels_types_organismes_fait_on_don_de_son_temps_au_Canada_2018,
    definition,
    GAV0301_fr, # sante
    GAV0302_fr, # religieux
    GAV0303_fr, # education
    GAV0304_fr, # services sociaux
    GAV0305_fr, # loisirs
    les_dons_et_le_benevolat_des_jeunes_2018,
    # 2013 data
    WDC010513_fr,
    WKC010613_fr,
    HDC010213_fr,
    WDA010113_fr,
    WDV020213_fr,
    WDC020513_fr,
    WKC020613_fr,
    WVA020113_fr,
    GAV0306_fr,
    GAV0307_fr,
    les_dons_et_le_benevolat_des_personnes_agees_2018

)

from apps.NSPS_2021_FR.app_layout import layout as NSPS_2021_FR_layout
from apps.NSR_2021_FR.app_layout import layout as NSR_2021_FR_layout
from apps.NLFC_2021_FR.app_layout import layout as NLFC_2021_FR_layout
from apps.ERNS_2021_FR.app_layout import layout as ERNS_2021_FR_layout

# Business Conditions Stories
from apps.LCLS_2023_FR.app_layout import layout as LCLS_2023_FR_layout
from apps.FOPC_2023_FR.app_layout import layout as FOPC_2023_FR_layout
from apps.IOIR_2023_FR.app_layout import layout as IOIR_2023_FR_layout
from apps.DT_2023_FR.app_layout import layout as DT_2023_FR_layout
from apps.CO_2023_FR.app_layout import layout as CO_2023_FR_layout

# Refactored modules
from apps.WDHG_2018_FR.app_layout import layout as WDHG_2018_FR_layout
from apps.HDCD_2018_FR.app_layout import layout as HDCD_2018_FR_layout
from apps.UTD_2018_FR.app_layout import layout as UTD_2018_FR_layout
from apps.WDCG_2018_FR.app_layout import layout as WDCG_2018_FR_layout
from apps.WKCG_2018_FR.app_layout import layout as WKCG_2018_FR_layout
from apps.WTOS_2018_FR.app_layout import layout as WTOS_2018_FR_layout
from apps.WDVD_2018_FR.app_layout import layout as WDVD_2018_FR_layout
from apps.WVHT_2018_FR.app_layout import layout as WVHT_2018_FR_layout
from apps.UTV_2018_FR.app_layout import layout as UTV_2018_FR_layout
from apps.HOCP_2018_FR.app_layout import layout as HOCP_2018_FR_layout

import homepage

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

app.index_string = """<!DOCTYPE html>
<html>
    <head>
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-L9SQCXF0DL"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'G-L9SQCXF0DL');
        </script>
                {%metas%}
                <title>{%title%}</title>
                {%favicon%}
                {%css%}
            </head>
            <body>
                {%app_entry%}
                <footer>
                    {%config%}
                    {%scripts%}
                    {%renderer%}
                </footer>
            </body>
</html>"""

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return dcc.Location(id='redirect', refresh=True, href="https://www.donetbenevolat.ca")
    elif pathname == '/Qui_donne_aux_organismes_caritatifs_et_combien_2018': #WDA0101_fr':
        return WDHG_2018_FR_layout
    elif pathname == '/Comment_donne_t_on_au_Canada_2018': #HDC0102_fr':
        return HDCD_2018_FR_layout
    elif pathname == '/Comprendre_les_grands_donateurs_2018': #UTD0103_fr':
        return UTD_2018_FR_layout
    elif pathname == '/Pourquoi_donne_t_on_au_Canada_2018': #/WDC0105_fr':
        return WDCG_2018_FR_layout
    elif pathname == '/Qu_est_ce_qui_empeche_de_donner_plus_2018': #WKC0106_fr':
        return WKCG_2018_FR_layout
    elif pathname == '/Quels_types_organismes_soutient_on_au_Canada_2018': #WTO0107_fr':
        return WTOS_2018_FR_layout
    elif pathname == '/Quelles_sont_les_activites_des_benevoles_2018': #WDV0202_fr':
        return WDVD_2018_FR_layout
    elif pathname == '/Qui_sont_les_benevoles_et_combien_heures_donnent_ils_2018': #WVA0201_fr':
        return WVHT_2018_FR_layout
    elif pathname == '/Comprendre_les_benevoles_tres_engages_2018': #/UTV0203_fr':
        return UTV_2018_FR_layout
    elif pathname == '/Aide_autrui_et_amelioration_communautaire_2018': #/HOA0204_fr':
        return HOCP_2018_FR_layout
    elif pathname == '/Pourquoi_fait_on_du_benevolat_2018': #WDC0205_fr':
        return Pourquoi_fait_on_du_benevolat_2018.layout
    elif pathname == '/Qu_est_ce_qui_empeche_de_faire_du_benevolat_2018': #WKC0206_fr':
        return Qu_est_ce_qui_empeche_de_faire_du_benevolat_2018.layout
    elif pathname == '/A_quels_types_organismes_fait_on_don_de_son_temps_au_Canada_2018': #WKC0206_fr':
        return A_quels_types_organismes_fait_on_don_de_son_temps_au_Canada_2018.layout
    elif pathname == '/dons_dargent_et_benevolat_pour_les_organismes_de_sante_2018': #GAV0304
        return GAV0301_fr.layout
    elif pathname == '/dons_et_benevolat_pour_les_organismes_du_secteur_de_leducation_2018': #GAV0304
        return GAV0303_fr.layout
    elif pathname == '/dons_et_benevolat_pour_les_organismes_de_services_sociaux_2018': #GAV0304
        return GAV0304_fr.layout
    elif pathname == '/dons_et_benevolat_pour_les_organismes_religieux_2018': #GAV0304
        return GAV0302_fr.layout
    elif pathname == '/dons_et_benevolat_pour_les_organismes_des_arts_et_des_loisirs_2018': #GAV0305
        return GAV0305_fr.layout
    elif pathname == '/les_dons_et_le_benevolat_des_personnes_nouvellement_arrivees_au_canada_2018': #GAV0306
        return GAV0306_fr.layout
    elif pathname == '/les_dons_et_le_benevolat_des_jeunes_2018': #GAV0307
        return les_dons_et_le_benevolat_des_jeunes_2018.layout
    elif pathname == '/les_dons_et_le_benevolat_des_personnes_agees_2018': #GAV0308
        return GAV0307_fr.layout
    elif pathname == '/comment_donne_t_on_au_canada_2013':
        return HDC010213_fr.layout
    elif pathname == '/pourquoi_donne_t_on_au_canada_2013':
        return WDC010513_fr.layout
    elif pathname == '/pourquoi_fait_on_du_benevolat_2013':
        return WDC020513_fr.layout
    elif pathname == '/qu_est_ce_qui_empeche_de_donner_plus_2013':
        return WKC010613_fr.layout
        # return qu_est_ce_qui_empeche_de_donner_plus_2013.layout
    elif pathname == '/qu_est_ce_qui_empeche_de_faire_du_benevolat_2013':
        return WKC020613_fr.layout
    elif pathname == '/quelles_sont_les_activites_des_benevoles_2013':
        return WDV020213_fr.layout
    elif pathname == '/qui_donne_aux_organismes_caritatifs_et_combien_2013':
        return WDA010113_fr.layout
    elif pathname == '/qui_sont_les_benevoles_et_combien_dheures_donnent_ils_2013':
        return WVA020113_fr.layout
    # WDC010513_fr,
    # WKC010613_fr
    # elif pathname == '/HDC0102_13':
    #     return HDC0102_13.layout
    # elif pathname == '/WDC0105_13':
    #     return WDC0105_13.layout
    elif pathname == '/popup':
        return definition.layout

    elif pathname == '/Personnel_remunere_du_secteur_sans_but_lucratif_2021':
        return NSPS_2021_FR_layout
    elif pathname == '/revenus_du_secteur_sans_but_lucratif_2021':
    # elif pathname == '/nonprofit_sector_revenue_2021':
        return NSR_2021_FR_layout
    elif pathname == '/Composition_de_la_population_active_du_secteur_sans_but_lucratif_2021':
    # elif pathname == '/nonprofit_labour_force_composition_2021':
        return NLFC_2021_FR_layout
    elif pathname == '/Role_economique_du_secteur_sans_but_lucratif_2021':
    # elif pathname == '/economic_role_of_the_nonprofit_sector_2021':
        return ERNS_2021_FR_layout
    
    # business conditions stories
    elif pathname == "/liquidite_et_aux_prets_du_cuec_2023":
        return LCLS_2023_FR_layout
    elif pathname == "/l_incidence_des_taux_d_interet_2023":
        return IOIR_2023_FR_layout
    elif pathname == "/perspectives_d_avenir_et_aux_changements_prevus_2023":
        return FOPC_2023_FR_layout
    elif pathname == "/tendances_en_matiere_de_don_2023":
        return DT_2023_FR_layout
    elif pathname == "/obstacles_actuels_2023":
        return CO_2023_FR_layout


    # else:
    #     return dcc.Location(id='redirect', refresh=True, href="https://www.donetbenevolat.ca")

if __name__ == '__main__':
    # app.run_server(debug=True)
    app.run_server(debug=True)
