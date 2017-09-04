import unittest
from unittest.mock import patch

from io import StringIO

from calc_area import *

class Test_calcarea(unittest.TestCase):
    def test_int_value(self):
        self.assertEqual(calc_area(10), 314)

    def test_float_value(self):
        self.assertEqual(calc_area(1.5), 7)

    def test_round(self):
        self.assertEqual(round(30.5), 31)
        self.assertEqual(round(30.499999), 30)
        self.assertEqual(round(30.500000), 31)

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

    def test_str_to_float_type(self):
        self.assertTrue(type(str_to_float('0')) == float)
        self.assertTrue(type(str_to_float('0.0')) == float)
        self.assertTrue(type(str_to_float('10')) == float)
        self.assertTrue(type(str_to_float('10.0')) == float)

    def test_str_to_float_number(self):
        self.assertEqual(str_to_float('0'), 0.0)
        self.assertEqual(str_to_float('0.0'), 0.0)
        self.assertEqual(str_to_float('10'), 10.0)
        self.assertEqual(str_to_float('10.0'), 10.0)

    def mock_print(self, _in, _out, callback):
        with patch('sys.stdin', StringIO(_in)), patch('sys.stdout', new_callable=StringIO) as mocked_out:
            callback()
            self.assertEqual(mocked_out.getvalue(), _out)
    
    def test_mock_print_single_line(self):
        self.mock_print('10\n', '314\n', main)
        self.mock_print('250\n', '196350\n', main)
        self.mock_print('100\n', '31416\n', main)
        self.mock_print('1.5\n', '7\n', main)

    def test_mock_print_multiple_lines(self):
        self.mock_print('10\n250\n100\n1.5\n', '314\n196350\n31416\n7\n', main)

    def test_mock_print_no_endl(self):
        self.mock_print('10', '314\n', main)
        self.mock_print('10\n250\n100\n1.5', '314\n196350\n31416\n7\n', main)

    def test_mock_print_crlf(self):
        self.mock_print('10\r\n', '314\n', main)
        self.mock_print('10\r\n250\r\n100\r\n1.5', '314\n196350\n31416\n7\n', main)
