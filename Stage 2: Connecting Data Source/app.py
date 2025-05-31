# ==========================================
# Imports
# ==========================================

# When creating dash apps, you will always use these imports as a starting point. 
from dash import Dash, html

# Common visulization components:
from dash import dash_table

# To allow us to work with datasets:
import pandas as pd

# ==========================================
# Connecting to a Data Source
# ==========================================

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
    html.Div(children='My First App with CSV Data'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=5)] 
# page_size controls how many rows are displayed in the table at once

# ==========================================
# Run the App
# ==========================================
if __name__ == '__main__':
    app.run(debug=True)