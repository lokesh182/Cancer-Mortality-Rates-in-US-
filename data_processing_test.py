from feature_engineering import bin_to_num
from feature_engineering import one_hot_encoding,cat_to_col
from data_ingest import DataIngest
from data_processing import (
    find_constant_columns, 
    find_few,
    drop_and_fill
    )

ingest_data = DataIngest()
df = ingest_data.get_data("ols-regression-data/original/cancer_new.csv")

cons_columns = find_constant_columns(df)
print("Columns that contain single value",cons_columns)
few_col = find_few(df,10)
print("Columns with few unique values",few_col)

df1 = bin_to_num(df)
df1 = cat_to_col(df1)
df1 = one_hot_encoding(df1)
df1 = drop_and_fill(df1)
df1.to_csv("ols-regression-data/cancer_Processed.csv",index = False)
print(df.shape)




