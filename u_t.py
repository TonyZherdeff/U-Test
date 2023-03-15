import unittest
from main import Numbers


class NumbersTesting(unittest.TestCase):
    def setUp(self):
        self.num = Numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_sum(self):
        self.assertEqual(self.num.sum_plist(), 55)
        self.assertEqual(self.num.sum_plist(), "55")

    def test_avg(self):
        self.assertEqual(self.num.avg_plist(), 5.5)
        self.assertEqual(self.num.avg_plist(), "5.5")

    def test_max(self):
        self.assertEqual(self.num.max_plist(), 10)
        self.assertEqual(self.num.max_plist(), "10")

    def test_min(self):
        self.assertEqual(self.num.min_plist(), 1)
        self.assertEqual(self.num.min_plist(), "1")


if __name__ == '__main__':
    unittest.main()