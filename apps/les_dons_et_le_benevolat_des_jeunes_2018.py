import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd

from utils.home_button import gen_home_button
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc
import os
import os.path as op

# from utils.graphs.WTO0207_graph_utils import rate_avg_cause, single_vertical_percentage_graph
# from utils.data.WTO0207_data_utils import get_data, process_data, get_region_names, get_region_values
from utils.data.general import get_dataframe

from app import app
from homepage import footer #navbar, footer

####################### Data processing ######################
YouthAvgDonAmt_2018 = get_dataframe("2018-YouthAvgDonAmt_FR.csv")
YouthAvgDonByCause_2018 = get_dataframe("2018-YouthAvgDonByCause_FR.csv")
YouthAvgDonByMeth_2018 = get_dataframe("2018-YouthAvgDonByMeth_FR.csv")
YouthAvgHrs_2018 = get_dataframe("2018-YouthAvgHrs_FR.csv")
YouthAvgHrsByActivity_2018 = get_dataframe("2018-YouthAvgHrsByActivity_FR.csv")
YouthAvgHrsByCause_2018 = get_dataframe("2018-YouthAvgHrsByCause_FR.csv")
YouthAvgHrsCommInvolve_2018 = get_dataframe("2018-YouthAvgHrsCommInvolve_FR.csv")
YouthAvgHrsHelpDirectly_2018 = get_dataframe("2018-YouthAvgHrsHelpDirectly_FR.csv")
YouthBarriers_2018 = get_dataframe("2018-YouthBarriersGiving_FR.csv")
YouthBarriersVol_2018 = get_dataframe("2018-YouthBarriersVol_FR.csv")
YouthCommInvolveRate_2018 = get_dataframe("2018-YouthCommInvolveRate_FR.csv")
YouthDonRateByCause_2018 = get_dataframe("2018-YouthDonRateByCause_FR.csv")
YouthDonRateByMeth_2018 = get_dataframe("2018-YouthDonRateByMeth_FR.csv")
YouthDonRates_2018 = get_dataframe("2018-YouthDonRates_FR.csv")
YouthEfficiencyConcerns_2018 = get_dataframe("2018-YouthEfficiencyConcerns_FR.csv")
YouthHelpDirectlyRate_2018 = get_dataframe("2018-YouthHelpDirectlyRate_FR.csv")
YouthReasonsGiving_2018 = get_dataframe("2018-YouthReasonsGiving_FR.csv")
YouthReasonsVol_2018 = get_dataframe("2018-YouthReasonsVol_FR.csv")
YouthSolicitationConcerns_2018 = get_dataframe("2018-YouthSolicitationConcerns_FR.csv")
YouthVolRateByActivity_2018 = get_dataframe("2018-YouthVolRateByActivity_FR.csv")
YouthVolRateByCause_2018 = get_dataframe("2018-YouthVolRateByCause_FR.csv")
YouthVolRate_2018 = get_dataframe("2018-YouthVolRates_FR.csv")

rates = [YouthBarriers_2018,
         YouthBarriersVol_2018,
         YouthCommInvolveRate_2018,
         YouthDonRateByCause_2018,
         YouthDonRateByMeth_2018,
         YouthDonRates_2018,
         YouthEfficiencyConcerns_2018,
         YouthHelpDirectlyRate_2018,
         YouthReasonsGiving_2018,
         YouthReasonsVol_2018,
         YouthSolicitationConcerns_2018,
         YouthVolRateByActivity_2018,
         YouthVolRateByCause_2018,
         YouthVolRate_2018]

data = [YouthAvgDonAmt_2018,
        YouthAvgDonByCause_2018,
        YouthAvgDonByMeth_2018,
        YouthAvgHrs_2018,
        YouthAvgHrsByActivity_2018,
        YouthAvgHrsByCause_2018,
        YouthAvgHrsCommInvolve_2018,
        YouthAvgHrsHelpDirectly_2018,
        YouthBarriers_2018,
        YouthBarriersVol_2018,
        YouthCommInvolveRate_2018,
        YouthDonRateByCause_2018,
        YouthDonRateByMeth_2018,
        YouthDonRates_2018,
        YouthEfficiencyConcerns_2018,
        YouthHelpDirectlyRate_2018,
        YouthReasonsGiving_2018,
        YouthReasonsVol_2018,
        YouthSolicitationConcerns_2018,
        YouthVolRateByActivity_2018,
        YouthVolRateByCause_2018,
        YouthVolRate_2018]

for i in range(len(rates)):
    rates[i]['Estimate'] = rates[i]['Estimate'] * 100
    rates[i]['CI Upper'] = rates[i]['CI Upper'] * 100


for i in range(len(data)):
    data[i]["Estimate"] = np.where(data[i]["Marker"] == "...", 0, data[i]["Estimate"])
    data[i]["CI Upper"] = np.where(data[i]["Marker"] == "...", 0, data[i]["CI Upper"])
    data[i]["Group"] = np.where(data[i]["Attribute"] == "Unable to determine", "", data[i]["Group"])
    data[i]["Group"] = np.where(data[i]["Attribute"] == "Unknown", "", data[i]["Group"])

    data[i]['Estimate'] = data[i]['Estimate'].round(0).astype(int)
    data[i]["CI Upper"] = data[i]["CI Upper"].round(0).astype(int)
    data[i]['cv'] = data[i]['cv'].round(2)

    # if not data[i]["Attribute"].isna().all():
    #     data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15)
    #     data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)
    #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Do not support<br>cause", "Do not support cause", data[i]["Attribute"])
    #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Do not report<br>barrier", "Do not report barrier", data[i]["Attribute"])
    #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Report<br>barrier", "Report barrier", data[i]["Attribute"])

    data[i]["QuestionText"] = data[i]["QuestionText"].str.wrap(20)
    data[i]["QuestionText"] = data[i]["QuestionText"].replace({'\n': '<br>'}, regex=True)

region_values = np.array(['CA', 'BC', 'AB', 'PR', 'ON', 'QC', 'AT'], dtype=object)
region_names = np.array(['Canada',
                         'British Columbia',
                         'Alberta',
                         'Prairie Provinces (SK, MB)',
                         'Ontario',
                         'Quebec',
                         'Atlantic Provinces (NB, NS, PE, NL)'], dtype=str)


###################### App layout ######################
navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                # dcc.Link("Home", href="/")
                dbc.NavLink("À propos", href="https://www.donetbenevolat.ca/",external_link=True)
            ),
            dbc.NavItem(
                dbc.NavLink("EN", href="http://app.givingandvolunteering.ca/giving_and_volunteering_by_youth",external_link=True)
            ),
        ],
        brand="Centre Canadien de Connaissances sur les Dons et le Bénévolat",
        brand_href="/",
        color="#4B161D",
        dark=True,
        sticky='top'
    )
home_button = gen_home_button()
marginTop = 20


layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1('Les dons et le bénévolat des jeunes (2018)'),
                        #html.Span(
                            #'David Lasby',
                            #className='meta'
                     #   )
                        ],
                        className='post-heading'
                    ),
                    className='col-md-10 col-lg-8 mx-auto position-relative'
                )
            )
        ),
    ],
        # className='masthead'
        className="bg-secondary text-white text-center pt-4",
    ),
    # Note: filters put in separate container to make floating element later
    dbc.Container([
        home_button,
        dbc.Row(
           dbc.Col(
               html.Div([
                   "Sélectionnez une région:",
                   dcc.Dropdown(
                       id='region-selection',
                       options=[{'label': region_names[i], 'value': region_values[i]} for i in range(len(region_values))],
                       value='CA',
                       ),
                    html.Br(),
                ],className="m-2 p-2"),
            ),id='sticky-dropdown'),
    ],className='sticky-top bg-light mb-2', fluid=True),
   dbc.Container([
       dbc.Row([
            html.Div([
                html.H3('Dons'),
                dcc.Markdown("""
                D’après les données de l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, il existe une forte corrélation entre l’âge et les comportements en matière de dons. Au Canada, les personnes âgées de 15 à 24 ans sont moins enclines à donner et donnent moins d’argent, en moyenne, que les personnes âgées de 25 à 34 ans qui, elles aussi, sont moins enclines à donner et donnent moins d’argent, en moyenne, que les personnes âgées de 35 ans ou plus. C’est vrai pour les dons aux causes laïques et aux causes religieuses. Les personnes âgées de 15 à 24 ans sont 3 fois plus susceptibles de donner de l’argent à des causes laïques qu’à des causes religieuses tandis que celles âgées de 25 à 34 ans sont trois fois et demie plus susceptibles de faire de même. Ces deux groupes, en revanche, donnent beaucoup plus d’argent, en moyenne, aux causes religieuses. 
                """
                ),
                # Donation rate and average donation amount
                dcc.Graph(id='YouthDonRateAmt', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Les dons selon la cause'),
                dcc.Markdown("""
                Les jeunes personnes ont tendance à donner le plus aux organismes de services sociaux, suivis par les organismes de santé et les congrégations religieuses, qui sont aussi les causes les plus populaires chez les personnes plus âgées. 
                """),
                # Donation rate by cause
                dcc.Graph(id='YouthDonRateByCause', style={'marginTop': marginTop}), 
                dcc.Markdown("""
                Les jeunes personnes donnent moins, en moyenne, aux causes qu’elles soutiennent, ce qui est vrai pour toutes les causes, bien que, dans de nombreux cas, les différences ne soient pas statistiquement significatives. 
                """),
                # Average amount donated by cause
                dcc.Graph(id='YouthAvgAmtByCause', style={'marginTop': marginTop}), 
            ], className='col-md-10 col-lg-8 mx-auto'),
            html.Div([
                html.H4('Méthodes de dons'),
                dcc.Markdown("""
                Les personnes plus jeunes ont moins tendance à donner par toutes les méthodes que les personnes plus âgées. Les différences sont cependant plus importantes pour certaines méthodes que pour d’autres. Elles sont particulièrement importantes pour les dons par courrier, à la mémoire de quelqu’un, pour parrainer quelqu’un et à la suite d’une sollicitation au porte-à-porte ou dans un lieu de culte. Les personnes âgées de 15 à 34 ans sont nettement moins enclines à donner par ces méthodes que celles âgées de 35 ans ou plus. 
                """),
                # Donation rate by method
                dcc.Graph(id='YouthDonRateByMeth', style={'marginTop': marginTop}), 
                dcc.Markdown("""
                Le montant moyen des dons des personnes âgées de 15 à 34 ans est le plus élevé quand elles donnent de l’argent dans les lieux de culte et de leur propre initiative.
                """),
                # Average amount donated by method
                dcc.Graph(id='YouthAvgAmtByMeth', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Motivations des dons'),
                dcc.Markdown("""
                En général, les personnes plus jeunes donnent de l’argent pour les mêmes raisons que les personnes plus âgées, la conviction du bien-fondé de la cause et la compassion envers les personnes dans le besoin étant les deux principales motivations des dons pour tous les groupes d’âge. Il existe cependant quelques différences. La différence la plus importante est liée aux crédits d’impôt que les personnes plus jeunes ont moins tendance à citer pour justifier leurs dons que les personnes plus âgées. Les personnes de 15 à 24 ans sont également moins susceptibles de déclarer donner de l’argent parce que la cause les touche personnellement ou en raison de leurs croyances spirituelles que les personnes âgées de 35 ans ou plus.
                """),
                # Motivations for donating
                dcc.Graph(id='YouthMotivations', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Freins à donner davantage'),
                dcc.Markdown("""
                Les personnes plus jeunes ont davantage tendance que les personnes plus âgées à déclarer ne pas avoir donné plus parce qu’elles n’en avaient pas les moyens, qu’elles avaient préféré faire du bénévolat ou qu’elles ne savaient pas où s’adresser pour donner de l’argent. En revanche, elles ont moins tendance que les personnes plus âgées à déclarer ne pas avoir donné plus parce qu’elles étaient satisfaites du montant de leurs dons, qu’elles ne pensaient pas que leur argent serait utilisé avec efficience, qu’elles avaient donné directement aux personnes dans le besoin, qu’elles n’aimaient pas la méthode de sollicitation ou qu’elles ne pensaient pas que le crédit d’impôt était suffisant. 
                """),
                # Barriers to donating more
                dcc.Graph(id='YouthBarriers', style={'marginTop': marginTop}), 
                html.Div([
                    html.H5('Préoccupations relatives à l’efficience'),
                    dcc.Markdown("""
                    La moindre préoccupation des personnes plus jeunes à l’égard de l’utilisation de leurs dons semble principalement liée à leur moindre préoccupation à l’égard des coûts des collectes de fonds.
                    """),
                    # Reasons for concern about efficiency
                    dcc.Graph(id='YouthEfficiency', style={'marginTop': marginTop}), 
                    ]),
                html.Div([
                    html.H5('Préoccupations relatives aux sollicitations'),
                    dcc.Markdown("""
                    La moindre préoccupation des personnes plus jeunes à l’égard des méthodes de sollicitation semble principalement liée à leur moindre préoccupation à l’égard de l’heure des sollicitations.
                    """),
                    # Reasons for disliking solicitations
                    dcc.Graph(id='YouthSolicitations', style={'marginTop': marginTop}), 
                    ]),
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
       dbc.Row([
            html.Div([
                html.H3('Bénévolat'),
                dcc.Markdown("""
                D’après les données de l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, les personnes âgées de 15 à 24 ans au Canada ont plus tendance à faire du bénévolat que les personnes plus âgées, mais en faisant don de moins d’heures de leur temps. À l’échelle nationale, les personnes canadiennes âgées de 15 à 24 ans qui font du bénévolat (52 % de ce groupe d’âge) lui consacrent en moyenne de 86 heures par année, tandis que les personnes canadiennes âgées de 35 ans ou plus qui font du bénévolat (40 % de ce groupe d’âge) lui consacrent en moyenne 145 heures. La corrélation est moins forte entre l’âge et la probabilité d’aider autrui par ses propres moyens (c.-à-d. en dehors d’un groupe ou d’un organisme) ou de pratiquer d’autres formes d’engagement communautaire. Les personnes plus jeunes participent à ces activités à une fréquence comparable à celle des personnes plus âgées, tout en y consacrant cependant moins d’heures en moyenne.
                """),
                # Rates and average hours devoted to volunteering, helping others and community engagement
                dcc.Graph(id='YouthVolRateVolAmt', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Bénévolat selon la cause'),
                dcc.Markdown("""
                Tout comme leurs homologues d’un âge plus avancé, c’est pour les organismes de services sociaux, d’éducation et de recherche, des sports et des loisirs et pour les congrégations religieuses que les personnes âgées de 15 à 34 ans sont les plus enclines à faire du bénévolat. Les personnes plus jeunes sont plus enclines à faire du bénévolat pour les organismes d’éducation et de recherche et pour les universités et les collèges que les personnes plus âgées, ce qui constitue la principale différence entre ces deux groupes d’âge. 
                """),
                # Volunteer rate by cause
                dcc.Graph(id='YouthVolRateByCause', style={'marginTop': marginTop}), 
                dcc.Markdown("""
                En raison de la grande variation des heures de bénévolat, la prudence est de rigueur pour interpréter les données. Par exemple, bien qu’il semble que, à l’échelle nationale, les bénévoles plus jeunes font don d’un plus grand nombre d’heures de leur temps aux organismes environnementaux et aux universités et aux collèges, ces différences ne sont pas statistiquement significatives. En revanche, les bénévoles plus jeunes font don d’un nombre d’heures de bénévolat significativement inférieur aux congrégations religieuses et aux organismes spécialisés dans le droit, le plaidoyer et la politique.
                """),
                # Average hours volunteered by cause
                dcc.Graph(id='YouthAvgHrsByCause', style={'marginTop': marginTop}), 
            ], className='col-md-10 col-lg-8 mx-auto'),
            html.Div([
                html.H4('Activités des bénévoles'),
                dcc.Markdown("""
                L’âge influe sur le type d’activités bénévoles. Les bénévoles plus jeunes ont plus tendance à organiser des activités ou des événements, à enseigner ou à mentorer, à entraîner, à arbitrer ou à jouer un autre rôle officiel dans le domaine sportif que les personnes plus âgées. Les bénévoles plus jeunes ont également moins tendance à siéger à des comités ou à des conseils d’administration, à offrir des soins ou du soutien en santé, à faire du travail de bureau ou à conduire bénévolement. 
                """),
                # Volunteer rate by activity
                dcc.Graph(id='YouthVolRateByActivity', style={'marginTop': marginTop}), 
                dcc.Markdown("""
                En moyenne, c’est aux activités d’enseignement, de mentorat, d’entraînement, d’arbitrage ou de présidence que les personnes canadiennes âgées de 15 à 34 ans consacrent le plus d’heures de bénévolat. Bien que les bénévoles plus jeunes consacrent moins de temps à la majorité des activités que les personnes plus âgées, la plupart des différences ne sont pas statistiquement significatives. En revanche, les bénévoles plus jeunes consacrent un nombre d’heures significativement inférieur aux activités d’entretien, de réparation, de construction ou à conduire bénévolement que les personnes plus âgées. 
                """),
                # Average hours volunteered by activity
                dcc.Graph(id='YouthAvgHrsByActivity', style={'marginTop': marginTop}), 
            
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Motivations du bénévolat'),
                dcc.Markdown("""
                Les personnes plus jeunes ont tendance à faire du bénévolat pour les mêmes raisons que les personnes plus âgées. Par exemple, apporter une contribution à la communauté et utiliser leurs compétences sont les deux principales motivations du bénévolat pour tous les groupes d’âge. Cela dit, il existe plusieurs différences. Les personnes âgées de 15 à 24 ans sont plus enclines à faire du bénévolat pour améliorer leurs possibilités d’emploi ou pour prendre conscience de leurs points forts que les personnes âgées de 25 à 34 ans qui sont, elles aussi, plus enclines à faire du bénévolat pour ces mêmes raisons que les personnes âgées de 35 ans ou plus. Les bénévoles les plus jeunes ont également plus tendance que les personnes plus âgées à faire du bénévolat pour utiliser leurs compétences ou parce que leurs proches sont des bénévoles. 
                """),
                # Motivations for volunteering
                dcc.Graph(id='YouthVolMotivations', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Freins au bénévolat'),
                dcc.Markdown("""
                Le manque de temps et l’impossibilité de s’engager à long terme pour faire du bénévolat sont les obstacles les plus fréquents pour tous les groupes d’âge. Les bénévoles plus jeunes ont moins tendance à limiter leur bénévolat parce qu’ils pensent avoir déjà donné suffisamment de leur temps, ou parce que plus de bénévolat ne présente aucun intérêt pour eux ou encore à cause de problèmes de santé. Les bénévoles plus jeunes ont plus tendance à limiter leur bénévolat faute de sollicitation ou de savoir comment s’impliquer. Les bénévoles de 15 à 24 ans ont relativement moins tendance à faire des dons de préférence au bénévolat, vraisemblablement en raison de leurs ressources financières souvent inférieures.  
                """),
                # Barriers to volunteering more
                dcc.Graph(id='YouthVolBarriers', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Aide directe d’autrui '),
                dcc.Markdown("""
                Les jeunes aident autrui directement de préférence en cuisinant, en faisant le ménage ou d’autres tâches à la maison, en offrant des soins liés à la santé ou personnels, ou en magasinant, en conduisant ou en accompagnant d’autres personnes à des magasins ou à des rendez-vous. Les jeunes personnes sont plus enclines à enseigner, à entraîner ou à aider à la lecture et moins enclines à apporter leur aide pour des tâches administratives ou les déclarations d’impôt que les personnes plus âgées. Les personnes âgées de 15 à 24 ans sont également moins susceptibles d’apporter leur aide en cuisinant, en faisant le ménage ou d’autres corvées ménagères que celles âgées de 25 à 34 ans. 
                """),
                # Methods of helping others directly
                dcc.Graph(id='YouthRateHelpDirect', style={'marginTop': marginTop}),
                dcc.Markdown("""
                Les jeunes consacrent le plus de temps en moyenne, à aider d’autres personnes en offrant des soins liés à la santé ou personnels, en cuisinant, en faisant le ménage ou d’autres corvées ménagères. En moyenne, cependant, les personnes âgées de 15 à 34 ans consacrent moins de temps à ces activités et à d’autres formes d’aide directe que les personnes âgées de 35 ans ou plus. 
                """),
                # Average hours devoted to means of helping others directly
                dcc.Graph(id='YouthHrsHelpDirect', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Engagement communautaire'),
                dcc.Markdown("""
                Sur le plan des activités visant à améliorer la communauté, les personnes âgées de moins de 35 ans au Canada sont plus enclines que les personnes âgées de 35 ans ou plus à créer ou à diffuser de l’information pour sensibiliser les autres personnes à un enjeu. Les personnes âgées de 15 à 24 ans ont moins tendance à participer à des réunions publiques que celles âgées de 25 ans ou plus. Les jeunes personnes sont à peu près aussi enclines à participer aux autres types d’activités communautaires que les personnes plus âgées.
                """),
                # Types of community engagement
                dcc.Graph(id='YouthRateCommInvolve', style={'marginTop': marginTop}), 
                dcc.Markdown("""
                L’âge n’a pas une incidence significative sur le nombre moyen d’heures consacrées aux diverses formes d’engagement communautaire au Canada.
                """),
                # Average hours devoted to forms of community engagement
                dcc.Graph(id='YouthHrsCommInvolve', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
   ]),
   footer
])


################## CALLBACKS ##################

def triple_horizontal_rate_avg(dff_1, dff_2, name1, name2, name3, title, giving=True):
    dff_1['Text'] = np.select([dff_1["Marker"] == "*", dff_1["Marker"] == "...", pd.isnull(dff_1["Marker"])],
                             [dff_1.Estimate.map(str) + "%*", "...", dff_1.Estimate.map(str)+"%"])
    dff_1['HoverText'] = np.select([dff_1["Marker"] == "*",
                                   dff_1["Marker"] == "...",
                                   pd.isnull(dff_1["Marker"])],
                                  ["Estimate: " + dff_1.Estimate.map(str) + "% ± " + (dff_1["CI Upper"] - dff_1["Estimate"]).map(str) + "%<br><b>Use with caution</b>",
                                   "Estimate Suppressed",
                                   "Estimate: " + dff_1.Estimate.map(str) + "% ± " + (dff_1["CI Upper"] - dff_1["Estimate"]).map(str)+"%"])

    if giving:
        dff_2['Text'] = np.select([dff_2["Marker"] == "*", dff_2["Marker"] == "...", pd.isnull(dff_2["Marker"])],
                                  ["$" + dff_2.Estimate.map(str) + "*", "...", "$" + dff_2.Estimate.map(str)])
        dff_2['HoverText'] = np.select([dff_2["Marker"] == "*",
                                        dff_2["Marker"] == "...",
                                        pd.isnull(dff_2["Marker"])],
                                       ["Estimate: $" + dff_2.Estimate.map(str) + " ± $" + (dff_2["CI Upper"] - dff_2["Estimate"]).map(str) + "<br><b>Use with caution</b>",
                                        "Estimate Suppressed",
                                        "Estimate: $" + dff_2.Estimate.map(str) + " ± $" + (dff_2["CI Upper"] - dff_2["Estimate"]).map(str)])
        dff_1['QuestionText'] = np.select([dff_1["QuestionText"] == 'Donor flag', dff_1["QuestionText"] == 'Secular donor flag', dff_1["QuestionText"] == 'Religious donor flag'],
                                         ["Le don en général", "Dons séculaires", "Dons religieux"])
        dff_2['QuestionText'] = np.select([dff_2["QuestionText"] == 'Total donation<br>amount', dff_2["QuestionText"] == 'Secular donation<br>amount', dff_2["QuestionText"] == 'Religious donation<br>amount'],
                                 ["Le don en général", "Dons séculaires", "Dons religieux"])
    else:
        dff_2['Text'] = np.select([dff_2["Marker"] == "*", dff_2["Marker"] == "...", pd.isnull(dff_2["Marker"])],
                                  [dff_2.Estimate.map(str) + "*", "...", dff_2.Estimate.map(str)])
        dff_2['HoverText'] = np.select([dff_2["Marker"] == "*",
                                        dff_2["Marker"] == "...",
                                        pd.isnull(dff_2["Marker"])],
                                       ["Estimate: " + dff_2.Estimate.map(str) + " ± " + (dff_2["CI Upper"] - dff_2["Estimate"]).map(str) + "<br><b>Use with caution</b>",
                                        "Estimate Suppressed",
                                        "Estimate: " + dff_2.Estimate.map(str) + " ± " + (dff_2["CI Upper"] - dff_2["Estimate"]).map(str)])
        dff_1['QuestionText'] = np.select([dff_1["QuestionText"] == 'Volunteer flag', dff_1["QuestionText"] == 'Direct help flag', dff_1["QuestionText"] == 'Community<br>involvement flag'],
                                          ["Volontariat", "Aider les autres", "Engagement communautaire"])
        dff_2['QuestionText'] = np.select([dff_2["QuestionText"] == 'Total formal<br>volunteer hours', dff_2["QuestionText"] == 'Total hours spent<br>helping directly', dff_2["QuestionText"] == 'Total hours spent on<br>community<br>involvement'],
                                          ["Volontariat", "Aider les autres", "Engagement communautaire"])


    dff1 = dff_1[dff_1['Attribute'] == name1]

    dff2 = dff_1[dff_1['Attribute'] == name2]

    dff3 = dff_1[dff_1['Attribute'] == name3]

    dff4 = dff_2[dff_2['Attribute'] == name1]

    dff5 = dff_2[dff_2['Attribute'] == name2]

    dff6 = dff_2[dff_2['Attribute'] == name3]

    fig = go.Figure()

    fig.add_trace(go.Bar(y=dff1['CI Upper'],
                         x=dff1['QuestionText'],
                         error_y=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=2,
                         yaxis='y2'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff2['CI Upper'],
                         x=dff2['QuestionText'],
                         error_y=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=1,
                         yaxis='y2'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff3['CI Upper'],
                         x=dff3['QuestionText'],
                         error_y=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=3,
                         yaxis='y2'
                         ),
                  )

    fig.add_trace(go.Bar(y=[0, 0, 0],
                         x=dff6['QuestionText'],
                         width=[0.5,0.5,0.5],
                         cliponaxis=False,
                         showlegend=False,
                         offsetgroup=4,
                         yaxis='y1'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff4['CI Upper'],
                         x=dff4['QuestionText'],
                         error_y=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=5,
                         yaxis='y1'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff5['CI Upper'],
                         x=dff5['QuestionText'],
                         error_y=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=6,
                         yaxis='y1'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff6['CI Upper'],
                         x=dff6['QuestionText'],
                         error_y=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=7,
                         yaxis='y1'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff1['Estimate'],
                         x=dff1['QuestionText'],
                         error_y=None,
                         hovertext=dff1['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#c8102e"),
                         text=dff1['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         name=name1,
                         offsetgroup=2,
                         yaxis='y2'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff2['Estimate'],
                         x=dff2['QuestionText'],
                         error_y=None,
                         hovertext=dff2['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#7BAFD4"),
                         text=dff2['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         name=name2,
                         offsetgroup=1, yaxis='y2'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff3['Estimate'],
                         x=dff3['QuestionText'],
                         error_y=None,
                         hovertext=dff3['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#50a684"),
                         text=dff3['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         name=name3,
                         offsetgroup=3, yaxis='y2'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff4['Estimate'],
                         x=dff4['QuestionText'],
                         error_y=None,
                         hovertext=dff4['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#c8102e"),
                         text=dff4['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         showlegend=False,
                         offsetgroup=5,
                         yaxis='y1'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff5['Estimate'],
                         x=dff5['QuestionText'],
                         error_y=None,
                         hovertext =dff5['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#7BAFD4"),
                         text=dff5['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         showlegend=False,
                         offsetgroup=6,
                         yaxis='y1'
                         ),
                  )

    fig.add_trace(go.Bar(y=dff6['Estimate'],
                         x=dff6['QuestionText'],
                         error_y=None,
                         hovertext=dff6['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#50a684"),
                         text=dff6['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         showlegend=False,
                         offsetgroup=7,
                         yaxis='y1'
                         ),
                  )


    y2 = go.layout.YAxis(overlaying='y',
                         side='left',
                         autorange = False,
                         range = [0, 1.25*max(np.concatenate([dff1["CI Upper"], dff2["CI Upper"], dff3["CI Upper"]]))])
    y1 = go.layout.YAxis(overlaying='y',
                         side='right',
                         autorange = False,
                         range = [0, 1.25*max(np.concatenate([dff4["CI Upper"], dff5["CI Upper"], dff6["CI Upper"]]))])

    fig.update_layout(title={'text': title,
                             'y': 0.99},
                      margin={'l': 30, 'b': 30, 'r': 10, 't': 10},
                      height=600,
                      plot_bgcolor='rgba(0, 0, 0, 0)',
                      bargroupgap=0.05,
                      yaxis2=y2,
                      yaxis1=y1,
                      barmode="group",
                      legend={'orientation': 'h', 'yanchor': "bottom", "xanchor": "center", "x": 0.5},
                      updatemenus=[
                          dict(
                              type = "buttons",
                              xanchor='right',
                              x = 1.2,
                              y = 0.5,
                              buttons=list([
                                  dict(
                                      args=[{"error_y": [None, None, None, None, None, None, None, None, None, None, None, None, None],
                                             "text": [None, None, None, None, None, None, None, dff1['Text'], dff2['Text'], dff3['Text'], dff4['Text'], dff5['Text'], dff6['Text']]}],
                                      label="Réinitialiser",
                                      method="restyle"
                                  ),
                                  dict(
                                      args=[{"error_y": [None, None, None, None, None, None, None,
                                                         dict(type="data", array=dff1["CI Upper"]-dff1["Estimate"], color="#424242", thickness=1.5),
                                                         dict(type="data", array=dff2["CI Upper"]-dff2["Estimate"], color="#424242", thickness=1.5),
                                                         dict(type="data", array=dff3["CI Upper"]-dff3["Estimate"], color="#424242", thickness=1.5),
                                                         dict(type="data", array=dff4["CI Upper"]-dff4["Estimate"], color="#424242", thickness=1.5),
                                                         dict(type="data", array=dff5["CI Upper"]-dff5["Estimate"], color="#424242", thickness=1.5),
                                                         dict(type="data", array=dff6["CI Upper"]-dff6["Estimate"], color="#424242", thickness=1.5)],
                                             "text": [dff1['Text'], dff2['Text'], dff3['Text'], None, dff4['Text'], dff5['Text'], dff6['Text'], None, None, None, None, None, None]}],
                                      label="Intervalles de confiance",
                                      method="restyle"
                                  )
                              ]),
                          ),
                      ]
                      )

    fig.update_yaxes(showgrid=False,
                     showticklabels=False)
    fig.update_xaxes(ticklabelposition="outside top",
                     tickfont=dict(size=12))

    markers = pd.concat([dff1["Marker"], dff2["Marker"], dff3["Marker"], dff4["Marker"], dff5["Marker"], dff6["Marker"]])
    if markers.isin(["*"]).any() and markers.isin(["..."]).any():
        fig.update_layout(margin={'l': 40, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="*<i>Use with caution<br>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    elif markers.isin(["*"]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="*<i>Use with caution</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    elif markers.isin(["..."]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="<i>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    else:
        fig.update_layout(margin={'l': 30, 'b': 30, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.32, x=1.2, align="left", showarrow=False)])

    return fig


def vertical_double_graph(dff, title, name1, name2, type, seniors=False):
    if type == "percent":
        dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
                                [dff.Estimate.map(str) + "%" + "*", "...", dff.Estimate.map(str) + "%"])
        dff['HoverText'] = np.select([dff["Marker"] == "*",
                                      dff["Marker"] == "...",
                                      pd.isnull(dff["Marker"])],
                                     ["Estimate: " + dff.Estimate.map(str) + "% ± " + (dff["CI Upper"] - dff["Estimate"]).map(str) + "%<br><b>Use with caution</b>",
                                      "Estimate Suppressed",
                                      "Estimate: " + dff.Estimate.map(str) + "% ± " + (dff["CI Upper"] - dff["Estimate"]).map(str) + "%"])
    elif type == "dollar":
        dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
                                ["$" + dff.Estimate.map(str) + "*", "...", "$" + dff.Estimate.map(str)])
        dff['HoverText'] = np.select([dff["Marker"] == "*",
                                      dff["Marker"] == "...",
                                      pd.isnull(dff["Marker"])],
                                     ["Estimate: $" + dff.Estimate.map(str) + " ± $" + (dff["CI Upper"] - dff["Estimate"]).map(str) + "<br><b>Use with caution</b>",
                                      "Estimate Suppressed",
                                      "Estimate: $" + dff.Estimate.map(str) + " ± $" + (dff["CI Upper"] - dff["Estimate"]).map(str)])

    elif type == "hours":
        dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
                                [dff.Estimate.map(str) + "*", "...", dff.Estimate.map(str)])
        dff['HoverText'] = np.select([dff["Marker"] == "*",
                                      dff["Marker"] == "...",
                                      pd.isnull(dff["Marker"])],
                                     ["Estimate: " + dff.Estimate.map(str) + " ± " + (dff["CI Upper"] - dff["Estimate"]).map(str) + "<br><b>Use with caution</b>",
                                      "Estimate Suppressed",
                                      "Estimate: " + dff.Estimate.map(str) + " ± " + (dff["CI Upper"] - dff["Estimate"]).map(str)])

    dff1 = dff[dff['Attribute'] == name1]

    dff2 = dff[dff['Attribute'] == name2]

    fig = go.Figure()

    fig.add_trace(go.Bar(x=dff1['CI Upper'],
                         y=dff1['QuestionText'],
                         orientation="h",
                         error_x=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=2
                         ),
                  )

    fig.add_trace(go.Bar(x=dff2['CI Upper'],
                         y=dff2['QuestionText'],
                         orientation="h",
                         error_x=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=1
                         ),
                  )

    fig.add_trace(go.Bar(x=dff1['Estimate'],
                         y=dff1['QuestionText'],
                         orientation="h",
                         error_x=None,
                         hovertext=dff1['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#c8102e"),
                         text=dff1['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         name=name1,
                         offsetgroup=2
                         ),
                  )

    fig.add_trace(go.Bar(x=dff2['Estimate'],
                         y=dff2['QuestionText'],
                         orientation="h",
                         error_x=None,
                         hovertext=dff2['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#7BAFD4"),
                         text=dff2['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         name=name2,
                         offsetgroup=1
                         ),
                  )

    fig.update_layout(title={'text': title,
                             'y': 0.97},
                      margin={'l': 30, 'b': 30, 'r': 10, 't': 10},
                      height=600,
                      plot_bgcolor='rgba(0, 0, 0, 0)',
                      bargroupgap=0.05,
                      barmode="group",
                      legend={'orientation': 'h', 'yanchor': "bottom"},
                      updatemenus=[
                          dict(
                              type="buttons",
                              xanchor='right',
                              x=1.2,
                              y=0.5,
                              buttons=list([
                                  dict(
                                      args=[{"error_x": [None, None, None, None],
                                             "text": [None, None, dff1['Text'], dff2['Text']]}],
                                      label="Réinitialiser",
                                      method="restyle"
                                  ),
                                  dict(
                                      args=[{"error_x": [None, None, dict(type="data", array=dff1["CI Upper"] - dff1["Estimate"], color="#424242", thickness=1.5), dict(type="data", array=dff2["CI Upper"] - dff2["Estimate"], color="#424242", thickness=1.5)],
                                             "text": [dff1['Text'], dff2['Text'], None, None]}],
                                      label="Intervalles de confiance",
                                      method="restyle"
                                  )
                              ]),
                          ),
                      ]
                      )

    if seniors:
        array = dff2.sort_values(by="Estimate", ascending=False)["QuestionText"]
    else:
        array = dff1.sort_values(by="Estimate", ascending=False)["QuestionText"]
    fig.update_xaxes(showgrid=False,
                     showticklabels=False,
                     autorange=False,
                     range=[0, 1.25 * max(np.concatenate([dff1["CI Upper"], dff2["CI Upper"]]))])
    fig.update_yaxes(autorange="reversed",
                     ticklabelposition="outside top",
                     tickfont=dict(size=11),
                     categoryorder='array',
                     categoryarray=array)

    markers = pd.concat([dff1["Marker"], dff2["Marker"]])
    if markers.isin(["*"]).any() and markers.isin(["..."]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="*<i>Use with caution<br>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    elif markers.isin(["*"]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="*<i>Use with caution</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    elif markers.isin(["..."]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="<i>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    else:
        fig.update_layout(margin={'l': 30, 'b': 30, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False)])

    return fig


def triple_vertical_graphs_pops(dff, title, name1, name2, name3, type):
    if type == "percent":
        dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
                                [dff.Estimate.map(str)+"%"+"*", "...", dff.Estimate.map(str)+"%"])
        dff['HoverText'] = np.select([dff["Marker"] == "*",
                                      dff["Marker"] == "...",
                                      pd.isnull(dff["Marker"])],
                                     ["Estimate: "+dff.Estimate.map(str)+"% ± "+(dff["CI Upper"] - dff["Estimate"]).map(str)+"%<br><b>Use with caution</b>",
                                      "Estimate Suppressed",
                                      "Estimate: "+dff.Estimate.map(str)+"% ± "+(dff["CI Upper"] - dff["Estimate"]).map(str)+"%"])
    elif type == "hours":
        dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
                                [dff.Estimate.map(str)+"*", "...", dff.Estimate.map(str)])
        dff['HoverText'] = np.select([dff["Marker"] == "*",
                                      dff["Marker"] == "...",
                                      pd.isnull(dff["Marker"])],
                                     ["Estimate: "+dff.Estimate.map(str)+" ± "+(dff["CI Upper"] - dff["Estimate"]).map(str)+"<br><b>Use with caution</b>",
                                      "Estimate Suppressed",
                                      "Estimate: "+dff.Estimate.map(str)+" ± "+(dff["CI Upper"] - dff["Estimate"]).map(str)])
    elif type == "dollar":
        dff['Text'] = np.select([dff["Marker"] == "*", dff["Marker"] == "...", pd.isnull(dff["Marker"])],
                                ["$"+dff.Estimate.map(str)+"*", "...", "$"+dff.Estimate.map(str)])
        dff['HoverText'] = np.select([dff["Marker"] == "*",
                                      dff["Marker"] == "...",
                                      pd.isnull(dff["Marker"])],
                                     ["Estimate: $"+dff.Estimate.map(str)+" ± $"+(dff["CI Upper"] - dff["Estimate"]).map(str)+"<br><b>Use with caution</b>",
                                      "Estimate Suppressed",
                                      "Estimate: $"+dff.Estimate.map(str)+" ± $"+(dff["CI Upper"] - dff["Estimate"]).map(str)])

    dff1 = dff[dff['Attribute'] == name1]

    dff2 = dff[dff['Attribute'] == name2]

    dff3 = dff[dff['Attribute'] == name3]


    fig = go.Figure()

    fig.add_trace(go.Bar(x=dff1['CI Upper'],
                         y=dff1['QuestionText'],
                         orientation="h",
                         error_x=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=2
                         ),
                  )

    fig.add_trace(go.Bar(x=dff2['CI Upper'],
                         y=dff2['QuestionText'],
                         orientation="h",
                         error_x=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=1
                         ),
                  )

    fig.add_trace(go.Bar(x=dff3['CI Upper'],
                         y=dff3['QuestionText'],
                         orientation="h",
                         error_x=None,
                         marker=dict(color="#FFFFFF", line=dict(color="#FFFFFF")),
                         showlegend=False,
                         hoverinfo="skip",
                         text=None,
                         textposition="outside",
                         cliponaxis=False,
                         offsetgroup=3
                         ),
                  )

    fig.add_trace(go.Bar(x=dff1['Estimate'],
                         y=dff1['QuestionText'],
                         orientation="h",
                         error_x=None,
                         hovertext=dff1['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#c8102e"),
                         text=dff1['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         name=name1,
                         offsetgroup=2
                         ),
                  )

    fig.add_trace(go.Bar(x=dff2['Estimate'],
                         y=dff2['QuestionText'],
                         orientation="h",
                         error_x=None,
                         hovertext =dff2['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#7BAFD4"),
                         text=dff2['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         name=name2,
                         offsetgroup=1
                         ),
                  )

    fig.add_trace(go.Bar(x=dff3['Estimate'],
                         y=dff3['QuestionText'],
                         orientation="h",
                         error_x=None,
                         hovertext=dff3['HoverText'],
                         hovertemplate="%{hovertext}",
                         hoverlabel=dict(font=dict(color="white")),
                         hoverinfo="text",
                         marker=dict(color="#50a684"),
                         text=dff3['Text'],
                         textposition='outside',
                         cliponaxis=False,
                         name=name3,
                         offsetgroup=3
                         ),
                  )

    fig.update_layout(title={'text': title,
                             'y': 0.99},
                      margin={'l': 30, 'b': 30, 'r': 10, 't': 10},
                      height=600,
                      plot_bgcolor='rgba(0, 0, 0, 0)',
                      bargroupgap=0.05,
                      barmode="group",
                      legend={'orientation': 'h', 'yanchor': "bottom"},
                      updatemenus=[
                          dict(
                              type = "buttons",
                              xanchor='right',
                              x = 1.2,
                              y = 0.5,
                              buttons=list([
                                  dict(
                                      args=[{"error_x": [None, None, None, None, None, None],
                                             "text": [None, None, None, dff1['Text'], dff2['Text'], dff3['Text']]}],
                                      label="Réinitialiser",
                                      method="restyle"
                                  ),
                                  dict(
                                      args=[{"error_x": [None, None, None, dict(type="data", array=dff1["CI Upper"]-dff1["Estimate"], color="#424242", thickness=1.5),
                                                         dict(type="data", array=dff2["CI Upper"]-dff2["Estimate"], color="#424242", thickness=1.5),
                                                         dict(type="data", array=dff3["CI Upper"]-dff3["Estimate"], color="#424242", thickness=1.5)],
                                             "text": [dff1['Text'], dff2['Text'], dff3['Text'], None, None, None]}],
                                      label="Intervalles de confiance",
                                      method="restyle"
                                  )
                              ]),
                          ),
                      ]
                      )

    fig.update_xaxes(showgrid=False,
                     showticklabels=False,
                     autorange=False,
                     range=[0, 1.25*max(np.concatenate([dff1["CI Upper"], dff2["CI Upper"], dff3["CI Upper"]]))])
    fig.update_yaxes(autorange="reversed",
                     ticklabelposition="outside top",
                     tickfont=dict(size=11),
                     categoryorder='array',
                     categoryarray=dff2.sort_values(by="Estimate", ascending=False)["QuestionText"])

    markers = pd.concat([dff1["Marker"], dff2["Marker"], dff3["Marker"]])
    if markers.isin(["*"]).any() and markers.isin(["..."]).any():
        fig.update_layout(margin={'l': 40, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="*<i>Use with caution<br>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    elif markers.isin(["*"]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="*<i>Use with caution</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    elif markers.isin(["..."]).any():
        fig.update_layout(margin={'l': 30, 'b': 75, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.31, x=1.2, align="left", showarrow=False),
                                       dict(text="<i>Some results too unreliable to be shown</i>", xref="paper", yref="paper", xanchor='right', yanchor="top", y=-0.08, x=1.2, align="right", showarrow=False, font=dict(size=13))])
    else:
        fig.update_layout(margin={'l': 30, 'b': 30, 'r': 10, 't': 40},
                          annotations=[dict(text="<a href=\"https://www.scribbr.com/statistics/confidence-interval/\">What is this?</a>", xref="paper", yref="paper", xanchor='right', y=0.32, x=1.2, align="left", showarrow=False)])

    return fig


@app.callback(
    dash.dependencies.Output('YouthDonRateAmt', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = YouthDonRates_2018[YouthDonRates_2018['Region'] == region]
    dff1 = dff1[dff1["Group"] == "Younger"]

    dff2 = YouthAvgDonAmt_2018[YouthAvgDonAmt_2018['Region'] == region]
    dff2 = dff2[dff2["Group"] == "Younger"]

    # name1 = "15 to 24"
    # name2 = "25 to 34"
    # name3 = ">=35"
    name1 = "15 à 24 ans"
    name2 = "25 à 34 ans"
    name3 = ">=35"

    title = '{}, {}'.format("Taux des dons laïcs et religieux totaux et montant moyen des dons", region)
    return triple_horizontal_rate_avg(dff1, dff2, name1, name2, name3, title, "dollar")


@app.callback(
    dash.dependencies.Output('YouthDonRateByCause', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = YouthDonRateByCause_2018[YouthDonRateByCause_2018['Region'] == region]
    dff = dff[dff["Group"] == "Younger2"]
    # name1 = "15 to 34"
    name1 = "15 à 34 ans"
    name2 = ">=35"
    title = '{}, {}'.format("Taux de dons par cause", region)
    return vertical_double_graph(dff, title, name1, name2, "percent")


@app.callback(
    dash.dependencies.Output('YouthAvgAmtByCause', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = YouthAvgDonByCause_2018[YouthAvgDonByCause_2018['Region'] == region]
    dff = dff[dff["Group"] == "Younger2"]
    # name1 = "15 to 34"
    name1 = "15 à 34 ans"
    name2 = ">=35"
    title = '{}, {}'.format("Montant moyen des dons selon la cause", region)
    return vertical_double_graph(dff, title, name1, name2, "dollar")


@app.callback(
    dash.dependencies.Output('YouthDonRateByMeth', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = YouthDonRateByMeth_2018[YouthDonRateByMeth_2018['Region'] == region]
    dff = dff[dff["Group"] == "Younger2"]
    # name1 = "15 to 34"
    name1 = "15 à 34 ans"
    name2 = ">=35"
    title = '{}, {}'.format("Taux de dons par méthode", region)
    return vertical_double_graph(dff, title, name1, name2, "percent")


@app.callback(
    dash.dependencies.Output('YouthAvgAmtByMeth', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = YouthAvgDonByMeth_2018[YouthAvgDonByMeth_2018['Region'] == region]
    dff = dff[dff["Group"] == "Younger2"]
    # name1 = "15 to 34"
    name1 = "15 à 34 ans"
    name2 = ">=35"
    title = '{}, {}'.format("Montant moyen des dons par méthode", region)
    return vertical_double_graph(dff, title, name1, name2, "dollar")


@app.callback(
    dash.dependencies.Output('YouthMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = YouthReasonsGiving_2018[YouthReasonsGiving_2018['Region'] == region]
    dff = dff[dff["Group"] == "Younger"]
    # name1 = "15 to 24"
    # name2 = "25 to 34"
    # name3 = ">=35"
    name1 = "15 à 24 ans"
    name2 = "25 à 34 ans"
    name3 = ">=35"
    title = '{}, {}'.format("Motivations des dons", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('YouthBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = YouthBarriers_2018[YouthBarriers_2018['Region'] == region]
    dff = dff[dff["Group"] == "Younger"]
    # name1 = "15 to 24"
    # name2 = "25 to 34"
    # name3 = ">=35"
    name1 = "15 à 24 ans"
    name2 = "25 à 34 ans"
    name3 = ">=35"
    title = '{}, {}'.format("Freins à donner davantage", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('YouthEfficiency', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = YouthEfficiencyConcerns_2018[YouthEfficiencyConcerns_2018['Region'] == region]
    dff = dff[dff["Group"] == "Younger2"]
    # name1 = "15 to 34"
    name1 = "15 à 34 ans"
    name2 = ">=35"
    title = '{}, {}'.format("Raisons des préoccupations relatives à l’efficience", region)
    return vertical_double_graph(dff, title, name1, name2, "percent")


@app.callback(
    dash.dependencies.Output('YouthSolicitations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = YouthSolicitationConcerns_2018[YouthSolicitationConcerns_2018['Region'] == region]
    dff = dff[dff["Group"] == "Younger2"]
    # name1 = "15 to 34"
    name1 = "15 à 34 ans"
    name2 = ">=35"
    title = '{}, {}'.format("Raisons de l’aversion pour les sollicitations", region)
    return vertical_double_graph(dff, title, name1, name2, "percent")



@app.callback(
    dash.dependencies.Output('YouthVolRateVolAmt', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = YouthVolRate_2018[YouthVolRate_2018['Region'] == region]
    dff1 = dff1[dff1["Group"] == "Younger"]

    dff2 = YouthAvgHrs_2018[YouthAvgHrs_2018['Region'] == region]
    dff2 = dff2[dff2["Group"] == "Younger"]

    # name1 = "15 to 24"
    # name2 = "25 to 34"
    # name3 = ">=35"
    name1 = "15 à 24 ans"
    name2 = "25 à 34 ans"
    name3 = ">=35"
    title = '{}, {}'.format("Taux et nombre moyen d’heures consacrées au bénévolat, <br> à l’aide d’autrui et à l’engagement communautaire", region)
    return triple_horizontal_rate_avg(dff1, dff2, name1, name2, name3, title, giving=False)


@app.callback(
    dash.dependencies.Output('YouthVolRateByCause', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = YouthVolRateByCause_2018[YouthVolRateByCause_2018['Region'] == region]
    dff = dff[dff["Group"] == "Younger2"]
    # name1 = "15 to 34"
    name1 = "15 à 34 ans"
    name2 = ">=35"
    title = '{}, {}'.format("Taux de bénévoles selon la cause", region)
    return vertical_double_graph(dff, title, name1, name2, "percent")


@app.callback(
    dash.dependencies.Output('YouthAvgHrsByCause', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = YouthAvgHrsByCause_2018[YouthAvgHrsByCause_2018['Region'] == region]
    dff = dff[dff["Group"] == "Younger2"]
    # name1 = "15 to 34"
    name1 = "15 à 34 ans"
    name2 = ">=35"
    title = '{}, {}'.format("Nombre moyen d’heures de bénévolat selon la cause", region)
    return vertical_double_graph(dff, title, name1, name2, "hours")


@app.callback(
    dash.dependencies.Output('YouthVolRateByActivity', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = YouthVolRateByActivity_2018[YouthVolRateByActivity_2018['Region'] == region]
    dff = dff[dff["Group"] == "Younger2"]
    # name1 = "15 to 34"
    name1 = "15 à 34 ans"
    name2 = ">=35"
    title = '{}, {}'.format("Taux de bénévoles par activité", region)
    return vertical_double_graph(dff, title, name1, name2, "percent")


@app.callback(
    dash.dependencies.Output('YouthAvgHrsByActivity', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = YouthAvgHrsByActivity_2018[YouthAvgHrsByActivity_2018['Region'] == region]
    dff = dff[dff["Group"] == "Younger2"]
    dff = dff[dff["Group"] == "Younger2"]
    # name1 = "15 to 34"
    name1 = "15 à 34 ans"
    name2 = ">=35"
    title = '{}, {}'.format("Nombre moyen d’heures de bénévolat par activité", region)
    return vertical_double_graph(dff, title, name1, name2, "hours")


@app.callback(
    dash.dependencies.Output('YouthVolMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = YouthReasonsVol_2018[YouthReasonsVol_2018['Region'] == region]
    dff = dff[dff["Group"] == "Younger"]
    # name1 = "15 to 24"
    # name2 = "25 to 34"
    # name3 = ">=35"
    name1 = "15 à 24 ans"
    name2 = "25 à 34 ans"
    name3 = ">=35"
    title = '{}, {}'.format("Motivations du bénévolat", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('YouthVolBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = YouthBarriersVol_2018[YouthBarriersVol_2018['Region'] == region]
    dff = dff[dff["Group"] == "Younger"]
    # name1 = "15 to 24"
    # name2 = "25 to 34"
    # name3 = ">=35"
    name1 = "15 à 24 ans"
    name2 = "25 à 34 ans"
    name3 = ">=35"
    title = '{}, {}'.format("Freins à faire plus de bénévolat", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('YouthRateHelpDirect', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = YouthHelpDirectlyRate_2018[YouthHelpDirectlyRate_2018['Region'] == region]
    dff = dff[dff["Group"] == "Younger"]
    # name1 = "15 to 24"
    # name2 = "25 to 34"
    # name3 = ">=35"
    name1 = "15 à 24 ans"
    name2 = "25 à 34 ans"
    name3 = ">=35"
    title = '{}, {}'.format("Méthodes d’aide directe d’autrui", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('YouthHrsHelpDirect', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = YouthAvgHrsHelpDirectly_2018[YouthAvgHrsHelpDirectly_2018['Region'] == region]
    dff = dff[dff["Group"] == "Younger2"]
    # name1 = "15 to 34"
    name1 = "15 à 34 ans"
    name2 = ">=35"
    title = '{}, {}'.format("Nombre moyen d’heures consacrées à l’aide directe d’autrui", region)
    return vertical_double_graph(dff, title, name1, name2, "hours")


@app.callback(
    dash.dependencies.Output('YouthRateCommInvolve', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = YouthCommInvolveRate_2018[YouthCommInvolveRate_2018['Region'] == region]
    dff = dff[dff["Group"] == "Younger"]
    # name1 = "15 to 24"
    # name2 = "25 to 34"
    # name3 = ">=35"
    name1 = "15 à 24 ans"
    name2 = "25 à 34 ans"
    name3 = ">=35"
    title = '{}, {}'.format("Types d’engagement communautaire", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('YouthHrsCommInvolve', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = YouthAvgHrsCommInvolve_2018[YouthAvgHrsCommInvolve_2018['Region'] == region]
    dff = dff[dff["Group"] == "Younger2"]
    # name1 = "15 to 34"
    name1 = "15 à 34 ans"
    name2 = ">=35"
    title = '{}, {}'.format("Nombre moyen d’heures consacrées aux formes d’engagement communautaire", region)
    return vertical_double_graph(dff, title, name1, name2, "hours")


if __name__ == '__main__':
    app.run_server(debug=True)
