from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(
                # dcc.Link("Home", href="/")
                dbc.NavLink("À propos", href="https://www.donetbenevolat.ca/",external_link=True)
            ),
            dbc.NavItem(
                dbc.NavLink("EN", href="http://app.givingandvolunteering.ca/",external_link=True)
            ),
        ],
        brand="Centre canadien de connaissances sur les dons et le bénévolat",
        brand_href="/",
        color="#4B161D",
        dark=True,
        sticky='top'
    )

footer = html.Footer(
       dbc.Container(
           dbc.Row(
               html.Div([
                #    html.P('© Imagine Canada 2021',className="text-center"),
                   html.P("Ce site Web a été développé grâce au financement du gouvernement du Canada, par le biais du Programme de partenariats pour le développement social d'Emploi et Développement social Canada.",className="text-center")
               ]
                   ,className='col-md-10 col-lg-8 mx-auto mt-5'
               ),
           )
       )
   )

content = dbc.Container(
    [
        dcc.Location(id='url', refresh=False),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Qui donne aux organismes caritatifs et combien?",className='card-title'), href='/Qui_donne_aux_organismes_caritatifs_et_combien_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("Plus de deux tiers des personnes au Canada donnent de l’argent aux organismes de bienfaisance et à but non lucratif et leur contribution se chiffre approximativement à 11,9 milliards $. Cette analyse montre comment les tendances des dons (probabilité de donner, montants caractéristiques, etc.) varient souvent selon le profil démographique des personnes.",className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
                dcc.Location(id='url', refresh=False),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Comment donne-t-on au Canada?",className='card-title'), href='/Comment_donne_t_on_au_Canada_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("Les personnes donnent de nombreuses façons différentes au Canada. Cette analyse détaille combien de personnes donnent par chaque méthode, le montant qu’elles ont tendance à donner et la variation de leurs méthodes de dons selon leur profil démographique.",className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
                dcc.Location(id='url', refresh=False),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Comprendre les grand.e.s. donateur.trice.s",className='card-title'), href='/Comprendre_les_grands_donateurs_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("Bien qu’approximativement neuf personnes sur dix donnent de l’argent au Canada, plus de quatre cinquièmes de la valeur totale des dons provient des grand.e.s donateur.trice.s (le quart de ces personnes qui donnent les montants les plus importants). Cette analyse porte sur le profil démographique des grand.e.s donateur.trice.s, sur les causes que ces personnes soutiennent, sur leurs motivations et sur les freins qui les empêchent de donner plus.",className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Pourquoi donne-t-on au Canada?",className='card-title'), href='/Pourquoi_donne_t_on_au_Canada_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("Les personnes donnent pour de nombreuses raisons différentes au Canada. Cette analyse révèle les différentes motivations courantes, comment ces motivations varient selon le profil démographique des donateur.trice.s et les liens de celles-ci avec les montants donnés et les causes soutenues.",className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Qu'est-ce qui empeche de donner plus?",className='card-title'), href='/Qu_est_ce_qui_empeche_de_donner_plus_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Bien que les personnes soient généreuses au Canada, plusieurs facteurs peuvent limiter leurs dons et les empêchent de donner plus. Cette analyse identifie les facteurs qui limitent les dons, leur incidence sur les montants donnés, la variation des freins potentiels selon le profil démographique des donateur.trice.s et leurs liens avec certaines causes.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Quels types d'organismes soutient-on au Canada?",className='card-title'), href='/Quels_types_organismes_soutient_on_au_Canada_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Cette analyse mesure les niveaux de soutien selon les causes, le nombre de personnes soutenant chaque cause, les montants caractéristiques des dons et la répartition de la valeur totale des dons.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Qui sont les bénévoles et combien d'heures donnent-ils?" ,className='card-title'), href='/Qui_sont_les_benevoles_et_combien_heures_donnent_ils_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Un peu plus de deux cinquièmes des personnes au Canada font don de 1,7 million d’heures de leur temps aux organismes de bienfaisance et à but non lucratif. Cette analyse montre comment les tendances du bénévolat (probabilité de faire du bénévolat, nombres d’heures de bénévolat caractéristiques, etc.) varient souvent selon le profil démographique des bénévoles.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Quelles sont les activités des bénévoles?",className='card-title'), href='/Quelles_sont_les_activites_des_benevoles_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Le bénévolat prend de nombreuses formes différentes au Canada, de la collecte de fonds à la lutte contre les incendies. Cette analyse détaille les activités des bénévoles et la tendance de leurs activités à varier selon leur profil démographique.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Comprendre les bénévoles très engagé.e.s",className='card-title'), href='/Comprendre_les_benevoles_tres_engages_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Au niveau national, environ quatre cinquièmes des heures de bénévolat sont attribuables aux bénévoles très engagé.e.s (le quart des bénévoles qui donnent le plus d’heures). Cette analyse porte sur le profil démographique des bénévoles très engagé.e.s, sur les causes que ces personnes soutiennent, sur leurs motivations et sur les freins qui les empêchent de faire plus de bénévolat.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Aide d’autrui et amélioration communautaire",className='card-title'), href='/Aide_autrui_et_amelioration_communautaire_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                En plus de faire du bénévolat pour les organismes de bienfaisance et à but non lucratif, les personnes aident aussi directement autrui au Canada (sans faire appel à un organisme) et participent à diverses formes d’améliorations communautaires. Cette analyse identifie les personnes qui pratiquent ces autres formes de soutien, leurs types d’activités et le nombre d’heures dont elles font don habituellement.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Pourquoi fait-on du bénévolat?",className='card-title'), href='/Pourquoi_fait_on_du_benevolat_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Les personnes font du bénévolat pour de nombreuses raisons différentes au Canada. Cette analyse révèle les différentes motivations courantes, leur incidence habituelle sur les niveaux de bénévolat, comment ces motivations varient selon le profil démographique des bénévoles et les liens entre les motivations et le soutien de certaines causes.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Qu’est-ce qui empêche de faire du bénévolat?",className='card-title'), href='/Qu_est_ce_qui_empeche_de_faire_du_benevolat_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Cette analyse porte sur les facteurs qui peuvent limiter les heures de bénévolat au Canada ou même qui empêchent totalement les personnes de faire du bénévolat. Elle décrit l’incidence des divers freins, leur incidence habituelle sur le nombre d’heures de bénévolat, leurs variations selon le profil démographique des bénévoles et les liens entre ces freins et certaines causes.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("À quels types d’organismes fait-on don de son temps au Canada?",className='card-title'), href='/A_quels_types_organismes_fait_on_don_de_son_temps_au_Canada_2018'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Cette analyse est axée sur les causes soutenues par les bénévoles au Canada. Elle mesure l’importance du bassin de bénévoles pour chaque cause, le nombre d’heures de bénévolat caractéristique au bénéfice de chaque cause et la répartition du nombre total d’heures de bénévolat entre les causes.
                                """,className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
#        html.Br(),
 #       html.Hr(),
  #              html.H2("Dons et bénévolat selon le type d'organisation"),
   #     html.Br(),
    #    dbc.Row(
     #       html.Div(
      #          html.Div(
       #             html.Div(
         #               html.Div(
          #                  [
           #                     dcc.Link(html.H4("Dons d’argent et bénévolat pour les organismes de santé",className='card-title'), href='/dons_dargent_et_benevolat_pour_les_organismes_de_sante_2018'),
            #                    # # html.H6("David Lasby",className="text-muted card-subtitle"),
             #                   html.P("""
              #                  Cette analyse des tendances des dons et du bénévolat au bénéfice des hôpitaux et des autres organismes de santé précise qui soutient ces organismes, le montant de leurs contributions, leurs méthodes de dons et les types d’activités bénévoles auxquelles ces personnes participent, ainsi que les motivations de leurs dons et de leur bénévolat pour ces organismes et les freins qui peuvent les empêcher de contribuer encore plus.
               #                 """),
                #                # className='card-text')
                 #           ]
                  #      ),
                   #     className='card-body'
