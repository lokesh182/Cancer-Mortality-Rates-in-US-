import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def bin_to_num(data):
    binnedinc = []
    for i in data['binnedInc']:
        # Remove the brackets and split the string
        i = i.strip("()[]")
        print(i)
        
        # Split the string by comma
        i = i.split(',')
        print(i)
        # Convert the string to a tuple
        i = tuple(i)
        print(i)
        
        i = tuple(map(float,i)) # Convert the string to a float(every individual element)
        print(i)
        
        i = list(i) # Convert the tuple to a list
        print(i)
        # Append the list to the binnedinc list
        binnedinc.append(i)
    
    # Convert the binnedinc list to a numpy array
    data['binnedInc'] = binnedinc
    
    data["lowerBound"] = [i[0] for i in data["binnedInc"]]
    data["upperBound"] = [i[1] for i in data["binnedInc"]]
    
    data["median"] = (data["lowerBound"] + data["upperBound"])/2
    
    data.drop("binnedInc",axis = 1,inplace = True)
    return data

def cat_to_col(df):
    
    
    df['county'] = [i.split(",")[0] for i in df["Geography"]] # Extract the county from the Geography column
    df['state'] = [i.split(",")[1] for i in df["Geography"]]# Extract the state from the Geography column
    
    # Drop the Geography column
    df.drop("Geography",axis = 1,inplace = True)
    return df
    
def one_hot_encoding(X):
    # Initialize the OneHotEncoder
    
    cat_col = X.select_dtypes(include = ['object']).columns
    print(cat_col)
    
    #one hot encode categorical columns
    O_encoder = OneHotEncoder(sparse_output=False,handle_unknown='ignore')
    
    # Fit the encoder to the categorical columns
    O_encoder1 = O_encoder.fit_transform(X[cat_col])
    
    # Get the feature names of the encoded columns
    feature_names = O_encoder.get_feature_names_out(cat_col)
    
    #convert to pd
    encoded_df = pd.DataFrame(O_encoder1,columns = feature_names)
    
    #drop the categorical columns from the original dataframe
    X = X.drop(cat_col,axis = 1)
    
    X = pd.concat([X,encoded_df],axis = 1)
    return X
    
    