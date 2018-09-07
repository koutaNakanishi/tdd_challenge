import unittest
import sys
from calc import Calc
import io
class TestCalc(unittest.TestCase):

    def test_io(self):
        calc = Calc()
        test_case= "12,13\n11,11\n"
        input=io.StringIO(test_case)
        self.assertEqual(calc.input_to_data(input),[[12,13],[11,11]])

        test_case= "12,13,11\n130\n"
        input=io.StringIO(test_case)
        self.assertEqual(calc.input_to_data(input),[[12,13,11],[130]])


                #output.write("HELLO")

                #sys.stdout.write(z+"AAA")

                #self.assertEqual(calc.calc_price(,24)


                #self.assertEqual(calc.calc_price([40, 16]),62)
                #self.assertEqual(calc.calc_price([100, 45]),160)
                #self.assertEqual(calc.calc_price([50, 50, 55]), 171)
                #self.assertEqual(calc.calc_price([]), 0)
                #self.assertEqual(calc.calc_price([11, 12, 13]),40)
