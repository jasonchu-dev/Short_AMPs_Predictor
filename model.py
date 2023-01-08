from Pfeature.pfeature import aac_wp
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import os
import joblib

def aac(_input, _output, label):
    aac_wp(_input, _output)
    df = pd.read_csv(_output)
    df['y'] = label
    os.remove(_output)
    return df

def main():
    # training data
    po_df = aac('train_set/po_cd_hit.txt', 'po_aac.csv', 1)
    ne_df = aac('train_set/ne_cd_hit.txt', 'ne_aac.csv', 0)

    X_train = pd.concat([po_df, ne_df], axis=0)
    # shuffle data
    X_train = X_train.sample(frac=1).reset_index(drop=True)
    y_train = X_train['y']
    X_train.drop(columns='y', inplace=True)

    # test data
    test_po_df = aac('test_set/po_cd_hit.txt', 'po_cd_hit.csv', 1)
    test_ne_df = aac('test_set/ne_cd_hit.txt', 'ne_cd_hit.csv', 0)
    
    X_test = pd.concat([test_po_df, test_ne_df], axis=0)
    y_test = X_test['y']
    X_test.drop(columns='y', inplace=True)

    X_test.to_csv('static/X_test.csv', index=False)
    y_test.to_csv('static/y_test.csv', index=False)

    model = RandomForestClassifier(n_estimators=500)
    model.fit(X_train, y_train)
    
    joblib.dump(model, "./model.joblib")

if __name__ == "__main__":
    main()