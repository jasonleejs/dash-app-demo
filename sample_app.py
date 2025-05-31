from dash import Dash, html
import dash_bootstrap_components as dbc
from dash import dcc
import plotly.express as px

df = px.data.gapminder()

def make_chart(fig):
    return dbc.Col(dcc.Graph(figure=fig), width=4)  # 3 per row (4+4+4 = 12)

# Generate 12 charts
charts = [
    make_chart(px.histogram(df, x="continent")),
    make_chart(px.bar(df[df.year == 2007], x="continent", y="pop")),
    make_chart(px.scatter(df[df.year == 2007], x="gdpPercap", y="lifeExp")),
    make_chart(px.line(df[df.country == "Canada"], x="year", y="lifeExp")),
    make_chart(px.scatter(df[df.country == "Germany"], x="year", y="gdpPercap")),
    make_chart(px.histogram(df[df.year == 2007], x="lifeExp")),
    make_chart(px.scatter(df[df.year == 2007], x="gdpPercap", y="pop")),
    make_chart(px.bar(df[df.year == 2007], x="continent", y="lifeExp")),
    make_chart(px.line(df[df.country == "Japan"], x="year", y="lifeExp")),
    make_chart(px.histogram(df[df.year == 2007], x="gdpPercap")),
    make_chart(px.scatter(df[df.year == 2007], x="lifeExp", y="pop")),
    make_chart(px.line(df[df.country == "India"], x="year", y="gdpPercap"))
]

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([html.H2("Dashboard of 12 Visualizations")], className="my-3"),
    *[dbc.Row(charts[i:i+3], className="mb-4") for i in range(0, 12, 3)]
], fluid=True)

if __name__ == '__main__':
    app.run(debug=True)
