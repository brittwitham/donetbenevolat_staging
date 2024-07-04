# import dash
# from dash import dcc, html
# import plotly.graph_objects as go
# import numpy as np
# import pandas as pd
# pd.options.mode.chained_assignment = None  # default='warn'
# import dash_bootstrap_components as dbc
# import os
# import os.path as op

# from utils.data.general import get_dataframe

# from app import app
# from homepage import footer #navbar, footer
# from utils.gen_navbar import gen_navbar

# ####################### Data processing ######################
# SeniorsAvgDonAmt_2018 = get_dataframe("2018-SeniorsAvgDonAmt.csv")
# SeniorsAvgDonByCause_2018 = get_dataframe("2018-SeniorsAvgDonByCause.csv")
# SeniorsAvgDonByMeth_2018 = get_dataframe("2018-SeniorsAvgDonByMeth.csv")
# SeniorsAvgHrs_2018 = get_dataframe("2018-SeniorsAvgHrs_FR.csv")
# SeniorsAvgHrsByActivity_2018 = get_dataframe("2018-SeniorsAvgHrsByActivity.csv")
# SeniorsAvgHrsByCause_2018 = get_dataframe("2018-SeniorsAvgHrsByCause.csv")
# SeniorsAvgHrsCommInvolve_2018 = get_dataframe("2018-SeniorsAvgHrsCommInvolve.csv")
# SeniorsAvgHrsHelpDirectly_2018 = get_dataframe("2018-SeniorsAvgHrsHelpDirectly.csv")
# SeniorsBarriers_2018 = get_dataframe("2018-SeniorsBarriersGiving.csv")
# SeniorsBarriersVol_2018 = get_dataframe("2018-SeniorsBarriersVol.csv")
# SeniorsCommInvolveRate_2018 = get_dataframe("2018-SeniorsCommInvolveRate.csv")
# SeniorsDonRateByCause_2018 = get_dataframe("2018-SeniorsDonRateByCause.csv")
# SeniorsDonRateByMeth_2018 = get_dataframe("2018-SeniorsDonRateByMeth.csv")
# SeniorsDonRates_2018 = get_dataframe("2018-SeniorsDonRates.csv")
# SeniorsEfficiencyConcerns_2018 = get_dataframe("2018-SeniorsEfficiencyConcerns.csv")
# SeniorsHelpDirectlyRate_2018 = get_dataframe("2018-SeniorsHelpDirectlyRate.csv")
# SeniorsReasonsGiving_2018 = get_dataframe("2018-SeniorsReasonsGiving.csv")
# SeniorsReasonsVol_2018 = get_dataframe("2018-SeniorsReasonsVol.csv")
# SeniorsSolicitationConcerns_2018 = get_dataframe("2018-SeniorsSolicitationConcerns.csv")
# SeniorsVolRateByActivity_2018 = get_dataframe("2018-SeniorsVolRateByActivity.csv")
# SeniorsVolRateByCause_2018 = get_dataframe("2018-SeniorsVolRateByCause.csv")
# SeniorsVolRate_2018 = get_dataframe("2018-SeniorsVolRates_FR.csv")

# rates = [SeniorsBarriers_2018,
#          SeniorsBarriersVol_2018,
#          SeniorsCommInvolveRate_2018,
#          SeniorsDonRateByCause_2018,
#          SeniorsDonRateByMeth_2018,
#          SeniorsDonRates_2018,
#          SeniorsEfficiencyConcerns_2018,
#          SeniorsHelpDirectlyRate_2018,
#          SeniorsReasonsGiving_2018,
#          SeniorsReasonsVol_2018,
#          SeniorsSolicitationConcerns_2018,
#          SeniorsVolRateByActivity_2018,
#          SeniorsVolRateByCause_2018,
#          SeniorsVolRate_2018]

