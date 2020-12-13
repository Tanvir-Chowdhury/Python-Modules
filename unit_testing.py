import unittest
import calc

class Testcalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)

    def test_div(self):
        self.assertRaises(ValueError, calc.div, 10, 0)

if __name__ == "__main__":
    unittest.main()