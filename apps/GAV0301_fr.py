import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc
import os
import os.path as op

from utils.graphs.GAV0301_graph_utils import vertical_percentage_graph
from utils.graphs.HOA0204_graph_utils import rate_avg_cause
from utils.data.GAV0301_data_utils import get_data, process_data, get_region_names, get_region_values

from app import app
from homepage import navbar, footer

####################### Data processing ######################
SubSecAvgDon_2018, SubSecDonRates_2018, SubSecAvgHrs_2018, SubSecVolRates_2018, HealthDonorsBarriers_2018, HealthDonorsDonMeth_2018, HealthDonorsDonRates_2018, HealthDonorsMotivations_2018, HealthVolsActivities_2018, HealthVolsBarriers_2018, HealthVolsMotivations_2018, HealthVolsVolRates_2018 = get_data()
data = [SubSecAvgDon_2018, SubSecDonRates_2018, HealthDonorsBarriers_2018, HealthDonorsDonMeth_2018, HealthDonorsDonRates_2018, HealthDonorsMotivations_2018, HealthVolsActivities_2018, HealthVolsBarriers_2018, HealthVolsMotivations_2018, HealthVolsVolRates_2018, SubSecAvgHrs_2018, SubSecVolRates_2018]
process_data(data)

region_values = get_region_values()
region_names = get_region_names()

###################### App layout ######################

marginTop = 20

layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                html.Div(
                    html.Div([
                        html.H1(('DONS D’ARGENT ET BÉNÉVOLAT POUR LES ORGANISMES DE SANTÉ').capitalize()),
                        # html.Span(
                        #     'David Lasby',
                        #     className='meta'
                        # )
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
    # dropdown menu
    dbc.Container([
        dbc.Row(
           dbc.Col(
               html.Div([
                   "Sélectionnez une région:",
                   dcc.Dropdown(
                       id='region-selection',
                       options=[{'label': region_values[i], 'value': region_values[i]} for i in range(len(region_values))],
                       value='CA',
                       ),
                    html.Br(),
                ],className="m-2 p-2"),
            ),id='sticky-dropdown'),
    ],className='sticky-top bg-light mb-2', fluid=True),
   dbc.Container([
       dbc.Row([
            html.Div([
                # html.H3('Giving'),
                html.P('In addition to measuring general levels of giving and volunteering, the General Social Survey on Giving, Volunteering, and Participating measures levels of support for 15 types of causes (commonly labelled “activity areas”), including health. As defined by the survey, the broader health category is made up of hospitals and general health organizations. Hospitals focus primarily on inpatient care while general health organizations focus primarily on outpatient care and other medical services such as health promotion, first aid training, and emergency services.'),
                html.P('Below we look at patterns of giving and volunteering for health organizations. The text describes national level findings; for additional detail, readers can use the pull down menu linked to the interactive data visualizations to show regional level results. While the regional specifics may differ from the national level results described in the text, the overall trends were quite similar.'),
                html.H4('Donation levels'),
                html.P('Nationally, just over two in five Canadians (41%) donated to health organizations during the one year period prior to the survey, making health the most commonly supported cause. Focusing on the two sub-causes, one in three Canadians donated to general health organizations and one in six donated to hospitals (9% donated to both). Looking at the amounts donated, the broader category of health organizations accounted for the second highest proportion of total donations (17%) behind religious organizations. General health organizations received most of this support (11%) and hospitals the remainder (6%). The divergence between the two sub-causes was driven almost exclusively by the relative size of their donor bases as donors gave virtually identical average amounts to each.'),
                # Donation rate and average donation amount by cause
                dcc.Graph(id='DonRateAvgDon', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [html.H4('Who Gives'),
                 html.P('Some Canadians are more likely to give to health organizations than others. Nationally, women are more likely to donate than men, those who are married or widowed are more likely to donate than those who are single, those who are employed or not in the labour force are more likely to donate than those who are unemployed, and those born in Canada are more likely to donate than New Canadians. In terms of major trends, the likelihood of donating tends to increase with age, level of formal education, frequency of attendance at religious services, and household income.')], className='col-md-10 col-lg-8 mx-auto'
            ),
            # html.Div([
            #     html.H4('Support for Other Organization Types'),
            #     # Donation rate and average donation amount by cause
            #     dcc.Graph(id='HealthDonsCauses', style={'marginTop': marginTop}), 
            #     ], className='col-md-10 col-lg-8 mx-auto'
            # ),
            html.Div([
                html.H4('Donation Methods'),
                html.P("The survey asks respondents whether they donated in response to any of 13 different types of solicitation. While the survey does not tie these methods directly to the cause supported, comparing health donors to non-health donors (i.e., donors who only supported other causes) provides insight into how donors tend to support health organizations. Nationally, health donors are particularly likely to donate in memory of someone, by sponsoring someone in an event (such as a bike-a-thon or golf tournament), and after being approached in a public place (such as on the street or in a shopping centre). They are somewhat less likely to donate in a place of worship."),
                # Donation rate by method
                dcc.Graph(id='HealthDonsMeth', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Motivations for donating'),
                html.P("The survey asks donors whether each of eight potential factors were important to their donation decisions. Again, while there are no direct ties between motivations and causes supported, comparing health donors with non-health donors gives insight into the reasons for supporting these organizations. Health donors are substantially more likely than non-health donors to give because they are personally affected or know someone who is personally affected by the cause of the organization and because they were asked to contribute by someone they know. They are comparatively less likely to give because of religious or spiritual beliefs."),
                # Barriers to donating more
                dcc.Graph(id='HealthMotivations', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Barriers to donating'),
                html.P('To gain insight into factors that may discourage donations, donors are asked whether each of ten potential barriers kept them from donating as much as they otherwise would have. Nationally, the biggest differences between health and non-health donors are that health donors are comparatively likely to be satisfied with the amounts they have already donated and comparatively less likely to volunteer instead of donating and to limit donations because they find it hard to find a cause worth supporting.'),
                # Barriers to donating more
                dcc.Graph(id='HealthBarriers', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            
        ]),
       dbc.Row([
            html.Div([
                html.H3('Volunteering levels'),
                # html.H4('Levels of Support'),
                html.P("Nationally, about one in every 17 Canadians (6%) volunteered for a health organization during the year prior to the survey, making health the fifth most commonly supported cause. Focusing on the two sub-causes, Canadians are about twice as likely to volunteer for general health organizations as volunteer for hospitals. Looking at the hours volunteered for the cause, health organizations receive just under 9% of total hours. Although the volunteer base for hospitals is considerably smaller, these volunteers tend to contribute more hours, meaning that total volunteer hours are split approximately evenly between hospitals and general health organizations. Nationally, health organizations receive the fifth largest proportion of volunteer hours behind arts & recreation (23%), social services (18%), religion (16%) and education & research (9%) organizations."),
                # Volunteer rate and average hours volunteered by cause
                dcc.Graph(id='VolRateAvgHrs', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [html.H4('Who Volunteers'),
                 html.P('Groups that stand out as being more likely to volunteer for health organizations include women, those with a post-secondary or higher levels of formal education and those born in Canada. In terms of trends, the likelihood of volunteering tends to increase with household income and with frequency of attendance at religious services.')],
            className='col-md-10 col-lg-8 mx-auto'),
            # html.Div([
            #     html.H4('Support for other organization types'),
            #     # Rates of volunteering for other causes
            #     dcc.Graph(id='HealthHrsCauses', style={'marginTop': marginTop}), 
            #     ], className='col-md-10 col-lg-8 mx-auto'
            # ),
            html.Div([
                html.H4('Volunteer activities'),
                html.P('The survey asks respondents whether they engaged in any of 14 different types of activities for an organization. While the survey does not tie activities specifically to the types of organization supported, comparing health volunteers to non-health volunteers provides insight into what volunteers do for these organizations. As one would expect, health volunteers are particularly likely to provide health care or support, but also more likely to engage in fundraising and canvassing. They are substantially less likely to coach or referee and somewhat less likely to carry out maintenance or repair work.'),
                # Volunteer rate by activity
                dcc.Graph(id='HealthVolActivity', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Motivations for volunteering'),
                html.P('The survey asks volunteers whether each of twelve potential factors was important to their volunteering decisions. Unlike with many other areas of the survey, these motivations are tied specifically to volunteering for particular causes. Nationally, health volunteers are most different in that they are more likely to volunteer because they have been personally affected by the cause or know someone who is personally affected. They are somewhat less likely to volunteer in order to network or meet people. Other motivations appear to affect health and non-health volunteers fairly equally.'),
                # Motivations for volunteering
                dcc.Graph(id='HealthVolMotivations', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Barriers to volunteering'),
                html.P('Volunteers are asked whether each of twelve potential barriers kept them from volunteering more time during the previous year. While barriers are not tied directly to the causes supported, comparing health volunteers with non-health volunteers provides some useful insight. Overall, health volunteers are quite similar to other volunteers in terms of how they respond to potential barriers. Nationally, the biggest differences with health volunteers are that they are slightly less likely to not have any interest in further volunteering and slightly more likely to prefer to give money instead.'),
                # Barriers to volunteering more
                dcc.Graph(id='HealthVolBarriers', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
   ]),
   footer
])

################ Callbacks ################

@app.callback(
    dash.dependencies.Output('DonRateAvgDon', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = SubSecDonRates_2018[SubSecDonRates_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "All"]
    dff1 = dff1.replace("Donation rate", "Taux de donateur.trice.s")

    # name1 = "Donation rate"
    name1 = "Taux de donateur.trice.s"

    dff2 = SubSecAvgDon_2018[SubSecAvgDon_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "All"]
    dff2 = dff2.replace("Average donation", "Dons annuels moyens")

    # name2 = "Average donation"
    name2 = "Dons annuels moyens"

    title = '{}, {}'.format("Taux de donateur.trice.s et montant moyen des dons selon la cause", region)

    return rate_avg_cause(dff1, dff2, name1, name2, title)


@app.callback(
    dash.dependencies.Output('HealthDonsCauses', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = HealthDonorsDonRates_2018[HealthDonorsDonRates_2018['Region'] == region]
    name1 = "Health donors"
    name2 = "Non-health donor"

    array = ["Health", "Hospitals", "Social services", "Religion",
             "Sports &<br>recreation", "Education &<br>research", "Grant-making,<br>fundraising",
             "International", "Environment", "Law, advocacy &<br>politics", "Arts & culture",
             "Development &<br>housing", "Other", "Universities &<br>colleges", "Business &<br>professional"]
    title = '{}, {}'.format("Rates of donating to other causes", region)
    return vertical_percentage_graph(dff, title, name1, name2, sort=True, array=array)


@app.callback(
    dash.dependencies.Output('HealthDonsMeth', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = HealthDonorsDonMeth_2018[HealthDonorsDonMeth_2018['Region'] == region]
    dff = dff.replace('Health donors', 'Donateur.trice.s de la santé')
    dff = dff.replace("Non-health donors", 'Autres donateur.trice.s')
    # name1 = "Health donors"
    # name2 = "Non-health donors"
    name1 = 'Donateur.trice.s de la santé'
    name2 = 'Autres donateur.trice.s'

    title = '{}, {}'.format("Taux de donateur.trice.s par méthode", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('HealthMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = HealthDonorsMotivations_2018[HealthDonorsMotivations_2018['Region'] == region]
    dff = dff.replace('Health donors', 'Donateur.trice.s de la santé')
    dff = dff.replace("Non-health donors", 'Autres donateur.trice.s')
    # name1 = "Health donors"
    # name2 = "Non-health donors"
    name1 = 'Donateur.trice.s de la santé'
    name2 = 'Autres donateur.trice.s'

    title = '{}, {}'.format("Motivations des dons", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('HealthBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = HealthDonorsBarriers_2018[HealthDonorsBarriers_2018['Region'] == region]

    dff = dff.replace('Health donors', 'Donateur.trice.s de la santé')
    dff = dff.replace("Non-health donors", 'Autres donateur.trice.s')
    # name1 = "Health donors"
    # name2 = "Non-health donors"
    name1 = 'Donateur.trice.s de la santé'
    name2 = 'Autres donateur.trice.s'

    title = '{}, {}'.format("Freins à donner plus", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('VolRateAvgHrs', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = SubSecVolRates_2018[SubSecVolRates_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "All"]
    dff1 = dff1.replace('Volunteer rate', 'Taux de bénévolat')
    # name1 = "Volunteer rate"
    name1 = 'Taux de bénévolat'

    dff2 = SubSecAvgHrs_2018[SubSecAvgHrs_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "All"]
    dff2 = dff2.replace('Average hours', "Nombre d'heures moyen")
    # name2 = "Average hours"
    name2 = "Nombre d'heures moyen"

    title = '{}, {}'.format("Taux de bénévoles et nombre moyen d’heures de bénévolat selon la cause", region)

    return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)


@app.callback(
    dash.dependencies.Output('HealthHrsCauses', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = HealthVolsVolRates_2018[HealthVolsVolRates_2018['Region'] == region]
    name1 = "Health volunteer"
    name2 = "Non-health volunteer"

    title = '{}, {}'.format("Rates of volunteering for other causes", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('HealthVolActivity', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = HealthVolsActivities_2018[HealthVolsActivities_2018['Region'] == region]
    
    dff = dff.replace("Health volunteer", "Bénévoles de la santé")
    dff = dff.replace("Non-health volunteer", "Autres bénévoles")
    name1 = "Bénévoles de la santé"
    name2 = "Autres bénévoles"
    # name1 = "Health volunteer"
    # name2 = "Non-health volunteer"
    
    title = '{}, {}'.format("Taux de bénévoles par activité", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('HealthVolMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = HealthVolsMotivations_2018[HealthVolsMotivations_2018['Region'] == region]
    
    dff = dff.replace("Health volunteer", "Bénévoles de la santé")
    dff = dff.replace("Non-health volunteer", "Autres bénévoles")
    name1 = "Bénévoles de la santé"
    name2 = "Autres bénévoles"
    # name1 = "Health volunteer"
    # name2 = "Non-health volunteer"

    title = '{}, {}'.format("Motivations du bénévolat", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('HealthVolBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = HealthVolsBarriers_2018[HealthVolsBarriers_2018['Region'] == region]
    
    dff = dff.replace("Health volunteer", "Bénévoles de la santé")
    dff = dff.replace("Non-health volunteer", "Autres bénévoles")
    name1 = "Bénévoles de la santé"
    name2 = "Autres bénévoles"
    # name1 = "Health volunteer"
    # name2 = "Non-health volunteer"

    title = '{}, {}'.format("Freins à faire plus de bénévolat", region)
    return vertical_percentage_graph(dff, title, name1, name2)