# data = [SeniorsAvgDonAmt_2018,
#         SeniorsAvgDonByCause_2018,
#         SeniorsAvgDonByMeth_2018,
#         SeniorsAvgHrs_2018,
#         SeniorsAvgHrsByActivity_2018,
#         SeniorsAvgHrsByCause_2018,
#         SeniorsAvgHrsCommInvolve_2018,
#         SeniorsAvgHrsHelpDirectly_2018,
#         SeniorsBarriers_2018,
#         SeniorsBarriersVol_2018,
#         SeniorsCommInvolveRate_2018,
#         SeniorsDonRateByCause_2018,
#         SeniorsDonRateByMeth_2018,
#         SeniorsDonRates_2018,
#         SeniorsEfficiencyConcerns_2018,
#         SeniorsHelpDirectlyRate_2018,
#         SeniorsReasonsGiving_2018,
#         SeniorsReasonsVol_2018,
#         SeniorsSolicitationConcerns_2018,
#         SeniorsVolRateByActivity_2018,
#         SeniorsVolRateByCause_2018,
#         SeniorsVolRate_2018]

# for i in range(len(rates)):
#     rates[i]['Estimate'] = rates[i]['Estimate'] * 100
#     rates[i]['CI Upper'] = rates[i]['CI Upper'] * 100


# for i in range(len(data)):
#     data[i]["Estimate"] = np.where(data[i]["Marker"] == "...", 0, data[i]["Estimate"])
#     data[i]["CI Upper"] = np.where(data[i]["Marker"] == "...", 0, data[i]["CI Upper"])
#     data[i]["Group"] = np.where(data[i]["Attribute"] == "Unable to determine", "", data[i]["Group"])
#     data[i]["Group"] = np.where(data[i]["Attribute"] == "Unknown", "", data[i]["Group"])

#     data[i]['Estimate'] = data[i]['Estimate'].round(0).astype(int)
#     data[i]["CI Upper"] = data[i]["CI Upper"].round(0).astype(int)
#     data[i]['cv'] = data[i]['cv'].round(2)

#     # if not data[i]["Attribute"].isna().all():
#     #     data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15, break_long_words=False)
#     #     data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)
#     #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Do not support<br>cause", "Do not support cause", data[i]["Attribute"])
#     #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Do not report<br>barrier", "Do not report barrier", data[i]["Attribute"])
#     #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Report<br>barrier", "Report barrier", data[i]["Attribute"])

#     data[i]["QuestionText"] = data[i]["QuestionText"].str.wrap(20, break_long_words=False)
#     data[i]["QuestionText"] = data[i]["QuestionText"].replace({'\n': '<br>'}, regex=True)

# region_values = np.array(['CA', 'BC', 'AB', 'PR', 'ON', 'QC', 'AT'], dtype=object)
# region_names = np.array(['Canada',
#                          'British Columbia',
#                          'Alberta',
#                          'Prairie Provinces (SK, MB)',
#                          'Ontario',
#                          'Quebec',
#                          'Atlantic Provinces (NB, NS, PE, NL)'], dtype=str)

# ###################### App layout ######################
# navbar = gen_navbar("giving_and_volunteering_by_seniors_2018")

# marginTop = 20


