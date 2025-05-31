from dash import Dash, html
from dash import dash_table, dcc, callback, Output, Input

import plotly.express as px

import dash_mantine_components as dmc

import pandas as pd

test_data_url = 'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv'
df = pd.read_csv(test_data_url)

app = Dash()

app.layout = dmc.MantineProvider([
    dmc.Container([
        dmc.Title("App using Dash Mantine Components",style={'color': 'black', 'text-align': 'center'}, size='h3'),
        dmc.RadioGroup(
            [dmc.Radio(i, value=i) for i in ['pop', 'lifeExp', 'gdpPercap']],
            value='pop', 
            id='my-radio-buttons',
            size="md",
        ),
        dmc.Grid([
            dmc.GridCol([
                dash_table.DataTable(
                    data=df.to_dict('records'),
                    page_size=10)
            ], span=6),
            dmc.GridCol([
                dcc.Graph(figure={}, id='graph-placeholder')
            ], span=6)
        ])
    ], fluid=True), # fluid makes the container width flexible
])

@callback(
    Output(component_id='graph-placeholder', component_property='figure'),
    Input(component_id='my-radio-buttons', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg', color='continent',
                       title=f"Average {col_chosen} by Continent")
    return fig  

if __name__ == '__main__':
    app.run(debug=True, port=8050)