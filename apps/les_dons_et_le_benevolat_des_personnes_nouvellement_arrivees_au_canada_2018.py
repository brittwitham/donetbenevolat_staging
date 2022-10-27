import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc
import os
import os.path as op

from utils.graphs.WTO0207_graph_utils import rate_avg_cause, single_vertical_percentage_graph
from utils.data.WTO0207_data_utils import get_data, process_data, get_region_names, get_region_values

from app import app
from homepage import footer #navbar, footer

####################### Data processing ######################
BarriersVol_2018, SubSecAvgHrs_2018, SubSecVolRates_2018, AllocationVol_2018 = get_data()

data = [SubSecVolRates_2018, SubSecAvgHrs_2018, AllocationVol_2018]
process_data(data)

region_values = get_region_values()
region_names = get_region_names()
region_names = ['CA', 'BC', 'AB', 'PR', 'ON', 'QC', 'AT']
###################### App layout ######################
navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                # dcc.Link("Home", href="/")
                dbc.NavLink("À propos", href="https://www.donetbenevolat.ca/",external_link=True)
            ),
            dbc.NavItem(
                dbc.NavLink("EN", href="http://app.givingandvolunteering.ca/What_types_of_organizations_do_Canadians_volunteer_for_2018",external_link=True)
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
                D’après les données de l’Enquête sociale générale sur les dons, le bénévolat et la participation de 2018, les personnes nouvellement arrivées au Canada et, plus particulièrement, celles qui n’ont pas encore obtenu la citoyenneté canadienne, sont relativement moins susceptibles de donner aux organismes de bienfaisance et à but non lucratif que les personnes nées au Canada. En revanche, les personnes naturalisées donnent légèrement plus, en moyenne, que les personnes nées au Canada et beaucoup plus que les personnes non citoyennes. Tout comme les personnes nées au Canada, les personnes nouvellement arrivées sont beaucoup plus enclines à donner à des causes laïques qu’à des causes religieuses, mais donnent plus d’argent, en moyenne, aux causes religieuses. 
                """
                ),
                # Donation rate and average donation amount
                #dcc.Graph(id='YouthDonRateAmt', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Les dons selon la cause'),
                dcc.Markdown("""
                Les deux principaux bénéficiaires des dons des personnes nouvellement arrivées sont les congrégations religieuses et les organismes de services sociaux, suivis par les organismes de santé et les hôpitaux. Les deux principaux bénéficiaires des dons des personnes nées au Canada sont les organismes de santé et de services sociaux, suivis par les congrégations religieuses et les hôpitaux. 
                """),
                # Donation rate by cause
                #dcc.Graph(id='YouthDonRateByCause', style={'marginTop': marginTop}), 
                dcc.Markdown("""
                Les personnes nouvellement arrivées au Canada donnent moins, en moyenne à la majorité des causes que les personnes nées au Canada, bien que, dans de nombreux cas, les différences ne soient pas statistiquement significatives. Les personnes naturalisées donnent plus, en moyenne, aux congrégations religieuses et aux organismes de santé que les personnes non citoyennes. 
                """),
                # Average amount donated by cause
                #dcc.Graph(id='YouthAvgAmtByCause', style={'marginTop': marginTop}), 
            ]),
            html.Div([
                html.H4('Méthodes de dons'),
                dcc.Markdown("""
                Les personnes nouvellement arrivées sont moins enclines que les personnes nées au Canada à donner après avoir été sollicitées dans un lieu public, pour parrainer quelqu’un, à la mémoire de quelqu’un ou à leur porte. Les personnes non citoyennes donnent moins fréquemment que les personnes citoyennes de leur propre initiative, au travail ou par courrier. Les personnes naturalisées ont plus tendance que les personnes non citoyennes et les personnes nées au Canada à donner à un lieu de culte.  
                """),
                # Donation rate by method
                #dcc.Graph(id='YouthDonRateByMeth', style={'marginTop': marginTop}), 
                dcc.Markdown("""
                Le montant moyen des dons des personnes nouvellement arrivées au Canada est le plus élevé quand elles donnent de l’argent dans les lieux de culte.
                """),
                # Average amount donated by method
                #dcc.Graph(id='YouthAvgAmtByMeth', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Motivations des dons'),
                dcc.Markdown("""
                En général, les personnes nouvellement arrivées donnent de l’argent pour les mêmes raisons que les personnes nées au Canada, la compassion envers les personnes dans le besoin et la conviction du bien-fondé de la cause étant les deux principales motivations des dons pour tous les groupes. Les personnes naturalisées sont nettement moins enclines à donner parce que la cause les touche personnellement et beaucoup plus enclines à donner pour des raisons religieuses ou spirituelles.
                """),
                # Motivations for donating
                #dcc.Graph(id='YouthMotivations', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Freins à donner davantage'),
                dcc.Markdown("""
                Les personnes nouvellement arrivées citent généralement les mêmes freins à donner davantage que les personnes nées au Canada. Tous les groupes de donateur.trice.s. expliquent le plus souvent qu’ils ne peuvent pas donner plus parce que leurs moyens financiers ne leur permettent pas et qu’ils sont satisfaits du montant de leurs dons. Les personnes naturalisées ont plus tendance que les autres à déclarer ne pas avoir donné plus parce qu’elles ne pensaient pas que l’argent serait utilisé efficacement. Les personnes non citoyennes ont plus tendance que les autres à déclarer ne pas avoir donné parce qu’elles n’aimaient pas la méthode de sollicitation. 
                """),
                # Barriers to donating more
                #dcc.Graph(id='YouthBarriers', style={'marginTop': marginTop}), 
                html.Div([
                    html.H5('Préoccupations relatives à l’efficience'),
                    dcc.Markdown("""
                    La préoccupation des personnes naturalisées à l’égard de l’utilisation efficiente des dons semble principalement liée aux explications données à ce sujet.
                    """),
                    # Reasons for concern about efficiency
                    #dcc.Graph(id='YouthEfficiency', style={'marginTop': marginTop}), 
                    ]),
                html.Div([
                    html.H5('Préoccupations relatives aux sollicitations'),
                    dcc.Markdown("""
                    La préoccupation des personnes non citoyennes à l’égard des méthodes de sollicitation des dons semble liée à plusieurs questions, dont la méthode de prise de contact, le nombre total de demandes et le nombre de demandes provenant du même organisme. 
                    """),
                    # Reasons for disliking solicitations
                    #dcc.Graph(id='YouthSolicitations', style={'marginTop': marginTop}), 
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
                #dcc.Graph(id='YouthVolRateVolAmt', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Bénévolat selon la cause'),
                dcc.Markdown("""
                Les personnes naturalisées ont plus tendance à faire du bénévolat pour les congrégations religieuses que les personnes citoyennes nées au Canada et moins tendance à faire don de leur temps aux organismes de services sociaux, des sports et des loisirs, et d’éducation et de recherche. 
                """),
                # Volunteer rate by cause
                #dcc.Graph(id='YouthVolRateByCause', style={'marginTop': marginTop}), 
                dcc.Markdown("""
                Sur le plan du nombre moyen d’heures de bénévolat à l’appui des diverses causes, les données n’indiquent aucune différence statistiquement significative entre les personnes nouvellement arrivées et les personnes nées au Canada.  
                """),
                # Average hours volunteered by cause
                #dcc.Graph(id='YouthAvgHrsByCause', style={'marginTop': marginTop}), 
            ]),
            html.Div([
                html.H4('Activités des bénévoles'),
                dcc.Markdown("""
                Les personnes nouvellement arrivées sont les plus enclines à organiser des activités ou des événements, à collecter des fonds, à siéger à des comités ou à des conseils d’administration et à enseigner ou à mentorer bénévolement. Les personnes naturalisées ont moins tendance à faire du bénévolat pour toutes ces activités que les personnes citoyennes nées au Canada. Les personnes non citoyennes ont moins tendance que les personnes citoyennes nées au Canada à participer bénévolement aux collectes de fonds. La majorité des autres différences dans le taux de bénévolat pour diverses activités ne sont pas statistiquement significatives. 
                """),
                # Volunteer rate by activity
                #dcc.Graph(id='YouthVolRateByActivity', style={'marginTop': marginTop}), 
                dcc.Markdown("""
                En moyenne, les personnes nouvellement arrivées consacrent le plus d’heures de bénévolat aux soins ou au soutien en santé, à l’enseignement ou au mentorat et au travail de bureau. Les personnes naturalisées consacrent moins d’heures, en moyenne, que les personnes citoyennes nées au Canada à plusieurs activités bénévoles, dont l’entraînement, la lutte contre les incendies et la conduite de véhicules. Les personnes non citoyennes consacrent moins d’heures de bénévolat, en moyenne, aux collectes de fonds que les personnes citoyennes nées au Canada. 
                """),
                # Average hours volunteered by activity
                #dcc.Graph(id='YouthAvgHrsByActivity', style={'marginTop': marginTop}), 
            
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Motivations du bénévolat'),
                dcc.Markdown("""
                Les personnes nouvellement arrivées ont tendance à faire du bénévolat pour les mêmes raisons que les personnes nées au Canada. Par exemple, apporter une contribution à la communauté et utiliser leurs compétences sont les deux principales motivations du bénévolat pour tous les groupes. Cela dit, il existe plusieurs différences. Les personnes naturalisées sont plus susceptibles de faire du bénévolat pour améliorer leur santé et leur bien-être, pour réseauter et rencontrer de nouvelles personnes, pour prendre conscience de leurs points forts personnels ou pour des raisons spirituelles et religieuses que les personnes citoyennes nées au Canada. Ces personnes ont moins tendance à faire du bénévolat parce que la cause les touche personnellement. Les personnes non citoyennes ont plus tendance à faire du bénévolat pour réseauter et pour faire la connaissance de nouvelles personnes que les personnes citoyennes nées au Canada.
                """),
                # Motivations for volunteering
                #dcc.Graph(id='YouthVolMotivations', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Freins au bénévolat'),
                dcc.Markdown("""
                Le manque de temps constitue, et de loin, le frein au bénévolat le plus répandu chez les personnes nées au Canada, naturalisées et non canadiennes, suivi par l’impossibilité de s’engager à long terme à faire du bénévolat et par la conviction d’avoir déjà donné suffisamment de leur temps. Quant aux différences entre les groupes, les personnes naturalisées et celles qui ne sont pas citoyennes ont relativement plus tendance à limiter leur bénévolat parce qu’elles ne savent pas comment s’impliquer et parce qu’elles ne pensent pas que le bénévolat leur permet d’utiliser leurs compétences.. 
                """),
                # Barriers to volunteering more
                #dcc.Graph(id='YouthVolBarriers', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Aide directe d’autrui '),
                dcc.Markdown("""
                Les personnes nouvellement arrivées sont les plus enclines à aider directement autrui en cuisinant, en faisant le ménage ou diverses autres tâches à domicile, en magasinant, en conduisant ou en accompagnant des personnes aux magasins ou à des rendez-vous et en offrant des soins en santé ou personnels. Les personnes naturalisées sont moins tendance à cuisiner, à nettoyer ou à faire d’autres corvées ménagères et à offrir des soins en santé ou personnels que les personnes citoyennes nées au Canada. Les personnes non citoyennes ont moins tendance à offrir des soins liés à la santé ou personnels, mais ont plus tendance à aider autrui en enseignant, en entraînant ou en offrant une aide à la lecture que les personnes nées au Canada.
                """),
                # Methods of helping others directly
                #dcc.Graph(id='YouthRateHelpDirect', style={'marginTop': marginTop}),
                dcc.Markdown("""
                En ce qui concerne le nombre moyen d’heures consacrées à aider directement autrui, c’est aux soins liés à la santé et personnels que les personnes naturalisées consacrent le plus d’heures. Les personnes non citoyennes, en revanche, consacrent le plus d’heures à l’enseignement, l’entraînement ou à l’aide à la lecture. En moyenne, les personnes naturalisées et les personnes non citoyennes, consacrent moins d’heures à cuisiner, à nettoyer ou à faire d’autres corvées ménagères pour aider autrui que les personnes nées au Canada. Les personnes non citoyennes consacrent moins de temps en moyenne, à offrir des soins liés à la santé ou personnels, à magasiner ou à conduire et aux formalités administratives et aux déclarations d’impôt que les personnes citoyennes nées au Canada.
                """),
                # Average hours devoted to means of helping others directly
                #dcc.Graph(id='YouthHrsHelpDirect', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Engagement communautaire'),
                dcc.Markdown("""
                Sur le plan des activités visant à améliorer la communauté, les personnes nouvellement arrivées au Canada sont les plus susceptibles de créer ou de diffuser de l’information pour sensibiliser les autres personnes à un enjeu, d’organiser ou de coordonner des événements et de participer à des réunions publiques. Les personnes naturalisées ont moins tendance à créer ou à diffuser de l’information, mais plus tendance à organiser ou à coordonner un événement que les personnes nées au Canada. 
                """),
                # Types of community engagement
                #dcc.Graph(id='YouthRateCommInvolve', style={'marginTop': marginTop}), 
                dcc.Markdown("""
                Les personnes nouvellement arrivées consacrent à peu près le même nombre d’heures aux divers types d’engagement communautaire que les personnes nées au Canada.
                """),
                # Average hours devoted to forms of community engagement
                #dcc.Graph(id='YouthHrsCommInvolve', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
   ]),
   footer
])

################## CALLBACKS ##################

# @app.callback(

#     dash.dependencies.Output('DonRateAvgDonAmt-Cause-2', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):

#     dff1 = SubSecVolRates_2018[SubSecVolRates_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == "All"]
#     dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")
#     # name1 = "Volunteer rate"
#     name1 = "Taux de bénévolat"

#     dff2 = SubSecAvgHrs_2018[SubSecAvgHrs_2018['Region'] == region]
#     dff2 = dff2[dff2['Group'] == "All"]
#     dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
#     # name2 = "Average hours"
#     name2 = "Nombre d'heures moyen"

#     title = '{}, {}'.format("Niveaux de soutien par cause", region)

#     return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)


# @app.callback(

#     dash.dependencies.Output('AllocationSupport-Cause-2', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):

#     dff = AllocationVol_2018[AllocationVol_2018['Region'] == region]
#     title = '{}, {}'.format("Répartition du soutien par cause", region)

#     return single_vertical_percentage_graph(dff, title, by="QuestionText", sort=True)