#                    ),
 #                   className="card"
  #              ),
   #             className="col-md-10 col-lg-8"
    #        )
     #   ),
      #  html.Br(),
       # dbc.Row(
        #    html.Div(
         #       html.Div(
          #          html.Div(
           #             html.Div(
            #                [
              #                  dcc.Link(html.H4("Dons et bénévolat pour les organismes religieux",className='card-title'), href='/dons_et_benevolat_pour_les_organismes_religieux_2018'),
               #                 # html.H6("David Lasby",className="text-muted card-subtitle"),
                #                html.P("""
                 #               Cette analyse des tendances des dons et du bénévolat au bénéfice des congrégations religieuses et des autres organismes religieux précise qui soutient ces organismes, le montant de leurs contributions, leurs méthodes de dons et les types d’activités bénévoles auxquelles ces personnes participent, ainsi que les motivations de leurs dons et de leur bénévolat pour ces organismes et les freins qui peuvent les empêcher de contribuer encore plus.
                  #              """),
                   #             # className='card-text')
                    #        ]
                     #   ),
                      #  className='card-body'
#                    ),
 #                   className="card"
  #              ),
   #             className="col-md-10 col-lg-8"
    #        )
     #   ),
      #  html.Br(),
       # dbc.Row(
        #    html.Div(
         #       html.Div(
          #          html.Div(
           #             html.Div(
            #                [
             #                   dcc.Link(html.H4("Dons et bénévolat pour les organismes du secteur de l’éducation",className='card-title'), href='/dons_et_benevolat_pour_les_organismes_du_secteur_de_leducation_2018'),
              #                  # html.H6("David Lasby",className="text-muted card-subtitle"),
               #                 html.P("""
                #                Cette analyse des tendances des dons et du bénévolat au bénéfice des établissements scolaires primaires et secondaires, des universités, des collèges et des établissements de recherche précise qui soutient ces organismes, le montant de leurs contributions, leurs méthodes de dons et les types d’activités bénévoles auxquelles ces personnes participent, ainsi que les motivations de leurs dons et de leur bénévolat pour ces organismes et les freins qui peuvent les empêcher de contribuer encore plus.
                 #               """),
                  #              # className='card-text')
                   #         ]
                    #    ),
                     #   className='card-body'
