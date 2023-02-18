import pandas as pd 

path = "../salkind_5e_data_sets_0/Chapter 3_Data Set 1.xlsx"
df = pd.read_excel(path, index_col=None)


# by hand
import ch2_1
score1 = df['Score 1'].values.tolist()
score2 = df['Score 2'].values.tolist()
score3 = df['Score 3'].values.tolist()

print("by hand:")
print("Mean:")
print("Score 1: ", ch2_1.mean(score1))
print("Score 2: ", ch2_1.mean(score2))
print("Score 3: ", ch2_1.mean(score3))

print("Median")
print("Score 1: ",ch2_1.median(score1))
print("Score 2: ",ch2_1.median(score2))
print("Score 3: ",ch2_1.median(score3))

print("Mode")
print("Score 1: ",ch2_1.mode(score1))
print("Score 2: ",ch2_1.mode(score2))
print("Score 3: ",ch2_1.mode(score3))

print("-----------------------------")

# use lib
print(df.mean())
print(df.median())
print(df.mode())
