from dash import dcc, html
from dash.dependencies import Input, Output
from app import app, server

from apps import (
    Qui_donne_aux_organismes_caritatifs_et_combien_2018,
    Comment_donne_t_on_au_Canada_2018,
    Comprendre_les_grands_donateurs_2018,
    Pourquoi_donne_t_on_au_Canada_2018,
    Qu_est_ce_qui_empeche_de_donner_plus_2018,
    Quels_types_organismes_soutient_on_au_Canada_2018,
    Qui_sont_les_benevoles_et_combien_heures_donnent_ils_2018,
    Quelles_sont_les_activites_des_benevoles_2018,
    Comprendre_les_benevoles_tres_engages_2018,
    Aide_autrui_et_amelioration_communautaire_2018,
    Pourquoi_fait_on_du_benevolat_2018,
    Qu_est_ce_qui_empeche_de_faire_du_benevolat_2018,
    A_quels_types_organismes_fait_on_don_de_son_temps_au_Canada_2018,
    definition,
    GAV0301_fr
    
)

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
        return homepage.layout
    elif pathname == '/Qui_donne_aux_organismes_caritatifs_et_combien_2018': #WDA0101_fr':
        return Qui_donne_aux_organismes_caritatifs_et_combien_2018.layout
    elif pathname == '/Comment_donne_t_on_au_Canada_2018': #HDC0102_fr':
        return Comment_donne_t_on_au_Canada_2018.layout
    elif pathname == '/Comprendre_les_grands_donateurs_2018': #UTD0103_fr':
        return Comprendre_les_grands_donateurs_2018.layout
    elif pathname == '/Pourquoi_donne_t_on_au_Canada_2018': #/WDC0105_fr':
        return Pourquoi_donne_t_on_au_Canada_2018.layout
    elif pathname == '/Qu_est_ce_qui_empeche_de_donner_plus_2018': #WKC0106_fr':
        return Qu_est_ce_qui_empeche_de_donner_plus_2018.layout
    elif pathname == '/Quels_types_organismes_soutient_on_au_Canada_2018': #WTO0107_fr':
        return Quels_types_organismes_soutient_on_au_Canada_2018.layout
    elif pathname == '/Quelles_sont_les_activites_des_benevoles_2018': #WDV0202_fr':
        return Quelles_sont_les_activites_des_benevoles_2018.layout
    elif pathname == '/Qui_sont_les_benevoles_et_combien_heures_donnent_ils_2018': #WVA0201_fr':
        return Qui_sont_les_benevoles_et_combien_heures_donnent_ils_2018.layout
    elif pathname == '/Comprendre_les_benevoles_tres_engages_2018': #/UTV0203_fr':
        return Comprendre_les_benevoles_tres_engages_2018.layout
    elif pathname == '/Aide_autrui_et_amelioration_communautaire_2018': #/HOA0204_fr':
        return Aide_autrui_et_amelioration_communautaire_2018.layout
    elif pathname == '/Pourquoi_fait_on_du_benevolat_2018': #WDC0205_fr':
        return Pourquoi_fait_on_du_benevolat_2018.layout
    elif pathname == '/Qu_est_ce_qui_empeche_de_faire_du_benevolat_2018': #WKC0206_fr':
        return Qu_est_ce_qui_empeche_de_faire_du_benevolat_2018.layout
    elif pathname == '/A_quels_types_organismes_fait_on_don_de_son_temps_au_Canada_2018': #WKC0206_fr':
        return A_quels_types_organismes_fait_on_don_de_son_temps_au_Canada_2018.layout
    elif pathname == '/dons_benevolat_pour_organisems_sante':
        return GAV0301_fr.layout
#     elif pathname == '/GAV0302':
#         return GAV0302.layout
#     elif pathname == '/GAV0303':
#         return GAV0303.layout
#     elif pathname == '/GAV0304':
#         return GAV0304.layout
#     elif pathname == '/GAV0305':
#         return GAV0305.layout
#     elif pathname == '/GAV0306':
#         return GAV0306.layout
#     elif pathname == '/GAV0307':
#         return GAV0307.layout
#     elif pathname == '/GAV0308':
#         return GAV0308.layout
#     elif pathname == '/HDC0102_13':
#         return HDC0102_13.layout
#     elif pathname == '/WDC0105_13':
#         return WDC0105_13.layout
    elif pathname == '/popup':
        return definition.layout
    else:
        return '404'

if __name__ == '__main__':
    # app.run_server(debug=True)
    app.run_server(debug=True)