#                    ),
#                    className="card"
 #               ),
  #              className="col-md-10 col-lg-8"
   #         )
    #    ),
     #   html.Br(),
      #  dbc.Row(
       #     html.Div(
        #        html.Div(
         #           html.Div(
          #              html.Div(
           #                 [
            #                    dcc.Link(html.H4("Dons et bénévolat pour les organismes de services sociaux",className='card-title'), href='/dons_et_benevolat_pour_les_organismes_de_services_sociaux_2018'),
             #                   # html.H6("David Lasby",className="text-muted card-subtitle"),
              #                  html.P("""
               #                 Cette analyse des tendances des dons et du bénévolat au bénéfice des organismes sociaux précise qui soutient ces organismes, le montant de leurs contributions, leurs méthodes de dons et les types d’activités bénévoles auxquelles ces personnes participent, ainsi que les motivations de leurs dons et de leur bénévolat pour ces organismes et les freins qui peuvent les empêcher de contribuer encore plus.
                #                """),
                 #               # className='card-text')
                  #          ]
                   #     ),
                    #    className='card-body'
#                    ),
#                    className="card"
 #               ),
  #              className="col-md-10 col-lg-8"
   #         )
    #    ),
     #   html.Br(),
      #  dbc.Row(
       #     html.Div(
        #        html.Div(
         #           html.Div(
          #              html.Div(
           #                 [
            #                    dcc.Link(html.H4("Dons et bénévolat pour les organismes des arts et des loisirs",className='card-title'), href='/dons_et_benevolat_pour_les_organismes_des_arts_et_des_loisirs_2018'),
             #                   # html.H6("David Lasby",className="text-muted card-subtitle"),
              #                  html.P("""
               #                 Cette analyse des tendances des dons et du bénévolat au bénéfice des organismes des arts, de la culture, des loisirs et des sports précise qui soutient ces organismes, le montant de leurs contributions, leurs méthodes de dons et les types d’activités bénévoles auxquelles ces personnes participent, ainsi que les motivations de leurs dons et de leur bénévolat pour ces organismes et les freins qui peuvent les empêcher de contribuer encore plus.
                #                """,
                 #               className='card-text')
                  #          ]
                   #     ),
                    #    className='card-body'
#                    ),
#                    className="card"
 #               ),
  #              className="col-md-10 col-lg-8"
   #         )
    #    ),
#        html.Br(),
 #       html.Hr(),
  #              html.H2("Dons et bénévolat selon les caractéristiques démographiques"),
#        html.Br(),
 #       dbc.Row(
  #          html.Div(
   #             html.Div(
    #                html.Div(
     #                   html.Div(
      #                      [
       #                         dcc.Link(html.H4("Les dons et le bénévolat des personnes nouvellement arrivées au canada",className='card-title'), href='/les_dons_et_le_benevolat_des_personnes_nouvellement_arrivees_au_canada_2018'),
        #                        html.P("""
         #                       Cette analyse des dons et du bénévolat des personnes nouvellement arrivées au Canada approfondit leurs différences avec ceux des personnes nées au Canada. Elle porte sur l’importance générale des dons et du bénévolat, les causes soutenues, les méthodes de dons, les types d’activités bénévoles, les motivations et les freins aux dons et au bénévolat, ainsi que sur des formes de bénévolat moins conventionnelles.
          #                      """),
