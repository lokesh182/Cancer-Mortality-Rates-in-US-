import pandas as pd 
class DataIngest:
    
    def  __init__(self) -> None:
        self.data_path = None
        
    def get_data(self,data_path):
        """Method to read the data from the given path

        Args:
            data_path (string): path to data file

        Returns:
            dataframe: pandas data frame
        """
        self.data_path = data_path
        df = pd.read_csv(self.data_path)
        return df.head(5)
    