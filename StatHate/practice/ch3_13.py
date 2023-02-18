import pandas as pd

df = pd.read_spss('../Salkind 7e Data Sets/Chapter 3 Data Set 4.sav')

print("Biased std: ", df.std(ddof=0))
print("Unbiased std: ", df.std(ddof=1))
print("Biased var: ", df.var(ddof=0))
print("Unbiased var: ", df.var(ddof=1))

# Biased lớn hơn vì nó có số lượng lớn hơn và là ước tính thận trọng hơn 
