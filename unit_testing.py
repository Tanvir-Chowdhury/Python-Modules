import unittest
import calc
import py_logging
from unittest.mock import patch

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

    def test_monthly_schedule(self):
        self.em1 = py_logging.Employee("Tanvir", "Chowdhury")
        with patch("Employee.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success!"

            schedule = self.em1.monthly_schedule("May")

            mocked_get.assert_called_with("http://company.com/Schefar/May")
            self.assertEqual(schedule, "Success!")

if __name__ == "__main__":
    unittest.main()