import pandas as pd 
import numpy as np

df = pd.read_spss('../Salkind 7e Data Sets/Chapter 2 Data Set 3.sav')

num_of_beds = df['Number_of_Beds'].to_numpy()
infec_rate = df['Infection_Rate'].to_numpy() 

print("Number_of_Beds mean: ", np.round(num_of_beds.mean(), decimals=2, out=None))
print("Infection_Rate mean: ", np.round( infec_rate.mean(), decimals=2, out=None))