#
 #                           ]
  #                      ),
   #                     className='card-body'
    #                ),
     #               className="card"
      #          ),
       #         className="col-md-10 col-lg-8"
        #    )
  #      ),
#        html.Br(),
 #       dbc.Row(
  #          html.Div(
   #             html.Div(
    #                html.Div(
     #                   html.Div(
      #                      [
       #                         dcc.Link(html.H4("Les dons et le bénévolat des personnes agées",className='card-title'), href='/les_dons_et_le_benevolat_des_personnes_agees_2018'),
        #                        html.P("""
         #                       Cette analyse des dons et du bénévolat des personnes âgées (de 65 ans ou plus) approfondit leurs différences avec ceux des personnes plus jeunes au Canada. Elle porte sur l’importance générale des dons et du bénévolat, les causes soutenues, les méthodes de dons, les types d’activités bénévoles, les motivations et les freins aux dons et au bénévolat, ainsi que sur des formes de bénévolat moins conventionnelles. Dans la mesure du possible, l’analyse fait la distinction entre les personnes de 65 à 74 ans et celles de 75 ans ou plus.
          #                      """),
           #                 ]
            #            ),
             #           className='card-body'
              #      ),
               #     className="card"
#                ),
 #               className="col-md-10 col-lg-8"
  #          )
   #     ),
    #    html.Br(),
     #   dbc.Row(
      #      html.Div(
       #         html.Div(
        #            html.Div(
         #               html.Div(
          #                  [
           #                     dcc.Link(html.H4("Les dons et le bénévolat des jeunes",className='card-title'), href='/les_dons_et_le_benevolat_des_jeunes_2018'),
            #                    # html.H6("David Lasby",className="text-muted card-subtitle"),
             #                   html.P("""
              #                  Cette analyse des dons et du bénévolat des personnes jeunes (de moins de 34 ans) approfondit leurs différences avec ceux des personnes plus âgées au Canada. Elle porte sur l’importance générale des dons et du bénévolat, les causes soutenues, les méthodes de dons, les types d’activités bénévoles, les motivations et les freins aux dons et au bénévolat, ainsi que sur des formes de bénévolat moins conventionnelles. Dans la mesure du possible, l’analyse fait la distinction entre les personnes de 15 à 24 ans et celles de 25 à 34 ans. 
               #                 """,
                #                className='card-text')
                 #           ]
                  #      ),
                   #     className='card-body'
                    #),
