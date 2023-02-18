import pandas as pd


# Prepare data
data = {'High Score': [12.1, 92, 42, 7.5, 27], 'Low Score': [
    3, 51, 42, 6, 26]}
df = pd.DataFrame(data=data)

df['Inclusive Range'] = df['High Score'] - df['Low Score'] + 1
df['Exclusive Range'] = df['High Score'] - df['Low Score']

print(df)
