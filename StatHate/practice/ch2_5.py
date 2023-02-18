import pandas as pd


# Prepare data
data = {'Average': ['Sales (in thousands of dollars)', 'Number of items purchsed', 'Number of visitors'], 'Store 1': [
    323.6, 3.454, 4.534], 'Store 2': [234.6, 5.645, 6.765], 'Store 3': [308.3, 4.565, 6.654]}
df = pd.DataFrame(data=data)

# ở đây không có giá trị ngoại lai cũng không đếm số lần xuất hiện nên chỉ cần dùng mean
df['New Store'] = df[['Store 1', 'Store 2', 'Store 3']].mean(axis=1)
print(df)
