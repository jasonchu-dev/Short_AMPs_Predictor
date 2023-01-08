import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash()

df = pd.read_csv('results.csv')

app.layout = html.Div(children=[
    html.H1('Feature Importance'),
    dcc.Graph(id='example',
        figure={
            'data': [
                {'x': df['Features'], 'y': df['Gini'], 'type': 'bar'},
                {'x': df['Features'], 'y': df['Gini'], 'type': 'line'}
            ],
            'layout': {
                'title': 'Chart'
            }
        })
])

if __name__ == '__main__':
    app.run_server(debug=True)