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
from utils.gen_navbar import gen_navbar

####################### Data processing ######################
NewCanadiansAvgDonAmt_2018 = get_dataframe("2018-NewCanadiansAvgDonAmt.csv")
NewCanadiansAvgDonByCause_2018 = get_dataframe("2018-NewCanadiansAvgDonByCause.csv")
NewCanadiansAvgDonByMeth_2018 = get_dataframe("2018-NewCanadiansAvgDonByMeth.csv")
NewCanadiansAvgHrs_2018 = get_dataframe("2018-NewCanadiansAvgHrs.csv")
NewCanadiansAvgHrsByActivity_2018 = get_dataframe("2018-NewCanadiansAvgHrsByActivity.csv")
NewCanadiansAvgHrsByCause_2018 = get_dataframe("2018-NewCanadiansAvgHrsByCause.csv")
NewCanadiansAvgHrsCommInvolve_2018 = get_dataframe("2018-NewCanadiansAvgHrsCommInvolve.csv")
NewCanadiansAvgHrsHelpDirectly_2018 = get_dataframe("2018-NewCanadiansAvgHrsHelpDirectly.csv")
NewCanadiansBarriers_2018 = get_dataframe("2018-NewCanadiansBarriersGiving.csv")
NewCanadiansBarriersVol_2018 = get_dataframe("2018-NewCanadiansBarriersVol.csv")
NewCanadiansCommInvolveRate_2018 = get_dataframe("2018-NewCanadiansCommInvolveRate.csv")
NewCanadiansDonRateByCause_2018 = get_dataframe("2018-NewCanadiansDonRateByCause.csv")
NewCanadiansDonRateByMeth_2018 = get_dataframe("2018-NewCanadiansDonRateByMeth.csv")
NewCanadiansDonRates_2018 = get_dataframe("2018-NewCanadiansDonRates.csv")
NewCanadiansEfficiencyConcerns_2018 = get_dataframe("2018-NewCanadiansEfficiencyConcerns.csv")
NewCanadiansHelpDirectlyRate_2018 = get_dataframe("2018-NewCanadiansHelpDirectlyRate.csv")
NewCanadiansReasonsGiving_2018 = get_dataframe("2018-NewCanadiansReasonsGiving.csv")
NewCanadiansReasonsVol_2018 = get_dataframe("2018-NewCanadiansReasonsVol.csv")
NewCanadiansSolicitationConcerns_2018 = get_dataframe("2018-NewCanadiansSolicitationConcerns.csv")
NewCanadiansVolRateByActivity_2018 = get_dataframe("2018-NewCanadiansVolRateByActivity.csv")
NewCanadiansVolRateByCause_2018 = get_dataframe("2018-NewCanadiansVolRateByCause.csv")
NewCanadiansVolRate_2018 = get_dataframe("2018-NewCanadiansVolRates.csv")

rates = [NewCanadiansBarriers_2018,
         NewCanadiansBarriersVol_2018,
         NewCanadiansCommInvolveRate_2018,
         NewCanadiansDonRateByCause_2018,
         NewCanadiansDonRateByMeth_2018,
         NewCanadiansDonRates_2018,
         NewCanadiansEfficiencyConcerns_2018,
         NewCanadiansHelpDirectlyRate_2018,
         NewCanadiansReasonsGiving_2018,
         NewCanadiansReasonsVol_2018,
         NewCanadiansSolicitationConcerns_2018,
         NewCanadiansVolRateByActivity_2018,
         NewCanadiansVolRateByCause_2018,
         NewCanadiansVolRate_2018]

