import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd


data = {
    "Region": ["north", "east", "south", "west"] * 10,
    "Sales": [20, 35, 50, 40, 30, 45, 55, 60, 25, 50] * 4,
    "Month": list(range(1, 11)) * 4
}
df = pd.DataFrame(data)


app = dash.Dash(__name__)


app.layout = html.Div(
    style={"fontFamily": "Arial, sans-serif", "backgroundColor": "#f9f9f9", "padding": "20px"},
    children=[
        html.H1("Soul Foods Sales Visualiser", style={"textAlign": "center", "color": "#333"}),
        html.Div(
            [
                html.Label("Filter by Region:", style={"fontSize": "18px", "fontWeight": "bold"}),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                        {"label": "All", "value": "all"},
                    ],
                    value="all",
                    style={"display": "flex", "gap": "10px"}
                ),
            ],
            style={
                "padding": "10px",
                "backgroundColor": "#e6f7ff",
                "borderRadius": "10px",
                "marginBottom": "20px",
            },
        ),
        dcc.Graph(id="sales-graph"),
    ],
)


@app.callback(
    Output("sales-graph", "figure"),
    [Input("region-filter", "value")]
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="Month",
        y="Sales",
        color="Region",
        title="Pink Morsels Sales by Region",
        labels={"Month": "Month", "Sales": "Sales (Units)"}
    )
    fig.update_layout(
        template="plotly_white",
        title={"x": 0.5},
        xaxis_title="Month",
        yaxis_title="Sales (Units)",
        legend_title="Region",
    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
