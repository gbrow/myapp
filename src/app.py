'''
 # @ Create Time: 2024-08-31 09:16:28.827899
'''

from dash import html, dash, dcc
import dash_leaflet as dl
import pandas as pd
import numpy as np

# Create example data frame.
lats = [56, 56, 56]
lons = [10, 11, 12]
df = pd.DataFrame(columns=["lat", "lon"], data=np.column_stack((lats, lons)))

# Create markers from data frame.
markers = [dl.Marker(position=[row["lat"], row["lon"]])
           for i, row in df.iterrows()]

# Create example app.
app = dash.Dash(
    title="MyApp",
    external_stylesheets=[
        'https://codepen.io/chriddyp/pen/bWLwgP.css'])

# Declare server for Heroku deployment. Needed for Procfile.
server = app.server

app.layout = html.Div([
    html.H1(children='Dash Leaflet App'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    html.Hr(),

    dl.Map(children=[dl.TileLayer(url="https://a.tile.openstreetmap.org/{z}/{x}/{y}.png"), dl.LayerGroup(markers)],
           style={'width': "100%", 'height': "100%"}, center=[56, 11], zoom=9, id="map"),

    dcc.Markdown(
        "Learn more about [Dash Leaflet](https://github.com/thedirtyfew/dash-leaflet)")

], style={'width': '1000px', 'height': '500px'})


if __name__ == '__main__':
    app.run_server(debug=True)
