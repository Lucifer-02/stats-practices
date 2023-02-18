import pandas as pd 

df = pd.read_spss('../Salkind 7e Data Sets/Chapter 2 Data Set 4.sav')

group_df = df.groupby('Group').mean()

print(group_df)
