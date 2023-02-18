import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_spss('../Salkind 7e Data Sets/Chapter 4 Data Set 1.sav')


# print frequency distribution with class interval of 10 and start at 0 and end at 100
print(pd.cut(df['Comprehension_Score'], bins=range(
    0, 60, 4)).value_counts(sort=False))


# plot histogram
df['Comprehension_Score'].plot.hist(bins=range(0, 60, 4))
plt.show()
