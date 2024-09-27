from bs4 import BeautifulSoup, Comment
import pytest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def clean_html(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    
    # Remove script and style tags
    for tag in soup(['script', 'style', 'head']):
        tag.decompose()

    # Remove comments
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    # Extract only <div> and <p> elements
    allowed_elements = [
        'div', 
        # 'p'
        ]
    
    #NewCanadiansDonRateAmt > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)
    charts = soup.findAll(
        allowed_elements, 
        class_='dash-graph',
        # id='NewCanadiansDonRateAmt'
        )
    paragraphs = soup.find_all('p')
    content = charts + paragraphs
    result = ''.join([str(tag) for tag in content])

    return result


def page_equality(html_live: str, html_dev: str) -> bool:
    result_live = clean_html(html_live)
    result_dev = clean_html(html_dev)

    return result_live == result_dev


def get_rendered_html(url: str) -> str:
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    selector = '.js-reference-point'

    try:
        driver.get(url) 

        #  # Wait for charts to load
        # WebDriverWait(driver, 3).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        # )

        rendered_html = driver.page_source  
    finally:
        driver.quit()  

    return rendered_html

@pytest.mark.parametrize("slug", [  
    '/Qui_donne_aux_organismes_caritatifs_et_combien_2018',
    '/Comment_donne_t_on_au_Canada_2018', #HDC0102_fr',
    '/Comprendre_les_grands_donateurs_2018', #UTD0103_fr',
    '/Pourquoi_donne_t_on_au_Canada_2018', #/WDC0105_fr',
    '/Qu_est_ce_qui_empeche_de_donner_plus_2018', #WKC0106_fr',
    '/Quels_types_organismes_soutient_on_au_Canada_2018', #WTO0107_fr',
    '/Quelles_sont_les_activites_des_benevoles_2018', #WDV0202_fr',
    '/Qui_sont_les_benevoles_et_combien_heures_donnent_ils_2018', #WVA0201_fr',
    '/Comprendre_les_benevoles_tres_engages_2018', #/UTV0203_fr',
    '/Aide_autrui_et_amelioration_communautaire_2018', #/HOA0204_fr',
    '/Pourquoi_fait_on_du_benevolat_2018', #WDC0205_fr',
    '/Qu_est_ce_qui_empeche_de_faire_du_benevolat_2018', #WKC0206_fr',
    '/A_quels_types_organismes_fait_on_don_de_son_temps_au_Canada_2018', #WKC0206_fr',
    '/dons_dargent_et_benevolat_pour_les_organismes_de_sante_2018', #GAV0304
    '/dons_et_benevolat_pour_les_organismes_du_secteur_de_leducation_2018', #GAV0304
    '/dons_et_benevolat_pour_les_organismes_de_services_sociaux_2018', #GAV0304
    '/dons_et_benevolat_pour_les_organismes_religieux_2018', #GAV0304
    '/dons_et_benevolat_pour_les_organismes_des_arts_et_des_loisirs_2018', #GAV0305
    '/les_dons_et_le_benevolat_des_personnes_nouvellement_arrivees_au_canada_2018', #GAV0306
    '/les_dons_et_le_benevolat_des_jeunes_2018', #GAV0307
    '/les_dons_et_le_benevolat_des_personnes_agees_2018', #GAV0308
    '/comment_donne_t_on_au_canada_2013',
    '/pourquoi_donne_t_on_au_canada_2013',
    '/pourquoi_fait_on_du_benevolat_2013',
    '/qu_est_ce_qui_empeche_de_donner_plus_2013',
    '/qu_est_ce_qui_empeche_de_faire_du_benevolat_2013',
    '/quelles_sont_les_activites_des_benevoles_2013',
    '/qui_donne_aux_organismes_caritatifs_et_combien_2013',
    '/qui_sont_les_benevoles_et_combien_dheures_donnent_ils_2013',
    '/Personnel_remunere_du_secteur_sans_but_lucratif_2021',
    '/revenus_du_secteur_sans_but_lucratif_2021',
    '/Composition_de_la_population_active_du_secteur_sans_but_lucratif_2021',
    '/Role_economique_du_secteur_sans_but_lucratif_2021',
    "/liquidite_et_aux_prets_du_cuec_2023",
    "/l_incidence_des_taux_d_interet_2023",
    "/perspectives_d_avenir_et_aux_changements_prevus_2023",
    "/tendances_en_matiere_de_don_2023",
    "/obstacles_actuels_2023",
      ])
def test_page_equality(slug):
    html_live = get_rendered_html(f'http://app.donetbenevolat.ca/{slug}')
    html_dev = get_rendered_html(f'http://127.0.0.1:8050/{slug}')
    assert page_equality(html_live, html_dev), "Unequal HTML pages"