# layout = html.Div([
#     navbar,
#     html.Header([
#         html.Div(className='overlay'),
#         dbc.Container(
#             dbc.Row(
#                 html.Div(
#                     html.Div([
#                         html.H1('Les dons et le bénévolat des personnes agées (2018)'),
#                         #html.Span(
#                             #'David Lasby',
#                             #className='meta'
#                      #   )
#                         ],
#                         className='post-heading'
#                     ),
#                     className='col-md-10 col-lg-8 mx-auto position-relative'
#                 )
#             )
#         ),
#     ],
#         # className='masthead'
#         className="sub-header bg-secondary text-white text-center py-4",
#     ),
#     # Note: filters put in separate container to make floating element later
#     dbc.Container([
#         dbc.Row(
#            dbc.Col(
#                html.Div([
#                    "Select a region of focus:",
#                    dcc.Dropdown(
#                        id='region-selection',
#                        options=[{'label': region_names[i], 'value': region_values[i]} for i in range(len(region_values))],
#                        value='CA',
#                        ),
#                     html.Br(),
#                 ],className="m-2 p-2"),
#             ),id='sticky-dropdown'),
#     ],className='sticky-top select-region mb-2', fluid=True),
#    dbc.Container([
#        dbc.Row([
#             html.Div([
#                 html.H3('Dons'),
#                 dcc.Markdown("""
#                 D’après les données de l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, les personnes âgées sont plus enclines à donner, et à donner plus, que les personnes plus jeunes au Canada, ce qui est vrai pour les dons aux causes laïques comme aux causes religieuses. Tout comme leurs homologues plus jeunes, les personnes âgées ont plus tendance à donner à des causes laïques qu’à des causes religieuses. En revanche, elles donnent beaucoup plus d’argent, en moyenne, aux causes religieuses.
#                 """
#                 ),
#                 # Donation rate and average donation amount
#                 dcc.Graph(id='YouthDonRateAmt', style={'marginTop': marginTop}), 
#                 ], className='col-md-10 col-lg-8 mx-auto'
#             ),
#             html.Div([
#                 html.H4('Les dons selon la cause'),
#                 dcc.Markdown("""
#                 Les personnes âgées ont plus tendance que les personnes plus jeunes à donner de l’argent à la majorité des causes, mais les différences les plus importantes ont trait aux causes les plus populaires. À l’échelle nationale, entre 39 % et 46 % des personnes canadiennes âgées de 65 ans ou plus donnent aux organismes de santé et de services sociaux, par comparaison avec moins d’un tiers de celles âgées de 15 à 64 ans. Les personnes plus âgées ont également beaucoup plus tendance à donner de l’argent aux congrégations religieuses. Les taux de dons pour les autres causes sont similaires pour les divers groupes d’âge. 
#                 """),
#                 # Donation rate by cause
#                 dcc.Graph(id='YouthDonRateByCause', style={'marginTop': marginTop}), 
#                 dcc.Markdown("""
#                 Les personnes plus âgées donnent plus d’argent, en moyenne, aux causes qu’elles soutiennent, mais, dans la majorité des cas, les différences ne sont pas statistiquement significatives. 
#                 """),
#                 # Average amount donated by cause
#                 dcc.Graph(id='YouthAvgAmtByCause', style={'marginTop': marginTop}), 
#             ], className='col-md-10 col-lg-8 mx-auto'),
#             html.Div([
#                 html.H4('Méthodes de dons'),
#                 dcc.Markdown("""
#                 L’incidence de l’âge est évidente sur le choix des méthodes de dons. Par exemple, le don par courrier est la méthode préférée des personnes âgées de 75 ans ou plus et la deuxième méthode par ordre de préférence pour les personnes âgées de 65 à 74 ans, tandis que les dons par courrier sont relativement rares chez les personnes âgées de 15 à 64 ans. Les personnes âgées ont également significativement plus tendance à donner à un lieu de culte ou à la mémoire de quelqu’un et significativement moins tendance à donner en ligne. Les personnes âgées de 65 à 74 ans sont plus enclines que celles des groupes d’âge plus jeunes et plus âgés à parrainer quelqu’un ou à donner de l’argent en étant sollicitées à leur porte. 
#                 """),
#                 # Donation rate by method
#                 dcc.Graph(id='YouthDonRateByMeth', style={'marginTop': marginTop}), 
#                 dcc.Markdown("""
#                 Le montant moyen des dons des personnes canadiennes âgées de 65 ans ou plus est le plus élevé quand elles donnent de l’argent dans les lieux de culte et de leur propre initiative.
#                 """),
#                 # Average amount donated by method
#                 dcc.Graph(id='YouthAvgAmtByMeth', style={'marginTop': marginTop}), 
#                 ], className='col-md-10 col-lg-8 mx-auto'
#             ),
#             html.Div([
#                 html.H4('Motivations des dons'),
#                 dcc.Markdown("""
#                 En général, les personnes plus âgées donnent de l’argent pour les mêmes raisons que les personnes plus jeunes, la conviction du bien-fondé de la cause et la compassion envers les personnes dans le besoin étant les deux principales motivations des dons pour tous les groupes d’âge. Il existe cependant quelques différences. Les personnes plus âgées sont plus enclines que les personnes plus jeunes à donner de l’argent pour des raisons religieuses ou spirituelles ou parce qu’elles recevront un crédit d’impôt et moins enclines à donner après avoir été sollicitées par une personne de leur connaissance. Les personnes âgées de 65 à 74 ans sont plus enclines à donner de l’argent parce que la cause les touche personnellement que les personnes plus jeunes et que les personnes plus âgées.
#                 """),
#                 # Motivations for donating
#                 dcc.Graph(id='YouthMotivations', style={'marginTop': marginTop}), 
#                 ], className='col-md-10 col-lg-8 mx-auto'
#             ),
#             html.Div([
#                 html.H4('Freins à donner davantage'),
#                 dcc.Markdown("""
#                 Les personnes plus âgées ont nettement plus tendance que les personnes plus jeunes à déclarer ne pas avoir donné plus parce qu’elles étaient satisfaites du montant de leurs dons ou parce qu’elles avaient donné directement aux personnes dans le besoin. L’âge ne semble pas avoir une grande incidence sur les autres freins à donner davantage.
#                 """),
#                 # Barriers to donating more
#                 dcc.Graph(id='YouthBarriers', style={'marginTop': marginTop}), 
#                 html.Div([
#                     html.H5('Préoccupations relatives à l’efficience'),
#                     dcc.Markdown("""
#                     Les personnes plus âgées ont relativement plus tendance que les personnes plus jeunes à déclarer ne pas avoir donné plus parce qu’elles ne croyaient pas que leur argent serait utilisé avec efficience. Cette préoccupation semble principalement liée à leur conviction que trop d’argent est dépensé pour les collectes de fonds.
#                     """),
#                     # Reasons for concern about efficiency
#                     dcc.Graph(id='YouthEfficiency', style={'marginTop': marginTop}), 
#                     ]),
#                 html.Div([
#                     html.H5('Préoccupations relatives aux sollicitations'),
#                     dcc.Markdown("""
#                     Les personnes plus âgées ont également plus tendance à déclarer ne pas avoir donné plus parce qu’elles n’aimaient pas les méthodes de sollicitation. Cette préoccupation semble principalement liée au nombre de demandes de don qu’elles reçoivent.
#                     """),
#                     # Reasons for disliking solicitations
#                     dcc.Graph(id='YouthSolicitations', style={'marginTop': marginTop}), 
#                     ]),
#                 ], className='col-md-10 col-lg-8 mx-auto'
#             ),
#         ]),
#        dbc.Row([
#             html.Div([
#                 html.H3('Bénévolat'),
#                 dcc.Markdown("""
#                 D’après les données de l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, les personnes plus âgées sont moins susceptibles de faire du bénévolat que les personnes plus jeunes au Canada. En revanche, les personnes plus âgées font don d’un nombre d’heures de bénévolat beaucoup plus important, en moyenne, que les bénévoles plus jeunes. À l’échelle nationale, les personnes canadiennes âgées de 75 ans ou plus qui font du bénévolat (30 % de ce groupe d’âge) font don en moyenne de 223 heures par année, tandis que les personnes canadiennes âgées de 15 à 64 ans qui font du bénévolat (42 % de ce groupe d’âge) font don en moyenne de 181 heures. Les personnes canadiennes âgées de 65 à 74 ans se situent entre le groupe d’âge plus jeune et le groupe d’âge plus âgé, à la fois pour leur taux et pour leur nombre moyen d’heures de bénévolat. Les personnes âgées de 75 ans ou plus ont moins tendance à aider autrui directement que les personnes âgées de moins de 75 ans (c.-à-d. en dehors d’un groupe ou d’un organisme) ou à pratiquer d’autres formes d’engagement communautaire. 
#                 """),
#                 # Rates and average hours devoted to volunteering, helping others and community engagement
#                 dcc.Graph(id='YouthVolRateVolAmt', style={'marginTop': marginTop}), 
#                 ], className='col-md-10 col-lg-8 mx-auto'
#             ),
#             html.Div([
#                 html.H4('Bénévolat selon la cause'),
#                 dcc.Markdown("""
#                 Les personnes âgées de 65 ans ou plus sont plus enclines à faire du bénévolat pour les congrégations religieuses, les organismes de services sociaux et les organismes des sports et des loisirs. Par comparaison avec les personnes âgées de 15 à 64 ans, celles âgées de 65 ans ou plus sont plus susceptibles de faire du bénévolat pour les organismes religieux et les hôpitaux. Elles sont moins susceptibles de faire du bénévolat pour les organismes d’éducation et de recherche, des sports et des loisirs et pour les universités et les collèges. 
#                 """),
#                 # Volunteer rate by cause
#                 dcc.Graph(id='YouthVolRateByCause', style={'marginTop': marginTop}), 
#                 dcc.Markdown("""
#                 En raison de la grande variation des heures de bénévolat, la prudence est de rigueur pour interpréter les données. Par exemple, bien qu’il semble que, à l’échelle nationale, les personnes plus âgées font don d’un plus grand nombre d’heures de bénévolat à la plupart des types d’organismes, un grand nombre de ces différences ne sont pas statistiquement significatives. En revanche, les personnes plus âgées font don d’un nombre d’heures de bénévolat significativement plus élevé aux organismes des arts et de la culture, aux hôpitaux, aux organismes des sports et des loisirs, aux organismes de services sociaux et aux organismes du développement et du logement.
#                 """),
#                 # Average hours volunteered by cause
#                 dcc.Graph(id='YouthAvgHrsByCause', style={'marginTop': marginTop}), 
#             ], className='col-md-10 col-lg-8 mx-auto'),
#             html.Div([
#                 html.H4('Activités des bénévoles'),
#                 dcc.Markdown("""
#                 La probabilité de participer à des activités bénévoles décroît avec l’âge. Par exemple, les personnes âgées de 75 ans ou plus sont moins susceptibles d’organiser des activités ou des événements et de collecter des fonds bénévolement que celles âgées de 65 à 74 ans et ces dernières sont moins susceptibles de pratiquer ces activités que les personnes âgées de 15 à 64 ans. En revanche, les bénévoles de 65 à 74 ans ont plus tendance à siéger à des comités ou à des conseils d’administration ou à faire du travail administratif que les bénévoles plus jeunes et plus âgés. 
#                 """),
#                 # Volunteer rate by activity
#                 dcc.Graph(id='YouthVolRateByActivity', style={'marginTop': marginTop}), 
#                 dcc.Markdown("""
#                 Sur le plan du nombre moyen d’heures consacrées aux diverses activités, les bénévoles de 65 ans ou plus consacrent moins d’heures, en moyenne, que les bénévoles de 15 à 64 ans à faire du travail de bureau, à offrir des soins de santé ou du soutien, à collecter, à offrir ou à livrer des marchandises, à organiser des activités et des événements, à conduire bénévolement et à collecter des fonds. 
#                 """),
#                 # Average hours volunteered by activity
#                 dcc.Graph(id='YouthAvgHrsByActivity', style={'marginTop': marginTop}), 
            
