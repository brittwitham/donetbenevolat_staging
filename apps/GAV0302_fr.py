import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import dash_bootstrap_components as dbc

from utils.graphs.GAV0302_graph_utils import vertical_percentage_graph
from utils.graphs.HOA0204_graph_utils import rate_avg_cause

from utils.data.GAV0302_data_utils import get_data, process_data, get_region_names, get_region_values

from app import app
from homepage import navbar, footer

####################### Data processing ######################
SubSecAvgDon_2018,SubSecDonRates_2018 ,SubSecAvgHrs_2018 ,SubSecVolRates_2018, ReligionDonorsBarriers_2018, ReligionDonorsDonMeth_2018, ReligionDonorsDonRates_2018, ReligionDonorsMotivations_2018, ReligionVolsActivities_2018, ReligionVolsBarriers_2018, ReligionVolsMotivations_2018, ReligionVolsVolRates_2018 = get_data()

# SubSecAvgDon_2018, SubSecDonRates_2018, ReligionDonorsBarriers_2018, ReligionDonorsDonMeth_2018, ReligionDonorsDonRates_2018, ReligionDonorsMotivations_2018, ReligionVolsActivities_2018, ReligionVolsBarriers_2018, ReligionVolsMotivations_2018, ReligionVolsVolRates_2018, SubSecAvgHrs_2018, SubSecVolRates_2018 = get_data()

# data = [SubSecAvgDon_2018, SubSecDonRates_2018, HealthDonorsBarriers_2018, HealthDonorsDonMeth_2018, HealthDonorsDonRates_2018, HealthDonorsMotivations_2018, HealthVolsActivities_2018, HealthVolsBarriers_2018, HealthVolsMotivations_2018, HealthVolsVolRates_2018, SubSecAvgHrs_2018, SubSecVolRates_2018]

data = [SubSecAvgDon_2018,SubSecDonRates_2018,SubSecAvgHrs_2018,SubSecVolRates_2018, ReligionDonorsBarriers_2018, ReligionDonorsDonMeth_2018, ReligionDonorsDonRates_2018, ReligionDonorsMotivations_2018, ReligionVolsActivities_2018, ReligionVolsBarriers_2018, ReligionVolsMotivations_2018, ReligionVolsVolRates_2018]

process_data(data)
# cause_names = BarriersByCause_2018["Group"].unique()
# barriers_names = Barriers_2018["QuestionText"].unique()

