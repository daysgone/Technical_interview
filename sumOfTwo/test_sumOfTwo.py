import unittest
from sumOfTwo import sumOfTwo


class MyTestCase(unittest.TestCase):
    def test_1(self):
        a = [1, 2, 3]
        b = [10, 20, 30, 40]
        v = 42
        self.assertTrue(sumOfTwo(a, b, v))

    def test_2(self):
        a = [1, 2, 3]
        b = [10, 20, 30, 40]
        v = 50
        self.assertFalse(sumOfTwo(a, b, v))

    def test_3(self):
        a = []
        b = [1, 2, 3, 4]
        v = 4
        self.assertFalse(sumOfTwo(a, b, v))

    def test_4(self):
        a = [10, 1, 5, 3, 8]
        b = [100, 6, 3, 1, 5]
        v = 4
        self.assertTrue(sumOfTwo(a, b, v))

    def test_6(self):
        a = [3, 2, 3, 7, 5, 0, 3, 0, 4, 2]
        b = [6, 8, 2, 9, 7, 10, 3, 8, 6, 0]
        v = 2
        self.assertTrue(sumOfTwo(a, b, v))

    def test_10(self):
        a = [17, 72, 18, 72, 73, 15, 83, 90, 8, 18]
        b = [100, 27, 33, 51, 2, 71, 76, 19, 16, 43]
        v = 37
        self.assertTrue(sumOfTwo(a, b, v))





if __name__ == '__main__':
    unittest.main()
