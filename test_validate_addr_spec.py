import unittest
from validate_addr_spec import *

class TestAddr(unittest.TestCase):
    def test_addr(self):
        self.assertEqual(validate_addr_spec('abc@example.com'), 'ok')
        self.assertEqual(validate_addr_spec('"abc"@example.com'), 'ok')
        self.assertEqual(validate_addr_spec('a..bc@exmaple.com'), 'ng')

    def test_domain_start_with_dot(self):
        self.assertEqual(validate_addr_spec('abc@.example.com'), 'ng')

    def test_domain_end_with_dot(self):
        self.assertEqual(validate_addr_spec('abc@example.com.'), 'ng')

    def test_domain_dots(self):
        self.assertEqual(validate_addr_spec('abc@example..com'), 'ng')

    def test_domain_none(self):
        self.assertEqual(validate_addr_spec('abc@'), 'ng')

    def test_domain_invalid_char(self):
        self.assertEqual(validate_addr_spec('abc@example,com'), 'ng')
        self.assertEqual(validate_addr_spec('abc@example(com'), 'ng')
        self.assertEqual(validate_addr_spec('abc@example)com'), 'ng')
        self.assertEqual(validate_addr_spec('abc@example[com'), 'ng')
        self.assertEqual(validate_addr_spec('abc@example]com'), 'ng')
        # self.assertEqual(validate_addr_spec('abc@example@com'), 'ng')
        self.assertEqual(validate_addr_spec('abc@example:com'), 'ng')
        self.assertEqual(validate_addr_spec('abc@example;com'), 'ng')
        self.assertEqual(validate_addr_spec('abc@example<com'), 'ng')
        self.assertEqual(validate_addr_spec('abc@example>com'), 'ng')

    def test_atmark_none(self):
        self.assertEqual(validate_addr_spec('abcexmaple.com'), 'ng')

    def test_dot_atom_start_with_dot(self):
        self.assertEqual(validate_addr_spec('.abc@exmaple.com'), 'ng')

    def test_dot_atom_end_with_dot(self):
        self.assertEqual(validate_addr_spec('abc.@exmaple.com'), 'ng')

    def test_dot_atom_dots(self):
        self.assertEqual(validate_addr_spec('a..bc@exmaple.com'), 'ng')

    def test_dot_atom_none(self):
        self.assertEqual(validate_addr_spec('@exmaple.com'), 'ng')

    def test_dot_atom_invalid_char(self):
        self.assertEqual(validate_addr_spec('a,bc@example.com'), 'ng')
        self.assertEqual(validate_addr_spec('a(bc@example.com'), 'ng')
        self.assertEqual(validate_addr_spec('a)bc@example.com'), 'ng')
        self.assertEqual(validate_addr_spec('a[bc@example.com'), 'ng')
        self.assertEqual(validate_addr_spec('a]bc@example.com'), 'ng')
        self.assertEqual(validate_addr_spec('a@bc@example.com'), 'ng')
        self.assertEqual(validate_addr_spec('a:bc@example.com'), 'ng')
        self.assertEqual(validate_addr_spec('a;bc@example.com'), 'ng')
        self.assertEqual(validate_addr_spec('a<bc@example.com'), 'ng')
        self.assertEqual(validate_addr_spec('a>bc@example.com'), 'ng')

    def test_quoted_start_with_double_quote(self):
        self.assertEqual(validate_addr_spec('abc"@example.com'), 'ng')

    def test_quoted_end_with_double_quote(self):
        self.assertEqual(validate_addr_spec('"abc@example.com'), 'ng')

    def test_quoted_none(self):
        self.assertEqual(validate_addr_spec('"@example.com'), 'ng')

