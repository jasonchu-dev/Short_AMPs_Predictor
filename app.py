import dash
from dash import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash()

features_df = pd.read_csv('static/features.csv')
results_df = pd.read_csv('static/results.csv')
results_df.reset_index(inplace=True)

app.layout = html.Div(children=[
    html.H1(children = 'Feature Importance',
        style = {
            'font-family': 'sans-serif'
        }
    ),
    dcc.Graph(id='example',
        figure={
            'data': [
                {'x': features_df['Features'], 'y': features_df['Gini'], 'type': 'bar'},
                {'x': features_df['Features'], 'y': features_df['Gini'], 'type': 'line', 'xaxis_title': 'Features', 'yaxis_title': 'Gini'}
            ],
            'layout':{
                'title':'Chart',
                'xaxis':{
                    'title':'Features'
                },
                'yaxis':{
                    'title':'Gini'
                }
            }
        }
    ),
    html.H1(children = 'Results',
        style = {
            'font-family': 'sans-serif'
        }
    ),
    dash_table.DataTable(
        data=results_df.to_dict('records'), 
        columns=[{"name": i, "id": i} for i in results_df.columns]
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)