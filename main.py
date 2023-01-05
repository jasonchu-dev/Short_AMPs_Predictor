from Pfeature.pfeature import aac_wp
from sklearn.feature_selection import VarianceThreshold
import pandas as pd
import os
import joblib
import argparse

def aac(_input):
    aac_wp(_input, 'aac_data.csv')
    df = pd.read_csv('aac_data.csv')
    os.remove('aac_data.csv')
    return df

def main(args):
    model = joblib.load("./model.joblib")    
    # aac_wp('test_set/po_cd_hit.txt', 'po_cd_hit.csv')
    # aac_wp('test_set/ne_cd_hit.txt', 'ne_cd_hit.csv')
    # test_po_df = pd.read_csv('po_cd_hit.csv')
    # test_ne_df = pd.read_csv('ne_cd_hit.csv')
    # y_test = [1 for i in range(test_po_df.index.stop)] + [0 for i in range(test_ne_df.index.stop)]
    # os.remove('po_cd_hit.csv')
    # os.remove('ne_cd_hit.csv')
    # X_test = pd.concat([test_po_df, test_ne_df], axis=0)
    df = aac(args.file)
    
    # all thresholds for aac will ussually be way greater than 0.1
    threshold = VarianceThreshold(threshold=0.1)
    threshold.fit_transform(df)

    df2 = df.loc[:, threshold.get_support()]

    pred = model.predict(df)

    final_df = pd.DataFrame(data={'Features': df2.columns, 'Gini' : model.feature_importances_})
    final_df.sort_values(by='Gini', ascending=False, inplace=True)
    final_df.reset_index(drop=True, inplace=True)
    
    final_df.to_csv('results.csv', index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-f", "--file", help="first txt file")

    args = parser.parse_args()
    main(args)