# ==========================================
# Imports
# ==========================================
from dash import Dash, html
from dash import dash_table, dcc
# the `dcc` (Dash Core Components) module includes a graph component called
# `dcc.Graph`, which is used to render interactive graphs
 
import plotly.express as px
# import px to build the interactive graphs
# 
# we build the custom histogram chart using px, and we give it as figure
# of the dcc.Graph component. 

import pandas as pd

# For CSV dataset
test_dataset_url = 'https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv'
df = pd.read_csv(test_dataset_url)

# ==========================================
# Building the App
# ==========================================

# Initialize the app: 
app = Dash() 
# This line is the Dash constructor, will be used to create every dash app

# App layout:
app.layout = [
    html.Div(children='My First App with Data and a Graph'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=5),
    dcc.Graph(figure=px.histogram(df, x='continent', y='pop', histfunc='sum'))] 
# page_size controls how many rows are displayed in the table at once

# ==========================================
# Run the App
# ==========================================
if __name__ == '__main__':
    app.run(debug=True)