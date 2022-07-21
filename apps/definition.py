from pydoc import classname
import dash
from dash import html
from dash.dependencies import  Input, Output
import dash_bootstrap_components as dbc

from app import app

layout = dbc.Container(
    [
        dbc.Row(
            html.Div(
                html.Div(
                    html.P(
                        "Les chiffres de cette visualisation sont des estimations des valeurs de la population, fondées sur une enquête représentative de la population canadienne. Comme dans toutes les enquêtes, un certain degré d’incertitude est associé à chaque estimation. Les lignes noires représentent cette incertitude pour chaque estimation. Compte tenu de l’importance et de la conception de l’enquête, les valeurs vraies de la population devraient se situer à l’intérieur des limites indiquées par les lignes noires dans 95 % des cas. Au chapitre de l’interprétation, quand les limites de différentes estimations se recoupent de manière significative, les valeurs vraies de la population qui sont comparées ne sont probablement pas différentes. En revanche, quand ces limites ne se recoupent pas du tout (ou seulement légèrement), il est plus probable que les valeurs de la population soient différentes.",className='card-text')
                ), className="d-flex justify-content-center p-3"
            ), 
        ),
        dbc.Row(
            html.Div([
                dbc.Button(
                        "Fermer", id="input", className="m-2", n_clicks=0,
                    ),
                html.Div(id='output-clientside'),

            ], className='d-flex justify-content-center p-3')
        ),
    ]
)



app.clientside_callback(
    """
        function(n_clicks) {
            if (n_clicks  === 0) {
                throw window.dash_clientside.PreventUpdate;
            }

            if (n_clicks === 0) {
                return window.dash_clientside.no_update;
            }
            
            if (n_clicks >= 1) {
                window.open('', '_self', '');
                window.close();  
            }
        }
        """,
    Output('output-clientside', 'children'),
    [Input("input", "n_clicks")]
)

if __name__ == "__main__":
    app.run_server(debug=True)