data = [NewCanadiansAvgDonAmt_2018,
        NewCanadiansAvgDonByCause_2018,
        NewCanadiansAvgDonByMeth_2018,
        NewCanadiansAvgHrs_2018,
        NewCanadiansAvgHrsByActivity_2018,
        NewCanadiansAvgHrsByCause_2018,
        NewCanadiansAvgHrsCommInvolve_2018,
        NewCanadiansAvgHrsHelpDirectly_2018,
        NewCanadiansBarriers_2018,
        NewCanadiansBarriersVol_2018,
        NewCanadiansCommInvolveRate_2018,
        NewCanadiansDonRateByCause_2018,
        NewCanadiansDonRateByMeth_2018,
        NewCanadiansDonRates_2018,
        NewCanadiansEfficiencyConcerns_2018,
        NewCanadiansHelpDirectlyRate_2018,
        NewCanadiansReasonsGiving_2018,
        NewCanadiansReasonsVol_2018,
        NewCanadiansSolicitationConcerns_2018,
        NewCanadiansVolRateByActivity_2018,
        NewCanadiansVolRateByCause_2018,
        NewCanadiansVolRate_2018]

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
    #     data[i]["Attribute"] = data[i]["Attribute"].str.wrap(15, break_long_words=False)
    #     data[i]["Attribute"] = data[i]["Attribute"].replace({'\n': '<br>'}, regex=True)
    #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Do not support<br>cause", "Do not support cause", data[i]["Attribute"])
    #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Do not report<br>barrier", "Do not report barrier", data[i]["Attribute"])
    #     data[i]["Attribute"] = np.where(data[i]["Attribute"] == "Report<br>barrier", "Report barrier", data[i]["Attribute"])

    data[i]["QuestionText"] = data[i]["QuestionText"].str.wrap(20, break_long_words=False)
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

navbar = gen_navbar("giving_and_volunteering_among_new_canadians")

marginTop = 20

layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1('Les dons et le bénévolat des personnes nouvellement arrivées au canada (2018)'),
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
        className="sub-header bg-secondary text-white text-center pt-5",
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
    ],className='sticky-top select-region mb-2', fluid=True),
   dbc.Container([
       dbc.Row([
            html.Div([
                html.H3('Dons'),
                dcc.Markdown("""
                D’après les données de l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, les personnes nouvellement arrivées au Canada et, plus particulièrement, celles qui n’ont pas encore obtenu la citoyenneté canadienne, sont relativement moins susceptibles de donner aux organismes de bienfaisance et à but non lucratif que les personnes nées au Canada. En revanche, les personnes naturalisées donnent légèrement plus, en moyenne, que les personnes nées au Canada et beaucoup plus que les personnes non citoyennes. Tout comme les personnes nées au Canada, les personnes nouvellement arrivées sont beaucoup plus enclines à donner à des causes laïques qu’à des causes religieuses, mais donnent plus d’argent, en moyenne, aux causes religieuses. 
                """
                ),
                # Donation rate and average donation amount
                dcc.Graph(id='YouthDonRateAmt', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Les dons selon la cause'),
                dcc.Markdown("""
                Les deux principaux bénéficiaires des dons des personnes nouvellement arrivées sont les congrégations religieuses et les organismes de services sociaux, suivis par les organismes de santé et les hôpitaux. Les deux principaux bénéficiaires des dons des personnes nées au Canada sont les organismes de santé et de services sociaux, suivis par les congrégations religieuses et les hôpitaux. 
                """),
                # Donation rate by cause
                dcc.Graph(id='YouthDonRateByCause', style={'marginTop': marginTop}), 
                dcc.Markdown("""
                Les personnes nouvellement arrivées au Canada donnent moins, en moyenne à la majorité des causes que les personnes nées au Canada, bien que, dans de nombreux cas, les différences ne soient pas statistiquement significatives. Les personnes naturalisées donnent plus, en moyenne, aux congrégations religieuses et aux organismes de santé que les personnes non citoyennes. 
                """),
                # Average amount donated by cause
                dcc.Graph(id='YouthAvgAmtByCause', style={'marginTop': marginTop}), 
            ], className='col-md-10 col-lg-8 mx-auto'),
            html.Div([
                html.H4('Méthodes de dons'),
                dcc.Markdown("""
                Les personnes nouvellement arrivées sont moins enclines que les personnes nées au Canada à donner après avoir été sollicitées dans un lieu public, pour parrainer quelqu’un, à la mémoire de quelqu’un ou à leur porte. Les personnes non citoyennes donnent moins fréquemment que les personnes citoyennes de leur propre initiative, au travail ou par courrier. Les personnes naturalisées ont plus tendance que les personnes non citoyennes et les personnes nées au Canada à donner à un lieu de culte.  
                """),
                # Donation rate by method
                dcc.Graph(id='YouthDonRateByMeth', style={'marginTop': marginTop}), 
                dcc.Markdown("""
                Le montant moyen des dons des personnes nouvellement arrivées au Canada est le plus élevé quand elles donnent de l’argent dans les lieux de culte.
                """),
                # Average amount donated by method
                dcc.Graph(id='YouthAvgAmtByMeth', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Motivations des dons'),
                dcc.Markdown("""
                En général, les personnes nouvellement arrivées donnent de l’argent pour les mêmes raisons que les personnes nées au Canada, la compassion envers les personnes dans le besoin et la conviction du bien-fondé de la cause étant les deux principales motivations des dons pour tous les groupes. Les personnes naturalisées sont nettement moins enclines à donner parce que la cause les touche personnellement et beaucoup plus enclines à donner pour des raisons religieuses ou spirituelles.
                """),
                # Motivations for donating
                dcc.Graph(id='YouthMotivations', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Freins à donner davantage'),
                dcc.Markdown("""
                Les personnes nouvellement arrivées citent généralement les mêmes freins à donner davantage que les personnes nées au Canada. Tous les groupes de donateur.trice.s. expliquent le plus souvent qu’ils ne peuvent pas donner plus parce que leurs moyens financiers ne leur permettent pas et qu’ils sont satisfaits du montant de leurs dons. Les personnes naturalisées ont plus tendance que les autres à déclarer ne pas avoir donné plus parce qu’elles ne pensaient pas que l’argent serait utilisé efficacement. Les personnes non citoyennes ont plus tendance que les autres à déclarer ne pas avoir donné parce qu’elles n’aimaient pas la méthode de sollicitation. 
                """),
                # Barriers to donating more
                dcc.Graph(id='YouthBarriers', style={'marginTop': marginTop}), 
                html.Div([
                    html.H5('Préoccupations relatives à l’efficience'),
                    dcc.Markdown("""
                    La préoccupation des personnes naturalisées à l’égard de l’utilisation efficiente des dons semble principalement liée aux explications données à ce sujet.
                    """),
                    # Reasons for concern about efficiency
                    dcc.Graph(id='YouthEfficiency', style={'marginTop': marginTop}), 
                    ]),
                html.Div([
                    html.H5('Préoccupations relatives aux sollicitations'),
                    dcc.Markdown("""
                    La préoccupation des personnes non citoyennes à l’égard des méthodes de sollicitation des dons semble liée à plusieurs questions, dont la méthode de prise de contact, le nombre total de demandes et le nombre de demandes provenant du même organisme. 
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
                D’après les données de l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, les personnes nouvellement arrivées sont toutes aussi enclines que les personnes nées au Canada à faire du bénévolat et à s’engager dans la communauté par d’autres moyens. En moyenne, elles font également don d’un nombre d’heures comparable pour ces activités. Au niveau national, les personnes naturalisées ont moins tendance à faire du bénévolat que les personnes citoyennes nées au Canada, ce qui constitue la seule différence statistiquement significative. Les différences sont plus nombreuses en ce qui concerne l’aide directe d’autrui (c.-à-d. en dehors d’un groupe ou d’un organisme). Les personnes naturalisées sont moins susceptibles d’aider d’autres personnes directement et consacrent moins d’heures à cette fin, en moyenne, que les personnes citoyennes nées au Canada. Les personnes non citoyennes ont à peu près autant tendance à aider directement autrui que les personnes naturalisées, mais y consacrent nettement moins de temps, en moyenne. 
                """),
                # Rates and average hours devoted to volunteering, helping others and community engagement
                dcc.Graph(id='YouthVolRateVolAmt', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Bénévolat selon la cause'),
                dcc.Markdown("""
                Les personnes naturalisées ont plus tendance à faire du bénévolat pour les congrégations religieuses que les personnes citoyennes nées au Canada et moins tendance à faire don de leur temps aux organismes de services sociaux, des sports et des loisirs, et d’éducation et de recherche. 
                """),
                # Volunteer rate by cause
                dcc.Graph(id='YouthVolRateByCause', style={'marginTop': marginTop}), 
                dcc.Markdown("""
                Sur le plan du nombre moyen d’heures de bénévolat à l’appui des diverses causes, les données n’indiquent aucune différence statistiquement significative entre les personnes nouvellement arrivées et les personnes nées au Canada.  
                """),
                # Average hours volunteered by cause
                dcc.Graph(id='YouthAvgHrsByCause', style={'marginTop': marginTop}), 
            ], className='col-md-10 col-lg-8 mx-auto'),
            html.Div([
                html.H4('Activités des bénévoles'),
                dcc.Markdown("""
                Les personnes nouvellement arrivées sont les plus enclines à organiser des activités ou des événements, à collecter des fonds, à siéger à des comités ou à des conseils d’administration et à enseigner ou à mentorer bénévolement. Les personnes naturalisées ont moins tendance à faire du bénévolat pour toutes ces activités que les personnes citoyennes nées au Canada. Les personnes non citoyennes ont moins tendance que les personnes citoyennes nées au Canada à participer bénévolement aux collectes de fonds. La majorité des autres différences dans le taux de bénévolat pour diverses activités ne sont pas statistiquement significatives. 
                """),
                # Volunteer rate by activity
                dcc.Graph(id='YouthVolRateByActivity', style={'marginTop': marginTop}), 
                dcc.Markdown("""
                En moyenne, les personnes nouvellement arrivées consacrent le plus d’heures de bénévolat aux soins ou au soutien en santé, à l’enseignement ou au mentorat et au travail de bureau. Les personnes naturalisées consacrent moins d’heures, en moyenne, que les personnes citoyennes nées au Canada à plusieurs activités bénévoles, dont l’entraînement, la lutte contre les incendies et la conduite de véhicules. Les personnes non citoyennes consacrent moins d’heures de bénévolat, en moyenne, aux collectes de fonds que les personnes citoyennes nées au Canada. 
                """),
                # Average hours volunteered by activity
                dcc.Graph(id='YouthAvgHrsByActivity', style={'marginTop': marginTop}), 
            
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Motivations du bénévolat'),
                dcc.Markdown("""
                Les personnes nouvellement arrivées ont tendance à faire du bénévolat pour les mêmes raisons que les personnes nées au Canada. Par exemple, apporter une contribution à la communauté et utiliser leurs compétences sont les deux principales motivations du bénévolat pour tous les groupes. Cela dit, il existe plusieurs différences. Les personnes naturalisées sont plus susceptibles de faire du bénévolat pour améliorer leur santé et leur bien-être, pour réseauter et rencontrer de nouvelles personnes, pour prendre conscience de leurs points forts personnels ou pour des raisons spirituelles et religieuses que les personnes citoyennes nées au Canada. Ces personnes ont moins tendance à faire du bénévolat parce que la cause les touche personnellement. Les personnes non citoyennes ont plus tendance à faire du bénévolat pour réseauter et pour faire la connaissance de nouvelles personnes que les personnes citoyennes nées au Canada.
                """),
                # Motivations for volunteering
                dcc.Graph(id='YouthVolMotivations', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Freins au bénévolat'),
                dcc.Markdown("""
                Le manque de temps constitue, et de loin, le frein au bénévolat le plus répandu chez les personnes nées au Canada, naturalisées et non canadiennes, suivi par l’impossibilité de s’engager à long terme à faire du bénévolat et par la conviction d’avoir déjà donné suffisamment de leur temps. Quant aux différences entre les groupes, les personnes naturalisées et celles qui ne sont pas citoyennes ont relativement plus tendance à limiter leur bénévolat parce qu’elles ne savent pas comment s’impliquer et parce qu’elles ne pensent pas que le bénévolat leur permet d’utiliser leurs compétences.. 
                """),
                # Barriers to volunteering more
                dcc.Graph(id='YouthVolBarriers', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Aide directe d’autrui '),
                dcc.Markdown("""
                Les personnes nouvellement arrivées sont les plus enclines à aider directement autrui en cuisinant, en faisant le ménage ou diverses autres tâches à domicile, en magasinant, en conduisant ou en accompagnant des personnes aux magasins ou à des rendez-vous et en offrant des soins en santé ou personnels. Les personnes naturalisées sont moins tendance à cuisiner, à nettoyer ou à faire d’autres corvées ménagères et à offrir des soins en santé ou personnels que les personnes citoyennes nées au Canada. Les personnes non citoyennes ont moins tendance à offrir des soins liés à la santé ou personnels, mais ont plus tendance à aider autrui en enseignant, en entraînant ou en offrant une aide à la lecture que les personnes nées au Canada.
                """),
                # Methods of helping others directly
                dcc.Graph(id='YouthRateHelpDirect', style={'marginTop': marginTop}),
                dcc.Markdown("""
                En ce qui concerne le nombre moyen d’heures consacrées à aider directement autrui, c’est aux soins liés à la santé et personnels que les personnes naturalisées consacrent le plus d’heures. Les personnes non citoyennes, en revanche, consacrent le plus d’heures à l’enseignement, l’entraînement ou à l’aide à la lecture. En moyenne, les personnes naturalisées et les personnes non citoyennes, consacrent moins d’heures à cuisiner, à nettoyer ou à faire d’autres corvées ménagères pour aider autrui que les personnes nées au Canada. Les personnes non citoyennes consacrent moins de temps en moyenne, à offrir des soins liés à la santé ou personnels, à magasiner ou à conduire et aux formalités administratives et aux déclarations d’impôt que les personnes citoyennes nées au Canada.
                """),
                # Average hours devoted to means of helping others directly
                dcc.Graph(id='YouthHrsHelpDirect', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Engagement communautaire'),
                dcc.Markdown("""
                Sur le plan des activités visant à améliorer la communauté, les personnes nouvellement arrivées au Canada sont les plus susceptibles de créer ou de diffuser de l’information pour sensibiliser les autres personnes à un enjeu, d’organiser ou de coordonner des événements et de participer à des réunions publiques. Les personnes naturalisées ont moins tendance à créer ou à diffuser de l’information, mais plus tendance à organiser ou à coordonner un événement que les personnes nées au Canada. 
                """),
                # Types of community engagement
                dcc.Graph(id='YouthRateCommInvolve', style={'marginTop': marginTop}), 
                dcc.Markdown("""
                Les personnes nouvellement arrivées consacrent à peu près le même nombre d’heures aux divers types d’engagement communautaire que les personnes nées au Canada.
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
                                          ["Volunteering", "Helping others", "Community engagement"])
        dff_2['QuestionText'] = np.select([dff_2["QuestionText"] == 'Total formal<br>volunteer hours', dff_2["QuestionText"] == 'Total hours spent<br>helping directly', dff_2["QuestionText"] == 'Total hours spent on<br>community<br>involvement'],
                                          ["Volunteering", "Helping others", "Community engagement"])

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
                         marker=dict(color="#FD7B5F"),
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
                         marker=dict(color="#234C66"),
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
                         marker=dict(color="#0B6623"),
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
                         marker=dict(color="#FD7B5F"),
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
                         marker=dict(color="#234C66"),
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
                         marker=dict(color="#0B6623"),
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
                         marker=dict(color="#FD7B5F"),
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
                         marker=dict(color="#234C66"),
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
                         marker=dict(color="#0B6623"),
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
    dash.dependencies.Output('NewCanadiansDonRateAmt', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = NewCanadiansDonRates_2018[NewCanadiansDonRates_2018['Region'] == region]

    dff2 = NewCanadiansAvgDonAmt_2018[NewCanadiansAvgDonAmt_2018['Region'] == region]

    name1 = "Native-born"
    name2 = "Naturalized"
    name3 = "Non-Canadian"
    title = '{}, {}'.format("Donation rate and average donation amount", region)
    return triple_horizontal_rate_avg(dff1, dff2, name1, name2, name3, title, giving=True)


@app.callback(
    dash.dependencies.Output('NewCanadiansDonRateByCause', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = NewCanadiansDonRateByCause_2018[NewCanadiansDonRateByCause_2018['Region'] == region]

    name1 = "Native-born"
    name2 = "Naturalized"
    name3 = "Non-Canadian"
    title = '{}, {}'.format("Donation rate by cause", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('NewCanadiansAvgAmtByCause', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = NewCanadiansAvgDonByCause_2018[NewCanadiansAvgDonByCause_2018['Region'] == region]

    name1 = "Native-born"
    name2 = "Naturalized"
    name3 = "Non-Canadian"
    title = '{}, {}'.format("Average amount donated by cause", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "dollar")


@app.callback(
    dash.dependencies.Output('NewCanadiansDonRateByMeth', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = NewCanadiansDonRateByMeth_2018[NewCanadiansDonRateByMeth_2018['Region'] == region]

    name1 = "Native-born"
    name2 = "Naturalized"
    name3 = "Non-Canadian"
    title = '{}, {}'.format("Donation rate by method", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('NewCanadiansAvgAmtByMeth', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = NewCanadiansAvgDonByMeth_2018[NewCanadiansAvgDonByMeth_2018['Region'] == region]

    name1 = "Native-born"
    name2 = "Naturalized"
    name3 = "Non-Canadian"
    title = '{}, {}'.format("Donation rate by method", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "dollar")


@app.callback(
    dash.dependencies.Output('NewCanadiansMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = NewCanadiansReasonsGiving_2018[NewCanadiansReasonsGiving_2018['Region'] == region]

    name1 = "Native-born"
    name2 = "Naturalized"
    name3 = "Non-Canadian"
    title = '{}, {}'.format("Motivations for donating", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('NewCanadiansBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = NewCanadiansBarriers_2018[NewCanadiansBarriers_2018['Region'] == region]

    name1 = "Native-born"
    name2 = "Naturalized"
    name3 = "Non-Canadian"
    title = '{}, {}'.format("Barriers to donating more", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('NewCanadiansEfficiency', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = NewCanadiansEfficiencyConcerns_2018[NewCanadiansEfficiencyConcerns_2018['Region'] == region]

    name1 = "Native-born"
    name2 = "Naturalized"
    name3 = "Non-Canadian"
    title = '{}, {}'.format("Reasons for concern about efficiency", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('NewCanadiansSolicitations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = NewCanadiansSolicitationConcerns_2018[NewCanadiansSolicitationConcerns_2018['Region'] == region]

    name1 = "Native-born"
    name2 = "Naturalized"
    name3 = "Non-Canadian"
    title = '{}, {}'.format("Reasons for disliking solicitations", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")



@app.callback(
    dash.dependencies.Output('NewCanadiansVolRateVolAmt', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = NewCanadiansVolRate_2018[NewCanadiansVolRate_2018['Region'] == region]

    dff2 = NewCanadiansAvgHrs_2018[NewCanadiansAvgHrs_2018['Region'] == region]

    name1 = "Native-born"
    name2 = "Naturalized"
    name3 = "Non-Canadian"
    title = '{}, {}'.format("Rates and average hours devoted to volunteering, helping others and community engagement", region)
    return triple_horizontal_rate_avg(dff1, dff2, name1, name2, name3, title, giving=False)


@app.callback(
    dash.dependencies.Output('NewCanadiansVolRateByCause', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = NewCanadiansVolRateByCause_2018[NewCanadiansVolRateByCause_2018['Region'] == region]

    name1 = "Native-born"
    name2 = "Naturalized"
    name3 = "Non-Canadian"
    title = '{}, {}'.format("Volunteer rate by cause", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('NewCanadiansAvgHrsByCause', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = NewCanadiansAvgHrsByCause_2018[NewCanadiansAvgHrsByCause_2018['Region'] == region]

    name1 = "Native-born"
    name2 = "Naturalized"
    name3 = "Non-Canadian"
    title = '{}, {}'.format("Average hours volunteered by cause", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "hours")


@app.callback(
    dash.dependencies.Output('NewCanadiansVolRateByActivity', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = NewCanadiansVolRateByActivity_2018[NewCanadiansVolRateByActivity_2018['Region'] == region]

    name1 = "Native-born"
    name2 = "Naturalized"
    name3 = "Non-Canadian"
    title = '{}, {}'.format("Volunteer rate by activity", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('NewCanadiansAvgHrsByActivity', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = NewCanadiansAvgHrsByActivity_2018[NewCanadiansAvgHrsByActivity_2018['Region'] == region]


    name1 = "Native-born"
    name2 = "Naturalized"
    name3 = "Non-Canadian"
    title = '{}, {}'.format("Average hours volunteered by activity", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "hours")


@app.callback(
    dash.dependencies.Output('NewCanadiansVolMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = NewCanadiansReasonsVol_2018[NewCanadiansReasonsVol_2018['Region'] == region]

    name1 = "Native-born"
    name2 = "Naturalized"
    name3 = "Non-Canadian"
    title = '{}, {}'.format("Motivations for volunteering", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('NewCanadiansVolBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = NewCanadiansBarriersVol_2018[NewCanadiansBarriersVol_2018['Region'] == region]

    name1 = "Native-born"
    name2 = "Naturalized"
    name3 = "Non-Canadian"
    title = '{}, {}'.format("Barriers to volunteering more", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('NewCanadiansRateHelpDirect', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = NewCanadiansHelpDirectlyRate_2018[NewCanadiansHelpDirectlyRate_2018['Region'] == region]

    name1 = "Native-born"
    name2 = "Naturalized"
    name3 = "Non-Canadian"
    title = '{}, {}'.format("Methods of helping others directly", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('NewCanadiansHrsHelpDirect', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = NewCanadiansAvgHrsHelpDirectly_2018[NewCanadiansAvgHrsHelpDirectly_2018['Region'] == region]

    name1 = "Native-born"
    name2 = "Naturalized"
    name3 = "Non-Canadian"
    title = '{}, {}'.format("Average hours devoted to means of helping others directly", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "hours")


@app.callback(
    dash.dependencies.Output('NewCanadiansRateCommInvolve', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = NewCanadiansCommInvolveRate_2018[NewCanadiansCommInvolveRate_2018['Region'] == region]

    name1 = "Native-born"
    name2 = "Naturalized"
    name3 = "Non-Canadian"
    title = '{}, {}'.format("Types of community engagement", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "percent")


@app.callback(
    dash.dependencies.Output('NewCanadiansHrsCommInvolve', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = NewCanadiansAvgHrsCommInvolve_2018[NewCanadiansAvgHrsCommInvolve_2018['Region'] == region]

    name1 = "Native-born"
    name2 = "Naturalized"
    name3 = "Non-Canadian"
    title = '{}, {}'.format("Average hours devoted to forms of community engagement", region)
    return triple_vertical_graphs_pops(dff, title, name1, name2, name3, "hours")

