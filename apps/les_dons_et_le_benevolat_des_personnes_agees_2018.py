import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc
import os
import os.path as op

from utils.data.general import get_dataframe

from app import app
from homepage import footer #navbar, footer

####################### Data processing ######################
SeniorsAvgDonAmt_2018 = get_dataframe("2018-SeniorsAvgDonAmt.csv")
SeniorsAvgDonByCause_2018 = get_dataframe("2018-SeniorsAvgDonByCause.csv")
SeniorsAvgDonByMeth_2018 = get_dataframe("2018-SeniorsAvgDonByMeth.csv")
SeniorsAvgHrs_2018 = get_dataframe("2018-SeniorsAvgHrs_FR.csv")
SeniorsAvgHrsByActivity_2018 = get_dataframe("2018-SeniorsAvgHrsByActivity.csv")
SeniorsAvgHrsByCause_2018 = get_dataframe("2018-SeniorsAvgHrsByCause.csv")
SeniorsAvgHrsCommInvolve_2018 = get_dataframe("2018-SeniorsAvgHrsCommInvolve.csv")
SeniorsAvgHrsHelpDirectly_2018 = get_dataframe("2018-SeniorsAvgHrsHelpDirectly.csv")
SeniorsBarriers_2018 = get_dataframe("2018-SeniorsBarriersGiving.csv")
SeniorsBarriersVol_2018 = get_dataframe("2018-SeniorsBarriersVol.csv")
SeniorsCommInvolveRate_2018 = get_dataframe("2018-SeniorsCommInvolveRate.csv")
SeniorsDonRateByCause_2018 = get_dataframe("2018-SeniorsDonRateByCause.csv")
SeniorsDonRateByMeth_2018 = get_dataframe("2018-SeniorsDonRateByMeth.csv")
SeniorsDonRates_2018 = get_dataframe("2018-SeniorsDonRates.csv")
SeniorsEfficiencyConcerns_2018 = get_dataframe("2018-SeniorsEfficiencyConcerns.csv")
SeniorsHelpDirectlyRate_2018 = get_dataframe("2018-SeniorsHelpDirectlyRate.csv")
SeniorsReasonsGiving_2018 = get_dataframe("2018-SeniorsReasonsGiving.csv")
SeniorsReasonsVol_2018 = get_dataframe("2018-SeniorsReasonsVol.csv")
SeniorsSolicitationConcerns_2018 = get_dataframe("2018-SeniorsSolicitationConcerns.csv")
SeniorsVolRateByActivity_2018 = get_dataframe("2018-SeniorsVolRateByActivity.csv")
SeniorsVolRateByCause_2018 = get_dataframe("2018-SeniorsVolRateByCause.csv")
SeniorsVolRate_2018 = get_dataframe("2018-SeniorsVolRates_FR.csv")

rates = [SeniorsBarriers_2018,
         SeniorsBarriersVol_2018,
         SeniorsCommInvolveRate_2018,
         SeniorsDonRateByCause_2018,
         SeniorsDonRateByMeth_2018,
         SeniorsDonRates_2018,
         SeniorsEfficiencyConcerns_2018,
         SeniorsHelpDirectlyRate_2018,
         SeniorsReasonsGiving_2018,
         SeniorsReasonsVol_2018,
         SeniorsSolicitationConcerns_2018,
         SeniorsVolRateByActivity_2018,
         SeniorsVolRateByCause_2018,
         SeniorsVolRate_2018]

