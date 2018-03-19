import unittest
from groupingDishes import *


class MyTestCase(unittest.TestCase):
    def test_1(self):
        dishes = [  ["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
                    ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
                    ["Quesadilla", "Chicken", "Cheese", "Sauce"],
                    ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

        sol = [["Cheese", "Quesadilla", "Sandwich"],
               ["Salad", "Salad", "Sandwich"],
               ["Sauce", "Pizza", "Quesadilla", "Salad"],
               ["Tomato", "Pizza", "Salad", "Sandwich"]]

        test = groupingDishes(dishes)
        self.assertTrue(test == sol, msg=test)

    def test_2(self):
        dishes =[["Pasta", "Tomato Sauce", "Onions", "Garlic"],
                 ["Chicken Curry", "Chicken", "Curry Sauce"],
                 ["Fried Rice", "Rice", "Onions", "Nuts"],
                 ["Salad", "Spinach", "Nuts"],
                 ["Sandwich", "Cheese", "Bread"],
                 ["Quesadilla", "Chicken", "Cheese"]]

        sol = [ ["Cheese","Quesadilla","Sandwich"],
                ["Chicken","Chicken Curry","Quesadilla"],
                ["Nuts","Fried Rice","Salad"],
                ["Onions","Fried Rice","Pasta"]]

        test = groupingDishes(dishes)
        self.assertTrue(test == sol, msg=test)

    def test_3(self):
        dishes = [  ["Pasta", "Tomato Sauce", "Onions", "Garlic"],
                    ["Chicken Curry", "Chicken", "Curry Sauce"],
                    ["Fried Rice", "Rice", "Onion", "Nuts"],
                    ["Salad", "Spinach", "Nut"],
                    ["Sandwich", "Cheese", "Bread"],
                    ["Quesadilla", "Chickens", "Cheeseeee"]]
        sol = []
        test = groupingDishes(dishes)
        self.assertTrue(test == sol, msg=test)

    def test_4(self):
        dishes = [["First", "a", "b", "c", "d", "e", "f", "g", "h", "i"],
                 ["Second", "i", "h", "g", "f", "e", "x", "c", "b", "a"]]

        sol = [ ["a","First","Second"],
                ["b","First","Second"],
                ["c","First","Second"],
                ["e","First","Second"],
                ["f","First","Second"],
                ["g","First","Second"],
                ["h","First","Second"],
                ["i","First","Second"]]

        test = groupingDishes(dishes)
        self.assertTrue(test == sol, msg=test)


if __name__ == '__main__':
    unittest.main()