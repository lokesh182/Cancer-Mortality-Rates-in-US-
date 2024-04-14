import numpy as np


    
def find_constant_columns(dataframe):
        """Find columns with constant values

        Args:
            dataframe (pandas.DataFrame): Input database
            
        Returns:
        list:A list of columns with constant values
        """
        constant_columns = [] # Initialize an empty list to store constant columns
        for column in dataframe.columns:# Iterate over all columns in the dataframe
            unique_value = dataframe[column].unique()# Get unique values in the column
            # If the column has only one unique value, it is a constant column
            if len(unique_value) == 1:
                # Append the column to the list
                constant_columns.append(column)
                # Print the column name and the unique value
        return constant_columns
    

def find_few(df,threshold):
        """
        Find columns with few unique values  with threshold

        Args:
            df (pd.Dataframe): dataframe 
            
        returns:
            list: A list of columns with few unique values
        """
        col_few = []
        for col in df.columns:
            unique_count = len(df[col].unique())
            if unique_count < threshold:
                col_few.append(col)
        return col_few

def drop_duplicate(df):
    """
    Drop duplicate rows from the dataframe

    Args:
        df (pd.Dataframe): dataframe 
        
    returns:
        pd.Dataframe: A dataframe with duplicate rows removed
    """
    df = df.drop_duplicates(keeo="first")
    return df

def drop_and_fill(dataframe):
    #select columns with missing values more than 50%
    cols_to_drop = dataframe.columns[dataframe.isnull().mean() > 0.5]
    
    #drop the columns
    dataframe = dataframe.drop(cols_to_drop,axis = 1)
    
    #fill missing values with the mean of the column
    dataframe = dataframe.fillna(dataframe.mean())
    return dataframe

def data_split(X, y, test_size=0.2, random_state=None):
        """
        Split the data into training and testing sets

        Args:
            X (numpy.ndarray or pandas.DataFrame): Input features
            y (numpy.ndarray or pandas.Series): Target variable
            test_size (float): Proportion of the data to include in the test set
            random_state (int): Random seed for reproducibility

        Returns:
            tuple: A tuple containing the training and testing sets (X_train, X_test, y_train, y_test)
        """
        # Set random seed if provided
        if random_state is not None:
            np.random.seed(random_state)

        # Get the number of samples
        num_samples = len(X)

        # Calculate the number of samples in the test set
        num_test_samples = int(test_size * num_samples)

        # Generate random indices for the test set
        test_indices = np.random.choice(num_samples, num_test_samples, replace=False)

        # Create the training and testing sets
        X_train = X[np.logical_not(np.isin(np.arange(num_samples), test_indices))]
        X_test = X[test_indices]
        y_train = y[np.logical_not(np.isin(np.arange(num_samples), test_indices))]
        y_test = y[test_indices]

        return X_train, X_test, y_train, y_test