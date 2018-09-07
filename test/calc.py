import unittest
from calc import Calc

class TestCalc(unittest.TestCase):
    def test_Calc(self):
        calc = Calc()
        self.assertEqual(calc.calc_price([10, 12]),24)
        self.assertEqual(calc.calc_price([40, 16]),62)
        self.assertEqual(calc.calc_price([100, 45]),160)
        self.assertEqual(calc.calc_price([50, 50, 55]), 171)
        self.assertEqual(calc.calc_price([]), 0)
        self.assertEqual(calc.calc_price([11, 12, 13]),40)
