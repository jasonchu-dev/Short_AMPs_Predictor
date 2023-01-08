from Pfeature.pfeature import aac_wp
from sklearn.feature_selection import VarianceThreshold
import pandas as pd
import os
import joblib

def aac(_input):
    aac_wp(_input, 'aac_data.csv')
    df = pd.read_csv('aac_data.csv')
    os.remove('aac_data.csv')
    return df

def predict(args):
    model = joblib.load("static/model.joblib")
    df = aac(args.file)
    
    # all thresholds for aac will ussually be way greater than 0.1
    threshold = VarianceThreshold(threshold=0.1)
    threshold.fit_transform(df)

    df2 = df.loc[:, threshold.get_support()]
    
    pred = model.predict(df)
    
    # need to find better way to map
    model_results = ['ne' if i == 0 else 'po' for i in pred]
    results_df = pd.DataFrame(model_results, columns=['results'])
    
    results_df.to_csv('static/results.csv', index=False)

    final_df = pd.DataFrame(data={'Features': df2.columns, 'Gini' : model.feature_importances_})
    final_df.sort_values(by='Gini', ascending=False, inplace=True)
    final_df.reset_index(drop=True, inplace=True)
    
    final_df.to_csv('static/features.csv', index=False)