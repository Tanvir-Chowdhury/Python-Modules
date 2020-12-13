import unittest
import calc

class Testcalc(unittest.TestCase):

    @classmethod
    def startUpClass(cls): # runs this function before all function
        pass

    @classmethod
    def tearDownClass(cls): # runs this function after all function
        pass

    def startUp(self): #runs this function before every single function
        pass

    def tearDown(self): #runs this function after every single function
        pass

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)

    def test_div(self):
        self.assertRaises(ValueError, calc.div, 10, 0)

if __name__ == "__main__":
    unittest.main()