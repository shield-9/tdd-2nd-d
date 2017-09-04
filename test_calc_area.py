import unittest
from calc_area import calc_area

class Test_calcarea(unittest.TestCase):
    def test_int_value(self):
        self.assertEqual(calc_area(10), 314)

    def test_float_value(self):
        self.assertEqual(calc_area(1.5), 7)

    def test_round(self):
        self.assertEqual(calc_area(3.1158388163), 31) # near 30.5

    def test_zero_value_int(self):
        self.assertEqual(calc_area(0), 0)

    def test_zero_value_float(self):
        self.assertEqual(calc_area(0.0), 0)

    def test_big_int_value(self):
        self.assertEqual(calc_area(9999), 314096437)

    def test_big_float_value(self):
        self.assertEqual(calc_area(9999.999), 314159203)

    def test_type_int(self):
        self.assertTrue(type(calc_area(10)) == int)

    def test_type_float(self):
        self.assertTrue(type(calc_area(10.0)) == int)