# process_data(data)

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
                        html.H1(('DONS ET BÉNÉVOLAT POUR LES ORGANISMES RELIGIEUX').capitalize()),
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
                html.P("In addition to measuring general levels of giving and volunteering, the General Social Survey on Giving, Volunteering, and Participating measures levels of support for 15 types of causes (commonly labelled “activity areas”), including religion. These organizations focus primarily on conducting religious rituals and promoting religious beliefs. This includes individual congregations (e.g., single mosques, churchs, synagogues, temples, etc.), associations of congregations, and organizations focusing on specifically religious education such as seminaries."),
                html.P('Below we look at patterns of giving and volunteering for these organizations. The text describes national level findings; for additional detail, readers can use the pull down menu linked to the interactive data visualizations to show regional level results. While the regional specifics may differ from the national level results described in the text, the overall trends were quite similar.'),
                html.H4('Donation Levels'),
                html.P('Nationally, one in four Canadians made at least one donation to religious organizations during the one year period prior to the survey, making religion the third most commonly supported cause. Religion organizations were much more highly ranked in terms of the amounts donated, accounting for nearly half (46%) of total donations, more than any other cause. Looking at the average amounts donated, religious donors gave far more than donors to any other cause, making them the most committed supporters by a significant margin.'),
                # Donation rate and average donation amount by cause
                dcc.Graph(id='DonRateAvgDon2', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div(
                [html.H4('Who Gives'),
                html.P('Some Canadians are more likely to give to religion organizations than others. Nationally, the likelihood of giving to these organizations increases significantly with the frequency of attending religious services and with age. Other groups more likely to give to religion organizations include women, widows and widowers, those not in the labour force, those with a university degree, and New Canadians.'),],
            className='col-md-10 col-lg-8 mx-auto'),
            # html.Div([
            #     html.H4('Support for Other Organization Types'),
            #     # Rates of donating to other causes
            #     dcc.Graph(id='HealthDonsCauses-2', style={'marginTop': marginTop}), 
            #     ], className='col-md-10 col-lg-8 mx-auto'
            # ),
            html.Div([
                html.H4('Donation Methods'),
                html.P('The survey asks respondents whether they donated in response to any of 13 different types of solicitation. While the survey does not tie these methods directly to the cause supported, comparing religion donors to non-religion donors (i.e., donors who only supported other causes) provides insight into how donors tend to support religion organizations. Nationally, as one would expect, religion donors are vastly more likely to donate in a place of worship, but also more likely to donate in memory of someone, on their own initiative, and in response to a mail request. Religion donors are less likely than other donors to donate in response to an online request, after being approached in a public place, or in any other way not specifically covered by the survey questionnaire.'),
                # Donation rate by method
                dcc.Graph(id='ReligionDonsMeth', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Motivations for donating'),
                html.P("The survey asks donors whether each of eight potential factors was important to their donation decisions. Again, while there are no direct ties between motivations and causes supported, comparing religion donors with non-religion donors gives insight into the reasons for supporting these organizations. As one would expect, religion donors are much more likely to donate because of their religious and spiritual beliefs. In addition, they are comparatively likely to donate in order to make a contribution to the community and because they will receive tax credits in return for donating."),
                # Barriers to donating more
                # dcc.Graph(id='ReligionMotivations', style={'marginTop': marginTop}),
                dcc.Graph(id='ReligionMotivations', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Barriers to donating'),
                html.P("To gain insight into factors that may discourage donations, donors are asked whether each of ten potential barriers kept them from donating as much as they otherwise would have. Nationally, religion donors are more likely than other donors to give directly to those in need rather than donating more to an organization and to volunteer instead. All other barriers have roughly comparable impacts on religion and non-religion donors."),
                # Barriers to donating more
                dcc.Graph(id='ReligionBarriers', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
       dbc.Row([
            html.Div([
                html.H3('Volunteering Levels'),
                # html.H4('Levels of Support'),
                html.P('Nationally, about one in every 12 Canadians (8%) volunteered for a religion organization during the year prior to the survey. Comparatively speaking, religion has the fifth largest volunteer base behind arts & recreation (12%), social services, education & research (9%), and health (9%). Because religion volunteers tend to contribute comparatively large amounts of time, religion accounts for the third highest proportion of total volunteer hours (16%), behind arts & recreation (23%) and social services (18%), and ahead of education & research and health (9% each).'),
                # Volunteer rate and average hours volunteered by cause
                dcc.Graph(id='VolRateAvgHrs2', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Who Volunteers'),
                html.P('National, the likelihood of volunteering for a religion organization increases with frequency of attendance at religious services and with age (among those 25 and over). Very broadly speaking, the demographic associations with volunteering are quite similar to those with donating, though the trends are not as strongly expressed.'),], className='col-md-10 col-lg-8 mx-auto'
            ),
            # html.Div([
            #     html.H4('Support for other organization types'),
            #     # Rates of volunteering for other causes
            #     dcc.Graph(id='HealthHrsCauses-2', style={'marginTop': marginTop}), 
            #     ], className='col-md-10 col-lg-8 mx-auto'
            # ),
            html.Div([
                html.H4('Volunteer activities'),
                html.P('The survey asks respondents whether they engaged in any of 14 different types of activities for an organization. While the survey does not tie activities specifically to the types of organization supported, comparing religion volunteers to non-religion volunteers provides insight into what volunteers do for these organizations. Nationally, religion volunteers are comparatively likely to engage in many activities, most notably collecting, serving or delivering goods or food, teaching or mentoring, repairing, maintaining or building facilities, and driving. They are comparatively less likely to coach, teach or referee or to engage in environmental protection activities.'),
                # Volunteer rate by activity
                dcc.Graph(id='ReligionVolActivity', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Motivations for volunteering'),
                html.P('The survey asks volunteers whether each of twelve potential factors was important to their volunteering decisions. Unlike with many other areas of the survey, these motivations are tied specifically to volunteering for particular causes. Nationally, the biggest motivational differences with religion volunteers are that they are much more likely to volunteer for religious or spiritual reasons. In addition, they are somewhat more likely to volunteer because a family member and/or friends volunteer and because they are personally affected by the cause. They are somewhat less likely to seek to improve their job opportunities through volunteering or to support a political or social cause.'),
                # Motivations for volunteering
                dcc.Graph(id='ReligionVolMotivations', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
            html.Div([
                html.H4('Barriers to volunteering'),
                html.P('Volunteers are asked whether each of twelve potential barriers kept them from volunteering more time during the previous year. While barriers are not tied directly to the causes supported, comparing religion volunteers with non-religion volunteers provides some useful insight into factors that may be particularly important for these volunteers. Nationally, religion volunteers are slightly more likely to limit their volunteering because of health problems or physical limitations. They are less likely to feel that the volunteer activities they are asked to do are insufficiently meaningful or to not have been asked to volunteer further. Most other differences are not as individually significant, though it is noteworthy that religion volunteers are fairly consistently less likely to report most potential barriers.'),
                # Barriers to volunteering more
                dcc.Graph(id='ReligionVolBarriers', style={'marginTop': marginTop}), 
                ], className='col-md-10 col-lg-8 mx-auto'
            ),
        ]),
   ]),
   footer
])

############### Callbacks ###############

# @app.callback(
#     dash.dependencies.Output('DonRateAvgDon-2', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     dff1 = SubSecDonRates_2018[SubSecDonRates_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == "All"]
#     name1 = "Donation rate"

#     dff2 = SubSecAvgDon_2018[SubSecAvgDon_2018['Region'] == region]
#     dff2 = dff2[dff2['Group'] == "All"]
#     name2 = "Average donation"

#     title = '{}, {}'.format("Donation rate and average donation amount by cause", region)

#     return rate_avg_cause(dff1, dff2, name1, name2, title)


# @app.callback(
#     dash.dependencies.Output('HealthDonsCauses-2', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     dff = HealthDonorsDonRates_2018[HealthDonorsDonRates_2018['Region'] == region]
#     name1 = "Health donors"
#     name2 = "Non-health donor"

#     array = ["Health", "Hospitals", "Social services", "Religion",
#              "Sports &<br>recreation", "Education &<br>research", "Grant-making,<br>fundraising",
#              "International", "Environment", "Law, advocacy &<br>politics", "Arts & culture",
#              "Development &<br>housing", "Other", "Universities &<br>colleges", "Business &<br>professional"]
#     title = '{}, {}'.format("Rates of donating to other causes", region)
#     return vertical_percentage_graph(dff, title, name1, name2, sort=True, array=array)


# @app.callback(
#     dash.dependencies.Output('HealthDonsMeth-2', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     dff = HealthDonorsDonMeth_2018[HealthDonorsDonMeth_2018['Region'] == region]
#     # dff = ReligionDonorsDonMeth_2018[ReligionDonorsDonMeth_2018['Region'] == region]
#     # name1 = "Health donors"
#     # name2 = "Non-health donors"
#     # name1 = 'Religion donors'
#     # name2 = 'Non-religion donors'
#     name1 = dff.Attribute.unique()[1]
#     name2 = dff.Attribute.unique()[0]

#     title = '{}, {}'.format("Donation rate by method", region)
#     return vertical_percentage_graph(dff, title, name1, name2)


# @app.callback(
#     dash.dependencies.Output('HealthMotivations-2', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     dff = HealthDonorsMotivations_2018[HealthDonorsMotivations_2018['Region'] == region]
#     name1 = "Health donors"
#     name2 = "Non-health donors"

#     title = '{}, {}'.format("Motivations for donating", region)
#     return vertical_percentage_graph(dff, title, name1, name2)


# @app.callback(
#     dash.dependencies.Output('HealthBarriers-2', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     dff = HealthDonorsBarriers_2018[HealthDonorsBarriers_2018['Region'] == region]
#     name1 = "Health donors"
#     name2 = "Non-health donors"

#     title = '{}, {}'.format("Barriers to donating more", region)
#     return vertical_percentage_graph(dff, title, name1, name2)


# @app.callback(
#     dash.dependencies.Output('VolRateAvgHrs-2', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     dff1 = SubSecVolRates_2018[SubSecVolRates_2018['Region'] == region]
#     dff1 = dff1[dff1['Group'] == "All"]
#     name1 = "Volunteer rate"

#     dff2 = SubSecAvgHrs_2018[SubSecAvgHrs_2018['Region'] == region]
#     dff2 = dff2[dff2['Group'] == "All"]
#     name2 = "Average hours"

#     title = '{}, {}'.format("Volunteer rate and average hours volunteered by cause", region)

#     return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)

# @app.callback(
#     dash.dependencies.Output('HealthHrsCauses-2', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     dff = HealthVolsVolRates_2018[HealthVolsVolRates_2018['Region'] == region]
#     name1 = "Health volunteer"
#     name2 = "Non-health volunteer"

#     title = '{}, {}'.format("Rates of volunteering for other causes", region)
#     return vertical_percentage_graph(dff, title, name1, name2)


# @app.callback(
#     dash.dependencies.Output('HealthVolActivity-2', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     dff = HealthVolsActivities_2018[HealthVolsActivities_2018['Region'] == region]
#     name1 = "Health volunteer"
#     name2 = "Non-health volunteer"

#     title = '{}, {}'.format("Volunteer rate by activity", region)
#     return vertical_percentage_graph(dff, title, name1, name2)


# @app.callback(
#     dash.dependencies.Output('HealthVolMotivations-2', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     dff = HealthVolsMotivations_2018[HealthVolsMotivations_2018['Region'] == region]
#     name1 = "Health volunteer"
#     name2 = "Non-health volunteer"

#     title = '{}, {}'.format("Motivations for volunteering", region)
#     return vertical_percentage_graph(dff, title, name1, name2)


# @app.callback(
#     dash.dependencies.Output('HealthVolBarriers-2', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     dff = HealthVolsBarriers_2018[HealthVolsBarriers_2018['Region'] == region]
#     name1 = "Health volunteer"
#     name2 = "Non-health volunteer"

#     title = '{}, {}'.format("Barriers to volunteering more", region)
#     return vertical_percentage_graph(dff, title, name1, name2)


## __________________________

# @app.callback(
#     dash.dependencies.Output('ReligionDonsMeth', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     dff = ReligionDonorsDonMeth_2018[ReligionDonorsDonMeth_2018['Region'] == region]
#     name1 = "Religion donors"
#     name2 = "Non-religion donors"

#     title = '{}, {}'.format("Donation rate by method", region)
#     return vertical_percentage_graph(dff, title, name1, name2)

# @app.callback(
#     dash.dependencies.Output('ReligionVolMotivations', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     dff = ReligionVolsMotivations_2018[ReligionVolsMotivations_2018['Region'] == region]
#     # name1 = "Religion volunteer"
#     # name2 = "Non-religion volunteer"
#     name1 = dff.Attribute.unique()[1]
#     name2 = dff.Attribute.unique()[0]

#     title = '{}, {}'.format("Motivations for volunteering", region)
#     return vertical_percentage_graph(dff, title, name1, name2)

# @app.callback(
#     dash.dependencies.Output('ReligionVolBarriers', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     dff = ReligionVolsBarriers_2018[ReligionVolsBarriers_2018['Region'] == region]
#     name1 = "Religion volunteer"
#     name2 = "Non-religion volunteer"

#     title = '{}, {}'.format("Barriers to volunteering more", region)
#     return vertical_percentage_graph(dff, title, name1, name2)

# @app.callback(
#     dash.dependencies.Output('ReligionBarriers', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     dff = ReligionDonorsBarriers_2018[ReligionDonorsBarriers_2018['Region'] == region]
#     name1 = "Religion donors"
#     name2 = "Non-religion donors"

#     title = '{}, {}'.format("Barriers to donating more", region)
#     return vertical_percentage_graph(dff, title, name1, name2)



# @app.callback(
#     dash.dependencies.Output('ReligionMotivations', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     dff = ReligionDonorsMotivations_2018[ReligionDonorsMotivations_2018['Region'] == region]
#     name1 = "Religion donors"
#     name2 = "Non-religion donors"

#     title = '{}, {}'.format("Motivations for donating", region)
#     return vertical_percentage_graph(dff, title, name1, name2)

# @app.callback(
#     dash.dependencies.Output('ReligionBarriers2', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     dff = ReligionDonorsBarriers_2018[ReligionDonorsBarriers_2018['Region'] == region]
#     name1 = "Religion donors"
#     name2 = "Non-religion donors"

#     title = '{}, {}'.format("Barriers to donating more", region)
#     return vertical_percentage_graph(dff, title, name1, name2)


# @app.callback(
#     dash.dependencies.Output('ReligionVolActivity', 'figure'),
#     [
#         dash.dependencies.Input('region-selection', 'value')
#     ])
# def update_graph(region):
#     dff = ReligionVolsActivities_2018[ReligionVolsActivities_2018['Region'] == region]
#     name1 = "Religion volunteer"
#     name2 = "Non-religion volunteer"

#     title = '{}, {}'.format("Volunteer rate by activity", region)
#     return vertical_percentage_graph(dff, title, name1, name2)

@app.callback(
    dash.dependencies.Output('DonRateAvgDon2', 'figure'),
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
    dash.dependencies.Output('ReligionDonsCauses', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = ReligionDonorsDonRates_2018[ReligionDonorsDonRates_2018['Region'] == region]
    name1 = "Religion donor"
    name2 = "Non-religion donor"

    title = '{}, {}'.format("Rates of donating to other causes", region)
    return vertical_percentage_graph(dff, title, name1, name2)

@app.callback(
    dash.dependencies.Output('ReligionDonsMeth', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = ReligionDonorsDonMeth_2018[ReligionDonorsDonMeth_2018['Region'] == region]
    dff = dff.replace("Religion donors", "Donateur.trice.s de la religion")
    dff = dff.replace("Non-religion donors", "Autres donateur.trice.s")
    # name1 = "Religion donors"
    # name2 = "Non-religion donors"
    name1 = "Donateur.trice.s de la religion"
    name2 = "Autres donateur.trice.s"

    title = '{}, {}'.format("Taux de donateur.trice.s par méthode", region)
    return vertical_percentage_graph(dff, title, name1, name2)

@app.callback(
    dash.dependencies.Output('ReligionMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = ReligionDonorsMotivations_2018[ReligionDonorsMotivations_2018['Region'] == region]
    dff = dff.replace("Religion donors", "Donateur.trice.s de la religion")
    dff = dff.replace("Non-religion donors", "Autres donateur.trice.s")
    # name1 = "Religion donors"
    # name2 = "Non-religion donors"
    name1 = "Donateur.trice.s de la religion"
    name2 = "Autres donateur.trice.s"

    title = '{}, {}'.format("Motivations des dons", region)
    return vertical_percentage_graph(dff, title, name1, name2)

@app.callback(
    dash.dependencies.Output('ReligionBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = ReligionDonorsBarriers_2018[ReligionDonorsBarriers_2018['Region'] == region]
    dff = dff.replace("Religion donors", "Donateur.trice.s de la religion")
    dff = dff.replace("Non-religion donors", "Autres donateur.trice.s")
    # name1 = "Religion donors"
    # name2 = "Non-religion donors"
    name1 = "Donateur.trice.s de la religion"
    name2 = "Autres donateur.trice.s"

    title = '{}, {}'.format("Freins à donner plus", region)
    return vertical_percentage_graph(dff, title, name1, name2)

@app.callback(
    dash.dependencies.Output('VolRateAvgHrs2', 'figure'),
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

    title = '{}, {}'.format("Taux de bénévolat et nombre moyen d’heures de bénévolat selon la cause", region)

    return rate_avg_cause(dff1, dff2, name1, name2, title, vol=True)

@app.callback(
    dash.dependencies.Output('ReligionHrsCauses', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = ReligionVolsVolRates_2018[ReligionVolsVolRates_2018['Region'] == region]
    name1 = "Religion volunteer"
    name2 = "Non-religion volunteer"

    title = '{}, {}'.format("Rates of volunteering for other causes", region)
    return vertical_percentage_graph(dff, title, name1, name2)

@app.callback(
    dash.dependencies.Output('ReligionVolActivity', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = ReligionVolsActivities_2018[ReligionVolsActivities_2018['Region'] == region]
    dff = dff.replace("Religion volunteer", "Bénévoles de la religion")
    dff = dff.replace("Non-religion volunteer", "Autres bénévoles")
    
    # name1 = "Religion volunteer"
    # name2 = "Non-religion volunteer"
    name1 = "Bénévoles de la religion"
    name2 = "Autres bénévoles"

    title = '{}, {}'.format("Taux de bénévolat par activité", region)
    return vertical_percentage_graph(dff, title, name1, name2)

@app.callback(
    dash.dependencies.Output('ReligionVolMotivations', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = ReligionVolsMotivations_2018[ReligionVolsMotivations_2018['Region'] == region]
    dff = dff.replace("Religion volunteer", "Bénévoles de la religion")
    dff = dff.replace("Non-religion volunteer", "Autres bénévoles")
    
    # name1 = "Religion volunteer"
    # name2 = "Non-religion volunteer"
    name1 = "Bénévoles de la religion"
    name2 = "Autres bénévoles"

    title = '{}, {}'.format("Motivations des bénévoles", region)
    return vertical_percentage_graph(dff, title, name1, name2)

@app.callback(
    dash.dependencies.Output('ReligionVolBarriers', 'figure'),
    [
        dash.dependencies.Input('region-selection', 'value')
    ])
def update_graph(region):
    dff = ReligionVolsBarriers_2018[ReligionVolsBarriers_2018['Region'] == region]
    dff = dff.replace("Religion volunteer", "Bénévoles de la religion")
    dff = dff.replace("Non-religion volunteer", "Autres bénévoles")
    
    # name1 = "Religion volunteer"
    # name2 = "Non-religion volunteer"
    name1 = "Bénévoles de la religion"
    name2 = "Autres bénévoles"

    title = '{}, {}'.format("Freins à faire plus de bénévolat", region)
    return vertical_percentage_graph(dff, title, name1, name2)
