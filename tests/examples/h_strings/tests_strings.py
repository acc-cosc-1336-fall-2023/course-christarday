import unittest

from src.examples.h_strings.strings import concat_strings, slice_strings, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_concat_strings(self):
        self.assertEqual(concat_strings("abc,", "def"), "abcdef")


    def test_slice_string(self):
        name = "Patty Lynne Smith"
        self.assertEqual(slice_strings(name), "Lynne")
        self.assertEqual(name[11:], "Smith")

    def test_slice_w_step_value(self):
        letters = "ABCDEFHIJKLMNOPQRSTUVWXYZ"
        