#                    className="card"
 #               ),
  #              className="col-md-10 col-lg-8"
   #         )
    #    ),
        html.Br(),
        html.Hr(),
        html.H2("Articles de 2013"),
        html.Br(),
        html.H3("Note générale sur la comparaison des résultats de l’enquête de 2013 et de celle de 2018 "),
        html.P(
        """En raison des modifications méthodologiques entre les versions de 2013 et de 2018 de l’enquête (principalement liées à la nouvelle option de répondre au questionnaire en ligne), la comparaison directe des résultats entre ses deux versions n’est pas pertinente. Les tendances générales (p. ex. variations selon les caractéristiques personnelles et économiques, liens avec les motivations et les freins, etc.) sont très similaires, mais les estimations clés, comme les taux généraux des dons et du bénévolat, sont quelque peu différentes. Bien qu’il soit impossible d’en être certain, ces différences sont vraisemblablement moins attribuables à des changements dans les habitudes de don et de bénévolat qu’aux modifications méthodologiques. """),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Qui donne aux organismes caritatifs et combien? (2013)",className='card-title'), href='/qui_donne_aux_organismes_caritatifs_et_combien_2013'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("En 2013, un peu plus de quatre cinquièmes des personnes au Canada ont contribué financièrement aux organismes de bienfaisance et à but non lucratif, leurs contributions se chiffrant environ à 12,8 milliards $. Cette analyse porte sur les variations générales des tendances (probabilité de donner, montants habituels des contributions, etc.) selon les caractéristiques personnelles et économiques des donateur.trice.s",className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Comment donne-t-on au Canada? (2013)",className='card-title'), href='/comment_donne_t_on_au_canada_2013'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Cette analyse des méthodes de dons des personnes au Canada en 2013 porte sur les montants qu’elles avaient tendance à donner et sur les variations de ces méthodes selon les caractéristiques personnelles et économiques des donateur.trice.s..
                                """),
                                # className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Pourquoi donne-t-on au Canada? (2013)",className='card-title'), href='/pourquoi_donne_t_on_au_canada_2013'),
                                # html.H6("David Lasby",className="text-muted card-subtitle"),
                                html.P("""
                                Cette analyse des motivations des dons des personnes au Canada en 2013 porte sur les différentes motivations courantes, sur leurs variations selon les caractéristiques personnelles et économiques des donateur.trice.s. et sur les liens entre les motivations et les montants des dons et les causes soutenues.
                                """),
                                # className='card-text')
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Qu’est-ce qui empêche de donner plus? (2013)",className='card-title'), href='/qu_est_ce_qui_empeche_de_donner_plus_2013'),
                                html.P(
                                    """
                                    Cette analyse des freins rencontrés par les donateur.trice.s en 2013 porte sur les facteurs qui ont limité les dons, sur l’incidence de ces freins sur les montants habituels des dons, sur les variations de ceux-ci selon les caractéristiques personnelles et économiques des donateur.trice.s. et sur leurs liens avec des causes particulières.
                                    """
                                )
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
#        html.Br(),
 #       dbc.Row(
  #          html.Div(
   #             html.Div(
    #                html.Div(
     #                   html.Div(
      #                      [
       #                         dcc.Link(html.H4("Qui sont les bénévoles et combien d’heures donnent-ils? (2013)",className='card-title'), href='/qui_sont_les_benevoles_et_combien_dheures_donnent_ils_2013'),
        #                        html.P(
         #                           """En 2013, un peu plus de deux cinquièmes des personnes au Canada ont fait du bénévolat pour les organismes de bienfaisance et à but non lucratif en leur faisant don de 2 milliards d’heures de leur temps. Cette analyse porte sur les variations générales des tendances (probabilité de faire du bénévolat, nombre habituel d’heures de bénévolat, etc.) selon les caractéristiques personnelles et économiques des bénévoles."""
          #                      )
           #                 ]
            #            ),
             #           className='card-body'
              #      ),
               #     className="card"
  #              ),
   #             className="col-md-10 col-lg-8"
    #        )
     #   ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Quelles sont les activités des bénévoles? (2013)",className='card-title'), href='/quelles_sont_les_activites_des_benevoles_2013'),
                                html.P(
                                    """Cette analyse des activités des bénévoles au Canada en 2013 porte sur la fréquence de chaque activité, le nombre habituel d’heures de bénévolat et les variations de ces activités selon les caractéristiques personnelles et économiques des bénévoles."""
                                )
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
        html.Br(),
        dbc.Row(
            html.Div(
                html.Div(
                    html.Div(
                        html.Div(
                            [
                                dcc.Link(html.H4("Pourquoi fait-on du bénévolat? (2013)",className='card-title'), href='/pourquoi_fait_on_du_benevolat_2013'),
                                html.P(
                                    """Cette analyse des motivations des bénévoles au Canada en 2013 porte sur les différentes motivations courantes des bénévoles, sur les variations de ces activités selon les caractéristiques personnelles et économiques des bénévoles et sur les liens entre les motivations et le nombre habituel d’heures de bénévolat et les causes soutenues."""
                                )
                            ]
                        ),
                        className='card-body'
                    ),
                    className="card"
                ),
                className="col-md-10 col-lg-8"
            )
        ),
#        html.Br(),
 #       dbc.Row(
  #          html.Div(
   #             html.Div(
    #                html.Div(
     #                   html.Div(
      #                      [
       #                         dcc.Link(html.H4("Qu’est-ce qui empêche de faire du bénévolat? (2013)",className='card-title'), href='/qu_est_ce_qui_empeche_de_faire_du_benevolat_2013'),
        #                        html.P(
         #                           """Cette analyse des freins rencontrés par les bénévoles au Canada en 2013 porte sur les facteurs qui ont limité leur nombre d’heures de bénévolat, sur l’incidence de ces freins sur le nombre habituel d’heures de bénévolat, sur les variations des heures de bénévolat selon les caractéristiques personnelles et économiques des bénévoles et les causes soutenues par les bénévoles."""
          #                      )
           #                 ]
            #            ),
             #           className='card-body'
              #      ),
       #             className="card"
        #        ),
         #       className="col-md-10 col-lg-8"
     #       )
      #  ),
    ]
)


layout = html.Div([
    navbar,
    html.Header([
        html.Div(className='overlay'),
        dbc.Container(
            dbc.Row(
                [
                    html.Div(
                        html.Div(
                            html.H1("Des données pour propulser l'impact communautaire"),
                            # className='site-heading data-catalyst'
                            className='data-catalyst'
                        ),
                        className="col-md-10 col-lg-8 mx-auto position-relative"
                    ),
                ]
            )
        ), 
    ],
        className='masthead',
        style={'backgroundImage':"url('./assets/portal_image.png')"}
    ),
    content,
    footer
])

