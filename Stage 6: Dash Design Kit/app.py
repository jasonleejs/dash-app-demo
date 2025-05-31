from dash import Dash, html
from dash import dash_table, dcc, callback, Output, Input
import plotly.express as px

import dash_design_kit as ddk

import pandas as pd

test_data_url = 'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv'
df = pd.read_csv(test_data_url)


app = Dash()

app.layout = ddk.App([
    ddk.Header(
        ddk.Title("App using (Dash Design Kit)")
    ),
    dcc.RadioItems(
        options=['pop', 'lifeExp', 'gdpPercap'],
        value='lifeExp',  # default value
        inline=True,
        id='my-radio-buttons'
    ),
    ddk.Row([
        ddk.Card([
            dash_table.DataTable(data=df.to_dict('records'), page_size=10, width=50)
        ], width=50),
        ddk.Card([
            ddk.Graph(figure={}, id='graph-placeholder-ddk')
        ], width=50)
    ]),
])

@callback(
    Output(component_id='graph-placeholder-ddk', component_property='figure'),
    Input(component_id='my-radio-buttons', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg', color='continent',
                       title=f"Average {col_chosen} by Continent")
    return fig


if __name__ == '__main__':
    app.run(debug=True, port=8050)
