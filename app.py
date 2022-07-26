import dash
# import dash_auth
import dash_bootstrap_components as dbc



app = dash.Dash(
    __name__, 
    title='Centre Canadien de Connaissances sur les Dons et le Bénévolat',
    suppress_callback_exceptions=True, 
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

server = app.server