import unittest
from containsCloseNums import *


class MyTestCase(unittest.TestCase):
    def test_3_or_less(self):
        nums = [0, 1, 2, 3, 5, 2]
        k = 3
        test = containsCloseNums(nums, k)

        self.assertTrue(test)

    def test_2_or_less(self):
        nums = [0, 1, 2, 3, 5, 2]
        k = 2
        test = containsCloseNums(nums, k)

        self.assertFalse(test)

    def test_empty_list(self):
        nums = []
        k = 0
        test = containsCloseNums(nums, k)

        self.assertFalse(test)

    def test_list_and_int_same_length(self):
        nums = [99, 99]
        k = 2
        test = containsCloseNums(nums, k)

        self.assertTrue(test)

    def test_int_larger_then_list_length(self):
        nums = [2, 2]
        k = 3
        test = containsCloseNums(nums, k)

        self.assertTrue(test)

    def test_no_repeats(self):
        nums = [1, 2]
        k = 2
        test = containsCloseNums(nums, k)

        self.assertFalse(test)

    def test_7(self):
        nums = [1, 2, 1]
        k = 2
        test = containsCloseNums(nums, k)

        self.assertTrue(test)

    def test_int_is_1(self):
        nums = [1, 0, 1, 1]
        k = 1
        test = containsCloseNums(nums, k)

        self.assertTrue(test)


if __name__ == '__main__':
    unittest.main()