data = [SeniorsAvgDonAmt_2018,
        SeniorsAvgDonByCause_2018,
        SeniorsAvgDonByMeth_2018,
        SeniorsAvgHrs_2018,
        SeniorsAvgHrsByActivity_2018,
        SeniorsAvgHrsByCause_2018,
        SeniorsAvgHrsCommInvolve_2018,
        SeniorsAvgHrsHelpDirectly_2018,
        SeniorsBarriers_2018,
        SeniorsBarriersVol_2018,
        SeniorsCommInvolveRate_2018,
        SeniorsDonRateByCause_2018,
        SeniorsDonRateByMeth_2018,
        SeniorsDonRates_2018,
        SeniorsEfficiencyConcerns_2018,
        SeniorsHelpDirectlyRate_2018,
        SeniorsReasonsGiving_2018,
        SeniorsReasonsVol_2018,
        SeniorsSolicitationConcerns_2018,
        SeniorsVolRateByActivity_2018,
        SeniorsVolRateByCause_2018,
        SeniorsVolRate_2018]

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
                dbc.NavLink("EN", href="http://app.givingandvolunteering.ca/giving_and_volunteering_by_seniors",external_link=True)
            ),
        ],
        brand="Centre Canadien de Connaissances sur les Dons et le Bénévolat",
        brand_href="/",
        color="#4B161D",
        dark=True,
        sticky='top'
    )

marginTop = 20


layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1('Les dons et le bénévolat des personnes agées (2018)'),
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
        className="bg-secondary text-white text-center py-4",
    ),
    # Note: filters put in separate container to make floating element later
    dbc.Container([
        dbc.Row(
           dbc.Col(
               html.Div([
                   "Select a region of focus:",
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
                D’après les données de l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, les personnes âgées sont plus enclines à donner, et à donner plus, que les personnes plus jeunes au Canada, ce qui est vrai pour les dons aux causes laïques comme aux causes religieuses. Tout comme leurs homologues plus jeunes, les personnes âgées ont plus tendance à donner à des causes laïques qu’à des causes religieuses. En revanche, elles donnent beaucoup plus d’argent, en moyenne, aux causes religieuses.
                """
                ),
                # Donation rate and average donation amount
                dcc.Graph(id='YouthDonRateAmt', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Les dons selon la cause'),
                dcc.Markdown("""
                Les personnes âgées ont plus tendance que les personnes plus jeunes à donner de l’argent à la majorité des causes, mais les différences les plus importantes ont trait aux causes les plus populaires. À l’échelle nationale, entre 39 % et 46 % des personnes canadiennes âgées de 65 ans ou plus donnent aux organismes de santé et de services sociaux, par comparaison avec moins d’un tiers de celles âgées de 15 à 64 ans. Les personnes plus âgées ont également beaucoup plus tendance à donner de l’argent aux congrégations religieuses. Les taux de dons pour les autres causes sont similaires pour les divers groupes d’âge. 
                """),
                # Donation rate by cause
                dcc.Graph(id='YouthDonRateByCause', style={'marginTop': marginTop}), 
                dcc.Markdown("""
                Les personnes plus âgées donnent plus d’argent, en moyenne, aux causes qu’elles soutiennent, mais, dans la majorité des cas, les différences ne sont pas statistiquement significatives. 
                """),
                # Average amount donated by cause
                dcc.Graph(id='YouthAvgAmtByCause', style={'marginTop': marginTop}), 
            ], className='col-md-10 col-lg-8 mx-auto'),
            html.Div([
                html.H4('Méthodes de dons'),
                dcc.Markdown("""
                L’incidence de l’âge est évidente sur le choix des méthodes de dons. Par exemple, le don par courrier est la méthode préférée des personnes âgées de 75 ans ou plus et la deuxième méthode par ordre de préférence pour les personnes âgées de 65 à 74 ans, tandis que les dons par courrier sont relativement rares chez les personnes âgées de 15 à 64 ans. Les personnes âgées ont également significativement plus tendance à donner à un lieu de culte ou à la mémoire de quelqu’un et significativement moins tendance à donner en ligne. Les personnes âgées de 65 à 74 ans sont plus enclines que celles des groupes d’âge plus jeunes et plus âgés à parrainer quelqu’un ou à donner de l’argent en étant sollicitées à leur porte. 
                """),
                # Donation rate by method
                dcc.Graph(id='YouthDonRateByMeth', style={'marginTop': marginTop}), 
                dcc.Markdown("""
                Le montant moyen des dons des personnes canadiennes âgées de 65 ans ou plus est le plus élevé quand elles donnent de l’argent dans les lieux de culte et de leur propre initiative.
                """),
                # Average amount donated by method
                dcc.Graph(id='YouthAvgAmtByMeth', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Motivations des dons'),
                dcc.Markdown("""
                En général, les personnes plus âgées donnent de l’argent pour les mêmes raisons que les personnes plus jeunes, la conviction du bien-fondé de la cause et la compassion envers les personnes dans le besoin étant les deux principales motivations des dons pour tous les groupes d’âge. Il existe cependant quelques différences. Les personnes plus âgées sont plus enclines que les personnes plus jeunes à donner de l’argent pour des raisons religieuses ou spirituelles ou parce qu’elles recevront un crédit d’impôt et moins enclines à donner après avoir été sollicitées par une personne de leur connaissance. Les personnes âgées de 65 à 74 ans sont plus enclines à donner de l’argent parce que la cause les touche personnellement que les personnes plus jeunes et que les personnes plus âgées.
                """),
                # Motivations for donating
                dcc.Graph(id='YouthMotivations', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Freins à donner davantage'),
                dcc.Markdown("""
                Les personnes plus âgées ont nettement plus tendance que les personnes plus jeunes à déclarer ne pas avoir donné plus parce qu’elles étaient satisfaites du montant de leurs dons ou parce qu’elles avaient donné directement aux personnes dans le besoin. L’âge ne semble pas avoir une grande incidence sur les autres freins à donner davantage.
                """),
                # Barriers to donating more
                dcc.Graph(id='YouthBarriers', style={'marginTop': marginTop}), 
                html.Div([
                    html.H5('Préoccupations relatives à l’efficience'),
                    dcc.Markdown("""
                    Les personnes plus âgées ont relativement plus tendance que les personnes plus jeunes à déclarer ne pas avoir donné plus parce qu’elles ne croyaient pas que leur argent serait utilisé avec efficience. Cette préoccupation semble principalement liée à leur conviction que trop d’argent est dépensé pour les collectes de fonds.
                    """),
                    # Reasons for concern about efficiency
                    dcc.Graph(id='YouthEfficiency', style={'marginTop': marginTop}), 
                    ]),
                html.Div([
                    html.H5('Préoccupations relatives aux sollicitations'),
                    dcc.Markdown("""
                    Les personnes plus âgées ont également plus tendance à déclarer ne pas avoir donné plus parce qu’elles n’aimaient pas les méthodes de sollicitation. Cette préoccupation semble principalement liée au nombre de demandes de don qu’elles reçoivent.
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
                D’après les données de l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, les personnes plus âgées sont moins susceptibles de faire du bénévolat que les personnes plus jeunes au Canada. En revanche, les personnes plus âgées font don d’un nombre d’heures de bénévolat beaucoup plus important, en moyenne, que les bénévoles plus jeunes. À l’échelle nationale, les personnes canadiennes âgées de 75 ans ou plus qui font du bénévolat (30 % de ce groupe d’âge) font don en moyenne de 223 heures par année, tandis que les personnes canadiennes âgées de 15 à 64 ans qui font du bénévolat (42 % de ce groupe d’âge) font don en moyenne de 181 heures. Les personnes canadiennes âgées de 65 à 74 ans se situent entre le groupe d’âge plus jeune et le groupe d’âge plus âgé, à la fois pour leur taux et pour leur nombre moyen d’heures de bénévolat. Les personnes âgées de 75 ans ou plus ont moins tendance à aider autrui directement que les personnes âgées de moins de 75 ans (c.-à-d. en dehors d’un groupe ou d’un organisme) ou à pratiquer d’autres formes d’engagement communautaire. 
                """),
                # Rates and average hours devoted to volunteering, helping others and community engagement
                dcc.Graph(id='YouthVolRateVolAmt', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Bénévolat selon la cause'),
                dcc.Markdown("""
                Les personnes âgées de 65 ans ou plus sont plus enclines à faire du bénévolat pour les congrégations religieuses, les organismes de services sociaux et les organismes des sports et des loisirs. Par comparaison avec les personnes âgées de 15 à 64 ans, celles âgées de 65 ans ou plus sont plus susceptibles de faire du bénévolat pour les organismes religieux et les hôpitaux. Elles sont moins susceptibles de faire du bénévolat pour les organismes d’éducation et de recherche, des sports et des loisirs et pour les universités et les collèges. 
                """),
                # Volunteer rate by cause
                dcc.Graph(id='YouthVolRateByCause', style={'marginTop': marginTop}), 
                dcc.Markdown("""
                En raison de la grande variation des heures de bénévolat, la prudence est de rigueur pour interpréter les données. Par exemple, bien qu’il semble que, à l’échelle nationale, les personnes plus âgées font don d’un plus grand nombre d’heures de bénévolat à la plupart des types d’organismes, un grand nombre de ces différences ne sont pas statistiquement significatives. En revanche, les personnes plus âgées font don d’un nombre d’heures de bénévolat significativement plus élevé aux organismes des arts et de la culture, aux hôpitaux, aux organismes des sports et des loisirs, aux organismes de services sociaux et aux organismes du développement et du logement.
                """),
                # Average hours volunteered by cause
                dcc.Graph(id='YouthAvgHrsByCause', style={'marginTop': marginTop}), 
            ], className='col-md-10 col-lg-8 mx-auto'),
            html.Div([
                html.H4('Activités des bénévoles'),
                dcc.Markdown("""
                La probabilité de participer à des activités bénévoles décroît avec l’âge. Par exemple, les personnes âgées de 75 ans ou plus sont moins susceptibles d’organiser des activités ou des événements et de collecter des fonds bénévolement que celles âgées de 65 à 74 ans et ces dernières sont moins susceptibles de pratiquer ces activités que les personnes âgées de 15 à 64 ans. En revanche, les bénévoles de 65 à 74 ans ont plus tendance à siéger à des comités ou à des conseils d’administration ou à faire du travail administratif que les bénévoles plus jeunes et plus âgés. 
                """),
                # Volunteer rate by activity
                dcc.Graph(id='YouthVolRateByActivity', style={'marginTop': marginTop}), 
                dcc.Markdown("""
                Sur le plan du nombre moyen d’heures consacrées aux diverses activités, les bénévoles de 65 ans ou plus consacrent moins d’heures, en moyenne, que les bénévoles de 15 à 64 ans à faire du travail de bureau, à offrir des soins de santé ou du soutien, à collecter, à offrir ou à livrer des marchandises, à organiser des activités et des événements, à conduire bénévolement et à collecter des fonds. 
                """),
                # Average hours volunteered by activity
                dcc.Graph(id='YouthAvgHrsByActivity', style={'marginTop': marginTop}), 
            
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Motivations du bénévolat'),
                dcc.Markdown("""
                Les personnes plus âgées ont tendance à faire du bénévolat pour les mêmes raisons que les personnes plus jeunes. Par exemple, apporter une contribution à la communauté et utiliser leurs compétences sont les deux principales motivations du bénévolat pour tous les groupes d’âge. Cela dit, il existe plusieurs différences. Les personnes plus âgées ont plus tendance à déclarer faire du bénévolat pour améliorer leur santé et leur bien-être, pour réseauter et rencontrer des personnes ou pour des raisons spirituelles ou religieuses. Les personnes âgées de 75 ans ou plus ont davantage tendance à déclarer faire du bénévolat parce que leurs connaissances en font. 
                """),
                # Motivations for volunteering
                dcc.Graph(id='YouthVolMotivations', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Freins au bénévolat'),
                dcc.Markdown("""
                Malgré la tendance à l’uniformité du classement général des freins au bénévolat entre les divers groupes d’âge, il existe d’importantes différences entre ceux-ci. Les personnes plus âgées ont moins tendance que les bénévoles plus jeunes à déclarer manquer de temps pour faire du bénévolat et ne pas savoir comment s’impliquer. En revanche, elles ont plus tendance à penser avoir déjà donné suffisamment de leur temps, à déclarer que plus de bénévolat ne présente aucun intérêt pour elles et à avoir des problèmes de santé qui les empêchent d’en faire plus.
                """),
                # Barriers to volunteering more
                dcc.Graph(id='YouthVolBarriers', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Aide directe d’autrui '),
                dcc.Markdown("""
                Les personnes plus âgées sont plus enclines à aider directement autrui en cuisinant, en faisant le ménage et d’autres tâches à domicile, en magasinant, en conduisant ou en accompagnant des personnes aux magasins ou à des rendez-vous et en offrant des soins en santé ou personnels. Les personnes âgées de 65 à 74 ans sont plus enclines que celles âgées de 75 ans ou plus à offrir tous les types d’aide directe. 
                """),
                # Methods of helping others directly
                dcc.Graph(id='YouthRateHelpDirect', style={'marginTop': marginTop}),
                dcc.Markdown("""
                Les personnes âgées de 65 ans ou plus consacrent plus de temps, en moyenne, à aider autrui directement que leurs homologues plus jeunes. Les différences les plus importantes concernent les soins liés à la santé ou personnels, cuisiner, faire le ménage ou les autres corvées ménagères, et magasiner, conduire ou accompagner d’autres personnes aux magasins ou à des rendez-vous. 
                """),
                # Average hours devoted to means of helping others directly
                dcc.Graph(id='YouthHrsHelpDirect', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Engagement communautaire'),
                dcc.Markdown("""
                Sur le plan des activités visant à améliorer la communauté, les personnes âgées de 65 ans et plus sont plus enclines que les personnes plus jeunes à participer à des réunions publiques, mais moins enclines à participer à la plupart des autres types d’activités. 
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
                                          ["Giving overall", "Secular giving", "Religious giving"])
        dff_2['QuestionText'] = np.select([dff_2["QuestionText"] == 'Total donation<br>amount', dff_2["QuestionText"] == 'Secular donation<br>amount', dff_2["QuestionText"] == 'Religious donation<br>amount'],
                                          ["Giving overall", "Secular giving", "Religious giving"])
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
                             'y': 0.97},
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
                             'y': 0.99},
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
    dash.dependencies.Output('SeniorsDonRateAmt', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = SeniorsDonRates_2018[SeniorsDonRates_2018['Region'] == region]
    dff1 = dff1[dff1["Group"] == "Senior"]

    dff2 = SeniorsAvgDonAmt_2018[SeniorsAvgDonAmt_2018['Region'] == region]
    dff2 = dff2[dff2["Group"] == "Senior"]

    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Donation rate and average donation amount", region)
    return triple_horizontal_rate_avg(dff1, dff2, name1, name2, name3, title, "dollar")


@app.callback(
    dash.dependencies.Output('SeniorsDonRateByCause', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsDonRateByCause_2018[SeniorsDonRateByCause_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Donation rate by cause", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('SeniorsAvgAmtByCause', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsAvgDonByCause_2018[SeniorsAvgDonByCause_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior2"]
    name1 = "15 to 64"
    name2 = "65 plus"
    title = '{}, {}'.format("Average amount donated by cause", region)
    return vertical_double_graph(dff, title, name1, name2, "dollar", seniors=True)


@app.callback(
    dash.dependencies.Output('SeniorsDonRateByMeth', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsDonRateByMeth_2018[SeniorsDonRateByMeth_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Donation rate by method", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('SeniorsAvgAmtByMeth', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsAvgDonByMeth_2018[SeniorsAvgDonByMeth_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior2"]
    name1 = "15 to 64"
    name2 = "65 plus"
    title = '{}, {}'.format("Donation rate by method", region)
    return vertical_double_graph(dff, title, name1, name2, "dollar", seniors=True)


@app.callback(
    dash.dependencies.Output('SeniorsMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsReasonsGiving_2018[SeniorsReasonsGiving_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Motivations for donating", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('SeniorsBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsBarriers_2018[SeniorsBarriers_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Barriers to donating more", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('SeniorsEfficiency', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsEfficiencyConcerns_2018[SeniorsEfficiencyConcerns_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Reasons for concern about efficiency", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('SeniorsSolicitations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsSolicitationConcerns_2018[SeniorsSolicitationConcerns_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Reasons for disliking solicitations", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")



@app.callback(
    dash.dependencies.Output('SeniorsVolRateVolAmt', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = SeniorsVolRate_2018[SeniorsVolRate_2018['Region'] == region]
    dff1 = dff1[dff1["Group"] == "Senior"]

    dff2 = SeniorsAvgHrs_2018[SeniorsAvgHrs_2018['Region'] == region]
    dff2 = dff2[dff2["Group"] == "Senior"]

    # name1 = "15 to 64"
    # name2 = "65 to 74"
    # name3 = "75 plus"
    name1 = "15 à 64 ans"
    name2 = "65 à 74 ans"
    name3 = "75 ans et plus"
    title = '{}, {}'.format("Taux et nombre moyen d’heures consacrées au <br> bénévolat, à l’aide d’autrui et à l’engagement communautaire", region)
    return triple_horizontal_rate_avg(dff1, dff2, name1, name2, name3, title, giving=False)


@app.callback(
    dash.dependencies.Output('SeniorsVolRateByCause', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsVolRateByCause_2018[SeniorsVolRateByCause_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior2"]
    name1 = "15 to 64"
    name2 = "65 plus"
    title = '{}, {}'.format("Volunteer rate by cause", region)
    return vertical_double_graph(dff, title, name1, name2, "percent", seniors=True)


@app.callback(
    dash.dependencies.Output('SeniorsAvgHrsByCause', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsAvgHrsByCause_2018[SeniorsAvgHrsByCause_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior2"]
    name1 = "15 to 64"
    name2 = "65 plus"
    title = '{}, {}'.format("Average hours volunteered by cause", region)
    return vertical_double_graph(dff, title, name1, name2, "hours", seniors=True)


@app.callback(
    dash.dependencies.Output('SeniorsVolRateByActivity', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsVolRateByActivity_2018[SeniorsVolRateByActivity_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Volunteer rate by activity", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('SeniorsAvgHrsByActivity', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsAvgHrsByActivity_2018[SeniorsAvgHrsByActivity_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior2"]
    dff = dff[dff["Group"] == "Senior2"]
    name1 = "15 to 64"
    name2 = "65 plus"
    title = '{}, {}'.format("Average hours volunteered by activity", region)
    return vertical_double_graph(dff, title, name1, name2, "hours", seniors=True)


@app.callback(
    dash.dependencies.Output('SeniorsVolMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsReasonsVol_2018[SeniorsReasonsVol_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Motivations for volunteering", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('SeniorsVolBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsBarriersVol_2018[SeniorsBarriersVol_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Barriers to volunteering more", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('SeniorsRateHelpDirect', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsHelpDirectlyRate_2018[SeniorsHelpDirectlyRate_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    name1 = "15 to 64"
    name2 = "65 to 74"
    name3 = "75 plus"
    title = '{}, {}'.format("Methods of helping others directly", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('SeniorsHrsHelpDirect', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsAvgHrsHelpDirectly_2018[SeniorsAvgHrsHelpDirectly_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior2"]
    name1 = "15 to 64"
    name2 = "65 plus"
    title = '{}, {}'.format("Average hours devoted to means of helping others directly", region)
    return vertical_double_graph(dff, title, name1, name2, "hours", seniors=True)


@app.callback(
    dash.dependencies.Output('SeniorsRateCommInvolve', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsCommInvolveRate_2018[SeniorsCommInvolveRate_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior"]
    # name1 = "15 to 64"
    # name2 = "65 to 74"
    # name3 = "75 plus"
    # name1 = "15 to 64"
    # name2 = "65 to 74"
    # name3 = "75 plus"
    name1 = "15 à 64 ans"
    name2 = "65 à 74 ans"
    name3 = "75 ans et plus"
    title = '{}, {}'.format("Types of community engagement", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('SeniorsHrsCommInvolve', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = SeniorsAvgHrsCommInvolve_2018[SeniorsAvgHrsCommInvolve_2018['Region'] == region]
    dff = dff[dff["Group"] == "Senior2"]
    name1 = "15 to 64"
    name2 = "65 plus"
    title = '{}, {}'.format("Average hours devoted to forms of community engagement", region)
    return vertical_double_graph(dff, title, name1, name2, "hours", seniors=True)


