import dash
# import dash_auth
import dash_bootstrap_components as dbc



app = dash.Dash(
    __name__, 
    title='Centre canadien de connaissances sur les dons et le bénévolat',
    suppress_callback_exceptions=True, 
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

server = app.server