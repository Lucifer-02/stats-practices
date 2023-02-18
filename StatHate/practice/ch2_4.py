import pandas as pd


# Prepare data
data = {'Special': ['Huge Burger', 'Baby Burger', 'Chicken Littles', 'Porker Burger',
                    'Yummy Burger', 'Coney Dog'], 'Number Sold': [20, 18, 25, 19, 17, 20], 'Cost': [2.95, 1.49, 3.50, 2.95, 1.99, 1.99]}
df = pd.DataFrame(data=data)


Special = df['Special']
Number_sold = df['Number Sold']
Cost = df['Cost']

total_specials_sold = Number_sold.sum()

# this is mode
max_sold_number = Number_sold.max()


print("Best sell food: ", max_sold_number)

print("Revenue: ", (Number_sold*Cost).sum())

