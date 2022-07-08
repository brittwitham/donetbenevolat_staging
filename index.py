from dash import dcc, html
from dash.dependencies import Input, Output
from app import app, server
# from apps import *
from apps import (
#     GAV0301, 
    WDA0101_fr, 
    HDC0102_fr,
    UTD0103_fr,
    WDC0105_fr,
    WDV0202_fr,
    WKC0106_fr,
    WTO0107_fr,
    WVA0201_fr,
    UTV0203_fr,
#     test_layout,
#     HOA0204,
#     WDC0205,
#     WKC0206,
#     WTO0207,
#     GAV0301,
#     GAV0302,
#     GAV0303,
#     GAV0304,
#     GAV0305,
#     GAV0306,
#     GAV0307,
#     GAV0308,
#     HDC0102_13,
#     WDC0105_13
)
from apps import WTO0107_fr
import homepage

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return homepage.layout
    elif pathname == '/WDA0101_fr':
        return WDA0101_fr.layout
    elif pathname == '/HDC0102_fr':
        return HDC0102_fr.layout
    elif pathname == '/UTD0103_fr':
        return UTD0103_fr.layout
    elif pathname == '/WDC0105_fr':
        return WDC0105_fr.layout
    elif pathname == '/WKC0106_fr':
        return WKC0106_fr.layout
    elif pathname == '/WTO0107_fr':
        return WTO0107_fr.layout
    elif pathname == '/WDV0202_fr':
        return WDV0202_fr.layout
    elif pathname == '/WVA0201_fr':
        return WVA0201_fr.layout
    elif pathname == '/UTV0203_fr':
        return UTV0203_fr.layout
#     elif pathname == '/test':
#         return test_layout.layout
#     elif pathname == '/HOA0204':
#         return HOA0204.layout
#     elif pathname == '/WDC0205':
#         return WDC0205.layout
#     elif pathname == '/WKC0206':
#         return WKC0206.layout
#     elif pathname == '/WTO0207':
#         return WTO0207.layout
#     elif pathname == '/GAV0301':
#         return GAV0301.layout
#     elif pathname == '/GAV0302':
#         return GAV0302.layout
#     elif pathname == '/GAV0303':
#         return GAV0303.layout
#     elif pathname == '/GAV0304':
#         return GAV0304.layout
#     elif pathname == '/GAV0305':
#         return GAV0305.layout
#     elif pathname == '/GAV0306':
#         return GAV0306.layout
#     elif pathname == '/GAV0307':
#         return GAV0307.layout
#     elif pathname == '/GAV0308':
#         return GAV0308.layout
#     elif pathname == '/HDC0102_13':
#         return HDC0102_13.layout
#     elif pathname == '/WDC0105_13':
#         return WDC0105_13.layout
#     else:
#         return '404'

if __name__ == '__main__':
    app.run_server(debug=True)