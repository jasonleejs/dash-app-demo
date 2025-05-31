# ==========================================
# Imports
# ==========================================

# When creating dash apps, you will always use these imports as a starting point. 
from dash import Dash, html

# ==========================================
# Building the App
# ==========================================

# Initialize the app: 
app = Dash() 

# App layout:
app.layout = [html.Div(children="A Very Basic Dash App")]
# app layout represents the app components that will be displayed in the web page. 
#
# In this example, the layout is provided as a list of components. 
# It could also be a single Dash component. 
# 
# Our simple layout has one Dash component: `html.Div`, which is a container for other components.
# The `Div` has a few properties, such as `children`, which we use to add text content into the page. 

# ==========================================
# Run the App
# ==========================================
if __name__ == "__main__":
    app.run(debug=True)

