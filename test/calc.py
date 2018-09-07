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

    def test_calc(self):
        calc = Calc()

        test_case = "\n10,12\n40,16\n100,45\n50,50,55\n\n"
        input = io.StringIO(test_case)
        output =io.StringIO()
        calc.calc_price(calc.input_to_data(input),output)

        self.assertEqual(output.getvalue(), "0\n24\n62\n160\n171\n0\n")
        sys.stdout.write(output.read())
        '''
        test_case = "40,16\n"
        input = io.StringIO(test_case)
        self.assertEqual(calc.calc_price(input), 62)

        test_case = "100,45\n"
        input = io.StringIO(test_case)
        self.assertEqual(calc.calc_price(input), 160)

        test_case = "50,50,55\n"
        input = io.StringIO(test_case)
        self.assertEqual(calc.calc_price(input), 171)

        test_case = "\n"
        input = io.StringIO(test_case)
        self.assertEqual(calc.calc_price(input), 0)
        '''

                #output.write("HELLO")

                #sys.stdout.write(z+"AAA")

                #self.assertEqual(calc.calc_price(,24)

                #self.assertEqual(calc.calc_price([40, 16]),62)
                #self.assertEqual(calc.calc_price([100, 45]),160)
                #self.assertEqual(calc.calc_price([50, 50, 55]), 171)
                #self.assertEqual(calc.calc_price([]), 0)
                #self.assertEqual(calc.calc_price([11, 12, 13]),40)
