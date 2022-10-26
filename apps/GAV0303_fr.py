import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd

from utils.data.WDA0101_data_utils import get_region_values
from utils.data.WDC0105_data_utils import get_region_names
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc
import os
import os.path as op

from utils.graphs.GAV0303_graph_utils import rate_avg_cause, vertical_percentage_graph
from utils.data.GAV0303_data_utils import get_data, process_data, get_region_names, get_region_values

from app import app
from homepage import navbar, footer

####################### Data processing ######################
SubSecAvgDon_2018, SubSecDonRates_2018, SubSecAvgHrs_2018, SubSecVolRates_2018, EducDonorsBarriers_2018, EducDonorsDonMeth_2018, EducDonorsDonRates_2018, EducDonorsMotivations_2018, EducVolsActivities_2018, EducVolsBarriers_2018, EducVolsMotivations_2018, EducVolsVolRates_2018 = get_data()
data = [SubSecAvgDon_2018, SubSecDonRates_2018, EducDonorsBarriers_2018, EducDonorsDonMeth_2018, EducDonorsDonRates_2018, EducDonorsMotivations_2018, EducVolsActivities_2018, EducVolsBarriers_2018, EducVolsMotivations_2018, EducVolsVolRates_2018, SubSecAvgHrs_2018, SubSecVolRates_2018]
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
                        html.H1(("DONS ET BÉNÉVOLAT POUR LES ORGANISMES DU SECTEUR DE L’ÉdUCATION").capitalize()),
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
    # Note: filters put in separate container to make floating element later
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
                html.P('In addition to measuring overall levels of giving and volunteering, the General Social Survey on Giving, Volunteering, and Participating measures levels of support for 15 types of causes (commonly labelled “activity areas”), including education. As defined by the survey, the education category is made up of universities & colleges and education & research organizations. Universities & colleges are defined as post-secondary degree-granting institutions, including associated professional faculties (business, law, and medical schools, etc.). Education & research organizations focus on elementary, primary and secondary education, vocational and technical education, and adult or continuing education, or research in the social, medical, physical, or technological sciences.'),
                html.P('Below we look at patterns of giving and volunteering for these organizations. The text describes national level findings; for additional detail, readers can use the pull down menu linked to the interactive data visualizations to show regional level results. While the regional specifics may differ from the national level results described in the text, the overall trends were quite similar.'),
                html.H4('Donation Levels'),
                # Donation rate and average donation amount by cause
                dcc.Graph(id='EducDonRateAvgDon', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Who Gives'),
                html.P('Some Canadians are more likely to give to education organizations than others. Nationally, the likelihood of giving increases with level of formal educational attainment and with household income. Looking at age, the likelihood of giving increases strongly until 35 to 44 and then declines somewhat. Other groups that stand out as being more likely to give include women, those who are married or in a common-law relationship, those who are employed, and those who were born in Canada.')], className='col-md-10 col-lg-8 mx-auto' 
            ),
            # html.Div([
            #     html.H4('Support for Other Organization Types'),
            #     # Rates of donating to other causes
            #     dcc.Graph(id='EducDonsCauses', style={'marginTop': marginTop}), 
            #     ], className='col-md-10 col-lg-8 mx-auto'
            # ),
            html.Div([
                html.H4('Donation Methods'),
                html.P('The survey asks respondents whether they donated in response to any of 13 different types of solicitation. While the survey does not tie these methods directly to the cause supported, comparing education donors to non-education donors (i.e., donors who only supported other causes) provides insight into how donors tend to support education organizations. Nationally, education donors are particularly likely to donate by sponsoring someone (such as in an event), in response to door-to-door canvassing, through their place of work, by attending a charity event, or in memory of someone. They are not particularly more likely to donate in places of worship, in response to a television or radio appeal or via other methods not specifically covered by the survey questionnaire.'),
                # Donation rate by method
                dcc.Graph(id='EducDonsMeth', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Motivations for donating'),
                html.P('The survey asks donors whether each of eight potential factors was important to their donation decisions. Again, while there are no direct ties between motivations and causes supported, comparing education donors with non-education donors gives insight into the reasons for supporting these organizations. Nationally, education donors are more likely than non-education donors to contribute because they were asked to contribute by someone they know, are personally affected or know someone who is personally affected by the cause of the organization, to make a contribution to the community and because they will receive a tax credit for donating. Religious and spiritual motivations do not appear to play a particularly significant role in donating decisions for education donors.'),
                # Barriers to donating more
                dcc.Graph(id='EducMotivations', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Barriers to donating'),
                html.P('To gain insight into factors that may discourage donations, donors are asked whether each of ten potential barriers kept them from donating as much as they otherwise would have. Nationally, education donors are more likely than other donors to restrict their donations because they do not like how requests for donations are made and because they believe they have already given enough. Most other barriers have broadly similar impacts as with non-education donors.'),
                # Barriers to donating more
                dcc.Graph(id='EducBarriers', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
       dbc.Row([
            html.Div([
                html.H3('Volunteering levels'),
                # html.H4('Levels of Support'),
                html.P('Nationally, about one in every 11 Canadians (9%) volunteered for an education & research organization during the year prior to the survey, making education the cause with the fourth largest volunteer base. Focusing on the two sub-causes, Canadians are substantially less likely to volunteer for universities & colleges than volunteer for general education & research organizations. Looking at the hours volunteered for the cause, education & research organizations receive just over 9% of total volunteer hours, with hours allocated about 1:2 for universities & colleges vs. general education & research organizations. Nationally, education & research ranks fourth in terms of the proportion of total volunteer hours behind arts & recreation (22%), social services (18%), and religion (16%).'),
                # Volunteer rate and average hours volunteered by cause
                dcc.Graph(id='EducVolRateAvgHrs', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Who Volunteers'),
                html.P('Nationally, groups more likely to volunteer for education organizations include women, those who are single and have never married, and those with either a university degree or a high school diploma or less. Looking at the effect of age, the likelihood of volunteering is highest among those 15 to 24, drops among those 25 to 34, peaks among those 35 to 44 and then drops, likely reflecting different life stages. Volunteering also tends to increase with household income, though households with incomes less than $20,000 deviate somewhat from this pattern, at least at the national level.'),], className='col-md-10 col-lg-8 mx-auto'
            ),
            # html.Div([
            #     html.H4('Support for other organization types'),
            #     # Rates of volunteering for other causes
            #     dcc.Graph(id='EducHrsCauses', style={'marginTop': marginTop}), 
            #     ], className='col-md-10 col-lg-8 mx-auto'
            # ),
            html.Div([
                html.H4('Volunteer activities'),
                html.P('The survey asks respondents whether they engaged in any of 14 different types of activities for an organization. While the survey does not tie activities specifically to the types of organization supported, comparing education & research volunteers to non-education & research volunteers provides insight into what volunteers do for these organizations. As one might anticipate, education & research volunteers are comparatively likely to teach and mentor others, but also to organize activities and events, coach or referee, and fundraise. They are comparatively unlikely to provide health care or support or to engage in volunteer activities not specifically mentioned in the survey.'),
                # Volunteer rate by activity
                dcc.Graph(id='EducVolActivity', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Motivations for volunteering'),
                html.P('The survey asks volunteers whether each of twelve potential factors was important to their volunteering decisions. Unlike with many other areas of the survey, these motivations are tied specifically to volunteering for particular causes. Nationally, education volunteers are more likely to volunteer in order to improve their job opportunities and to network or meet people. They are less likely to volunteer due to religious or spiritual beliefs, because a family member volunteers or to support some sort of political, environmental or social cause.'),
                # Motivations for volunteering
                dcc.Graph(id='EducVolMotivations', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Barriers to volunteering'),
                html.P('Volunteers are asked whether each of twelve potential barriers kept them from volunteering more time during the previous year. While barriers are not tied directly to the causes supported, comparing education & research volunteers with non-education & research volunteers provides some useful insight into factors that may be particularly important for these volunteers. Nationally, education volunteers are more likely to limit their volunteering because they don’t have the time. They are somewhat less likely to feel they have already contributed enough time or to have health problems or physical impediments that limit their volunteering.'),
                # Barriers to volunteering more
                dcc.Graph(id='EducVolBarriers', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
   ]),
   footer
])

@app.callback(
    dash.dependencies.Output('EducDonRateAvgDon', 'figure'),
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

    title = '{}, {}'.format("Taux et montant moyen des dons selon la cause", region)

    return rate_avg_cause(dff1, dff2, name1, name2, title)


@app.callback(
    dash.dependencies.Output('EducDonsCauses', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = EducDonorsDonRates_2018[EducDonorsDonRates_2018['Region'] == region]
    name1 = "Education and research donor"
    name2 = "Non-education and research donor"

    array = ["Education &<br>research", "Universities &<br>colleges", "Health", "Social services", "Religion", "Hospitals",
             "Sports &<br>recreation", "Grant-making,<br>fundraising",
             "Environment", "International", "Arts & culture", "Law, advocacy &<br>politics",
             "Development &<br>housing", "Other", "Business &<br>professional"]
    title = '{}, {}'.format("Rates of donating to other causes", region)
    return vertical_percentage_graph(dff, title, name1, name2, sort=True, array=array)


@app.callback(
    dash.dependencies.Output('EducDonsMeth', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = EducDonorsDonMeth_2018[EducDonorsDonMeth_2018['Region'] == region]
    dff = dff.replace("Education and research donors", "Donateur.trice.s de l'éducation")
    dff = dff.replace("Non-education and research donors", "Autres donateur.trice.s")

    # name1 = "Education and research donors"
    # name2 = "Non-education and research donors"
    name1 = "Donateur.trice.s de l'éducation"
    name2 = "Autres donateur.trice.s"

    title = '{}, {}'.format("Taux de donateur.trice.s par méthode", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('EducMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = EducDonorsMotivations_2018[EducDonorsMotivations_2018['Region'] == region]
    dff = dff.replace("Education and research donors", "Donateur.trice.s de l'éducation")
    dff = dff.replace("Non-education and research donors", "Autres donateur.trice.s")

    # name1 = "Education and research donors"
    # name2 = "Non-education and research donors"
    name1 = "Donateur.trice.s de l'éducation"
    name2 = "Autres donateur.trice.s"

    title = '{}, {}'.format("Motivations des dons", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('EducBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = EducDonorsBarriers_2018[EducDonorsBarriers_2018['Region'] == region]
    dff = dff.replace("Education and research donors", "Donateur.trice.s de l'éducation")
    dff = dff.replace("Non-education and research donors", "Autres donateur.trice.s")

    # name1 = "Education and research donors"
    # name2 = "Non-education and research donors"
    name1 = "Donateur.trice.s de l'éducation"
    name2 = "Autres donateur.trice.s"

    title = '{}, {}'.format("Freins à donner plus", region)
    return vertical_percentage_graph(dff, title, name1, name2)


# @app.callback(
#     dash.dependencies.Output('EducVolRateAvgHrs', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     dff1 = SubSecVolRates_2018[SubSecVolRates_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == "All"]
#     # dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")
#     name1 = "Volunteer rate"
#     # name1 = "Taux de bénévolat"

#     dff2 = SubSecAvgHrs_2018[SubSecAvgHrs_2018['Region'] == region]
#     # dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
#     name2 = "Average hours"
#     # name2 = "Nombre d'heures moyen"

#     title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures de bénévolat selon la cause", region)

#     return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)

@app.callback(
    dash.dependencies.Output('EducVolRateAvgHrs', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff1 = SubSecVolRates_2018[SubSecVolRates_2018['Region'] == region]
    dff1 = dff1[dff1['Group'] == "All"]
    dff1 = dff1.replace("Volunteer rate", "Taux de bénévolat")
    # name1 = "Volunteer rate"
    name1 = "Taux de bénévolat"

    dff2 = SubSecAvgHrs_2018[SubSecAvgHrs_2018['Region'] == region]
    dff2 = dff2[dff2['Group'] == "All"]
    dff2 = dff2.replace("Average hours", "Nombre d'heures moyen")
    # name2 = "Average hours"
    name2 = "Nombre d'heures moyen"

    title = '{}, {}'.format("Volunteer rate and average hours volunteered by cause", region)

    return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)



@app.callback(
    dash.dependencies.Output('EducHrsCauses', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = EducVolsVolRates_2018[EducVolsVolRates_2018['Region'] == region]
    dff = dff.replace("Education and research volunteer", "Bénévoles de l'éducation")
    dff = dff.replace("Non-education and research volunteer", "Autres bénévoles")
    
    # name1 = "Education and research volunteer"
    # name2 = "Non-education and research volunteer"
    name1 = "Bénévoles de l'éducation"
    name2 = "Autres bénévoles"

    title = '{}, {}'.format("Rates of volunteering for other causes", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('EducVolActivity', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = EducVolsActivities_2018[EducVolsActivities_2018['Region'] == region]
    dff = dff.replace("Education and research volunteer", "Bénévoles de l'éducation")
    dff = dff.replace("Non-education and research volunteer", "Autres bénévoles")
    
    # name1 = "Education and research volunteer"
    # name2 = "Non-education and research volunteer"
    name1 = "Bénévoles de l'éducation"
    name2 = "Autres bénévoles"

    title = '{}, {}'.format("Taux de bénévolat par activité", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('EducVolMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = EducVolsMotivations_2018[EducVolsMotivations_2018['Region'] == region]
    dff = dff.replace("Education and research volunteer", "Bénévoles de l'éducation")
    dff = dff.replace("Non-education and research volunteer", "Autres bénévoles")
    
    # name1 = "Education and research volunteer"
    # name2 = "Non-education and research volunteer"
    name1 = "Bénévoles de l'éducation"
    name2 = "Autres bénévoles"

    title = '{}, {}'.format("Motivations des bénévoles", region)
    return vertical_percentage_graph(dff, title, name1, name2)


@app.callback(
    dash.dependencies.Output('EducVolBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = EducVolsBarriers_2018[EducVolsBarriers_2018['Region'] == region]
    dff = dff.replace("Education and research volunteer", "Bénévoles de l'éducation")
    dff = dff.replace("Non-education and research volunteer", "Autres bénévoles")
    
    # name1 = "Education and research volunteer"
    # name2 = "Non-education and research volunteer"
    name1 = "Bénévoles de l'éducation"
    name2 = "Autres bénévoles"

    title = '{}, {}'.format("Freins à faire plus de bénévolat", region)
    return vertical_percentage_graph(dff, title, name1, name2)

