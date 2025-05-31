from dash import Dash, html
from dash import dash_table, dcc, callback, Input, Output
import plotly.express as px

import pandas as pd

test_data_url = 'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv'
df = pd.read_csv(test_data_url)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(external_stylesheets=external_stylesheets)

app.layout = [
    html.Div(children="An App with some Style", className='row',
             style={'textAlign': 'center', 'margin': '20px', 'fontSize': '24px'}),
    html.Div(children=[
        dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'],
                       value='lifeExp',# default value
                       inline=True,
                       id='my-radio-buttons')
        ]),
    html.Div(className='row', children=[
        html.Div(className='six columns', children=[
            dash_table.DataTable(data=df.to_dict(orient='records'), page_size=10, style_table={'overflowX': 'auto'})
        ]),
        html.Div(className='six columns', style={'float': 'right'}, children=[
            dcc.Graph(figure={}, id='histo-chart')
        ])    
    ])
    
]

@callback(
    Output(component_id='histo-chart', component_property='figure'),
    Input(component_id='my-radio-buttons', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg', color='continent',
                       title=f"Average {col_chosen} by Continent")
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)