import pandas as pd
import joblib
import argparse
import os
from Pfeature.pfeature import aac_wp

def aac(_input):
    aac_wp(_input, 'aac_data.csv')
    df = pd.read_csv('aac_data.csv')
    os.remove('aac_data.csv')
    return df

def main(args):
    df = pd.read_csv('static/features.csv')
    print(df)
    
    model = joblib.load("static/model.joblib")
    
    df = aac(args.file)
    
    predictions = model.predict(df)
    
    # need to find better way to map
    model_results = ['ne' if i == 0 else 'po' for i in predictions]
    results_df = pd.DataFrame(model_results, columns=['results'])
    
    # won't print since after aac_wp
    print(results_df)
    
    results_df.to_csv('static/results.csv', index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-f", "--file", help="txt file (converted from fasta with CD-HIT")

    args = parser.parse_args()
    main(args)