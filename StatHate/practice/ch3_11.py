import pandas as pd

df = pd.read_spss('../Salkind 7e Data Sets/Chapter 3 Data Set 3.sav')

print("Range:\n", df.max() - df.min())
print("Std:\n", df.std(axis=0))
print("Var:\n", df.var(axis=0))
