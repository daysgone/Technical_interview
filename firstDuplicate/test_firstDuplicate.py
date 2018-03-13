import unittest
from firstDuplicate import firstDuplicate1


class MyTestCase(unittest.TestCase):
    def test_1(self):
        a =[2, 3, 3, 1, 5, 2]
        self.assertTrue(firstDuplicate1(a) == 3)

    def test_2(self):
        a = [2, 4, 3, 5, 1]
        self.assertTrue(firstDuplicate1(a) == -1)

    def test_4(self):
        a = [2, 2]
        self.assertTrue(firstDuplicate1(a) == 2)

    def test_8(self):
        a = [3, 3, 3]
        self.assertTrue(firstDuplicate1(a) == 3)


if __name__ == '__main__':
    unittest.main()
