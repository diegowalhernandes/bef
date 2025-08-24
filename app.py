import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import geopandas as gpd

# --- Dados fictícios para o MVP ---
bases = pd.DataFrame({
    "nome": ["Base Centro", "Base Zona Leste", "Base Zona Sul"],
    "lat": [-23.55, -23.53, -23.62],
    "lon": [-46.63, -46.50, -46.70]
})

hidrantes = pd.DataFrame({
    "id": [1, 2, 3],
    "lat": [-23.54, -23.56, -23.58],
    "lon": [-46.60, -46.65, -46.62]
})

reservatorios = pd.DataFrame({
    "id": [1, 2],
    "lat": [-23.57, -23.59],
    "lon": [-46.68, -46.55]
})

# Exemplo de focos (em MVP podemos carregar da API do INPE)
focos = pd.DataFrame({
    "id": [1, 2, 3],
    "lat": [-23.60, -23.52, -23.56],
    "lon": [-46.64, -46.58, -46.62]
})

# --- Criação do Dash ---
app = dash.Dash(__name__)

fig = px.scatter_mapbox(bases, lat="lat", lon="lon", text="nome", 
                        color_discrete_sequence=["red"], size_max=15, zoom=11)

# Adiciona camadas
fig.add_scattermapbox(lat=hidrantes["lat"], lon=hidrantes["lon"], 
                      mode="markers", marker=dict(size=9, color="blue"), name="Hidrantes")

fig.add_scattermapbox(lat=reservatorios["lat"], lon=reservatorios["lon"], 
                      mode="markers", marker=dict(size=11, color="green"), name="Reservatórios")

fig.add_scattermapbox(lat=focos["lat"], lon=focos["lon"], 
                      mode="markers", marker=dict(size=13, color="orange"), name="Focos de Incêndio")

# Layout do mapa
fig.update_layout(mapbox_style="open-street-map", height=700, margin={"r":0,"t":0,"l":0,"b":0})

# Layout do dashboard
app.layout = html.Div([
    html.H1("MVP - Batalhão Escudo de Fogo"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
