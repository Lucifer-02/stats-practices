# by hand
import describe
import numpy as np
import unittest

print("By hand:")

ls1 = [58, 56, 48, 76, 69, 76, 78, 45, 66]
std1 = describe.desc_unbiased_std(ls1)
var1 = describe.desc_unbiased_var(ls1)

print("Unbiased std: ", std1)
print("Unbiased var: ", var1)

# by lib
print("By lib:")
ls2 = np.array([58, 56, 48, 76, 69, 76, 78, 45, 66])
std2 = np.std(ls2, ddof=1)
var2 = np.var(ls1, ddof=1)

# NOTE: "ddof" là option cho unbiased
print("Unbiased std: ", std2)
print("Unbiased var: ", var2)


class Test(unittest.TestCase):

    def test_std(self):
        self.assertEqual(round(std1, ndigits=2), 12.39)
        self.assertEqual(round(std2, ndigits=2), 12.39)

    def test_var(self):
        self.assertEqual(round(var1, ndigits=2), 153.53)
        self.assertEqual(round(var2, ndigits=2), 153.53)


if __name__ == '__main__':
    unittest.main()
