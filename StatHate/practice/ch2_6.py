import pandas as pd


# Prepare data
data = {'Snack Food': ['Loaded Nachos', 'Fruit Cup', 'Spicy Wings', 'Gargantuan Overstuffed Pizza', 'Beer Chicken'], 'North Fans': [
    4, 2, 4, 3, 5], 'East Fans': [4, 1, 3, 4, 5], 'South Fans': [5, 2, 3, 4, 5], 'West Fans': [4, 1, 3, 5, 4]}
df = pd.DataFrame(data=data)

fans = ['North Fans', 'East Fans', 'South Fans', 'West Fans']

df['Mean Rating'] = df[fans].mean(axis=1)

print(df)

