import pandas as pd
import warnings
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from data_processing import data_split
warnings.filterwarnings("ignore")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm




def correlation_among_numeric_features(df,cols):
    numeric_col = df[cols]
    corr = numeric_col.corr()
    
    #get highly correlated features and also tell to which feature it is correlated
    correlated_features = set()
    for i in range(len(corr.columns)):
        for j in range(i):
            if abs(corr.iloc[i, j]) > 0.8:
                colname = corr.columns[i]
                correlated_features.add(colname)
    return correlated_features

def lr_model(x_train,y_train):
    x_train_with_intercept = sm.add_constant(x_train)
    lr = sm.OLS(y_train, x_train_with_intercept).fit()
    return lr



def identify_significant_vars(lr,p_value_threshold=0.05):
    print(lr.pvalues)
    
    print(lr.rsquared)
    
    print(lr.rsquared_adj)
    
    significant_vars = [var for var in lr.pvalues.index if lr.pvalues[var] < p_value_threshold]
    return significant_vars



if __name__ == "__main__":
    capped_data = pd.read_csv( "ols-regression-data/capped_data.csv")
    
    #remove highly correlated features
    
    correlated_features = correlation_among_numeric_features(capped_data, capped_data.columns)
    print(correlated_features)
    
    highly_corr_cols = [
        'state_ District of Columbia', 
        'MedianAgeMale', 'PctPrivateCoverageAlone'
        , 'MedianAgeFemale',
        'povertyPercent',
        'upperBound',
        'median',
        'popEst2015',
        'PctMarriedHouseholds',
        'PctPrivateCoverage',
        'lowerBound', 
        'PctEmpPrivCoverage', 
        'PctBlack', 
        'PctPublicCoverageAlone'
    ]
    cols = [col for col in capped_data.columns if col not in highly_corr_cols]
    len(cols)
    x_train, x_test, y_train, y_test = train_test_split(capped_data[cols], capped_data["TARGET_deathRate"], test_size=0.3, random_state=42)
    lr = lr_model(x_train, y_train)
    summary = lr.summary()
    print(summary)
    significant_vars = identify_significant_vars(lr)
    print(len(significant_vars))
    
    # significant_vars.remove("const")
    x_train = sm.add_constant(x_train)
    lr = lr_model(x_train[significant_vars], y_train)
    summary = lr.summary()
    print(summary)