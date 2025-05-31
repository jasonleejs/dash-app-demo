from dash import Dash, html
from dash import dcc, dash_table, callback, Output, Input

import plotly.express as px
import dash_bootstrap_components as dbc

import pandas as pd

test_data_url = 'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv'
df = pd.read_csv(test_data_url)


external_stylesheets = [dbc.themes.CERULEAN]
app = Dash(external_stylesheets=external_stylesheets)



app.layout = [
    dbc.Row(html.Div(children="App using DBC (Dash Bootstrap Components)", className="text-primary text-center fs-3")),
    dbc.Row(dbc.RadioItems(
        options=[{'label': x, 'value': x} for x in ['pop', 'lifeExp', 'gdpPercap']],
        value='lifeExp',
        inline=True,
        id='radio-buttons')
        
    ),
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                data=df.to_dict('records'),
                page_size=10,
                style_cell={'textAlign': 'left'},
            )
        ], width=6),
        dbc.Col([
            dcc.Graph(figure={}, id='graph-placeholder')
        ], width= 6)
    ])
]

@callback(
    Output(component_id='graph-placeholder', component_property='figure'),
    Input(component_id='radio-buttons', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg', color='continent',
                       title=f"Average {col_chosen} by Continent")
    return fig

if __name__ == '__main__':
    app.run(debug=True, port=8050)