# by hand
import unittest
import numpy as np
import describe

print("By hand:")

hand_a = [5, 7, 9, 11]
hand_b = [0.3, 0.5, 0.6, 0.9]
hand_c = [6.1, 7.3, 4.5, 3.8]
hand_d = [435, 456, 423, 546, 465]

hand_ls_scores = [hand_a, hand_b, hand_c, hand_d]

hand_inc_ranges = [describe.desc_inc_range(
    scores) for scores in hand_ls_scores]
hand_std = [describe.desc_unbiased_std(scores) for scores in hand_ls_scores]
hand_var = [describe.desc_unbiased_var(scores) for scores in hand_ls_scores]

print("Inclusive range: ", hand_inc_ranges)
print("Std: ", hand_std)
print("Var: ", hand_var)

# by lib
print("By lib:")

lib_a = np.array([5, 7, 9, 11])
lib_b = np.array([0.3, 0.5, 0.6, 0.9])
lib_c = np.array([6.1, 7.3, 4.5, 3.8])
lib_d = np.array([435, 456, 423, 546, 465])

lib_ls_scores = [hand_a, hand_b, hand_c, hand_d]

lib_inc_ranges = [(np.max(scores) - np.min(scores) + 1)
                  for scores in lib_ls_scores]
lib_std = [np.std(scores, ddof=1) for scores in lib_ls_scores]
lib_var = [np.var(scores, ddof=1) for scores in lib_ls_scores]

print("Inclusive range: ", lib_inc_ranges)
print("Std: ", lib_std)
print("Var: ", lib_var)


class Test(unittest.TestCase):

    def test_inc_ranges(self):
        self.assertEqual(list(round(rg, 2)
                         for rg in hand_inc_ranges), [7, 1.6, 4.5, 124])
        self.assertEqual(list(round(rg, 2)
                         for rg in lib_inc_ranges), [7, 1.6, 4.5, 124])

    def test_stds(self):
        self.assertEqual(list(round(std, 2)
                         for std in hand_std), [2.58, 0.25, 1.58, 48.23])
        self.assertEqual(list(round(std, 2)
                         for std in lib_std), [2.58, 0.25, 1.58, 48.23])

    def test_vars(self):
        self.assertEqual(list(round(var, 2)
                         for var in hand_var), [6.67, 0.06, 2.49, 2326.5])
        self.assertEqual(list(round(var, 2)
                         for var in lib_var), [6.67, 0.06, 2.49, 2326.5])


if __name__ == '__main__':
    unittest.main()
