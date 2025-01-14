import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


data = {
    "date": [
        "2020-12-01", "2020-12-02", "2020-12-03", "2020-12-04", "2020-12-05", 
        "2021-01-01", "2021-01-02", "2021-01-03", "2021-01-04", "2021-01-05", 
        "2021-01-15", "2021-01-16", "2021-01-17", "2021-01-18", "2021-01-19"
    ],
    "sales": [100, 110, 105, 98, 95, 102, 115, 120, 110, 108, 130, 135, 125, 140, 150]
}

df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])  


app = dash.Dash(__name__)

fig = px.line(df, x='date', y='sales', title='Sales Over Time', labels={'date': 'Date', 'sales': 'Sales'},
              line_shape='linear')
fig.add_vline(x=pd.to_datetime('2021-01-15'), line=dict(color='red', dash='dash'), 
              annotation_text="Price Increase", annotation_position="top right")

app.layout = html.Div(children=[
    html.H1("Sales Data Visualizer for Soul Foods"),
    dcc.Graph(figure=fig),
])

if __name__ == '__main__':
    app.run_server(debug=True)