#                 ], className='col-md-10 col-lg-8 mx-auto'
#             ),
#             html.Div([
#                 html.H4('Motivations du bénévolat'),
#                 dcc.Markdown("""
#                 Les personnes plus âgées ont tendance à faire du bénévolat pour les mêmes raisons que les personnes plus jeunes. Par exemple, apporter une contribution à la communauté et utiliser leurs compétences sont les deux principales motivations du bénévolat pour tous les groupes d’âge. Cela dit, il existe plusieurs différences. Les personnes plus âgées ont plus tendance à déclarer faire du bénévolat pour améliorer leur santé et leur bien-être, pour réseauter et rencontrer des personnes ou pour des raisons spirituelles ou religieuses. Les personnes âgées de 75 ans ou plus ont davantage tendance à déclarer faire du bénévolat parce que leurs connaissances en font. 
#                 """),
#                 # Motivations for volunteering
#                 dcc.Graph(id='YouthVolMotivations', style={'marginTop': marginTop}), 
#                 ], className='col-md-10 col-lg-8 mx-auto'
#             ),
#             html.Div([
#                 html.H4('Freins au bénévolat'),
#                 dcc.Markdown("""
#                 Malgré la tendance à l’uniformité du classement général des freins au bénévolat entre les divers groupes d’âge, il existe d’importantes différences entre ceux-ci. Les personnes plus âgées ont moins tendance que les bénévoles plus jeunes à déclarer manquer de temps pour faire du bénévolat et ne pas savoir comment s’impliquer. En revanche, elles ont plus tendance à penser avoir déjà donné suffisamment de leur temps, à déclarer que plus de bénévolat ne présente aucun intérêt pour elles et à avoir des problèmes de santé qui les empêchent d’en faire plus.
#                 """),
#                 # Barriers to volunteering more
#                 dcc.Graph(id='YouthVolBarriers', style={'marginTop': marginTop}), 
#                 ], className='col-md-10 col-lg-8 mx-auto'
#             ),
#             html.Div([
#                 html.H4('Aide directe d’autrui '),
#                 dcc.Markdown("""
#                 Les personnes plus âgées sont plus enclines à aider directement autrui en cuisinant, en faisant le ménage et d’autres tâches à domicile, en magasinant, en conduisant ou en accompagnant des personnes aux magasins ou à des rendez-vous et en offrant des soins en santé ou personnels. Les personnes âgées de 65 à 74 ans sont plus enclines que celles âgées de 75 ans ou plus à offrir tous les types d’aide directe. 
#                 """),
#                 # Methods of helping others directly
#                 dcc.Graph(id='YouthRateHelpDirect', style={'marginTop': marginTop}),
#                 dcc.Markdown("""
#                 Les personnes âgées de 65 ans ou plus consacrent plus de temps, en moyenne, à aider autrui directement que leurs homologues plus jeunes. Les différences les plus importantes concernent les soins liés à la santé ou personnels, cuisiner, faire le ménage ou les autres corvées ménagères, et magasiner, conduire ou accompagner d’autres personnes aux magasins ou à des rendez-vous. 
#                 """),
#                 # Average hours devoted to means of helping others directly
#                 dcc.Graph(id='YouthHrsHelpDirect', style={'marginTop': marginTop}), 
#                 ], className='col-md-10 col-lg-8 mx-auto'
#             ),
#             html.Div([
#                 html.H4('Engagement communautaire'),
#                 dcc.Markdown("""
#                 Sur le plan des activités visant à améliorer la communauté, les personnes âgées de 65 ans et plus sont plus enclines que les personnes plus jeunes à participer à des réunions publiques, mais moins enclines à participer à la plupart des autres types d’activités. 
#                 """),
#                 # Types of community engagement
#                 dcc.Graph(id='YouthRateCommInvolve', style={'marginTop': marginTop}), 
#                 dcc.Markdown("""
#                 L’âge n’a pas une incidence significative sur le nombre moyen d’heures consacrées aux diverses formes d’engagement communautaire au Canada.
#                 """),
#                 # Average hours devoted to forms of community engagement
#                 dcc.Graph(id='YouthHrsCommInvolve', style={'marginTop': marginTop}), 
#                 ], className='col-md-10 col-lg-8 mx-auto'
#             ),
#         ]),
#    ]),
#    footer
# ])
