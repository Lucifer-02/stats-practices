import pandas as pd


# Prepare data
data = {'Week': [1, 2, 3, 4], 'Chocolate Silk': [
    12, 14, 18, 27], 'Apple': [21, 15, 14, 12], 'Douglas County Pie': [7, 12, 21, 15]}
df = pd.DataFrame(data=data)

df['Week mean'] = df[['Chocolate Silk', 'Apple',
                      'Douglas County Pie']].mean(axis=1)


print(df)
