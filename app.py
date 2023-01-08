import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import argparse
from predictor import predict

app = dash.Dash()

df = pd.read_csv('static/features.csv')

app.layout = html.Div(children=[
    html.H1(children = 'Feature Importance',
        style = {
            'font-family': 'sans-serif'
        }
    ),
    dcc.Graph(id='example',
        figure={
            'data': [
                {'x': df['Features'], 'y': df['Gini'], 'type': 'bar'},
                {'x': df['Features'], 'y': df['Gini'], 'type': 'line', 'xaxis_title': 'Features', 'yaxis_title': 'Gini'}
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
        })
])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-f", "--file", help="txt file (converted from fasta with CD-HIT")

    args = parser.parse_args()
    predict(args)
    
    app.run_server(
                    mode='inline', 
                    port = 8090, 
                    dev_tools_ui=True, 
                    debug=True,
                    dev_tools_hot_reload =True, 
                    threaded=True
                )