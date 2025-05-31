from dash import Dash, html
from dash import dash_table, dcc
import plotly.express as px

from dash import callback, Output, Input

import pandas as pd

test_data_url = 'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv'
df = pd.read_csv(test_data_url)

app = Dash()

app.layout = [
    html.Div(children='A More Interactive App with Controls and Callbacks'),
    html.Hr(),
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='pop', id='controls-and-radio-item'),
    dash_table.DataTable(data=df.to_dict(orient='records'), page_size=5),
    dcc.Graph(figure={}, id='controls-and-graph')
]

# ============================================
# Adding Controls to build Interaction
# ============================================
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg', color='continent', title=f'Population by {col_chosen}')
    return fig

if __name__ == '__main__':
    app.run(debug=True)