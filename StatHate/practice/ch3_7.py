# NOTE: đáp án và thư viện chuẩn sử dụng cách tính khác nhau cho ra kết quả khác nhau, cả 2 cách đều đúng

import numpy as np
from scipy import stats as st
import describe

# by hand

tests = [[50, 48, 51, 46, 49, 48, 49, 49, 50, 50], [50, 49, 51, 46,
                                                    48, 53, 49, 52, 48, 55], [49, 47, 51, 55, 55, 45, 47, 45, 46, 53]]

ranges = [describe.desc_range(test) for test in tests]
means = [describe.desc_mean(test) for test in tests]
medians = [describe.desc_median(test) for test in tests]
modes = [describe.desc_mode(test) for test in tests]
stds = [describe.desc_unbiased_std(test) for test in tests]
variances = [describe.desc_unbiased_var(test) for test in tests]

print("By hand:")
print("Ranges:", ranges)
print("Means", means)
print("Medians: ", medians)
print("Modes: ", modes)
print("Stds: ", stds)
print("Vars: ", variances)

print("Highest average score: ", describe.desc_ls_max(means))

print("-------------------------------------")
# by lib

tests2 = np.array([[50, 48, 51, 46, 49, 48, 49, 49, 50, 50], [50, 49, 51, 46,
                                                              48, 53, 49, 52, 48, 55], [49, 47, 51, 55, 55, 45, 47, 45, 46, 53]], dtype=np.float16)

ranges = np.max(tests2, axis=1) - np.min(tests2, axis=1)
means = np.mean(tests2, axis=1)
medians = np.median(tests2, axis=1)
modes = st.mode(tests2, axis=1, keepdims=False).mode
stds = np.std(tests2, axis=1)
variances = np.var(tests2, axis=1)

print("By lib:")
print("Ranges:", ranges)
print("Means", means)
print("Medians: ", medians)
print("Modes: ", modes)
print("Stds: ", stds)
print("Vars: ", variances)

print("Highest average score: ", np.max(means))
