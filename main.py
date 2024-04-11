from data_ingest import DataIngest

df = DataIngest()
dataframe = df.get_data('ols-regression-data/original/cancer_new.csv')
print(dataframe)
