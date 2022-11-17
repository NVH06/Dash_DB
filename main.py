from dash import Dash
from src.layout import create_layout
from dash_bootstrap_components.themes import LUX

app = Dash(__name__, external_stylesheets=[LUX])
app.title = "DASHBOARD"
app.layout = create_layout(app)

if __name__ == "__main__":
    app.run_server(debug=False)
