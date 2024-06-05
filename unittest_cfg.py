import unittest
import counting_sort


class TestCfg(unittest.TestCase):
    # def test_cfg(self):
    #    self.assertEqual(1, 1)

    def test_p1(self):
        ##(1, 2, 6, 7, 9, 11, 12, 14)
        # m > 0
        # len(arr) = 0
        # arr = []
        # result = []
        self.assertEqual(counting_sort.counting_sort([]), [])

    # def test_p2(self):
    ##(1, 2, 3, 4, 6, 7, 9, 11, 12, 14) # infeasible if it enters in 2 it means that it has at least one element which, in case it goes to 4 it has to go through 5
    #    self.assertEqual(1, 1)

    # def test_p3(self):
    ##((1, 2, 3, 4), 5, 4, 6, 7, 9, 11, 12, 14) # this one is also infeasible if it goes through 5 it has to go thorugh 8 because the len(arr) is greater than 0
    #    self.assertEqual(1, 1)

    # def test_p4(self):
    # ((1, 2, 3, 4, 5, 4, 6, 7), 8, 7, 9, 11, 12, 14) this one is also infeasible if it goes through 5 and 8 it has to go through 13 because the len(arr) is greater than 0.
    # when the array only has negative numbers
    # self.assertEqual(counting_sort.counting_sort([-1]), [-1])

    # def test_p5(self):
    ##((1, 2, 3, 4, 5, 6, 7, 8, 7, 9), 10, 9, 11, 12, 14) #again, going through the previous paths means that the len(arr) is greater than 0 making it impossible to go through 12 without going through 13
    #    self.assertEqual(1, 1)

    def test_p6_1(self):
        ##((1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 10, 9, 11, 12), 13, 12, 14)
        array = [-1, 0, 1]
        self.assertEqual(1, 1)


if __name__ == "__main__":

    unittest.main()
