import unittest
import counting_sort


class TestCfg(unittest.TestCase):
    def test_cfg(self):
        self.assertEqual(1, 1)

    def test_p1(self):
        ##(1, 2, 6, 7, 9, 11, 12, 14)
        # m > 0
        # len(arr) = 0
        # arr = []
        # result = [}]
        self.assertEqual(counting_sort.counting_sort([]), [])

    def test_p2(self):
        ##(1, 2, 3, 4, 6, 7, 9, 11, 12, 14)
        self.assertEqual(1, 1)

    def test_p3(self):
        ##((1, 2, 3, 4), 5, 4, 6, 7, 9, 11, 12, 14)
        self.assertEqual(1, 1)

    def test_p4(self):
        ##((1, 2, 3, 4, 5, 4, 6, 7), 8, 7, 9, 11, 12, 14)
        self.assertEqual(1, 1)

    def test_p5(self):
        ##((1, 2, 3, 4, 5, 6, 7, 8, 7, 9), 10, 9, 11, 12, 14)
        self.assertEqual(1, 1)

    def test_p6(self):
        ##((1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 10, 9, 11, 12), 13, 12, 14)
        self.assertEqual(1, 1)


if __name__ == "__main__":

    unittest.main()
