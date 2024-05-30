
from dotenv import load_dotenv
import os
from numpy import who
import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

load_dotenv()

env_var = os.getenv("DATA_SOURCE")

if env_var is None:
    raise ValueError("There is no file path in the environment variables")

if not os.path.exists(env_var):
    raise FileNotFoundError("The file does not exist")

df = pd.read_json(env_var)

gb_df = df.groupby("RequestPath").count().reset_index()

fig = px.bar(gb_df, y="RequestPath", x="ClientHost")

filtered_df = df[df["RequestPath"].str.contains(r"14032025/", na=False) & (df["RequestPath"].str.len() < 30)]


fig2 = px.scatter(filtered_df, y="RequestPath", x="ClientHost")

app = Dash(__name__)

app.layout = html.Div(children=[
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    dcc.Graph(
        id='Local',
        figure=fig2
    )
])

if __name__ == '__main__':
    app.run(debug=True)

