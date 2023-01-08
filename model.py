from Pfeature.pfeature import aac_wp
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import VarianceThreshold
import pandas as pd
import os
import joblib

def aac_preprocess(_input, _output, label):
    aac_wp(_input, _output)
    df = pd.read_csv(_output)
    df['y'] = label
    os.remove(_output)
    return df

def aac_features(_input):
    aac_wp(_input, 'aac_data.csv')
    df = pd.read_csv('aac_data.csv')
    os.remove('aac_data.csv')
    return df

def features():
    model = joblib.load("static/model.joblib")
    
    # any txt file to extract all amino acids
    df = aac_features('test_set/ne_cd_hit.txt')
    
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

def main():
    # training data
    po_df = aac_preprocess('train_set/po_cd_hit.txt', 'po_aac.csv', 1)
    ne_df = aac_preprocess('train_set/ne_cd_hit.txt', 'ne_aac.csv', 0)

    X_train = pd.concat([po_df, ne_df], axis=0)
    # shuffle data
    X_train = X_train.sample(frac=1).reset_index(drop=True)
    y_train = X_train['y']
    X_train.drop(columns='y', inplace=True)

    # test data
    test_po_df = aac_preprocess('test_set/po_cd_hit.txt', 'po_cd_hit.csv', 1)
    test_ne_df = aac_preprocess('test_set/ne_cd_hit.txt', 'ne_cd_hit.csv', 0)
    
    X_test = pd.concat([test_po_df, test_ne_df], axis=0)
    y_test = X_test['y']
    X_test.drop(columns='y', inplace=True)

    X_test.to_csv('static/X_test.csv', index=False)
    y_test.to_csv('static/y_test.csv', index=False)

    model = RandomForestClassifier(n_estimators=500)
    model.fit(X_train, y_train)
    
    joblib.dump(model, "static/model.joblib")
    
    features()
    
if __name__ == "__main__":
    main()